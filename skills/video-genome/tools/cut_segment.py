#!/usr/bin/env python3
"""Cut one take segment into a clip file for a HyperFrames composition, with no stutter: every kept take frame sits at
its true time (the first kept frame is not pulled to 0, so lips stay in sync), and the clip is meant to start half a
frame in (data-media-start = 0.5/fps), so the browser never shows the same frame twice.

usage: python3 cut_segment.py <take.mp4> <in_s> <out_s> <out.mp4|out.webm> [--speed 1.0] [--matte matte.mp4]
         [--erode 1] [--pad 0.3]

  --matte   grey matte (white = person) cut the same way and merged as alpha: writes a VP9 webm with transparency
  --erode   1 px edge trims on the matte (0 = none)
  --pad     extra seconds kept past out_s so a slightly longer slot never holds the last frame
Prints the clip attributes to paste: data-media-start, data-duration. Why both rules: WebM stores frame times in whole
milliseconds (frame 17 at 30 fps = 0.567 s, asked for at 0.5667 s), so a clip started on a whole frame repeats every
third frame and skips the next; and ffmpeg's first kept frame after a seek lands at time 0 unless it is placed.
glitch_gate.py checks both (half-frame start on every clip, frame_map.py drift and doubled first frames).
Needs ffmpeg.
"""
import argparse
import json
import math
import subprocess


def fps_of(p):
    s = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=avg_frame_rate",
                                   "-of", "json", p], capture_output=True, text=True).stdout)["streams"][0]["avg_frame_rate"]
    n, d = s.split("/")
    return float(n) / float(d or 1)


def cut(take, a_raw, b, out, speed=1.0, matte=None, erode=1, pad=0.3, fps=None):
    fps = fps or round(fps_of(take), 3)
    a = round(max(0.0, a_raw - 1 / fps), 4)                       # seek one take frame early ...
    ln = b - a + pad
    off = (math.ceil(a * fps - 1e-6) / fps - a_raw) / speed       # ... and place the first kept frame at its true time
    vf = f"setpts=(PTS-STARTPTS)/{speed}{off:+.6f}/TB,fps={fps}:start_time=0"
    dur = (b - a_raw) / speed
    trim = f"trim=duration={dur + pad:.4f}"
    if matte:
        er = ",".join(["erosion"] * erode)
        fc = f"[0:v]{vf}[c];[1:v]{vf},format=gray{',' + er if er else ''}[m];[c][m]alphamerge,format=yuva420p,{trim}[o]"
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.4f}", "-t", f"{ln:.4f}", "-i", take, "-ss", f"{a:.4f}", "-t", f"{ln:.4f}", "-i", matte,
               "-filter_complex", fc, "-map", "[o]", "-an", "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0", "-crf", "30",
               "-deadline", "good", "-cpu-used", "4", "-row-mt", "1", "-auto-alt-ref", "0", out]
    else:
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.4f}", "-t", f"{ln:.4f}", "-i", take, "-vf", f"{vf},{trim}", "-an",
               "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", "-g", str(int(fps)), out]
    subprocess.run(cmd, check=True)
    return {"data-media-start": round(0.5 / fps, 4), "data-duration": round(dur, 4), "fps": fps}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("take"); ap.add_argument("a", type=float); ap.add_argument("b", type=float); ap.add_argument("out")
    ap.add_argument("--speed", type=float, default=1.0); ap.add_argument("--matte"); ap.add_argument("--erode", type=int, default=1)
    ap.add_argument("--pad", type=float, default=0.3)
    x = ap.parse_args()
    r = cut(x.take, x.a, x.b, x.out, x.speed, x.matte, x.erode, x.pad)
    print(f'{x.out}: data-media-start="{r["data-media-start"]}" data-duration="{r["data-duration"]}" (start the clip on a frame: '
          f'data-start = frame / {r["fps"]:g})')


if __name__ == "__main__":
    main()
