#!/usr/bin/env python3
"""The sound step's measured checks, before the creator approves a draft: loudness on target, no clipping, music bed as
long as the video, voice clear of the bed, the render's sound matching the mix, plus a listen file for the creator.

usage: python3 sound_check.py <mix.wav> [--comp hf/] [--length 43.27] [--bed bed.wav] [--voice voice.wav --music music.wav]
         [--sources take1.wav ...] [--target -14] [--render out/final.mp4] [--listen _review/listen-r3.m4a]

  --comp     reads the composition's length and every <audio> clip's window (a clip whose file ends early = silence)
  --bed      the music bed file as placed: it must run to the end of the video (minus a planned fade)
  --voice / --music   stems as mixed: voice must sit at least --over dB (default 8) over the ducked music
  --sources  files that had gain added (takes, voice lines): any clipped run is a FIX (gain added before a limiter)
  --render   a rendered video: its sound must match the mix within 1 LU; HyperFrames renders have come out ~5 dB low,
             so the fix is to remux the mix onto the render (command printed), never to re-render
  --listen   writes an AAC copy of the mix for the creator to hear before approving (shorts/build.md "Sound step")
Targets: integrated loudness within 1 LU of --target (the brand's number wins; default -14), true peak at or under -1 dBTP.
Prints FIX lines and a PASS/FAIL line; exit 1 on any FIX. Needs ffmpeg and numpy.
"""
import argparse
import re
import subprocess
from pathlib import Path

import numpy as np

FIXES = []


def fix(what, how):
    FIXES.append((what, how)); print(f"FIX  {what} -> {how}")


def loud(p):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    tail = e[e.rfind("Summary:"):]
    i = re.search(r"I:\s+(-?[\d.]+|-inf) LUFS", tail); pk = re.search(r"Peak:\s+(-?[\d.]+|-inf) dBFS", tail)
    f = lambda m: float(m.group(1)) if m and m.group(1) != "-inf" else -99.0
    return f(i), f(pk)


def length(p):
    o = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout
    return float(o.strip() or 0)


def clipped_runs(p, sr=48000):
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-vn", "-ar", str(sr), "-f", "f32le", "-"],
                                     capture_output=True).stdout, np.float32)
    hot = np.abs(x) >= 0.999
    if not hot.any():
        return 0
    d = np.diff(np.r_[0, hot.astype(np.int8), 0]); s, e = np.where(d == 1)[0], np.where(d == -1)[0]
    return int(((e - s) >= 3).sum())


def comp_audio(hf):
    idx = Path(hf); idx = idx / "index.html" if idx.is_dir() else idx
    html = idx.read_text(encoding="utf-8")
    root = re.search(r"<[^>]*data-composition-id[^>]*>", html).group(0)
    dur = float(re.search(r'data-duration="([\d.]+)"', root).group(1))
    rows = []
    for m in re.finditer(r"<audio\b[^>]*>", html):
        tag = m.group(0); g = lambda k: (re.search(rf'\b{k}="([^"]*)"', tag) or [None, None])[1]
        if not g("src"):
            continue
        st, du, ms = float(g("data-start") or 0), float(g("data-duration") or dur), float(g("data-media-start") or 0)
        f = idx.parent / g("src"); fl = length(f) if f.exists() else 0
        rows.append({"id": g("id"), "src": g("src"), "end": min(st + du, st + fl - ms), "file": f})
    return dur, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mix"); ap.add_argument("--comp"); ap.add_argument("--length", type=float); ap.add_argument("--bed")
    ap.add_argument("--voice"); ap.add_argument("--music"); ap.add_argument("--over", type=float, default=8.0)
    ap.add_argument("--sources", nargs="*", default=[]); ap.add_argument("--target", type=float, default=-14.0)
    ap.add_argument("--render"); ap.add_argument("--listen"); ap.add_argument("--fade", type=float, default=1.0, help="planned fade-out at the end, s")
    a = ap.parse_args()

    L = a.length
    if a.comp:
        L, rows = comp_audio(a.comp)
        for r in rows:
            gap = L - r["end"]
            print(f"audio {r['id'] or r['src']}: ends {r['end']:.2f} s of {L:.2f}")
            if gap > 0.1 and r["end"] > 0.5 * L:
                fix(f"{r['src']} stops {gap:.2f} s before the video ends", "extend or loop it to the end (its own phrase, level-matched joins)")
    I, TP = loud(a.mix); ml = length(a.mix)
    print(f"mix: {I:.1f} LUFS, true peak {TP:.1f} dBTP, {ml:.2f} s (target {a.target:.0f} LUFS, peak <= -1)")
    if abs(I - a.target) > 1:
        fix(f"mix at {I:.1f} LUFS, target {a.target:.0f}", f"gain the whole mix by {a.target - I:+.1f} dB, then limit to -1 dBTP")
    if TP > -1.0:
        fix(f"true peak {TP:.1f} dBTP", "limit the master at -1 dBTP (e.g. alimiter or loudnorm TP=-1)")
    if clipped_runs(a.mix):
        fix("the mix has clipped samples", "lower the gain before the limiter; find the clipped source with --sources")
    if L and ml < L - 0.05:
        fix(f"mix is {ml:.2f} s, video {L:.2f} s", "the mix must run the full video")
    if a.bed:
        bl = length(a.bed)
        print(f"bed: {bl:.2f} s")
        if L and bl < L - a.fade:
            fix(f"music bed {bl:.2f} s on a {L:.2f} s video", "loop a phrase of the bed (level-matched, short equal-power joins) to the end")
    if a.voice and a.music:
        vi, _ = loud(a.voice); mi, _ = loud(a.music)
        print(f"voice {vi:.1f} LUFS over music {mi:.1f} LUFS: {vi - mi:.1f} dB")
        if vi - mi < a.over:
            fix(f"voice only {vi - mi:.1f} dB over the music", f"duck the music to at least {a.over:.0f} dB under the voice")
    for s in a.sources:
        n = clipped_runs(s)
        if n:
            fix(f"{Path(s).name}: {n} clipped runs", "take the gain off before this file is written; gain later, then limit")
    if a.render:
        ri, rp = loud(a.render)
        print(f"render sound: {ri:.1f} LUFS, {rp:.1f} dBTP (mix {I:.1f})")
        if abs(ri - I) > 1:
            fix(f"render sound {ri:.1f} LUFS against the mix {I:.1f}",
                f'remux the mix: ffmpeg -i "{a.render}" -i "{a.mix}" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest <out>.mp4')
    if a.listen:
        Path(a.listen).parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.mix, "-c:a", "aac", "-b:a", "256k", a.listen], check=True)
        print(f"listen file: {a.listen} (the creator hears this before approving the sound)")
    print("FAIL" if FIXES else "PASS", f"{len(FIXES)} fixes")
    raise SystemExit(1 if FIXES else 0)


if __name__ == "__main__":
    main()
