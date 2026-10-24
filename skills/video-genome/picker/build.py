#!/usr/bin/env python3
"""Build a video's live picker page from its picker.json.

usage: build.py picker.json out_dir [--only rowId[,rowId]]

--only builds a branched page holding just those rows (a re-pick), into its own out_dir; it shares the
picks store, so its answers land on the same rows.

out_dir gets index.html (the page), spec.json (what compose.js assembles; the render uses the same file)
and copies of the HyperFrames project's assets/ and fonts/ (published as the artifact's files).
Field reference: README.md.
"""
import json, re, shutil, sys, html, pathlib

here = pathlib.Path(__file__).parent
args = sys.argv[1:]
only = None
if "--only" in args:
    i = args.index("--only"); only = args[i + 1].split(","); del args[i:i + 2]
src = pathlib.Path(args[0]).resolve()
out = pathlib.Path(args[1]).resolve()
P = json.loads(src.read_text(encoding="utf-8"))
base_dir = src.parent
hf = (base_dir / P["hf"]).resolve()
base = (base_dir / P["base"]).read_text(encoding="utf-8")
problems = []
for m in ("/*@css*/", "<!--@html-->", "/*@js*/"):
    if base.count(m) != 1: problems.append(f"base composition needs exactly one {m}")

# ---- option fragments: a file with <style>, markup and <script>, or inline css/html/js ----
def fragment(o):
    if "src" in o:
        t = (base_dir / o.pop("src")).read_text(encoding="utf-8")
        o["css"] = "".join(re.findall(r"<style>(.*?)</style>", t, flags=re.S))
        o["js"] = "".join(re.findall(r"<script>(.*?)</script>", t, flags=re.S))
        o["html"] = re.sub(r"<(style|script)>.*?</\1>", "", t, flags=re.S).strip()

# ---- captions: one style for the whole video, generated from word timing ----
# option "captions": {"mode": "word"|"pair"|"line", "top": 1440, "maxWords": 3}
# Each chunk is a clip with data-beat = the beat row it falls in, so a beat with on-screen text hides its captions.
total = float(re.search(r'data-composition-id="[^"]+"[^>]*?data-duration="([\d.]+)"', base).group(1))
words = json.loads((base_dir / P["words"]).read_text(encoding="utf-8")) if P.get("words") else []
key = {k.lower() for k in P.get("keyWords", [])}
beats = [r for r in P["rows"] if r.get("tab") != "look" and r.get("span")]
def beat_of(t):
    for r in beats:
        if r["span"][0] <= t < r["span"][1]: return r["id"]
    return ""
def chunks(mode, most):
    out, cur = [], []
    for i, w in enumerate(words):
        if cur and (beat_of(w["t0"]) != beat_of(cur[0]["t0"]) or w["t0"] - cur[-1]["t1"] > 0.6):
            out.append(cur); cur = []
        cur.append(w)
        ends = bool(re.search(r"[.,!?]$", w["w"]))
        if mode == "word" or (mode == "pair" and (len(cur) >= most or ends)) or (mode == "line" and (ends or len(cur) >= most)):
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def captions(o):
    c = o.pop("captions"); mode = c.get("mode", "pair"); most = c.get("maxWords", 3 if mode == "pair" else 5)
    cs = chunks(mode, most); h, j = [], []
    for n, ch in enumerate(cs):
        t0 = ch[0]["t0"]; nxt = cs[n + 1][0]["t0"] if n + 1 < len(cs) else None
        t1 = ch[-1]["t1"] + 0.35
        if nxt is not None and beat_of(nxt) == beat_of(t0) and nxt - ch[-1]["t1"] <= 0.6: t1 = nxt
        if nxt is not None: t1 = min(t1, nxt)
        t1 = min(t1, total)
        span = " ".join(f'<i class="{"k" if re.sub(r"[^a-z0-9]", "", w["w"].lower()) in key else ""}">{html.escape(w["w"].rstrip(",."))}</i>' for w in ch)
        h.append(f'<div id="cap{n}" class="cap clip" data-beat="{beat_of(t0)}" data-start="{t0:.3f}" data-duration="{t1 - t0:.3f}" data-track-index="{c.get("track", 4)}"><span>{span}</span></div>')
        j.append(f'tl.fromTo("#cap{n} span",{{scale:1.12,opacity:0}},{{scale:1,opacity:1,duration:.12,ease:"power3.out",immediateRender:false}},{t0:.3f});')
    o["html"] = "\n".join(h) + "\n"; o["js"] = "\n".join(j) + "\n"
    o.setdefault("css", "")

ids = set()
for r in P["rows"]:
    if r["id"] in ids: problems.append(f"two rows called {r['id']}")
    ids.add(r["id"])
    oids = [o["id"] for o in r["options"]]
    if len(set(oids)) != len(oids): problems.append(f"row {r['id']}: repeated option ids")
    if r.get("default") not in oids: problems.append(f"row {r['id']}: default must be one of its options")
    if sum(1 for o in r["options"] if o.get("pick")) > 1: problems.append(f"row {r['id']}: more than one 'Our pick'")
    if r.get("tab") not in [t["id"] for t in P["tabs"]]: problems.append(f"row {r['id']}: unknown tab")
    for o in r["options"]:
        fragment(o)
        if "captions" in o: captions(o)

# ---- plain words: no internal labels in anything the creator reads (same rule as the decision pages) ----
CODE = re.compile(r"\b[A-Z]{1,2}\d{1,2}\b"); OK = {"4K", "EP"} | set(P.get("allowWords", []))
def readable():
    yield P.get("heading", ""); yield P.get("lede", "")
    for t in P["tabs"]: yield t["name"]; yield t.get("ask", "")
    for r in P["rows"]:
        yield r["name"]; yield r.get("short", ""); yield r.get("ask", "")
        for o in r["options"]: yield o["name"]; yield o.get("feel", ""); yield o.get("why", "")
for t in readable():
    for m in CODE.finditer(t or ""):
        if m.group(0) not in OK: problems.append(f"internal label '{m.group(0)}' in: {t[:70]}")
    if re.search(r"\b[a-z0-9]+_[a-z0-9_]+\b", t or ""): problems.append(f"slug-like word in: {t[:70]}")
if only:
    ids = {r["id"] for r in P["rows"]}
    problems += [f"--only: no row '{x}'" for x in only if x not in ids]
if problems: sys.exit("build.py: " + "\n  ".join(problems))

spec = {k: P[k] for k in ("video", "store", "tabs", "rows") if k in P}
spec.update({k: P[k] for k in ("heading", "lede", "watchNote", "locked") if k in P})
spec["round"] = P.get("round", 1); spec["base"] = base
if only: spec["only"] = only

if out.exists(): shutil.rmtree(out)
out.mkdir(parents=True)
for d in ("assets", "fonts"):
    if (hf / d).exists(): shutil.copytree(hf / d, out / d)
(out / "spec.json").write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
page = (here / "picker.html").read_text(encoding="utf-8")
page = page.replace("__TITLE__", html.escape(P.get("title", "Live picker")))
page = page.replace("__PLAYER__", f"https://cdn.jsdelivr.net/npm/@hyperframes/player@{P['hyperframes']}/dist/hyperframes-player.global.js")
page = page.replace("/*COMPOSE*/", (here / "compose.js").read_text(encoding="utf-8"))
page = page.replace("/*SPEC*/{}", json.dumps(spec, ensure_ascii=False).replace("</", "<\\/"))
(out / "index.html").write_text(page, encoding="utf-8")
files = sorted(str(f.relative_to(out)).replace("\\", "/") for f in out.rglob("*") if f.is_file() and f.name not in ("index.html", "spec.json"))
size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file())
print(f"wrote {out / 'index.html'} · {len(P['rows'])} rows · {sum(len(r['options']) for r in P['rows'])} options · {size // 1024} KB")
print("publish files:", json.dumps(files))
