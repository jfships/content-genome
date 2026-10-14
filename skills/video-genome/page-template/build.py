#!/usr/bin/env python3
"""Build one video-genome decision page from the template + a data JSON.

usage: build.py data.json out.html

The data JSON holds the page (see ../decision-pages.md, "Build every page from the
template"). Two fields are handled here rather than in the page's script:
  fonts: ["bebas-neue", ...]  slugs from fonts/fonts.json; each font is inlined as
                               a base64 @font-face so the page looks the same on
                               every machine with no network.
  head:  "<style>…</style><script>…</script>"  injected once into <head>; for
                               click-to-play functions (option play: "fnName")
                               and Web Audio sketches. Never autoplay.
  stage, stepId, part, journeyIf: the header band is computed from journey.json.
  nicheWords: the creator's niche words; the build stops if option copy uses any.
  houseRules: {"words": [...], "noAllCaps": true}; noAllCaps is applied (Title Case), a banned word stops the build.
  locked: true republishes a reviewed page read-only ("Done. Your picks are saved. Continue in chat.").
Images in options are paths relative to out.html.
"""
import json, sys, html, pathlib, base64

here = pathlib.Path(__file__).parent
data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
tpl = (here / "voting-page.html").read_text(encoding="utf-8")

fonts_css = ""
if data.get("fonts"):
    manifest = json.loads((here / "fonts" / "fonts.json").read_text(encoding="utf-8"))
    for slug in data["fonts"]:
        if slug not in manifest or slug.startswith("_"):
            sys.exit(f"build.py: unknown font slug '{slug}' (see fonts/fonts.json)")
        m = manifest[slug]
        b64 = m.get("woff2", "")   # the font file itself, stored inline in fonts.json
        if not b64:
            sys.exit(f"build.py: font '{slug}' has no data in fonts/fonts.json")
        fonts_css += (f'@font-face{{font-family:"{m["family"]}";src:url(data:font/woff2;base64,{b64}) '
                      f'format("woff2");font-weight:{m["weight"]};font-style:normal;font-display:block}}\n')

# fontFiles: brand fonts that aren't in fonts.json (kept in the brand folder's 01 Brand Kit/fonts/):
#   [{"family": "Brand Sans", "path": "/abs/or/relative/to/data.json/BrandSans.woff2", "weight": 700}]
for ff in data.get("fontFiles", []):
    fp = pathlib.Path(ff["path"])
    if not fp.is_absolute(): fp = pathlib.Path(sys.argv[1]).parent / fp
    if not fp.exists(): sys.exit(f"build.py: font file not found: {fp}")
    fmt = {".woff2": "woff2", ".woff": "woff", ".ttf": "truetype", ".otf": "opentype"}.get(fp.suffix.lower(), "woff2")
    mime = {"woff2": "font/woff2", "woff": "font/woff", "truetype": "font/ttf", "opentype": "font/otf"}[fmt]
    fonts_css += (f'@font-face{{font-family:"{ff["family"]}";src:url(data:{mime};base64,{base64.b64encode(fp.read_bytes()).decode()}) '
                  f'format("{fmt}");font-weight:{ff.get("weight", 400)};font-style:normal;font-display:block}}\n')

# ---- journey: the header band (stage n of N, step n of N, strip, % done) comes from journey.json ----
if data.get("stage"):
    J = json.loads((here / "journey.json").read_text(encoding="utf-8"))
    want = set(data.get("journeyIf", []))
    stages = [st for st in J["stages"] if not st.get("if") or st["if"] in want]
    ids = [st["id"] for st in stages]
    if data["stage"] not in ids:
        sys.exit(f"build.py: unknown stage '{data['stage']}' (see journey.json)")
    si = ids.index(data["stage"]); st = stages[si]
    sids = [x["id"] for x in st["steps"]]
    if data.get("stepId") not in sids:
        sys.exit(f"build.py: unknown stepId '{data.get('stepId')}' for stage '{data['stage']}' (see journey.json)")
    k = sids.index(data["stepId"]); step = st["steps"][k]
    total = sum(len(x["steps"]) for x in stages)
    before = sum(len(x["steps"]) for x in stages[:si]) + k
    data["_journey"] = {
        "stages": [{"name": x["name"], "state": "now" if i == si else "done" if (i < si or data.get("change")) else ""} for i, x in enumerate(stages)],
        "stageName": st["name"], "stageIndex": si + 1, "stageCount": len(stages),
        "step": k + 1, "stepCount": len(st["steps"]), "part": data.get("part", ""),
        "pct": round(100 * before / total)}
    data.setdefault("skippable", not step.get("required", True))

# ---- copy checks: option copy is universal (never the creator's niche) and never uses banned words ----
import re
def texts():
    yield data.get("title", ""); yield data.get("what", "")
    secs = data.get("sections") or [{"options": data.get("options") or []}]
    for sec in secs:
        yield sec.get("title", ""); yield sec.get("line", ""); yield sec.get("rule", "")
        for o in sec.get("options", []):
            yield o.get("name", ""); yield o.get("line", "")
            h = re.sub(r"<style.*?</style>", " ", o.get("html", ""), flags=re.S)
            yield re.sub(r"<[^>]+>", " ", h)
BANNED = [r"made[- ]pictures?", r"made[- ]scenes?"]
niche = [w for w in data.get("nicheWords", []) if w.strip()]
hits = []
for t in texts():
    for pat in BANNED + [r"\b" + re.escape(w) for w in niche]:
        m = re.search(pat, t or "", flags=re.I)
        if m: hits.append(f"'{m.group(0)}' in: {t.strip()[:80]}")
# House rules the creator set (house-rules.md) bind option copy and mocks too:
#   houseRules: {"words": ["epic", ...], "noAllCaps": true}
# After noAllCaps is applied (below), the check that follows only catches what slipped through.
HR = data.get("houseRules") or {}
CAPS_OK = {"TV", "EP", "OK", "AI", "DIY", "VHS", "REC", "CAM", "LIVE", "USA", "UK", "BPM", "HD", "4K", "DJ", "FAQ", "PM", "AM"}
# noAllCaps is applied, not just checked: all-caps words in option copy and mocks become Title Case, and
# text-transform:uppercase / letter-spacing are dropped, so example mocks follow the rule without hand edits.
# (A font that only has capitals, like Bebas Neue, still draws capitals: that's the creator's font choice.)
def _title(m):
    w = m.group(0)
    return w if w in CAPS_OK else w[0] + w[1:].lower()
def _decap_text(t): return re.sub(r"\b[A-Z][A-Z']{1,}\b", _title, t)
def _decap_html(h):
    h = re.sub(r"text-transform\s*:\s*uppercase\s*;?", "", h, flags=re.I)
    h = re.sub(r"letter-spacing\s*:\s*[^;\"']+;?", "", h, flags=re.I)
    return re.sub(r">([^<]+)<", lambda m: ">" + _decap_text(m.group(1)) + "<", h)
if HR.get("noAllCaps") and data.get("page") != "genome":
    fixed = 0
    for sec in (data.get("sections") or [{"options": data.get("options") or []}]):
        for o in sec.get("options", []):
            if o.get("houseExempt"): continue
            for k in ("name", "line"):
                if o.get(k): o[k] = _decap_text(o[k])
            if o.get("html"):
                nh = _decap_html(o["html"]); fixed += nh != o["html"]; o["html"] = nh
    if fixed: print(f"build.py: no-all-caps house rule applied to {fixed} mocks")
def opt_texts():
    secs = data.get("sections") or [{"options": data.get("options") or []}]
    for sec in secs:
        for o in sec.get("options", []):
            if o.get("houseExempt"): continue
            h = re.sub(r"<style.*?</style>", " ", o.get("html", ""), flags=re.S)
            yield o.get("name", ""), o.get("line", ""), h
for name, line, h in opt_texts():
    vis = " ".join([name, line, re.sub(r"<[^>]+>", " ", h)])
    for w in HR.get("words", []):
        if w.strip() and re.search(r"\b" + re.escape(w), vis, flags=re.I): hits.append(f"house rule word '{w}' in: {name}")
    if HR.get("noAllCaps"):
        if re.search(r"text-transform\s*:\s*uppercase", h, flags=re.I): hits.append(f"house rule (no all-caps): text-transform:uppercase in: {name}")
        for m in re.finditer(r"\b[A-Z][A-Z']{2,}\b", vis):
            if m.group(0) not in CAPS_OK: hits.append(f"house rule (no all-caps): '{m.group(0)}' in: {name}"); break
# ---- video-genome checks: plain words, one decision per page ----
# Internal labels never reach the creator: step/beat/layout codes (A4, B5, L1, C3) and the page's own
# ids and slugs (option ids, round, section ids). Real words with a hyphen ("day-by-day") are fine.
# A page can allow a real-world code with "allowWords": ["Q3"].
CODE = re.compile(r"\b[A-Z]{1,2}\d{1,2}\b")
CODE_OK = {"4K", "EP"} | set(data.get("allowWords", []))
ids = {data.get("round", "")}
for sec in (data.get("sections") or [{"options": data.get("options") or []}]):
    ids.add(sec.get("id", ""))
    ids |= {o.get("id", "") for o in sec.get("options", [])}
ids = {i for i in ids if i and ("-" in i or "_" in i)}
def plain_fields():
    yield data.get("title", ""); yield data.get("what", ""); yield data.get("next", "")
    for v in (data.get("context") or {}).values(): yield str(v)
    for sec in (data.get("sections") or [{"options": data.get("options") or []}]):
        yield sec.get("title", ""); yield sec.get("line", "")
        for o in sec.get("options", []):
            yield o.get("name", ""); yield o.get("line", ""); yield o.get("at", ""); yield o.get("why", "")
            if isinstance(o.get("taken"), str): yield o["taken"]
for t in plain_fields():
    t = t or ""
    for m in CODE.finditer(t):
        if m.group(0) not in CODE_OK: hits.append(f"internal label '{m.group(0)}' in: {t.strip()[:80]} (say where and what in plain words)")
    for i in ids:
        if re.search(r"(?<![\w-])" + re.escape(i) + r"(?![\w-])", t): hits.append(f"internal id '{i}' in: {t.strip()[:80]}")
    if re.search(r"\b[a-z0-9]+_[a-z0-9_]+\b", t): hits.append(f"slug-like word in: {t.strip()[:80]}")
picks = [s for s in (data.get("sections") or []) if s.get("single")]
if len(picks) > 1:
    hits.append(f"{len(picks)} sections each pick a Main: that's {len(picks)} decisions. One decision per page; split it.")
if hits and data.get("page") != "genome":   # the Genome page is the creator's own: their niche belongs there
    sys.exit("build.py: copy check failed (option copy must be universal; banned words and house-rule breaks never appear):\n  " + "\n  ".join(hits))

page = tpl.replace("__TITLE__", html.escape(data.get("title", "Voting page")))
page = page.replace("__FONTS__", fonts_css)
page = page.replace("__HEAD__", data.get("head", ""))
page = page.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
pathlib.Path(sys.argv[2]).write_text(page, encoding="utf-8")
n = len(data.get("options") or []) + sum(len(s.get("options", s.get("items", []))) for s in data.get("sections", []))
print("wrote", sys.argv[2], "with", n, "options", f"and {len(data.get('fonts', []))} fonts" if data.get("fonts") else "")
