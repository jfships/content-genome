#!/usr/bin/env python3
"""Speed up a voice line without the squeezed sound: Rubber Band's finer engine (R3), offline, formants kept.

usage: python3 voice_stretch.py <in.wav|mp4> <out.wav> --speed 1.08 [--ab]

ffmpeg's rubberband filter only has the older engine (R2), which distorted voices at 1.18-1.25x on a real Short; the
finer engine through pylibrb is the default here. Limit 1.10x: above it the tool refuses unless --force, and the
creator judges an A/B by ear first (--ab writes <out>-r2.wav next to it for that comparison). A line still slow at
1.10x is re-recorded faster. Picture for the same line: setpts=PTS/<speed>, frames placed at true time
(shorts/build.md "Clip timing"). Output 48 kHz, the input's channel count.
Needs ffmpeg, numpy, pylibrb (pip install pylibrb).
"""
import argparse
import subprocess
import wave

import numpy as np

SR = 48000
LIMIT = 1.10


def read(p, ch):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vn", "-ac", str(ch), "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, ch).copy()


def channels(p):
    o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=channels", "-of", "csv=p=0", p],
                       capture_output=True, text=True).stdout.strip()
    return max(1, min(2, int(o or 1)))


def finer(x, speed):
    import pylibrb as rb
    if abs(speed - 1) < 1e-6:
        return x.copy()
    O = rb.Option
    opts = O.PROCESS_OFFLINE | O.ENGINE_FINER | O.FORMANT_PRESERVED | O.CHANNELS_TOGETHER | O.PitchHighQuality | O.WINDOW_STANDARD
    s = rb.RubberBandStretcher(SR, x.shape[1], opts, 1.0 / speed, 1.0)
    a = np.ascontiguousarray(x.T.astype(np.float32))
    s.set_expected_input_duration(a.shape[1])
    if hasattr(s, "set_max_process_size"):
        s.set_max_process_size(a.shape[1])   # whole line in one block: avoids the buffer-resize warnings
    s.study(a, final=True); s.process(a, final=True)
    return np.ascontiguousarray(s.retrieve_available().T)


def write(p, x):
    w = wave.open(p, "wb"); w.setnchannels(x.shape[1]); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()); w.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("--speed", type=float, required=True)
    ap.add_argument("--ab", action="store_true"); ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    if a.speed > LIMIT and not a.force:
        raise SystemExit(f"{a.speed}x is over the {LIMIT}x limit: re-record the line faster, or A/B by ear with the creator and pass --force")
    ch = channels(a.src); x = read(a.src, ch); y = finer(x, a.speed); write(a.out, y)
    print(f"{len(x) / SR:.3f} s -> {len(y) / SR:.3f} s at {a.speed}x (finer engine) -> {a.out}")
    if a.ab:
        r2 = a.out.rsplit(".", 1)[0] + "-r2.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.src, "-ac", str(ch), "-ar", str(SR), "-af",
                        f"rubberband=tempo={a.speed}:transients=crisp:formant=preserved:pitchq=quality:channels=together", r2], check=True)
        print(f"A/B: {r2} (older engine) next to {a.out}")


if __name__ == "__main__":
    main()
