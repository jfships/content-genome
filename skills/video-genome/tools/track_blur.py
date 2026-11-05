#!/usr/bin/env python3
"""Blur something off-limits that moves and grows through a shot (a house number, a plate, a name on a screen).

usage: python3 track_blur.py <clip.mp4> <out.mp4> <anchor_s> x y w h [--pad 24] [--stop <frame>] [--json track.json]

x y w h = the box around it at the anchor time, in the clip's pixels. Each frame the box is searched near its last
place at 0.9-1.12x its last size (the camera walks toward it); the template refreshes from confident matches. Below
the score floor the box keeps its last place and size (blurring a little too much beats showing it). --stop = the
last frame that still shows it. Prints the box and score every 6 frames, so every frame can be checked on a sheet.
Writes H.264 with BT.709 tags. Needs ffmpeg, numpy, opencv-python.
"""
import argparse
import json
import os
import subprocess

import cv2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("t0", type=float); ap.add_argument("box", type=int, nargs=4)
    ap.add_argument("--pad", type=int, default=24); ap.add_argument("--stop", type=int, default=10 ** 9); ap.add_argument("--json")
    a = ap.parse_args()
    cap = cv2.VideoCapture(a.src); fps = cap.get(cv2.CAP_PROP_FPS) or 30; F = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        F.append(f)
    H, W = F[0].shape[:2]; G = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY) for f in F]
    x0, y0, w0, h0 = a.box; k0 = int(round(a.t0 * fps)); box = {k0: (x0, y0, w0, h0, 1.0)}
    for rng in (range(k0 + 1, len(F)), range(k0 - 1, -1, -1)):
        x, y, w, h = x0, y0, w0, h0; tpl = G[k0][y0:y0 + h0, x0:x0 + w0]
        for k in rng:
            best = (-1, None)
            for sc in (0.9, 0.95, 1.0, 1.05, 1.12):
                tw, th = max(16, int(sc * w)), max(16, int(sc * h)); t_ = cv2.resize(tpl, (tw, th))
                sx, sy = max(0, x - 80), max(0, y - 80); win = G[k][sy:min(H, y + h + 80), sx:min(W, x + w + 80)]
                if win.shape[0] <= th or win.shape[1] <= tw:
                    continue
                r = cv2.matchTemplate(win, t_, cv2.TM_CCOEFF_NORMED); _, mv, _, ml = cv2.minMaxLoc(r)
                if mv > best[0]:
                    best = (mv, (sx + ml[0], sy + ml[1], tw, th))
            if best[0] >= 0.45:
                x, y, w, h = best[1]; tpl = G[k][y:y + h, x:x + w]
            box[k] = (x, y, w, h, round(best[0], 2))
    for k, f in enumerate(F):
        if k > a.stop:
            break
        x, y, w, h, _ = box[k]
        bx, by, ex, ey = max(0, x - a.pad), max(0, y - a.pad), min(W, x + w + a.pad), min(H, y + h + a.pad)
        if ex > bx + 4 and ey > by + 4:
            f[by:ey, bx:ex] = cv2.GaussianBlur(f[by:ey, bx:ex], (0, 0), 16)
    tmp = a.out + ".avi"; vw = cv2.VideoWriter(tmp, cv2.VideoWriter_fourcc(*"MJPG"), fps, (W, H))
    for f in F:
        vw.write(f)
    vw.release()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-i", a.src, "-map", "0:v", "-map", "1:a?", "-vf", "format=yuv420p", "-c:v", "libx264",
                    "-preset", "veryfast", "-crf", "18", "-c:a", "copy", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", a.out], check=True)
    os.remove(tmp)
    if a.json:
        json.dump([box[k] for k in range(len(F))], open(a.json, "w"))
    print(" ".join(f"{k}:{box[k][0]},{box[k][1]},{box[k][2]}x{box[k][3]}@{box[k][4]}" for k in range(0, len(F), 6)))


if __name__ == "__main__":
    main()
