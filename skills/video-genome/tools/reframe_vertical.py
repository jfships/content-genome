#!/usr/bin/env python3
"""Reframe 16:9 footage to 9:16 by following the speaker's face (no stretching).

Usage: python3 reframe_vertical.py in.mp4 out.mp4 [--start S --end E]

Follows the speaker's head: from work/subject.json if base.py already wrote it
(--subject), otherwise by sampling ~4 frames a second with the bundled person
segmentation (talking-head/scripts/base.py: MediaPipe, fallback rembg). If
neither is available it falls back to a center crop and says so. The path is
smoothed and a full-height 9:16 window keeps the head centered horizontally. Output is scaled to 1080x1920. Use it for the
footage layer of a vertical cut; graphics and captions are then laid out over
it in the Genome's vertical layout.
"""
import argparse
import subprocess

import cv2
import numpy as np


import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "talking-head" / "scripts"))


def make_tracker():
    try:
        from base import Seg, measure
        seg = Seg()

        def head_x(frame):
            small = cv2.resize(frame, (256, 144))
            r = measure(seg(cv2.cvtColor(small, cv2.COLOR_BGR2RGB)))
            return None if r is None else r[0] * frame.shape[1]
        return head_x
    except Exception as e:  # no mediapipe / rembg installed
        print(f"person tracking unavailable ({str(e)[:60]}); using a center crop")
        return lambda frame: None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--start", type=float, default=0)
    ap.add_argument("--end", type=float, default=None)
    ap.add_argument("--subject", help="work/subject.json from base.py (per-frame head_x fractions)")
    a = ap.parse_args()

    cap = cv2.VideoCapture(a.src)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    end = a.end if a.end else n / fps
    cw = int(H * 9 / 16) // 2 * 2
    times, xs = [], []
    subj = json.load(open(a.subject)) if a.subject else None
    if isinstance(subj, dict):
        subj = subj.get("frames", subj.get("subject", []))
    head_x = None if subj else make_tracker()
    t = a.start
    while t < end:
        if subj:
            fi = min(int(t * fps), len(subj) - 1)
            row = subj[fi] if fi >= 0 else None
            fx = row[0] * W if row else None
        else:
            cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
            ok, fr = cap.read()
            if not ok:
                break
            fx = head_x(fr)
        times.append(t - a.start)
        xs.append(fx)
        t += 0.25
    known = [x for x in xs if x is not None]
    fallback = np.median(known) if known else W / 2
    xs = np.array([x if x is not None else np.nan for x in xs], dtype=float)
    # fill gaps, then smooth over ~2 s so the frame doesn't wobble
    idx = np.arange(len(xs))
    good = ~np.isnan(xs)
    xs = np.interp(idx, idx[good], xs[good]) if good.any() else np.full(len(xs), fallback)
    k = 9
    xs = np.convolve(np.pad(xs, k // 2, mode="edge"), np.ones(k) / k, mode="valid")
    lefts = np.clip(xs - cw / 2, 0, W - cw)

    # piecewise-linear crop x as an ffmpeg expression (keyframes every 1 s)
    keys = [(times[i], lefts[i]) for i in range(0, len(times), 4)] or [(0, (W - cw) / 2)]
    expr = f"{keys[-1][1]:.1f}"
    for (t0, x0), (t1, x1) in reversed(list(zip(keys, keys[1:]))):
        seg = f"{x0:.1f}+({x1:.1f}-{x0:.1f})*(t-{t0:.2f})/{max(t1 - t0, 0.01):.2f}"
        expr = f"if(lt(t,{t1:.2f}),{seg},{expr})"
    vf = f"crop={cw}:{H}:'{expr}':0,scale=1080:1920:flags=lanczos"
    cmd = ["ffmpeg", "-y", "-ss", str(a.start), "-to", str(end), "-i", a.src,
           "-vf", vf, "-c:v", "libx264", "-crf", "17", "-c:a", "aac", "-b:a", "192k", a.out]
    subprocess.run(cmd, check=True)
    print(f"head found in {int(good.sum())}/{len(good)} samples -> {a.out}")


if __name__ == "__main__":
    main()
