#!/usr/bin/env python3
"""Is the picture in sync with the voice? Mouth opening per frame (face landmarks) against the voice level.

usage: python3 lip_sync.py <video> [--audio voice.wav --audio-at 12.4] [--from 0] [--to end] [--ref take.mp4 --ref-from 3.2]
       [--words words.json]

Prints the lag in frames: + = picture LATE against the sound, - = picture early (sub-frame, parabola on the best match
of a +-8 frame cross-correlation). With --words (take time, [{t0, t1, w}] or {"words": [...]}) it also checks every
word starting with b, p or m: the lips close, then open as the sound starts; the release-to-onset offset per word
and its median are the absolute check (the cross-correlation can be fooled by a steady talker).
The mouth opens before the sound, so an in-sync take reads about 1-2 frames "early" here (4 takes measured: -1.0 to
-2.7): the number is relative. Compare a built clip with its own take: --ref <take> and --ref-from (the clip's in
point in the take); FIX when they differ by more than half a frame. frame_map.py is the exact check when the clip file
keeps the take's framing; this one works on any framing.
Needs ffmpeg, numpy, opencv-python, mediapipe (face model downloads once to ~/.cache/video-genome/).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from draft_checks import MODEL, MODEL_URL  # noqa: E402


def fps_of(p):
    s = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=avg_frame_rate",
                                   "-of", "json", p], capture_output=True, text=True).stdout)["streams"][0]["avg_frame_rate"]
    n, d = s.split("/"); return float(n) / float(d or 1)


def mouth(path, t0, t1, fps):
    import urllib.request
    import mediapipe as mp
    from mediapipe.tasks.python import BaseOptions, vision
    if not MODEL.exists():
        MODEL.parent.mkdir(parents=True, exist_ok=True); urllib.request.urlretrieve(MODEL_URL, MODEL)
    lm = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path=str(MODEL)),
                                                                                running_mode=vision.RunningMode.VIDEO, num_faces=1))
    cap = cv2.VideoCapture(path); cap.set(cv2.CAP_PROP_POS_MSEC, t0 * 1000); out = []; i = 0
    while True:
        ok, f = cap.read()
        if not ok or (t1 and t0 + i / fps >= t1):
            break
        r = lm.detect_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(f, cv2.COLOR_BGR2RGB)), int(i * 1000 / fps))
        if r.face_landmarks:
            p = r.face_landmarks[0]; H, W = f.shape[:2]
            d = np.hypot((p[13].x - p[14].x) * W, (p[13].y - p[14].y) * H); fh = np.hypot((p[10].x - p[152].x) * W, (p[10].y - p[152].y) * H)
            out.append(d / fh)
        else:
            out.append(np.nan)
        i += 1
    lm.close(); a = np.array(out); m = np.isnan(a)
    if m.any() and (~m).any():
        a[m] = np.interp(np.where(m)[0], np.where(~m)[0], a[~m])
    return a


def audio(path, sr=16000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)


def level(x, t0, n, fps, sr=16000):
    h = int(0.020 * sr); out = []
    for k in range(n):
        c = int((t0 + k / fps) * sr); s = x[max(0, c - h):max(0, c + h)]
        out.append(np.sqrt((s ** 2).mean()) if len(s) else 0)
    return np.log10(np.array(out) + 1e-4)


def lag(mo, en, R=8):
    z = lambda v: (v - np.nanmean(v)) / (np.nanstd(v) + 1e-9)
    n = min(len(mo), len(en)); m, e = z(mo[:n]), z(en[:n]); r = {}
    for L in range(-R, R + 1):
        r[L] = float((m[L:] * e[:n - L]).mean()) if L >= 0 else float((m[:n + L] * e[-L:]).mean())
    b = max(r, key=r.get); fb = float(b)
    if -R < b < R:
        y0, y1, y2 = r[b - 1], r[b], r[b + 1]; fb = b + 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2 + 1e-12)
    return round(fb, 2), round(r[b], 2)


def plosives(g, x, words, t0, fps, sr=16000):
    h = int(0.005 * sr); lv = 20 * np.log10(np.sqrt((x[:len(x) // h * h].reshape(-1, h) ** 2).mean(1)) + 1e-5)
    lt = (np.arange(len(lv)) + 0.5) * 0.005; ft = t0 + np.arange(len(g)) / fps; res = []
    for i, w in enumerate(words):
        if i == 0 or not w["w"][:1].lower() in "bpm":
            continue
        win = (ft > w["t0"] - 0.30) & (ft < w["t0"] + 0.12)
        if win.sum() < 5:
            continue
        fi = np.where(win)[0]; jm = fi[np.argmin(g[fi])]; after = np.arange(jm, min(len(g), jm + 9))
        gmin, gmax = g[jm], g[after].max()
        if gmax - gmin < 0.03:
            continue
        thr = gmin + 0.35 * (gmax - gmin); k = after[np.argmax(g[after] > thr)]
        if k == 0:
            continue
        vrel = ft[k - 1] + (thr - g[k - 1]) / (g[k] - g[k - 1] + 1e-9) / fps
        ai = np.where((lt > ft[jm] - 0.10) & (lt < ft[jm] + 0.35))[0]
        if not len(ai):
            continue
        lo, hi = lv[ai[:max(3, len(ai) // 6)]].min(), lv[ai].max()
        if hi - lo < 10:
            continue
        aon = lt[ai[np.argmax(lv[ai] > lo + 0.5 * (hi - lo))]]
        res.append((w["w"], round((vrel - aon) * fps, 2)))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("--audio"); ap.add_argument("--from", dest="t0", type=float, default=0.0)
    ap.add_argument("--to", dest="t1", type=float, default=0.0); ap.add_argument("--audio-at", type=float, help="where the clip sits in --audio (s); default --from")
    ap.add_argument("--words"); ap.add_argument("--ref"); ap.add_argument("--ref-from", type=float, default=0.0)
    a = ap.parse_args()
    fps = fps_of(a.video); mo = mouth(a.video, a.t0, a.t1, fps)
    x = audio(a.audio or a.video); at = a.audio_at if a.audio_at is not None else a.t0
    L, c = lag(mo, level(x, at, len(mo), fps), )
    print(f"{len(mo)} frames: picture {'LATE' if L > 0 else 'early'} by {abs(L):.2f} frames (corr {c:.2f})")
    if a.ref:
        rf = fps_of(a.ref); rm = mouth(a.ref, a.ref_from, a.ref_from + len(mo) / fps, rf)
        RL, rc = lag(rm, level(audio(a.ref), a.ref_from, len(rm), rf))
        print(f"its take: {RL:+.2f} frames (corr {rc:.2f}); build against take {L - RL:+.2f} frames" + ("  FIX" if abs(L - RL) > 0.5 else "  ok"))
    if a.words:
        d = json.load(open(a.words, encoding="utf-8")); d = d.get("words", d) if isinstance(d, dict) else d
        ws = [{"w": w["w"], "t0": float(w.get("t0", w.get("start", 0)))} for w in d]
        if a.audio and a.audio_at is not None:
            print("b/p/m check needs words on the same clock as the picture; skipped"); return
        r = plosives(mo, x, ws, a.t0, fps)
        if r:
            print(f"b/p/m lip release vs sound: median {np.median([v for _, v in r]):+.2f} frames over {len(r)} words: {r}")
        else:
            print("b/p/m check: no clear lip closures found")


if __name__ == "__main__":
    main()
