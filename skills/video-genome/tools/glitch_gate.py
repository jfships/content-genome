#!/usr/bin/env python3
"""The glitch and seam gate: runs on the HyperFrames composition itself, no render, and returns a pass/fail list a
builder can act on. Every draft passes it before the creator sees the live preview (shorts/build.md "Glitch gate").

usage: python3 glitch_gate.py <hf folder> --out _review/gate-<round> [--timeline work/timeline.json --root .]
         [--marks work/marks.json] [--accept _review/accepted-flags.json] [--cuts 12.4,30.1] [--pad 9]
         [--line 1500] [--target -14] [--bed <bed file>] [--flicker] [--quick]

What it checks (FIX lines carry the time, the check, what is wrong and the fix):
  composition (read from index.html)
    half-frame      a video clip that doesn't start half a frame in (data-media-start = in point + 0.5/fps): WebM's
                    millisecond frame times then repeat every 3rd frame and skip the next (a 10-a-second stutter)
    frame-grid      a clip starting off the frame grid; a composition length rounded up (renders one frame long)
    short-file      a clip whose file ends inside its window (holds its last frame or goes blank)
    sound           mix loudness off target, true peak over -1 dBTP, clipped samples, any audio (the music bed) that
                    stops before the video ends
  stills, pad frames before and after every cut (comp_stills.py; one strip per cut in <out>/strips/)
    pop             a 1-frame flash: a frame unlike both neighbours while they match each other
    black / flat    a black or flat frame
    doubled-frame   the first frame after a cut repeats (a 1-frame freeze)
    jump-cut        (take cuts only) head jumps at the same size across a take cut (the head-jump number is printed at every cut), or the
                    picture barely changes across a cut (near-identical jump cut): punch in 10-15 %, cut away, or align
    seam-speed      (take cuts at the same framing) a move changes speed at the seam (an eased move, a push stopping on the cut)
    lips            the lower lip under the bottom line on any still
  what is on screen, every frame (DOM, no screenshots)
    blink           an element on screen for 1-2 frames only
    early / late    a mark on screen before its anchor (--marks: [{"id", "at", "hold"}] in seconds), or 3+ frames late
    short-hold      a mark held shorter than its planned hold (--marks); --min-hold 1.0 also flags any text under 1 s
    hard-entrance   text or a small graphic going from hidden to fully shown in one frame with no move or fade
    nudge           an element shifting a few px for one frame, or the same picture shifting position across a cut
    text-block      a title/hook block (class hook, title, hook-text or [data-text-block]) with more than one font size
                    or line height, or line gaps that differ by more than 2 px (emphasis is color only)
  with --timeline   lip-sync drift, doubled first frames, rewinds and dropped frames per on-camera clip (frame_map.py)
  with --flicker    cutout edge flicker on every transparent .webm clip (cutout_flicker.py)
Accepted flags: known false positives go in --accept (default <video folder>/_review/accepted-flags.json) as
[{"key": "<key from the report>", "why": "<reason>"}]; they are listed, not failed. Report: <out>/gate.json + gate.txt.
Exit 1 while any FIX is left. --quick = pad 3 and no full-timeline scan (for a re-check of one change).
Needs playwright (+ chromium), opencv-python, numpy, mediapipe, ffmpeg.
"""
import argparse
import json
import math
import re
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comp_stills  # noqa: E402

FIXES = []


def fix(t, check, what, how, eid=None):
    key = f"{check}@{t:.2f}" + (f":{eid}" if eid else "")
    FIXES.append({"t": round(t, 3), "check": check, "what": what, "how": how, "id": eid, "key": key})


# ---------------------------------------------------------------- composition
def parse(index):
    html = Path(index).read_text(encoding="utf-8")
    info = comp_stills.comp_info(index)
    clips = []
    for m in re.finditer(r"<(\w+)\b([^>]*\bdata-start=\"[^\"]*\"[^>]*)>", html):
        tag, attrs = m.group(1).lower(), m.group(2)
        if "data-composition-id" in attrs:
            continue
        g = lambda k: (re.search(rf'\b{k}="([^"]*)"', attrs) or [None, None])[1]
        clips.append({"tag": tag, "id": g("id") or "", "src": g("src"), "start": float(g("data-start")),
                      "dur": float(g("data-duration") or info["duration"]), "ms": float(g("data-media-start") or 0)})
    return info, clips


def flen(p):
    import subprocess
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout
    try:
        return float(o.strip())
    except ValueError:
        return None


def static_checks(info, clips, hf, a):
    fps, D = info["fps"], info["duration"]
    n = D * fps
    if abs(n - round(n)) > 1e-6 and n - math.floor(n) < 0.01:
        fix(D, "frame-grid", f"length {D} s = {n:.4f} frames: renders {math.ceil(n)} frames, one more than {math.floor(n)}",
            f"write the length rounded down: {math.floor(math.floor(n) / fps * 1e4) / 1e4}")
    for c in clips:
        name = c["id"] or c["src"] or c["tag"]
        if c["tag"] == "video":
            frac = (c["ms"] * fps) % 1
            if abs(frac - 0.5) > 0.1:
                fix(c["start"], "half-frame", f"{name} starts its file at {c['ms']:.4f} s ({frac:.2f} of a frame in)",
                    f"data-media-start = in point + {0.5 / fps:.4f} (half a frame); cut files with cut_segment.py", name)
        if c["tag"] in ("video", "img"):          # captions and words starting mid-frame just show on the next frame
            sf = (c["start"] * fps) % 1
            if 0.01 < sf < 0.99 and c["start"] > 0:
                fix(c["start"], "frame-grid", f"{name} starts {sf:.2f} of a frame past a frame boundary",
                    "start clips on a frame (frame/fps, rounded down to 4 decimals)", name)
        if c["tag"] in ("video", "audio") and c["src"]:
            L = flen(hf / c["src"])
            if L is None:
                fix(c["start"], "short-file", f"{name}: file {c['src']} missing or unreadable", "fix the path", name)
                continue
            end_file = c["start"] + L - c["ms"]; end_slot = min(c["start"] + c["dur"], D)
            if c["tag"] == "video" and end_file < end_slot - 0.5 / fps:
                fix(end_file, "short-file", f"{name} file ends {end_slot - end_file:.2f} s before its slot ends (last frame holds or blanks)",
                    "cut the file longer (cut_segment.py --pad) or end the slot earlier", name)
            if c["tag"] == "audio" and end_file < D - 0.1 and c["dur"] >= 0.5 * D:
                fix(end_file, "sound", f"{name} stops {D - end_file:.2f} s before the video ends",
                    "loop or extend the bed to the end (level-matched joins); re-bake the mix", name)
    # sound
    import sound_check as sc
    for c in clips:
        if c["tag"] != "audio" or not c["src"] or c["dur"] < 0.5 * D:
            continue
        p = hf / c["src"]
        if not p.exists():
            continue
        I, TP = sc.loud(p)
        if abs(I - a.target) > 1:
            fix(0, "sound", f"{c['src']} at {I:.1f} LUFS, target {a.target:.0f}", f"gain by {a.target - I:+.1f} dB, limit -1 dBTP", c["id"] or None)
        if TP > -1:
            fix(0, "sound", f"{c['src']} true peak {TP:.1f} dBTP", "limit the master at -1 dBTP", c["id"] or None)
        if sc.clipped_runs(p):
            fix(0, "sound", f"{c['src']} has clipped samples", "lower gain before the limiter (sound_check.py --sources finds where)", c["id"] or None)
    if a.bed:
        L = flen(a.bed)
        if L is not None and L < D - 1.0:
            fix(L, "sound", f"music bed {L:.2f} s on a {D:.2f} s video", "loop a phrase of the bed to the end")


def cut_times(info, clips, extra):
    """Every clip boundary (frame numbers), and the subset where an on-camera video clip starts or ends (take cuts)."""
    fps, D = info["fps"], info["duration"]
    ts, vid = set(), set()
    for c in clips:
        if c["tag"] == "audio":
            continue
        for t in (c["start"], c["start"] + c["dur"]):
            if 0.5 / fps < t < D - 0.5 / fps:
                k = math.ceil(t * fps - 1e-3); ts.add(k)
                if c["tag"] == "video":
                    vid.add(k)
    for t in extra:
        k = round(t * fps); ts.add(k); vid.add(k)
    return sorted(ts), vid


# ---------------------------------------------------------------- faces
LM = None


def face(png):
    global LM
    import mediapipe as mp
    from mediapipe.tasks.python import BaseOptions, vision
    if LM is None:
        from draft_checks import MODEL, MODEL_URL
        import urllib.request
        if not MODEL.exists():
            MODEL.parent.mkdir(parents=True, exist_ok=True); urllib.request.urlretrieve(MODEL_URL, MODEL)
        LM = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=str(MODEL)), running_mode=vision.RunningMode.IMAGE, num_faces=2))
    im = cv2.imread(png); H, W = im.shape[:2]
    r = LM.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)))
    best = None
    for f in r.face_landmarks:
        sp = math.hypot((f[33].x - f[263].x) * W, (f[33].y - f[263].y) * H)
        if best is None or sp > best["sp"]:
            best = {"sp": sp, "x": f[168].x * W, "y": f[168].y * H, "lip": f[17].y * H}
    return best


# ---------------------------------------------------------------- stills around cuts
def gray(png):
    return cv2.resize(cv2.imread(png, cv2.IMREAD_GRAYSCALE), (135, 240)).astype(np.float32)


def strip(rows, c, fps, label, out):
    tiles = []
    for r in rows:
        im = cv2.resize(cv2.imread(r["png"]), (135, 240))
        cv2.putText(im, f"{r['frame'] - c:+d}", (4, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255) if r["frame"] == c else (255, 255, 255), 1)
        if r["frame"] == c:
            cv2.rectangle(im, (0, 0), (134, 239), (0, 255, 255), 2)
        tiles.append(im)
    k = sum(1 for r in rows if r["frame"] < c)
    top, bot = tiles[:k], tiles[k:]
    w = max(len(top), len(bot))
    pad = lambda row: row + [np.zeros_like(tiles[0])] * (w - len(row))
    img = np.vstack([np.hstack(pad(top)), np.hstack(pad(bot))]) if top and bot else np.hstack(tiles)
    bar = np.zeros((26, img.shape[1], 3), np.uint8)
    cv2.putText(bar, label, (6, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.imwrite(str(out), np.vstack([bar, img]), [cv2.IMWRITE_JPEG_QUALITY, 85])


def still_checks(cuts, rows, fps, scale, a, out, vid):
    by = {r["frame"]: r for r in rows}
    G, F = {}, {}
    g = lambda f: G.setdefault(f, gray(by[f]["png"]))
    fc = lambda f: F.setdefault(f, face(by[f]["png"]))
    (out / "strips").mkdir(parents=True, exist_ok=True)
    report = []
    flagged_lip = set()
    for c in cuts:
        fs = [f for f in range(c - a.pad, c + a.pad + 1) if f in by]
        if c not in by or c - 1 not in by:
            continue
        t = c / fps
        d = {f: float(np.abs(g(f) - g(f - 1)).mean()) for f in fs if f - 1 in by}
        for f in fs:
            if f - 1 in by and f + 1 in by and f in d and f + 1 in d:
                ac = float(np.abs(g(f + 1) - g(f - 1)).mean())
                if d[f] > 6 and d[f + 1] > 6 and ac < 0.5 * min(d[f], d[f + 1]):
                    fix(f / fps, "pop", f"frame {f} ({f - c:+d} from the cut at {t:.2f}) flashes for 1 frame", "find the element or clip that is on for that frame only")
            im = g(f)
            if im.std() < 4 and not (f - 1 in by and g(f - 1).std() < 4 and f + 1 in by and g(f + 1).std() < 4):
                fix(f / fps, "black" if im.mean() < 16 else "flat", f"frame {f} is {'black' if im.mean() < 16 else 'a flat color'}",
                    "something under the cut ends early: overlap the outgoing clip by 1-2 frames")
        moving = [v for k, v in d.items() if k not in (c,)]
        med = float(np.median(moving)) if moving else 0
        if c + 1 in d and d[c + 1] < 0.15 and med > 0.6:
            fix(t, "doubled-frame", f"first frame after the cut at {t:.2f} repeats", "seek one take frame earlier, frames at true time (cut_segment.py)")
        # heads: only at take cuts (a video clip starts or ends here); graphic changes over a running take are not seams
        line = f"cut {t:7.3f}" + ("" if c in vid else "  (graphics)")
        if c not in vid:
            report.append(line); strip([by[f] for f in fs], c, fps, line, out / "strips" / f"cut-{t:07.3f}.jpg")
            continue
        f0, f1 = fc(c - 1), fc(c)
        if f0 and f1:
            dx, dy = (f1["x"] - f0["x"]) / scale, (f1["y"] - f0["y"]) / scale
            jump = math.hypot(dx, dy); size = f1["sp"] / f0["sp"] - 1
            steps = []
            for f in fs:
                if f != c and f - 1 in by:
                    p, q = fc(f - 1), fc(f)
                    if p and q:
                        steps.append((f, math.hypot(q["x"] - p["x"], q["y"] - p["y"]) / scale, q["sp"] / p["sp"] - 1))
            base = float(np.median([s[1] for s in steps])) if steps else 0
            line += f"  head jump {jump:5.1f} px, size {size * 100:+.1f} %, normal motion {base:.1f} px/frame"
            sp = f0["sp"] / scale
            if abs(size) < 0.08 and max(10.0, 3 * base) < jump < 1.5 * sp:
                fix(t, "jump-cut", f"head jumps {jump:.0f} px at the same size ({size * 100:+.0f} %) at {t:.2f}",
                    f"punch in 10-15 % on the incoming shot, cut away, or shift it {-dx:+.0f},{-dy:+.0f} px to line the heads up")
            vb = [s[1] for s in steps if c - 3 <= s[0] < c]; va = [s[1] for s in steps if c < s[0] <= c + 3]
            zb = [abs(s[2]) for s in steps if c - 3 <= s[0] < c]; za = [abs(s[2]) for s in steps if c < s[0] <= c + 3]
            if vb and va:
                b_, a_ = np.mean(vb), np.mean(va)
                hi, lo = max(b_, a_), min(b_, a_)
                zh, zl = max(np.mean(zb), np.mean(za)), min(np.mean(zb), np.mean(za))
                if abs(size) < 0.08 and ((hi > 4 and lo < 0.35 * hi) or (zh > 0.015 and zl < 0.35 * zh)):   # same framing both sides
                    fix(t, "seam-speed", f"move speed jumps at the seam {t:.2f}: {b_:.1f} -> {a_:.1f} px/frame, zoom {np.mean(zb) * 100:.2f} -> {np.mean(za) * 100:.2f} %/frame",
                        "carry the move across the cut at constant speed (linear at the seam, ease only at the far ends) or start it after the cut")
        else:
            line += "  no face on both sides"
            if 1.0 < d.get(c, 0) < max(1.5 * med, 2.0):
                fix(t, "jump-cut", f"picture barely changes across the cut at {t:.2f} (diff {d[c]:.1f}, normal {med:.1f})",
                    "near-identical jump cut: punch in 10-15 %, cut away, or drop one side")
        for f in fs:
            q = fc(f)
            if q and q["lip"] / scale > a.line and f not in flagged_lip:
                flagged_lip.add(f)
                fix(f / fps, "lips", f"lower lip at y {q['lip'] / scale:.0f}, under the {a.line:.0f} line", "lift the speaker until the mouth clears the line on every frame")
        report.append(line)
        strip([by[f] for f in fs], c, fps, line, out / "strips" / f"cut-{t:07.3f}.jpg")
    return report


# ---------------------------------------------------------------- DOM timeline
def dom_checks(frames, info, a, cut_set, marks):
    fps = info["fps"]; area = info["width"] * info["height"]
    ign = re.compile(a.ignore) if a.ignore else None
    ids = sorted({k for fr in frames for k in fr["dom"]})
    N = len(frames)
    for eid in ids:
        seq = [fr["dom"].get(eid) for fr in frames]
        on = np.array([bool(s and s["on"]) for s in seq])
        if not on.any():
            continue
        any_ = next(s for s in seq if s)
        small = any_["box"][2] * any_["box"][3] < 0.5 * area
        texty = any(s and s.get("txt") for s in seq)
        ignored = bool(ign and ign.search(eid))
        d = np.diff(np.r_[0, on.astype(np.int8), 0]); starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
        for s0, e0 in zip(starts, ends):
            t0 = frames[s0]["t"]; n_on = e0 - s0
            if n_on <= 2 and not ignored and 0 < s0 and e0 < N:
                fix(t0, "blink", f"{eid} is on screen for {n_on} frame{'s' if n_on > 1 else ''}", "check its tween start/end and clip window", eid)
            if not ignored and s0 > 0 and (texty or (small and any_.get("src"))):
                cur, nxt = seq[s0], seq[s0 + 1] if s0 + 1 < N else None
                if cur and nxt and cur["o"] >= 0.9 and (frames[s0]["frame"] not in cut_set or texty):
                    moved = max(abs(p - q) for p, q in zip(cur["box"], nxt["box"]))
                    if moved < 0.5 and (nxt["o"] - cur["o"]) < 0.05:
                        fix(t0, "hard-entrance", f"{eid} appears fully in one frame with no move or fade", "give it an entrance (4-8 frame fade, scale or slide) unless the hard cut is planned", eid)
            if a.min_hold and not ignored and texty and eid not in marks and n_on / fps < a.min_hold and e0 < N:
                fix(t0, "short-hold", f"{eid} on screen {n_on / fps:.2f} s", f"hold text at least {a.min_hold:.1f} s (proof 1.1 s, overlays 2 s)", eid)
            # nudges inside the run
            for k in range(s0 + 2, e0 - 1):
                p, q, r_, b_ = seq[k - 1], seq[k], seq[k + 1], seq[k - 2]
                if not (p and q and r_ and b_):
                    continue
                st = max(abs(x - y) for x, y in zip(p["box"], q["box"]))
                before = max(abs(x - y) for x, y in zip(b_["box"], p["box"])); after = max(abs(x - y) for x, y in zip(q["box"], r_["box"]))
                if 0.5 < st <= 8 and before <= 0.05 and after <= 0.05:
                    fix(frames[k]["t"], "nudge", f"{eid} shifts {st:.1f} px in one frame while still", "find the second tween or layout change touching it", eid)
        if eid in marks:
            m = marks[eid]; first = frames[starts[0]]["t"]
            if first < m["at"] - 0.5 / fps:
                fix(first, "early", f"{eid} shows {round((m['at'] - first) * fps)} frames before its anchor at {m['at']:.2f}", "start it on the anchor's measured onset (onsets.py)", eid)
            elif first > m["at"] + 3 / fps:
                fix(first, "late", f"{eid} shows {round((first - m['at']) * fps)} frames after its anchor at {m['at']:.2f}", "start it on the anchor's measured onset", eid)
            if m.get("hold"):
                held = (ends[0] - starts[0]) / fps
                if held < m["hold"] - 0.5 / fps:
                    fix(first, "short-hold", f"{eid} holds {held:.2f} s, planned {m['hold']:.2f} s ({round((m['hold'] - held) * fps)} frames short)", "extend its clip/tween end", eid)
        # text block rule, once, at the first fully shown frame
        tb = next((s for s in seq if s and s.get("text") and s["o"] >= 0.99), None)
        if tb:
            T = tb["text"]
            if len(T["sizes"]) > 1 or len(T["line_heights"]) > 1:
                fix(frames[starts[0]]["t"], "text-block", f"{eid} mixes sizes {T['sizes']} / line heights {T['line_heights']}",
                    "one font size and one fixed line height per block; emphasis by color only", eid)
            tops = [l[0] for l in T["lines"]]
            if len(tops) > 2:
                pit = np.diff(tops)
                if pit.max() - pit.min() > 2:
                    fix(frames[starts[0]]["t"], "text-block", f"{eid} line gaps {', '.join(f'{x:.0f}' for x in pit)} px differ by more than 2 px",
                        "fixed line height in px on the block; no per-line sizes or margins", eid)
    # same picture shifting position across a cut
    for c in cut_set:
        k = next((i for i, fr in enumerate(frames) if fr["frame"] == c), None)
        if not k:
            continue
        prev, cur = frames[k - 1]["dom"], frames[k]["dom"]
        outs = {e: v for e, v in prev.items() if v.get("src") and v["on"] and not (cur.get(e) or {}).get("on")}
        ins = {e: v for e, v in cur.items() if v.get("src") and v["on"] and not (prev.get(e) or {}).get("on")}
        for e1, v1 in outs.items():
            for e2, v2 in ins.items():
                if v1["src"] == v2["src"]:
                    dd = max(abs(x - y) for x, y in zip(v1["box"], v2["box"]))
                    if 0.5 < dd <= 20:
                        fix(c / fps, "nudge", f"{v1['src']} shifts {dd:.1f} px from {e1} to {e2} at the cut", "give both the same box", e2)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hf"); ap.add_argument("--out", required=True)
    ap.add_argument("--timeline"); ap.add_argument("--root", default=".")
    ap.add_argument("--marks"); ap.add_argument("--accept"); ap.add_argument("--cuts", default="")
    ap.add_argument("--pad", type=int, default=9); ap.add_argument("--scale", type=float, default=0.375)
    ap.add_argument("--line", type=float, default=1500); ap.add_argument("--target", type=float, default=-14.0)
    ap.add_argument("--bed"); ap.add_argument("--flicker", action="store_true"); ap.add_argument("--flicker-limit", type=float, default=25)
    ap.add_argument("--min-hold", type=float, default=0.0, help="flag any text shorter than this (s); off by default, marks carry planned holds"); ap.add_argument("--ignore", default=r"^(cap|caption|sub|chunk|word)")
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args()
    if a.quick:
        a.pad = 3
    hf = Path(a.hf); index = hf / "index.html" if hf.is_dir() else hf; hf = index.parent
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    info, clips = parse(index); fps = info["fps"]
    print(f"composition {info['width']}x{info['height']} {fps:g} fps {info['duration']} s, {len(clips)} clips")

    static_checks(info, clips, hf, a)
    cuts, vid = cut_times(info, clips, [float(x) for x in a.cuts.split(",") if x.strip()])
    frames = sorted({f for c in cuts for f in range(c - a.pad, c + a.pad + 1) if 0 <= f < round(info["duration"] * fps)})
    print(f"{len(cuts)} cuts, {len(frames)} stills ...", flush=True)
    rows = comp_stills.shoot(index, frames, out / "stills", fps, a.scale)
    report = still_checks(cuts, rows, fps, a.scale, a, out, vid)

    marks = {}
    if a.marks:
        for m in json.load(open(a.marks, encoding="utf-8")):
            marks[m["id"]] = m
    if not a.quick:
        allf = list(range(0, int(math.floor(info["duration"] * fps + 1e-6))))
        print(f"on-screen scan, {len(allf)} frames ...", flush=True)
        dom = comp_stills.shoot(index, allf, out / "stills", fps, a.scale, dom=True, shots=False)
        dom_checks(dom, info, a, set(cuts), marks)
    if a.timeline:
        import frame_map
        for r in frame_map.run(index, a.timeline, a.root, fps):
            if "error" in r:
                report.append(f"frame map {r['id']}: skipped, {r['error']}"); continue
            report.append(f"frame map {r['id']}: drift {r['drift_median']:+.2f} fr, skips {r['skips']}/{r['expected_skips']}")
            for k, w, h in r["faults"]:
                fix(r["t"], k, f"{r['id']}: {w}", h, r["id"])
    if a.flicker:
        import cutout_flicker
        for c in clips:
            if c["tag"] == "video" and (c["src"] or "").lower().endswith(".webm"):
                r = cutout_flicker.measure(str(hf / c["src"]), a.flicker_limit)
                if "error" in r:
                    continue
                report.append(f"flicker {c['id'] or c['src']}: head {r['top_mid_bottom_per_s'][0]}/s")
                if r["fix"]:
                    fix(c["start"], "cutout-flicker", f"{c['id'] or c['src']}: {r['top_mid_bottom_per_s'][0]} flicker spots/s on the head edge (limit {a.flicker_limit:g})",
                        "edge_smooth.py on the matte, or a better matte for this take", c["id"] or None)

    acc_path = Path(a.accept) if a.accept else hf.parent / "_review" / "accepted-flags.json"
    accepted = json.load(open(acc_path, encoding="utf-8")) if acc_path.exists() else []
    acc = {x["key"]: x.get("why", "") for x in accepted if "key" in x}
    left = [f for f in FIXES if f["key"] not in acc]; kept = [f for f in FIXES if f["key"] in acc]
    lines = [*report, ""]
    for f in sorted(left, key=lambda f: f["t"]):
        lines.append(f"FIX  {f['t']:7.3f}  {f['check']:<14} {f['what']} -> {f['how']}   [{f['key']}]")
    if kept:
        lines.append(f"accepted ({len(kept)}): " + "; ".join(f"{f['key']} ({acc[f['key']]})" for f in kept))
    lines.append(("FAIL" if left else "PASS") + f"  {len(left)} to fix, {len(kept)} accepted, {len(cuts)} cuts checked; strips in {out / 'strips'}")
    txt = "\n".join(lines); print(txt)
    (out / "gate.txt").write_text(txt, encoding="utf-8")
    (out / "gate.json").write_text(json.dumps({"fix": left, "accepted": kept, "cuts": [c / fps for c in cuts]}, indent=1), encoding="utf-8")
    raise SystemExit(1 if left else 0)


if __name__ == "__main__":
    main()
