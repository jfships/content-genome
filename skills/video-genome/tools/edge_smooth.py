#!/usr/bin/env python3
"""Calm a crawling cutout edge: motion-compensated smoothing of the matte's edge band only.

usage: python3 edge_smooth.py <take.mp4> <matte.mp4> <out_matte.mp4> [--top 0.5] [--frames a-b]

Each frame's edge band is averaged with its 4 neighbours (t-2..t+2, weights 1 2 3 2 1), each neighbour first moved onto
this frame with optical flow from the take, so the edge stays where the person is and only frame-to-frame flicker is
averaged out. Solid inside and empty outside are untouched; a neighbour that disagrees by more than half (a fast hand,
a flow error) is skipped. --top limits the work to the top share of the person's box (default 0.5: head, ears, hair,
shoulders; 1 = everything). Output: grey matte mp4 (white = person), same size and frame rate.
Measure before and after with cutout_flicker.py (one video: ears 41 -> 20 spots a second). Slow: ~1 s a frame at 1080p.
Needs ffmpeg, numpy, opencv-python.
"""
import argparse
import json
import subprocess

import cv2
import numpy as np

WT = {-2: 1, -1: 2, 0: 3, 1: 2, 2: 1}


def probe(p):
    s = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,avg_frame_rate",
                                   "-of", "json", p], capture_output=True, text=True).stdout)["streams"][0]
    n, d = s["avg_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(d or 1)


def load(p, w, h, sel=None):
    vf = (f"select='between(n,{sel[0]},{sel[1]})'," if sel else "") + f"scale={w}:{h},format=gray"
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vf", vf, "-fps_mode", "passthrough", "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(r, np.uint8).reshape(-1, h, w)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("take"); ap.add_argument("matte"); ap.add_argument("out")
    ap.add_argument("--top", type=float, default=0.5); ap.add_argument("--frames")
    a = ap.parse_args()
    w, h, fps = probe(a.matte)
    sel = tuple(map(int, a.frames.split("-"))) if a.frames else None
    A = load(a.matte, w, h, sel); G = load(a.take, w, h, sel); n = min(len(A), len(G))
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray", "-s", f"{w}x{h}", "-r", str(fps), "-i", "-",
                            "-vf", "format=yuv420p", "-c:v", "libx264", "-crf", "8", "-preset", "slow", a.out], stdin=subprocess.PIPE)
    for i in range(n):
        al = A[i].astype(np.float32) / 255; out = al.copy()
        ys, xs = np.where(al > 0.5)
        if len(ys) > 100:
            y0 = max(0, ys.min() - 12); y1 = min(h, int(ys.min() + (ys.max() - ys.min()) * a.top) + 12)
            x0 = max(0, xs.min() - 12); x1 = min(w, xs.max() + 12)
            ar = al[y0:y1, x0:x1]; g0 = G[i, y0:y1, x0:x1]
            band = cv2.dilate(((ar > 0.01) & (ar < 0.99)).astype(np.uint8), np.ones((5, 5), np.uint8)).astype(np.float32)
            sa = ar * WT[0]; sw = np.full(ar.shape, WT[0], np.float32)
            gy, gx = np.mgrid[0:y1 - y0, 0:x1 - x0].astype(np.float32)
            for k in (-2, -1, 1, 2):
                j = i + k
                if not 0 <= j < n:
                    continue
                fl = cv2.calcOpticalFlowFarneback(g0, G[j, y0:y1, x0:x1], None, 0.5, 3, 21, 3, 5, 1.1, 0)
                aj = cv2.remap(A[j, y0:y1, x0:x1].astype(np.float32) / 255, gx + fl[..., 0], gy + fl[..., 1], cv2.INTER_LINEAR,
                               borderMode=cv2.BORDER_REPLICATE)
                ok = (np.abs(aj - ar) < 0.5).astype(np.float32) * WT[k]
                sa += aj * ok; sw += ok
            box = np.zeros(ar.shape, np.float32); box[8:-8, 8:-8] = 1; box = cv2.GaussianBlur(box, (0, 0), 6)
            wgt = cv2.GaussianBlur(band, (0, 0), 1.5) * box
            out[y0:y1, x0:x1] = ar * (1 - wgt) + (sa / sw) * wgt
        enc.stdin.write((np.clip(out, 0, 1) * 255 + .5).astype(np.uint8).tobytes())
    enc.stdin.close(); enc.wait()
    print(f"{n} frames -> {a.out}")


if __name__ == "__main__":
    main()
