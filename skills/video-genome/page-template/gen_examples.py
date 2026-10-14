#!/usr/bin/env python3
"""Regenerate the model page JSONs in examples/ (one per kind of video-genome decision).

usage: python3 gen_examples.py          → writes examples/*.json
Build any of them:  python3 build.py examples/hooks-pick.json out.html

Sample copy is universal (a sample video called "I Tried It for 30 Days"). In a real run,
copy the nearest example, swap the mocks for real stills of the creator's footage or the
built scene, and fill `context` with the real time, line and what's on screen.
"""
import json, pathlib
from mocks import svg, speaker, text, panel, lower_third, curve, thumb, phone, BG, BG2, SP, INK

OUT = pathlib.Path(__file__).parent / "examples"
OUT.mkdir(exist_ok=True)
FONTS = ["inter"]

# The included kits (setup/brand-intake.md). Each: palette (background, words, pop color), title/text fonts, motion feel.
KITS = [
    ("clean-studio", "Clean studio", "#F5F5F2", "#121212", "#2F6BFF", "inter", "Inter", "inter", "Glide", "Calm, clear, explainers and tutorials"),
    ("night-desk", "Night desk", "#0E1116", "#E8ECF1", "#3DDC97", "space-grotesk", "Space Grotesk", "space-grotesk", "Snap", "Tech, tools, screens and builds"),
    ("marker-paper", "Marker and paper", "#FAF6EC", "#222222", "#FF5A36", "permanent-marker", "Permanent Marker", "patrick-hand", "Deadpan", "Handmade, funny, honest takes"),
    ("bold-block", "Bold block", "#111111", "#FFFFFF", "#FFDD00", "anton", "Anton", "inter", "Punch", "High energy, reactions, big claims"),
    ("editorial", "Editorial", "#F2EEE6", "#1B1B1B", "#C8102E", "dm-serif-display", "DM Serif Display", "source-serif-4", "Drift", "Stories, essays, slower and premium"),
    ("arcade", "Arcade", "#1A1033", "#F7F2FF", "#FF3D9A", "bungee", "Bungee", "space-mono", "Mechanical", "Games, internet culture, playful"),
    ("calm-natural", "Calm natural", "#EEF2EC", "#23302A", "#4E8A63", "fraunces", "Fraunces", "nunito", "Glide", "Lifestyle, food, slow living, wellness"),
    ("soup-kitchen", "Soup Kitchen", "#FFF4D6", "#1F2A44", "#E8452C", "titan-one", "Titan One", "nunito", "Handmade", "Food spots, small businesses, funny day-in-the-life, clay characters"),
]


def kit_mock(bg, ink, pop, tfam):
    f = f"'{tfam}',Inter,Arial,sans-serif"
    return svg(speaker(250, 0.95, "#9aa3b2") + text(18, 62, 24, "I Tried It", ink, 800, font=f)
               + text(18, 90, 24, "for 30 Days", pop, 800, font=f)
               + f'<rect x="18" y="104" width="70" height="4" fill="{pop}"/>'
               + f'<rect x="16" y="132" width="132" height="30" rx="2" fill="{ink}" opacity=".08"/><rect x="16" y="132" width="4" height="30" fill="{pop}"/>'
               + text(26, 146, 11, "Sam Rivera", ink, 800, font=f) + text(26, 157, 7.5, "Day 1 vs Day 30", ink, 500)
               + f'<rect x="168" y="150" width="140" height="18" rx="2" fill="#000" opacity=".55"/>'
               + text(176, 162, 9, "and that's the", "#fff", 700) + text(250, 162, 9, "part", pop, 800), bg)


def write(name, page):
    (OUT / f"{name}.json").write_text(json.dumps(page, indent=1, ensure_ascii=False), encoding="utf-8")


PICK_BUTTONS = [{"value": "pick", "label": "Main"}, {"value": "backup", "label": "Backup"},
                {"value": "alt", "label": "Alternative"}, {"value": "no", "label": "Discard"}]
PICK = {"kind": "fixed", "single": "pick", "singleFallback": "backup", "altValue": "alt",
        "buttons": PICK_BUTTONS, "keepValues": ["pick", "backup", "alt"], "keepWord": "option|options"}
FINALISTS = {"kind": "finalists", "layout": "tiles", "trimAbove": 6, "keepWord": "finalist|finalists",
             "keepValues": ["yes"], "buttons": [{"value": "yes", "label": "Finalist"}, {"value": "no", "label": "Discard"}]}

# ---- Start · Your brand: the included kits (only when they have no brand kit) ----
write("brand-kits", {**PICK, "round": "brand-kits", "stage": "start", "stepId": "brand",
    "fonts": sorted({"inter"} | {k[5] for k in KITS} | {k[7] for k in KITS}),
    "title": "Included brand kits",
    "what": "Pick the kit your videos will use. Colors, fonts and how things move all come with it.",
    "next": "Next: what you brought (your idea, brief or plan).",
    "options": [{"id": k[0], "name": k[1], "line": f"For: {k[9]}. Moves: {k[8].lower()}.",
                 "swatches": [{"hex": k[2], "role": "background"}, {"hex": k[3], "role": "words"}, {"hex": k[4], "role": "pop color"}],
                 "html": kit_mock(k[2], k[3], k[4], k[6]), **({"pick": True, "why": "Fits most talking-head videos; easy to read on a phone."} if i == 0 else {})}
                for i, k in enumerate(KITS)]})

# ---- Start · What you brought: confirm what was taken from their plan / brief ----
def note_card(t1, t2):
    return svg(text(18, 74, 15, t1, INK, 800) + text(18, 100, 12, t2, SP, 500), BG2)

write("intake-confirm", {"round": "intake-confirm", "stage": "start", "stepId": "intake", "fonts": FONTS,
    "kind": "adjust", "keepValues": ["ok"], "keepWord": "item|items",
    "buttons": [{"value": "ok", "label": "Confirm"}, {"value": "change", "label": "Change it"}],
    "title": "What you brought",
    "what": "These came from your plan. Confirm each one, or mark it to change. Nothing here gets asked again unless you change it.",
    "next": "Next: the open decisions, one at a time.",
    "options": [
        {"id": "promise", "name": "Promise", "taken": True, "line": "What the viewer gets: whether the 30-day test was worth it.", "html": note_card("The promise", "Was it worth it? You'll know by 0:10.")},
        {"id": "arc", "name": "Story arc", "taken": "your brief", "line": "Problem, turn, payoff. Switching arcs would mean rewriting the middle of your script.", "html": note_card("Problem → turn → payoff", "Your script already follows this.")},
        {"id": "length", "name": "Length", "taken": True, "line": "About 8 minutes.", "html": note_card("About 8 min", "Long video plus 2 Shorts")},
        {"id": "hook", "name": "Opening line", "taken": "your script", "line": "\"Day 1, I almost quit.\"", "html": note_card("“Day 1, I almost quit.”", "First words on screen")},
    ]})

# ---- Plan · Opening line: finalists → pick ----
HOOKS = [("cold-open", "Cold open", "Start on day 30's result, then rewind.", "Day 30."),
         ("confession", "Confession", "Start with the moment you almost quit.", "I almost quit."),
         ("number", "One number", "Start on the number that changed.", "38%"),
         ("question", "Question", "Ask the viewer the question you had.", "Worth it?"),
         ("contrast", "Day 1 vs Day 30", "Show both days side by side, no words.", "1 vs 30"),
         ("dare", "The dare", "Start with who told you it wouldn't work.", "\"You won't last.\"")]

def hook_mock(word, accent="#F2B33D"):
    return svg(speaker(80, 1.0) + text(220, 100, 30 if len(word) < 10 else 20, word, accent, 900, "middle"))

write("hooks-tiles", {**FINALISTS, "round": "hooks-tiles", "stage": "plan", "stepId": "hooks", "part": "1 of 2", "fonts": FONTS,
    "title": "Opening line",
    "what": "The first 3 seconds: what you say, the words on screen and the first picture, together.",
    "next": "Next: pick a main and a backup from your finalists.",
    "options": [{"id": h[0], "name": h[1], "line": h[2], "html": hook_mock(h[3])} for h in HOOKS]})
write("hooks-pick", {**PICK, "round": "hooks-pick", "stage": "plan", "stepId": "hooks", "part": "2 of 2", "fonts": FONTS,
    "title": "Opening line: your finalists",
    "what": "Pick the opening you'll record first. The backup gets recorded too, so the edit can swap them.",
    "next": "Next: the script.",
    "options": [{"id": h[0], "name": h[1], "line": h[2], "html": hook_mock(h[3]), **({"pick": True, "why": "Proves the promise before anything else."} if h[0] == "cold-open" else {})}
                for h in HOOKS[:3]]})

# ---- Plan · Story arc: one pick, one taken from their brief ----
ARCS = [("problem-turn-payoff", "Problem, turn, payoff", [(0, .3), (.3, .2), (.55, .5), (.75, .9), (1, .7)]),
        ("rags-riches", "Low to high", [(0, .1), (.4, .3), (.7, .6), (1, .95)]),
        ("man-in-hole", "Fall, then climb", [(0, .6), (.3, .15), (.6, .5), (1, .9)]),
        ("loop", "Ends where it starts", [(0, .6), (.3, .3), (.6, .8), (1, .6)])]
write("arc", {**PICK, "round": "arc", "stage": "plan", "stepId": "arc", "fonts": FONTS,
    "title": "Story arc",
    "what": "How the feeling moves from start to end. The line shows energy over the video.",
    "next": "Next: the rest of the story plan.",
    "options": [{"id": a[0], "name": a[1], "line": "The shape your brief already follows." if i == 0 else "Would change where the high point lands.",
                 "html": svg(curve(a[2], "#F2B33D")), **({"taken": "your brief", "pick": True, "why": "Your script is already built on it; changing it means rewriting the middle."} if i == 0 else {})}
                for i, a in enumerate(ARCS)]})

# ---- Plan · Title: pick, shown at feed size ----
write("titles", {**PICK, "round": "titles", "stage": "plan", "stepId": "titles", "fonts": FONTS,
    "title": "Title",
    "what": "How the video reads in the feed. Each title is shown with the thumbnail idea it promises.",
    "next": "Next: the thumbnail.",
    "options": [{"id": "t1", "name": "I Tried It for 30 Days", "line": "Plain promise. Safe.", "html": thumb("30 DAYS|LATER", "#F2B33D")},
                {"id": "t2", "name": "Day 1 vs Day 30", "line": "The contrast does the work.", "html": thumb("DAY 1|DAY 30", "#3DDC97"), "pick": True, "why": "The thumbnail can show it in one glance."},
                {"id": "t3", "name": "Nobody Tells You This About Day 12", "line": "Curiosity; must pay off.", "html": thumb("DAY|12", "#FF5A36")}]})

# ---- Plan · Break-from-reality moments: library, each with where it lands ----
def strip(a, b, c):
    return svg(f'<rect x="0" y="0" width="104" height="180" fill="{BG2}"/><rect x="108" y="0" width="104" height="180" fill="{BG}"/><rect x="216" y="0" width="104" height="180" fill="{BG2}"/>'
               + text(52, 96, 12, a, INK, 700, "middle") + text(160, 96, 12, b, "#F2B33D", 800, "middle") + text(268, 96, 12, c, INK, 700, "middle"))
write("break-from-reality", {"round": "break-from-reality", "stage": "plan", "stepId": "break-from-reality", "fonts": FONTS,
    "kind": "library", "keepValues": ["keep"], "keepWord": "moment|moments",
    "buttons": [{"value": "keep", "label": "Draft it"}, {"value": "no", "label": "Skip"}],
    "title": "Cutaway gags",
    "what": "Short cutaways where the video stops being normal for a beat. Final videos keep one or two. (Use the brand file's own name for these if it has one.)",
    "next": "Next: music.",
    "options": [
        {"id": "nature-doc", "name": "Nature documentary", "at": "1:40, after \"I almost quit\"", "line": "A narrator describes you like a wild animal.", "html": strip("you, tired", "“the creature rests”", "back to you")},
        {"id": "clone-meeting", "name": "Meeting with yourself", "at": "3:10, the turn", "line": "Three of you argue about quitting.", "html": strip("question", "3 of you", "the answer"), "pick": True, "why": "Lands on the turn, where the energy needs a lift."},
        {"id": "trailer", "name": "Movie trailer", "at": "6:30, before the result", "line": "The last week cut like a trailer.", "html": strip("day 25", "IN A WORLD", "day 30")},
    ]})

# ---- Build · One moment: the look for a single moment, with context ----
A = "#F2B33D"
write("moment-look", {**PICK, "round": "moment-look", "stage": "build-f", "stepId": "moments", "journeyIf": ["footage-first"], "fonts": FONTS,
    "title": "The 38% moment",
    "what": "What appears while you say the number.",
    "context": {"time": "2:14", "said": "and my focus went up thirty-eight percent", "now": "you, center-left, talking to camera",
                "changes": "only this moment; the next one is decided on its own page"},
    "next": "Next: the moment at 2:31.",
    "options": [
        {"id": "big-number", "name": "Big number", "line": "The number fills the open side.", "html": svg(speaker(90) + text(225, 104, 52, "38%", A, 900, "middle") + text(225, 126, 11, "focus, day 1 vs day 30", INK, 600, "middle")), "pick": True, "why": "One clear star; nothing to read but the number."},
        {"id": "bar", "name": "Bar grows", "line": "Two bars, day 1 and day 30.", "html": svg(speaker(90) + f'<rect x="168" y="110" width="40" height="40" fill="{SP}"/><rect x="226" y="60" width="40" height="90" fill="{A}"/>' + text(188, 164, 9, "Day 1", INK, 600, "middle") + text(246, 164, 9, "Day 30", INK, 600, "middle"))},
        {"id": "behind", "name": "Words behind you", "line": "The number sits behind your shoulder.", "html": svg(text(118, 118, 66, "38%", A, 900, "middle") + speaker(232))},
        {"id": "stamp", "name": "Stamp", "line": "A rubber-stamp number thuds onto the frame.", "outside": True, "html": svg(speaker(90) + f'<g transform="rotate(-8 230 95)"><rect x="180" y="66" width="104" height="54" fill="none" stroke="{A}" stroke-width="4"/>' + text(232, 106, 32, "+38%", A, 900, "middle") + "</g>")},
    ]})

# ---- Build · Where you sit on screen: placement on a real frame ----
G = "#2EB67D"
write("placement", {**PICK, "round": "placement", "stage": "build-g", "stepId": "placement", "journeyIf": ["graphics-first"], "fonts": FONTS,
    "title": "Where you sit on screen",
    "what": "Your default spot next to the graphics. Single moments can still change it.",
    "context": {"time": "0:42–1:30", "said": "here's what the first week looked like", "now": "a list of the first 7 days", "changes": "the default for the whole video"},
    "next": "Next: rebuild the video on your words.",
    "options": [
        {"id": "third", "name": "You on a third", "line": "You on the left, the graphic fills the rest.", "html": svg(speaker(80) + panel(150, 26, 154, 128, G, 6)), "pick": True, "why": "Keeps your face big and the list readable."},
        {"id": "bubble", "name": "Corner bubble", "line": "You small in a corner, the graphic full size.", "html": svg(panel(16, 16, 288, 148, G, 8) + f'<rect x="218" y="104" width="86" height="60" rx="6" fill="{BG}" stroke="{INK}" stroke-width="1.5"/>' + f'<g transform="translate(221,104) scale(.27)">{speaker(150)}</g>')},
        {"id": "turns", "name": "Taking turns", "line": "You full screen, then the graphic full screen.", "html": svg(f'<g opacity=".55">{speaker(90)}</g>' + panel(170, 26, 134, 128, G, 6) + text(160, 172, 9, "alternates", SP, 600, "middle"))},
        {"id": "split", "name": "Split", "line": "Half you, half the graphic.", "html": svg(f'<rect x="160" y="0" width="160" height="180" fill="{BG2}"/>' + speaker(80) + panel(176, 26, 128, 128, G, 6))},
    ]})

# ---- Build · The cut: keep or cut each span ----
write("cut-list", {"round": "cut-list", "stage": "build-f", "stepId": "cut", "journeyIf": ["footage-first"], "fonts": FONTS,
    "kind": "adjust", "keepValues": ["keep"], "keepWord": "part|parts",
    "buttons": [{"value": "keep", "label": "Keep"}, {"value": "cut", "label": "Cut"}],
    "title": "The cut",
    "what": "Each part of your take, in order. Stumbles and repeats are already out; these are the judgment calls.",
    "next": "Next: the style of the edit.",
    "options": [
        {"id": "s1", "name": "Second try at the opening", "at": "0:04–0:09", "line": "\"Day 1, I almost quit. Like, really.\" Cleaner than the first try.", "html": svg(speaker(160) + text(160, 170, 10, "take 2", SP, 600, "middle"))},
        {"id": "s2", "name": "The side story", "at": "1:52–2:20", "line": "The story about the gym. Funny, but slows the middle.", "html": svg(speaker(160) + text(160, 170, 10, "28 s", SP, 600, "middle"))},
        {"id": "s3", "name": "Long pause before the result", "at": "6:41–6:44", "line": "A 3-second pause. Could be tension, could be dead air.", "html": svg(speaker(160) + text(160, 170, 10, "3 s", SP, 600, "middle"))},
    ]})

# ---- Build · Draft video review: per scene ----
write("draft-review", {"round": "draft-review", "stage": "build-g", "stepId": "draft", "journeyIf": ["graphics-first"], "fonts": FONTS,
    "kind": "adjust", "keepValues": ["ok"], "keepWord": "scene|scenes",
    "buttons": [{"value": "ok", "label": "Looks right"}, {"value": "change", "label": "Change it"}],
    "title": "Draft video",
    "what": "One still per scene of the draft. Mark what to change and say how in the note.",
    "next": "Next: your recording kit.",
    "options": [
        {"id": "sc1", "name": "Opening", "at": "0:00–0:06", "line": "Day 30 result, then rewind.", "html": svg(text(160, 100, 36, "DAY 30", A, 900, "middle"))},
        {"id": "sc2", "name": "The first week", "at": "0:42–1:30", "line": "List of the first 7 days beside you.", "html": svg(speaker(80) + panel(150, 26, 154, 128, A, 6))},
        {"id": "sc3", "name": "The 38% moment", "at": "2:14", "line": "Big number on the open side.", "html": svg(speaker(90) + text(225, 104, 52, "38%", A, 900, "middle"))},
    ]})

# ---- Deliver · Brand review: anything used outside the brand this session ----
write("brand-review", {"round": "brand-review", "stage": "deliver", "stepId": "brand-review", "fonts": FONTS,
    "kind": "adjust", "keepValues": ["add"], "keepWord": "item|items",
    "buttons": [{"value": "add", "label": "Add to my brand"}, {"value": "once", "label": "Keep as one-off"}, {"value": "no", "label": "Don't use again"}],
    "title": "Brand review",
    "what": "Things this video used that aren't in your brand yet. Decide what happens to each.",
    "next": "Next: files and delivery.",
    "options": [
        {"id": "stamp", "name": "Stamp number", "at": "2:14, the 38% moment", "line": "A stamped number. Same colors and fonts, new move.", "outside": True, "html": svg(speaker(90) + f'<g transform="rotate(-8 230 95)"><rect x="180" y="66" width="104" height="54" fill="none" stroke="{A}" stroke-width="4"/>' + text(232, 106, 32, "+38%", A, 900, "middle") + "</g>")},
        {"id": "split", "name": "Split screen", "at": "5:02–5:20", "line": "Half you, half the graphic. Your brand had only the corner bubble.", "outside": True, "html": svg(f'<rect x="160" y="0" width="160" height="180" fill="{BG2}"/>' + speaker(80) + panel(176, 26, 128, 128, A, 6))},
    ]})

# ---- Plan · Rest of the story plan: Claude's picks for the remaining layers, confirmed on one page ----
write("story-rest", {"round": "story-rest", "stage": "plan", "stepId": "story-rest", "fonts": FONTS,
    "kind": "adjust", "keepValues": ["ok"], "keepWord": "part|parts",
    "buttons": [{"value": "ok", "label": "Confirm"}, {"value": "change", "label": "Change it"}],
    "title": "Rest of the story plan",
    "what": "How the video keeps people watching. Picked to fit your arc; confirm each or mark it to change.",
    "next": "Next: the opening line.",
    "options": [
        {"id": "proof", "name": "Proof", "line": "Show the day 30 result on screen, not just say it.", "html": note_card("Proof", "The real result, shown")},
        {"id": "retention", "name": "Keeping people watching", "line": "A tease at 2:00 (\"day 12 nearly ended it\") paid off at 4:30.", "html": note_card("Tease and payoff", "2:00 → 4:30")},
        {"id": "pacing", "name": "Pace", "line": "Fast first minute, slower middle, fastest just before the result.", "html": svg(curve([(0, .8), (.3, .4), (.6, .5), (.8, .95), (1, .6)], "#F2B33D"))},
        {"id": "ending", "name": "Ending and ask", "line": "Call back to day 1, then one reason to watch the next video.", "html": note_card("Callback + next video", "No slow wind-down")},
    ]})

# ---- Plan · Music: one lane per part of the video, confirmed on one page ----
write("music", {"round": "music", "stage": "plan", "stepId": "music", "fonts": FONTS,
    "kind": "adjust", "keepValues": ["ok"], "keepWord": "part|parts",
    "buttons": [{"value": "ok", "label": "Sounds right"}, {"value": "change", "label": "Change it"}],
    "title": "Music",
    "what": "The kind of music under each part, from your brand. These are descriptions; real tracks come later (cost shown first).",
    "next": "Next: Shorts moments.",
    "options": [
        {"id": "m-open", "name": "Opening", "at": "0:00–0:40", "line": "Tension pulse, 128 BPM, builds to the first cut.", "html": note_card("Tension pulse · 128", "0:00–0:40")},
        {"id": "m-middle", "name": "The 30 days", "at": "0:40–6:00", "line": "Minimal electronic, 118 BPM, low under your voice.", "html": note_card("Minimal electronic · 118", "0:40–6:00")},
        {"id": "m-end", "name": "The result", "at": "6:00–end", "line": "Cinematic build, 96 BPM, peaks on the result.", "html": note_card("Cinematic build · 96", "6:00–end")},
    ]})

# ---- Plan · Shorts moments: library in 9:16 ----
write("vertical-moments", {"round": "vertical-moments", "stage": "plan", "stepId": "vertical-moments", "fonts": FONTS, "aspect": "9/16", "layout": "tiles",
    "kind": "library", "keepValues": ["keep"], "keepWord": "Short|Shorts",
    "buttons": [{"value": "keep", "label": "Make a Short"}, {"value": "no", "label": "Skip"}],
    "title": "Shorts moments",
    "what": "Parts of the video that work alone. Each needs a hook in its first 3 seconds.",
    "next": "Next: the ending and the ask.",
    "options": [
        {"id": "v1", "name": "Almost quit", "at": "1:35–2:05", "line": "Opens on \"I almost quit.\"", "html": phone(f'<g transform="translate(-26,0) scale(.5)">{speaker(160)}</g>' + f'<rect x="10" y="124" width="88" height="18" rx="2" fill="{A}"/>')},
        {"id": "v2", "name": "The 38%", "at": "2:10–2:40", "line": "Opens on the number.", "html": phone(text(54, 60, 26, "38%", A, 900, "middle") + f'<g transform="translate(-26,40) scale(.5)">{speaker(160)}</g>')},
    ]})

# ---- Plan · look: motion test pack (rendered clips, Keep / Skip) ----
# Clip cards: the mock sits under the video, so the page reads even before the clips are rendered.
# In a real run each clip is the move rebuilt in the brand with real screens (craft/spatial/README.md),
# drafted at 15 fps, 6 s, and published with the page as clips/<id>.mp4 + clips/<id>.jpg.
CLIP_HEAD = ('<script>window.playClip=function(id,el){var v=el.querySelector("video");if(v){v.currentTime=0;v.play();}};'
             'window.playClipStop=function(id,el){var v=el.querySelector("video");if(v){v.pause();}};</script>')
def clip_card(cid, mock):
    return mock + (f'<video src="clips/{cid}.mp4" poster="clips/{cid}.jpg" preload="metadata" muted playsinline '
                   'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"></video>')
def scr(x, y, w, h, skew=0, op=1):
    return (f'<g transform="translate({x},{y}) skewY({skew})" opacity="{op}"><rect width="{w}" height="{h}" rx="4" fill="{BG2}" stroke="{SP}" stroke-width="1"/>'
            f'<rect x="6" y="6" width="{w*0.4:.0f}" height="5" rx="2" fill="{A}"/><rect x="6" y="16" width="{w-12}" height="3" rx="1.5" fill="{SP}"/>'
            f'<rect x="6" y="23" width="{w*0.7:.0f}" height="3" rx="1.5" fill="{SP}"/></g>')
MOVES = [
    ("m1", "Screen floats in", "A page floats in space, tilted; a light sweeps across it.", "Introducing a tool",
     scr(80, 40, 160, 95, -8) + '<path d="M120 30 L170 30 L120 150 L70 150 Z" fill="#fff" opacity=".08"/>'),
    ("m2", "Fly through the steps", "The camera flies past each step in a row of screens.", "Showing a process",
     scr(30, 70, 70, 45, -6, .5) + scr(115, 55, 90, 58, -6, .75) + scr(215, 35, 95, 65, -6)),
    ("m3", "Cards stack in depth", "Screens sit behind each other; focus moves from back to front.", "Before and after",
     scr(120, 30, 120, 75, 0, .4) + scr(95, 50, 120, 75, 0, .7) + scr(70, 70, 120, 75)),
    ("m4", "Tools on a ring", "Cards circle one center, the one that matters turns to face you.", "How tools connect",
     f'<ellipse cx="160" cy="95" rx="120" ry="34" fill="none" stroke="{SP}" stroke-dasharray="3 4"/>' + scr(40, 70, 50, 32, 0, .6) + scr(230, 70, 50, 32, 0, .6) + scr(125, 85, 70, 45)),
    ("m5", "Push into the screen", "The camera pushes into one card until it fills the frame.", "Going into detail",
     scr(110, 55, 100, 62) + f'<path d="M95 45 h12 M95 45 v12 M225 45 h-12 M225 45 v12 M95 130 h12 M95 130 v-12 M225 130 h-12 M225 130 v-12" stroke="{A}" stroke-width="2"/>'),
    ("m6", "3D title", "A big title flies in, turns and catches a glint.", "Episode or chapter title",
     text(162, 104, 44, "DAY 30", "#000", 900, "middle") + text(160, 100, 44, "DAY 30", A, 900, "middle")),
]
write("motion-pack", {"round": "motion-pack", "stage": "plan", "stepId": "look", "fonts": FONTS, "aspect": "16/9", "layout": "tiles",
    "kind": "library", "keepValues": ["keep"], "keepWord": "move|moves",
    "buttons": [{"value": "keep", "label": "Keep"}, {"value": "no", "label": "Skip"}],
    "title": "Moves for your screens",
    "what": "Six ways to show a screen or an idea, built in your colors. Click a card to play it. Keep the ones that feel like you.",
    "next": "Next: where you sit on screen.",
    "head": CLIP_HEAD,
    "options": [{"id": cid, "name": name, "line": line + " Good for: " + use.lower() + ".", "play": "playClip", "playMs": 6300,
                 "html": clip_card(cid, svg(mock))} for cid, name, line, use, mock in MOVES]})

print("wrote", len(list(OUT.glob("*.json"))), "examples to", OUT)
