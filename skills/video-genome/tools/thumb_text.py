#!/usr/bin/env python3
"""Thumbnail text block: build it to the rules in craft/thumbnails.md and measure it.

Usage: python3 thumb_text.py spec.json out.jpg

spec.json (1280x720 unless "size" says otherwise):
{
  "size": [1280, 720],
  "background": "bg.jpg" | "#1B4F8A",
  "person": {"file": "cutout.png", "x": 650, "y": -18, "scale": 0.8, "outline": 10},   # optional; white outline + soft drop
  "font": "/path/Display.ttf",                     # ONE family for the whole block
  "block": {"x": 60, "cy": 360, "width": 560, "gap": 26, "shadow": [3, 5, 2.5]},
  "rows": [
    {"text": "I Had", "color": "#FFFFFF", "size": 64},              # small lead-in, fixed size, may stay narrower
    {"text": "Zero", "color": "#FF7A1A"},                            # loud line: ink fit to the block width
    {"text": "Clue.", "color": "#FF7A1A"},
    {"text": "So I built 3 tools", "color": "#FFFFFF", "group": "c"},     # same group = one shared size,
    {"text": "to make my first video", "color": "#FFFFFF", "group": "c"}  # fit so the longest line fills the width
  ]
}

Rules it enforces: loud lines share one ink width (right edges line up); one fixed gap for the
whole block, measured from each line's baseline to the next line's top ink (descenders hang into
the gap and don't count; never scaled by font size); a small crisp shadow; the block is centered
on "cy". After rendering it re-measures the ink and prints every gap and right edge, so spacing is
checked by numbers, not by eye. A gap more than 2 px off the target prints FIX.
"""
import json
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def rgb(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def font(path, size):
    return ImageFont.truetype(path, int(size))


def ink_box(f, text):
    """Real ink bounds (x0, top, x1, bottom) relative to the baseline origin, from a rendered mask."""
    b = f.getbbox(text, anchor="ls")
    pad = 4
    w, h = b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).text((pad - b[0], pad - b[1]), text, font=f, fill=255, anchor="ls")
    ys, xs = np.where(np.array(m) > 60)
    ox, oy = pad - b[0], pad - b[1]
    return (int(xs.min()) - ox, int(ys.min()) - oy, int(xs.max()) + 1 - ox, int(ys.max()) + 1 - oy)


def size_for_width(path, text, width, lo=12, hi=500):
    while hi - lo > 1:
        m = (lo + hi) // 2
        b = ink_box(font(path, m), text)
        if b[2] - b[0] <= width:
            lo = m
        else:
            hi = m
    return lo


def person_layer(spec, size):
    p = Image.open(spec["file"]).convert("RGBA")
    s = spec.get("scale", 1.0)
    p = p.resize((int(p.width * s), int(p.height * s)), Image.LANCZOS)
    o = spec.get("outline", 10)
    pad = o * 3
    a = Image.new("L", (p.width + 2 * pad, p.height + 2 * pad), 0)
    a.paste(p.split()[3], (pad, pad))
    ring = a.filter(ImageFilter.MaxFilter(o * 2 + 1)).filter(ImageFilter.GaussianBlur(1))
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    x, y = spec.get("x", 0) - pad, spec.get("y", 0) - pad
    sh = Image.new("RGBA", a.size, (0, 0, 0, 0))
    sh.putalpha(ring.filter(ImageFilter.GaussianBlur(18)).point(lambda v: int(v * 0.6)))
    out.paste(sh, (x + 8, y + 10), sh)
    white = Image.new("RGBA", a.size, (255, 255, 255, 255))
    white.putalpha(ring)
    out.paste(white, (x, y), white)
    out.paste(p, (x + pad, y + pad), p)
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    spec = json.load(open(sys.argv[1]))
    W, H = spec.get("size", [1280, 720])
    bg = spec.get("background", "#000000")
    if bg.startswith("#"):
        im = Image.new("RGBA", (W, H), rgb(bg) + (255,))
    else:
        im = Image.open(bg).convert("RGBA").resize((W, H), Image.LANCZOS)
    if spec.get("person"):
        im.alpha_composite(person_layer(spec["person"], (W, H)))

    fp = spec["font"]
    blk = spec["block"]
    width, gap = blk["width"], blk.get("gap", round(26 * H / 720))
    sx, sy, blur = blk.get("shadow", [3, 5, 2.5])
    rows = spec["rows"]

    groups = {}
    for r in rows:
        if "group" in r:
            groups.setdefault(r["group"], []).append(r["text"])
    gsize = {g: min(size_for_width(fp, t, width) for t in ts) for g, ts in groups.items()}
    fonts = []
    for r in rows:
        if "size" in r:
            fonts.append(font(fp, r["size"]))
        elif "group" in r:
            fonts.append(font(fp, gsize[r["group"]]))
        else:
            fonts.append(font(fp, size_for_width(fp, r["text"], width)))

    # Vertical placement: baselines. Line i+1's top ink sits `gap` below line i's baseline.
    boxes = [ink_box(f, r["text"]) for r, f in zip(rows, fonts)]  # real ink, relative to baseline
    baselines = [0]
    for i in range(1, len(rows)):
        baselines.append(baselines[-1] + gap - boxes[i][1])
    top = boxes[0][1]
    bottom = baselines[-1] + boxes[-1][3]
    shift = blk["cy"] - (top + bottom) / 2
    baselines = [b + shift for b in baselines]

    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ds = ImageDraw.Draw(sh)
    for r, f, b, bx in zip(rows, fonts, baselines, boxes):
        ds.text((blk["x"] - bx[0] + sx, b + sy), r["text"], font=f, fill=(0, 0, 0, 150), anchor="ls")
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(im)
    for r, f, b, bx in zip(rows, fonts, baselines, boxes):
        d.text((blk["x"] - bx[0], b), r["text"], font=f, fill=rgb(r.get("color", "#FFFFFF")), anchor="ls")
    im.convert("RGB").save(sys.argv[2], quality=93)

    # Measure the real ink of each line on its own and report.
    print(f"target gap {gap}px · block width {width}px · left edge {blk['x']}px")
    tops, rights = [], []
    for r, f, b, bx in zip(rows, fonts, baselines, boxes):
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).text((blk["x"] - bx[0], b), r["text"], font=f, fill=255, anchor="ls")
        a = np.array(m) > 60
        ys, xs = np.where(a)
        tops.append(ys.min())
        rights.append(xs.max())
    bad = 0
    for i in range(1, len(rows)):
        g = int(tops[i] - round(baselines[i - 1]))
        flag = "" if abs(g - gap) <= 2 else "  FIX"
        bad += bool(flag)
        print(f"  gap {i}: baseline of '{rows[i-1]['text']}' -> top ink of '{rows[i]['text']}' = {g}px{flag}")
    # Lines fit to the width: every ungrouped loud line, plus the longest line of each group.
    fitted = [i for i, r in enumerate(rows) if "size" not in r and "group" not in r]
    for g in groups:
        idx = [i for i, r in enumerate(rows) if r.get("group") == g]
        fitted.append(max(idx, key=lambda i: rights[i]))
    if fitted:
        edges = sorted(int(rights[i]) for i in fitted)
        spread = edges[-1] - edges[0]
        tol = max(4, round(width * 0.02))
        print(f"  right edges of width-fitted lines: {edges} (spread {spread}px, allowed {tol}){'  FIX' if spread > tol else ''}")
        bad += spread > tol
    for i, (r, f) in enumerate(zip(rows, fonts)):
        print(f"  size {f.size:>3}px  '{r['text']}'")
    print("OK" if not bad else f"{bad} problem(s)")


if __name__ == "__main__":
    main()
