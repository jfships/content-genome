#!/usr/bin/env python3
"""Regenerate the example page JSONs in examples/ (demo creator: Wren, a dog groomer in Austin).
Run from page-template/: python3 gen_examples.py && cd examples && for f in *.json; do python3 ../build.py $f out/${f%.json}.html; done
Images are referenced as img/<benchmark file> and img/looks/<slug>.jpg next to the built page."""
import json, pathlib
EX = pathlib.Path(__file__).parent / "examples"; EX.mkdir(exist_ok=True)
# Where each example sits in the journey (page-template/journey.json): round -> (stage, stepId, part)
PLACE_IN = {
 "footage-looks-tiles": ("look", "color-editing", "1 of 2"), "footage-looks-pick": ("look", "color-editing", "2 of 2"),
 "footage-filters": ("look", "scene-filters", ""), "made-scenes": ("look", "art-styles", ""),
 "palette-tiles": ("look", "palette", "1 of 2"), "change-palette-tiles": ("look", "palette", "1 of 2"), "palette-compare": ("look", "palette", "2 of 2"),
 "fonts-tiles": ("look", "fonts", "1 of 2"), "font-sets": ("look", "fonts", "2 of 2"),
 "text-style-tiles": ("look", "text-style", "1 of 2"), "text-style-pick": ("look", "text-style", "2 of 2"),
 "captions-tiles": ("look", "captions", "1 of 2"), "captions-pick": ("look", "captions", "2 of 2"),
 "backdrops": ("look", "backdrops", ""), "moments-library": ("look", "extras", ""), "break-from-reality": ("look", "break-from-reality", ""),
 "motion-entrances": ("movement", "motion-feel", ""), "scene-changes": ("movement", "scene-changes", ""),
 "music": ("sound", "music", ""),
 "wordmark-tiles": ("kit", "wordmark", "1 of 2"), "wordmark-pick": ("kit", "wordmark", "2 of 2"),
 "name-tag-tiles": ("kit", "name-tag", "1 of 2"), "name-tag-pick": ("kit", "name-tag", "2 of 2"),
 "series-tag-tiles": ("kit", "series-tag", "1 of 2"), "series-tag-pick": ("kit", "series-tag", "2 of 2"),
 "sting-tiles": ("kit", "sting", "1 of 2"), "sting-pick": ("kit", "sting", "2 of 2"),
 "sound-logo-tiles": ("kit", "sound-logo", "1 of 2"), "sound-logo-pick": ("kit", "sound-logo", "2 of 2"),
 "close-out": ("kit", "close-out", ""),
 "profile-picture-tiles": ("kit", "profile-picture", "1 of 2"), "profile-picture-pick": ("kit", "profile-picture", "2 of 2"),
 "banner-tiles": ("kit", "banner", "1 of 2"), "banner-pick": ("kit", "banner", "2 of 2"),
 "vertical-layouts": ("vertical", "vertical-layouts", "")}
NICHE = ["dog", "groom", "poodle", "coat", "matted", "mats", "dryer", "clipper", "fur", "paw", "leash", "bark"]   # Wren's niche: never in option copy
LABELS = {"no": "Discard", "keep": "Keep in library"}
def _fix(d):
    for b in d.get("buttons", []) or []:
        if b.get("value") in LABELS: b["label"] = LABELS[b["value"]]
    for sec in d.get("sections", []) or []: _fix(sec)
# one recommendation per option set (Principle 3) on the library examples that don't mark one inline
PICKS = {"music": ("lofi", "Relaxed under talking, and it never fights your voice."), "scene-changes": ("dissolve", "Calm and invisible; it fits most cuts."),
         "moments-library": ("callout", "The extra most videos need: pointing at one detail."), "break-from-reality": ("nature-doc", "Gentle and funny; it suits how you talk."),
         "close-out": None, "vertical-layouts": None}
def _mark_pick(name, d):
    if not PICKS.get(name): return
    oid, why = PICKS[name]
    for sec in (d.get("sections") or [{"options": d.get("options") or []}]):
        for o in sec.get("options", []):
            if o["id"] == oid: o.update({"pick": True, "why": why})
def W(name, d):
    _mark_pick(name, d)
    if name in PLACE_IN:
        st, sid, part = PLACE_IN[name]; d.pop("step", None)
        d.update({"stage": st, "stepId": sid, "journeyIf": ["vertical"], "nicheWords": NICHE})
        if part: d["part"] = part
    _fix(d)
    d.pop("step", None); d.pop("mainWord", None)
    (EX / (name + ".json")).write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
FACE = "img/01-desk-talking.jpg"; HANDS = "img/05-vanity.jpg"; PLACE = "img/06-shop-counter.jpg"
P = ["#F4FBF7", "#13302A", "#2EC4A6", "#FFD166", "#E8F3EE"]   # Wren's palette: background, words, pop color, second color, pale
BG, TX, HL, EX2, LT = P
ROLES = ["background", "words", "pop color", "second color", "pale"]
TITLE = "'Bebas Neue',Impact,sans-serif"; TEXT = "'Inter',Arial,sans-serif"; NOTES = "'Caveat',cursive"; MONO = "'Space Mono',monospace"
SAY_PERSONA = "Wren"
# Page copy rules: the title names the thing in plain words; ONE short line under it; nothing else
# above the cards (no say/note). The section rule line says what the buttons allow. One decision type per page.
# Standard sample words on every picker mock (fonts, colors, words on video, captions, motion, backdrops).
# The same for every creator, whatever their field. Never rewrite them for the creator. Only NAME_TAG is personal.
# Use-when lines under cards are universal moments too ("For: a flashback"); the creator's niche stays in chat.
TITLE_LINES = ("I TRIED IT", "FOR 30 DAYS")            # the sample title, split where a two-line title breaks
SAMPLE_TEXT = "Here's what actually happened."
SAMPLE_LABEL = "Day 1 vs Day 30"
SAMPLE_CAPTION = "and that's the part nobody tells you"
SAMPLE_LIST = ["1 · Week one", "2 · The hard part", "3 · The result"]
SAMPLE_TITLE = " ".join(TITLE_LINES)
NAME_TAG = "Wren · Austin"                             # the sample name tag
PHOTO_TAG = "Test photo"   # small tag on every benchmark image, instead of a paragraph about test photos
IMGS = [FACE, HANDS, PLACE]
# Words never sit on a face. When a mock puts text over the face photo, reframe it: zoom 1.25x and keep the left
# 80%, so the speaker sits right of center and the words take the clear space on the left (the window side).
FRAMED = "position:absolute;left:0;top:-8%;width:125%;height:125%;object-fit:cover;object-position:left center"


# ---------- the shared finalist flow (voting-pages.md): finalists (tiles) -> pick (Main / Backup / Alternative / Discard) ----------
FIN_RULE = "mark as many finalists as you like. Next, you'll pick a main and a backup from them, and keep any others as alternatives."
FIN_BTN = [{"value": "yes", "label": "Finalist"}, {"value": "no", "label": "Discard"}]
PICK_BTN = [{"value": "pick", "label": "Main"}, {"value": "backup", "label": "Backup"}, {"value": "alt", "label": "Alternative"}, {"value": "no", "label": "Discard"}]
def finalist_flow(base, title, what, options, fin, nxt, fonts, head="", aspect=None, pick_aspect=None, control=None, tiles_extra=None, pick_what="Your finalists, large.", photo_tag=None):
    """options: list of option dicts (id, name, line, html|images, play...). fin: the example's finalist ids, in order."""
    common = {"fonts": fonts, **({"head": head} if head else {}), **({"photoTag": photo_tag} if photo_tag else {})}
    tiles = {"round": base + "-tiles", "kind": "finalists", "layout": "tiles", **common, **({"aspect": aspect} if aspect else {}),
      "title": title, "what": what, "rule": FIN_RULE, "keepWord": "finalist|finalists", "trimAbove": 6,
      "buttons": FIN_BTN, "keepValues": ["yes"], "next": "Next: your finalists, large. You'll pick a main and a backup.", "persona": SAY_PERSONA,
      "options": ([control] if control else []) + options}
    if tiles_extra: tiles.update(tiles_extra)
    W(base + "-tiles", tiles)
    big = [dict(o) for o in options if o["id"] in fin]   # the recommendation (pick + why) carries over when it's a finalist
    big.sort(key=lambda o: fin.index(o["id"]))
    W(base + "-pick", {"round": base + "-pick", "kind": "fixed", **common, **({"aspect": pick_aspect or aspect} if (pick_aspect or aspect) else {}),
      "title": title + ": your finalists", "what": pick_what,
      "single": "pick", "singleFallback": "backup", "altValue": "alt", "keepValues": ["pick", "backup", "alt"],
      "buttons": PICK_BTN, "next": nxt, "persona": SAY_PERSONA, "options": big})

# ---------- 1. color editing: finalists -> pick (Main / Backup / Alternative) ----------
def look(id, name, line, css, overlay=None, **kw):
    o = {"id": id, "name": name, "line": line, "images": IMGS, "css": css}
    if overlay: o["overlay"] = overlay
    o.update(kw); return o
LOOKS = [
 look("clean-bright", "Clean & bright", "Fresh and true to life.", "contrast(1.06) saturate(1.08) brightness(1.04)", pick=True, why="Bright and clean, true to how things really look."),
 look("warm-film", "Warm film", "Golden and soft.", "sepia(.22) saturate(1.15) contrast(.97) brightness(1.02)", "background:rgba(255,170,80,.12);mix-blend-mode:soft-light"),
 look("pastel", "Pastel", "Light, gentle colors.", "saturate(.7) brightness(1.1) contrast(.9)", "background:rgba(255,230,240,.12)"),
 look("punchy", "Punchy", "Strong colors and contrast.", "saturate(1.55) contrast(1.2)"),
 look("teal-orange", "Teal & orange", "Warm skin, cool shadows.", "saturate(1.25) contrast(1.12)", "background:linear-gradient(rgba(0,120,140,.35),rgba(0,120,140,.35));mix-blend-mode:screen;opacity:.45"),
 look("sun-flare", "Sun flare", "A warm glow from one corner.", "saturate(1.1) brightness(1.03)", "background:radial-gradient(circle at 85% 10%,rgba(255,200,120,.75),rgba(255,200,120,0) 55%);mix-blend-mode:screen"),
 look("portra", "Soft film", "Warm, a little faded, fine grain.", "contrast(.92) saturate(.92) brightness(1.04) sepia(.1)", "background:rgba(255,220,200,.10)"),
 look("cool-clean", "Cool & crisp", "Clean with a cool, modern edge.", "saturate(.95) contrast(1.1) brightness(1.02) hue-rotate(-6deg)", "background:rgba(120,170,230,.12);mix-blend-mode:soft-light"),
 look("matte", "Soft & faded", "Calm colors, nothing harsh.", "contrast(.85) saturate(.8) brightness(1.06)"),
 look("rich", "Rich & deep", "Deep shadows, rich color.", "contrast(1.22) saturate(1.2) brightness(.95)")]
finalist_flow("footage-looks", "Color editing", "Color optimization of your raw footage.", LOOKS,
 ["clean-bright", "warm-film", "portra", "cool-clean"], "Next: filters for specific scenes.", [],
 control={"id": "as-shot", "name": "As shot", "line": "No editing. Here so you can compare.", "images": IMGS, "control": True},
 photo_tag=PHOTO_TAG, pick_what="Your finalists, large, on the same three test photos.")

# ---------- 2. filters for specific scenes (library) ----------
# Every card shows exactly what its name promises: the color AND the overlay that makes the filter recognizable
# (letterbox bars, a camcorder's PLAY and date, CAM 01 and REC, a scope mask, a real heat ramp), on a frame that
# suits it (tiny world needs a high, wide shot; fake night needs a scene with lights). Built as code over the photos.
STREET = "img/08-street-vlog.jpg"; HIGH = "img/12-high-street.jpg"
def svgf(fid, body):   # an inline SVG filter, used by CSS filter:url(#fid) on the images of one card
    return f'<svg width="0" height="0" style="position:absolute"><filter id="{fid}" color-interpolation-filters="sRGB">{body}</filter></svg>'
LUMA = '<feColorMatrix type="matrix" values=".3 .59 .11 0 0  .3 .59 .11 0 0  .3 .59 .11 0 0  0 0 0 1 0"/>'
def ramp(r, g, b): return f'<feComponentTransfer><feFuncR type="table" tableValues="{r}"/><feFuncG type="table" tableValues="{g}"/><feFuncB type="table" tableValues="{b}"/></feComponentTransfer>'
def panel(img, css, layers="", pos="center"):
    return (f'<div style="position:relative;overflow:hidden;container-type:size;background:#000">'
            f'<img src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};filter:{css}">{layers}</div>')
def fcard(imgs, css, layers=lambda i: "", defs="", pos=("50% 30%", "center", "center")):
    a, b, c = imgs
    return (defs + f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1.55fr 1fr;grid-template-rows:1fr 1fr;gap:2px;background:#000">'
            f'<div style="grid-row:1/3;display:grid">{panel(a, css, layers(0), pos[0])}</div><div style="display:grid">{panel(b, css, layers(1), pos[1])}</div><div style="display:grid">{panel(c, css, layers(2), pos[2])}</div></div>')
def one(img, css, layers="", defs="", pos="center"):
    return defs + f'<div style="position:absolute;inset:0;display:grid">{panel(img, css, layers, pos)}</div>'
VT = "'VT323','Space Mono',monospace"
VIG = lambda k=.65: f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 45%,rgba(0,0,0,{k}) 100%)"></div>'
GRAIN = '<div style="position:absolute;inset:0;opacity:.18;background:repeating-radial-gradient(circle at 13% 27%,#fff 0 .5px,transparent .5px 2px),repeating-radial-gradient(circle at 71% 63%,#000 0 .5px,transparent .5px 2.4px)"></div>'
LETTERBOX = '<div style="position:absolute;left:0;right:0;top:0;height:13%;background:#000"></div><div style="position:absolute;left:0;right:0;bottom:0;height:13%;background:#000"></div>'
def vhs_l(i):
    big = i == 0
    return ('<div style="position:absolute;inset:0;background:repeating-linear-gradient(rgba(0,0,0,.22) 0 1px,transparent 1px 3px)"></div>'
            '<div style="position:absolute;left:0;right:0;top:62%;height:5%;background:linear-gradient(90deg,rgba(255,255,255,.35),rgba(255,255,255,.05) 30%,rgba(255,255,255,.4) 60%,rgba(255,255,255,.1));filter:blur(1px)"></div>'
            + (f'<div style="position:absolute;left:5%;top:6%;font:400 9cqw/1 {VT};color:#fff;text-shadow:.4cqw 0 #f33,-.4cqw 0 #3ff">PLAY ▶</div>'
               f'<div style="position:absolute;left:5%;bottom:7%;font:400 7cqw/1.05 {VT};color:#fff;text-shadow:.4cqw 0 #f33,-.4cqw 0 #3ff">SEP 12 2026<br>10:42 PM</div>' if big else
               f'<div style="position:absolute;right:5%;bottom:6%;font:400 12cqw/1 {VT};color:#fff">0:42:17</div>'))
def cam_l(i):
    return (VIG(.75) + '<div style="position:absolute;inset:0;opacity:.25;background:repeating-linear-gradient(rgba(255,255,255,.4) 0 1px,transparent 1px 2px)"></div>'
            f'<div style="position:absolute;left:4%;top:5%;font:400 {9 if i == 0 else 13}cqw/1 {VT};color:#fff">CAM 0{i+1}</div>'
            f'<div style="position:absolute;right:4%;top:5%;display:flex;align-items:center;gap:1.4cqw;font:400 {9 if i == 0 else 13}cqw/1 {VT};color:#fff"><i style="width:{3 if i == 0 else 5}cqw;height:{3 if i == 0 else 5}cqw;border-radius:50%;background:#f22;display:block"></i>REC</div>'
            + (f'<div style="position:absolute;left:4%;bottom:5%;font:400 7cqw/1 {VT};color:#fff">2026-09-12 23:14:07</div>' if i == 0 else ''))
SCOPE = '<svg viewBox="0 0 160 90" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%"><defs><mask id="__M"><rect width="160" height="90" fill="#fff"/><circle cx="58" cy="45" r="34" fill="#000"/><circle cx="102" cy="45" r="34" fill="#000"/></mask></defs><rect width="160" height="90" fill="#000" mask="url(#__M)"/></svg>'
BLINDS = '<div style="position:absolute;inset:-20%;transform:rotate(-14deg);background:repeating-linear-gradient(0deg,rgba(0,0,0,.62) 0 5.5%,transparent 5.5% 11%)"></div>'
def glitch_l(img, pos):
    sl = lambda top, h, dx, f: f'<div style="position:absolute;inset:0;clip-path:inset({top}% 0 {100-top-h}% 0);transform:translateX({dx}%)"><img src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};filter:{f}"></div>'
    return (f'<div style="position:absolute;inset:0;transform:translateX(-1.6%);mix-blend-mode:screen;opacity:.75"><img src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};filter:url(#flt-red)"></div>'
            f'<div style="position:absolute;inset:0;transform:translateX(1.6%);mix-blend-mode:screen;opacity:.75"><img src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};filter:url(#flt-cyan)"></div>'
            + sl(18, 7, 7, "saturate(2)") + sl(46, 4, -9, "hue-rotate(90deg) saturate(2)") + sl(71, 9, 5, "invert(1)")
            + '<div style="position:absolute;left:62%;top:30%;width:9%;height:8%;background:#0f0;mix-blend-mode:difference"></div><div style="position:absolute;left:12%;top:58%;width:14%;height:5%;background:#f0f;mix-blend-mode:difference"></div><div style="position:absolute;left:40%;top:83%;width:7%;height:6%;background:#0ff;mix-blend-mode:difference"></div>')
DITHER = svgf("flt-1bit", LUMA + '<feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="1" seed="3" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 1" result="n2"/><feComposite in="SourceGraphic" in2="n" operator="arithmetic" k1="0" k2="1" k3=".55" k4="-.3"/>' + LUMA + ramp("0 1", "0 1", "0 1").replace('type="table"', 'type="discrete"'))
FDEFS = (svgf("flt-heat", LUMA + ramp(".04 .30 .62 .92 1 1 1", "0 0 0 .1 .55 .9 1", ".30 .62 .72 .32 0 .1 .95"))
         + svgf("flt-nv", LUMA + ramp("0 .15 .55", ".04 .55 1", "0 .12 .5").replace("</feComponentTransfer>", "</feComponentTransfer>").replace("<feComponentTransfer>", '<feComponentTransfer result="g">') + '<feTurbulence type="fractalNoise" baseFrequency=".9" seed="7" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0  .3 .3 .3 0 0  0 0 0 0 0  0 0 0 .35 0" result="n2"/><feBlend in="g" in2="n2" mode="screen"/>')
         + svgf("flt-ir", '<feColorMatrix type="matrix" values=".45 .95 0 0 0  .55 .15 0 0 0  .1 .55 .45 0 0  0 0 0 1 0"/>')
         + svgf("flt-cyano", LUMA + ramp(".04 .96", ".16 .94", ".39 .90"))
         + svgf("flt-xproc", ramp("0 .1 .75 1", ".08 .5 1 1", ".35 .42 .3 .55"))
         + svgf("flt-red", LUMA + ramp("0 1", "0 0", "0 0")) + svgf("flt-cyan", LUMA + ramp("0 0", "0 1", "0 1"))
         + DITHER)
NIGHT_LIGHTS = lambda img, pos: f'<img src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};filter:brightness(1.6) contrast(5) saturate(1.4);mix-blend-mode:screen;opacity:.85">'
def tiny_l():
    blur = lambda m: f'<div style="position:absolute;inset:0;-webkit-mask-image:{m};mask-image:{m}"><img src="{HIGH}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:blur(4px) saturate(1.5) contrast(1.15)"></div>'
    return blur("linear-gradient(#000 0,#000 18%,transparent 42%,transparent 62%,#000 86%)")
FILTERS = [  # id, name, line, card html
 ("faded-memory", "Faded memory", "For: a flashback", fcard(IMGS, "contrast(.78) brightness(1.12) saturate(.6) sepia(.25) blur(.4px)", lambda i: '<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 40%,rgba(255,244,225,.85) 100%)"></div>')),
 ("black-white", "Black & white", "For: the \"before\" in a before-and-after", fcard(IMGS, "grayscale(1) contrast(1.02) brightness(1.04)")),
 ("noir", "Noir", "For: a mystery or a dramatic reveal", fcard(IMGS, "grayscale(1) contrast(1.75) brightness(.82)", lambda i: BLINDS + VIG(.85))),
 ("one-bit", "Black & white dots", "For: a retro computer joke", fcard(IMGS, "url(#flt-1bit)")),
 ("old-photo", "Old photograph", "For: \"back in my day\"", fcard(IMGS, "sepia(.9) contrast(1.05) brightness(.95) saturate(.8)", lambda i: VIG(.7) + GRAIN + '<div style="position:absolute;left:30%;top:0;bottom:0;width:1px;background:rgba(255,255,255,.35)"></div><div style="position:absolute;left:68%;top:0;bottom:30%;width:1px;background:rgba(255,255,255,.25)"></div>')),
 ("movie-trailer", "Movie trailer", "For: a dramatic intro", fcard(IMGS, "saturate(1.3) contrast(1.2)", lambda i: '<div style="position:absolute;inset:0;background:linear-gradient(rgba(0,110,130,.38),rgba(255,140,60,.2));mix-blend-mode:overlay"></div>' + LETTERBOX)),
 ("vhs", "VHS tape", "For: a blooper or an old clip", fcard(IMGS, "saturate(1.4) contrast(1.05) blur(.6px)", vhs_l), {"houseExempt": True}),
 ("security-cam", "Security camera", "For: \"caught in the act\"", fcard(IMGS, "grayscale(.85) sepia(.35) hue-rotate(50deg) contrast(1.35) brightness(.95) blur(.5px)", cam_l), {"houseExempt": True}),
 ("night-vision", "Night vision", "For: sneaking around at night", one(PLACE, "url(#flt-nv) brightness(1.1)", GRAIN + SCOPE.replace("__M", "nvm"))),
 ("heat-map", "Heat map", "For: \"things are heating up\"", fcard(IMGS, "url(#flt-heat)")),
 ("fake-night", "Fake night", "For: a late-night scene shot in daylight", one(STREET, "brightness(.45) saturate(.5) contrast(1.2)", '<div style="position:absolute;inset:0;background:#0b2350;mix-blend-mode:color;opacity:.75"></div>' + NIGHT_LIGHTS(STREET, "center") + VIG(.6))),
 ("tiny-world", "Tiny world", "For: making a place look like a toy model", one(HIGH, "saturate(1.5) contrast(1.15) brightness(1.05)", tiny_l())),
 ("glitch", "Glitch", "For: something going wrong", one(FACE, "contrast(1.1)", glitch_l(FACE, "50% 30%"), pos="50% 30%")),
 ("cross-process", "Odd colors", "For: something strange or dreamy", fcard(IMGS, "url(#flt-xproc) contrast(1.2) saturate(1.4)")),
 ("negative", "X-ray", "For: \"let's look inside\"", fcard(IMGS, "invert(1) grayscale(.6) contrast(1.2)", lambda i: '<div style="position:absolute;inset:0;background:rgba(40,120,255,.35);mix-blend-mode:color"></div>')),
 ("blueprint-blue", "Blueprint blue", "For: explaining how something works", fcard(IMGS, "url(#flt-cyano) contrast(1.1)")),
 ("golden-glow", "Golden glow", "For: a happy ending", fcard(IMGS, "sepia(.3) saturate(1.3) brightness(1.08)", lambda i: '<div style="position:absolute;inset:0;background:radial-gradient(circle at 78% 18%,rgba(255,200,110,.85),transparent 60%);mix-blend-mode:screen"></div>')),
 ("super8", "Home movie", "For: a childhood memory", fcard(IMGS, "sepia(.35) saturate(1.2) contrast(1.05) blur(.5px)", lambda i: GRAIN + '<div style="position:absolute;inset:0;border-radius:9%;box-shadow:0 0 0 30cqw #000"></div>')),
 ("instant-photo", "Instant photo", "For: a snapshot moment", fcard(IMGS, "contrast(.9) saturate(.85) brightness(1.08) sepia(.15)", lambda i: '<div style="position:absolute;inset:0;border:solid #f6f3ec;border-width:5cqw 5cqw 16cqw"></div>')),
 ("newsprint", "Newsprint", "For: a \"breaking news\" joke", fcard(IMGS, "grayscale(1) contrast(1.6) brightness(1.08)", lambda i: '<div style="position:absolute;inset:0;background:radial-gradient(circle,rgba(0,0,0,.55) 1px,transparent 1.6px) 0 0/5px 5px;mix-blend-mode:multiply"></div><div style="position:absolute;inset:0;background:#efe6cf;mix-blend-mode:multiply"></div>')),
 ("low-key", "Moody dark", "For: a serious moment", fcard(IMGS, "brightness(.7) contrast(1.4) saturate(.9)", lambda i: VIG(.85))),
 ("infrared", "Infrared pink", "For: a strange, other-world moment", fcard(IMGS, "url(#flt-ir) saturate(1.5) contrast(1.1)"))]
W("footage-filters", {
 "round": "footage-filters", "kind": "library", "layout": "tiles", "photoTag": PHOTO_TAG, "keepWord": "filter|filters", "fonts": ["vt323"],
 "title": "Filters for specific scenes",
 "what": "Short color changes for one scene, like a flashback, a before-and-after or a joke.",
 "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "keepValues": ["keep"],
 "next": "Next: art styles for scenes you can't film.", "persona": SAY_PERSONA,
 "options": [{"id": f[0], "name": f[1], "line": f[2], "html": (FDEFS if "url(#" in f[3] else "") + f[3], **(f[4] if len(f) > 4 else {}), **({"pick": True, "why": "A flashback is the moment most videos need first."} if f[0] == "faded-memory" else {})} for f in FILTERS]})

# ---------- 2. made scenes ----------
looks = [("watercolor", "Watercolor", "For: a soft memory"),
 ("pencil", "Pencil sketch", "For: explaining how something works"),
 ("pop-comic", "Pop comic", "For: a dramatic \"before\""),
 ("paper-diorama", "Paper diorama", "For: a \"what if\""),
 ("claymation", "Claymation", "For: a joke"),
 ("blueprint", "Blueprint", "For: a plan or a build"),
 ("chalkboard", "Chalkboard", "For: prices and numbers"),
 ("toy-bricks", "Toy bricks", "For: a silly rebuild")]
W("made-scenes", {
 "round": "made-scenes", "kind": "library", "layout": "tiles", "keepWord": "art style|art styles", "photoTag": "Test scene",
 "title": "Art styles for scenes you can't film",
 "what": "A generated picture for imaginary scenes: a flashback, a what-if.",
 "next": "Next: your color palette.", "persona": SAY_PERSONA,
 "sections": [{"id": "moments", "title": "", "line": "", "kind": "library", "keepWord": "art style|art styles",
   "keepValues": ["keep"], "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}],
   "options": [{"id": s, "name": n, "line": l, "images": [f"img/looks/{s}.jpg"], **({"pick": True, "why": "Soft and warm; it suits the before-and-after stories you told me."} if s == "watercolor" else {})} for s, n, l in looks]}]})

# ---------- 3a. palette tiles ----------
pals = [("fresh-mint", "Fresh mint", P, True, "Clean and friendly, like your shop on a good morning."),
 ("warm-clay", "Warm clay", ["#F6EFE6", "#3A2A22", "#C96A3B", "#E9C46A", "#D9CBB8"], False, None),
 ("midnight-lime", "Midnight lime", ["#0F1115", "#F2F2F2", "#C7F464", "#5B5F6B", "#1C1F26"], False, None),
 ("paper-ink", "Paper & ink", ["#FAF7F0", "#1A1A1A", "#D62828", "#8A8A8A", "#EDE8DC"], False, None),
 ("sky-coral", "Sky & coral", ["#EAF4FF", "#143055", "#FF6B6B", "#4D96FF", "#D6E6F7"], False, None),
 ("forest", "Forest", ["#1E2D24", "#F1F5EE", "#9CCB7A", "#E0B458", "#2C4034"], False, None),
 ("candy", "Candy", ["#FFF3F8", "#2B1B2F", "#FF4FA3", "#7C4DFF", "#FFD6EA"], False, None),
 ("sand-navy", "Sand & navy", ["#F0E9DC", "#1B2A49", "#C8A24A", "#3E5C76", "#E2D8C4"], False, None),
 ("peach", "Peach cream", ["#FFF1E6", "#4A2C2A", "#FF8C61", "#FFC09F", "#FFE3D1"], False, None),
 ("slate", "Slate & ember", ["#2A2F36", "#F5F5F5", "#FF7A1A", "#8C96A3", "#3A414A"], False, None),
 ("lavender", "Lavender", ["#F3F0FA", "#2E2740", "#8E6CF2", "#B8A9F0", "#E6E0F6"], False, None),
 ("tomato", "Tomato & cream", ["#FFF8F0", "#2B1A14", "#E63946", "#F4A261", "#FBE4D2"], False, None)]
def pmock(c, img=FACE):
    bg, tx, ac, ex, lt = c
    return (f'<svg viewBox="0 0 320 180" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"><image href="{img}" x="0" y="-22" width="400" height="225" preserveAspectRatio="xMinYMid slice"/>'
            f'<rect width="320" height="180" fill="{bg}" opacity=".3"/><rect x="14" y="20" width="112" height="30" fill="{ac}"/><text x="22" y="43" font-family="Bebas Neue,Impact,sans-serif" font-size="24" fill="{bg}">{TITLE_LINES[0]}</text>'
            f'<rect x="14" y="56" width="124" height="30" fill="{bg}"/><text x="22" y="79" font-family="Bebas Neue,Impact,sans-serif" font-size="24" fill="{tx}">{TITLE_LINES[1]}</text>'
            f'<rect x="14" y="146" width="118" height="22" rx="3" fill="{tx}"/><text x="22" y="161" font-family="Inter,Arial,sans-serif" font-size="11" fill="{bg}">{NAME_TAG}</text>'
            f'<rect x="212" y="150" width="94" height="18" rx="9" fill="{ex}"/><text x="226" y="163" font-family="Inter,Arial,sans-serif" font-size="10" fill="{tx}">EP 1</text></svg>')
W("palette-tiles", {
 "round": "palette-tiles", "photoTag": PHOTO_TAG, "kind": "finalists", "keepWord": "finalist|finalists", "layout": "tiles", "fonts": ["bebas-neue", "inter"],
 "title": "Color palette",
 "what": "The colors on your titles, name tags, thumbnails and channel page.",
 "rule": "mark as many finalists as you like. Next, you'll compare them side by side.",
 "trimAbove": 6, "buttons": [{"value": "yes", "label": "Finalist"}, {"value": "no", "label": "Discard"}], "keepValues": ["yes"],
 "next": "Next: your finalists, large and side by side. You'll pick one.", "persona": SAY_PERSONA,
 "options": [{"id": s, "name": n, "html": pmock(c), "swatches": [{"hex": h, "role": r} for h, r in zip(c, ROLES)], **({"pick": True, "why": why} if pk else {})} for s, n, c, pk, why in pals]})

# ---------- 3b. palette compare ----------
def SAMPLE_TITLE_HTML(ac, bg):
    first, rest = TITLE_LINES[1].split(" ", 1)
    return f'{TITLE_LINES[0]} {first} <span style="background:{ac};color:{bg};padding:0 6px;white-space:nowrap">{rest}</span>'
def pbig(c):
    bg, tx, ac, ex, lt = c
    return (f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:3px;background:#000">'
            f'<div style="grid-row:1/3;position:relative;overflow:hidden;background:{lt};display:flex;align-items:center;padding:0 6px"><div style="position:relative;width:100%;aspect-ratio:16/9;box-shadow:0 2px 10px rgba(0,0,0,.25)">{pmock(c, FACE).replace("width=\"100%\" height=\"100%\"", "style=\"position:absolute;inset:0;width:100%;height:100%\"")}</div></div>'
            f'<div style="background:{bg};display:flex;flex-direction:column;justify-content:center;padding:6%;gap:6px"><div style="font:400 26px/1.15 {TITLE};color:{tx}">{SAMPLE_TITLE_HTML(ac, bg)}</div><div style="font:12px {TEXT};color:{tx};opacity:.7">Title card</div></div>'
            f'<div style="background:{tx};display:flex;align-items:flex-end;padding:6%;position:relative"><img src="{FACE}" style="{FRAMED};opacity:.85"><div style="position:relative;background:{bg};color:{tx};font:600 12px {TEXT};padding:5px 9px;border-left:4px solid {ac}">{NAME_TAG}</div></div></div>')
fin = [p for p in pals if p[0] in ("fresh-mint", "sky-coral", "paper-ink", "forest")]
W("palette-compare", {
 "round": "palette-compare", "kind": "fixed", "fonts": ["bebas-neue", "inter"],
 "title": "Color palette: your finalists",
 "what": "Each finalist on a thumbnail, a title card and a name tag.",
 "single": "pick", "singleFallback": "",
 "buttons": [{"value": "pick", "label": "This one"}, {"value": "no", "label": "Discard"}], "keepValues": ["pick"],
 "next": "Next: fonts. (Your color editing gets tuned to your palette automatically.)", "persona": SAY_PERSONA,
 "options": [{"id": s, "name": n, "html": pbig(c), "swatches": [{"hex": h, "role": r} for h, r in zip(c, ROLES)], **({"pick": True, "why": why} if pk else {})} for s, n, c, pk, why in fin]})

# ---------- 5a. fonts: finalists per job (every bundled font for that job: 20-30 tiles each) ----------
# Each font's sample is scaled by its `scale` in fonts/fonts.json, so wide fonts fit and swapped fonts never overlap.
FMAN = {k: v for k, v in json.loads((pathlib.Path(__file__).parent / "fonts" / "fonts.json").read_text(encoding="utf-8")).items() if not k.startswith("_")}
GENERIC = {"title": "Impact,sans-serif", "text": "Arial,sans-serif", "notes": "cursive"}
def fcss(slug, job):   # the CSS a slot gets: family, weight and the width scale as --fs
    m = FMAN[slug]
    return f"'{m['family']}',{GENERIC[job]};font-weight:{m['weight']};--fs:{m['scale']}"
TIER_ORDER = {"C": 0, "R": 1, "F": 2}
FONTS = {job: [(s, m["family"], fcss(s, job)) for s, m in sorted(FMAN.items(), key=lambda kv: (TIER_ORDER[kv[1]["tier"]], kv[1]["family"])) if job in m["jobs"].split()] for job in ("title", "text", "notes")}
ALLF = sorted({s for job in FONTS.values() for s, _, _ in job})
def ftile(css, sample, size):
    return f'<div style="position:absolute;inset:0;background:{BG};display:flex;align-items:center;justify-content:center;padding:5%"><div style="font-family:{css};font-size:calc({size}px * var(--fs,1));line-height:1.2;color:{TX};text-align:center">{sample}</div></div>'
def fsec(id, title, sample, size):
    return {"id": id, "title": title, "line": "", "kind": "finalists", "keepWord": "finalist|finalists", "layout": "tiles", "aspect": "16/9", "keepValues": ["yes"],
            "buttons": [{"value": "yes", "label": "Finalist"}, {"value": "no", "label": "Discard"}], "movable": False, "trimAbove": 6,
            "options": [{"id": f"{id}-{s}", "name": n, "html": ftile(c, sample, size), **({"pick": True, "why": "Tall and clear; it fits a lot of words in a thumbnail."} if s == "bebas-neue" and id == "title" else {})} for s, n, c in FONTS[id]]}
W("fonts-tiles", {
 "round": "fonts-tiles", "kind": "finalists", "fonts": ALLF,
 "title": "Fonts",
 "what": "Fonts for big titles, regular text and small handwritten notes.",
 "rule": "mark as many finalists as you like in each group. Next, I'll combine your finalists into font sets over a sample clip.",
 "next": "Next: your finalists combined into sets, over a sample clip. You'll build one.", "persona": SAY_PERSONA,
 "sections": [fsec("title", "Big titles", "<br>".join(TITLE_LINES), 30), fsec("text", "Text", SAMPLE_TEXT, 19), fsec("notes", "Notes", "start here →", 30)]})

# ---------- 5b. font sets ----------
# the three small "Title / Text / Notes" labels tie each slot's picker to what it changes in the preview
PLAB = lambda s, pos: f'<span class="lab" style="{pos}">{s}</span>'
prev = (f'<img src="{FACE}" style="{FRAMED}"><div class="ov2" style="padding:5% 6%;display:flex;flex-direction:column;justify-content:space-between">'
        f'<div style="position:relative;padding-top:20px">{PLAB("Title", "left:0;top:0;bottom:auto")}<div style="display:inline-block;background:{HL};color:{BG};padding:4px 10px;font-family:{{{{title}}}};font-size:calc(28px * var(--fs,1));line-height:1.2">{TITLE_LINES[0]}</div><br>'
        f'<div style="display:inline-block;background:{BG};color:{TX};padding:4px 10px;margin-top:6px;font-family:{{{{title}}}};font-size:calc(28px * var(--fs,1));line-height:1.2">{TITLE_LINES[1]}</div></div>'
        f'<div style="display:flex;justify-content:space-between;align-items:flex-end"><div style="position:relative;padding-top:20px;max-width:60%">{PLAB("Text", "left:0;top:0;bottom:auto")}<div style="background:{BG};color:{TX};padding:6px 10px;font-family:{{{{text}}}};font-size:calc(15px * var(--fs,1));line-height:1.3">{SAMPLE_TEXT}</div></div>'
        f'<div style="position:relative;padding-top:20px">{PLAB("Notes", "left:auto;right:0;top:0;bottom:auto")}<div style="color:{EX2};font-family:{{{{notes}}}};font-size:calc(26px * var(--fs,1));line-height:1.2;transform:rotate(-6deg);text-shadow:0 1px 3px #000">start here →</div></div></div></div>')
FS_FIN = {"title": ["bebas-neue", "bowlby-one", "fraunces", "anton"], "text": ["inter", "lora", "dm-sans"], "notes": ["caveat", "permanent-marker", "special-elite"]}   # the example's finalists
ch = lambda job: [{"id": s, "name": n, "css": c} for s, n, c in FONTS[job] if s in FS_FIN[job]]
W("font-sets", {
 "round": "font-sets", "kind": "fixed", "mode": "sets", "fonts": sorted({x for v in FS_FIN.values() for x in v}),
 "title": "Font set",
 "what": "Your finalists combined into sets. Swap any font, then use the set you like.",
 "next": "Next: text style.", "persona": SAY_PERSONA,
 "slots": [{"id": "title", "label": "Title"}, {"id": "text", "label": "Text"}, {"id": "notes", "label": "Notes"}],
 "choices": {"title": ch("title"), "text": ch("text"), "notes": ch("notes")},
 "presets": [{"name": "Bold & friendly", "pick": True, "line": "Tall title, plain text, handwritten notes.", "picks": {"title": "bebas-neue", "text": "inter", "notes": "caveat"}},
  {"name": "Classic", "line": "Magazine-style title and text, typewriter notes.", "picks": {"title": "fraunces", "text": "lora", "notes": "special-elite"}},
  {"name": "Loud", "line": "Heavy title, clean text, marker notes.", "picks": {"title": "bowlby-one", "text": "dm-sans", "notes": "permanent-marker"}}],
 "preview": prev})

# ---------- 7. text style: finalists -> pick (Main / Backup / Alternative / Discard) ----------
# Static only: how text moves is Movement. Every option is drawn in the creator's font set and palette, over the
# reframed face photo (speaker right of center, words on the clear left side). Sizes in cqw so tiles and big cards match.
TS_T1, TS_T2 = TITLE_LINES
def ts(style):
    img = f'<img src="{FACE}" style="{FRAMED}">'
    W_ = 'position:absolute;inset:0;container-type:size;font-family:' + TITLE
    T = lambda css, inner: f'<div style="position:absolute;left:5%;top:9%;max-width:48%;{css}">{inner}</div>'
    Lb = lambda css, inner: f'<div style="position:absolute;left:5%;bottom:11%;{css}">{inner}</div>'
    lab_txt = SAMPLE_LABEL
    t2 = f'{TS_T1}<br>{TS_T2}'
    S = {
     "plain":     T('color:#fff;font-size:9cqw;line-height:1.02;text-shadow:0 .4cqw 1.6cqw rgba(0,0,0,.7)', t2) + Lb(f'color:#fff;font:600 3.6cqw {TEXT};text-shadow:0 .3cqw 1.2cqw rgba(0,0,0,.8)', lab_txt),
     "blocks":    T('font-size:8.5cqw;line-height:1.18', f'<span style="background:{HL};color:{BG};padding:0 1.6cqw;box-decoration-break:clone;-webkit-box-decoration-break:clone">{TS_T1}</span><br><span style="background:{BG};color:{TX};padding:0 1.6cqw">{TS_T2}</span>') + Lb(f'background:{BG};color:{TX};font:600 3.4cqw {TEXT};padding:.8cqw 1.8cqw', lab_txt),
     "highlighter": T(f'color:{TX};font-size:9cqw;line-height:1.08', f'<span style="background:linear-gradient(transparent 18%,{EX2} 18%,{EX2} 90%,transparent 90%);color:{TX};padding:0 1cqw">{TS_T1}</span><br><span style="background:linear-gradient(transparent 18%,{HL} 18%,{HL} 90%,transparent 90%);color:{TX};padding:0 1cqw">{TS_T2}</span>') + Lb(f'color:#fff;font:600 3.5cqw {TEXT};border-bottom:.6cqw solid {HL};padding-bottom:.4cqw;text-shadow:0 .2cqw .8cqw rgba(0,0,0,.7)', lab_txt),
     "outline":   T(f'color:transparent;-webkit-text-stroke:.35cqw #fff;font-size:10cqw;line-height:1', t2) + Lb(f'color:#fff;font:700 3.4cqw {TEXT};border:.35cqw solid #fff;padding:.6cqw 1.6cqw;border-radius:99px', lab_txt),
     "bar":       f'<div style="position:absolute;left:0;bottom:12%;background:{BG};border-left:1.6cqw solid {HL};padding:1.2cqw 3cqw 1.2cqw 4cqw;max-width:62%"><div style="font-size:6.6cqw;line-height:1;color:{TX}">{TS_T1} {TS_T2}</div><div style="font:600 3.2cqw {TEXT};color:{TX};opacity:.8;margin-top:.6cqw">{lab_txt}</div></div>',
     "pill":      T(f'color:#fff;font-size:9cqw;line-height:1.02;text-shadow:0 .3cqw 1.2cqw rgba(0,0,0,.6)', t2) + Lb(f'background:{HL};color:{BG};font:700 3.4cqw {TEXT};padding:.9cqw 2.4cqw;border-radius:99px', lab_txt),
     "underline": T(f'color:#fff;font-size:9cqw;line-height:1.05;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)', f'{TS_T1}<br><span style="border-bottom:1.1cqw solid {HL}">{TS_T2}</span>') + Lb(f'color:#fff;font:600 3.4cqw {TEXT};text-shadow:0 .2cqw .8cqw rgba(0,0,0,.8)', '→ ' + lab_txt),
     "kicker":    T('', f'<div style="font:700 3cqw {TEXT};letter-spacing:.3cqw;color:{HL};text-transform:uppercase;margin-bottom:.8cqw;text-shadow:0 .2cqw .8cqw rgba(0,0,0,.6)">{lab_txt}</div><div style="color:#fff;font-size:10cqw;line-height:.98;text-shadow:0 .4cqw 1.4cqw rgba(0,0,0,.6)">{t2}</div>'),
     "stacked":   T('font-size:9.5cqw;line-height:.96', f'<span style="color:#fff;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)">{TS_T1}</span><br><span style="color:{HL};text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)">{TS_T2}</span>') + Lb(f'color:{TX};background:{LT};font:600 3.3cqw {TEXT};padding:.7cqw 1.8cqw', lab_txt),
     "shadow":    T(f'color:{BG};font-size:9.5cqw;line-height:1.02;text-shadow:.7cqw .7cqw 0 {TX}', t2) + Lb(f'background:{EX2};color:{TX};font:700 3.4cqw {TEXT};padding:.7cqw 1.8cqw;box-shadow:.6cqw .6cqw 0 {TX}', lab_txt),
     "brackets":  T(f'color:#fff;font-size:8.6cqw;line-height:1.02;padding:2cqw 2.6cqw;border-left:.5cqw solid {HL};border-top:.5cqw solid {HL};text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)', t2) + Lb(f'color:#fff;font:600 3.4cqw {TEXT};padding:0 0 0 2cqw;border-left:.5cqw solid {HL};text-shadow:0 .2cqw .8cqw rgba(0,0,0,.8)', lab_txt),
     "tape":      T('transform:rotate(-2.5deg)', f'<div style="background:{LT};color:{TX};font-size:8cqw;line-height:1.05;padding:1.2cqw 3cqw;clip-path:polygon(2% 0,98% 4%,100% 50%,97% 100%,1% 96%,0 50%);box-shadow:0 .5cqw 1.4cqw rgba(0,0,0,.3)">{t2}</div>') + Lb(f'background:{HL};color:{BG};font:700 3.3cqw {TEXT};padding:.7cqw 2cqw;transform:rotate(2deg);clip-path:polygon(3% 0,100% 6%,97% 100%,0 92%)', lab_txt),
     "stamp":     T(f'color:{HL};font-size:8.6cqw;line-height:1.02;border:.7cqw solid {HL};padding:1.2cqw 2.4cqw;transform:rotate(-6deg);background:rgba(255,255,255,.12);text-shadow:0 .2cqw .6cqw rgba(0,0,0,.35)', t2) + Lb(f'color:#fff;font:700 3.4cqw {TEXT};text-transform:uppercase;letter-spacing:.3cqw;text-shadow:0 .2cqw .8cqw rgba(0,0,0,.8)', lab_txt),
     "sticker":   T(f'background:#fff;color:{TX};font-size:8.2cqw;line-height:1.02;padding:1.6cqw 2.6cqw;border:.6cqw solid {TX};border-radius:2cqw;box-shadow:1cqw 1cqw 0 {HL};transform:rotate(-3deg)', t2) + Lb(f'background:{EX2};color:{TX};font:800 3.4cqw {TEXT};padding:.8cqw 2cqw;border:.5cqw solid {TX};border-radius:99px;transform:rotate(2deg)', lab_txt),
     "handwritten": T(f'color:#fff;font:700 10cqw/1 {NOTES};text-shadow:0 .3cqw 1.2cqw rgba(0,0,0,.7);transform:rotate(-3deg)', 'I tried it<br>for 30 days') + Lb(f'color:{EX2};font:700 6cqw {NOTES};text-shadow:0 .2cqw 1cqw rgba(0,0,0,.8)', lab_txt + ' →'),
     "split":     T(f'font-size:10cqw;line-height:1;background:linear-gradient(180deg,#fff 50%,{HL} 50%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 .3cqw .8cqw rgba(0,0,0,.5))', t2) + Lb(f'color:#fff;font:700 3.4cqw {TEXT};background:rgba(0,0,0,.55);padding:.7cqw 1.8cqw', lab_txt),
     "glitch":    T(f'color:#fff;font-size:9.5cqw;line-height:1.02;text-shadow:.5cqw 0 0 {HL},-.5cqw 0 0 {EX2}', t2) + Lb(f'color:#fff;font:700 3.4cqw {MONO};background:#000;padding:.6cqw 1.6cqw;text-shadow:.25cqw 0 0 {HL}', lab_txt),
     "clipping":  T('', ''.join(f'<span style="display:inline-block;margin:.3cqw;padding:.2cqw 1.1cqw;font-size:{fs}cqw;line-height:1;background:{bg};color:{fg};transform:rotate({r}deg);font-family:{ff}">{w}</span>' for w, fs, bg, fg, r, ff in [
         ("I", 8, "#fff", TX, -4, TITLE), ("TRIED", 7.4, HL, BG, 3, "'Bowlby One',Impact,sans-serif"), ("IT", 8.4, TX, BG, -2, TITLE), ("FOR", 6.8, LT, TX, 4, "'Fraunces',Georgia,serif"), ("30", 9, EX2, TX, -5, "'Anton',Impact,sans-serif"), ("DAYS", 7.6, "#fff", TX, 2, "'Special Elite',monospace")])) + Lb(f'color:#fff;font:600 3.4cqw {TEXT};text-shadow:0 .2cqw .8cqw rgba(0,0,0,.8)', lab_txt),
    }
    # Styles with no box of their own get the soft dark wash real edits use behind bare text on a bright window.
    scrim = '' if style in ("blocks", "bar", "tape", "sticker", "shadow") else '<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.55),rgba(0,0,0,.25) 45%,transparent 70%)"></div>'
    return img + scrim + f'<div style="{W_}">{S[style]}</div>'
TS_OPTS = [  # (id, name, tier, line)
 ("blocks", "Color blocks", "C", "Words on solid blocks of your colors."), ("plain", "Bare words", "C", "Just the words with a soft shadow."),
 ("bar", "Bottom bar", "C", "Title and label in one bar at the bottom."), ("highlighter", "Highlighter", "C", "A marker stroke behind the words."),
 ("pill", "Pill label", "C", "Plain title, label in a rounded pill."), ("underline", "Underline", "C", "One thick line under the key words."),
 ("kicker", "Kicker", "C", "A small label above a big title."), ("stacked", "Two-tone stack", "R", "Each line in a different color."),
 ("outline", "Outline", "R", "Hollow letters, thin outline."), ("shadow", "Hard shadow", "R", "A solid offset shadow, a bit retro."),
 ("brackets", "Corner brackets", "R", "Words framed by two corner lines."), ("tape", "Tape label", "R", "Words on a strip of tape."),
 ("split", "Split color", "R", "Letters half one color, half another."), ("stamp", "Stamp", "F", "A tilted rubber stamp."),
 ("sticker", "Sticker", "F", "A thick-outlined sticker, slightly tilted."), ("handwritten", "Handwritten", "F", "Your notes font, like you wrote it on."),
 ("glitch", "Glitch", "F", "A color-split, digital edge."), ("clipping", "Cut-out letters", "F", "Each word cut from a different scrap.")]
TS_LINE = "Shown in your fonts and colors. How text moves comes later, in Movement."
TS_FONTS = ["bebas-neue", "inter", "caveat", "space-mono", "bowlby-one", "fraunces", "anton", "special-elite"]
TS_FIN = ["blocks", "highlighter", "bar", "sticker", "stacked"]   # the example's finalists
finalist_flow("text-style", "Text style", "How titles and labels sit on your video. " + TS_LINE,
 [{"id": i, "name": n, "line": l, "html": ts(i), **({"pick": True, "why": "Clean and readable, and it carries your colors without shouting."} if i == "blocks" else {})} for i, n, t, l in TS_OPTS],
 TS_FIN, "Next: captions.", TS_FONTS, photo_tag=PHOTO_TAG, pick_what="Your finalists, large, over the test photo. " + TS_LINE)

# ---------- 8. captions: finalists -> pick (Main / Backup / Alternative / Discard) ----------
# Captions are the one look that plays here: how words appear (word by word, one big word) is part of the style.
# Static state = the caption mid-sentence (key word "nobody" active), so a card reads before anyone presses Play.
CAP_WORDS = SAMPLE_CAPTION.split()
CAP_STEP = 0.34                      # seconds per word when playing
CAP_MS = int(len(CAP_WORDS) * CAP_STEP * 1000 + 900)
CAP_KEY = 4                          # "nobody": the word shown active in the static card
CAPF = TEXT                          # the caption font: the text font unless the creator picked one just for captions (Stage 4.7)
def cap(style):
    n = len(CAP_WORDS); c = f"cp-{style}"
    img = f'<img src="{FACE}" style="{FRAMED}">'
    dl = lambda: ''.join(f'.card.playing .{c} .w:nth-child({i+1}){{animation-delay:{i*CAP_STEP:.2f}s}}' for i in range(n))
    span = lambda extra='': ''.join(f'<span class="w{" k" if i == CAP_KEY else ""}">{w}</span>' for i, w in enumerate(CAP_WORDS))
    bottom = "position:absolute;left:6%;right:6%;bottom:9%;display:flex;flex-wrap:wrap;justify-content:center;gap:0 1.4cqw;text-align:center;container-type:normal"
    appear = f'.card.playing .{c} .w{{animation:{c}-in .2s ease-out both}}{dl()}@keyframes {c}-in{{from{{opacity:0;transform:translateY(.8cqw)}}to{{opacity:1;transform:none}}}}'
    pop = f'.card.playing .{c} .w{{animation:{c}-in .28s cubic-bezier(.3,1.6,.5,1) both}}{dl()}@keyframes {c}-in{{from{{opacity:0;transform:scale(.4)}}to{{opacity:1;transform:none}}}}'
    def moving(prop_on, prop_off):   # the active treatment travels word to word while playing
        # fill-mode none: a word is lit only while its own step runs, so exactly one word is lit at a time, in order.
        # (with "both", every word showed the lit frame while waiting for its turn: the karaoke bug)
        return (f'.card.playing .{c} .k{{{prop_off}}}.card.playing .{c} .w{{animation:{c}-hl {CAP_STEP:.2f}s step-end none}}{dl()}'
                f'@keyframes {c}-hl{{0%{{{prop_on}}}100%{{{prop_on}}}}}')
    T = {
     "plain":    (f'color:#fff;font:700 4.6cqw {CAPF};text-shadow:0 .3cqw 1cqw #000,0 0 .4cqw #000', '', appear),
     "strip":    (f'color:#fff;font:600 4.3cqw {CAPF};background:rgba(0,0,0,.78);padding:1cqw 2cqw;border-radius:1cqw;left:12%;right:12%', '', appear),
     "highlight":(f'color:#fff;font:800 4.6cqw {CAPF};text-shadow:0 .3cqw 1cqw #000', f'.{c} .k{{background:{HL};color:{BG};text-shadow:none;padding:0 1cqw;border-radius:.6cqw}}',
                  moving(f'background:{HL};color:{BG};text-shadow:none;padding:0 1cqw;border-radius:.6cqw', 'background:transparent;color:#fff;padding:0 1cqw')),
     "fill":     (f'font:800 4.6cqw {CAPF};background:rgba(0,0,0,.55);padding:1cqw 2cqw;border-radius:1cqw;left:12%;right:12%', f'.{c} .w{{color:rgba(255,255,255,.55)}}.{c} .w:nth-child(-n+{CAP_KEY+1}){{color:{HL}}}',
                  f'.card.playing .{c} .w{{color:rgba(255,255,255,.55);animation:{c}-f .01s step-end both}}' + ''.join(f'.card.playing .{c} .w:nth-child({i+1}){{animation-delay:{i*CAP_STEP:.2f}s}}' for i in range(n)) + f'@keyframes {c}-f{{to{{color:{HL}}}}}'),
     "bigword":  (f'position:absolute;left:4%;top:34%;width:52%;height:34%;font:400 15cqw/1 {TITLE};color:#fff;text-shadow:0 .5cqw 1.6cqw rgba(0,0,0,.8)', f'.{c} .w{{position:absolute;left:0;top:0;opacity:0}}.{c} .k{{opacity:1}}',
                  f'.card.playing .{c} .k{{opacity:0}}.card.playing .{c} .w{{animation:{c}-s {CAP_STEP:.2f}s step-end both;animation-fill-mode:none}}{dl()}.card.playing .{c} .w:last-child{{animation-fill-mode:forwards}}@keyframes {c}-s{{0%{{opacity:1;transform:scale(1.08)}}100%{{opacity:1}}}}'),
     "twoline":  (f'color:#fff;font:500 4cqw {CAPF};text-shadow:0 .2cqw .8cqw #000;max-width:60%;left:20%;right:20%', '', appear),
     "popup":    (f'color:#fff;font:900 5cqw {CAPF};text-transform:uppercase;text-shadow:0 .4cqw 0 #000,0 0 1cqw #000', '', pop),
     "keycolor": (f'color:#fff;font:800 4.6cqw {CAPF};text-shadow:0 .3cqw 1cqw #000', f'.{c} .w:nth-child(5),.{c} .w:nth-child(4){{color:{EX2}}}', appear),
     "outlined": (f'color:#fff;font:900 5.2cqw {CAPF};-webkit-text-stroke:.5cqw #000;paint-order:stroke fill;text-transform:uppercase', '', pop),
     "classic":  (f'color:{EX2};font:700 4.4cqw {CAPF};-webkit-text-stroke:.35cqw #000;paint-order:stroke fill', '', appear),
     "chips":    (f'gap:.8cqw;font:700 4cqw {CAPF}', f'.{c} .w{{background:rgba(0,0,0,.7);color:#fff;padding:.4cqw 1.2cqw;border-radius:.8cqw}}.{c} .k{{background:{HL};color:{BG}}}',
                  moving(f'background:{HL};color:{BG}', 'background:rgba(0,0,0,.7);color:#fff')),
     "corner":   (f'justify-content:flex-start;text-align:left;left:4%;right:auto;max-width:46%;color:#fff;font:600 3.8cqw {CAPF};border-left:.8cqw solid {HL};padding-left:1.6cqw;background:linear-gradient(90deg,rgba(0,0,0,.6),transparent)', '', appear),
     "typewriter":(f'color:{TX};background:{BG};font:700 3.8cqw {MONO};padding:1cqw 1.8cqw;left:10%;right:10%', '', f'.card.playing .{c} .w{{animation:{c}-in .01s step-end both}}{dl()}@keyframes {c}-in{{from{{visibility:hidden}}to{{visibility:visible}}}}'),
     "stacked":  (f'position:absolute;left:5%;top:30%;width:46%;flex-direction:column;align-items:flex-start;text-align:left;font:400 8cqw/0.98 {TITLE};color:#fff;text-shadow:0 .4cqw 1.2cqw rgba(0,0,0,.8)', f'.{c} .w{{display:none}}.{c} .w:nth-child(4),.{c} .w:nth-child(5),.{c} .w:nth-child(6){{display:block}}.{c} .k{{color:{HL}}}',
                  f'.card.playing .{c} .w{{display:block;animation:{c}-in .2s ease-out both}}{dl()}@keyframes {c}-in{{from{{opacity:0;transform:translateX(-2cqw)}}to{{opacity:1;transform:none}}}}'),
     "bubble":   (f'position:absolute;left:4%;bottom:auto;top:44%;right:auto;max-width:40%;display:flex;flex-wrap:wrap;gap:0 1.2cqw;justify-content:flex-start;text-align:left;background:#fff;color:{TX};font:700 3.8cqw {CAPF};padding:1.6cqw 2.2cqw;border-radius:3cqw 3cqw 3cqw .6cqw;box-shadow:0 .6cqw 1.6cqw rgba(0,0,0,.35)', '', appear),
     "slam":     (f'color:#fff;font:400 7cqw {TITLE};text-shadow:0 .4cqw 0 {TX},0 0 1.2cqw rgba(0,0,0,.6);gap:0 1.8cqw', f'.{c} .k{{color:{HL}}}',
                  f'.card.playing .{c} .w{{animation:{c}-in .22s cubic-bezier(.2,1.8,.4,1) both}}{dl()}@keyframes {c}-in{{from{{opacity:0;transform:scale(2.2) rotate(-8deg)}}to{{opacity:1;transform:none}}}}'),
     "handwritten":(f'color:#fff;font:700 6.4cqw {NOTES};text-shadow:0 .3cqw 1cqw #000', f'.{c} .k{{color:{EX2}}}', appear),
     "neon":     (f'color:#fff;font:700 4.8cqw {CAPF};text-shadow:0 0 .6cqw {HL},0 0 2cqw {HL},0 0 4cqw {HL}', '', appear),
    }
    box, static_css, play_css = T[style]
    pos = box if box.startswith('position:absolute') else bottom + ';' + box
    return (img + f'<div style="position:absolute;inset:0;container-type:size">'
            + f'<style>{static_css}{play_css}</style><div class="{c}" style="{pos}">{span()}</div></div>')
CAP_OPTS = [
 ("strip", "Dark strip", "C", "Words on a dark strip. Readable on anything."), ("plain", "Plain white", "C", "White words, soft shadow."),
 ("highlight", "Highlight", "C", "The word being said lights up in your color."), ("fill", "Fill-in", "C", "Words fill with your color as you say them."),
 ("outlined", "Bold outline", "C", "Thick outlined capitals, the short-video classic."), ("popup", "Pop-up", "C", "Each word pops in with a bounce."),
 ("twoline", "Subtitle", "C", "Small, quiet, like a film subtitle."), ("keycolor", "Key words", "R", "The important words in your second color."),
 ("chips", "Word chips", "R", "Each word on its own chip; the one being said lights up."), ("classic", "Yellow classic", "R", "Yellow with a black edge, old-TV style."),
 ("corner", "Side note", "R", "Small, to the side, out of the way."), ("bigword", "One big word", "R", "One word at a time, huge."),
 ("stacked", "Stacked", "F", "A few words stacked big beside you."), ("typewriter", "Typewriter", "F", "Typed out, one word at a time."),
 ("bubble", "Speech bubble", "F", "Your words in a bubble beside you."), ("slam", "Slam", "F", "Each word slams in."),
 ("handwritten", "Handwritten", "F", "In your notes font."), ("neon", "Neon", "F", "Glowing in your pop color.")]
CAP_FONTS = ["bebas-neue", "inter", "caveat", "space-mono"]
CAP_FIN = ["strip", "highlight", "chips", "outlined", "fill"]   # the example's finalists
finalist_flow("captions", "Captions", "The words on screen while you talk. Press Play on any card to see them come in.",
 [{"id": i, "name": n, "line": l, "html": cap(i), "play": True, "playMs": CAP_MS, **({"pick": True, "why": "Readable on any background, so it never fights your footage."} if i == "strip" else {})} for i, n, t, l in CAP_OPTS],
 CAP_FIN, "Next: one quick question about which videos get captions, then backdrops.", CAP_FONTS, photo_tag=PHOTO_TAG, pick_what="Your finalists, large. Press Play to see each one come in.")

# ---------- 9. backdrops (library) ----------
# Universal names and "For:" lines; colors come from the palette. The gray figure stands in for the creator.
sil = '<div style="position:absolute;left:74%;bottom:0;transform:translateX(-50%);width:22%;height:46%;background:#8a8a8a;border-radius:50% 50% 0 0/40% 40% 0 0"></div><div style="position:absolute;left:74%;bottom:38%;transform:translateX(-50%);width:10.5%;aspect-ratio:1;background:#8a8a8a;border-radius:50%"></div>'
def bd(style, withsil=True, chalk=False):
    s = sil if withsil else ''
    col = "#f4f4f4" if chalk else TX; bgc = "transparent" if chalk else BG
    tc = f'<div style="position:absolute;left:8%;top:14%;font:400 7.5cqw {TITLE};color:{col};background:{bgc};padding:.6cqw 2cqw">Part 2</div>' if not withsil else ''
    return f'<div style="position:absolute;inset:0;container-type:size"><div style="position:absolute;inset:0;{style}"></div>{s}{tc}</div>'
IMG_BD = lambda slug: f"background:url(img/backdrops/{slug}.jpg) center/cover"
bds_every = [("light-plain", "Light plain", f"background:{BG}", "For: title cards", False, False),
 ("pop-plain", "Pop color", f"background:{HL}", "For: behind you when your room is removed", True, False),
 ("dark-plain", "Dark plain", f"background:{TX}", "For: serious moments and the last screen", True, False),
 ("studio", "Studio sweep", f"background:radial-gradient(ellipse at 50% 30%,#ffffff,{LT} 45%,#b9c4bf)", "For: a clean, professional backdrop", True, False),
 ("blur", "Your space, blurred", f"background:url({PLACE}) center/cover;filter:blur(6px)", "For: staying in your world, without the clutter", True, False),
 ("grad", "Soft gradient", f"background:linear-gradient(135deg,{HL},{BG})", "For: chapter cards", False, False),
 ("paper", "Paper", f"background:{BG} repeating-linear-gradient(0deg,rgba(0,0,0,.035) 0 2px,transparent 2px 4px)", "For: notes and lists", False, False),
 ("grid", "Grid paper", f"background:{BG};background-image:linear-gradient(rgba(0,0,0,.1) 1px,transparent 1px),linear-gradient(90deg,rgba(0,0,0,.1) 1px,transparent 1px);background-size:6cqw 6cqw", "For: explaining something step by step", False, False),
 ("spots", "Polka dots", f"background:{LT};background-image:radial-gradient({EX2} 18%,transparent 19%);background-size:7cqw 7cqw", "For: bloopers and silly moments", True, False),
 ("rays", "Sunburst", f"background:repeating-conic-gradient(from 0deg at 50% 100%,{EX2} 0 10deg,{BG} 10deg 20deg)", "For: big announcements", True, False),
 ("city-night", "City at night", IMG_BD("city-night"), "For: a calm, after-hours feel", True, False),
 ("chalkboard", "Chalkboard", IMG_BD("chalkboard"), "For: numbers and prices", True, False),
 ("corkboard", "Cork board", IMG_BD("corkboard"), "For: plans and ideas pinned up", True, False),
 ("blueprint", "Blueprint", IMG_BD("blueprint"), "For: how something works", True, False),
 ("space", "Space", IMG_BD("space"), "For: a big idea, or \"out of this world\"", True, False)]
bds_fun = [("weather", "Weather map", IMG_BD("weather-map"), "For: a \"forecast\" joke", True, False),
 ("news-desk", "News desk", IMG_BD("news-desk"), "For: announcing something small as if it's huge", True, False),
 ("courtroom", "Courtroom", IMG_BD("courtroom"), "For: putting a habit on trial", True, False),
 ("game-show", "Game show", IMG_BD("game-show"), "For: a quiz or a big choice", True, False),
 ("award-stage", "Award stage", IMG_BD("award-stage"), "For: celebrating a tiny win", True, False),
 ("moon", "The moon", IMG_BD("moon"), "For: \"one small step\"", True, False),
 ("fish-tank", "Inside a fish tank", IMG_BD("fish-tank"), "For: feeling watched", True, False),
 ("giant-kitchen", "Giant's kitchen", IMG_BD("giant-kitchen"), "For: feeling tiny next to a problem", True, False),
 ("crime-scene", "Crime scene", IMG_BD("crime-scene"), "For: \"what went wrong here\"", True, False),
 ("cereal-box", "Cereal box", IMG_BD("cereal-box"), "For: selling something like an ad", True, False)]
bds_you = [("president", "President", IMG_BD("president-office"), "For: a big announcement from \"the office\"", True, False),
 ("pilot", "Pilot", IMG_BD("cockpit"), "For: \"this is your captain speaking\"", True, False),
 ("baseball", "Pro ballplayer", IMG_BD("baseball"), "For: stepping up to a challenge", True, False),
 ("detective", "Detective", IMG_BD("detective"), "For: solving a mystery", True, False),
 ("olympian", "Champion", IMG_BD("podium"), "For: winning at something small", True, False)]
BD_BTN = [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}]
bd_sec = lambda id, title, line, rows: {"id": id, "title": title, "line": line, "kind": "library", "keepWord": "backdrop|backdrops", "layout": "tiles", "movable": False,
   "buttons": BD_BTN, "keepValues": ["keep"],
   "options": [{"id": s, "name": n, "line": l, "html": bd(c, w, ck), **({"pick": True, "why": "A calm default for title cards; you can change it any time."} if s == "light-plain" else {})} for s, n, c, l, w, ck in rows]}
W("backdrops", {
 "round": "backdrops", "kind": "library", "keepWord": "backdrop|backdrops", "fonts": ["bebas-neue"],
 "title": "Backdrops",
 "what": "What goes behind you when your room is removed, and behind title cards. The gray figure stands in for you.",
 "next": "Next: extras for special moments.", "persona": SAY_PERSONA,
 "sections": [bd_sec("everyday", "Everyday", "", bds_every), bd_sec("fun", "Fun and absurd", "For a joke or a big moment.", bds_fun),
              bd_sec("you-as", "You as…", "Sets that cast you in a role for a moment.", bds_you)]})

# ---------- 10. extras (library): small extras + big moments ----------
# Every card has to show the effect at a glance, on a picture where it makes sense. Universal copy only.
def fr(inner, img=FACE, framed=True):
    st = FRAMED if framed and img == FACE else "position:absolute;inset:0;width:100%;height:100%;object-fit:cover"
    return f'<img src="{img}" style="{st}"><div style="position:absolute;inset:0;container-type:size">{inner}</div>'
PIN = f'<svg viewBox="0 0 24 24" style="width:4.5cqw;height:4.5cqw;vertical-align:middle;margin-right:1cqw"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z" fill="{HL}"/></svg>'
ARROW = f'<svg viewBox="0 0 100 60" style="position:absolute;left:20%;top:40%;width:22%;overflow:visible"><path d="M95 5 C 70 10, 45 25, 18 48" fill="none" stroke="{HL}" stroke-width="5" stroke-linecap="round"/><path d="M8 54 L 28 50 L 18 38 Z" fill="{HL}"/></svg>'
small = [
 ("callout", "Callout", "For: pointing at one detail", fr(f'<svg viewBox="0 0 320 180" style="position:absolute;inset:0;width:100%;height:100%"><circle cx="40" cy="128" r="22" fill="none" stroke="{HL}" stroke-width="3.5"/><line x1="60" y1="116" x2="104" y2="86" stroke="{HL}" stroke-width="3"/><rect x="104" y="72" width="78" height="24" rx="3" fill="{BG}"/><text x="112" y="89" font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" fill="{TX}">this one</text></svg>')),
 ("arrow", "Arrow", "For: \"look here\"", fr(ARROW + f'<div style="position:absolute;left:40%;top:30%;font:700 4cqw {NOTES};color:#fff;text-shadow:0 .2cqw .8cqw #000">look!</div>')),
 ("chapter", "Chapter card", "For: starting a new part of the video", f'<div style="position:absolute;inset:0;container-type:size;background:{BG};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1cqw"><div style="font:700 3.6cqw {TEXT};color:{HL};letter-spacing:.6cqw">PART 2</div><div style="font:400 11cqw/1 {TITLE};color:{TX}">THE HARD PART</div></div>'),
 ("spotlight", "Spotlight", "For: making everyone look at one thing", fr('<div style="position:absolute;inset:0;background:radial-gradient(circle at 63% 34%,transparent 13cqw,rgba(0,0,0,.86) 22cqw)"></div>')),
 ("zoom", "Zoom-in", "For: a reaction that needs a close-up", f'<div style="position:absolute;inset:0;background:url({FACE}) 50% 26%/260% no-repeat"></div><div style="position:absolute;inset:6%;border:3px solid #fff;border-radius:2px;clip-path:polygon(0 0,18% 0,18% 3%,3% 3%,3% 18%,0 18%,0 82%,3% 82%,3% 97%,18% 97%,18% 100%,82% 100%,82% 97%,97% 97%,97% 82%,100% 82%,100% 18%,97% 18%,97% 3%,82% 3%,82% 0,100% 0,100% 100%,0 100%)"></div>'),
 ("timer", "Timer", "For: showing how long something takes", fr(f'<div style="position:absolute;left:4%;top:8%;background:{TX};color:{BG};font:700 7cqw {MONO};padding:1cqw 3cqw;border-radius:1.5cqw">00:30</div>')),
 ("progress", "Progress bar", "For: how far along you are", fr(f'<div style="position:absolute;left:0;right:0;top:0;height:2.6cqw;background:rgba(0,0,0,.35)"><div style="width:62%;height:100%;background:{HL}"></div></div><div style="position:absolute;left:3%;top:5cqw;font:700 3.4cqw {TEXT};color:#fff;text-shadow:0 .2cqw .8cqw #000">Day 18 of 30</div>')),
 ("checklist", "Checklist", "For: steps or a list as you go", fr(f'<div style="position:absolute;left:4%;top:10%;background:{BG};color:{TX};font:600 3.8cqw/1.7 {TEXT};padding:1.8cqw 3cqw;border-radius:1.5cqw">' + ''.join(f'<div><span style="color:{HL};font-weight:800">{"✓" if i < 2 else "○"}</span> {t.split(" · ")[1]}</div>' for i, t in enumerate(SAMPLE_LIST)) + '</div>')),
 ("scorecard", "Scorecard", "For: rating something", fr(f'<div style="position:absolute;left:4%;top:10%;background:{BG};color:{TX};font:700 3.6cqw/1.75 {TEXT};padding:1.8cqw 3cqw;border-radius:1.5cqw">Difficulty <span style="color:{HL}">★★★★☆</span><br>Cost <span style="color:{HL}">★★☆☆☆</span><br>Worth it <span style="color:{HL}">★★★★★</span></div>')),
 ("counter", "Big number", "For: one number that matters", fr(f'<div style="position:absolute;left:5%;top:16%;color:#fff;text-shadow:0 .5cqw 1.6cqw rgba(0,0,0,.7)"><div style="font:400 22cqw/0.9 {TITLE};color:{HL}">30</div><div style="font:400 7cqw/1 {TITLE}">DAYS</div></div>')),
 ("thought", "Inner voice", "For: what you were really thinking", fr(f'<div style="position:absolute;left:4%;top:12%;background:#fff;color:{TX};font:italic 600 4cqw {TEXT};padding:2cqw 3cqw;border-radius:4cqw;max-width:40%">is this even working?</div><div style="position:absolute;left:38%;top:36%;width:3cqw;height:3cqw;border-radius:50%;background:#fff"></div><div style="position:absolute;left:43%;top:42%;width:1.8cqw;height:1.8cqw;border-radius:50%;background:#fff"></div>')),
 ("comment", "Viewer comment", "For: answering a question someone asked", fr(f'<div style="position:absolute;left:4%;top:12%;background:#fff;color:#111;font:4cqw {TEXT};padding:2cqw 2.6cqw;border-radius:2cqw;max-width:44%;box-shadow:0 .6cqw 2cqw rgba(0,0,0,.35)"><div style="font:700 3.2cqw {TEXT};color:#666;margin-bottom:.6cqw">@viewer</div>Does this really work?</div>')),
 ("location", "Location tag", "For: saying where you are", fr(f'<div style="position:absolute;left:4%;bottom:12%;background:{BG};color:{TX};font:700 3.8cqw {TEXT};padding:1.2cqw 2.6cqw;border-radius:99px;display:flex;align-items:center">{PIN}Somewhere new</div>')),
 ("quote", "Quote card", "For: a line worth repeating", f'<div style="position:absolute;inset:0;container-type:size;background:{TX};display:flex;align-items:center;padding:0 9%"><div style="font:400 8.5cqw/1.05 {TITLE};color:{BG}"><span style="color:{HL}">“</span>THE HARD PART IS WEEK ONE.<span style="color:{HL}">”</span></div></div>'),
 ("compare", "Side by side", "For: comparing before and after", f'<div style="position:absolute;inset:0;container-type:size;display:grid;grid-template-columns:1fr 1fr;gap:3px;background:#000"><div style="position:relative;background:url({HANDS}) center/cover;filter:grayscale(1) brightness(.9)"><span style="position:absolute;left:5%;top:7%;background:#000;color:#fff;font:700 3.4cqw {TEXT};padding:.6cqw 1.6cqw">DAY 1</span></div><div style="position:relative;background:url({HANDS}) center/cover;filter:saturate(1.3)"><span style="position:absolute;left:5%;top:7%;background:{HL};color:{BG};font:700 3.4cqw {TEXT};padding:.6cqw 1.6cqw">DAY 30</span></div></div>')]
big = [
 ("freeze", "Freeze & draw", "For: stopping the action to explain it", fr(f'<div style="position:absolute;inset:0;background:rgba(255,255,255,.08);filter:saturate(.6)"></div><svg viewBox="0 0 320 180" style="position:absolute;inset:0;width:100%;height:100%"><path d="M30 40 C 60 20, 100 30, 110 60" fill="none" stroke="{HL}" stroke-width="4" stroke-linecap="round"/><path d="M104 52 L 112 64 L 98 62" fill="none" stroke="{HL}" stroke-width="4" stroke-linecap="round"/></svg><div style="position:absolute;left:4%;top:7%;font:700 5cqw {NOTES};color:#fff;text-shadow:0 .2cqw .8cqw #000">wait for it</div><div style="position:absolute;right:3%;bottom:6%;background:#000;color:#fff;font:700 3cqw {MONO};padding:.6cqw 1.4cqw">❚❚ PAUSED</div>')),
 ("clones", "Clone grid", "For: arguing with yourself", '<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:2px;background:#000">' + ''.join(f'<div style="background:url({FACE}) center 30%/cover;filter:{f}"></div>' for f in ["none", "hue-rotate(40deg)", "saturate(1.6)", "grayscale(1)"]) + '</div>'),
 ("wordburst", "Word burst", "For: a punchline, one word at a time", fr(f'<div style="position:absolute;left:4%;top:30%;display:flex;gap:2cqw;font:400 11cqw/1 {TITLE};color:#fff;text-shadow:0 .5cqw 1.4cqw #000"><span>WAIT.</span><span style="color:{HL}">FOR.</span><span>IT.</span></div>')),
 ("countdown", "Countdown", "For: building up to a reveal", fr(f'<div style="position:absolute;left:8%;top:10%;font:400 34cqw/1 {TITLE};color:{HL};text-shadow:0 .8cqw 2cqw rgba(0,0,0,.6)">3</div>')),
 ("wipe", "Before/after wipe", "For: a reveal with a sliding line", f'<div style="position:absolute;inset:0;container-type:size;background:url({PLACE}) center/cover;filter:saturate(1.3)"></div><div style="position:absolute;inset:0 48% 0 0;background:url({PLACE}) left center/cover;filter:grayscale(1) brightness(.85);background-size:208% auto"></div><div style="position:absolute;left:52%;top:0;bottom:0;width:4px;background:#fff;box-shadow:0 0 8px rgba(0,0,0,.6)"></div><div style="position:absolute;left:52%;top:50%;transform:translate(-50%,-50%);width:9%;aspect-ratio:1;border-radius:50%;background:#fff;box-shadow:0 0 8px rgba(0,0,0,.5)"></div>'),
 ("replay", "Instant replay", "For: \"let's see that again\"", fr(f'<div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.07) 0 2px,transparent 2px 5px)"></div><div style="position:absolute;left:4%;top:8%;background:#e11;color:#fff;font:800 4cqw {TEXT};padding:.8cqw 2cqw;letter-spacing:.3cqw">◀◀ REPLAY</div><div style="position:absolute;left:4%;bottom:8%;color:#fff;font:700 3.4cqw {MONO};text-shadow:0 .2cqw .6cqw #000">0.5x</div>')),
 ("scratch", "Record scratch", "For: \"yep, that's me\" freeze-frames", fr(f'<div style="position:absolute;inset:0;filter:none;background:rgba(0,0,0,.18)"></div><div style="position:absolute;left:4%;top:14%;font:700 7cqw/1.05 {NOTES};color:#fff;text-shadow:0 .3cqw 1cqw #000;max-width:46%">Yep. That\'s me.<br><span style="font-size:4.4cqw">You\'re probably wondering how I got here.</span></div>')),
 ("glitch", "Glitch cut", "Big moments only. The frame tears apart for a second.", fr(f'<div style="position:absolute;inset:0;background:url({FACE}) center/cover;clip-path:inset(30% 0 55% 0);transform:translateX(4cqw);filter:hue-rotate(90deg)"></div><div style="position:absolute;inset:0;background:url({FACE}) center/cover;clip-path:inset(62% 0 25% 0);transform:translateX(-3cqw);filter:invert(1)"></div>', framed=False))]
mk = lambda id, title, line, items: {"id": id, "title": title, "line": line, "kind": "library", "keepWord": "extra|extras", "layout": "tiles", "keepValues": ["keep"], "movable": False, "photoTag": PHOTO_TAG,
 "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "options": [{"id": s, "name": n, "line": l, "html": h, **({} if "img/" in h else {"photoTag": ""})} for s, n, l, h in items]}
W("moments-library", {
 "round": "moments-library", "kind": "library", "fonts": ["bebas-neue", "inter", "caveat", "space-mono"],
 "title": "Extras", "what": "Things a video can do when a moment calls for one. You won't use them all; they're there when needed.",
 "next": "Next: break-from-reality moments (the last Look step).", "persona": SAY_PERSONA,
 "sections": [mk("extras", "Small extras", "", small), mk("big", "Big moments", "Bigger pieces, used once in a while.", big)]})

# ---------- 11. break-from-reality moments (library, own page) ----------
# Each card is a 3-frame strip: normal shot -> the cutaway -> back to normal. The cutaways are pre-made once
# (benchmark/bfr/<slug>.jpg, generated from the face test photo) and ship with the skill. Universal copy only;
# the creator's own jokes are written per video by video-genome.
def strip(slug, over):
    lab = lambda t: f'<span style="position:absolute;left:4%;bottom:5%;background:rgba(0,0,0,.65);color:#fff;font:600 2.4cqw {TEXT};padding:.3cqw 1cqw;border-radius:.6cqw">{t}</span>'
    arrow = f'<div style="position:absolute;top:50%;transform:translate(-50%,-50%);width:4.4cqw;height:4.4cqw;border-radius:50%;background:#fff;color:#111;font:800 2.8cqw/4.4cqw {TEXT};text-align:center;box-shadow:0 .3cqw .8cqw rgba(0,0,0,.4);z-index:2;'
    return (f'<div style="position:absolute;inset:0;container-type:size;display:grid;grid-template-columns:1fr 1.7fr 1fr;gap:3px;background:#000">'
            f'<div style="position:relative;background:url({FACE}) 52% 30%/cover">{lab("1 · normal")}</div>'
            f'<div style="position:relative;background:url(img/bfr/{slug}.jpg) center/cover"><div style="position:absolute;inset:0;container-type:size">{over}</div>{lab("2 · the cutaway")}</div>'
            f'<div style="position:relative;background:url({FACE}) 52% 26%/auto 150% no-repeat">{lab("3 · back")}<span style="position:absolute;left:8%;top:8%;color:#fff;font:italic 600 3.4cqw {TEXT};text-shadow:0 .3cqw 1cqw #000">…anyway.</span></div>'
            f'{arrow}left:21.4%">›</div>{arrow}left:78.6%">›</div></div>')
def tk(text, bg="#d4142a"):   # a lower ticker inside the cutaway panel (cqw of that panel)
    return f'<div style="position:absolute;left:0;right:0;bottom:17%;background:{bg};color:#fff;font:800 5.2cqw {TEXT};padding:1cqw 3cqw;white-space:nowrap;overflow:hidden">{text}</div>'
def ttl(text, css=""):
    return f'<div style="position:absolute;left:5%;top:7%;font:400 9cqw/1 {TITLE};color:#fff;text-shadow:0 .4cqw 1.4cqw rgba(0,0,0,.8);{css}">{text}</div>'
bfr_opts = [
 ("breaking-news", "Breaking news", "For: announcing something small as if it's huge", tk("BREAKING: SHE FINISHED IT")),
 ("trailer", "The trailer", "For: an ordinary task cut like a movie trailer", '<div style="position:absolute;left:0;right:0;top:0;height:13%;background:#000"></div><div style="position:absolute;left:0;right:0;bottom:0;height:13%;background:#000"></div>' + ttl("THIS SUMMER", "left:auto;right:5%;top:auto;bottom:18%")),
 ("nature-doc", "Nature documentary", "For: a hushed narrator observing you like wildlife", f'<div style="position:absolute;left:6%;right:6%;bottom:18%;color:#fff;font:italic 5cqw {TEXT};text-shadow:0 .3cqw 1cqw #000;text-align:center">"Here, the creator, in her natural habitat…"</div>'),
 ("department-of-me", "Department of Me", "For: clones of you playing every role", ''.join(f'<span style="position:absolute;top:8%;left:{x}%;background:#fff;color:#111;font:800 3.6cqw {TEXT};padding:.4cqw 1.2cqw;border-radius:.6cqw">{t}</span>' for x, t in [(6, "RESEARCH"), (40, "FINANCE"), (72, "INTERN")])),
 ("infomercial", "The infomercial", "For: \"Are YOU tired of…?\"", ttl("ARE YOU TIRED<br>OF THIS?!", f"color:{EX2};font-size:10cqw")),
 ("sports-commentary", "Sports commentary", "For: two commentators calling the action", f'<span style="position:absolute;left:5%;top:7%;background:#d4142a;color:#fff;font:800 4cqw {TEXT};padding:.5cqw 1.6cqw">● LIVE</span>' + tk("WHAT A MOVE. UNBELIEVABLE.", "#0b2a5b")),
 ("courtroom", "The courtroom", "For: putting a habit or a tool on trial", tk("THE PEOPLE vs. COFFEE", "#3b2a1a")),
 ("weather-report", "Weather report", "For: a \"forecast\" for your week", tk("FORECAST: 100% CHANCE OF CHAOS", "#0b5cad")),
 ("boss-fight", "Boss fight", "For: a problem as a video-game boss", f'<div style="position:absolute;left:8%;right:8%;top:8%"><div style="font:800 3.6cqw {TEXT};color:#fff;text-shadow:0 .2cqw .6cqw #000;margin-bottom:.6cqw">THE TO-DO LIST</div><div style="height:3cqw;background:#300;border:.4cqw solid #fff"><div style="width:72%;height:100%;background:#e21d1d"></div></div></div>'),
 ("reality-show", "Confessional", "For: reacting to what just happened, reality-show style", f'<span style="position:absolute;left:5%;bottom:18%;background:{HL};color:{BG};font:800 3.8cqw {TEXT};padding:.6cqw 1.8cqw;letter-spacing:.3cqw">CONFESSIONAL</span>'),
 ("award-show", "Award show", "For: a trophy for a tiny win", tk("AND THE AWARD GOES TO…", "#6b4f0b")),
 ("tiny-me", "Tiny me", "For: a miniature you giving directions", f'<span style="position:absolute;right:5%;top:8%;background:#fff;color:#111;font:700 3.6cqw {NOTES};padding:.6cqw 1.6cqw;border-radius:2cqw">actual size</span>')]
W("break-from-reality", {
 "round": "break-from-reality", "kind": "library", "keepWord": "moment|moments", "aspect": "5/2", "fonts": ["bebas-neue", "inter", "caveat"],
 "title": "Break-from-reality moments",
 "what": "Short, silly cutaways where the video breaks from reality for a laugh, then snaps back. They keep people watching.",
 "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "keepValues": ["keep"],
 "next": "Next: how your videos move (Movement).", "persona": SAY_PERSONA,
 "options": [{"id": s, "name": n, "line": l, "html": strip(s, o)} for s, n, l, o in bfr_opts]})

# ---------- 12. Movement: motion feel (finalists -> Main + Backup), how things come in (library), scene changes (library) ----------
# Demos on a plain background in the creator's palette and fonts: no photos, no extra zoom, no image switch.
# Static = the finished frame. Play runs the move twice, with a short hold, then stops.
MV_T = f'{TS_T1}<br>{TS_T2}'
def mv_scene(cid, title_html=None, extra=''):
    th = title_html if title_html is not None else MV_T
    return (f'<div class="{cid}" style="position:absolute;inset:0;container-type:size;background:{BG};overflow:hidden">'
            f'<div class="t" style="position:absolute;left:8%;top:18%;font:400 13cqw/1 {TITLE};color:{TX}">{th}</div>'
            f'<div class="l" style="position:absolute;left:8%;bottom:16%;font:700 4.4cqw {TEXT};color:{BG};background:{HL};padding:1cqw 2.4cqw">{SAMPLE_LABEL}</div>{extra}</div>')
def kf(cid, sel, frames, dur, ease="ease", delay=0.0, it=2):
    return (f'.card.playing .{cid} {sel}{{animation:{cid}{sel.strip(".").replace(" ","")} {dur}s {ease} {delay}s {it} both}}'
            f'@keyframes {cid}{sel.strip(".").replace(" ","")}{{{frames}}}')
FEELS = [  # id, name, tier, line, title frames, label frames, ease, dur
 ("snap", "Snap", "C", "Quick and crisp. Things pop into place and stop.", "0%{transform:translateX(-120%)}22%{transform:none}100%{transform:none}", "0%,12%{transform:scale(0)}26%{transform:scale(1.08)}32%,100%{transform:none}", "cubic-bezier(.16,1,.3,1)", 1.6),
 ("glide", "Glide", "C", "Smooth and unhurried. Everything slides and fades.", "0%{opacity:0;transform:translateY(12%)}45%,100%{opacity:1;transform:none}", "0%,20%{opacity:0;transform:translateY(40%)}60%,100%{opacity:1;transform:none}", "cubic-bezier(.45,0,.2,1)", 2.2),
 ("punch", "Punch", "C", "Big hits. Things land hard.", "0%{transform:scale(1.8);opacity:0}14%{transform:scale(.94);opacity:1}20%,100%{transform:none}", "0%,18%{transform:translateX(-140%)}26%{transform:translateX(6%)}30%,100%{transform:none}", "cubic-bezier(.2,.9,.3,1)", 1.6),
 ("deadpan", "Deadpan", "R", "No easing at all. Things are there, then they're not.", "0%,20%{clip-path:inset(0 100% 0 0)}21%,100%{clip-path:inset(0 0 0 0)}", "0%,45%{opacity:0}46%,100%{opacity:1}", "linear", 1.8),
 ("drift", "Drift", "R", "Slow and floaty, never quite still.", "0%{opacity:0;transform:translate(8%,4%)}60%{opacity:1;transform:translate(1%,0)}100%{transform:none}", "0%,30%{opacity:0;transform:translateX(10%)}80%,100%{opacity:1;transform:none}", "cubic-bezier(.37,0,.63,1)", 2.8),
 ("mechanical", "Mechanical", "R", "Precise, stepped, like a machine.", "0%{transform:translateX(-100%)}40%,100%{transform:none}", "0%,40%{transform:scaleX(0)}70%,100%{transform:none}", "steps(5,end)", 1.8),
 ("editorial", "Editorial", "R", "Measured reveals, like a magazine.", "0%{clip-path:inset(100% 0 0 0);transform:translateY(10%)}45%,100%{clip-path:inset(0 0 0 0);transform:none}", "0%,35%{clip-path:inset(0 100% 0 0)}70%,100%{clip-path:inset(0 0 0 0)}", "cubic-bezier(.65,0,.35,1)", 2.2),
 ("cinematic", "Cinematic", "R", "Slow push and long fades, like a film.", "0%{opacity:0;transform:scale(1.12)}70%,100%{opacity:1;transform:none}", "0%,50%{opacity:0}85%,100%{opacity:1}", "cubic-bezier(.33,0,.2,1)", 3.0),
 ("playful", "Playful spring", "F", "Springy and bouncy, a bit cartoon.", "0%{transform:scale(0) rotate(-8deg)}18%{transform:scale(1.15) rotate(3deg)}26%{transform:scale(.95) rotate(-1deg)}32%,100%{transform:none}", "0%,22%{transform:translateY(160%)}34%{transform:translateY(-20%)}40%,100%{transform:none}", "ease-out", 2.0),
 ("handmade", "Handmade jitter", "F", "Choppy, like stop-motion.", "0%{transform:translate(-60%,0) rotate(-3deg)}10%{transform:translate(-40%,2%) rotate(2deg)}20%{transform:translate(-20%,-1%) rotate(-2deg)}30%{transform:translate(-4%,1%) rotate(1deg)}40%{transform:none}55%{transform:rotate(.6deg)}70%{transform:rotate(-.6deg)}100%{transform:none}", "0%,35%{opacity:0}36%{opacity:1;transform:rotate(-3deg)}50%{transform:rotate(2deg)}65%,100%{transform:none}", "steps(1,end)", 2.0),
 ("glitchy", "Glitchy", "F", "Digital stutters and color splits.", "0%{opacity:0}6%{opacity:1;transform:translateX(6%);text-shadow:.6cqw 0 #f0f,-.6cqw 0 #0ff}10%{transform:translateX(-4%)}14%{opacity:.2}18%{opacity:1;transform:none;text-shadow:none}100%{transform:none}", "0%,20%{opacity:0}22%{opacity:1;transform:skewX(20deg)}26%{transform:none}30%{opacity:.3}32%,100%{opacity:1}", "linear", 1.8)]
def mf(fid):
    f = next(x for x in FEELS if x[0] == fid); cid = f"mf-{fid}"
    css = kf(cid, ".t", f[4], f[7], f[6]) + kf(cid, ".l", f[5], f[7], f[6])
    bars = '<div class="bar" style="position:absolute;left:0;right:0;top:0;height:9%;background:#000"></div><div style="position:absolute;left:0;right:0;bottom:0;height:9%;background:#000"></div>' if fid == "cinematic" else ''
    return f'<style>{css}</style>' + mv_scene(cid, extra=bars)
FEEL_MS = lambda fid: int(next(x for x in FEELS if x[0] == fid)[7] * 2 * 1000 + 300)
MV_FONTS = ["bebas-neue", "inter"]
# How things come in: one title entering. Letter- and word-based moves are built per character.
def letters(cls_extra=''):
    out, k = [], 0
    for line in (TS_T1, TS_T2):
        out.append(''.join(f'<span class="c" style="display:inline-block;--i:{(k := k + 1)}">{ch if ch != " " else "&nbsp;"}</span>' for ch in line))
    return '<br>'.join(out)
def words():
    return f'<span class="w" style="display:inline-block;--i:1">I</span> <span class="w" style="display:inline-block;--i:2">TRIED</span> <span class="w" style="display:inline-block;--i:3">IT</span><br><span class="w" style="display:inline-block;--i:4">FOR</span> <span class="w" style="display:inline-block;--i:5">30</span> <span class="w" style="display:inline-block;--i:6">DAYS</span>'
ENTR = [  # id, name, tier, line, kind(t=whole title, c=letters, w=words), keyframes, dur, ease
 ("fade-up", "Fade up", "C", "Fades in while rising a little.", "t", "0%{opacity:0;transform:translateY(12%)}40%,100%{opacity:1;transform:none}", 1.8, "ease-out"),
 ("cut", "Hard cut", "C", "Just appears.", "t", "0%,30%{opacity:0}31%,100%{opacity:1}", 1.4, "linear"),
 ("mask", "Mask reveal", "C", "Slides up from behind an invisible edge.", "t", "0%{clip-path:inset(0 0 100% 0);transform:translateY(30%)}40%,100%{clip-path:inset(0 0 0 0);transform:none}", 1.8, "cubic-bezier(.65,0,.35,1)"),
 ("word-stagger", "Word by word", "C", "Words arrive one after another.", "w", "0%{opacity:0;transform:translateY(40%)}12%,100%{opacity:1;transform:none}", 2.2, "ease-out"),
 ("typewriter", "Typewriter", "C", "Letters appear one by one.", "c", "0%{opacity:0}1%,100%{opacity:1}", 2.2, "steps(1)"),
 ("wipe", "Wipe", "C", "A clean edge sweeps it in.", "t", "0%{clip-path:inset(0 100% 0 0)}40%,100%{clip-path:inset(0 0 0 0)}", 1.8, "cubic-bezier(.65,0,.35,1)"),
 ("zoom", "Zoom in", "C", "Grows into place.", "t", "0%{transform:scale(.4);opacity:0}35%,100%{transform:none;opacity:1}", 1.6, "cubic-bezier(.16,1,.3,1)"),
 ("slide", "Slide in", "C", "Slides in from the side.", "t", "0%{transform:translateX(-110%)}35%,100%{transform:none}", 1.6, "cubic-bezier(.16,1,.3,1)"),
 ("blur", "Blur in", "R", "Comes into focus.", "t", "0%{filter:blur(2.4cqw);opacity:0}45%,100%{filter:none;opacity:1}", 2.0, "ease-out"),
 ("highlight", "Marker sweep", "R", "A marker stroke sweeps in behind it.", "hl", "0%{background-size:0% 100%}40%,100%{background-size:100% 100%}", 2.0, "cubic-bezier(.65,0,.35,1)"),
 ("scramble", "Decode", "R", "Random letters settle into the words.", "c", "0%{opacity:.3;transform:translateY(-30%) rotate(20deg);filter:blur(.3cqw)}10%,100%{opacity:1;transform:none;filter:none}", 2.2, "steps(3)"),
 ("rotate", "Rotate in", "R", "Swings in on a pivot.", "t", "0%{transform:rotate(-25deg) translateY(-20%);opacity:0;transform-origin:0 100%}40%,100%{transform:none;opacity:1}", 1.8, "cubic-bezier(.16,1,.3,1)"),
 ("swing-in", "Hanging sign", "R", "Drops and swings into place like a sign.", "t", "0%{transform:translateY(-150%) rotate(10deg)}22%{transform:rotate(-8deg)}32%{transform:rotate(4deg)}40%{transform:rotate(-2deg)}46%,100%{transform:none}", 2.2, "ease-out"),
 ("side-slam", "Side slam", "R", "Slams in from the side and stops dead.", "t", "0%{transform:translateX(160%)}16%{transform:translateX(-4%)}20%,100%{transform:none}", 1.6, "cubic-bezier(.2,1,.3,1)"),
 ("slam", "Slam", "R", "Drops in hard with a tiny shake.", "t", "0%{transform:translateY(-160%) scale(1.2)}16%{transform:none}20%{transform:translate(1.5%,1%)}24%{transform:translate(-1.5%,0)}28%,100%{transform:none}", 1.8, "cubic-bezier(.5,0,.75,0)"),
 ("glitch", "Glitch", "R", "Color-split jitter, then settles.", "t", "0%{opacity:0}8%{opacity:1;transform:translateX(5%);text-shadow:.8cqw 0 #f0f,-.8cqw 0 #0ff}14%{transform:translateX(-3%)}18%{opacity:.3}22%,100%{opacity:1;transform:none;text-shadow:none}", 1.8, "linear"),
 ("word-spring", "Word spring", "F", "Each word springs in with a bounce.", "w", "0%{transform:scale(0)}8%{transform:scale(1.25)}12%,100%{transform:none}", 2.2, "ease-out"),
 ("letter-drop", "Letter drop", "F", "Letters fall in one by one.", "c", "0%{transform:translateY(-220%);opacity:0}6%{transform:translateY(10%);opacity:1}9%,100%{transform:none}", 2.4, "ease-in"),
 ("flip", "Flip", "F", "Flips over like a card.", "t", "0%{transform:perspective(60cqw) rotateX(-90deg);opacity:0}35%,100%{transform:none;opacity:1}", 1.8, "cubic-bezier(.16,1,.3,1)"),
 ("stamp", "Stamp", "F", "Stamps down with a thud.", "t", "0%{transform:scale(2.4) rotate(-6deg);opacity:0}14%{transform:scale(.96) rotate(-3deg);opacity:1}20%,100%{transform:rotate(-3deg)}", 1.8, "cubic-bezier(.5,0,.75,0)"),
 ("squash", "Squash & stretch", "F", "Lands with a cartoon squash.", "t", "0%{transform:translateY(-140%) scaleY(1.3)}18%{transform:translateY(0) scale(1.2,.7)}26%{transform:scale(.92,1.12)}32%,100%{transform:none}", 1.8, "ease-in"),
 ("neon-flicker", "Neon flicker", "F", "Flickers on like a neon tube.", "t", "0%{opacity:0}5%{opacity:1}8%{opacity:.1}12%{opacity:.9}15%{opacity:.2}22%,100%{opacity:1}", 1.8, "steps(1)"),
 ("print-out", "Print out", "F", "Prints out line by line like a receipt.", "t", "0%{clip-path:inset(0 0 100% 0)}20%{clip-path:inset(0 0 55% 0)}40%,100%{clip-path:inset(0 0 0 0)}", 2.0, "steps(4)"),
 ("shatter", "Reform", "F", "Pieces fly in and snap together.", "c", "0%{transform:translate(calc((var(--i) - 8) * 6cqw),calc((var(--i) % 3 - 1) * 14cqw)) rotate(calc(var(--i) * 40deg));opacity:0}14%,100%{transform:none;opacity:1}", 2.2, "cubic-bezier(.16,1,.3,1)"),
 ("ink-bleed", "Ink bleed", "F", "Spreads in like ink on paper.", "t", "0%{filter:blur(3cqw);opacity:0;transform:scale(1.05)}50%,100%{filter:none;opacity:1;transform:none}", 2.4, "ease-out"),
 ("page-curl", "Page curl", "F", "Peels in like a page turn.", "t", "0%{transform:perspective(60cqw) rotateY(80deg);transform-origin:0 50%;opacity:.2}40%,100%{transform:none;opacity:1}", 2.0, "cubic-bezier(.16,1,.3,1)"),
 ("bounce", "Bounce", "F", "Drops from above and bounces three times.", "t", "0%{transform:translateY(-160%)}14%{transform:none}20%{transform:translateY(-18%)}26%{transform:none}30%{transform:translateY(-6%)}34%,100%{transform:none}", 2.0, "ease-in"),
 ("unroll", "Unroll", "F", "Unrolls downward like a scroll.", "t", "0%{transform:scaleY(0);transform-origin:50% 0;filter:brightness(.6)}30%{transform:scaleY(1.06);transform-origin:50% 0;filter:none}36%,100%{transform:none}", 1.8, "cubic-bezier(.16,1,.3,1)"),
 ("counter", "Counter roll", "C", "Numbers roll up to the value.", "num", "", 2.2, "linear"),
 ("boil", "Boiling lines", "F", "A hand-drawn wiggle that never quite stops.", "t", "0%{transform:rotate(-.8deg)}25%{transform:rotate(.6deg) translateX(.3%)}50%{transform:rotate(-.4deg)}75%{transform:rotate(.8deg)}100%{transform:none}", 0.5, "steps(1)")]
def ent(eid):
    e = next(x for x in ENTR if x[0] == eid); cid = f"en-{eid}"; kind, frames, dur, ease = e[4], e[5], e[6], e[7]
    if kind == "c":
        css = (f'.card.playing .{cid} .c{{animation:{cid}c {dur}s {ease} 2 both;animation-delay:calc(var(--i) * {dur * 0.03:.3f}s)}}'
               f'@keyframes {cid}c{{{frames}}}')
        return f'<style>{css}</style>' + mv_scene(cid, letters()).replace(f'<div class="l"', f'<div class="l" style="display:none"', 0)
    if kind == "w":
        css = (f'.card.playing .{cid} .w{{animation:{cid}w {dur}s {ease} 2 both;animation-delay:calc(var(--i) * {dur * 0.06:.3f}s)}}'
               f'@keyframes {cid}w{{{frames}}}')
        return f'<style>{css}</style>' + mv_scene(cid, words())
    if kind == "hl":
        th = f'<span class="hl" style="background:linear-gradient({EX2},{EX2}) 0 85%/100% 70% no-repeat;padding:0 1cqw">{TS_T1}</span><br><span class="hl" style="background:linear-gradient({EX2},{EX2}) 0 85%/100% 70% no-repeat;padding:0 1cqw">{TS_T2}</span>'
        css = f'.card.playing .{cid} .hl{{animation:{cid}h {dur}s {ease} 2 both}}@keyframes {cid}h{{{frames}}}'
        return f'<style>{css}</style>' + mv_scene(cid, th)
    if kind == "num":
        digits = ''.join(f'<span style="display:inline-block;height:1em;overflow:hidden;vertical-align:top"><span class="d" style="display:block;--n:{n}">' + '<br>'.join(str(k) for k in range(10)) + '</span></span>' for n in (3, 0))
        th = f'{TS_T1}<br>FOR {digits} DAYS'
        css = (f'.{cid} .d{{transform:translateY(calc(var(--n) * -1em))}}.card.playing .{cid} .d{{animation:{cid}n {dur}s cubic-bezier(.16,1,.3,1) 2 both}}'
               f'@keyframes {cid}n{{0%{{transform:translateY(-9em)}}50%,100%{{transform:translateY(calc(var(--n) * -1em))}}}}')
        return f'<style>{css}</style>' + mv_scene(cid, th)
    it = "infinite" if eid == "boil" else 2
    css = f'.card.playing .{cid} .t{{animation:{cid}t {dur}s {ease} 0s {it} both}}@keyframes {cid}t{{{frames}}}'
    return f'<style>{css}</style>' + mv_scene(cid)
# One page: the entrances grouped under the feel they belong to. Each group opens with a reference card that plays
# the feel itself (title + label together); the group header picks Main / Backup feel; each entrance is kept or not.
GROUPS = [  # id, title, line, the feel card (FEELS id), entrance ids
 ("calm", "Calm", "Slow, soft arrivals. Nothing jumps.", "glide", ["fade-up", "blur", "ink-bleed", "word-stagger", "highlight"]),
 ("smooth", "Smooth", "Clean, measured reveals.", "editorial", ["mask", "wipe", "slide", "rotate", "flip", "page-curl"]),
 ("snappy", "Snappy", "Quick and crisp. In and done.", "snap", ["cut", "zoom", "typewriter", "scramble", "print-out", "counter"]),
 ("punchy", "Punchy", "Big hits that land hard.", "punch", ["slam", "side-slam", "stamp", "glitch", "neon-flicker", "shatter"]),
 ("playful", "Playful", "Bouncy and cartoony.", "playful", ["word-spring", "bounce", "letter-drop", "swing-in", "squash", "unroll", "boil"])]
ENTR_BTN = [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}]
def ent_opt(i):
    e = next(x for x in ENTR if x[0] == i)
    return {"id": i, "name": e[1], "line": e[3], "html": ent(i), "play": True, "playMs": int(e[6] * 2 * 1000 + 300) if i != "boil" else 3000}
def feel_card(gid, fid):
    f = next(x for x in FEELS if x[0] == fid)
    return {"id": "feel-" + gid, "name": "The " + gid + " feel", "line": "Titles and labels together, in this feel.", "html": mf(fid), "play": True, "playMs": FEEL_MS(fid), "control": True,
            **({"pick": True, "why": "Calm and clear: it suits explaining things without rushing."} if gid == "calm" else {})}
W("motion-entrances", {
 "round": "motion-entrances", "kind": "library", "badge": "Pick a feel + library", "fonts": MV_FONTS,
 "title": "Motion feel and how things come in",
 "what": "How titles and labels arrive on screen, grouped by feel. Pick a main feel and a backup, and keep any entrances you like.",
 "purpose": "You're picking how your videos move, and building your library of entrances.",
 "sectionPick": {"word": "feel", "buttons": [{"value": "pick", "label": "Main feel"}, {"value": "backup", "label": "Backup feel"}, {"value": "alt", "label": "Alternative"}]},
 "next": "Next: scene changes.", "persona": SAY_PERSONA,
 "sections": [{"id": g, "title": t, "line": l, "kind": "library", "layout": "tiles", "keepWord": "entrance|entrances", "movable": False, "rule": "keep any entrances you like from this group.",
   "buttons": ENTR_BTN, "keepValues": ["keep"], "options": [feel_card(g, fid)] + [ent_opt(i) for i in ids]} for g, t, l, fid, ids in GROUPS]})
assert sorted(i for *_, ids in GROUPS for i in ids) == sorted(x[0] for x in ENTR), "every entrance sits in one feel group"

# Scene changes: scene A (light) to scene B (dark), then back. Plain scenes, so only the transition is judged.
def scA(): return f'<div style="position:absolute;inset:0;background:{BG};display:flex;align-items:center;padding-left:8%;font:400 12cqw {TITLE};color:{TX}">SCENE 1</div>'
def scB(): return f'<div style="position:absolute;inset:0;background:{TX};display:flex;align-items:center;padding-left:8%;font:400 12cqw {TITLE};color:{HL}">SCENE 2</div>'
TRANS = [  # id, name, tier, line, css for .b (scene B layer) keyframes, extra layer html, extra layer keyframes, dur
 ("hard-cut", "Hard cut", "C", "Straight to the next shot.", "0%,45%{opacity:0}46%,100%{opacity:1}", "", "", 2.0),
 ("dissolve", "Dissolve", "C", "One shot melts into the next.", "0%,25%{opacity:0}65%,100%{opacity:1}", "", "", 2.2),
 ("soft-rise", "Soft rise", "C", "The next shot rises gently into place.", "0%,25%{opacity:0;transform:translateY(10%)}60%,100%{opacity:1;transform:none}", "", "", 2.2),
 ("color-wipe", "Color wipe", "R", "A band of your color sweeps across.", "0%,45%{clip-path:inset(0 100% 0 0)}46%,100%{clip-path:inset(0 0 0 0)}", f'<div class="x" style="position:absolute;inset:0;background:{HL};transform:translateX(-101%)"></div>', "0%,15%{transform:translateX(-101%)}45%{transform:translateX(0)}75%,100%{transform:translateX(101%)}", 2.2),
 ("split-slide", "Split slide", "R", "The shot splits and slides apart.", "0%,100%{opacity:1}", f'<div class="x" style="position:absolute;inset:0 50% 0 0;overflow:hidden">{scA()}</div><div class="y" style="position:absolute;inset:0 0 0 50%;overflow:hidden"><div style="position:absolute;inset:0 0 0 -100%">{scA()}</div></div>', "0%,25%{transform:none}65%,100%{transform:translateX(-101%)}", 2.2),
 ("whip-pan", "Whip pan", "R", "A fast blurred swish to the next shot.", "0%,40%{transform:translateX(100%);filter:blur(3cqw)}60%{transform:none;filter:blur(1cqw)}70%,100%{filter:none;transform:none}", "", "", 2.0),
 ("zoom-through", "Zoom through", "R", "Flies through the shot into the next one.", "0%,40%{opacity:0;transform:scale(.6)}65%,100%{opacity:1;transform:none}", "", "", 2.2),
 ("slice-shift", "Slice shift", "R", "Strips slide away to reveal the next shot.", "0%,100%{opacity:1}", ''.join(f'<div class="x{k}" style="position:absolute;left:0;right:0;top:{k*25}%;height:25%;overflow:hidden"><div style="position:absolute;left:0;right:0;top:{-k*100}%;height:400%">{scA()}</div></div>' for k in range(4)), "", 2.2),
 ("iris", "Iris", "F", "A circle closes and opens, old-cartoon style.", "0%,45%{clip-path:circle(0% at 50% 50%)}75%,100%{clip-path:circle(75% at 50% 50%)}", "", "", 2.4),
 ("film-burn", "Film burn", "F", "A warm light burn flares between shots.", "0%,45%{opacity:0}50%,100%{opacity:1}", '<div class="x" style="position:absolute;inset:0;background:radial-gradient(circle at 70% 40%,#fff6d0,#ffb347 30%,#d1401a 60%,transparent 80%);opacity:0;mix-blend-mode:screen"></div>', "0%,25%{opacity:0}45%{opacity:1}75%,100%{opacity:0}", 2.4),
 ("spin-blur", "Spin blur", "F", "The shot spins away into the next.", "0%,40%{opacity:0;transform:rotate(-40deg) scale(.6);filter:blur(2cqw)}65%,100%{opacity:1;transform:none;filter:none}", "", "", 2.2),
 ("pixel", "Pixel dissolve", "F", "Breaks into blocks and rebuilds.", "0%,30%{opacity:0;filter:blur(2.5cqw) contrast(6)}55%{opacity:1;filter:blur(1cqw) contrast(3)}70%,100%{filter:none}", "", "", 2.2),
 ("ink-wipe", "Ink wipe", "F", "An ink blot spreads into the next shot.", "0%,30%{clip-path:circle(0% at 30% 60%)}70%,100%{clip-path:circle(85% at 30% 60%)}", "", "", 2.4),
 # break-from-reality transitions
 ("record-scratch", "Record scratch", "F", "Freeze, a scratch, then the next shot.", "0%,55%{opacity:0}56%,100%{opacity:1}", f'<div class="x" style="position:absolute;inset:0;background:rgba(0,0,0,.35);opacity:0;display:flex;align-items:flex-end;padding:5%"><span style="background:#fff;color:#111;font:800 4.4cqw {TEXT};padding:.6cqw 1.6cqw;transform:rotate(-4deg)">*record scratch*</span></div>', "0%,20%{opacity:0}22%,54%{opacity:1}55%,100%{opacity:0}", 2.6),
 ("page-tear", "Page tear", "F", "The shot rips away like paper.", "0%,100%{opacity:1}", f'<div class="x" style="position:absolute;inset:0;clip-path:polygon(0 0,55% 0,48% 18%,57% 36%,47% 55%,56% 74%,49% 100%,0 100%)">{scA()}</div><div class="y" style="position:absolute;inset:0;clip-path:polygon(55% 0,100% 0,100% 100%,49% 100%,56% 74%,47% 55%,57% 36%,48% 18%)">{scA()}</div>', "0%,25%{transform:none}65%,100%{transform:translateX(-110%) rotate(-8deg)}", 2.4),
 ("cartoon-whip", "Cartoon whip", "F", "Speed lines and a zip to the next shot.", "0%,45%{transform:translateX(100%)}55%,100%{transform:none}", ''.join(f'<div class="x" style="position:absolute;left:0;right:0;top:{12+k*15}%;height:1.2cqw;background:#fff;opacity:0;transform-origin:0 50%"></div>' for k in range(6)), "0%,30%{opacity:0;transform:scaleX(0)}42%{opacity:.9;transform:scaleX(1)}55%,100%{opacity:0;transform:scaleX(1)}", 2.2),
 ("tv-static", "TV static", "F", "A burst of static between shots.", "0%,52%{opacity:0}53%,100%{opacity:1}", '<div class="x" style="position:absolute;inset:0;opacity:0;background:repeating-radial-gradient(circle at 17% 32%,#fff 0 1px,#555 1px 2px,#111 2px 3px),repeating-linear-gradient(0deg,rgba(255,255,255,.2) 0 1px,transparent 1px 3px);background-size:7px 7px,100% 100%"></div>', "0%,30%{opacity:0}32%,52%{opacity:1}53%,100%{opacity:0}", 2.4),
 ("comic-panel", "Comic panels", "F", "The screen splits into comic panels.", "0%,45%{clip-path:polygon(0 0,0 0,0 100%,0 100%)}75%,100%{clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}", '<div class="x" style="position:absolute;inset:0;opacity:0;background:linear-gradient(115deg,transparent 48%,#000 48% 52%,transparent 52%),linear-gradient(0deg,transparent 48%,#000 48% 52%,transparent 52%);border:1.2cqw solid #000"></div>', "0%,25%{opacity:0}35%,60%{opacity:1}75%,100%{opacity:0}", 2.4),
 ("tv-off", "TV switch-off", "F", "Squeezes to a line like an old TV.", "0%,45%{opacity:0}46%,100%{opacity:1}", f'<div class="x" style="position:absolute;inset:0">{scA()}</div>', "0%,15%{transform:none}35%{transform:scaleY(.02)}45%,100%{transform:scale(0,.02);opacity:0}", 2.2)]
BFR_T = {"record-scratch", "page-tear", "cartoon-whip", "tv-static", "comic-panel", "tv-off"}
def trn(tid):
    t = next(x for x in TRANS if x[0] == tid); cid = f"tr-{tid}"; bkf, layer, lkf, dur = t[4], t[5], t[6], t[7]
    css = f'.{cid} .b{{opacity:0}}.card.playing .{cid} .b{{animation:{cid}b {dur}s ease-in-out 0s 2 both}}@keyframes {cid}b{{{bkf}}}'
    if tid == "slice-shift":
        css += ''.join(f'.card.playing .{cid} .x{k}{{animation:{cid}s {dur}s cubic-bezier(.65,0,.35,1) {k*0.06:.2f}s 2 both}}' for k in range(4)) + f'@keyframes {cid}s{{0%,25%{{transform:none}}65%,100%{{transform:translateX(-101%)}}}}'
        css += f'.{cid} .b{{opacity:1}}.{cid} [class^=x]{{display:none}}.card.playing .{cid} [class^=x]{{display:block}}'
        lay = layer
    elif tid in ("split-slide", "page-tear"):
        css += f'.{cid} .b{{opacity:1}}.{cid} .x,.{cid} .y{{display:none}}.card.playing .{cid} .x,.card.playing .{cid} .y{{display:block}}'
        css += f'.card.playing .{cid} .x{{animation:{cid}x {dur}s cubic-bezier(.65,0,.35,1) 0s 2 both}}@keyframes {cid}x{{{lkf}}}'
        css += f'.card.playing .{cid} .y{{animation:{cid}y {dur}s cubic-bezier(.65,0,.35,1) 0s 2 both}}@keyframes {cid}y{{{lkf.replace("-110%) rotate(-8deg)", "110%) rotate(8deg)").replace("translateX(-101%)", "translateX(101%)")}}}'
        lay = layer
    else:
        lay = layer
        if lkf: css += f'.card.playing .{cid} .x{{animation:{cid}x {dur}s ease-in-out 0s 2 both}}@keyframes {cid}x{{{lkf}}}'
        if tid == "tv-off": css += f'.{cid} .x{{display:none}}.card.playing .{cid} .x{{display:block}}'
    static_b = f'.card:not(.playing) .{cid} .b{{opacity:1;clip-path:inset(0 0 0 50%)}}'   # static: half scene 1, half scene 2
    return (f'<style>{css}{static_b}</style><div class="{cid}" style="position:absolute;inset:0;container-type:size;overflow:hidden">'
            f'{scA()}<div class="b" style="position:absolute;inset:0">{scB()}</div>{lay}</div>')
W("scene-changes", {
 "round": "scene-changes", "kind": "library", "layout": "tiles", "fonts": MV_FONTS, "keepWord": "scene change|scene changes",
 "title": "Scene changes", "what": "How one shot turns into the next. Press Play on each.",
 "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "keepValues": ["keep"],
 "next": "Next: four plain lines on how your feel plays out, for you to confirm. Then Sound.", "persona": SAY_PERSONA,
 "sections": [{"id": "standard", "title": "Everyday", "kind": "library", "keepWord": "scene change|scene changes", "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "keepValues": ["keep"], "layout": "tiles", "movable": False,
   "options": [{"id": i, "name": n, "line": l, "html": trn(i), "play": True, "playMs": int(d * 2 * 1000 + 200)} for i, n, t, l, b, x, y, d in TRANS if i not in BFR_T]},
  {"id": "bfr", "title": "Break-from-reality transitions", "line": "Playful ones, for a joke or a big moment.", "kind": "library", "keepWord": "scene change|scene changes", "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "keepValues": ["keep"], "layout": "tiles", "movable": False,
   "options": [{"id": i, "name": n, "line": l, "html": trn(i), "play": True, "playMs": int(d * 2 * 1000 + 200)} for i, n, t, l, b, x, y, d in TRANS if i in BFR_T]}]})

# ---------- 13. Sound: music (library) ----------
# Each card plays a 4-bar sketch of the lane (drums + bass + chords at the lane's tempo) made in Web Audio,
# so the page needs no files. Play/Pause on the big button. The sketch is a recipe, not the final track.
MUSIC = [  # id, name, tier, line, bpm, kick, snare, hat, bass(root midi per bar), chord intervals, bassWave, padWave, extra
 ("lofi", "Lo-fi beats", "C", "Relaxed and warm. Good under talking.", 80, "x.....x...x.....", "....x.......x...", "x.x.x.x.x.x.x.x.", [45, 43, 41, 40], [0, 3, 7, 10], "triangle", "sine", "crackle"),
 ("acoustic", "Light acoustic", "C", "Bright and friendly. Good under talking.", 105, "x.......x.......", "....x.......x...", "..x...x...x...x.", [48, 43, 45, 41], [0, 4, 7], "triangle", "triangle", "pluck"),
 ("indie-pop", "Indie pop", "C", "Upbeat and hopeful. Good for montages.", 115, "x...x...x...x...", "....x.......x...", "x.x.x.x.x.x.x.x.", [43, 47, 45, 41], [0, 4, 7], "sawtooth", "square", ""),
 ("minimal", "Minimal electronic", "C", "Focused and modern. Good under explaining.", 118, "x...x...x...x...", "........x.......", ".x.x.x.x.x.x.x.x", [41, 41, 44, 39], [0, 3, 7], "sine", "sine", "arp"),
 ("boom-bap", "Boom bap", "C", "Confident swagger. Good for intros.", 90, "x......x..x.....", "....x.......x...", "x.x.x.x.x.x.x.x.", [38, 38, 41, 36], [0, 3, 7], "sine", "triangle", ""),
 ("cinematic", "Cinematic build", "C", "Rising and epic. Good for reveals.", 96, "x.......x.......", "................", "................", [36, 41, 43, 44], [0, 7, 12, 16], "sawtooth", "sawtooth", "rise"),
 ("tropical", "Tropical house", "C", "Sunny and light. Good for travel and wins.", 108, "x...x...x...x...", "....x.......x...", "..x...x...x...x.", [45, 41, 48, 43], [0, 4, 7], "sine", "triangle", "marimba"),
 ("funk", "Funk", "R", "Groovy and playful. Good for fast fixes.", 108, "x..x..x...x.....", "....x.......x...", "xxxxxxxxxxxxxxxx", [40, 40, 45, 43], [0, 4, 7, 10], "square", "square", ""),
 ("jazz", "Jazz trio", "R", "Smart, late-night. Good under talking.", 120, "x.........x.....", "......x.......x.", "x..x.xx..x.xx..x", [41, 46, 39, 44], [0, 4, 7, 11], "triangle", "sine", ""),
 ("synthwave", "Synthwave", "R", "Retro, nighttime drive. Good for intros.", 100, "x...x...x...x...", "....x.......x...", "x.x.x.x.x.x.x.x.", [45, 41, 43, 40], [0, 3, 7], "sawtooth", "sawtooth", "arp"),
 ("tension", "Tension pulse", "R", "Suspense. Good before a reveal.", 128, "x.......x.......", "................", "x.x.x.x.x.x.x.x.", [38, 38, 39, 39], [0, 1], "sawtooth", "sine", "tick"),
 ("ambient", "Ambient", "R", "Calm and spacious. Good for thoughtful parts.", 70, "................", "................", "................", [40, 45, 43, 38], [0, 7, 12, 16], "sine", "sine", ""),
 ("chiptune", "Chiptune", "F", "Retro game, playful. Good for jokes.", 140, "x...x...x...x...", "....x.......x...", "x.x.x.x.x.x.x.x.", [48, 45, 41, 43], [0, 4, 7, 12], "square", "square", "arp"),
 ("western", "Desert western", "F", "Dramatic standoff, wry. Good for showdowns.", 88, "x.......x.......", "....x.......x...", "................", [40, 40, 43, 38], [0, 7], "triangle", "triangle", "twang"),
 ("pizzicato", "Mischief pizzicato", "F", "Sneaky and comic. Good for little disasters.", 120, "x.......x.......", "................", "................", [43, 41, 40, 38], [0, 4, 7], "triangle", "triangle", "pluck"),
 ("elevator", "Elevator bossa", "F", "Ironic and calm. Good for deadpan bits.", 112, "x..x..x.x..x..x.", "....x.......x...", "..x...x...x...x.", [41, 46, 44, 39], [0, 4, 7, 11], "sine", "sine", "")]
MUSIC_JS = r'''<script>
(function(){
  var ctx = null, playing = {};
  function ac(){ if(!ctx){ ctx = new (window.AudioContext||window.webkitAudioContext)(); } if(ctx.state==='suspended') ctx.resume(); return ctx; }
  function mtof(m){ return 440*Math.pow(2,(m-69)/12); }
  function env(g,t,a,d,v){ g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(v,t+a); g.gain.exponentialRampToValueAtTime(0.0001,t+a+d); }
  function osc(type,f,t,dur,v,out){ var o=ctx.createOscillator(), g=ctx.createGain(); o.type=type; o.frequency.setValueAtTime(f,t); o.connect(g); g.connect(out); env(g,t,0.01,dur,v); o.start(t); o.stop(t+dur+0.05); return o; }
  function noise(t,dur,v,hp,out){ var n=ctx.createBufferSource(), b=ctx.createBuffer(1,ctx.sampleRate*dur,ctx.sampleRate), d=b.getChannelData(0); for(var i=0;i<d.length;i++) d[i]=Math.random()*2-1; n.buffer=b; var f=ctx.createBiquadFilter(); f.type='highpass'; f.frequency.value=hp; var g=ctx.createGain(); n.connect(f); f.connect(g); g.connect(out); env(g,t,0.002,dur,v); n.start(t); n.stop(t+dur); }
  function kick(t,out){ var o=ctx.createOscillator(), g=ctx.createGain(); o.frequency.setValueAtTime(140,t); o.frequency.exponentialRampToValueAtTime(42,t+0.18); o.connect(g); g.connect(out); env(g,t,0.003,0.28,0.9); o.start(t); o.stop(t+0.35); }
  window.bgMusic = function(id, el){
    var L = (window.BG_MUSIC||{})[id]; if(!L) return; window.bgMusicStop(id, el); ac();
    var out = ctx.createGain(); out.gain.value = 0.55; out.connect(ctx.destination); playing[id] = out;
    var t0 = ctx.currentTime + 0.06, s = 60/L.bpm/4;   // 16th-note length
    for (var bar=0; bar<4; bar++) for (var st=0; st<16; st++){
      var t = t0 + (bar*16+st)*s;
      if (L.kick[st]==='x') kick(t,out);
      if (L.snare[st]==='x') noise(t,0.16,0.35,1200,out);
      if (L.hat[st]==='x') noise(t,0.04,0.12,7000,out);
      var root = L.bass[bar];
      if (st%4===0 && L.kick.indexOf('x')>=0 || (L.kick.indexOf('x')<0 && st===0)) osc(L.bw, mtof(root), t, s*3.5, 0.28, out);
      if (st===0) L.chord.forEach(function(iv){ osc(L.pw, mtof(root+24+iv), t, s*15, L.pw==='sawtooth'||L.pw==='square'?0.035:0.07, out); });
      if (L.x==='arp' && st%2===0) osc('square', mtof(root+36+L.chord[(st/2)%L.chord.length]), t, s*1.2, 0.04, out);
      if ((L.x==='pluck'||L.x==='marimba'||L.x==='twang') && (st===0||st===6||st===10)) osc(L.x==='twang'?'sawtooth':'triangle', mtof(root+24+L.chord[(st/2)%L.chord.length]), t, s*2, 0.12, out);
      if (L.x==='tick' && st%2===0) noise(t,0.015,0.2,9000,out);
      if (L.x==='crackle' && Math.random()<0.4) noise(t+Math.random()*s,0.01,0.05,3000,out);
      if (L.x==='rise' && st===0 && bar===3) { var o=ctx.createOscillator(), g=ctx.createGain(); o.type='sawtooth'; o.frequency.setValueAtTime(200,t); o.frequency.exponentialRampToValueAtTime(1200,t+16*s); o.connect(g); g.connect(out); g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(0.06,t+16*s); o.start(t); o.stop(t+16*s); }
    }
  };
  window.bgMusicStop = function(id){ var out = playing[id]; if(out){ try{ out.gain.setTargetAtTime(0.0001, ctx.currentTime, 0.03); setTimeout(function(){ out.disconnect(); }, 200); }catch(e){} delete playing[id]; } };
})();
</script>'''
def music_card(m):
    i, n, t, l, bpm = m[0], m[1], m[2], m[3], m[4]
    bars = ''.join(f'<i style="animation-delay:-{(k*0.37)%1:.2f}s"></i>' for k in range(18))
    return (f'<div class="mu" style="position:absolute;inset:0;container-type:size;background:{TX};color:{BG};padding:7% 8%;display:flex;flex-direction:column;justify-content:space-between">'
            f'<div style="font:400 10cqw/1 {TITLE};color:{BG}">{n}</div>'
            f'<div class="eq" style="display:flex;align-items:flex-end;gap:1.2cqw;height:24cqw">{bars}</div>'
            f'<div style="font:700 3.6cqw {TEXT};color:{HL}">{bpm} BPM · 4-bar sketch</div></div>')
MUSIC_CSS = (f'<style>.mu .eq i{{display:block;flex:1;background:{HL};height:22%;border-radius:.6cqw .6cqw 0 0;opacity:.55}}'
             '.card.playing .mu .eq i{animation:eqb .5s ease-in-out infinite alternate;opacity:1}'
             '@keyframes eqb{0%{height:15%}50%{height:85%}100%{height:35%}}</style>')
MUSIC_DATA = '<script>window.BG_MUSIC=' + json.dumps({m[0]: {"bpm": m[4], "kick": m[5], "snare": m[6], "hat": m[7], "bass": m[8], "chord": m[9], "bw": m[10], "pw": m[11], "x": m[12]} for m in MUSIC}) + ';</script>'
W("music", {
 "round": "music", "kind": "library", "layout": "tiles", "fonts": ["bebas-neue", "inter"], "keepWord": "kind of music|kinds of music",
 "head": MUSIC_CSS + MUSIC_DATA + MUSIC_JS,
 "title": "Music", "what": "Sketches of each kind of music (its tempo and energy). Your library saves the recipe; real tracks are made from it when a video is edited.",
 "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "keepValues": ["keep"],
 "next": "Next: sound effects.", "persona": SAY_PERSONA,
 "options": [{"id": m[0], "name": m[1], "line": m[3], "html": music_card(m), "play": "bgMusic", "playMs": int(64 * 60 / m[4] / 4 * 1000 + 400)} for m in MUSIC]})

# ---------- 14. Kit: wordmark (fixed, Main + Backup) ----------
# Quality bar: the original wordmark round. ~12 clearly different marks, each shown where it lives
# (end card, profile picture, corner of a video), in the creator's palette, with a built-in device where it helps.
WM_NAME, WM_HANDLE, WM_INIT = "Wren", "@wren", "W"
def bc(n, seed, h="9cqw"):
    s, out = seed, ""
    for i in range(n):
        s = (s * 9301 + 49297) % 233280; w = 1 + int(s / 233280 * 3.2); g = (1 + (s >> 3) % 2) if i % 2 else 0
        out += f'<u style="display:block;background:currentColor;width:{w*.36:.2f}cqw;margin-right:{(g+.6)*.36:.2f}cqw"></u>'
    return f'<span style="display:flex;align-items:stretch;height:{h}">{out}</span>'
SWOOSH = f'<svg viewBox="0 0 200 30" style="width:62cqw;height:auto;margin-top:-4cqw"><path d="M6 20 C 50 6, 110 4, 150 14 S 190 22, 196 8" fill="none" stroke="{HL}" stroke-width="3" stroke-linecap="round"/></svg>'
F = {"anton": "'Anton',Impact,sans-serif", "unb": "'Unbounded',Arial,sans-serif", "fr": "'Fraunces',Georgia,serif", "is": "'Instrument Serif',Georgia,serif",
     "mono": MONO, "cav": NOTES, "pm": "'Permanent Marker',cursive", "se": "'Special Elite',monospace", "bow": "'Bowlby One',Impact,sans-serif", "beb": TITLE, "int": TEXT}
WMS = [  # id, name, tier, line, end card html, avatar html, corner html
 ("episode-pill", "Episode pill", "C", "Your name with an episode number that changes every video.",
  f'<div style="display:grid;gap:2.4cqw;justify-items:start"><div style="font:400 17cqw/.85 {F["anton"]};letter-spacing:.01em">{WM_NAME.upper()}</div><div style="display:flex;gap:2.4cqw;align-items:center"><span style="font:800 4.6cqw/1 {F["int"]};background:{HL};color:{BG};padding:1cqw 2.4cqw;border-radius:99cqw">EP 12</span><span style="font:600 4.2cqw/1 {F["int"]}">{WM_HANDLE}</span></div></div>',
  f'<div style="display:grid;justify-items:center;gap:3cqw"><div style="font:400 44cqw/.8 {F["anton"]}">{WM_INIT}</div><span style="font:800 9cqw/1 {F["int"]};background:{HL};color:{BG};padding:2cqw 4cqw;border-radius:99cqw">EP 12</span></div>',
  f'<div style="display:flex;gap:1.4cqw;align-items:center;font:400 6cqw/1 {F["anton"]}">{WM_NAME.upper()} <span style="font:800 2.8cqw {F["int"]};background:{HL};color:{BG};padding:.6cqw 1.2cqw;border-radius:99cqw">EP 12</span></div>'),
 ("stacked", "Stacked block", "C", "Big, solid letters, like a poster. Very readable on thumbnails.",
  f'<svg viewBox="0 0 100 46" style="width:70cqw"><text x="0" y="40" textLength="100" lengthAdjust="spacingAndGlyphs" font-size="52" font-family="Anton,Impact,sans-serif" fill="currentColor">{WM_NAME.upper()}</text><rect x="0" y="43" width="100" height="3" fill="{HL}"/></svg>',
  f'<svg viewBox="0 0 100 100" style="width:60cqw"><text x="50" y="86" text-anchor="middle" font-size="110" font-family="Anton,Impact,sans-serif" fill="currentColor">{WM_INIT}</text><rect x="20" y="92" width="60" height="6" fill="{HL}"/></svg>',
  f'<div style="font:400 6.4cqw/1 {F["anton"]};border-bottom:.6cqw solid {HL}">{WM_NAME.upper()}</div>'),
 ("monogram-box", "Monogram box", "C", "An initial in a square with one color corner. Clean at tiny sizes.",
  f'<div style="display:flex;align-items:center;gap:4cqw"><div style="position:relative;border:1.2cqw solid currentColor;display:grid;place-items:center;font:800 11cqw/1 {F["unb"]};width:24cqw;aspect-ratio:1">{WM_INIT}<i style="position:absolute;right:-1.2cqw;bottom:-1.2cqw;width:6cqw;height:6cqw;background:{HL}"></i></div><div style="display:grid;gap:2cqw"><div style="font:400 8cqw/1 {F["unb"]}">{WM_NAME}</div><div style="font:800 3.8cqw/1 {F["unb"]};color:{HL}">{WM_HANDLE}</div></div></div>',
  f'<div style="position:relative;border:3cqw solid currentColor;display:grid;place-items:center;font:800 24cqw/1 {F["unb"]};width:52cqw;aspect-ratio:1">{WM_INIT}<i style="position:absolute;right:-3cqw;bottom:-3cqw;width:13cqw;height:13cqw;background:{HL}"></i></div>',
  f'<div style="position:relative;border:.5cqw solid currentColor;display:grid;place-items:center;font:800 4cqw/1 {F["unb"]};width:9cqw;aspect-ratio:1">{WM_INIT}<i style="position:absolute;right:-.5cqw;bottom:-.5cqw;width:2.2cqw;height:2.2cqw;background:{HL}"></i></div>'),
 ("editorial", "Editorial serif", "C", "An elegant serif name with a colored full stop.",
  f'<div style="display:grid;gap:1cqw;justify-items:start"><div style="font:400 19cqw/.9 {F["is"]};letter-spacing:-.01em">{WM_NAME}<span style="color:{HL}">.</span></div><div style="font:italic 400 5cqw/1 {F["is"]};opacity:.75">{WM_HANDLE}</div></div>',
  f'<div style="font:400 50cqw/1 {F["is"]}">{WM_INIT}<span style="color:{HL}">.</span></div>',
  f'<div style="font:400 7cqw/1 {F["is"]}">{WM_NAME}<span style="color:{HL}">.</span></div>'),
 ("signature", "Signature", "R", "Your name, handwritten, with a swoosh. The most personal.",
  f'<div style="display:grid;justify-items:center;gap:1cqw"><div style="font:700 21cqw/1 {F["cav"]};transform:rotate(-4deg)">{WM_NAME}</div>{SWOOSH}<div style="font:700 5cqw/1 {F["cav"]};opacity:.8">{WM_HANDLE}</div></div>',
  f'<div style="display:grid;justify-items:center"><div style="font:700 52cqw/.9 {F["cav"]};transform:rotate(-6deg)">{WM_INIT}</div></div>',
  f'<div style="font:700 8cqw/1 {F["cav"]};transform:rotate(-4deg)">{WM_NAME}</div>'),
 ("progress", "Progress bar", "R", "Your name over a bar that fills a little more each video.",
  f'<div style="width:70cqw;display:grid;gap:2.6cqw"><div style="font:400 15cqw/.9 {F["beb"]}">{WM_NAME.upper()}</div><div style="height:2.4cqw;background:rgba(127,127,127,.25)"><i style="display:block;width:60%;height:100%;background:{HL}"></i></div><div style="display:flex;justify-content:space-between;font:600 4cqw/1 {F["int"]}"><span>{WM_HANDLE}</span><span style="color:{HL};font-weight:800">day 18 / 30</span></div></div>',
  f'<div style="width:62cqw;display:grid;gap:5cqw"><div style="font:400 44cqw/.8 {F["beb"]};text-align:center">{WM_INIT}</div><div style="height:6cqw;background:rgba(127,127,127,.3)"><i style="display:block;width:60%;height:100%;background:{HL}"></i></div></div>',
  f'<div style="width:14cqw;display:grid;gap:.8cqw"><div style="font:400 5cqw/1 {F["beb"]}">{WM_NAME.upper()}</div><div style="height:.8cqw;background:rgba(255,255,255,.3)"><i style="display:block;width:60%;height:100%;background:{HL}"></i></div></div>'),
 ("label", "Label", "R", "A printed label with a barcode; the episode number is the code.",
  f'<div style="background:{BG};border:.8cqw solid currentColor;width:68cqw;display:grid;transform:rotate(-1.5deg)"><div style="display:flex;justify-content:space-between;align-items:flex-end;padding:2.4cqw 3cqw 1.6cqw;border-bottom:.5cqw solid currentColor"><span style="font:400 13cqw/.85 {F["anton"]}">{WM_NAME.upper()}</span><span style="font:800 4.4cqw/1 {F["int"]};background:{HL};color:{BG};padding:.8cqw 1.6cqw">EP 012</span></div><div style="display:flex;gap:3cqw;align-items:center;padding:2cqw 3cqw">{bc(34, 7)}<span style="font:600 3.8cqw/1.15 {F["int"]}">{WM_HANDLE}</span></div></div>',
  f'<div style="display:grid;justify-items:center;gap:3cqw"><div style="font:400 38cqw/.85 {F["anton"]}">{WM_INIT}</div><span style="color:{HL}">{bc(20, 3, "12cqw")}</span></div>',
  f'<div style="display:grid;gap:.6cqw;justify-items:end"><span style="font:400 5cqw/.9 {F["anton"]}">{WM_NAME.upper()}</span>{bc(16, 5, "2.4cqw")}</div>'),
 ("marker", "Marker", "R", "Bold marker lettering with a scribbled underline.",
  f'<div style="display:grid;justify-items:start"><div style="font:400 18cqw/1 {F["pm"]};transform:rotate(-3deg)">{WM_NAME}</div><svg viewBox="0 0 200 24" style="width:56cqw;margin-top:-2cqw"><path d="M4 14 C 60 4, 120 22, 196 8 M 20 20 C 80 12, 140 22, 180 16" fill="none" stroke="{HL}" stroke-width="5" stroke-linecap="round"/></svg></div>',
  f'<div style="font:400 50cqw/1 {F["pm"]};transform:rotate(-6deg)">{WM_INIT}</div>',
  f'<div style="font:400 6.6cqw/1 {F["pm"]};transform:rotate(-3deg)">{WM_NAME}</div>'),
 ("seal", "Round seal", "R", "Your name around a circle, like a badge or stamp.",
  f'<svg viewBox="0 0 120 120" style="width:40cqw"><defs><path id="wmc" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs><circle cx="60" cy="60" r="56" fill="none" stroke="currentColor" stroke-width="3"/><circle cx="60" cy="60" r="32" fill="{HL}"/><text font-family="Inter,Arial,sans-serif" font-weight="800" font-size="12" letter-spacing="3" fill="currentColor"><textPath href="#wmc">{WM_NAME.upper()} · {WM_HANDLE.upper()} · {WM_NAME.upper()} ·</textPath></text><text x="60" y="71" text-anchor="middle" font-family="Anton,Impact,sans-serif" font-size="32" fill="{BG}">{WM_INIT}</text></svg>',
  f'<svg viewBox="0 0 120 120" style="width:84cqw"><circle cx="60" cy="60" r="40" fill="{HL}"/><text x="60" y="76" text-anchor="middle" font-family="Anton,Impact,sans-serif" font-size="46" fill="{TX}">{WM_INIT}</text></svg>',
  f'<svg viewBox="0 0 120 120" style="width:10cqw"><circle cx="60" cy="60" r="56" fill="{HL}"/><text x="60" y="80" text-anchor="middle" font-family="Anton,Impact,sans-serif" font-size="60" fill="{TX}">{WM_INIT}</text></svg>'),
 ("typewriter", "Typewriter", "F", "Typed out on an old typewriter, with a blinking cursor.",
  f'<div style="font:400 14cqw/1 {F["se"]}">{WM_NAME.lower()}<span style="display:inline-block;width:.5em;height:.9em;background:{HL};margin-left:.1em;vertical-align:-.1em"></span><div style="font:400 4.4cqw/1 {F["se"]};opacity:.75;margin-top:2cqw">{WM_HANDLE}</div></div>',
  f'<div style="font:400 40cqw/1 {F["se"]}">{WM_INIT.lower()}<span style="display:inline-block;width:.45em;height:.8em;background:{HL};vertical-align:-.05em"></span></div>',
  f'<div style="font:400 6cqw/1 {F["se"]}">{WM_NAME.lower()}<span style="display:inline-block;width:.45em;height:.85em;background:{HL};vertical-align:-.1em"></span></div>'),
 ("bubble", "Speech bubble", "F", "Your name in a chunky speech bubble.",
  f'<div style="position:relative;background:{HL};color:{BG};font:400 12cqw/1 {F["bow"]};padding:3cqw 6cqw;border-radius:6cqw">{WM_NAME.lower()}!<i style="position:absolute;left:12%;bottom:-3.6cqw;border:3cqw solid transparent;border-top-color:{HL};border-left-color:{HL}"></i></div>',
  f'<div style="position:relative;background:{HL};color:{TX};font:400 32cqw/1 {F["bow"]};padding:6cqw 10cqw;border-radius:12cqw">{WM_INIT}!</div>',
  f'<div style="background:{HL};color:{BG};font:400 4.6cqw/1 {F["bow"]};padding:1cqw 2cqw;border-radius:2cqw">{WM_NAME.lower()}!</div>'),
 ("slash", "Split color", "F", "Half your name in one color, half in another.",
  f'<div style="font:400 20cqw/.9 {F["anton"]};letter-spacing:.02em"><span>{WM_NAME[:2].upper()}</span><span style="color:{HL}">{WM_NAME[2:].upper()}</span><div style="font:700 4.2cqw/1 {F["int"]};letter-spacing:.4cqw;margin-top:1.6cqw">{WM_HANDLE.upper()}</div></div>',
  f'<div style="font:400 44cqw/.9 {F["anton"]}">{WM_NAME[:1].upper()}<span style="color:{HL}">{WM_NAME[1:2].upper()}</span></div>',
  f'<div style="font:400 6.4cqw/1 {F["anton"]}">{WM_NAME[:2].upper()}<span style="color:{HL}">{WM_NAME[2:].upper()}</span></div>')]
def wm_card(w):
    _, n, t, l, full, av, bug = w
    cap = lambda s: f'<div style="font:600 2.6cqw {TEXT};color:#666;margin-top:.8cqw">{s}</div>'
    return (f'<div style="position:absolute;inset:0;container-type:size;background:#e4e6e5;padding:2.4%;display:grid;grid-template-rows:auto auto;gap:2cqw;align-content:start">'
            f'<div><div style="position:relative;aspect-ratio:16/9;container-type:inline-size;background:{BG};color:{TX};display:grid;place-items:center;border-radius:.6cqw;overflow:hidden">{full}</div>{cap("Closing card")}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1.78fr;gap:2cqw;align-items:start">'
            f'<div><div style="aspect-ratio:1;container-type:inline-size;background:{TX};color:{BG};border-radius:50%;display:grid;place-items:center;overflow:hidden">{av}</div>{cap("Profile picture")}</div>'
            f'<div><div style="position:relative;aspect-ratio:16/9;container-type:inline-size;background:url({FACE}) center/cover;border-radius:.6cqw;overflow:hidden;color:#fff"><div style="position:absolute;inset:0;background:radial-gradient(ellipse at 100% 100%,rgba(0,0,0,.55),transparent 45%)"></div><div style="position:absolute;right:4cqw;bottom:4cqw;transform:scale(1.7);transform-origin:100% 100%;text-shadow:0 .3cqw 1.2cqw rgba(0,0,0,.6)">{bug}</div></div>{cap("Corner of a video")}</div></div></div>')
WM_FONTS = ["anton", "unbounded", "fraunces", "instrument-serif", "space-mono", "caveat", "permanent-marker", "special-elite", "bowlby-one", "bebas-neue", "inter"]
finalist_flow("wordmark", "Wordmark", "Your name set as a logo, shown where it lives: a closing card, your profile picture and the corner of a video.",
 [{"id": w[0], "name": w[1], "line": w[3], "html": wm_card(w), **({"pick": True, "why": "The episode number gives every video a reason to exist in a series."} if w[0] == "episode-pill" else {})} for w in WMS],
 ["episode-pill"] + [w[0] for w in WMS[1:4]], "Next: your name tag.", WM_FONTS, aspect="16/17.5")

# ---------- 14b. Kit: name tag (finalists -> pick) ----------
# The tag with their name when they first speak, over the face frame, in the clear space beside the speaker.
NT_NAME, NT_SUB = NAME_TAG.split(" · ")
def nt_html(x):
    return (f'<img src="{FACE}" style="{FRAMED}"><div style="position:absolute;inset:0;background:radial-gradient(ellipse 60% 55% at 15% 82%,rgba(0,0,0,.45),transparent 75%)"></div>'
            f'<div style="position:absolute;inset:0;container-type:size"><div style="position:absolute;left:5%;bottom:12%">{x[4]}</div></div>')
NTAGS = [  # id, name, tier, line, html
 ("bar", "Side bar", "C", "Name on a bar with a stripe of your color.", f'<div style="background:{BG};border-left:1.4cqw solid {HL};padding:1.2cqw 2.6cqw"><div style="font:800 4.4cqw/1.1 {TEXT};color:{TX}">{NT_NAME}</div><div style="font:500 2.8cqw/1.3 {TEXT};color:{TX};opacity:.75">{NT_SUB}</div></div>'),
 ("two-block", "Two blocks", "C", "Name and place on two color blocks.", f'<div style="display:grid;justify-items:start"><span style="background:{HL};color:{BG};font:800 4.6cqw/1.2 {TEXT};padding:.6cqw 2cqw">{NT_NAME}</span><span style="background:{TX};color:{BG};font:600 3cqw/1.3 {TEXT};padding:.5cqw 2cqw">{NT_SUB}</span></div>'),
 ("pill", "Pill", "C", "A rounded pill with your name.", f'<span style="display:inline-flex;gap:1.6cqw;align-items:center;background:{BG};color:{TX};font:700 3.8cqw {TEXT};padding:1.2cqw 3cqw;border-radius:99cqw"><i style="width:2.2cqw;height:2.2cqw;border-radius:50%;background:{HL}"></i>{NT_NAME}<span style="opacity:.6;font-weight:500">{NT_SUB}</span></span>'),
 ("underline", "Underline", "C", "Big name, a line of your color under it.", f'<div style="color:#fff;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)"><div style="font:400 8cqw/1 {TITLE};border-bottom:1cqw solid {HL};padding-bottom:.6cqw">{NT_NAME}</div><div style="font:600 3cqw/1.6 {TEXT}">{NT_SUB}</div></div>'),
 ("title-font", "Big title", "R", "Your name in your title font, no box.", f'<div style="font:400 11cqw/.9 {TITLE};color:#fff;text-shadow:0 .4cqw 1.4cqw rgba(0,0,0,.7)">{NT_NAME}<br><span style="font-size:5cqw;color:{EX2}">{NT_SUB}</span></div>'),
 ("tape", "Tape label", "R", "Your name on a strip of tape.", f'<div style="transform:rotate(-2deg);background:{LT};color:{TX};font:700 4.2cqw/1.2 {TEXT};padding:1cqw 3cqw;clip-path:polygon(2% 0,98% 6%,100% 50%,97% 100%,1% 94%,0 50%)">{NT_NAME} · {NT_SUB}</div>'),
 ("handwritten", "Handwritten", "R", "Written on, in your notes font.", f'<div style="font:700 8cqw/1 {NOTES};color:#fff;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.7);transform:rotate(-4deg)">hi, I\'m {NT_NAME}<span style="color:{EX2}"> ←</span></div>'),
 ("mono", "Typed", "R", "Typed out, like a caption in a documentary.", f'<div style="font:700 3.6cqw/1.5 {MONO};color:#fff;background:rgba(0,0,0,.6);padding:1cqw 2cqw">{NT_NAME}<br><span style="color:{HL}">{NT_SUB}</span></div>'),
 ("sticker", "Sticker", "F", "A thick-outlined sticker, slightly tilted.", f'<div style="transform:rotate(-3deg);background:#fff;color:{TX};font:800 4.4cqw/1.1 {TEXT};padding:1.4cqw 2.6cqw;border:.6cqw solid {TX};border-radius:2cqw;box-shadow:.8cqw .8cqw 0 {HL}">{NT_NAME}<div style="font:600 2.8cqw {TEXT}">{NT_SUB}</div></div>'),
 ("id-badge", "ID badge", "F", "Like a conference badge clipped on.", f'<div style="width:28cqw;background:#fff;border-radius:1.4cqw;overflow:hidden;box-shadow:0 .6cqw 2cqw rgba(0,0,0,.4);text-align:center"><div style="background:{HL};color:{BG};font:800 2.6cqw/2.2 {TEXT}">HELLO, I\'M</div><div style="font:400 8cqw/1.3 {TITLE};color:{TX}">{NT_NAME}</div><div style="font:600 2.6cqw/2 {TEXT};color:{TX};opacity:.7">{NT_SUB}</div></div>')]
finalist_flow("name-tag", "Name tag", "The tag with your name when you first speak. Shown with a sample name.",
 [{"id": x[0], "name": x[1], "line": x[3], "html": nt_html(x), **({"pick": True, "why": "Readable at a glance and matches your text style."} if x[0] == "bar" else {})} for x in NTAGS],
 ["bar", "two-block", "pill", "handwritten"], "Next: one quick check on how your name and wordmark sit together, then your series tag.", ["bebas-neue", "inter", "caveat", "space-mono"], photo_tag=PHOTO_TAG)

# ---------- 15. Kit: series tag, sting, sound logo (each: finalists -> Main + Backup) ----------
def two_step(base, stage_line, opts, fin, mk_html, title, what, rule_tiles, main_word, nxt_tiles, nxt_compare, fonts, head="", play=None, play_ms=None, pick=None, why="", control=None, aspect=None):
    """Kit rounds: build the options, then the shared finalist flow (finalists -> Main / Backup / Alternative / Discard).
    (nxt_tiles, rule_tiles and main_word are kept for the call sites; the shared flow writes that copy itself.)"""
    def o(x):
        d = {"id": x[0], "name": x[1], "line": x[3], "html": mk_html(x)}
        if play: d.update({"play": play, "playMs": play_ms})
        if pick and x[0] == pick: d.update({"pick": True, "why": why})
        return d
    finalist_flow(base, title, what, [o(x) for x in opts], fin, nxt_compare, fonts, head=head, aspect=aspect, control=control)

# Series tag: names the show format once, ~4 s after the sting, over the first spoken line. Over the face photo,
# in the clear space beside the speaker.
SERIES, EPN = "30-DAY TESTS", "EP 12"
STAGS = [  # the episode number always sits on its own line, above or below the series name
 ("pill", "Pill", "C", "Rounded pills: the series, the episode under it.", f'<div style="display:grid;gap:1cqw;justify-items:start"><span style="background:{HL};color:{BG};font:800 4.4cqw {TEXT};padding:1.2cqw 2.8cqw;border-radius:99px">{SERIES}</span><span style="background:{BG};color:{TX};font:800 3.2cqw {TEXT};padding:.8cqw 2.2cqw;border-radius:99px">{EPN}</span></div>'),
 ("bar", "Side bar", "C", "A bar with a colored edge.", f'<div style="background:{BG};color:{TX};border-left:1.4cqw solid {HL};padding:1.4cqw 3cqw;font:400 6cqw/1 {TITLE}">{SERIES}<div style="font:700 3cqw {TEXT};color:{HL};margin-top:.6cqw">{EPN}</div></div>'),
 ("stack", "Stacked", "C", "Episode number above the series name.", f'<div style="color:#fff;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)"><div style="display:inline-block;font:800 3.4cqw {TEXT};background:{HL};color:{BG};letter-spacing:.3cqw;padding:.4cqw 1.4cqw;margin-bottom:.8cqw;text-shadow:none">{EPN}</div><div style="font:400 8cqw/1 {TITLE}">{SERIES}</div></div>'),
 ("underline", "Underline", "C", "Name with a thick colored line, the episode under it.", f'<div style="color:#fff;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)"><div style="font:400 7.4cqw/1 {TITLE};border-bottom:1cqw solid {HL};padding-bottom:.6cqw;display:inline-block">{SERIES}</div><div style="font:800 3.4cqw {TEXT};letter-spacing:.3cqw;margin-top:1cqw">{EPN}</div></div>'),
 ("box", "Outline box", "R", "A thin outlined box, two lines.", f'<div style="border:.5cqw solid #fff;color:#fff;padding:1.4cqw 2.6cqw;background:rgba(0,0,0,.55);display:inline-block"><div style="font:700 4cqw {TEXT};letter-spacing:.3cqw">{SERIES}</div><div style="font:800 3.2cqw {TEXT};color:{HL};letter-spacing:.3cqw;margin-top:.6cqw">{EPN}</div></div>'),
 ("chapter", "Chapter number", "R", "A big episode number, the series under it.", f'<div style="color:#fff;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.6)"><div style="font:400 15cqw/.85 {TITLE};color:{HL}">12</div><div style="font:700 3.6cqw/1.2 {TEXT};letter-spacing:.2cqw;margin-top:.6cqw">{SERIES}</div></div>'),
 ("tab", "Folder tab", "R", "A file-folder tab with the episode on it.", f'<div style="display:inline-block"><div style="background:{EX2};color:{TX};font:800 2.8cqw {TEXT};padding:.6cqw 1.8cqw;border-radius:1.2cqw 1.2cqw 0 0;display:inline-block">{EPN}</div><div style="background:{BG};color:{TX};font:400 7cqw/1 {TITLE};padding:1.4cqw 2.6cqw">{SERIES}</div></div>'),
 ("ticket", "Ticket", "R", "A ticket with a tear-off stub for the episode.", f'<div style="display:inline-grid;background:{EX2};color:{TX};border-radius:1cqw;overflow:hidden"><span style="font:400 6.4cqw/1 {TITLE};padding:1.6cqw 2.6cqw 1.2cqw">{SERIES}</span><span style="border-top:.5cqw dashed {TX};padding:1cqw 2.6cqw;font:800 3.2cqw {MONO}">{EPN}</span></div>'),
 ("stamp", "Stamp", "F", "A tilted rubber stamp.", f'<div style="border:.7cqw solid {HL};color:{HL};font:400 7cqw/1 {TITLE};padding:1.2cqw 2.4cqw;transform:rotate(-6deg);background:rgba(255,255,255,.85);display:inline-block">{SERIES}<div style="font:700 3cqw {MONO};text-align:right;margin-top:.4cqw">{EPN}</div></div>'),
 ("sticker", "Sticker", "F", "A thick-outlined sticker with a smaller one under it.", f'<div style="display:grid;justify-items:start;gap:1.2cqw"><div style="background:#fff;color:{TX};border:.6cqw solid {TX};box-shadow:.8cqw .8cqw 0 {HL};font:400 7cqw/1 {TITLE};padding:1.6cqw 2.6cqw;border-radius:2cqw;transform:rotate(-3deg)">{SERIES}</div><div style="background:{HL};color:{TX};border:.5cqw solid {TX};font:800 3.4cqw {TEXT};padding:.8cqw 2cqw;border-radius:1.4cqw;transform:rotate(2deg);margin-left:3cqw">{EPN}</div></div>'),
 ("tape", "Tape", "F", "Two strips of tape.", f'<div style="display:grid;justify-items:start;gap:.8cqw"><div style="background:{LT};color:{TX};font:400 7cqw/1 {TITLE};padding:1.2cqw 3cqw;transform:rotate(-2deg);clip-path:polygon(2% 0,98% 4%,100% 50%,97% 100%,1% 96%,0 50%)">{SERIES}</div><div style="background:{EX2};color:{TX};font:800 3.4cqw {TEXT};padding:.8cqw 2.4cqw;transform:rotate(1.5deg);clip-path:polygon(3% 0,97% 6%,100% 50%,96% 100%,2% 94%,0 50%)">{EPN}</div></div>'),
 ("hand", "Handwritten", "F", "Written on like a note.", f'<div style="color:#fff;text-shadow:0 .3cqw 1cqw rgba(0,0,0,.7);transform:rotate(-4deg)"><div style="font:700 9cqw/1 {NOTES}">30-day tests</div><div style="font:700 6cqw/1 {NOTES};color:{EX2};margin-left:6cqw">episode 12</div></div>')]
def stag_html(x):
    return (f'<img src="{FACE}" style="{FRAMED}"><div style="position:absolute;inset:0;background:radial-gradient(ellipse 60% 55% at 18% 20%,rgba(0,0,0,.55),transparent 75%)"></div>'
            f'<div style="position:absolute;inset:0;container-type:size"><div style="position:absolute;left:5%;top:12%">{x[4]}</div></div>')
two_step("series-tag", "", STAGS, ["pill", "bar", "chapter", "sticker"], stag_html,
 "Series tag", "Names the show once, a few seconds in, over your first line. Shown with a sample series name.",
 "mark as many finalists as you like. Next, you'll pick a main tag and a backup.", "tag",
 "Next: your finalists, large. You'll pick a main tag and a backup.", "Next: your sting.",
 ["bebas-neue", "inter", "caveat", "space-mono"], pick="pill", why="Small and clear; the number does the work.")

# Sting: a 1-2 s branded opener with sound, right after the hook. The first card shows where it plays.
STING_JS = r'''<script>
(function(){
  var ctx=null, live={};
  function A(){ if(!ctx) ctx=new (window.AudioContext||window.webkitAudioContext)(); if(ctx.state==='suspended') ctx.resume(); return ctx; }
  function g(out,t,a,d,v){ var x=ctx.createGain(); x.gain.setValueAtTime(0.0001,t); x.gain.exponentialRampToValueAtTime(v,t+a); x.gain.exponentialRampToValueAtTime(0.0001,t+a+d); x.connect(out); return x; }
  function tone(out,type,f,t,d,v,f2){ var o=ctx.createOscillator(); o.type=type; o.frequency.setValueAtTime(f,t); if(f2) o.frequency.exponentialRampToValueAtTime(f2,t+d); o.connect(g(out,t,.005,d,v)); o.start(t); o.stop(t+d+.05); }
  function nz(out,t,d,v,f1,f2,type){ var n=ctx.createBufferSource(), b=ctx.createBuffer(1,Math.ceil(ctx.sampleRate*d),ctx.sampleRate), c=b.getChannelData(0); for(var i=0;i<c.length;i++) c[i]=Math.random()*2-1; n.buffer=b; var f=ctx.createBiquadFilter(); f.type=type||'bandpass'; f.frequency.setValueAtTime(f1,t); if(f2) f.frequency.exponentialRampToValueAtTime(f2,t+d); n.connect(f); f.connect(g(out,t,.01,d,v)); n.start(t); n.stop(t+d); }
  function m(n){ return 440*Math.pow(2,(n-69)/12); }
  var S = {
    whoosh:function(o,t){ nz(o,t,.5,.5,300,4000); tone(o,'sine',m(76),t+.45,.5,.18); },
    pop:function(o,t){ tone(o,'sine',m(84),t,.08,.4,m(96)); tone(o,'triangle',m(79),t+.12,.35,.2); },
    chime:function(o,t){ [72,76,79,84].forEach(function(n,i){ tone(o,'sine',m(n),t+i*.09,.9,.14); }); },
    thump:function(o,t){ tone(o,'sine',140,t,.35,.9,40); nz(o,t,.08,.3,2000); tone(o,'sawtooth',m(48),t+.05,.5,.06); },
    riser:function(o,t){ nz(o,t,.9,.25,400,6000,'highpass'); tone(o,'sawtooth',200,t,.9,.05,900); tone(o,'sine',140,t+.95,.4,.9,40); },
    type:function(o,t){ for(var i=0;i<6;i++) nz(o,t+i*.08,.03,.4,3500); tone(o,'sine',m(88),t+.55,.3,.15); },
    glitch:function(o,t){ for(var i=0;i<8;i++) tone(o,'square',m(60+Math.floor(Math.random()*24)),t+i*.05,.04,.08); nz(o,t+.42,.2,.3,1500); },
    drums:function(o,t){ [0,.1,.2,.28,.36].forEach(function(d,i){ nz(o,t+d,.08,.4,900+i*300); }); tone(o,'sine',150,t+.48,.4,.9,45); },
    kalimba:function(o,t){ [72,79,76,84].forEach(function(n,i){ tone(o,'triangle',m(n),t+i*.13,.6,.18); }); },
    stab:function(o,t){ [60,64,67,71].forEach(function(n){ tone(o,'sawtooth',m(n),t,.4,.05); }); tone(o,'sine',m(36),t,.5,.4); },
    scratch:function(o,t){ nz(o,t,.25,.6,800,3000); nz(o,t+.25,.2,.5,3000,600); tone(o,'sine',m(79),t+.5,.3,.18); },
    bell:function(o,t){ tone(o,'sine',m(83),t,1.2,.2); tone(o,'sine',m(83)*2.76,t,.6,.05); }
  };
  window.bgSting=function(id,el){ A(); window.bgStingStop(id); var o=ctx.createGain(); o.gain.value=.6; o.connect(ctx.destination); live[id]=o; var k=(window.BG_STING||{})[id]; if(S[k]) S[k](o,ctx.currentTime+.05); };
  window.bgStingStop=function(id){ var o=live[id]; if(o){ try{o.disconnect();}catch(e){} delete live[id]; } };
  window.bgLogo=function(id,el){ A(); window.bgStingStop(id); var o=ctx.createGain(); o.gain.value=.6; o.connect(ctx.destination); live[id]=o;
    var L=(window.BG_LOGO||{})[id]; if(!L) return; var t=ctx.currentTime+.05; (S[window.BG_CHOSEN_STING]||S.pop)(o,t); t+=.45; L.n.forEach(function(n,i){ tone(o,L.w,m(n),t+i*L.s,L.d,.22); }); };
  window.bgLogoStop=window.bgStingStop;
})();
</script>'''
STINGS = [  # id, name, tier, line, sound, css keyframes for the mark, layout tweak
 ("pop-in", "Pop in", "C", "Your wordmark pops in with a bright pop.", "pop", "0%{transform:scale(0)}35%{transform:scale(1.12)}50%,100%{transform:none}"),
 ("swipe", "Color swipe", "C", "A band of your color swipes across and leaves your name.", "whoosh", "0%,30%{clip-path:inset(0 100% 0 0)}60%,100%{clip-path:inset(0 0 0 0)}"),
 ("chime", "Chime", "C", "A soft rise with a little chime. Friendly.", "chime", "0%{opacity:0;transform:translateY(20%)}55%,100%{opacity:1;transform:none}"),
 ("drop", "Bass drop", "C", "Lands hard on a deep thump.", "thump", "0%{transform:translateY(-140%)}22%{transform:translateY(4%)}30%,100%{transform:none}"),
 ("riser", "Riser and hit", "R", "Builds up, then hits.", "riser", "0%,60%{transform:scale(.2);opacity:0}70%{transform:scale(1.15);opacity:1}80%,100%{transform:none}"),
 ("typed", "Typed", "R", "Typed out with key clicks.", "type", "0%{clip-path:inset(0 100% 0 0)}50%,100%{clip-path:inset(0 0 0 0)}"),
 ("glitch", "Glitch", "R", "A digital stutter, then clean.", "glitch", "0%{opacity:0}10%{opacity:1;transform:translateX(6%) skewX(12deg)}20%{transform:translateX(-4%)}30%{opacity:.3}40%,100%{opacity:1;transform:none}"),
 ("drum-fill", "Drum fill", "R", "A quick drum fill into your name.", "drums", "0%,40%{opacity:0;transform:scale(.8)}55%,100%{opacity:1;transform:none}"),
 ("kalimba", "Kalimba", "F", "Plucky notes, playful and warm.", "kalimba", "0%{transform:rotate(-12deg) scale(.6);opacity:0}40%{transform:rotate(4deg) scale(1.05);opacity:1}60%,100%{transform:none}"),
 ("synth-stab", "Synth stab", "F", "One bold synth chord. Retro.", "stab", "0%{opacity:0;letter-spacing:1em}30%,100%{opacity:1;letter-spacing:normal}"),
 ("scratch", "Record scratch", "F", "A scratch, then your name. Comic.", "scratch", "0%,45%{transform:rotate(-90deg) scale(.4);opacity:0}65%,100%{transform:none;opacity:1}"),
 ("bell", "Bell", "F", "One clear bell. Calm and premium.", "bell", "0%{opacity:0;filter:blur(2cqw)}60%,100%{opacity:1;filter:none}")]
def sting_html(x):
    cid = f"st-{x[0]}"
    swipe = f'<div class="swp" style="position:absolute;inset:0;background:{HL};transform:translateX(-101%)"></div>' if x[0] == "swipe" else ''
    css = (f'.card.playing .{cid} .mk{{animation:{cid} 1.4s cubic-bezier(.2,.9,.3,1) both}}@keyframes {cid}{{{x[5]}}}'
           + (f'.card.playing .{cid} .swp{{animation:{cid}s 1.2s ease-in-out both}}@keyframes {cid}s{{0%{{transform:translateX(-101%)}}40%{{transform:translateX(0)}}100%{{transform:translateX(101%)}}}}' if x[0] == "swipe" else ''))
    snd = {"pop": "bright pop", "whoosh": "whoosh", "chime": "chime", "thump": "deep thump", "riser": "riser + hit", "type": "key clicks",
           "glitch": "glitch", "drums": "drum fill", "kalimba": "kalimba", "stab": "synth chord", "scratch": "record scratch", "bell": "bell"}[x[4]]
    css += f'.card.playing .{cid} .mk{{opacity:1}}.card.playing .{cid} .sn{{opacity:0}}'
    return (f'<style>{css}</style><div class="{cid}" style="position:absolute;inset:0;container-type:size;background:{BG};display:grid;place-items:center;overflow:hidden">{swipe}'
            f'<div class="mk" style="opacity:.16"><div style="font:400 22cqw/.85 {F["anton"]};color:{TX}">{WM_NAME.upper()}</div></div>'
            f'<div class="sn" style="position:absolute;left:5%;bottom:7%;font:700 3.6cqw {TEXT};color:{TX};background:#fff;border:.3cqw solid {TX};padding:.8cqw 2cqw;border-radius:99cqw;transition:opacity .2s">♪ {snd} · 1.5 s</div></div>')
TIMELINE = {"id": "where", "name": "Where your sting plays", "line": "Hook first (about 10–20 seconds), then the sting, then the video.", "control": True,
 "html": (f'<div style="position:absolute;inset:0;container-type:size;background:#fff;display:flex;flex-direction:column;justify-content:center;gap:4cqw;padding:0 6%">'
          f'<div style="display:flex;height:16cqw;font:700 4cqw {TEXT};color:#fff;border-radius:1.6cqw;overflow:hidden">'
          f'<div style="flex:2.2;background:#8a8f8d;display:grid;place-items:center">Hook</div>'
          f'<div style="flex:.7;background:{HL};color:{BG};display:grid;place-items:center;font-weight:900">Sting</div>'
          f'<div style="flex:6;background:{TX};display:grid;place-items:center">The video</div></div>'
          f'<div style="display:flex;font:600 3.4cqw {TEXT};color:#555"><span style="flex:2.2">0 s</span><span style="flex:.7;margin-left:-2cqw;white-space:nowrap">~15 s</span><span style="flex:6;text-align:right">rest of the video</span></div></div>')}
STING_DATA = '<script>window.BG_STING=' + json.dumps({x[0]: x[4] for x in STINGS}) + ';</script>'
two_step("sting", "", STINGS, ["pop-in", "swipe", "drop", "kalimba"], sting_html,
 "Sting", "Your sting is a 1–2 second branded opener, a tiny intro with your name and sound. It plays right after your hook, about 10–20 seconds in.",
 "mark as many finalists as you like. Next, you'll pick a main sting and a backup.", "sting",
 "Next: your finalists, large. You'll pick a main sting and a backup.", "Next: your sound logo.",
 ["anton", "inter"], head=STING_DATA + STING_JS, play="bgSting", play_ms=1700, pick="pop-in", why="Short and bright; it won't wear out after fifty videos.", control=TIMELINE)

# Sound logo: a 3-5 note signature, played with the chosen sting so it's judged in place.
LOGOS = [
 ("rise3", "Three up", "C", "Three rising notes. Bright, hopeful.", {"n": [72, 76, 79], "w": "triangle", "s": .14, "d": .5}),
 ("fall3", "Three down", "C", "Three falling notes. Calm, wrapped up.", {"n": [79, 76, 72], "w": "sine", "s": .16, "d": .6}),
 ("doorbell", "Doorbell", "C", "Two notes, like a friendly doorbell.", {"n": [76, 72], "w": "sine", "s": .28, "d": .8}),
 ("sparkle", "Sparkle", "C", "A quick sparkle of high notes.", {"n": [84, 88, 91, 96], "w": "sine", "s": .07, "d": .5}),
 ("bass2", "Low two", "R", "Two deep notes. Serious, confident.", {"n": [43, 48], "w": "triangle", "s": .22, "d": .7}),
 ("arp5", "Arpeggio", "R", "Five notes running up a chord.", {"n": [60, 64, 67, 72, 76], "w": "square", "s": .08, "d": .3}),
 ("question", "Question", "R", "Ends up high, like a question.", {"n": [72, 74, 79], "w": "triangle", "s": .16, "d": .5}),
 ("octave", "Octave jump", "R", "One note, then the same an octave up.", {"n": [67, 79], "w": "sine", "s": .2, "d": .7}),
 ("chip", "Game coin", "F", "An 8-bit coin sound.", {"n": [83, 88], "w": "square", "s": .08, "d": .35}),
 ("bluesy", "Bluesy", "F", "Three notes with a blue note in the middle.", {"n": [67, 70, 72], "w": "sawtooth", "s": .15, "d": .45}),
 ("tritone", "Mischief", "F", "A sneaky, unresolved pair.", {"n": [72, 78], "w": "triangle", "s": .2, "d": .6}),
 ("whistle", "Whistle", "F", "A two-note whistle.", {"n": [86, 91], "w": "sine", "s": .25, "d": .6})]
def logo_html(x):
    notes = x[4]["n"]; lo, hi = min(notes), max(notes)
    dots = ''.join(f'<i style="position:absolute;left:{18 + k * 64 / max(1, len(notes) - 1):.0f}%;bottom:{18 + (n - lo) / max(1, hi - lo) * 46 if hi > lo else 40:.0f}%;width:6cqw;height:6cqw;border-radius:50%;background:{HL}"></i>' for k, n in enumerate(notes))
    return (f'<div style="position:absolute;inset:0;container-type:size;background:{TX}">'
            f'<div style="position:absolute;left:6%;top:8%;font:400 9cqw/1 {F["anton"]};color:{BG}">{WM_NAME.upper()} <span style="font:800 3.4cqw {TEXT};background:{HL};color:{BG};padding:.6cqw 1.6cqw;border-radius:99cqw;vertical-align:middle">EP 12</span></div>'
            f'<div style="position:absolute;left:6%;right:6%;top:34%;bottom:10%">{dots}</div>'
            f'<div style="position:absolute;right:5%;top:9%;font:600 3cqw {TEXT};color:{BG};opacity:.7">plays with your sting</div></div>')
# window.BG_CHOSEN_STING = the sound of the creator's Main sting, so every logo plays right after THEIR sting (never the example's)
LOGO_DATA = '<script>window.BG_LOGO=' + json.dumps({x[0]: x[4] for x in LOGOS}) + ';window.BG_CHOSEN_STING=' + json.dumps(next(x[4] for x in STINGS if x[0] == 'pop-in')) + ';</script>'
two_step("sound-logo", "", LOGOS, ["rise3", "doorbell", "sparkle", "chip"], logo_html,
 "Sound logo", "A few notes people learn to recognize as you. Each one plays right after your main sting, so you hear it in place.",
 "mark as many finalists as you like. Next, you'll pick a main sound logo and a backup.", "sound logo",
 "Next: your finalists. You'll pick a main sound logo and a backup.", "Next: ways to close a video.",
 ["anton", "inter"], head=LOGO_DATA + STING_JS, play="bgLogo", play_ms=2000, pick="rise3", why="Bright and short; it matches a pop-in sting.")


# ---------- 16. Kit: ways to close a video (library), profile picture + banner (Main + Backup) ----------
NEXT1, NEXT2 = "WHAT I'D DO DIFFERENTLY", "DAY 31"
def thumb(title, img=FACE, w="100%"):
    bgimg = (f'<img src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:70% 30%">' if img else
             f'<div style="position:absolute;inset:0;background:{TX}"></div><div style="position:absolute;right:-8cqw;bottom:-14cqw;width:60cqw;aspect-ratio:1;border-radius:50%;background:{HL}"></div>')
    return (f'<div style="position:relative;width:{w};aspect-ratio:16/9;container-type:inline-size;border-radius:1.4cqw;overflow:hidden;background:#000;box-shadow:0 .6cqw 2cqw rgba(0,0,0,.35)">'
            f'{bgimg}'
            f'<div style="position:absolute;left:5cqw;top:6cqw;right:45cqw;font:400 13cqw/.9 {TITLE};color:#fff;text-shadow:0 .5cqw 2cqw rgba(0,0,0,.7)">{title}</div>'
            f'<span style="position:absolute;right:3cqw;bottom:3cqw;background:rgba(0,0,0,.8);color:#fff;font:600 5cqw {TEXT};padding:.5cqw 1.6cqw;border-radius:1cqw">12:04</span></div>')
def endscreen(inner, bg=None, img=None, dim=.0):
    base = (f'<img src="{img}" style="{FRAMED}"><div style="position:absolute;inset:0;background:rgba(0,0,0,{dim})"></div>' if img else '')
    return (f'<div style="position:absolute;inset:0;container-type:size;background:{bg or BG};color:{TX};overflow:hidden">{base}{inner}'
            f'<span style="position:absolute;right:2.4%;top:4%;font:700 2.4cqw {TEXT};color:{TX if not img else "#fff"};opacity:.6;letter-spacing:.2cqw">LAST 10 SECONDS</span></div>')
WMK = lambda size, col=None: f'<span style="font:400 {size}cqw/.85 {F["anton"]};color:{col or TX}">{WM_NAME.upper()}</span>'
SUB = f'<span style="display:inline-flex;align-items:center;gap:1cqw;background:#e5262b;color:#fff;font:700 3.2cqw {TEXT};padding:1.4cqw 3cqw;border-radius:99cqw">Subscribe</span>'
CLOSE = [  # id, name, tier, line, html
 ("next-video", "Next video", "C", "For: most videos. One big \"watch next\".",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1.3fr;align-items:center;gap:5cqw;padding:0 7%"><div style="display:grid;gap:2cqw">{WMK(11)}<div style="font:700 4cqw/1.2 {TEXT}">Watch this one next</div><div style="font:400 9cqw {TITLE};color:{HL}">→</div></div>{thumb(NEXT1)}</div>')),
 ("two-grid", "Two-video grid", "C", "For: giving people a choice of two.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;align-content:center;gap:3cqw;padding:0 7%"><div style="display:flex;justify-content:space-between;align-items:end">{WMK(8)}<span style="font:700 3.4cqw {TEXT}">Keep watching</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:4cqw">{thumb(NEXT1)}{thumb(NEXT2, None)}</div></div>')),
 ("subscribe-one", "Subscribe + one video", "C", "For: early videos, when growing the channel matters most.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1.3fr;align-items:center;gap:5cqw;padding:0 7%"><div style="display:grid;justify-items:center;gap:3cqw"><div style="width:26cqw;aspect-ratio:1;border-radius:50%;background:{TX};display:grid;place-items:center">{WMK(12, BG)}</div>{SUB}</div>{thumb(NEXT1)}</div>')),
 ("minimal", "Centered minimal", "C", "For: calm endings. Just your name and handle.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;place-items:center;align-content:center;gap:2cqw">{WMK(22)}<div style="font:600 4cqw {TEXT};color:{HL}">{WM_HANDLE}</div></div>')),
 ("arrows", "Hand-drawn arrow", "R", "For: a playful point at the next video.",
  endscreen(f'<div style="position:absolute;left:7%;top:20%;font:700 8cqw/1 {NOTES};color:{TX};transform:rotate(-4deg)">watch this<br>one next!</div>'
            f'<svg viewBox="0 0 100 60" style="position:absolute;left:30%;top:46%;width:20%;overflow:visible"><path d="M5 10 C 35 55, 70 50, 92 30" fill="none" stroke="{HL}" stroke-width="4" stroke-linecap="round"/><path d="M80 24 L96 28 L88 42" fill="none" stroke="{HL}" stroke-width="4" stroke-linecap="round"/></svg>'
            f'<div style="position:absolute;right:7%;top:24%;width:44%">{thumb(NEXT1)}</div>')),
 ("credits", "Credits roll", "R", "For: big episodes. Thanks scroll up like a film.",
  endscreen(f'<div style="position:absolute;inset:0;background:#0c0c0c"></div><div style="position:absolute;inset:0;display:grid;place-items:center;align-content:center;gap:2.4cqw;color:#fff;text-align:center;font:500 3.6cqw/1.3 {TEXT}">'
            f'<div style="opacity:.55">Filmed, edited and over-thought by</div><div style="font:400 10cqw/1 {F["anton"]}">{WM_NAME.upper()}</div><div style="opacity:.55;margin-top:2cqw">Music</div><div>Your music lane</div><div style="opacity:.55;margin-top:2cqw">Thanks for watching</div><div style="color:{HL}">{WM_HANDLE}</div></div>', bg="#0c0c0c")),
 ("loop", "Loop back to the hook", "R", "For: a long video that ends where it began. (Shorts loop in their own way.)",
  endscreen(f'<div style="position:absolute;left:6%;bottom:12%;right:40%;display:grid;gap:1.6cqw"><span style="justify-self:start;background:{HL};color:{BG};font:800 3cqw {TEXT};padding:1cqw 2.4cqw;border-radius:99cqw">↺ BACK TO THE START</span><div style="font:400 9cqw/.9 {TITLE};color:#fff;text-shadow:0 .4cqw 1.4cqw rgba(0,0,0,.6)">{SAMPLE_TITLE}</div></div>', img=FACE, dim=.15)),
 ("freeze", "Freeze-frame sign-off", "R", "For: ending on a funny or honest moment.",
  endscreen(f'<div style="position:absolute;inset:0;backdrop-filter:grayscale(1) contrast(1.1)"></div><div style="position:absolute;left:6%;top:14%;display:grid;gap:2cqw"><span style="font:800 3cqw {MONO};color:#fff;letter-spacing:.3cqw">❚❚ PAUSED</span><div style="font:400 9cqw/.9 {TITLE};color:#fff;background:{TX};padding:1.4cqw 3cqw">SEE YOU NEXT TIME.</div></div>', img=FACE, dim=.1)),
 ("blooper", "Blooper tag", "F", "For: one outtake after the goodbye.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1.2fr;align-items:center;gap:5cqw;padding:0 7%"><div style="display:grid;gap:2cqw">{WMK(9)}<div style="font:700 7cqw/1 {NOTES};color:{TX}">wait, one more thing…</div></div>'
            f'<div style="position:relative;transform:rotate(3deg)">{thumb("TAKE 14", FACE)}<span style="position:absolute;left:-3cqw;top:-3cqw;background:{EX2};color:{TX};font:800 3cqw {TEXT};padding:1cqw 2cqw;transform:rotate(-8deg)">OUTTAKE</span></div></div>')),
 ("one-liner", "One-line sign-off", "C", "For: no card at all; your catchphrase as a caption.",
  endscreen(f'<div style="position:absolute;left:0;right:0;bottom:10%;display:flex;justify-content:flex-start;padding-left:6%"><span style="background:{BG};color:{TX};font:800 4.6cqw {TEXT};padding:1.4cqw 3cqw;border-radius:1cqw">That\'s it. Go try it.</span></div>', img=FACE)),
 ("question", "Question for the comments", "C", "For: starting a conversation under the video.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;align-content:center;gap:3cqw;padding:0 8%"><span style="font:800 3.4cqw {TEXT};color:{HL};letter-spacing:.3cqw">TELL ME IN THE COMMENTS</span><div style="font:400 11cqw/.9 {TITLE}">WHAT WOULD YOU TRY<br>FOR 30 DAYS?</div><div style="display:flex;gap:2cqw;align-items:center;font:600 3.4cqw {TEXT};opacity:.75"><span style="width:6cqw;aspect-ratio:1;border-radius:50%;background:{LT};border:.4cqw solid {TX}"></span>Add a comment…</div></div>')),
 ("teaser", "Next-episode teaser", "R", "For: series. A quick look at what's coming.",
  endscreen(f'<div style="position:absolute;left:6%;top:14%;display:grid;gap:1.6cqw;color:#fff;text-shadow:0 .4cqw 1.4cqw rgba(0,0,0,.6)"><span style="font:800 3.4cqw {TEXT};letter-spacing:.3cqw;color:{EX2}">NEXT WEEK</span><div style="font:400 13cqw/.85 {TITLE}">{NEXT2}</div><span style="font:700 3.6cqw {TEXT}">EP 13 · Tuesday</span></div>', img=FACE, dim=.55)),
 ("progress", "Series progress", "R", "For: series with a set length. Shows how far along it is.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;align-content:center;gap:3cqw;padding:0 8%"><div style="display:flex;justify-content:space-between;align-items:end">{WMK(9)}<span style="font:800 4cqw {TEXT}">EP 12 <span style="opacity:.5">/ 30</span></span></div>'
            f'<div style="display:grid;grid-template-columns:repeat(30,1fr);gap:.6cqw">{"".join(f"<i style=\'height:4cqw;border-radius:.6cqw;background:{HL if k < 12 else LT}\'></i>" for k in range(30))}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:4cqw;align-items:center"><span style="font:700 4cqw {TEXT}">Next: episode 13 →</span>{thumb(NEXT2, None)}</div></div>')),
 ("fade", "Fade to color", "C", "For: a clean, quiet ending in your pop color.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;place-items:center">{WMK(20, BG)}</div>', bg=HL)),
 ("split", "Split screen", "F", "For: still talking while the next video plays beside you.",
  endscreen(f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr"><div style="position:relative;overflow:hidden"><img src="{FACE}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:68% 30%"></div>'
            f'<div style="display:grid;align-content:center;gap:3cqw;padding:0 6%;background:{TX};color:{BG}"><span style="font:800 3.2cqw {TEXT};color:{HL};letter-spacing:.3cqw">UP NEXT</span>{thumb(NEXT1, None)}</div></div>')),
 ("pinned", "Pinned-comment pointer", "F", "For: sending people to a link or resource.",
  endscreen(f'<div style="position:absolute;left:6%;bottom:12%;display:grid;gap:1.4cqw;justify-items:start"><span style="background:{EX2};color:{TX};font:800 4.4cqw {TEXT};padding:1.4cqw 3cqw;border-radius:1cqw">Everything I used is in the pinned comment</span><span style="font:400 10cqw/1 {TITLE};color:#fff;text-shadow:0 .4cqw 1.4cqw rgba(0,0,0,.6);margin-left:4cqw">↓</span></div>', img=FACE))]
W("close-out", {
 "round": "close-out", "kind": "library", "keepWord": "ending|endings", "layout": "tiles", "fonts": ["anton", "bebas-neue", "inter", "caveat", "space-mono"],
 "title": "Ways to close a video", "what": "The last seconds of a long video. Keep every ending you'd use; each video picks one.",
 "buttons": [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}], "keepValues": ["keep"],
 "next": "Next: thumbnail layouts.", "persona": SAY_PERSONA,
 "options": [{"id": c[0], "name": c[1], "line": c[3], "html": c[4], **({"pick": True, "why": "The one that keeps people watching your next video."} if c[0] == "next-video" else {})} for c in CLOSE]})

# Profile picture options, for when it isn't a photo: each shown big, then at the sizes people actually see it.
PFP = [  # id, name, tier, line, circle html (in a container with container-type:inline-size), bg
 ("mono", "Monogram", "C", "Your initial in your title font.", f'<div style="font:400 62cqw/1 {F["anton"]};color:{BG}">{WM_INIT}</div>', TX),
 ("mono-pop", "Monogram on pop color", "C", "Your initial on your brightest color.", f'<div style="font:400 62cqw/1 {F["anton"]};color:{TX}">{WM_INIT}</div>', HL),
 ("wordmark", "Wordmark", "C", "Your whole name, if it's short enough.", f'<div style="font:400 26cqw/1 {F["anton"]};color:{BG}">{WM_NAME.upper()}</div>', TX),
 ("seal", "Seal", "R", "Your initial in a ring.", f'<div style="width:78cqw;aspect-ratio:1;border-radius:50%;border:5cqw solid {HL};display:grid;place-items:center;font:400 48cqw/1 {F["anton"]};color:{BG}">{WM_INIT}</div>', TX),
 ("episode", "Initial + episode pill", "R", "Your initial with the episode pill from your wordmark.", f'<div style="display:grid;justify-items:center;gap:2cqw"><div style="font:400 46cqw/.85 {F["anton"]};color:{TX}">{WM_INIT}</div><span style="font:800 10cqw/1 {TEXT};background:{HL};color:{BG};padding:2cqw 5cqw;border-radius:99cqw">EP</span></div>', BG),
 ("split", "Split color", "R", "Half and half in your two main colors.", f'<div style="position:absolute;inset:0;background:linear-gradient(135deg,{TX} 50%,{HL} 50%)"></div><div style="position:relative;font:400 58cqw/1 {F["anton"]};color:{BG}">{WM_INIT}</div>', TX),
 ("bubble", "Speech bubble", "F", "Your initial in a chunky speech bubble.", f'<div style="position:relative;background:{HL};color:{TX};font:400 36cqw/1 {F["bow"]};padding:6cqw 12cqw;border-radius:14cqw">{WM_INIT}!<i style="position:absolute;left:18%;bottom:-6cqw;border:5cqw solid transparent;border-top-color:{HL};border-left-color:{HL}"></i></div>', EX2),
 ("silhouette", "Silhouette", "F", "A simple figure in your colors. No face needed.", f'<svg viewBox="0 0 100 100" style="width:100%;height:100%"><circle cx="50" cy="40" r="17" fill="{HL}"/><path d="M18 100 C 20 70, 80 70, 82 100 Z" fill="{HL}"/></svg>', TX)]
def pfp_circle(html, bg, px):
    return f'<div style="width:{px};aspect-ratio:1;border-radius:50%;background:{bg};display:grid;place-items:center;overflow:hidden;container-type:inline-size;position:relative;flex:none">{html}</div>'
def pfp_card(p):
    _, n, t, l, html, bg = p
    cap = lambda s: f'<div style="font:600 2.8cqw {TEXT};color:#666;margin-top:1.2cqw;text-align:center">{s}</div>'
    return (f'<div style="position:absolute;inset:0;container-type:size;background:#eef0ef;display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:4cqw;padding:0 5%">'
            f'<div>{pfp_circle(html, bg, "100%")}{cap("Your channel page")}</div>'
            f'<div style="display:grid;gap:4cqw">'
            f'<div style="display:flex;gap:2.4cqw;align-items:center;background:#fff;border-radius:1.6cqw;padding:2.4cqw">{pfp_circle(html, bg, "10cqw")}<div style="display:grid;gap:1cqw"><b style="font:700 3.4cqw {TEXT}">{WM_NAME}</b><span style="font:500 2.8cqw {TEXT};color:#777">1.2K views · 2 days ago</span></div></div>'
            f'<div style="display:flex;gap:2cqw;align-items:flex-start;background:#fff;border-radius:1.6cqw;padding:2.4cqw">{pfp_circle(html, bg, "6.4cqw")}<div style="font:500 2.8cqw/1.35 {TEXT};color:#333"><b>{WM_HANDLE}</b> Thanks for watching, more on Tuesday!</div></div>'
            f'<div style="background:#111;border-radius:1.6cqw;padding:2.4cqw;display:flex;gap:2.4cqw;align-items:center">{pfp_circle(html, bg, "8cqw")}<span style="font:600 3cqw {TEXT};color:#fff">{WM_HANDLE} · Follow</span></div>'
            f'{cap("In the feed, in comments, on a dark screen")}</div></div>')
# "Will your profile picture be a photo of you?" Yes -> tips, no page. No -> the logo options only. Not sure -> both
# groups on one page (this example), so the creator compares a photo-style picture with a logo one.
PH = lambda pos="62% 26%", f="": f'<img src="{FACE}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};{f}">'
PFP_PHOTO = [  # same shape as PFP; the test photo stands in for theirs until they send one
 ("photo-plain", "Photo, plain", "C", "Your face filling the circle. The most common choice.", PH(), "#000"),
 ("photo-ring", "Photo + color ring", "C", "Your photo inside a ring of your color.", f'<div style="position:absolute;inset:7%;border-radius:50%;overflow:hidden">{PH()}</div>', HL),
 ("photo-tint", "Photo in your colors", "R", "Your photo tinted in your two main colors.", PH(f="filter:grayscale(1) contrast(1.2)") + f'<div style="position:absolute;inset:0;background:linear-gradient(135deg,{HL},{TX});mix-blend-mode:color"></div>', TX),
 ("photo-badge", "Photo + name badge", "R", "Your photo with a small name badge at the bottom.", PH() + f'<span style="position:absolute;left:50%;bottom:9%;transform:translateX(-50%);background:{HL};color:{TX};font:400 13cqw/1 {F["anton"]};padding:1.6cqw 5cqw;border-radius:99cqw">{WM_NAME.upper()}</span>', "#000")]
finalist_flow("profile-picture", "Profile picture", "Shown big and at the tiny sizes people really see it: the feed, comments, a dark screen.",
 [{"id": p[0], "name": p[1], "line": p[3], "html": pfp_card(p), **({"pick": True, "why": "Reads clearly even at the smallest size."} if p[0] == "mono-pop" else {})} for p in PFP_PHOTO + PFP],
 ["photo-plain", "photo-ring", "mono-pop", "seal"], "Next: your banner.", ["anton", "bowlby-one", "inter"], aspect="16/10",
 tiles_extra={"what": "With a photo of you or without one, shown at the sizes people really see it. The test photo stands in for yours."})

# Banner (YouTube): the channel page mock, with the area every screen shows outlined.
BAN = [  # id, name, tier, line, html inside a 2560x1440 frame (cqw of the full banner)
 ("promise", "Promise", "C", "What the channel is, in a few words, plus how often you post.",
  f'<div style="position:absolute;inset:0;background:{BG}"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:grid;justify-items:center;gap:.8cqw;text-align:center"><div style="font:400 5.4cqw/1 {TITLE};color:{TX}">I TRY THINGS FOR 30 DAYS</div><div style="font:700 1.5cqw {TEXT};color:{TX}">so you don\'t have to · <span style="color:{HL}">new video every week</span></div></div>'),
 ("wordmark", "Wordmark center", "C", "Your wordmark big, on your main color.",
  f'<div style="position:absolute;inset:0;background:{TX}"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:1.6cqw"><span style="font:400 8cqw/.85 {F["anton"]};color:{BG}">{WM_NAME.upper()}</span><span style="font:800 1.8cqw {TEXT};background:{HL};color:{TX};padding:.5cqw 1.2cqw;border-radius:99cqw">EP 12</span></div>'),
 ("pattern", "Pattern", "R", "A repeating pattern of your initial, with your name in the middle.",
  f'<div style="position:absolute;inset:0;background:{HL};background-image:radial-gradient({TX} 18%,transparent 19%);background-size:3cqw 3cqw;opacity:1"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:{BG};padding:1cqw 3cqw;border:.5cqw solid {TX}"><span style="font:400 6cqw/1 {F["anton"]};color:{TX}">{WM_NAME.upper()}</span></div>'),
 ("collage", "Collage", "R", "A strip of moments from your videos.",
  f'<div style="position:absolute;inset:0;background:{TX}"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:48.2%;height:23.5%;display:grid;grid-template-columns:1fr 1fr 1fr 1.2fr;gap:.4cqw">'
  f'<img src="{FACE}" style="width:100%;height:100%;object-fit:cover;object-position:70% 30%"><div style="background:{EX2};display:grid;place-items:center;font:400 2.4cqw/1 {TITLE};color:{TX}">DAY 1</div><img src="{FACE}" style="width:100%;height:100%;object-fit:cover;object-position:85% 60%;filter:saturate(1.3)">'
  f'<div style="background:{HL};display:grid;place-items:center;font:400 4cqw/1 {F["anton"]};color:{TX}">{WM_NAME.upper()}</div></div>'),
 ("split", "Split color", "R", "Two colors split on a slant, name on the line.",
  f'<div style="position:absolute;inset:0;background:linear-gradient(100deg,{TX} 50%,{HL} 50%)"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font:400 7cqw/1 {F["anton"]};color:{BG};text-shadow:0 .3cqw 0 {TX}">{WM_NAME.upper()}</div>'),
 ("shows", "Your shows", "C", "The shows you make, side by side.",
  f'<div style="position:absolute;inset:0;background:{LT}"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;gap:1.2cqw">'
  + ''.join(f'<span style="font:400 2.6cqw/1 {TITLE};background:{c};color:{tc};padding:1cqw 1.8cqw;border-radius:.6cqw">{t}</span>' for t, c, tc in [("30-DAY TESTS", HL, TX), ("QUICK ANSWERS", TX, BG), ("Q&A FRIDAYS", EX2, TX)]) + '</div>'),
 ("note", "Handwritten note", "F", "A note in your handwriting font, a bit tilted.",
  f'<div style="position:absolute;inset:0;background:{EX2}"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-3deg);background:#fff;padding:1cqw 3cqw;box-shadow:.4cqw .4cqw 0 {TX}"><span style="font:700 4.6cqw/1 {NOTES};color:{TX}">hi, I\'m {WM_NAME}. I try things.</span></div>'),
 ("stripe", "Bold stripe", "F", "A thick stripe of your pop color through a dark banner.",
  f'<div style="position:absolute;inset:0;background:{TX}"></div><div style="position:absolute;left:0;right:0;top:44%;height:12%;background:{HL}"></div><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font:400 6.4cqw/1 {F["anton"]};color:{TX};background:{HL};padding:0 2cqw">{WM_NAME.upper()} · 30-DAY TESTS</div>')]
def ban_card(b):
    _, n, t, l, html = b
    cap = lambda s: f'<div style="font:600 2.6cqw {TEXT};color:#666;margin-top:1cqw">{s}</div>'
    # Desktop shows the middle strip (2560x423); the safe area every screen shows is the center 1235x338.
    full = (f'<div style="position:relative;aspect-ratio:16/9;container-type:inline-size;overflow:hidden;border-radius:.8cqw">{html}'
            f'<div style="position:absolute;left:0;right:0;top:35.3%;height:29.4%;outline:.25cqw dashed rgba(255,255,255,.9);box-shadow:0 0 0 999cqw rgba(0,0,0,.35)"></div>'
            f'<div style="position:absolute;left:25.9%;top:38.3%;width:48.2%;height:23.5%;outline:.35cqw solid #fff"></div></div>')
    strip = (f'<div style="position:relative;aspect-ratio:2560/423;container-type:inline-size;overflow:hidden;border-radius:.8cqw .8cqw 0 0">'
             f'<div style="position:absolute;left:0;width:100%;top:-120.2%;aspect-ratio:16/9;container-type:inline-size">{html}</div></div>')
    page = (f'<div style="background:#fff;border-radius:.8cqw;overflow:hidden">{strip}<div style="display:flex;gap:2.4cqw;align-items:center;padding:2cqw 2.4cqw">'
            f'{pfp_circle(PFP[1][4], PFP[1][5], "9cqw")}<div style="display:grid;gap:.6cqw"><b style="font:800 3.6cqw {TEXT}">{WM_NAME}</b><span style="font:500 2.4cqw {TEXT};color:#777">{WM_HANDLE} · 48 videos</span></div>'
            f'<span style="margin-left:auto;background:#111;color:#fff;font:700 2.4cqw {TEXT};padding:1.2cqw 2.6cqw;border-radius:99cqw">Subscribe</span></div></div>')
    return (f'<div style="position:absolute;inset:0;container-type:size;background:#eef0ef;padding:3.5% 4%;display:grid;gap:3cqw;align-content:start">'
            f'<div>{page}{cap("Your channel page on a computer")}</div>'
            f'<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:3cqw;align-items:start"><div>{full}{cap("The full banner. Dashed: what computers show. White box: what every screen shows; keep words inside it.")}</div>'
            f'<div style="display:grid;gap:1cqw"><div style="width:62%;justify-self:center;background:#fff;border-radius:2.4cqw;padding:1.6cqw;box-shadow:0 0 0 .5cqw #222"><div style="position:relative;aspect-ratio:1546/423;container-type:inline-size;overflow:hidden;border-radius:.6cqw"><div style="position:absolute;left:-32.9%;width:165.6%;top:-120.2%;aspect-ratio:16/9;container-type:inline-size">{html}</div></div>'
            f'<div style="display:flex;gap:1.4cqw;align-items:center;margin-top:1.4cqw">{pfp_circle(PFP[1][4], PFP[1][5], "4.4cqw")}<b style="font:800 2.4cqw {TEXT}">{WM_NAME}</b></div></div>{cap("On a phone")}</div></div></div>')
finalist_flow("banner", "Banner", "The wide image at the top of your channel page, shown on a computer and a phone.",
 [{"id": b[0], "name": b[1], "line": b[3], "html": ban_card(b), **({"pick": True, "why": "A new visitor knows what you make in one look."} if b[0] == "promise" else {})} for b in BAN],
 [b[0] for b in BAN[:4]], "Next: layouts for Shorts, Reels and TikTok.", ["anton", "bebas-neue", "inter", "caveat"], aspect="16/14")

# ---------- 17. Vertical: layouts library, each a real 9:16 test frame in a phone, with the app's buttons ghosted ----------
# Built on the native vertical test photo, never a 16:9 photo cropped to 9:16. Every phone draws the safe box
# (x 65-930, y 250-1450 on 1080x1920, dashed) and the Instagram 3:4 grid crop (y 240-1680 survive, dotted lines).
VF = "img/10-car-vertical.jpg"
SAFE = ('<div style="position:absolute;left:6.02%;width:80.09%;top:13.02%;height:62.5%;border:.5cqw dashed rgba(255,255,255,.9);box-shadow:0 0 0 .25cqw rgba(0,0,0,.35);z-index:6;pointer-events:none"></div>'
        + ''.join(f'<i style="position:absolute;left:0;right:0;top:{y};border-top:.5cqw dotted rgba(255,255,255,.85);box-shadow:0 0 0 .2cqw rgba(0,0,0,.3);z-index:6;display:block"></i>' for y in ("12.5%", "87.5%")))
def phone(inner):
    ui = (f'<div style="position:absolute;right:3.5%;bottom:18%;display:grid;gap:5cqw;justify-items:center;opacity:.55;z-index:5">'
          + ''.join(f'<i style="width:9cqw;aspect-ratio:1;border-radius:50%;background:rgba(255,255,255,.85);display:block"></i>' for _ in range(4)) + '</div>'
          f'<div style="position:absolute;left:5%;right:20%;bottom:5%;display:grid;gap:2cqw;opacity:.55;z-index:5"><i style="height:3cqw;width:45%;background:rgba(255,255,255,.9);border-radius:2cqw;display:block"></i><i style="height:2.6cqw;width:80%;background:rgba(255,255,255,.8);border-radius:2cqw;display:block"></i></div>')
    return (f'<div style="position:absolute;inset:0;container-type:size;background:#e9ecea;display:grid;place-items:center">'
            f'<div style="height:94%;aspect-ratio:9/16;background:#111;border-radius:6cqh;padding:1.2cqh;box-sizing:border-box;box-shadow:0 1cqh 3cqh rgba(0,0,0,.25)">'
            f'<div style="position:relative;width:100%;height:100%;border-radius:5cqh;overflow:hidden;container-type:inline-size;background:{TX}">{inner}{ui}{SAFE}</div></div></div>')
SCREEN = (f'<div style="position:absolute;inset:0;background:{LT};padding:12% 9%;display:grid;align-content:start;gap:4cqw">'
          f'<div style="font:800 5cqw {TEXT};color:{TX};opacity:.6">My 30 days</div><div style="display:flex;align-items:flex-end;gap:3cqw;height:40cqw">'
          + ''.join(f'<i style="flex:1;height:{h}%;background:{HL if k == 4 else TX};border-radius:1.4cqw 1.4cqw 0 0;display:block"></i>' for k, h in enumerate([22, 35, 30, 55, 92])) +
          f'</div><div style="display:flex;justify-content:space-between;font:700 4cqw {TEXT};color:{TX}"><span>Day 1</span><span>Day 30</span></div></div>')
VIMG = lambda img, pos="50% 50%", extra="": f'<img src="{img}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};{extra}">'
VCAP = lambda top="62%": f'<div style="position:absolute;left:8%;right:14%;top:{top};text-align:center;z-index:4"><span style="font:900 7cqw/1.25 {TEXT};color:#fff;text-shadow:0 .4cqw 1.2cqw rgba(0,0,0,.6);white-space:nowrap">NOBODY <span style="color:{HL}">TELLS</span> YOU</span></div>'
VTITLE = lambda top="9%", col="#fff": f'<div style="position:absolute;left:7%;right:7%;top:{top};font:400 13cqw/.9 {TITLE};color:{col};text-shadow:0 .5cqw 2cqw rgba(0,0,0,.5);z-index:4">{SAMPLE_TITLE}</div>'
VERT = [  # id, name, tier, line, inner
 ("full-face", "Full frame + captions", "C", "For: talking straight to camera.", VIMG(VF) + VCAP()),
 ("title-top", "Title on top", "C", "For: a hook that needs words on screen from the first second.",
  f'<div style="position:absolute;left:0;right:0;top:24%;bottom:0">{VIMG(VF, "50% 28%")}</div>' + VTITLE("7%") + VCAP("66%")),
 ("split", "Split: screen + you", "C", "For: showing something while you explain it.",
  f'<div style="position:absolute;left:0;right:0;top:0;height:60%;overflow:hidden">{SCREEN}</div><div style="position:absolute;left:0;right:0;bottom:0;height:40%">{VIMG(VF, "50% 22%")}</div>'
  f'<i style="position:absolute;left:0;right:0;top:59.6%;height:.8%;background:{HL};z-index:3"></i>' + VCAP("56.5%")),
 ("pip", "Picture in picture", "C", "For: the thing is the star, you comment in the corner.",
  SCREEN + f'<div style="position:absolute;left:6%;top:50.5%;width:33.3%;aspect-ratio:3/4;border-radius:4cqw;overflow:hidden;border:1cqw solid {HL};z-index:4">{VIMG(VF, "50% 24%")}</div>' + VCAP("42%")),
 ("card-text", "Text card", "C", "For: a list or a tip, no footage needed.",
  f'<div style="position:absolute;inset:0;background:{BG};padding:14% 8%;display:grid;align-content:start;gap:5cqw">'
  f'<div style="font:400 13cqw/.9 {TITLE};color:{TX}">{SAMPLE_TITLE}</div>' + ''.join(f'<div style="font:700 6cqw {TEXT};color:{TX};border-left:1.6cqw solid {HL};padding-left:3cqw">{x}</div>' for x in SAMPLE_LIST) + '</div>'),
 ("backdrop", "You over a backdrop", "R", "For: your room removed, a color behind you.",
  f'<div style="position:absolute;inset:0;background:{HL}"></div>{VIMG(VF, "50% 28%", "-webkit-mask-image:radial-gradient(ellipse 42% 38% at 50% 44%,#000 70%,transparent 72%);mask-image:radial-gradient(ellipse 42% 38% at 50% 44%,#000 70%,transparent 72%)")}' + VTITLE("8%", TX) + VCAP("70%")),
 ("before-after", "Before / after", "R", "For: showing a change, top vs bottom.",
  f'<div style="position:absolute;left:0;right:0;top:0;height:50%">{VIMG(VF, "50% 28%", "filter:grayscale(1) brightness(.75)")}</div><div style="position:absolute;left:0;right:0;bottom:0;height:50%">{VIMG(VF, "50% 28%", "filter:saturate(1.25)")}</div>'
  + ''.join(f'<span style="position:absolute;left:6%;top:{t};z-index:4;font:400 9cqw/1 {TITLE};background:{b};color:{c};padding:1cqw 3cqw">{w}</span>' for t, b, c, w in [("6%", "#fff", TX, "DAY 1"), ("56%", HL, TX, "DAY 30")])),
 ("reaction", "Reaction", "R", "For: reacting to something, your face small at the bottom.",
  f'<div style="position:absolute;left:0;right:0;top:44.7%;bottom:0">{VIMG(VF, "50% 18%")}</div><div style="position:absolute;left:0;right:0;top:13%;aspect-ratio:16/9;overflow:hidden;z-index:2">{SCREEN}</div>'
  f'<span style="position:absolute;left:6%;top:47%;z-index:4;background:{EX2};color:{TX};font:800 5cqw {TEXT};padding:1cqw 2.6cqw;border-radius:2cqw">wait for it…</span>' + VCAP("67%")),
 ("quote", "Big quote", "R", "For: one line you want people to screenshot.",
  f'<div style="position:absolute;inset:0;background:{TX};display:grid;align-content:center;padding:0 9%;gap:4cqw"><div style="font:400 30cqw/.6 {F["fr"]};color:{HL}">“</div>'
  f'<div style="font:400 11cqw/1 {F["is"]};color:{BG}">{SAMPLE_CAPTION[0].upper() + SAMPLE_CAPTION[1:]}.</div><div style="font:700 5cqw {TEXT};color:{HL}">{WM_HANDLE}</div></div>'),
 ("listicle", "Countdown list", "F", "For: top-3 style videos, the number stays on screen.",
  f'<div style="position:absolute;left:0;right:0;top:24%;bottom:0">{VIMG(VF, "50% 28%")}</div>' + f'<div style="position:absolute;left:6%;top:4%;z-index:4;display:flex;gap:3cqw;align-items:center"><span style="font:400 22cqw/.8 {TITLE};color:{HL}">#3</span><span style="font:800 6cqw {TEXT};color:#fff;background:{TX};padding:1cqw 2.4cqw">{SAMPLE_LIST[2][4:]}</span></div>'),
 ("zoom-frame", "Framed window", "F", "For: a softer look, the shot inside a border in your color.",
  f'<div style="position:absolute;inset:0;background:{EX2}"></div><div style="position:absolute;left:7%;right:7%;top:24%;bottom:22%;border-radius:6cqw;overflow:hidden;border:1.4cqw solid {TX}">{VIMG(VF, "50% 28%")}</div>' + VTITLE("3%", TX) + VCAP("78%")),
 ("notes", "Handwritten notes", "F", "For: explaining something, notes drawn over the shot.",
  VIMG(VF, "50% 28%") + f'<div style="position:absolute;left:6%;top:60%;z-index:4;font:700 10cqw/1 {NOTES};color:#fff;transform:rotate(-5deg);text-shadow:0 .4cqw 1.4cqw rgba(0,0,0,.7)">{SAMPLE_LABEL}</div>'
  f'<svg viewBox="0 0 100 20" style="position:absolute;left:6%;top:69%;width:52%;z-index:4;overflow:visible"><path d="M3 12 C 30 4, 60 18, 97 6" fill="none" stroke="{EX2}" stroke-width="3.5" stroke-linecap="round"/></svg>')]
# Cut-out and green-screen layouts use a plain gray silhouette for the creator (never another person's photo).
VSIL = lambda left="50%", h="58%", bottom="0", col="#8d8d8d": (f'<svg viewBox="0 0 100 120" preserveAspectRatio="xMidYMax meet" style="position:absolute;left:{left};bottom:{bottom};height:{h};transform:translateX(-50%);z-index:3;overflow:visible">'
    f'<circle cx="50" cy="32" r="20" fill="{col}"/><path d="M8 120 C 8 78, 26 60, 50 60 C 74 60, 92 78, 92 120 Z" fill="{col}"/></svg>')
DRAWN = (f'<div style="position:absolute;inset:0;background:linear-gradient({LT},{BG})"></div><div style="position:absolute;right:14%;top:12%;width:18cqw;aspect-ratio:1;border-radius:50%;background:{EX2}"></div>'
         f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute;left:0;right:0;bottom:0;height:50%;width:100%"><path d="M0 40 C 20 20, 40 30, 60 18 S 90 30, 100 22 L100 100 L0 100Z" fill="{HL}"/><path d="M0 70 C 25 55, 55 72, 100 58 L100 100 L0 100Z" fill="{TX}" opacity=".85"/></svg>')
WEBCARD = (f'<div style="position:absolute;inset:0;background:#f4f4f4;padding:10% 7%;display:grid;align-content:start;gap:3cqw">'
           f'<div style="display:flex;gap:2cqw;align-items:center"><i style="width:8cqw;height:8cqw;border-radius:50%;background:{HL};display:block"></i><i style="height:3cqw;width:40%;background:#bbb;border-radius:2cqw;display:block"></i></div>'
           + ''.join(f'<i style="height:3cqw;width:{w}%;background:#cfcfcf;border-radius:2cqw;display:block"></i>' for w in (92, 86, 95, 70)) +
           f'<div style="height:30cqw;border-radius:2cqw;background:linear-gradient(135deg,{HL},{EX2})"></div></div>')
FACECIRC = lambda left, top, size, pos="50% 26%": f'<div style="position:absolute;left:{left};top:{top};width:{size};aspect-ratio:1;border-radius:50%;overflow:hidden;border:1cqw solid #fff;z-index:4;box-shadow:0 1cqw 3cqw rgba(0,0,0,.4)">{VIMG(VF, pos)}</div>'
VERT_CUT = [
 ("cutout-screen", "Cut-out over the screen", "R", "For: talking over what you're showing.", SCREEN + VSIL("50%", "48%") + VCAP("44%")),
 ("title-behind", "Title behind you", "R", "For: a hook that sits right behind your head.", f'<div style="position:absolute;inset:0;background:{HL}"></div><div style="position:absolute;left:4%;right:4%;top:18%;font:400 26cqw/.82 {TITLE};color:{TX};z-index:2">I TRIED<br>IT</div>' + VSIL("50%", "56%")),
 ("number-behind", "Number behind you", "R", "For: a countdown or a big stat.", f'<div style="position:absolute;inset:0;background:{TX}"></div><div style="position:absolute;left:0;right:0;top:12%;text-align:center;font:400 78cqw/.8 {TITLE};color:{HL};z-index:2">30</div>' + VSIL("50%", "52%", col="#9a9a9a")),
 ("drawn-world", "You in a drawn world", "F", "For: a story told inside an illustration.", DRAWN + VSIL("38%", "44%", "6%")),
 ("green-room", "Green-screen room", "R", "For: a set you couldn't film in.", f'<div style="position:absolute;inset:0;background:url(img/backdrops/city-night.jpg) 40% center/cover"></div>' + VSIL("50%", "52%") + VCAP("62%")),
 ("over-screenshot", "Over a screenshot", "C", "For: reacting to a post, a page or a message.", WEBCARD + VSIL("62%", "40%")),
 ("floating-head", "Floating head", "C", "For: commenting on something, your face in a circle.", WEBCARD + FACECIRC("8%", "60%", "38%")),
 ("floating-cards", "Floating cards", "R", "For: listing points around you.", f'<div style="position:absolute;inset:0;background:{BG}"></div>' + VSIL("50%", "50%")
   + ''.join(f'<span style="position:absolute;left:{l};top:{t};z-index:4;background:#fff;color:{TX};font:700 5.4cqw {TEXT};padding:1.6cqw 3cqw;border-radius:2cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.2);transform:rotate({r}deg)">{w}</span>' for l, t, r, w in [("6%", "14%", -4, "Week one"), ("48%", "26%", 3, "The hard part"), ("12%", "38%", 2, "The result")])),
 ("comment-reply", "Reply to a comment", "C", "For: answering a viewer.", VIMG(VF) + f'<div style="position:absolute;left:6%;right:18%;top:12%;z-index:4;background:#fff;border-radius:3cqw;padding:3cqw;box-shadow:0 1cqw 3cqw rgba(0,0,0,.3)"><div style="font:700 4cqw {TEXT};color:#666">Reply to @viewer</div><div style="font:600 5.4cqw/1.25 {TEXT};color:#111">Does this really work?</div></div>'),
 ("pointing", "Pointing at the screen", "R", "For: \"look at this part\".", SCREEN + VSIL("30%", "46%") + f'<svg viewBox="0 0 100 100" style="position:absolute;left:30%;top:36%;width:40%;z-index:4;overflow:visible"><path d="M5 60 L 70 10" stroke="#8d8d8d" stroke-width="9" stroke-linecap="round"/><path d="M62 4 L 80 4 L 74 22" fill="none" stroke="{HL}" stroke-width="5" stroke-linecap="round"/></svg>'),
 ("stacked-reactions", "Stacked reactions", "F", "For: two takes on the same thing.", SCREEN + FACECIRC("6%", "56%", "34%") + FACECIRC("44%", "62%", "30%", "50% 26%")),
 ("side-by-side", "Side by side", "R", "For: comparing two things.", f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;gap:2px;background:#000"><div style="position:relative">{VIMG(VF, "50% 28%", "filter:grayscale(1)")}</div><div style="position:relative">{VIMG(VF, "50% 28%", "filter:saturate(1.3)")}</div></div>'
   + ''.join(f'<span style="position:absolute;left:{l};top:8%;z-index:4;font:400 9cqw/1 {TITLE};background:{b};color:{c};padding:1cqw 2.4cqw">{w}</span>' for l, b, c, w in [("4%", "#fff", TX, "THIS"), ("54%", HL, TX, "THAT")]))]
VERT_BFR = [
 ("notification", "Trapped in a notification", "F", "For: a joke about being ignored.", SCREEN + f'<div style="position:absolute;left:5%;right:5%;top:6%;z-index:4;background:rgba(255,255,255,.95);border-radius:4cqw;padding:2.6cqw;display:flex;gap:3cqw;align-items:center;box-shadow:0 1cqw 3cqw rgba(0,0,0,.3)"><div style="width:16cqw;aspect-ratio:1;border-radius:3cqw;overflow:hidden;position:relative;flex:none">{VIMG(VF)}</div><div><div style="font:800 4.4cqw {TEXT};color:#111">Let me out of here</div><div style="font:500 4cqw {TEXT};color:#666">now · tap to reply</div></div></div>'),
 ("peek", "Peeking in", "F", "For: interrupting your own video.", SCREEN + f'<div style="position:absolute;right:-22%;top:34%;width:60%;aspect-ratio:3/4;border-radius:50% 50% 0 0;overflow:hidden;z-index:4;transform:rotate(-12deg)">{VIMG(VF, "50% 28%")}</div><span style="position:absolute;left:12%;top:40%;z-index:4;font:700 9cqw {NOTES};color:{TX}">psst…</span>'),
 ("shrunk", "Shrunk in a frame", "F", "For: feeling small, or a \"portrait\" joke.", f'<div style="position:absolute;inset:0;background:#d9cfc0;background-image:repeating-linear-gradient(90deg,rgba(0,0,0,.04) 0 2px,transparent 2px 9px)"></div><div style="position:absolute;left:32%;top:30%;width:36%;aspect-ratio:3/4;border:2.6cqw solid #a07a3e;box-shadow:inset 0 0 0 1cqw #d8b46a,0 2cqw 4cqw rgba(0,0,0,.35);overflow:hidden">{VIMG(VF, "50% 28%")}</div>'),
 ("crack", "The screen cracks", "F", "For: a moment that \"breaks\" the video.", VIMG(VF) + '<svg viewBox="0 0 100 178" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%;z-index:4"><g fill="none" stroke="#fff" stroke-width=".7" opacity=".9"><path d="M30 60 L10 20 M30 60 L0 70 M30 60 L22 110 L5 150 M30 60 L60 40 L90 10 M30 60 L55 85 L100 95 M55 85 L60 130 L80 178 M22 110 L45 120"/></g></svg>'),
 ("tilt", "The frame tilts", "F", "For: things going sideways.", f'<div style="position:absolute;inset:0;background:#111"></div><div style="position:absolute;inset:10% 4%;transform:rotate(-9deg);border:1cqw solid #fff;overflow:hidden">{VIMG(VF)}</div>' + VCAP("72%"))]
VBTN = [{"value": "keep", "label": "Keep in library"}, {"value": "no", "label": "Discard"}]
vsec = lambda id, title, line, rows: {"id": id, "title": title, "line": line, "kind": "library", "keepWord": "layout|layouts", "layout": "tiles", "aspect": "3/4.6", "movable": False,
   "buttons": VBTN, "keepValues": ["keep"], "options": [{"id": v[0], "name": v[1], "line": v[3], "html": phone(v[4]), **({} if VF in v[4] else {"photoTag": ""}), **({"pick": True, "why": "It's the one you'll use most; the captions carry the video."} if v[0] == "full-face" else {})} for v in rows]}
W("vertical-layouts", {
 "round": "vertical-layouts", "kind": "library", "keepWord": "layout|layouts", "photoTag": PHOTO_TAG,
 "fonts": ["bebas-neue", "inter", "fraunces", "instrument-serif", "caveat"],
 "title": "Layouts for Shorts, Reels and TikTok", "what": "Each one on a phone. Faded shapes are the app's buttons; keep words inside the dashed box; the dotted lines show what the grid keeps.",
 "next": "Next: hook text, the words on screen from the first second.", "persona": SAY_PERSONA,
 "sections": [vsec("everyday", "Everyday", "", VERT), vsec("cutout", "Cut-out and green screen", "Your background removed or replaced.", VERT_CUT), vsec("bfr", "Break-from-reality", "Layouts that bend the frame for a laugh.", VERT_BFR)]})

# ---------- Change mode (revisit.md): the same page as the first build, opened on one decision ----------
# The current pick comes first, tagged "What you have now"; the header says only this one thing is changing.
_c = json.loads((EX / "palette-tiles.json").read_text(encoding="utf-8"))
_opts = [o for o in _c["options"] if not o.get("control")]
_cur = dict(_opts[0]); _cur.update({"id": "current", "current": True}); _cur.pop("pick", None); _cur.pop("why", None)
_c.update({"round": "change-palette-tiles", "change": "Color palette",
           "what": "Your current palette is first. Mark any you'd compare against it; you'll pick one next.",
           "options": [o for o in _c["options"] if o.get("control")] + [_cur] + [dict(o, **({"pick": True, "why": "Close to what you have, a little warmer."} if i == 0 else {})) for i, o in enumerate(_opts[1:])]})
for k in ("stage", "stepId", "part", "journeyIf", "nicheWords"): _c.pop(k, None)
W("change-palette-tiles", _c)

# ---------- The Brand Genome page (Stage 9): one page, built from the picks' own cards ----------
# build.py sees "page": "genome" and uses genome-page.html. Each item copies the html of the option that was picked
# on its round's page, so the Genome shows exactly what was chosen. This example is Wren's (the demo persona).
def _ex(name): return json.loads((EX / (name + ".json")).read_text(encoding="utf-8"))
def _opts(d): return [o for s in (d.get("sections") or [{"options": d.get("options") or []}]) for o in s["options"] if not o.get("control")]
def _item(name, oid, label, note=None):
    d = _ex(name); o = next(x for x in _opts(d) if x["id"] == oid)
    it = {"id": oid, "name": o["name"], "label": label, "note": note if note is not None else o.get("line", "")}
    for k in ("html", "play", "playMs"):
        if k in o: it[k] = o[k]
    if "images" in o: it.update({"image": o["images"][0], "css": o.get("css", ""), "overlay": o.get("overlay", "")})
    if d.get("aspect"): it["aspect"] = d["aspect"]
    return it
def _lib(name, ids, label="Kept"): return [_item(name, i, label) for i in ids]
_heads = {}
for n in ("music", "sting-pick", "sound-logo-pick"):
    _heads[n] = _ex(n).get("head", "")
GEN_HEAD = _heads["music"] + LOGO_DATA + STING_DATA + STING_JS
W("genome-wren", {
 "page": "genome", "title": "Wren · Brand Genome", "updated": "2026-10-09", "persona": SAY_PERSONA, "head": GEN_HEAD,
 "fonts": ["bebas-neue", "inter", "caveat", "anton", "space-mono", "fraunces", "instrument-serif", "bowlby-one", "unbounded", "permanent-marker", "special-elite"],
 "fontsCss": {"title": TITLE, "text": TEXT, "notes": NOTES},
 "palette": [{"hex": h, "role": r, "on": TX if i != 1 else BG} for i, (h, r) in enumerate(zip(P, ROLES))],
 "creator": {"name": "Wren", "handle": "@wren", "promise": "Calm, honest grooming for anxious dogs, filmed the way I wish other groomers did.",
             "chips": ["Entertaining first", "Then useful", "YouTube · Shorts · Reels"],
             "wordmarkHtml": f'<div style="position:absolute;inset:0;container-type:inline-size;background:{BG};color:{TX};display:grid;place-items:center">{WMS[0][4]}</div>'},
 "sections": [
  {"title": "Who and why", "change": "interview answers", "line": "Written from the interview. Every script, hook and title is checked against it.",
   "text": ["Wren runs a one-chair grooming studio in Austin. The channel exists because grooming videos online look loud and rushed, and nervous dogs deserve better.",
            "For: owners of anxious dogs, and groomers who want a calmer way to work."],
   "list": ["Feel: entertaining first, then useful", "How far she'll go: her face on camera, her own clients' dogs (with permission), no fake rescues", "Proof first, humble line second"]},
  {"title": "Formats", "change": "Formats", "line": "The shows she repeats. Ideas come per video from idea-genome.",
   "list": ["The 60-second fix: one problem, solved on camera, before and after (vertical)", "The full session: one nervous dog, start to finish, calm and honest (long)"]},
  {"title": "Colors", "change": "Color palette", "from": "", "line": "Fresh mint. Roles in order: background, words, pop color, second color, pale.", "palette": True},
  {"title": "Footage look", "change": "Color editing", "line": "How her clips are colored. The backup is for days the main one doesn't work.", "min": "340px",
   "items": [_item("footage-looks-pick", "clean-bright", "Main", "Tuned to her palette automatically."), _item("footage-looks-pick", "warm-film", "Backup")]},
  {"title": "Fonts", "change": "Fonts", "line": "One set for everything.",
   "fontSet": [{"job": "Big titles", "name": "Bebas Neue", "css": TITLE, "sample": "I TRIED IT"}, {"job": "Text", "name": "Inter", "css": TEXT, "sample": "Here's what happened."}, {"job": "Notes", "name": "Caveat", "css": NOTES, "sample": "start here →"}]},
  {"title": "Words on video", "change": "Text style", "line": "How titles and labels sit on the video, and the captions while she talks.", "min": "340px",
   "items": [_item("text-style-pick", "blocks", "Main", "Text style"), _item("text-style-pick", "bar", "Backup", "Text style"), _item("captions-pick", "strip", "Main", "Captions, in her caption font"), _item("captions-pick", "highlight", "Backup", "Captions")]},
  {"title": "Movement", "change": "Motion feel", "line": "How everything moves. Press Play.", "min": "340px",
   "items": [{"id": "feel-glide", "name": "Calm", "label": "Main", "note": "Motion feel", "html": mf("glide"), "play": True, "playMs": FEEL_MS("glide")},
             {"id": "feel-snap", "name": "Snappy", "label": "Backup", "note": "Motion feel", "html": mf("snap"), "play": True, "playMs": FEEL_MS("snap")}] + _lib("motion-entrances", ["fade-up", "mask"], "Library")},
  {"title": "Sound", "change": "Music", "line": "Sketches of the music lanes she kept, then her sting and sound logo. Press Play.",
   "items": _lib("music", ["lofi", "acoustic"], "Library") + [_item("sting-pick", "pop-in", "Main", "Sting: plays right after the hook"), _item("sound-logo-pick", "rise3", "Main", "Sound logo: plays with the sting")]},
  {"title": "Brand kit", "change": "Brand kit", "line": "Every piece, shown where it lives.", "min": "340px",
   "items": [_item("wordmark-tiles", "episode-pill", "Main"), _item("name-tag-tiles", "bar", "Main"), _item("series-tag-tiles", "pill", "Main"), _item("close-out", "next-video", "Library"), _item("profile-picture-tiles", "mono-pop", "Main"), _item("banner-tiles", "promise", "Main")]},
  {"title": "Shorts and Reels", "change": "Vertical layouts", "line": "Her vertical layouts, on a phone.", "min": "220px",
   "items": _lib("vertical-layouts", ["full-face", "split", "before-after"], "Library")},
  {"title": "Voice", "change": "Writing voice", "line": "How she writes: warm, plain, a little dry.",
   "list": ["“He hated the dryer. Then we tried this.”", "“No sedation, no tricks. Just time.”", "“If your dog shakes in the car, start here.”"]},
  {"title": "Profiles", "change": "Bios", "line": "Written automatically from everything above. Change any line by asking in chat.",
   "list": ["YouTube: Calm grooming for anxious dogs. New full session every Tuesday, quick fixes in Shorts.", "Instagram: Austin groomer · anxious dogs welcome · before and afters, no drama"]},
  {"title": "Run sheet", "change": "Run sheet", "line": "The checks every video plan passes.",
   "list": ["Format named, or a one-off with a reason", "Main look, backdrop and any filters from the library", "Motion table and music lane per section", "Every beat delivers \"entertaining\" (a joke, a reveal, a payoff)", "Inside how far she'll go", "2–3 break-from-reality spots proposed, 1–2 kept", "Pictures follow the image rules", "Vertical moments with a 3-second hook", "Script passes the voice kit", "Every claim traces to Proof"]},
  {"title": "Break-from-reality moments", "change": "Break-from-reality moments", "line": "The cutaways she kept: normal shot, the cutaway, back. Each with when to use it.", "min": "420px",
   "items": [dict(_item("break-from-reality", "nature-doc", "Our pick", "Use when: a slow, careful moment needs a laugh."), aspect="5/2"),
             dict(_item("break-from-reality", "breaking-news", "Kept", "Use when: a tiny win deserves a headline."), aspect="5/2"),
             dict(_item("break-from-reality", "courtroom", "Your quirk", "From her interview: she puts bad habits on trial. Use when: an owner admits a mistake."), aspect="5/2")]},
  {"title": "Images and likeness", "change": "Image rules", "line": "How generated pictures may show her.",
   "list": ["Generated pictures show her subject, not her, unless she approves a likeness brief first", "Reference photos: 2 of 9 sent (face straight on, smiling); 7 still owed, all optional", "Never show a real person or animal doing something they didn't", "AI labels only where a platform requires them"]},
  {"title": "House rules", "change": "House rules", "line": "Every no, with its reason. They bind every video.",
   "list": ["No neon: it reads as a nightclub, not a studio", "No bouncy text: it feels childish for nervous owners", "No stock music with vocals under talking"]}],
 "highlights": "Highlights only. The full brand, including every library, research default and rule, is in Brand Genome.md in your brand folder. Every video skill reads that file.",
 "offline": "Brand Genome (visual).html",
 "changes": ["2026-10-09 · Brand Genome built (demo)."]})
