#!/usr/bin/env python3
"""Make a built page work offline: every image path it references is inlined as a data URL.

usage: offline.py page.html out.html [image_root]

image_root (default: the folder page.html is in) is where the page's relative image paths
(img/01-desk-talking.jpg, img/backdrops/moon.jpg, a creator's photo…) are found.
Images are resized to at most 1280 px wide (needs Pillow; without it they are inlined as-is).
Used for offline copies of decision pages kept in the episode folder.
"""
import base64, io, pathlib, re, sys

src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
root = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else src.parent
page = src.read_text(encoding="utf-8")
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}
try:
    from PIL import Image
except ImportError:
    Image = None
cache, missing = {}, set()

def data_url(rel):
    if rel in cache: return cache[rel]
    f = root / rel
    if not f.exists():
        missing.add(rel); cache[rel] = rel; return rel
    raw, mime = f.read_bytes(), MIME[f.suffix.lower()]
    if Image is not None:
        im = Image.open(io.BytesIO(raw))
        if im.width > 1280:
            im.thumbnail((1280, 1280 * 4)); b = io.BytesIO()
            if mime == "image/jpeg": im.convert("RGB").save(b, "JPEG", quality=84)
            else: im.save(b, "PNG")
            raw = b.getvalue()
    cache[rel] = f"data:{mime};base64," + base64.b64encode(raw).decode("ascii")
    return cache[rel]

# any relative image path inside attributes, CSS url(...) or the page's JSON data
pat = re.compile(r"""(?<=["'(=])\s*((?:\.\./)?(?:[\w .&-]+/)*[\w .&-]+\.(?:jpe?g|png|webp))(?=\s*["')])""", re.I)
page = pat.sub(lambda m: m.group(0).replace(m.group(1), data_url(m.group(1).strip())), page)
out.write_text(page, encoding="utf-8")
print(f"wrote {out} ({out.stat().st_size / 1e6:.1f} MB, {len(cache) - len(missing)} images inlined)")
if missing: print("not found (left as paths):", ", ".join(sorted(missing)))
