# The looks

Nine looks, in three groups. A video uses **2–4 of them**, agreed with the user in the interview (see SKILL.md §2). Every look below says when it fits, when it doesn't, and exactly how to build it.

| Look | Kind in plan.json | Face on screen? | Built by |
|---|---|---|---|
| Full cutaway | `full` | no | clip (engine) |
| Side panel | `panel` | yes | clip, `bg:null` |
| Speaker to side / corner | `pip` | yes, smaller | clip with `speaker:` layer |
| Real screenshots | inside any clip | depends | clip layer with `<img>` |
| Word pop | `pop` | yes | clip, `bg:null`, optional `behind` |
| Text behind speaker | `pop` + `"behind": true` | yes | clip + matte |
| Background blur / dim / colour / image | `plan.base.background` | yes | base.py |
| Zoom-in | `plan.base.zooms` | yes | base.py |
| Captions | `plan.captions` | yes | captions.py |

---

## Graphics that replace or share the frame

### Full cutaway (`kind: full`)
The original motion-broll look: one shape that morphs from state to state, driven by a cursor, filling the frame.
- **Fits:** a process, a product, a comparison, a number, a chapter change. Something to *see*.
- **Doesn't fit:** personal, emotional or opinion lines. The first second of the hook. Anything within 2s of another cutaway.
- **Build:** `reference/engine-api.md`, `examples/opus-aoe2/`, `examples/intro-pip/03-disconnected.html`.
- Length 3–10s. Cutting away from a face costs trust. On personal videos, prefer *speaker to side*.

### Side panel (`kind: panel`)
A transparent clip placed in empty space the edit already leaves (a plain wall, a PiP layout).
- **Fits:** footage with real empty space on one side. Can run 15s+.
- **Doesn't fit:** a speaker who fills the frame (check `contact.png`). Use *speaker to side* instead.
- **Build:** `bg:null`, `center` in the empty area, sized to stay clear of the speaker at every moment. Render to `.mov`.

### Speaker to side / corner (`kind: pip`) — NEW
The speaker's own footage shrinks into a rounded box (side or corner) while a graphic plays on the brand canvas, then grows back to full frame. The clip starts and ends full-frame, so the cuts are invisible.
- **Fits:** personal, intro and trust videos where the face should never leave, while still showing something. The strongest general-purpose look for talking heads.
- **Doesn't fit:** very short beats (<4s): the move itself takes ~0.8s each way.
- **Build:**
  1. Add the clip to plan.json first (`id`, `in`, `out`, `kind: "pip"`).
  2. `python3 $SKILL/scripts/speaker_frames.py motion/plan.json <id>`: JPEG frames of the (treated) footage.
  3. In the clip: `speaker:{src:'../work/frames/<id>/', fps:<video fps>, focus:'auto', start:'full', boxes:{side:[x,y,w,h,r]}, SEQ:[[0.05,'side'],[OUT,'full']], shadow:'…'}`.
     **focus:'auto'** (the default): speaker_frames.py tracks the head in every frame, and the box re-centres on it (head centred
     horizontally, 40% down), so an off-centre speaker ends up centred in the box and stays centred when they move. It never
     exposes an edge of the footage. A fixed `[fx,fy]` is only for when tracking fails. Boxes are screen pixels.
     Put the box on the side of the frame where the speaker already sits (shortest move, least jarring), and the graphic on the other side.
  4. Move the graphic's camera `center` into the free side. Fade the world out at `OUT` (see example).
- Side box at 2560x1440: `[1560,110,900,1220,40]` (right third, tall). Corner box: `[1760,900,720,405,28]`.
- Example: `examples/intro-pip/02-backstory-pip.html`.
- Render cost: the speaker frames make these clips slow (roughly 1 minute of rendering per second of clip at 1440p). Keep them tight.
- Captions default to hidden here. If shown, they sit under both the graphic and the box, so check they don't cross the box edge.

### Real screenshots — NEW
The user's actual screens inside the morphing shape: proof beats a drawn stand-in.
- **Fits:** product demos, "I built this" moments, sales. Ask for screenshots in the interview (`motion/inputs/shots/`).
- **Doesn't fit:** screenshots with private data (customer names, amounts). Ask, blur or crop before using.
- **Build:** a layer holding `<img src="../inputs/shots/x.png" style="position:absolute;left:-W/2px;top:…;width:…;border-radius:…;object-fit:cover">`. Morph the shape to the screenshot's aspect ratio. Use the cursor to point at the one thing that matters, a highlight ring (an `.a` div with an accent outline) on the word it lands on, or a slow push-in (`cam` change) instead of a static hold.
- Example: `examples/intro-pip/07-screenshot.html`.

## Graphics over the speaker

### Word pop (`kind: pop`) — NEW
1–4 of the speaker's own words, big, landing one by one on their word times. Transparent clip.
- **Fits:** the line the viewer should remember. High-energy and social videos: often. Personal and B2B videos: 1–2 per video at most.
- **Doesn't fit:** more than every ~15s. It turns into noise and cheapens the rest.
- **Build:** `bg:null`, hide the shape (`#shape{display:none}`), words in the `world` slot, each word springs in on its time. Display font, heavy. Use the accent colour on one word only.
- Example: `examples/intro-pip/06-life-pop-behind.html`.

### Text behind the speaker (`"behind": true`) — NEW
A word pop placed so it passes behind the speaker's head/shoulders. Needs the matte from base.py (`"matte": true`).
- **Fits:** a single standout moment, often the hook. Once per video.
- **Build:** same as a word pop, positioned to cross behind the head (around forehead height). Add `"behind": true` to the clip in plan.json. composite.py redraws the speaker over it.
- **Hard rule: the speaker may tuck behind part of a word, never hide one.** Every word stays at least 70% visible at every
  moment. A hidden word is pointless. Lay out from `python3 $SKILL/scripts/subject.py box motion/plan.json <in> <out>`: put words
  in `free_left` / `free_right` / `free_above`, and let only the edge of one word, or the gap between words, pass behind the head or shoulder.
- After rendering, **always run** `python3 $SKILL/scripts/subject.py occlusion motion/plan.json <id>`. FAIL = move or resize, re-render, run again. Never deliver a FAIL.
- Check a composite frame, not the beats sheet: beats draws the text on top.

## Treating the footage itself

### Background blur / dim / colour / image — NEW
`plan.base.background`, run by `scripts/base.py`.
- **blur**: shallow depth of field. Hides a messy room and makes the speaker pop. Safe default for home recordings. Amount 0.4–0.7.
- **dim**: darkens (and optionally blurs) the room so brand graphics and captions stand out.
- **color / image**: replaces the room. Edges show more, so check hair and hands. Brand canvas colour is the cleanest.
- It runs across the whole video. It's slow (about 10x the video length on 2 cores), so run it once, early, and run everything else from `base.mp4`.

### Zoom-in — NEW
`plan.base.zooms`: the camera eases in on a key word, holds, and eases out.
- **ease** (default): subtle, for personal/B2B. Scale 1.06–1.12.
- **punch**: instant cut-in, for high-energy videos. Scale 1.15–1.25.
- Place zooms on emphasis words, never during a clip that covers the face. Leave 4s+ between zooms.
- `focus: "auto"` (default): the zoom re-centres on the speaker's head, pulling an off-centre speaker toward the middle as it zooms,
  as far as it can without showing an edge. A bigger scale allows more re-centring: a speaker far off-centre needs ~1.15+.

### Captions
`scripts/captions.py`, burned in last.
- **plain**: white phrases, soft shadow. Personal, B2B, anything professional.
- **highlight**: the spoken word turns the accent colour. Social, high-energy.
- Phrases are hidden during `full` and `pip` clips by default. Set a clip's `"captions": "show"` to keep them, or `"high"` to lift them above a lower-third.
- Always read and fix `captions.json` before writing the ASS file: orphan words, odd capitals, names.
