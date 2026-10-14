#!/usr/bin/env python3
"""Brand check: list colors and fonts in a build that aren't in the brand file's packs (Brand Genome.md or Brand Sheet.md; colors and fonts under "## 5. Look" or a "Packs" heading).

Usage:
  python3 brand_check.py <build folder> "<Brand Genome.md | Brand Sheet.md>" [--pack "Pack name"] [--allow "Geist,#0B0B0B"]

Scan the folder you render from (the HyperFrames project, or motion/clips for the
talking-head engine). Colors and fonts are read only from the Genome's "Packs"
section (one pack with --pack), so colors mentioned under house rules or "No"
options don't count as on-brand. Prints off-brand items with the files they're
in; exit code 1 if any.

Checked: hex (#rgb, #rgba, #rrggbb, #rrggbbaa), rgb()/rgba() with or without
commas, hsl()/hsla(), CSS font-family (quoted or not) and JS fontFamily.
Ignored: black, white, fully transparent colors, generic font names, HTML
character codes (&#160;), CSS id selectors, node_modules, and the bundled
talking-head engine's own base styles. Named CSS colors (e.g. "tomato") are
not checked; avoid them in builds.
"""
import argparse
import colorsys
import re
import sys
from pathlib import Path

HEX = re.compile(r"(?<![&\w])#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{4}|[0-9a-fA-F]{3})\b(?!\s*[{,]\s*[#.\w-]*\s*\{)(?!\s*\{)")
RGB = re.compile(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)")
HSL = re.compile(r"hsla?\(\s*([\d.]+)(?:deg)?[\s,]+([\d.]+)%[\s,]+([\d.]+)%(?:\s*[,/]\s*([\d.]+%?))?\s*\)")
FONT_CSS = re.compile(r"font-family\s*:\s*([^;}{]+)", re.I)
FONT_JS = re.compile(r"fontFamily\s*[:=]\s*[\"'`]([^\"'`]+)[\"'`]")
GENERIC = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "inherit",
           "initial", "unset", "ui-sans-serif", "ui-serif", "ui-monospace", "emoji", "math"}
NEUTRAL = {"#000000", "#ffffff"}
ENGINE_FILES = {"base.css"}


def norm_hex(h):
    h = h.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    return "#" + h[:6], (int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)


def alpha(a):
    if a in (None, ""):
        return 1.0
    return float(a[:-1]) / 100 if a.endswith("%") else float(a)


def packs_section(text, pack):
    m = (re.search(r"^\s*(?:#+\s*)?(?:\d+\.\s*)?\**Packs?\**.*$", text, re.M | re.I)
         or re.search(r"^\s*#+\s*\d+\.\s*\**Look\b.*$", text, re.M | re.I))   # Brand Genome / Brand Sheet: "## 5. Look"
    if not m:
        return text
    rest = text[m.start():]
    nxt = re.search(r"^\s*(?:#+\s*)?\d+\.\s*\**Movement", rest, re.M | re.I)
    sec = rest[: nxt.start()] if nxt else rest
    if pack:
        p = re.search(re.escape(pack), sec, re.I)
        if p:
            sec = sec[p.start():]
            q = re.search(r"^\s*(?:#+|\*\*|-\s*\*\*)\s*(?:Pack|[A-Z][\w &]+:)", sec[len(pack):], re.M)
            sec = sec[: len(pack) + q.start()] if q else sec
    return sec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build")
    ap.add_argument("genome")
    ap.add_argument("--pack")
    ap.add_argument("--allow", default="")
    a = ap.parse_args()

    gtext = Path(a.genome).read_text(encoding="utf-8", errors="ignore")
    sec = packs_section(gtext, a.pack)
    g_colors = {norm_hex(h)[0] for h in HEX.findall(sec)}
    allow = {x.strip().lower() for x in a.allow.split(",") if x.strip()}
    g_low = sec.lower()

    def font_ok(name):
        n = name.lower()
        if n in GENERIC or n in allow or n.startswith("var("):
            return True
        return re.search(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", g_low) is not None

    off_c, off_f = {}, {}
    files = [p for p in Path(a.build).rglob("*")
             if p.suffix.lower() in {".html", ".css", ".js", ".mjs"}
             and "node_modules" not in p.parts and p.name not in ENGINE_FILES
             and not p.name.endswith(".min.js")]
    for p in files:
        t = p.read_text(encoding="utf-8", errors="ignore")
        t = re.sub(r"&#\d+;|&#x[0-9a-f]+;", "", t, flags=re.I)
        found = []
        for h in HEX.findall(t):
            c, al = norm_hex(h)
            found.append((c, al))
        for r, g, b, al in RGB.findall(t):
            found.append(("#%02x%02x%02x" % (int(float(r)), int(float(g)), int(float(b))), alpha(al)))
        for hh, s, l, al in HSL.findall(t):
            r, g, b = colorsys.hls_to_rgb(float(hh) / 360, float(l) / 100, float(s) / 100)
            found.append(("#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255)), alpha(al)))
        for c, al in found:
            if al == 0 or c in NEUTRAL or c in g_colors or c in allow:
                continue
            off_c.setdefault(c, set()).add(p.name)
        fams = FONT_CSS.findall(t) + FONT_JS.findall(t)
        for fam in fams:
            for f in fam.split(","):
                f = f.strip().strip("'\"` ").strip()
                if f and not font_ok(f):
                    off_f.setdefault(f, set()).add(p.name)

    print(f"Scanned {len(files)} files; {len(g_colors)} brand colors in the Genome's packs"
          + (f" ({a.pack})" if a.pack else "") + ".")
    if not off_c and not off_f:
        print("PASS: every color and font is in the Genome.")
        return
    if off_c:
        print("\nColors not in the Genome (fix, or allow with a reason, e.g. a shade used for a shadow):")
        for c, fs in sorted(off_c.items()):
            print(f"  {c}  in {', '.join(sorted(fs))}")
    if off_f:
        print("\nFonts not in the Genome:")
        for f, fs in sorted(off_f.items()):
            print(f"  {f}  in {', '.join(sorted(fs))}")
    sys.exit(1)


if __name__ == "__main__":
    main()
