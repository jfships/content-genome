#!/usr/bin/env python3
"""Snap each word's start to where its sound really begins in the take, so graphics anchored to a word land on it
without measuring onsets by hand. Whisper's word times drift 50-150 ms; this measures the take's level around each
start and moves it to the onset.

usage: python3 onsets.py <take.mp4|wav> work/words.json work/words_onsets.json [--window 0.12] [--words "nine,dollar"]
       [--drift auto|0|<seconds>]

words.json: [{t0, t1, w}] (transcribe.py), {"words": [...]}, [{start, end, w}] or [[t0, t1, w]], in take time.
Writes the same words with t0 moved to the onset, the old time kept as t0_asr, and how it was found:
  gap   the word starts after a quiet stretch: the rise out of it (exact to ~5 ms)
  rise  connected speech: the sharpest level rise near the old start (good to ~20 ms; check anchors by ear)
  kept  nothing clear in the window: Whisper's time kept
--words limits the snap to those words (the graphic anchors); the rest are copied unchanged.
Drift first: Whisper can put a whole take early or late (0.8 s early has happened), which a 0.12 s search can never
reach. --drift auto (default) matches every word that starts a phrase (after a pause in the transcript) to the
nearest rise out of silence within 1.5 s, either side, and shifts all words by the median when 3+ agree; the shift
is printed and kept per word as "drift". --drift 0 turns it off; a number forces it.
Prints the words moved more than 40 ms. Needs ffmpeg and numpy.
"""
import argparse
import json
import subprocess

import numpy as np

HOP = 0.005


def level(path, sr=16000, win=0.01):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-vn", "-ac", "1", "-ar", str(sr), "-f", "s16le",
                          "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    fr = np.lib.stride_tricks.sliding_window_view(x, round(win * sr))[::round(HOP * sr)]
    return 20 * np.log10(np.sqrt((fr ** 2).mean(axis=1)) + 1e-9)


def load(path):
    data = json.load(open(path, encoding="utf-8"))
    wrapped = isinstance(data, dict)
    rows = data.get("words", []) if wrapped else data
    words = []
    for r in rows:
        if isinstance(r, (list, tuple)):
            words.append({"t0": float(r[0]), "t1": float(r[1]), "w": str(r[2])})
        else:
            d = dict(r)
            if "t0" not in d:
                d["t0"], d["t1"] = float(d.pop("start")), float(d.pop("end"))
            words.append(d)
    return words, wrapped, data


def onset(lv, t0, t1, prev, window, floor):
    a = max(round((t0 - window) / HOP), round(prev / HOP) + 1, 1)
    b = min(round((t0 + 0.08) / HOP), round((t1 - 0.03) / HOP), len(lv) - 1)
    if b <= a:
        return t0, "kept"
    seg = lv[a:b + 1]
    need = round(0.02 / HOP)
    quiet = 0
    for k, v in enumerate(seg):             # out of a quiet stretch: the first hop back above the floor
        if v < floor:
            quiet += 1
        elif quiet >= need:
            return (a + k) * HOP, "gap"
        else:
            quiet = 0
    rise = np.diff(lv[a - 1:b + 1], n=1)
    rise = np.convolve(rise, np.ones(3), "same")   # rise over 15 ms
    k = int(np.argmax(rise))
    if rise[k] < 6:                          # under 6 dB in 15 ms: no clear start
        return t0, "kept"
    return (a + k) * HOP, "rise"


def drift_auto(lv, words, floor, reach=1.5):
    need = round(0.02 / HOP); quiet = 0; rises = []
    for k, v in enumerate(lv):                       # every rise out of >= 20 ms of quiet in the take
        if v < floor:
            quiet += 1
        else:
            if quiet >= need:
                rises.append(k * HOP)
            quiet = 0
    if not rises:
        return 0.0, 0
    rises = np.array(rises)
    starts = np.array([w["t0"] for i, w in enumerate(words) if i == 0 or w["t0"] - words[i - 1]["t1"] >= 0.25])
    if len(starts) < 3:
        return 0.0, len(starts)
    def hits(s):                                     # phrase starts landing within 50 ms of a rise after shift s
        return int(sum(np.min(np.abs(rises - (t + s))) < 0.05 for t in starts))
    grid = np.round(np.arange(-reach, reach + 1e-9, 0.01), 2)
    score = np.array([hits(s) for s in grid]); best = int(np.argmax(score)); s = float(grid[best])
    base = hits(0.0)
    if score[best] >= max(3, 0.4 * len(starts)) and score[best] >= base + 2 and abs(s) > 0.04:
        return round(s, 3), len(starts)
    return 0.0, len(starts)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("take")
    ap.add_argument("words")
    ap.add_argument("out")
    ap.add_argument("--window", type=float, default=0.12, help="seconds before the old start to search")
    ap.add_argument("--words", dest="only", help="comma list: snap only these words")
    ap.add_argument("--drift", default="auto", help="auto, 0, or seconds to shift every word before snapping")
    a = ap.parse_args()

    lv = level(a.take)
    floor = max(float(np.percentile(lv, 10)) + 15, -45.0)
    only = {x.strip().lower() for x in a.only.split(",")} if a.only else None
    words, wrapped, data = load(a.words)
    if a.drift == "auto":
        dr, n = drift_auto(lv, words, floor)
        print(f"drift: {dr * 1000:+.0f} ms from {n} phrase starts" + ("" if dr else " (none applied)"))
    else:
        dr = float(a.drift)
    if dr:
        for w in words:
            w["t0"], w["t1"], w["drift"] = round(w["t0"] + dr, 3), round(w["t1"] + dr, 3), dr
    count = {"gap": 0, "rise": 0, "kept": 0}
    prev = 0.0
    for w in words:
        if only is None or w["w"].strip(" .,!?'\"").lower() in only:
            t, how = onset(lv, w["t0"], w["t1"], prev, a.window, floor)
            w["t0_asr"], w["t0"], w["onset"] = w["t0"], round(t, 3), how
            count[how] += 1
            if abs(t - w["t0_asr"]) > 0.04:
                print(f"{w['w']:<16} {w['t0_asr']:8.3f} -> {t:8.3f}  ({(t - w['t0_asr']) * 1000:+.0f} ms, {how})")
        prev = w["t0"]
    out = dict(data, words=words) if wrapped else words
    json.dump(out, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{sum(count.values())} words: {count['gap']} after a pause, {count['rise']} in connected speech, "
          f"{count['kept']} kept · floor {floor:.0f} dB · wrote {a.out}")


if __name__ == "__main__":
    main()
