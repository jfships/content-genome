#!/usr/bin/env python3
"""Stills straight from a HyperFrames composition, with no render: seeks the GSAP timeline, sets every video to its own
time, hides clips outside their window, then screenshots. Also reads what is on screen per element (opacity, box) so
checks can run on the composition (glitch_gate.py imports it).

usage: python3 comp_stills.py <hf folder | index.html> --out <folder>
         (--at 1.2,3.4 | --frames 30-60 | --around 2.47,6.83 [--pad 9]) [--scale 0.5] [--dom] [--clean]

  --at       times in seconds          --frames  a range of frame numbers at the composition's fps (both ends kept)
  --around   cut times: every frame from pad before to pad after each one
  --scale    still size against the composition (0.5 = 540 wide); --dom writes dom.json (per frame, every element
             with an id: opacity on screen, box, shown or not); --clean hides [data-cue] / .cue / .placeholder elements
Stills are named f<frame>-t<seconds>.png; stills.json lists them. The page is opened from disk (file://), so assets
must sit inside the hf folder; the composition must register window.__timelines (setup/gotchas.md).
Video time per clip = data-media-start + (t - data-start), the same rule the renderer uses, so a clip that starts on a
whole frame shows the same repeated frames here as in the render (shorts/build.md "Clip timing").
Needs: pip install playwright && python -m playwright install chromium.
"""
import argparse
import json
import re
from pathlib import Path

SEEK_JS = """async ([t, clean, media]) => {
  await document.fonts.ready;
  const tls = window.__timelines || {};
  const tl = tls.main || Object.values(tls)[0];
  if (!tl) throw new Error('no window.__timelines registered');
  tl.pause(); tl.seek(t, false);
  const root = document.querySelector('[data-composition-id]');
  const waits = [];
  document.querySelectorAll('[data-start]').forEach(el => {
    if (el === root) return;
    const s = +el.dataset.start, d = +(el.dataset.duration || 1e9);
    const on = t >= s - 1e-6 && t < s + d - 1e-6;
    el.style.visibility = on ? 'visible' : 'hidden';
    if (media && (el.tagName === 'VIDEO' || el.tagName === 'AUDIO') && on) {
      const m = +(el.dataset.mediaStart || 0) + (t - s);
      el.pause();
      if (Math.abs(el.currentTime - m) > 1e-4) waits.push(new Promise(r => {
        const done = () => r(); el.addEventListener('seeked', done, {once: true}); setTimeout(done, 3000); el.currentTime = m; }));
    }
  });
  if (clean) document.querySelectorAll('[data-cue],.cue,.placeholder').forEach(el => el.style.visibility = 'hidden');
  await Promise.all(waits);
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
}"""

DOM_JS = """() => {
  const W = innerWidth, H = innerHeight, out = {};
  const op = el => { let o = 1; for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return 0; o *= +cs.opacity; } return o; };
  document.querySelectorAll('[id]').forEach(el => {
    if (el.hasAttribute('data-composition-id') || el.tagName === 'SCRIPT' || el.tagName === 'AUDIO') return;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) return;
    const o = op(el), inview = r.right > 0 && r.bottom > 0 && r.left < W && r.top < H;
    const item = {o: +o.toFixed(3), box: [r.left, r.top, r.width, r.height].map(v => +v.toFixed(2)), on: o > 0.02 && inview,
      txt: [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())};
    if (el.tagName === 'IMG' || el.tagName === 'VIDEO') item.src = el.getAttribute('src');
    if (el.matches('[data-text-block],.hook,.title,.hook-text')) {     // text blocks: one size + fixed line height rule
      const sizes = new Set(), lhs = new Set(), lines = [];
      el.querySelectorAll('*').forEach(c => { if (c.childNodes.length && [...c.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) {
        const cs = getComputedStyle(c); sizes.add(cs.fontSize); lhs.add(cs.lineHeight); } });
      const cs = getComputedStyle(el); if ([...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) { sizes.add(cs.fontSize); lhs.add(cs.lineHeight); }
      const rg = document.createRange(); rg.selectNodeContents(el);
      for (const q of rg.getClientRects()) { if (q.width < 2) continue; const l = lines.find(x => Math.abs(x[0] - q.top) < 3);
        if (l) { l[1] = Math.max(l[1], q.bottom); } else lines.push([q.top, q.bottom]); }
      lines.sort((a, b) => a[0] - b[0]);
      item.text = {sizes: [...sizes], line_heights: [...lhs], lines: lines.map(l => [+l[0].toFixed(1), +l[1].toFixed(1)])};
    }
    out[el.id] = item;
  });
  return out;
}"""


def comp_info(index):
    html = Path(index).read_text(encoding="utf-8")
    m = re.search(r"<[^>]*data-composition-id[^>]*>", html)
    tag = m.group(0) if m else ""
    num = lambda k, d: float(re.search(rf'{k}="([\d.]+)"', tag).group(1)) if re.search(rf'{k}="([\d.]+)"', tag) else d
    return {"fps": num("data-fps", 30.0), "duration": num("data-duration", 0.0),
            "width": int(num("data-width", 1080)), "height": int(num("data-height", 1920))}


def index_path(p):
    p = Path(p)
    return p / "index.html" if p.is_dir() else p


def shoot(index, frames, out, fps, scale=0.5, dom=False, clean=False, shots=True):
    """frames: list of frame numbers. Returns [{frame, t, png, dom}]. shots=False skips screenshots and video seeks (DOM only, fast)."""
    from playwright.sync_api import sync_playwright
    index = index_path(index); info = comp_info(index); out = Path(out); out.mkdir(parents=True, exist_ok=True)
    rows, errors = [], []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        pg = b.new_page(viewport={"width": info["width"], "height": info["height"]}, device_scale_factor=scale)
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.goto(index.resolve().as_uri()); pg.wait_for_timeout(500)
        if errors:
            raise SystemExit(f"the composition throws on load (its timeline won't run): {errors[0]}")
        for f in sorted(set(frames)):
            t = round(f / fps, 6)
            pg.evaluate(SEEK_JS, [t, clean, shots])
            row = {"frame": f, "t": t}
            if shots:
                png = out / f"f{f:05d}-t{t:07.3f}.png"
                pg.screenshot(path=str(png)); row["png"] = str(png)
            if dom:
                row["dom"] = pg.evaluate(DOM_JS)
            rows.append(row)
        b.close()
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("comp"); ap.add_argument("--out", required=True)
    ap.add_argument("--at"); ap.add_argument("--frames"); ap.add_argument("--around"); ap.add_argument("--pad", type=int, default=9)
    ap.add_argument("--scale", type=float, default=0.5); ap.add_argument("--dom", action="store_true"); ap.add_argument("--clean", action="store_true")
    a = ap.parse_args()
    fps = comp_info(index_path(a.comp))["fps"]; fr = []
    if a.at: fr += [round(float(x) * fps) for x in a.at.split(",")]
    if a.frames:
        lo, hi = map(int, a.frames.split("-")); fr += list(range(lo, hi + 1))
    if a.around:
        for c in a.around.split(","):
            k = round(float(c) * fps); fr += list(range(k - a.pad, k + a.pad + 1))
    if not fr:
        raise SystemExit("give --at, --frames or --around")
    rows = shoot(a.comp, [f for f in fr if f >= 0], a.out, fps, a.scale, a.dom, a.clean)
    Path(a.out, "stills.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
    print(f"{len(rows)} stills -> {a.out}")


if __name__ == "__main__":
    main()
