#!/usr/bin/env python3
"""Camera motion per second of a clip, to pick steady windows: speed = smooth movement, shake = jitter around it.

usage: python3 steady_scan.py <clip.mp4> [more ...]

Phase correlation between consecutive frames on a 270-px-wide grey copy, reported in px at the clip's own width.
Prints one column per second. Pick windows where shake stays low (under ~2 px) for walk-and-talk or handheld shots.
Needs ffmpeg and numpy.
"""
import json
import subprocess
import sys

import numpy as np


def scan(path, w=270):
    s = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,avg_frame_rate",
                                   "-of", "json", path], capture_output=True, text=True).stdout)["streams"][0]
    W, H = s["width"], s["height"]; h = int(round(H * w / W / 2) * 2); n_, d_ = s["avg_frame_rate"].split("/"); fps = round(float(n_) / float(d_ or 1))
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"scale={w}:{h},format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    n = len(raw) // (w * h); fr = np.frombuffer(raw, np.uint8)[: n * w * h].reshape(n, h, w).astype(np.float32)
    win = np.outer(np.hanning(h), np.hanning(w)); k = W / w; d = []
    for a, b in zip(fr, fr[1:]):
        F = np.fft.fft2(a * win) * np.conj(np.fft.fft2(b * win)); R = np.fft.ifft2(F / (np.abs(F) + 1e-6)).real
        y, x = np.unravel_index(np.argmax(R), R.shape); y = y - h if y > h // 2 else y; x = x - w if x > w // 2 else x
        d.append((x * k, y * k))
    d = np.array(d, float); sm = np.stack([np.convolve(d[:, i], np.ones(9) / 9, "same") for i in range(2)], 1)
    return fps, np.sqrt(((d - sm) ** 2).sum(1)), np.sqrt((sm ** 2).sum(1))


def main():
    for path in sys.argv[1:]:
        fps, jit, spd = scan(path); secs = len(jit) // fps
        print(path)
        print("  s    : " + " ".join(f"{i:>4}" for i in range(secs)))
        print("  speed: " + " ".join(f"{spd[i * fps:(i + 1) * fps].mean():4.0f}" for i in range(secs)))
        print("  shake: " + " ".join(f"{jit[i * fps:(i + 1) * fps].mean():4.1f}" for i in range(secs)))


if __name__ == "__main__":
    main()
