#!/usr/bin/env python3
"""Which take frame each on-camera clip really shows, frame by frame, against where the voice is: lip-sync drift,
a doubled first frame, rewinds and dropped frames on sped-up lines. Runs on the composition's clip files, no render.

usage: python3 frame_map.py <hf folder> --timeline work/timeline.json [--root <video folder>] [--json out.json]

Timeline clips need "id", "out_start", "src_in", "source" (take path, relative to --root or absolute) and "speed"
(or src_out/out_end to work it out). A composition clip is matched to a timeline clip when its element id is the
clip id or "v_<id>", or its file name is "<id>.<ext>".
How: each clip file frame and every take frame are shrunk to 160x90 grey and matched (sub-frame by a parabola on the
best match). The frame on screen at composition time t is media time data-media-start + (t - data-start).
Per clip it prints: drift = picture minus voice in frames (+ = picture late), the take frames shown, a doubled first
frame, backward steps, and skips beyond what the speed explains. FIX when the median drift is over 0.3 frame (a naive cut measured -0.39, true-time placement -0.06),
the first frame is doubled (unless the clip starts under a planned hold), any rewind, or more dropped frames than the
speed explains (+2). Needs the clip file to keep the take's framing (cut, speed and cutout only, no crop).
Needs ffmpeg and numpy.
"""
import argparse
import json
import math
import re
import subprocess
from pathlib import Path

import numpy as np

TW, TH = 160, 90


def thumbs(path):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-vf", f"scale={TW}:{TH},format=gray", "-f", "rawvideo", "-"],
                       capture_output=True).stdout
    return np.frombuffer(r, np.uint8).reshape(-1, TH, TW).astype(np.float32)


def comp_clips(index):
    html = Path(index).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"<(video)\b[^>]*>", html):
        tag = m.group(0)
        g = lambda k: (re.search(rf'\b{k}="([^"]*)"', tag) or [None, None])[1]
        if g("data-start") is None or g("src") is None:
            continue
        out.append({"id": g("id") or "", "src": g("src"), "start": float(g("data-start")), "dur": float(g("data-duration") or 0),
                    "media_start": float(g("data-media-start") or 0)})
    return out


def match(T, w, guess, win=20):
    lo, hi = max(0, guess - win), min(len(T), guess + win + 1)
    if hi <= lo:
        lo, hi = 0, len(T)
    d = np.abs(T[lo:hi] - w).mean((1, 2)); j = int(np.argmin(d))
    jj = float(lo + j)
    if 0 < j < len(d) - 1:
        y0, y1, y2 = d[j - 1], d[j], d[j + 1]; den = y0 - 2 * y1 + y2
        if den > 1e-9:
            jj += 0.5 * (y0 - y2) / den
    return int(lo + j), jj, float(d[j])


def map_clip(media, take, start, dur, media_start, out_start, src_in, speed, fps, T=None):
    T = thumbs(take) if T is None else T
    W = thumbs(media)
    n0, n1 = math.ceil(start * fps - 1e-6), math.ceil((start + dur) * fps - 1e-6)   # composition frames inside the clip
    shown, offs, dist = [], [], []
    for f in range(max(0, n0), n1):
        t = f / fps
        k = int(math.floor((media_start + t - start) * fps + 1e-3))
        if not 0 <= k < len(W):
            continue
        vs = src_in + (t - out_start) * speed
        j, jj, dd = match(T, W[k], int(round(vs * fps)))
        shown.append(j); dist.append(dd)
        if t >= out_start - 1e-3:
            offs.append((vs - jj / fps) / speed * fps)
    js = np.array(shown); st = np.diff(js) if len(js) > 1 else np.array([])
    exp_skips = max(0.0, (speed - 1) * len(js))
    res = {"frames": len(js), "take_first": int(js[0]) if len(js) else None, "take_last": int(js[-1]) if len(js) else None,
           "drift_median": round(float(np.median(offs)), 2) if offs else None,
           "drift_min": round(float(np.min(offs)), 2) if offs else None, "drift_max": round(float(np.max(offs)), 2) if offs else None,
           "doubled_first": bool(len(js) > 1 and js[1] == js[0]), "backward": [int(i) for i in np.where(st < 0)[0]][:6],
           "skips": int((st > 1).sum()), "expected_skips": round(exp_skips, 1), "repeats": int((st == 0).sum()),
           "match_dist": round(float(np.median(dist)), 1) if dist else None}
    return res


def faults(r, fps):
    out = []
    if r["match_dist"] is not None and r["match_dist"] > 25:
        out.append(("frame-map", "clip file doesn't match its take (crop or wrong take?)", "check the timeline source; skip this clip"))
        return out
    if r["drift_median"] is not None and abs(r["drift_median"]) > 0.3:
        side = "late" if r["drift_median"] > 0 else "early"
        out.append(("lip-sync", f"picture {abs(r['drift_median']):.2f} frames {side} against the voice",
                    "place each kept take frame at its true time (shorts/build.md 'Clip timing'); rebuild the clip file"))
    if r["doubled_first"]:
        out.append(("doubled-first-frame", "the first frame shows twice (a 1-frame freeze at the cut)",
                    "seek one take frame earlier and place frames at true time, not pulled to 0"))
    if r["backward"]:
        out.append(("rewind", f"the picture steps back at clip frames {r['backward']}", "rebuild the clip file from the take"))
    if r["skips"] > r["expected_skips"] + 2:
        out.append(("dropped-frames", f"{r['skips']} skipped take frames, the speed explains {r['expected_skips']}",
                    "re-cut the clip; on a sped-up line keep speed <= 1.10x or build in-between frames"))
    return out


def run(hf, timeline, root, fps=30.0):
    hf = Path(hf); index = hf / "index.html" if hf.is_dir() else hf
    tl = json.load(open(timeline, encoding="utf-8"))
    tl = tl.get("clips", tl) if isinstance(tl, dict) else tl
    by = {c["id"]: c for c in tl if isinstance(c, dict) and "id" in c}
    cache, rows = {}, []
    for c in comp_clips(index):
        cid = c["id"][2:] if c["id"].startswith("v_") and c["id"][2:] in by else c["id"]
        if cid not in by:
            cid = Path(c["src"]).stem
        if cid not in by:
            continue
        e = by[cid]
        sp = e.get("speed") or ((e["src_out"] - e["src_in"]) / (e["out_end"] - e["out_start"]))
        src = Path(e["source"]); src = src if src.is_absolute() else Path(root) / src
        media = index.parent / c["src"]
        if not src.exists() or not media.exists():
            rows.append({"id": cid, "t": c["start"], "error": f"missing {src if not src.exists() else media}"}); continue
        T = cache.setdefault(str(src), thumbs(src))
        r = map_clip(media, src, c["start"], c["dur"], c["media_start"], e["out_start"], e["src_in"], sp, fps, T)
        r.update(id=cid, t=c["start"], speed=sp, faults=faults(r, fps)); rows.append(r)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hf"); ap.add_argument("--timeline", required=True); ap.add_argument("--root", default=".")
    ap.add_argument("--fps", type=float, default=30.0); ap.add_argument("--json")
    a = ap.parse_args()
    rows = run(a.hf, a.timeline, a.root, a.fps); bad = 0
    for r in rows:
        if "error" in r:
            print(f"{r['id']:8s} SKIPPED {r['error']}"); continue
        print(f"{r['id']:8s} x{r['speed']:.2f} drift {r['drift_median']:+.2f} fr ({r['drift_min']:+.2f}..{r['drift_max']:+.2f}) "
              f"take {r['take_first']}..{r['take_last']} skips {r['skips']}/{r['expected_skips']} repeats {r['repeats']}"
              + ("".join(f"\n   FIX {k}: {w} -> {h}" for k, w, h in r["faults"])))
        bad += bool(r["faults"])
    print("FAIL" if bad else "PASS", f"{bad} of {len(rows)} clips")
    if a.json:
        json.dump(rows, open(a.json, "w"), indent=1)
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
