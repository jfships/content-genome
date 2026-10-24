# Checks: four gates

*Long videos. A Short uses `shorts/checks.md` (its gates, timing numbers and technical review).*

Nothing reaches the creator without passing the gates for its stage. Log every gate in `_review/review-log.md`: date, what was checked, faults found, what changed.

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

## Gate 4: Technical review (before the creator sees it)

Taste is the creator's. The builder's own check of the look is the beat brief (`craft/graphic-jobs.md` "Self-check": every beat does its job, nothing only illustrates its line, no device or layout repeats on consecutive beats, every proof reads alone, every device passes the execution bar). No scores: a score of taste from the person who built it, or from an agent reading stills, has never predicted what the creator will say.

**Then the technical review.** Start a separate agent that did not build the video. Give it the render, `words_out.json`, `work/shots.json` (the built video's edit points on the cut's timeline: a JSON list of shot start times or `[start, end]` pairs; not `cutlist.json`, which is source time), the caption file (`captions.py` phrases or `{start,end,text}`), `work/beats.json`, the planned holds, the brand's motion table, vertical rules and house rules, and `tools/tech_review.py`. It returns a pass/fail list, one line per fault with the time, what is wrong and how to fix it, covering:

| Check | Fault |
|---|---|
| Clipped words | A cut, swap or transition lands less than 0.1 s after a word ends or before one starts; a word is cut short at any edit point |
| Last-word cuts | A beat holds more than 0.2 s after the speaker's last word before the next beat (unless the hold is in the beat brief) |
| Captions | A caption's words or times disagree with `words_out.json`; a caption overlaps hook text, a label or the face; a caption outside its box; a line over the chunk limit; the last 10 s transcript diffed against the captions |
| Collisions and boxes | Two elements overlap during a swap; any text or face outside the safe box (vertical) or margins (wide); a speaker or graphic outside the beat brief's box; text touching a frame edge |
| Layout | Consecutive beats share a layout without a planned hold; a graphic left where the speaker used to be |
| Freezes | A frame held longer than 0.4 s where no hold is planned (`ffmpeg freezedetect`); a clip holding its last frame because it was shorter than its slot |
| Durations | A proof on screen under 1.1 s; any single graphic over ~4 s; a title on screen outside the brand's range (default 2–3 s long-form, 1.5–2 s vertical) |
| Pace | Speech outside the brand's pace target after the edit; gaps over the brand's limit (default 1.0 s long-form, 0.6 s vertical) |
| Sound | Voice level and master loudness off target (`craft/sound.md`); music not ducked under voice; levels uneven between speakers; silence where there shouldn't be; an SFX off its frame |
| Render | Black or duplicate frames, flicker on a cutout edge, blurry scaled-up text, low contrast, wrong size or frame rate |
| Brand | `tools/brand_check.py`: colors or fonts outside the pack |
| Linger and endings | A beat holds past its last word into the speaker leaning back, dropping or looking away (check each cut against the body, not only the audio); a word's ending clipped by more than 30 ms at a cut; an angle change that doesn't land on a sentence boundary; also at the end of held moments (the eyes drift) |
| Face and lines | The lower lip below the platform's bottom rows (y 1450 at 1920 tall) on any frame; an overlay touching the face on any frame it is up, its pop-in or slide-in included, not only at rest; a blank or flat-color panel flashing for 1–3 frames at a cut |

**`work/beats.json`** is the beat brief written out by the builder when the brief is locked, one object per beat: `{"id", "start", "end", "layout", "job", "speaker": [x,y,w,h], "graphic": [x,y,w,h], "hook": [x,y,w,h]}` plus flags where they apply: `"hold": true` (the hold is planned), `"proof": true`, `"still": true` (a planned still frame), `"bleed": true` (a full-width band), `"overlap": true` (the graphic is meant to sit over the speaker). Boxes in render pixels. Keep it in step with `plan.md`; it is the file the checks read.

**`work/timeline.json`** (for `draft_checks.py`) is the built clip list: `{"clips": [{"out_start", "out_end", "src_in", "src_out", "source", "said", "angle", "tail_s"}]}`, render times and take times in seconds; `said` is the clip's words, `angle` names the camera or crop, `tail_s` is sound kept past the picture cut on purpose. **`work/overlays.json`**: every text or graphic over the speaker, `{"id", "start", "end", "box": [x,y,w,h] at rest, "scale_from", "in_s"}` (a pop-in from 160 % over 0.3 s is `"scale_from": 1.6, "in_s": 0.3`).

`tools/tech_review.py` runs the measurable rows (clipped and last-word cuts, caption timing, case and centering, uncaptioned speech, boxes and safe box, freezes, durations, pace, levels) and `tools/draft_checks.py` the per-frame ones (lips line, blank flashes, clipped word endings against the take, moves out of delivery, angle changes, overlays vs the face, and one linger sheet per beat end: the last 12 frames + the next clip's first). **Both run on every draft built from real footage, from the first one, not only the final.** The agent looks at every linger sheet (each beat ends while the speaker is still in delivery) and checks the rest by eye on the contact sheet, the strips and the phone view and adds its lines; the agent checks the rest by eye on the contact sheet, the strips and the phone view and adds its lines. Nothing reaches the creator with an open item: fix, re-render only what changed, rerun. Log the list and the rerun in `_review/review-log.md`.

**Fix rounds** (review → fix → recheck, before the creator sees it) cost minutes, not a full render each:
- **Sound only** (levels, an SFX, a sound swap): rebuild the mix from the same clip list and remux it onto the existing picture. No frames are drawn.
- **Picture:** redraw only the time range of each changed beat, padded by 1 s on each side, at the same size and frame rate as the render it patches. Splice the new frames over the old ones and re-encode once. Matting, cutouts and other per-segment work are cached and never redone unless a cut point moved.
- **Redraw everything** only when a change reaches every beat: a global style, the caption system, the cut list, or the frame rate.
- **Recheck what changed:** the review reruns on the changed beats plus the cut on each side, and the whole-video measures that a local change can move (master loudness, sync). It doesn't rerun the full list.
- Build the renderer so it can draw a time range from day one. A range render that matches the full render frame for frame is what makes a patch safe. Check one patched beat against a full render once per project.

**Show the creator** the draft with the review's one-line result ("technical review clean, 2 planned holds") and a draft-review page (`decision-pages.md`): rendered clip cards for beats that move, stills for beats that don't. Say plainly that sound was metered, not heard. Any question of taste goes to them on a rendered clip card, never a still and never a score.
