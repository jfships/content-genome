#!/usr/bin/env python3
"""Measured frame and sound checks on a draft or final render: the things a creator and the final reviewers kept
catching by eye. Runs on every draft next to tech_review.py (review/checks.md gate 4), not instead of it.

python3 draft_checks.py <render> --timeline work/timeline.json [--source <take.mp4>] --out <folder>
       [--overlays work/overlays.json] [--line 1450] [--top 288] [--json report.json]

Checks:
  lips      lower lip above the platform bottom rows (y 1450 at 1920 tall) on every frame a face is found
  blank     empty-panel / flat-color flashes: a flat patch that appears for 1-3 frames (or a whole flat frame)
  endings   word endings clipped: the take's sound still runs > 30 ms past a clip's source out point
  delivery  the speaker moves out of delivery (leans back, drops or turns away) in a clip's last 12 frames
  angle     an angle change ("angle" differs from the clip before) that doesn't land on a sentence boundary
  overlays  an overlay box touches the face on any frame it is up, the pop-in included (scale_from)
  linger    one sheet per beat end: the clip's last 12 frames + the next clip's first, for the eye check
            (each beat ends while the speaker is still in delivery). Sheets carry the top / bottom lines as guides.

Timeline: {"clips": [{"out_start", "out_end", "src_in", "src_out", optional "source", "tail_s", "said", "angle"}]}
in seconds (out_* on the render, src_* on the take). "tail_s" = audio deliberately kept past the picture cut.
A plain list of cut times also works (endings and angle are then skipped). --source is the take file when clips
don't name one.
Overlays: [{"id", "start", "end", "box": [x, y, w, h] at rest, in render px, optional "scale_from" (e.g. 1.6 for a
pop-in from 160 %) and "in_s" (pop-in length, default 0.3)}]. During the pop-in the box is checked at its largest.
Prints one FIX line per fault, then a summary; sheets go to --out. Exit 1 when any FIX remains.
Needs ffmpeg, numpy, opencv-python and mediapipe; the face model downloads once to ~/.cache/video-genome/.
Not measured here (eye checks): overlays out of the top rows, a person listening to the mix.
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

import cv2
import numpy as np

MODEL = Path(os.environ.get("VIDEO_GENOME_CACHE", Path.home() / ".cache" / "video-genome")) / "face_landmarker.task"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
LIPS = [0, 13, 14, 17, 37, 39, 40, 61, 78, 80, 81, 82, 84, 87, 88, 91, 95, 146, 178, 181, 185, 191, 267, 269, 270,
        291, 308, 310, 311, 312, 314, 317, 318, 321, 324, 375, 402, 405, 409, 415]
CHIN = 152
THUMB = (135, 240)      # flat-frame scan size (w, h): 15 px tiles, 9 x 16 grid
SHEET = (216, 384)      # tile size on the sheets
LINGER_N = 12
END_MS = 30
EYES, BRIDGE = (33, 263), 168   # stable points: eye corners (head size) and nose bridge (head position)
SHRINK, SHIFT = 0.05, 0.25      # head size change, or bridge move as a share of eye spacing, that reads as leaving delivery
FAULTS, NOTES = [], []


def fix(t, check, what, how):
    FAULTS.append((t, check, what, how))


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,avg_frame_rate,r_frame_rate:format=duration", "-of", "json", str(path)],
                         capture_output=True, text=True).stdout
    d = json.loads(out)
    st = d["streams"][0]
    # phone files: r_frame_rate can read 120 while the real rate is avg_frame_rate
    rate = st.get("avg_frame_rate") if st.get("avg_frame_rate") not in (None, "0/0") else st["r_frame_rate"]
    num, den = rate.split("/")
    return int(st["width"]), int(st["height"]), float(num) / float(den), float(d["format"]["duration"])


def load_timeline(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict):
        return sorted(data.get("clips", []), key=lambda c: float(c["out_start"]))
    times = sorted(float(t) for t in data)
    return [{"out_start": a, "out_end": b} for a, b in zip(times, times[1:])]


def frames(path, w, h):
    """Yield every frame of the render as RGB arrays at a scan width of at most 720."""
    sw = min(w, 720) // 2 * 2
    sh = round(h * sw / w) // 2 * 2
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-vf", f"scale={sw}:{sh}", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    size = sw * sh * 3
    while True:
        buf = p.stdout.read(size)
        if len(buf) < size:
            break
        yield np.frombuffer(buf, np.uint8).reshape(sh, sw, 3)
    p.wait()


def landmarker():
    if not MODEL.exists():
        MODEL.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(MODEL_URL, MODEL)
    import mediapipe as mp
    from mediapipe.tasks.python import BaseOptions, vision
    opts = vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path=str(MODEL)),
                                        running_mode=vision.RunningMode.VIDEO, num_faces=3)
    return mp, vision.FaceLandmarker.create_from_options(opts)


def flat_fraction(thumb):
    tiles = thumb.reshape(16, 15, 9, 15, 3).transpose(0, 2, 1, 3, 4).reshape(16, 9, 225, 3)
    return float((tiles.std(axis=2).max(axis=2) < 2.5).mean())


def runs(idx):
    """Group sorted frame numbers into [first, last] runs."""
    out = []
    for i in idx:
        if out and i == out[-1][1] + 1:
            out[-1][1] = i
        else:
            out.append([i, i])
    return out


# ---------- checks ----------

def scan(render, w, h, fps, keep):
    mp, lm = landmarker()
    lips, chins, faces, heads, flats, thumbs, kept = [], [], [], [], [], [], {}
    for i, rgb in enumerate(frames(render, w, h)):
        res = lm.detect_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(rgb)),
                                  round(i * 1000 / fps))
        lip = chin = box = head = None
        if res.face_landmarks:
            face = max(res.face_landmarks, key=lambda f: (max(p.y for p in f) - min(p.y for p in f)))
            lip, chin = max(face[k].y for k in LIPS) * 1920, face[CHIN].y * 1920  # rule scale, any render size
            xs, ys = [p.x * w for p in face], [p.y * h for p in face]
            box = (min(xs), min(ys), max(xs), max(ys))                            # render px
            e0, e1, nb = face[EYES[0]], face[EYES[1]], face[BRIDGE]
            head = (float(np.hypot((e1.x - e0.x) * w, (e1.y - e0.y) * h)), nb.x * w, nb.y * h)
        lips.append(lip)
        chins.append(chin)
        faces.append(box)
        heads.append(head)
        thumb = cv2.resize(rgb, THUMB, interpolation=cv2.INTER_AREA)
        flats.append(flat_fraction(thumb))
        thumbs.append(thumb)
        if i in keep:
            kept[i] = cv2.resize(rgb, SHEET, interpolation=cv2.INTER_AREA)
    lm.close()
    return lips, chins, faces, heads, flats, thumbs, kept


def check_lips(lips, chins, fps, line_px):
    over = [i for i, y in enumerate(lips) if y is not None and y > line_px]
    for a, b in runs(over):
        peak = max(range(a, b + 1), key=lambda i: lips[i])
        need = lips[peak] - line_px
        fix(a / fps, "lips", f"lower lip below the bottom line on frames {a}-{b} (lowest y {lips[peak]:.0f} at frame "
            f"{peak}, line {line_px:.0f})", f"lift the speaker about {need + 10:.0f} px (the smallest lift that clears "
            f"it), or change the layout")
    seen = [y for y in lips if y is not None]
    if seen:
        c = [y for y in chins if y is not None]
        NOTES.append(f"lips: face found on {len(seen)} of {len(lips)} frames · lowest lip y {max(seen):.0f} · "
                     f"lowest chin y {max(c):.0f} (chin is not a fail, for the eye)")
    else:
        NOTES.append("lips: no face found on any frame (check skipped)")
    return over


def check_blank(flats, fps, cuts):
    flagged = []
    for i, f in enumerate(flats):
        # a flash is flat on this frame but not on either side (a flat card that stays is planned)
        before, after = flats[max(0, i - 8):max(0, i - 3)], flats[i + 4:i + 9]
        sides = max(float(np.median(s)) for s in (before, after) if s) if (before or after) else f
        if f >= 0.9 or f - sides >= 0.12:
            flagged.append(i)
    for a, b in runs(flagged):
        if b - a > 3:
            continue  # a flat patch that stays is a design choice, not a flash
        near = min(cuts, key=lambda c: abs(c - a), default=None)
        where = f", {a - near:+d} frames from the cut at frame {near}" if near is not None and abs(a - near) <= 4 else ""
        fix(a / fps, "blank frame", f"flat-color flash on frames {a}-{b}{where} ({max(flats[a:b + 1]):.0%} of the "
            f"frame flat)", "fill the panel on those frames (picture starts late or ends early)")
    return [r for r in runs(flagged) if r[1] - r[0] <= 3]


def check_delivery(clips, ends, heads, fps):
    """The last LINGER_N frames of each clip: the head shrinking (lean back), moving or leaving reads as out of
    delivery. Measured on the eyes and nose bridge, so a held expression or an open mouth doesn't count."""
    for c, end in zip(clips, ends):
        a = max(round(float(c["out_start"]) * fps), end - LINGER_N)
        ref = heads[a] if a < len(heads) else None
        if not ref or c.get("hold_s"):
            continue
        for i in range(a + 1, min(end, len(heads))):
            f = heads[i]
            if f is None:
                fix(i / fps, "delivery", f"face lost at frame {i}, {end - i} frames before the cut at {c['out_end']:.2f}",
                    "cut before the speaker turns away (see the linger sheet)")
                break
            grow = abs(f[0] - ref[0]) / ref[0]
            move = float(np.hypot(f[1] - ref[1], f[2] - ref[2])) / ref[0]
            if grow > SHRINK or move > SHIFT:
                what = f"head size {grow:.0%}" if grow > SHRINK else f"head moved {move:.0%} of eye spacing"
                fix(i / fps, "delivery", f"speaker moves out of delivery at frame {i} ({what}), {end - i} frames "
                    f"before the cut at {c['out_end']:.2f}",
                    "cut at the end of the last word, before the move (a couple of frames of tail at most)")
                break


def check_angles(clips):
    for prev, c in zip(clips, clips[1:]):
        if "angle" not in c or "angle" not in prev or c["angle"] == prev["angle"]:
            continue
        said = str(prev.get("said", "")).rstrip(" \"'”’)")
        if said and said[-1] not in ".?!…":
            fix(float(c["out_start"]), "angle", f"angle change mid-sentence after '…{said[-30:]}'",
                "move the angle change to the next sentence boundary")


def check_overlays(overlays, faces, fps, w, h):
    for o in overlays:
        x, y, bw, bh = o["box"]
        s0, e0 = float(o["start"]), float(o["end"])
        scale, ins = float(o.get("scale_from", 1)), float(o.get("in_s", 0.3))
        hit = []
        for i in range(max(0, round(s0 * fps)), min(len(faces), round(e0 * fps) + 1)):
            f = faces[i]
            if f is None:
                continue
            k = max(scale, 1) if i / fps < s0 + ins else 1   # the pop-in at its largest
            cx, cy = x + bw / 2, y + bh / 2
            bx0, by0, bx1, by1 = cx - bw * k / 2, cy - bh * k / 2, cx + bw * k / 2, cy + bh * k / 2
            ov = min(bx1, f[2]) - max(bx0, f[0]), min(by1, f[3]) - max(by0, f[1])
            if ov[0] > 0 and ov[1] > 0:
                hit.append((i, ov[1]))
        for a, b in runs([i for i, _ in hit]):
            deep = max(d for i, d in hit if a <= i <= b)
            phase = "during the pop-in" if a / fps < s0 + ins else "at rest"
            fix(a / fps, "overlay", f"'{o.get('id', '?')}' touches the face on frames {a}-{b} {phase} "
                f"({deep:.0f} px deep)", "place it from the face (move it clear by that much, or start the pop-in "
                "smaller)")


def speech_end(level, hop, t0, floor_db, limit=0.4):
    """Seconds after t0 until the take's level stays under floor_db for 40 ms (limit if it never does)."""
    need = round(0.04 / hop)
    start = max(0, round(t0 / hop))
    quiet = 0
    for k in range(start, min(len(level), start + round(limit / hop))):
        quiet = quiet + 1 if level[k] < floor_db else 0
        if quiet >= need:
            return (k - need + 1) * hop - t0
    return limit


def take_level(path, hop=0.005, win=0.01, sr=16000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "1", "-ar", str(sr), "-f", "s16le",
                          "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    n, step = round(win * sr), round(hop * sr)
    frames_ = np.lib.stride_tricks.sliding_window_view(x, n)[::step]
    return 20 * np.log10(np.sqrt((frames_ ** 2).mean(axis=1)) + 1e-9), hop


def check_endings(clips, default_source):
    levels = {}
    checked = 0
    for c in clips:
        src = c.get("source") or default_source
        if src is None or "src_out" not in c:
            continue
        if src not in levels:
            lvl, hop = take_level(src)
            floor = max(float(np.percentile(lvl, 10)) + 15, -45.0)
            levels[src] = (lvl, hop, floor)
        lvl, hop, floor = levels[src]
        run_on = speech_end(lvl, hop, float(c["src_out"]), floor) - float(c.get("tail_s", 0))
        checked += 1
        if run_on * 1000 > END_MS:
            said = str(c.get("said", "")).split()
            word = f" ('{said[-1]}')" if said else ""
            longer = "at least " if run_on >= 0.4 - float(c.get("tail_s", 0)) else ""
            fix(float(c["out_end"]), "word ending", f"clip ending {c['out_end']:.2f}{word}: the take's sound runs "
                f"{longer}{run_on * 1000:.0f} ms past the cut (limit {END_MS})",
                "extend the audio out to the end of the word (fade over the extension), or move the cut")
    if checked:
        NOTES.append(f"endings: {checked} clip ends measured against the take (speech floor {floor:.0f} dB)")
    else:
        NOTES.append("endings: no src_out + source in the timeline (check skipped)")


# ---------- sheets ----------

def guides(img, h, line_px, top_px):
    s = img.shape[0] / h
    cv2.line(img, (0, round(top_px * s)), (img.shape[1], round(top_px * s)), (0, 200, 255), 1)
    cv2.line(img, (0, round(line_px * s)), (img.shape[1], round(line_px * s)), (255, 60, 60), 1)
    return img


def label(img, text):
    cv2.rectangle(img, (0, 0), (img.shape[1], 18), (0, 0, 0), -1)
    cv2.putText(img, text, (4, 13), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1, cv2.LINE_AA)
    return img


def sheet(tiles, cols, title, path):
    th, tw = tiles[0].shape[:2]
    rows = -(-len(tiles) // cols)
    out = np.full((rows * th + 30, cols * tw, 3), 24, np.uint8)
    for k, t in enumerate(tiles):
        r, c = divmod(k, cols)
        out[30 + r * th:30 + (r + 1) * th, c * tw:(c + 1) * tw] = t
    ascii_title = title.encode("ascii", "replace").decode()
    cv2.putText(out, ascii_title, (8, 21), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imwrite(str(path), cv2.cvtColor(out, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 88])


def linger_sheets(clips, ends, kept, fps, h, line_px, top_px, lips, out):
    paths = []
    for n, (c, end) in enumerate(zip(clips, ends), 1):
        tiles = []
        for i in list(range(max(0, end - LINGER_N), end)) + [end]:
            if i not in kept:
                continue
            tag = "NEXT " if i == end else ""
            low = f" lip {lips[i]:.0f}" if i < len(lips) and lips[i] is not None else ""
            tiles.append(label(guides(kept[i].copy(), h, line_px, top_px), f"{tag}f{i} {i / fps:.2f}s{low}"))
        if not tiles:
            continue
        said = " ".join(str(c.get("said", "")).split()[-6:])
        p = out / f"linger-{n:02d}.jpg"
        sheet(tiles, 7, f"Beat end {n}: {c['out_end']:.2f}s  ...{said}  (last {LINGER_N} frames + next)", p)
        paths.append(p)
    return paths


def flagged_sheet(events, thumbs, fps, title, path):
    tiles = []
    for a, b in events[:12]:
        for i in range(max(0, a - 1), min(len(thumbs), b + 2)):
            t = cv2.resize(thumbs[i], SHEET, interpolation=cv2.INTER_NEAREST)
            tiles.append(label(t, f"{'>> ' if a <= i <= b else ''}f{i} {i / fps:.2f}s"))
    if tiles:
        sheet(tiles, 6, title, path)
        return path


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("render")
    ap.add_argument("--timeline", required=True)
    ap.add_argument("--source")
    ap.add_argument("--out", required=True)
    ap.add_argument("--overlays")
    ap.add_argument("--line", type=float, default=1450, help="bottom no-go line at 1920 tall")
    ap.add_argument("--top", type=float, default=288, help="top platform rows at 1920 tall (sheet guide only)")
    ap.add_argument("--json")
    a = ap.parse_args()

    w, h, fps, dur = probe(a.render)
    line_px, top_px = a.line * h / 1920, a.top * h / 1920
    clips = load_timeline(a.timeline)
    total = round(dur * fps)
    ends = [min(total - 1, round(float(c["out_end"]) * fps)) for c in clips]
    cuts = [round(float(c["out_start"]) * fps) for c in clips[1:]]
    keep = {i for e in ends for i in range(e - LINGER_N, e + 1)}
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    lips, chins, faces, heads, flats, thumbs, kept = scan(a.render, w, h, fps, keep)
    if abs(len(lips) - total) > 1:
        NOTES.append(f"frame count {len(lips)} vs {total} expected from duration x fps (an extra frame at the end "
                     f"shows before the loop: check the last frame)")
    over = check_lips(lips, chins, fps, a.line)
    blank = check_blank(flats, fps, cuts)
    check_endings(clips, a.source)
    check_delivery(clips, ends, heads, fps)
    check_angles(clips)
    if a.overlays:
        check_overlays(json.load(open(a.overlays, encoding="utf-8")), faces, fps, w, h)
    else:
        NOTES.append("no --overlays: overlay-vs-face check skipped (eye check on the sheets)")
    sheets = linger_sheets(clips, ends, kept, fps, h, line_px, top_px, lips, out)
    extra = [flagged_sheet(blank, thumbs, fps, "Flat-color flashes (>> = flagged)", out / "blank-frames.jpg"),
             flagged_sheet(runs(over), thumbs, fps, "Lips below the bottom line (>> = flagged)", out / "lips.jpg")]
    sheets += [p for p in extra if p]

    FAULTS.sort()
    for t, c, what, how in FAULTS:
        print(f"FIX  t={t:6.2f}  {c:<12} {what}  ->  {how}")
    for n in NOTES:
        print(f"NOTE {n}")
    print(f"NOTE eye checks left: overlays out of the top {a.top:.0f} px, linger on the sheets, and a person "
          f"listening to the mix")
    print(f"{'CLEAN' if not FAULTS else str(len(FAULTS)) + ' to fix'} · {w}x{h} {fps:.0f} fps {len(lips)} frames · "
          f"{len(clips)} clips · {len(sheets)} sheets in {out}")
    if a.json:
        json.dump({"faults": [dict(t=t, check=c, what=w_, fix=h_) for t, c, w_, h_ in FAULTS], "notes": NOTES,
                   "sheets": [str(p) for p in sheets]}, open(a.json, "w", encoding="utf-8"), indent=1)
    sys.exit(1 if FAULTS else 0)


if __name__ == "__main__":
    main()
