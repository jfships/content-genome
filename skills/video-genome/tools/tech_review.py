#!/usr/bin/env python3
"""Technical review of a render: the measurable rows of review/checks.md gate 4 (and shorts/checks.md).

Usage:
  python3 tech_review.py out/draft-v3.mp4 --words work/words_out.json [--cuts work/shots.json]
         [--captions work/captions.json] [--beats work/beats.json] [--hold 18.2 --hold 26.0]
         [--pace 2.6-3.0] [--loudness -14] [--vertical | --wide] [--json report.json]

Inputs (all optional except the render; each missing input skips its checks and says so):
  --words     word times ON THE CUT: {"words":[{"start","end","w"}...]} (tools/remap_words.py output) or a list.
  --cuts      work/shots.json: the built video's edit points ON THE CUT'S TIMELINE, a JSON list of shot
              start times or of [start, end] pairs (NOT cutlist.json, which holds source-time spans).
  --captions  JSON list of {"start","end","text"} or captions.py phrases {"a","b","text"}, optional
              "x","y","w","h" (px at the render size).
  --beats     work/beats.json, written from the beat brief: list of {"id","start","end","layout","job",
              optional "hold": true (a planned hold), "proof": true, "still": true (a planned still frame),
              "bleed": true (a full-width band), "speaker":[x,y,w,h], "graphic":[x,y,w,h], "hook":[x,y,w,h],
              "overlap": true (the graphic is meant to sit over the speaker: words behind, a page he reads),
              "captions_off": "<why>" (no captions on this beat on purpose)}. Spoken words with no caption
              and no captions_off beat are flagged.
  --case      the brand's caption case (sentence | caps | title); flags every chunk in another case.
  --center    caption center x from the brand's caption spec; flags boxes centered more than 4 px off.
  --chunk     caption words per chunk limit (default 5 vertical, 7 wide).
  --gap       longest spoken gap in seconds (default 0.6 vertical, 1.0 wide).
  --hold      planned hold times (seconds); a freeze or a lingering beat near one is not a fault.
  --pace      the brand's spoken pace target in words a second (default 2.6-3.0).
  --loudness  master target LUFS (default -14).
  --vertical  safe box x 65-930, y 250-1450 at 1080x1920 (default when the render is taller than wide).
  --wide      96 px margin at 1920x1080.

Prints one line per fault: FIX  t=12.30  <check>  <what>  ->  <how to fix>, then a summary.
Exit code 1 when any FIX remains. Everything it can't measure (flicker, blurry text, contrast,
SFX frame) stays with the reviewing agent's eyes.
"""
import argparse
import json
import re
import subprocess
import sys

FAULTS = []
NOTES = []


def fix(t, check, what, how):
    FAULTS.append((t, check, what, how))


def note(msg):
    NOTES.append(msg)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stderr


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,avg_frame_rate,r_frame_rate:format=duration", "-of", "json", path],
                         capture_output=True, text=True).stdout
    d = json.loads(out)
    st = d["streams"][0]
    # phone files: r_frame_rate can read 120 while the real rate is avg_frame_rate
    rate = st.get("avg_frame_rate") if st.get("avg_frame_rate") not in (None, "0/0") else st["r_frame_rate"]
    num, den = rate.split("/")
    return int(st["width"]), int(st["height"]), float(num) / float(den), float(d["format"]["duration"])


def load_words(path):
    data = json.load(open(path))
    if isinstance(data, dict):
        data = data.get("words", data.get("segments", []))
    words = []
    for w in data:
        s, e = w.get("start", w.get("t0")), w.get("end", w.get("t1"))
        if s is None or e is None:
            continue
        words.append((float(s), float(e), str(w.get("w", w.get("word", w.get("text", "")))).strip()))
    return sorted(words)


def load_cuts(path, dur):
    data = json.load(open(path))
    if data and isinstance(data[0], (list, tuple)):
        return [(float(a), float(b)) for a, b in data]
    starts = sorted(float(x) for x in data)
    return [(s, starts[i + 1] if i + 1 < len(starts) else dur) for i, s in enumerate(starts)]


def near_hold(t, holds, tol=0.5):
    return any(abs(t - h) <= tol for h in holds)


def overlap(a, b):
    if not a or not b:
        return 0
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    w = min(ax + aw, bx + bw) - max(ax, bx)
    h = min(ay + ah, by + bh) - max(ay, by)
    return max(0, w) * max(0, h)


def outside(box, safe):
    if not box:
        return False
    x, y, w, h = box
    sx0, sy0, sx1, sy1 = safe
    return x < sx0 or y < sy0 or x + w > sx1 or y + h > sy1


# ---------- checks ----------

def check_cuts(words, cuts, holds):
    seen = set()
    edits = sorted({round(t, 2) for s, e in cuts for t in (s, e)})
    for t in edits:
        for ws, we, w in words:
            key = (t, ws, w)
            if key in seen:
                continue
            if ws < t < we and min(t - ws, we - t) > 0.04:
                seen.add(key)
                fix(t, "clipped word", f"'{w}' ({ws:.2f}-{we:.2f}) is cut at {t:.2f}", "move the edit to the word's edge, or keep the whole word")
            elif 0 <= ws - t < 0.04:
                seen.add(key)
                fix(t, "tight head", f"'{w}' starts {ws - t:.2f} s after the edit", "leave at least 0.04 s before the first word")
    for s, e in cuts:
        last = [we for ws, we, w in words if s <= we <= e]
        if last and e - max(last) > 0.2 and not near_hold(e, holds):
            fix(max(last), "lingering", f"shot {s:.2f}-{e:.2f} holds {e - max(last):.2f} s after its last word", "cut the moment the last word ends, or plan the hold in the beat brief (--hold)")


def check_pace(words, pace, holds, gap_limit):
    lo, hi = (float(x) for x in pace.split("-"))
    if len(words) < 2:
        return
    span = words[-1][1] - words[0][0]
    wps = len(words) / span if span else 0
    if wps < lo:
        fix(0, "pace", f"{wps:.2f} words a second, target {lo}-{hi}", f"trim gaps, then speed up by {min(12, round((lo / wps - 1) * 100))}% at most")
    elif wps > hi:
        fix(0, "pace", f"{wps:.2f} words a second, above {hi}", "slow the fastest lines or drop the speed-up")
    for (s0, e0, w0), (s1, e1, w1) in zip(words, words[1:]):
        gap = s1 - e0
        if gap > gap_limit and not near_hold(e0, holds):
            fix(e0, "gap", f"{gap:.2f} s between '{w0}' and '{w1}'", "cut the pause, or plan it as a hold")


def case_of(text):
    ws = [w for w in re.findall(r"[A-Za-z][A-Za-z']*", text)]
    if not ws:
        return None
    if len(ws) > 1 and all(w.isupper() for w in ws if len(w) > 1):
        return "caps"
    # Title Case: two or more words after the first, none starting a new sentence, all capitalized
    # (one capital word mid-chunk is a name, not a style)
    mid = [m.group(0) for m in re.finditer(r"[A-Za-z][A-Za-z']*", text)
           if m.start() > 0 and not re.search(r"[.?!]\s*$", text[:m.start()]) and len(m.group(0)) > 1]
    if len(mid) >= 2 and all(w[0].isupper() for w in mid):
        return "title"
    return "sentence"


def check_captions(caps, words, beats, safe, chunk, case=None, center=None):
    covered = []
    for c in caps:
        s, e, text = float(c.get("start", c.get("a", 0))), float(c.get("end", c.get("b", 0))), c.get("text", "")
        spoken = [w for ws, we, w in words if we > s - 0.05 and ws < e + 0.05]
        norm = lambda t: re.sub(r"[^a-z0-9' ]", "", t.lower()).split()
        if words and spoken:
            missing = [w for w in norm(text) if w not in {x for sw in spoken for x in norm(sw)}]
            if missing:
                fix(s, "caption text", f"'{text}' has words not spoken in {s:.2f}-{e:.2f}: {' '.join(missing)}", "match the caption to words_out.json")
        covered.append((s, e))
        got = case_of(text)
        if case and got and got != case and not (case == "sentence" and got == "caps" and len(text.split()) == 1):
            fix(s, "caption case", f"'{text}' reads as {got} case", f"the brand's caption spec says {case} case")
        n = max(1, len(text.split()))
        if n > chunk:
            fix(s, "caption chunk", f"'{text}' is {n} words", f"2-3 word chunks, {chunk} at most")
        if e - s < 0.25 * n:
            fix(s, "caption time", f"'{text}' on screen {e - s:.2f} s for {n} words", "hold a caption at least 0.25 s a word")
        box = [c[k] for k in ("x", "y", "w", "h")] if all(k in c for k in ("x", "y", "w", "h")) else None
        if box and outside(box, safe):
            fix(s, "caption box", f"'{text}' outside the safe box", "move it inside the safe box")
        if box and center is not None and abs(box[0] + box[2] / 2 - center) > 4:
            fix(s, "caption center", f"'{text}' centered on x {box[0] + box[2] / 2:.0f}", f"center captions on x {center:.0f} (the caption spec)")
        for b in beats:
            if box and float(b["start"]) < e and float(b["end"]) > s:
                for key in ("hook", "graphic"):
                    if overlap(box, b.get(key)) > 0:
                        fix(s, "collision", f"caption '{text}' overlaps the {key} of beat {b.get('id')}", "move the caption or the element; captions sit below the chin")
    off = [(float(b["start"]), float(b["end"])) for b in beats if b.get("captions_off")]
    bare = [(ws, w) for ws, we, w in words
            if not any(a - 0.05 <= (ws + we) / 2 <= b + 0.05 for a, b in covered + off)]
    for i, (t, w) in enumerate(bare):
        if i == 0 or t - bare[i - 1][0] > 1.0:
            run_words = [x for tt, x in bare[i:] if tt - t <= 1.5][:6]
            fix(t, "uncaptioned", f"spoken with no caption: '{' '.join(run_words)}'",
                "caption it, or give the beat \"captions_off\": \"<why>\" in beats.json")


def check_beats(beats, safe, holds, vertical):
    prev = None
    for b in beats:
        s, e = float(b["start"]), float(b["end"])
        job = str(b.get("job", "")).lower()
        if not job or "illustrat" in job:
            fix(s, "beat job", f"beat {b.get('id')} has no job ('{job}')", "name one of: straight man, unsaid line, exaggeration, proof, breather")
        if b.get("proof") and e - s < 1.1:
            fix(s, "proof time", f"beat {b.get('id')} proof on screen {e - s:.2f} s", "hold a proof at least 1.1 s, alone")
        if b.get("graphic") and e - s > 4.2 and not b.get("hold"):
            fix(s, "graphic time", f"beat {b.get('id')} graphic on screen {e - s:.2f} s", "no single graphic over about 4 s; change it or cut")
        if outside(b.get("hook"), safe):
            fix(s, "safe box", f"beat {b.get('id')} hook box {b.get('hook')} leaves the safe box {safe}", "move it inside the safe box")
        sp = b.get("speaker")
        if sp and vertical and (sp[0] + sp[2] > safe[2] + 60 or sp[1] + sp[3] > safe[3] + 120 and sp[1] > safe[1]):
            fix(s, "button zone", f"beat {b.get('id')} speaker box {sp} runs into the right rail or bottom rows", "move the speaker left or up; the face stays inside x 65-930, y 250-1450")
        g = b.get("graphic")
        if g and (g[1] < safe[1] or g[1] + g[3] > safe[3]) and not b.get("bleed"):
            fix(s, "safe box", f"beat {b.get('id')} graphic box {g} runs into the top or bottom platform rows", "keep the graphic between y {safe[1]} and {safe[3]} (a full-bleed band may mark bleed: true)".replace("{safe[1]}", str(safe[1])).replace("{safe[3]}", str(safe[3])))
        if overlap(b.get("speaker"), b.get("graphic")) > 0 and not b.get("overlap") and b.get("layout", "").lower() in ("split top", "side panel", "speaker third + graphic", "split", "shoulder panel", "full graphic"):
            fix(s, "overlap", f"beat {b.get('id')} speaker and graphic boxes overlap in layout '{b.get('layout')}'", "separate the boxes, or use Words behind / Over their page on purpose")
        if prev and prev.get("layout") and prev.get("layout") == b.get("layout") and not (b.get("hold") or near_hold(s, holds)):
            fix(s, "layout repeat", f"beats {prev.get('id')} and {b.get('id')} both use '{b.get('layout')}'", "rotate the layout, unless the hold is the joke (mark hold)")
        prev = b


def check_freezes(path, holds, beats):
    err = run(["ffmpeg", "-v", "info", "-i", path, "-vf", "freezedetect=n=0.003:d=0.4", "-an", "-f", "null", "-"])
    planned = set(holds) | {float(b["start"]) for b in beats if b.get("hold")}
    stills = [(float(b["start"]), float(b["end"])) for b in beats if b.get("hold") or b.get("proof") or b.get("still")]
    for m in re.finditer(r"freeze_start: ([\d.]+)", err):
        t = float(m.group(1))
        if any(s0 - 0.1 <= t <= e0 for s0, e0 in stills):
            continue
        if not any(abs(t - h) <= 0.6 for h in planned):
            fix(t, "freeze", "picture frozen 0.4 s or more with no planned hold", "a clip shorter than its slot holds its last frame: extend the clip, or plan the hold")
    err = run(["ffmpeg", "-v", "info", "-i", path, "-vf", "blackdetect=d=0.08:pix_th=0.05", "-an", "-f", "null", "-"])
    for m in re.finditer(r"black_start:([\d.]+)", err):
        fix(float(m.group(1)), "black frames", "black for 0.08 s or more", "fill the gap in the composition")


def check_sound(path, target):
    err = run(["ffmpeg", "-v", "info", "-i", path, "-af", "ebur128=peak=true", "-vn", "-f", "null", "-"])
    ms = re.findall(r"I:\s+(-?[\d.]+) LUFS", err)
    if ms:
        i = float(ms[-1])
        if abs(i - target) > 1.5:
            fix(0, "loudness", f"master {i:.1f} LUFS, target {target}", "run tools/mix.py to the target")
    else:
        note("no audio stream: loudness not checked")
        return
    pk = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", err)
    if pk and float(pk[-1]) > -1.0:
        fix(0, "peak", f"true peak {pk[-1]} dBFS", "limit to -1 dBTP")
    err = run(["ffmpeg", "-v", "info", "-i", path, "-af", "silencedetect=n=-40dB:d=0.7", "-vn", "-f", "null", "-"])
    for m in re.finditer(r"silence_start: ([\d.]+)", err):
        fix(float(m.group(1)), "silence", "0.7 s or more under -40 dB", "music bed or room tone under the gap, or cut it")


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("render")
    ap.add_argument("--words")
    ap.add_argument("--cuts")
    ap.add_argument("--captions")
    ap.add_argument("--beats")
    ap.add_argument("--hold", type=float, action="append", default=[])
    ap.add_argument("--pace", default="2.6-3.0")
    ap.add_argument("--loudness", type=float, default=-14.0)
    ap.add_argument("--vertical", action="store_true")
    ap.add_argument("--wide", action="store_true")
    ap.add_argument("--chunk", type=int)
    ap.add_argument("--gap", type=float)
    ap.add_argument("--case", choices=["sentence", "caps", "title"], help="the brand's caption case")
    ap.add_argument("--center", type=float, help="caption center x from the brand's caption spec (needs caption boxes)")
    ap.add_argument("--json")
    a = ap.parse_args()

    w, h, fps, dur = probe(a.render)
    vertical = a.vertical or (h > w and not a.wide)
    safe = (65, 250, 930, 1450) if vertical else (96, 96, w - 96, h - 96)
    if vertical and (w, h) != (1080, 1920):
        note(f"render is {w}x{h}; safe box assumes 1080x1920 (scale boxes accordingly)")
    if fps < 23:
        fix(0, "frame rate", f"{fps:.1f} fps", "deliver at the footage's rate (24-30 fps); drafts may be lower on purpose")

    chunk = a.chunk or (5 if vertical else 7)
    gap_limit = a.gap or (0.6 if vertical else 1.0)
    words = load_words(a.words) if a.words else []
    beats = json.load(open(a.beats)) if a.beats else []
    holds = list(a.hold) + [float(b["start"]) for b in beats if b.get("hold")]
    if a.words:
        check_pace(words, a.pace, holds, gap_limit)
        if a.cuts:
            check_cuts(words, load_cuts(a.cuts, dur), holds)
        else:
            note("no --cuts: clipped-word and lingering checks skipped")
    else:
        note("no --words: pace, gaps, clipped-word and caption-text checks skipped")
    if a.captions:
        check_captions(json.load(open(a.captions)), words, beats, safe, chunk, a.case, a.center)
    else:
        note("no --captions: caption checks skipped")
    if beats:
        check_beats(beats, safe, holds, vertical)
        last = max(float(b["end"]) for b in beats)
        if abs(last - dur) > 0.5:
            note(f"beat brief ends at {last:.2f} s, render is {dur:.2f} s")
    else:
        note("no --beats: job, box, layout-rotation and duration checks skipped")
    check_freezes(a.render, holds, beats)
    check_sound(a.render, a.loudness)

    FAULTS.sort()
    for t, c, what, how in FAULTS:
        print(f"FIX  t={t:6.2f}  {c:<14} {what}  ->  {how}")
    for n in NOTES:
        print(f"NOTE {n}")
    print(f"{'CLEAN' if not FAULTS else str(len(FAULTS)) + ' to fix'} · {w}x{h} {fps:.0f} fps {dur:.1f} s · "
          f"{len(words)} words · {len(beats)} beats · planned holds {len(holds)}")
    if a.json:
        json.dump({"faults": [dict(t=t, check=c, what=w_, fix=h_) for t, c, w_, h_ in FAULTS], "notes": NOTES},
                  open(a.json, "w"), indent=1)
    sys.exit(1 if FAULTS else 0)


if __name__ == "__main__":
    main()
