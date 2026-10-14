#!/usr/bin/env python3
"""Apply a Brand Genome grade recipe to footage or a still, with ffmpeg.

Usage:
  python3 grade.py recipe.json in.mp4 out.mp4          # print + run
  python3 grade.py recipe.json --print                 # just print the filter

recipe.json (copy the values from the Genome's grade recipe):
  {"shadows": "#0f4c5c", "highlights": "#ffb27a", "saturation": 1.15,
   "contrast": 1.15, "brightness": 0.0, "grain": 8, "vignette": 0.3,
   "mono": false, "lift_blacks": 0.0, "strength": 0.6}

- shadows / highlights: tint colors pushed into the dark and bright tones.
- strength: how hard the tints push (0.3 subtle … 1.0 strong).
- grain: 0 (none) … 20 (heavy). vignette: 0 (none) … 0.6 (heavy).
- mono: true for black-and-white grades. lift_blacks: 0 … 0.15 (faded look).
Recipes the filter can't express (thermal maps, halftone, pixelation) are built
in code instead; see craft/graphics-library.md, "Building catalog options".
"""
import json
import subprocess
import sys


def hex_to_bal(h, strength):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    avg = (r + g + b) / 3
    return tuple(max(-1.0, min(1.0, (c - avg) * 2 * strength)) for c in (r, g, b))


def build_filter(rc):
    s = rc.get("strength", 0.6)
    parts = []
    if rc.get("shadows") or rc.get("highlights"):
        sr, sg, sb = hex_to_bal(rc.get("shadows", "#808080"), s)
        hr, hg, hb = hex_to_bal(rc.get("highlights", "#808080"), s)
        parts.append(f"colorbalance=rs={sr:.3f}:gs={sg:.3f}:bs={sb:.3f}:"
                     f"rh={hr:.3f}:gh={hg:.3f}:bh={hb:.3f}")
    sat = 0 if rc.get("mono") else rc.get("saturation", 1.0)
    parts.append(f"eq=contrast={rc.get('contrast', 1.0)}:saturation={sat}:"
                 f"brightness={rc.get('brightness', 0.0)}")
    lift = rc.get("lift_blacks", 0)
    if lift:
        parts.append(f"curves=all='0/{lift} 1/1'")
    if rc.get("grain"):
        parts.append(f"noise=alls={int(rc['grain'])}:allf=t")
    if rc.get("vignette"):
        angle = 0.3 + float(rc["vignette"])  # radians; larger = stronger
        parts.append(f"vignette=angle={angle:.2f}")
    return ",".join(parts)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    rc = json.load(open(sys.argv[1]))
    vf = build_filter(rc)
    if sys.argv[2] == "--print":
        print(vf)
        return
    src, out = sys.argv[2], sys.argv[3]
    cmd = ["ffmpeg", "-y", "-i", src, "-vf", vf]
    if out.lower().endswith((".mp4", ".mov", ".mkv")):
        cmd += ["-c:v", "libx264", "-crf", "16", "-preset", "medium", "-c:a", "copy"]
    cmd.append(out)
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
