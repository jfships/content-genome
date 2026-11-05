#!/usr/bin/env python3
"""How much a cutout's edge flickers: frame-to-frame changes of the matte that steady motion doesn't explain.

usage: python3 cutout_flicker.py <matte.mp4 | clip.webm> [more ...] [--limit 25] [--heat out.jpg]

A grey matte (white = person) or a VP9 webm with alpha both work. Per frame, on the edge band only (6 px each side of
the 50 % line): |a[t] - (a[t-1] + a[t+1]) / 2| (zero for steady motion). Prints per file: flicker spots a second
(>= 20 px of edge flipping > 15 % in one frame: what reads as a crawling edge), the share of edge pixels flipping,
and splits it top / middle / bottom third of the person's box (ears and hair usually sit in the top third).
FIX when the top third (head, ears, hair) passes --limit spots a second; the lower thirds are printed only, since fast
hands break the steady-motion test. Calibrated on one landscape talking-head video (accepted mattes: 0-14 a second in
the top third; a clean-up pass that made the ears visibly crawl: 41; the same after edge_smooth.py: 20); treat the limit as a starting point.
Fixes: smooth the edge over time (edge_smooth.py), feed the model a crop where the face is bigger, or a better model.
Needs ffmpeg, numpy, scipy (and opencv-python for --heat).
"""
import argparse
import json
import subprocess

import numpy as np
from scipy.ndimage import binary_dilation, binary_erosion, label


def probe(p):
    o = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                   "stream=width,height,codec_name,avg_frame_rate", "-of", "json", p], capture_output=True, text=True).stdout)
    s = o["streams"][0]; n, d = s["avg_frame_rate"].split("/")
    return s["width"], s["height"], s["codec_name"], float(n) / float(d or 1)


def alpha(p, max_w=960):
    w, h, codec, fps = probe(p)
    sc = min(1.0, max_w / w); W, H = int(w * sc) // 2 * 2, int(h * sc) // 2 * 2
    webm = p.lower().endswith(".webm")
    dec = ["-c:v", "libvpx-vp9"] if webm and codec == "vp9" else []
    vf = f"scale={W}:{H}," + ("format=rgba,alphaextract,format=gray" if webm else "format=gray")
    r = subprocess.run(["ffmpeg", "-v", "error", *dec, "-i", p, "-vf", vf, "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(r, np.uint8).reshape(-1, H, W), fps, sc


def measure(p, limit=25.0, heat=None):
    A, fps, sc = alpha(p)
    n = len(A)
    if n < 3:
        return {"file": p, "error": "under 3 frames"}
    spots, hot, thirds = [], [], np.zeros(3)
    hm = np.zeros(A.shape[1:], np.float32)
    min_blob = max(6, int(20 * sc * sc))
    for i in range(1, n - 1):
        m = A[i] > 127
        if m.sum() < 100:
            continue
        band = binary_dilation(m, iterations=6) & ~binary_erosion(m, iterations=6)
        ha = np.abs(A[i].astype(np.float32) - (A[i - 1].astype(np.float32) + A[i + 1]) / 2)
        hm += ha * band
        flip = (ha > 38) & band
        hot.append(flip[band].mean() * 100)
        lab, nb = label(flip)
        if nb:
            sz = np.bincount(lab.ravel()); big = [b for b in np.where(sz >= min_blob)[0] if b > 0]
            spots.append(len(big))
            ys = np.where(m.any(1))[0]; y0, y1 = ys[0], ys[-1] + 1
            for b in big:
                cy = np.where(lab == b)[0].mean()
                thirds[min(2, int(3 * (cy - y0) / max(1, y1 - y0)))] += 1
        else:
            spots.append(0)
    k = max(1, len(spots))
    res = {"file": p, "frames": n, "spots_per_s": round(sum(spots) / k * fps, 1), "edge_flip_pct": round(float(np.mean(hot)), 2) if hot else 0,
           "top_mid_bottom_per_s": [round(float(x) / k * fps, 1) for x in thirds]}
    res["fix"] = res["top_mid_bottom_per_s"][0] > limit   # judged on the top third (head, ears, hair): hands below move too fast for the steady-motion test
    if heat:
        import cv2
        im = np.clip(hm / k * 10, 0, 255).astype(np.uint8)
        cv2.imwrite(heat, cv2.applyColorMap(im, cv2.COLORMAP_INFERNO))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+"); ap.add_argument("--limit", type=float, default=25.0); ap.add_argument("--heat")
    a = ap.parse_args(); bad = 0
    for p in a.files:
        r = measure(p, a.limit, a.heat if len(a.files) == 1 else None)
        if "error" in r:
            print(p, r["error"]); continue
        bad += r["fix"]
        print(f"{'FIX ' if r['fix'] else 'ok  '} {p}: {r['spots_per_s']} spots/s, {r['edge_flip_pct']} % edge px flipping, "
              f"top/mid/bottom {r['top_mid_bottom_per_s']} /s")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
