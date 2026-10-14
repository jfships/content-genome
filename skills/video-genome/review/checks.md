# Checks: four gates

Nothing reaches the creator without passing the gates for its stage. Log every gate in `_review/review-log.md`: date, what was checked, scores, problems found, what changed.

## Gate 1: Plan (before asking for approval)

- [ ] Every run-sheet item filled; nothing left as "TBD" without a reason.
- [ ] Every item is confirmed (taken from their material) or decided on its own page or question, with Main, Backup and Alternatives recorded where there were options.
- [ ] Nothing the creator saw used an internal label (step codes, beat or layout codes, slugs); every decision named its time, line and what it changes.
- [ ] `idea.md` is in the episode folder and the plan matches its promise, angle and format.
- [ ] Story stack: picks within each layer's count, compatibility sentence written, no known clash, not a repeat of the last episode's arc + hook unless the log supports it.
- [ ] Every beat names what delivers the lead personality pick (joke, twist, surprise, real artifact, payoff).
- [ ] The ending has a callback and a shown reason to watch the next video.
- [ ] Every claim traces to Proof; every number is real or labeled illustrative.
- [ ] Moves come only from options the brand's packs kept, or are labeled outside the brand and logged (`craft/brand-fit.md`); none from its No lists or house rules.
- [ ] 2–4 signature moments, at most 1 wildcard, 2–3 break-from-reality spots proposed.
- [ ] Rights: music, images, footage and fonts are the creator's, generated, or licensed for the platform.
- [ ] Disclosure needs listed (synthetic people, voices, events).
- [ ] Paid generation listed with cost from the tool's own price check.

## Gate 2: Build (on stills, before any long render)

- [ ] `npx hyperframes check` passes (with the browser path set; see `setup/gotchas.md`). Expected noise: text-overlap findings on split-character text and deliberate layering; eyeball those in stills.
- [ ] A still of every beat (Playwright for HyperFrames scenes, `beats.js` for engine clips). Fix layout here; stills take seconds, renders take minutes.
- [ ] **Brand check:** `python3 $SKILL/tools/brand_check.py <HyperFrames project or motion/clips> "<brand file>" --pack "<pack name>"` lists every color and font in the build that isn't in that pack. Every hit is fixed or explained.
- [ ] Kit placements match the brand (sting after the hook, series tag timing, end card, corner mark on or off).
- [ ] **Layout:** the 12-point still check in `craft/layout.md` §3 on every scene still. Any "no" is fixed here.
- [ ] Text sizes: ≥ 28 px on 16:9 (key phrases ≈ 76 px, nothing under ≈ 43 px per `craft/layout.md`); ≥ 44 / 34 / 30 px on 9:16.
- [ ] Vertical stills with each platform's safe-zone overlay drawn on; nothing important underneath.
- [ ] Anti-slideshow test (`craft/motion.md` §9) on 5 random stills.

## Gate 3: Render

- [ ] **Debt is zero:** every row in `debt.md` is `done`, `reused` or `cut`; no placeholders left on screen. New reusable assets are filed in `07 Asset Library/` with IDs.

After rendering, check five views:
- [ ] **Contact sheet:** 1 frame every 3 s over the first 30 s, then every 6 s.
- [ ] **Phone view:** the contact sheet at 360 px wide; every word must read.
- [ ] **Strips:** 12 consecutive frames around each big hit and transition, to catch pops, overlaps and sliding.
- [ ] **Audio:** meter every section (`volumedetect`) for silent gaps and clipping; master within ±1 LU of target.
- [ ] **Captions:** compare caption text against `words_out.json`, allowing only the fillers and stutters `captions.py` drops on purpose; names and numbers exact.
- [ ] **Face checks** (footage with overlays): the head never cropped by a zoom or box; `subject.py occlusion` passes on every text-behind clip (a FAIL blocks delivery).
- [ ] **Sync:** video and audio durations match within 0.05 s. For each big hit, compare the SFX onset (from the mix plan, or `ffmpeg -af silencedetect` on the SFX stem) with the frame where the action lands in the strips; within 1 frame.
- [ ] **Deliverables checklist** in `craft/deliverables.md`.

## Gate 4: Scored review (before the creator sees it)

**Self-review first.** Score each 1–10 as a harsh motion director, not a proud author:
1. **Entertaining / personality:** would a stranger keep watching this beat? Every beat has a named reason; the ending isn't a wind-down.
2. **Hook:** striking in 0–2 s, promise shown by 10 s.
3. **Phone readability.**
4. **Motion:** eased, no dead frames, layers present, follows the brand's table.
5. **Variety:** no repeated transition, composition or flat background twice in a row.
6. **Composition:** passes `craft/layout.md`: the graphic fills the open side, one focal point, depth, safe margins, nothing touching frame edges, no empty patch without a job.
7. **Brand accuracy:** palette, fonts, placements, motion language, house rules.
8. **Uniqueness:** passes the "whose channel is this?" and "is this a template?" tests (`craft/uniqueness.md`).
9. **Sound:** hits on beats and on the exact frame, at most ~1 SFX per 3 s, no unintended silence, music carved under voice.

Hunt specifically for:
- text overlapping during swaps
- anything sliding instead of easing
- a dead beat with nothing moving
- the same composition twice in a row
- type touching frame edges
- blurry scaled-up text
- low contrast
- an empty frame at a section start
- a speaker on one side, an empty middle, and a small graphic pushed against the far edge
- a graphic left where the speaker used to be after the shot changed

List the 3 worst problems with timestamps, fix them, re-render only what changed (or recheck stills), and score again. Repeat until every score is 8+. Stop and report if two rounds don't raise the lowest score.

**Then a fresh reviewer.** Start a separate agent that did not build the video. Give it only:
- the render's contact sheet
- the phone view
- the strips
- the transcript
- the brand's personality, packs, motion table and house rules
- the plan's promise (title and hook)

Ask it to score the same 9 points cold and name the 3 worst problems. Where its score is 2+ points below yours, treat its view as right unless you can show it's wrong. Fix, recheck, log both sets of scores.

**Show the creator** the draft with one line of final scores and a draft-review page (`decision-pages.md`), and say plainly that sound was metered, not heard.
