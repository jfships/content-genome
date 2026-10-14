> **Bundled tool manual.** This is the reference for the talking-head tools that ship with video-genome. The workflow lives in `paths/footage-first.md` (and `paths/graphics-first.md` for cutouts and captions); the Brand Genome replaces the brand step below. `$SKILL` below means this folder, `tools/talking-head/`.


# Talking-head motion

You turn a video of someone talking into a finished edit: motion graphics that land on their words, a treated picture, captions, and thumbnails if wanted. You have **nine looks** (see `reference/looks.md`). **A video uses only the 2–4 that fit its tone, and the user picks them with you.** More looks is not better. The looks the user turns down are as important as the ones they choose.

Built on motion-broll by Barty-Bart (MIT, `LICENSE-motion-broll`). The engine's one-shape, cursor-driven style is kept for graphics.

Below, `$SKILL` = this folder. Work in `motion/` inside the user's project: `motion/{clips,dist,out,work,brand,inputs,models}`.

## 1. Set up (first run)
```bash
bash $SKILL/scripts/setup.sh ./motion
```
It needs Node 18+, Python 3, and ffmpeg (with prores_ks for transparent clips). It installs Playwright + Chromium into `motion/node_modules` and the Python packages (numpy, opencv, mediapipe, fonttools, sherpa-onnx, faster-whisper). Run engine scripts with `NODE_PATH=./motion/node_modules`. On Windows, run everything from Git Bash, which Claude Code uses. If `python3` is missing, use `python`.

## 2. Interview: two short rounds, with AskUserQuestion

**Round 1: inputs** (skip anything already answered):
- **The video.** Copy or link it as `motion/work/source.<ext>`.
- **Brand.** A brand kit (HTML, PDF, image), colours and fonts, or "use the default". Put files in `motion/inputs/`.
- **What it's for.** Where it will be posted and who watches it (a profile intro, a YouTube explainer, a LinkedIn post, an ad). This drives the tone.
- **Proof material.** Real screenshots or screen recordings of what they talk about → `motion/inputs/shots/`. Real numbers they want shown.
- **Extras.** Captions? Thumbnails? Final size (e.g. 1080p for upload)?

Then do §3 (inspect + transcribe) **before** round 2, so your proposal is based on the actual footage and words.

**Round 2: direction.** This is decided *with* the user, never by you alone. Propose, with one line of reasoning each:
- **Tone** you read from the footage, the words and the purpose: personal/trust, explainer/demo, high-energy social, sales/B2B, or a mix.
- **2–4 looks** for that tone, from the guide below, plus which looks you'd deliberately *not* use and why.
- **Density**: light (2–4 moments/min), medium (4–7), heavy (most lines).
- **Caption style** (plain / word-highlight / none) and **canvas** (light or dark, matched to the footage).

Ask them to confirm or change each (AskUserQuestion, multiSelect for looks). Their answer is the brief. Don't add looks outside it without asking.

### Tone → looks guide (a starting point for your proposal, not a rule)
| Tone | Lean on | Use sparingly | Usually skip |
|---|---|---|---|
| Personal / intro / trust | speaker to side, plain captions, background blur, 2–3 gentle zoom-ins | 1 word pop, 1 full cutaway for proof | highlight captions, punch zooms, heavy density |
| Explainer / product demo | full cutaways, real screenshots, panels | zoom-ins, word pops | text behind speaker |
| High-energy social | punch zoom-ins, word pops, highlight captions, text behind speaker (hook) | cutaways | long panels, slow morphs |
| Sales / B2B | real screenshots, one proof cutaway, plain captions | speaker to side | word pops, punch zooms, text behind speaker |

## 3. Inspect and transcribe
```bash
python3 $SKILL/scripts/inspect_video.py motion/work/source.mp4 motion/work        # contact.png + video.json (res, fps, layout)
python3 $SKILL/scripts/transcribe.py motion/work/source.mp4 motion/work             # words.json / words.txt / transcript.srt
```
- Look at `contact.png` yourself: where the face sits (for `focus`), whether there's empty space (panels) or the speaker fills the frame (use speaker-to-side instead), and whether the footage is light or dark.
- The transcript uses faster-whisper, with Parakeet (downloaded from GitHub) as the fallback when Hugging Face is blocked. Word times are real, ±0.05s. If the user supplies an SRT instead, `scripts/words.py` estimates word times (±0.2s).
- Read the transcript. Flag misheard words and ask about any you're unsure of. Never "correct" what they actually said without asking.

**Brand:** see `reference/brand.md`. For an HTML kit: `node $SKILL/scripts/brand_from_html.js kit.html motion/brand`, then write `motion/brand/brand.json`.

## 4. Plan: get approval before any code
One row per moment:

| # | In–Out | Line it covers | Look | What happens, on which words | Why this look |

Rules carried from motion-broll, which still hold:
- Show the subject's real objects, taken from the words. Map each idea to the interaction vocabulary in `reference/engine-api.md`.
- **Never invent numbers, quotes, prices or results.** Use relative bars, skeleton lines and labels taken from the transcript. List what's illustrative.
- One idea per clip. Pace to speech: one change per spoken beat (0.4–1.2s).
- ≥2s of plain face between moments that cover or move the face. Nothing in the first second of the hook.
Also list the base treatment (background mode, zoom words), caption style and thumbnail ideas. Wait for approval or edits.

## 5. Build
Order matters, because later steps use earlier outputs:
1. **Base** (only if background or zoom looks were chosen): fill `plan.base`, run `python3 $SKILL/scripts/base.py motion/plan.json`, and set `"base_video": "work/base.mp4"` (and `"matte"`). It's slow, so start it first and write clips while it runs.
2. **Clips**: `motion/clips/NN-name.html`, following `reference/engine-api.md`, `reference/looks.md` and the examples (`examples/intro-pip/` shows every new look, `examples/opus-aoe2/` the original style). Speaker-to-side clips need `scripts/speaker_frames.py` first, which runs after base.
   `python3 $SKILL/engine/build.py motion/dist motion/clips/*.html` picks up `motion/brand/brand.json` automatically.
3. **Check stills** on the key words (for text behind the speaker, also run `subject.py occlusion` after rendering): `node $SKILL/engine/beats.js motion/dist/NN.html motion/work/NN.png 0.4 1.2 …`. For transparent clips, add `BEATS_BG=motion/work/still.png` to see them over the footage. Look at every sheet. Fix anything cramped, clipped, unreadable, off-word or cursor-out-of-frame, then check again.
4. **Render**: `node $SKILL/engine/render.js motion/dist/NN.html motion/out/NN-name_0m32s40.mp4 <fps>`. Match the video's fps and resolution. Transparent clips (`bg:null`) go to `.mov`. Slower than real time, so run two in parallel on multi-core machines.
5. **Captions** (if chosen): `captions.py phrases`, then read and fix `work/captions.json`, then `captions.py ass … --style plain|highlight`. Set `"captions": "work/captions.ass"` in plan.json.

## 6. Composite and deliver
```bash
python3 $SKILL/scripts/composite.py motion/plan.json motion/out/preview.mp4 --deliver motion/out/final-1080p.mp4 --size 1920x1080 --fps 30
python3 $SKILL/scripts/make_pages.py motion/plan.json motion/out/preview.mp4
```
- **Say plainly which file is the finished video** (`final-1080p.mp4`, or `preview.mp4` at full res). The individual clips are only for re-editing, and people mistake them for the deliverable.
- Name the finished file after the person and the purpose (e.g. `sam-intro.mp4`). Keep it under the size limits of wherever it's going.
- Also delivered: `TIMING.md`, `viewer.html`, `compare.html`. Background, zooms, text behind the speaker and captions exist only in the composite.
- Transparent clips: also export a small `.webm` with alpha for CapCut/DaVinci (`ffmpeg -i x.mov -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 30 x.webm`).

## 7. Thumbnails (if asked)
Pick 1–3 stills where the speaker looks good (mouth closed or smiling, eyes to camera), then write `motion/thumbs.json` and run `node $SKILL/scripts/thumbs.js motion/thumbs.json`. Layouts: `headline` (hook + accent line), `card` (headline + proof checklist), `name` (name + roles). Offer 2–3 options with a recommendation. Headlines use the video's own claims, 2–6 words, readable on a phone.

## Two hard rules for anything that moves or covers the speaker
- **Re-centre on the subject, not the frame.** Zoom-ins and speaker boxes follow the tracked head (`focus:"auto"`, the default), so an off-centre speaker is centred when the framing changes. Check it in the stills: if a box or zoom crops the head or leaves the speaker off-centre, fix it before rendering.
- **Never fully hide copy behind the speaker.** Words placed behind the speaker must stay ≥70% visible. Lay out with `scripts/subject.py box` and verify with `scripts/subject.py occlusion` after rendering. A FAIL blocks delivery.

## Style defaults (the brand and the agreed looks override these)
- Motion: springs with a tiny overshoot at most. Leading and trailing edges ride different springs. The camera zooms so each state fills the frame.
- One accent colour doing one job. One icon set, one stroke weight (`M.icon`).
- Banned: bouncy easing, particles, glows, gradients on UI chrome, mixed icon strokes, dead time, template looks, made-up data, and effects stacked because they're available.

## Gotchas
- No `will-change` on anything the camera scales, or the text blurs.
- Swapping text inside a morphing container needs `M.vis` din/lin/lout, or old and new overlap.
- Keep the cursor in frame at every zoom.
- Word times from an SRT drift. From `transcribe.py` they're good, but still put key changes on stressed words.
- A speaker-to-side clip must start and end on the `full` box, or the cut shows.
- The high-res footage stills sheet needs the viewport sized to the stage (already fixed in `beats.js`).
- If Playwright's browser download is blocked but a browser is preinstalled, pin the playwright version that matches it (e.g. `playwright@1.56.1` for chromium-1194).
- base.py processes the whole video. For quick tests, trim a section first and shift the plan times.
