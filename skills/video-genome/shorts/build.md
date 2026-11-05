# Building a Short

Everything here is 1080×1920 from the first frame of the first draft. Nothing starts as a 16:9 timeline.

## Direction pages (S2b, before the first rough build)

A rough draft built before the creator has chosen a look gets judged on the look and wastes the round. So two pages come first, built from real material (the subject's films, pages and shots; a code-drawn mock only where nothing exists yet, labeled as a mock):
1. **The world:** whose visuals fill the frame (the subject's own films, ads or footage; product or object shots in space; the creator's own set). Two or three options.
2. **How the creator and the source share the frame:** full bleed with the creator over it, split top and bottom, or cutting between them. Two or three options.

Before anything is filmed, each option is a 1080×1920 still with the safe box drawn on, two stills per option (the hook frame and one mid beat); Main and Backup picked and saved in `plan.md`. Once real takes exist, both decisions are rows on the Short's live picker instead, playing on the takes, one pick each. Only then build the rough draft.

## Beat brief (S2c, after the direction pick, before the first rough build)

The direction pages settle the world and the frame. The beat brief settles every beat, and it is the builder's creative work, not the creator's: done on the creative tier (SKILL.md, "Which model for which part"), written into `plan.md`, one row per beat:

| # | In–Out | Line | Job | Device (source) | Layout + speaker box | Graphic box | Size | Enter / exit | Hold | Why this, not the two alternates |

- **Job:** straight man · unsaid line · exaggeration · proof · breather (`craft/graphic-jobs.md`). "Illustrates the line" is not a job.
- **Device (source):** *their material* · *stock <id>* (a sample from the stock library, `craft/stock.md`) · *kept* (the brand's lists) · *new* (designed for this line in brand limits, `craft/brand-fit.md`) · *generated* (image or clip, brand image rules). List candidates from every source before picking; "used last time" and "first in the list" are not reasons.
- **Layout:** one of the named layouts below, with the speaker's box; consecutive beats never share a layout unless the hold is the joke.
- **Why:** 2–3 treatments per beat, ranked, with why the builder's pick beat the others. Once the creator's takes or a first edit exist, each beat that gets a treatment is a row on the Short's live picker (**Beats** tab, `../decision-pages.md` "The live picker"), its treatments playing on that beat; one pick per row. Captions are picked once on the **Look** tab; when a beat's on-screen text is up, captions hide.
- Every moving graphic is proved as a rendered 2–4 s clip of that beat before the rough draft.
- Gate: every beat has a job, a source, a reason and a layout, and the `craft/graphic-jobs.md` self-check passes.

**Source visuals.** For a Short about a company, product or person, look for that subject's own films, ads, talks and footage first (official channels), and gather far more frames than the Short needs so the creator can choose. A screenshot of a web page is only for when the page itself is the point (an out-of-stock label, a price). Note every source in `plan/asset-debt.md`; check reuse rights as in `review/checks.md` gate 1. If downloads are blocked, see `setup/gotchas.md` "Frames from the web".

## Rough draft (S3, optional, before recording)

Optional. Build it only when the creator wants to judge the shape, a gag or a layout by watching before filming; a talking Short goes straight to recording, and the live picker (S5b) shows the choices on the real takes instead.
- Build it 9:16 in HyperFrames at draft quality, at the planned length, with the shape's beats on the planned times.
- Voice: the creator's recorded lines wherever they exist; a free temp voice (`setup/tools.md` §3b) for every line not yet recorded, at the brand's target pace ("Spoken pace" below), so the creator can judge the whole Short. Tag each temp stretch "temp voice" on screen. Never leave a line out or wait on a recording.
- On screen: the hook text from frame 1, captions in the brand's style, the layout, the backdrop, placeholders for what isn't shot yet.
- Show it with the script beside it. The creator says what changes; the plan is updated before recording.
- Building over budget on length is fine; cuts are made after watching.

## Recording (S4)

Shoot for the tall frame:
- **Native vertical** (phone upright) by default. Or **4K horizontal framed for a center crop** (the center 1215×2160 becomes 1080×1920). A 1080p horizontal crop is too soft for a full-frame face; use it only for a small inset.
- **Framing:** chest-up, head in the top 30–40% of the frame, eyes near the upper third line (y≈640), centered. Same distance, light and backdrop as the brand's vertical setup.
- **Record the hook fresh,** 3–6 ways, Main and Backup first. Then the lines, each new thought opening with its own hook sentence.
- **Delivery:** at the brand's pace (default 2.6–3 words a second after the edit), eyes on the lens, one idea. Energy comes from the writing and the cut, not from shouting. A deadpan read lands on a tight cut.
- Write `RECORDING.md` in plain words (setup, framing, the exact words that must be said: names, numbers, the hook, the last line). For words on screen while recording, use a prompter skill if one is installed (recording-prompter builds its page from the locked script card, one spoken slate per take, opened locally); never hand-build a one-off cue page.

## Take Check (S4b, before the cut)

Before anything is transcribed or cut, the creator screens the takes on `tools/take-check.html` (copy it into the video's `_review/`; it runs in the browser on their computer, nothing is uploaded). It splits each recording into takes at the pauses; they mark each take Keep, Maybe or Drop, optionally tag the script line, and write a comment in the box under the player.
- **Proposed marks:** the builder may pre-mark takes. Write `_review/take-check-proposed.json` (`{"script": [lines], "beats": [{"line", "text", "picture"}], "takes": [{"file", "start", "end", "mark", "line", "note"}]}`, `picture` a path relative to the page, e.g. a still of the beat) and the creator loads it with "Load proposed marks" (or drops it on the page). Proposed takes keep the builder's start and end; the creator's own marks always win. The beat's picture shows beside each take tagged with its line.
- Marks are stored per copy of the page (per video); one video's marks never show up in another's.
- The split follows the room level through the recording, and the summary lists any stretch over 20 s with no takes ("NO TAKES FOUND"): play those before saving, in case a whole pass was missed.
- Only Keep and Maybe takes go forward. The page's summary (file + start/end per kept take, lines still missing a keeper) is the input to the cut; save it as `_review/take-check.txt` (Copy summary or Save picks file).
- A line with no keeper goes back to recording before the cut, not after the draft.
- The builder may rank Maybes against each other on eyes, face and words (step 0 below); it never overrules a Drop.

## Acting takes with no spoken words (S4c)

When the creator acts silently against a voice track (a narrator, a clip), takes have no words to split or cut on.
1. **Record against playback:** the voice track plays out loud in the room (a prompter skill's clip mode), so each take's own audio carries the voice and can be lined up by sound. Never record acting in silence.
2. **Split one file per take** on the creator's markers (spoken beat line, "take N", "moving on") and the playback audio. Never merge two takes; when pauses are short, split finer on the markers.
3. **Line up each take** by matching its room audio to the voice track (cross-correlation); write the offset per take. Measure the reaction lag (move start minus the trigger word's onset) and write it too.
4. **Weed out** takes that can't work (wrong beat, out of frame, mouth moving), listed with times so the creator can overrule.
5. **Take Check card per take:** beat and take number, trimmed to the take, the beat's picture and voice line beside it, Keep / Maybe / Drop and a comment.
6. **Cut each kept take at the start of the move,** not the blink or reset before it; the move lands on its trigger word (measured onset, `tools/onsets.py`). Show 2–3 candidate windows per beat on a 0.1 s contact sheet before choosing.

## Cut (S5)

**Draft quality, asked again.** When the first draft built from real takes starts, and on any resumed session, ask the draft quality again with the measured time, and recommend the input's own frame rate: lip sync, eye contact and cut timing can't be judged at 15 fps. HyperFrames always draws at the composition size, so offer frame rate (and a smaller composition), not sizes it can't do (`plan/intake.md` "Draft quality").

0. **Screen every take on words, eyes, face and framing.** Never rank takes by audio alone and never assume a line stays voice-only: edits change and any line can end up on camera. Cut every take with picture at full quality.
1. Transcribe the finalists from Take Check (`tools/talking-head/scripts/transcribe.py`), pick among them, cut frame-accurate (`paths/graphics-first.md` A3 "The cut" method). Save `cutlist.json`, run `tools/remap_words.py`.
2. **Trim dead air first:** cut every gap over about 0.4–0.5 s, and cut 0.1–0.2 s into the end of each line. Breaths go.
3. **Then bring the speech to the target pace** ("Spoken pace" below): measure it, and speed up only by the gap between what was said and the target. Never speed up instead of trimming.
4. Measure the cut with `tools/short_timing.py` (`checks.md`) before building graphics on it.
5. **Inserting audio before a take:** split the take's picture and voice. The picture can hold or slow; the voice is placed by its word times. Never start a take's media earlier than its first-word lead allows, or its own audio plays under the insert.
6. **Take files:** keep proxies shallow (small copies of the takes in one shallow folder such as `work/takes/`; deep folder trees can fail when files are copied between computers) and convert only the candidate segments listed from the transcript. Phone 4K HEVC decodes slower than real time on many laptops.
7. **Footage clips** (a source ad, a screen recording) are their own top-level clips in the composition, placed by CSS; the scene section holds only graphics (a video inside a timed section fails lint).

### Clip timing (every build; stutter and sync)

Two rules for every video clip in a HyperFrames composition, found on a Short whose speaker stuttered 10 times a second:
- **Start half a frame in.** `data-media-start` = the clip's in point + 0.5/fps (0.0167 at 30 fps). WebM stores frame times in whole milliseconds (frame 17 at 30 fps is stamped 0.567 s, asked for at 0.5667 s), so a clip started on a whole frame shows every third frame twice and skips the next. Measured on composition stills: 10 repeats and 9 skips a second at a whole-frame start, none at half a frame.
- **First kept frame at its true time.** When a take segment is cut to its own file, seek one take frame early and place every kept frame at its true time; ffmpeg otherwise pulls the first kept frame to 0 and the picture runs up to a frame ahead of the voice. `tools/cut_segment.py` does both and prints the attributes to paste (measured: picture -0.39 frame against the voice with a plain cut, -0.06 with it).
- **Starts and lengths on the frame grid, rounded down:** `data-start` = frame/fps written down to 4 decimals; the composition's `data-duration` = frames/fps rounded down. Rounding the length up by even 0.0001 s renders one extra frame (2.0001 s at 30 fps rendered 61 frames). Overlays that end on a cut end half a frame early.
- **Build scripts never run on import.** All work sits under `if __name__ == "__main__":`; a checker that imported a build script once restarted a 35-minute build. Checks read the build's output files, never import the build.

### Speed-ups

A speed-up is 10% at most (1.10×). Voice: `tools/voice_stretch.py` (Rubber Band's finer engine; ffmpeg's `rubberband`/`atempo` use the older engine, which squeezed a voice at 1.18–1.25×); picture: `setpts=PTS/<speed>` with frames at true time (`cut_segment.py --speed`). Over 1.10×: re-record the line faster, or A/B both versions by ear with the creator first (`voice_stretch.py --ab`). A sped-up line drops one take frame every ~1/(speed−1) frames; that's expected, and `frame_map.py` only flags drops beyond it.

## Live preview (S5d, before any video file is sent)

The creator watches each draft live instead of waiting for a render.
- **Every draft, from the first, is built in `hf/`** (the video folder's HyperFrames project), so every edit reloads in the preview in about 5 s. No draft is composited outside HyperFrames.
- **Drafts are never rendered.** Every check on a draft runs on the composition itself: the glitch gate below, stills from `tools/comp_stills.py`, and `tools/tech_review.py` on `work/beats.json` (`checks.md` gate 2). The only render is the final (S6); `draft_checks.py` and the render half of `tech_review.py` run on it.
- **Glitch gate before the link** (below). The link goes to the creator when it passes; the message lists any accepted flags and any leftovers in one line each.
- **Launcher:** copy `tools/preview.bat` into the video folder as `preview.bat` and fill `{{VIDEO}}` and `{{VERSION}}` (the HyperFrames version written in the log at setup, `setup/tools.md` §2; never `latest`). It starts the preview in the background, prints the Studio link, and stops it when the creator presses a key in its window. Without Windows: `cd hf && npx hyperframes@<version> preview`, and `--stop` when done. Give the creator the launcher, or the preview link it prints; never send a render first.
- The creator calls tweaks in chat while watching. A tweak that is a value (timing, size, position, a color inside the brand) is edited in `hf/` and they watch it reload. A moment that needs new ideas is a new picker round for that row only (`picker/README.md`, branched page).
- Renders are for the final only, never for checks or for showing combinations.
- Gate: the creator says the edit is right. Then the final (S6).

## Glitch gate (every draft, before the creator sees it)

```
python3 $SKILL/tools/glitch_gate.py hf --out _review/gate-r<N> --timeline work/timeline.json --root . \
  --marks work/marks.json --target <brand LUFS, default -14> [--bed <bed file>] [--flicker]
```
It runs on the composition, no render (stills around every cut and a frame-by-frame read of what is on screen), and prints a pass/fail list with times: 1-frame pops, black or flat frames, a doubled first frame, near-identical jump cuts and the head-jump number at every cut, moves that change speed at a seam, lips under the line, marks showing early or late, holds short of plan, hard entrances, pictures shifting position, text blocks breaking the one-size rule, clips not started half a frame in, files shorter than their slot, a length that renders one frame long, mix loudness, peaks and clipping, a music bed that stops before the end, lip-sync drift, rewinds and dropped frames on sped-up lines (`--timeline`), and cutout edge flicker (`--flicker`). A strip of 9 frames before and after each cut lands in `<out>/strips/` with the head-jump number on it.
- `work/marks.json`: every graphic keyed to a word, `[{"id": "<element id>", "at": <measured onset, s>, "hold": <planned s>}]` (onsets from `tools/onsets.py`).
- **Known false positives** go in `_review/accepted-flags.json` as `[{"key": "<key printed after the FIX>", "why": "<reason>"}]` (one list per video, kept across rounds) so they stop coming back; never accept a real fault to get a pass.
- **On a fail, the builder fixes and reruns, up to 2 tries.** Still failing after the second try: the draft goes to the creator anyway, with each leftover named in plain words (time, what is wrong, what was tried). No extra review loop.
- `--quick` re-checks one change in seconds (3 frames each side, no full scan); the last run before the link is a full one.

## Pace

Pace is two numbers the brand sets: how long each shot stays, and how fast the speech runs. Both live in the Brand Genome's vertical motion row; the defaults below apply when there's no Genome or it's silent.

### Cut length by what the shot is doing

One range for every shot ("a change every 3–5 s") makes a slow Short. Each shot gets the length its job needs, and nothing longer:

| Shot | Length | How |
|---|---|---|
| Hook | face and spoken line on frame 1; first change by about 1.5 s | the first frame makes sense with no sound |
| Talking line (creator to camera) | ends with the last word; usually 1–2.5 s | cut 0.1–0.2 s into the end; no tail. A line longer than the ceiling is split by a punch-in, a cutaway or a proof shot |
| Proof to read (a quote, a price, a page, terms, a post) | reading time: about 0.3 s a word + 0.5 s, at least 1.1 s | one piece of proof at a time; a long quote is cut down, split, or highlighted as it's said |
| Reaction, cutaway, product shot | 0.5–1.5 s | |
| Deadpan hold | up to 1.5 s, one per punchline | it's the joke, not dead air |
| Last line | ends on the payoff; 1 s or less after it | |

- **Ceiling:** no shot runs past the brand's ceiling (default about 2.5 s) unless it's reading time or the planned hold. It's a soft rule, judged by watching, but every shot over it needs a reason in `log.md`.
- **Average:** about 1.5–2 s a shot across the Short for fast or comedic brands, 2–3 s for calm ones.
- Cut the moment the last word ends; when the picture leaves the speaker, the next beat starts on that frame.
- A punch-in ("Transitions and camera in 9:16") counts as a new shot; use it on the hook and the punchlines and to hide jump cuts.
- No single visual (one graphic, one screen) longer than about 4 s, even with motion inside it.

### Spoken pace

The target is a pace, in words a second after the edit, never a fixed speed-up. The creator's natural pace changes as they improve, so the speed-up shrinks to nothing on its own.
- **Default target 2.6–3 words a second** (the brand's number wins). Longest silence 0.6 s or less unless it's the planned hold.
- Order: trim gaps first, then measure (`tools/short_timing.py`, which prints the speed-up needed). Already at the target: no speed-up. Below it: speed up just enough to reach the low end, 10% at most ("Speed-ups" above). Still slow at 10%: re-record that line faster.
- Per line is fine: a line that drags gets its own speed; a deadpan line may stay slower on purpose.
- Speed-up blunts deadpan and makes voices sound squeezed past about 10%; judge by watching. Write the measured pace and any speed in `log.md`.

### Structure

- First payoff (laugh, twist, result) by 3 s; aim for the hook itself to be it.
- Call-and-response: 4 exchanges or fewer, each one escalating. Cutting back and forth more than that is the most common way a Short goes slow.
- The long-form energy arc (build-up, climax two-thirds in) doesn't apply. The Short peaks at the hook and again at the last line.

## Layouts

Coordinates at 1080×1920 (`craft/layout.md` §1, Shorts and Reels). **Safe box** for anything important: x 65–930, y 210–1500. The right rail (x > 930) is covered by buttons from about y 900 down; the bottom ~420 px by the caption, handle and audio rows; the top ~210 px by the platform's top bar (Reels top UI, checked 2026-05; Meta's 270 is for ads; recheck yearly).

Every beat names one of these layouts in the beat brief. Two consecutive beats never share one unless the hold is the joke; one layout for a whole Short is a fail. Boxes are the defaults; a beat may move them, inside the safe box, by writing the new box in its row's "Layout + speaker box" / "Graphic box" cells.

The stock id after each name is its sample in the stock library (`craft/stock.md`).

| Layout | Speaker | Graphic | Use when |
|---|---|---|---|
| **Full frame** (LAY-01) | Chest-up, centered, eyes at y≈640 (head in the top 30–40%) | None, or hook text y 210–520 | Breathers, the hook, a punchline hold |
| **Punch-in** (CAM-01, CAM-02) | Full frame scaled 1.15–1.4×, eyes stay ≈ y 640; may shift off-centre to make room | A word or label in the space opened up | Key lines, hiding a jump cut, a reaction |
| **Split top** (LAY-02) | Cutout or crop in the lower band, eyes at ≈ 60% of frame height (y≈1150), centered | 16:9 band at x 0–1080, y 210–818 (their footage, a screen) | Straight man and proof beats where their material and the reaction are seen together |
| **Half and half** (LAY-03) | Bottom half (y 960–1920), lifted until the mouth sits above y 1500 on every frame (about 50 px on a chest-up take; measure, `draft_checks.py`) | Top half, 1080×960; anything read inside x 65–930, y 210–930. The picture moves (a still card fails); each picture holds ≥ 1 s so it can be read | A picture beat that is as important as the speaker: proof, their footage, a generated scene |
| **Over their page** (LAY-04) | Cutout at about 0.64 of its full-frame size, bottom-left (about x 40–620, y 850–1450), feathered edge, never over the subject of the shot, never in x > 930 | Their page, post or shot full-bleed behind | Reading or reacting to a page, a post, a quote |
| **Full graphic** (LAY-05) | Off screen, 1.1–4 s at most | The whole safe box | Proof that must be read alone; a gag; the unsaid line as a scene |
| **Words behind** (LAY-06) | Full frame or punch-in | Big words layered between the backdrop and the cutout, beside the head, ≥ 70% visible | One standout line, the hook, a reveal |
| **Floating card** (LAY-07) | Full frame | A card, notification or object in the open space at head height, on the side the speaker faces | The unsaid line, an interruption, a small proof |
| **Corner bubble** (LAY-08) | Round face bubble about 320 px across, lower-left (about x 65–385, y 1150–1470), never in x > 930 | The screen fills the safe box; the bubble never covers the part being pointed at | A screen beat where the screen is the subject and the speaker reacts or explains |
| **Lights out** (CAM-04) | Full frame or punch-in, still lit | The backdrop drops to near black on the trigger word; at most one word or prop in the dark space; back on the next beat | The serious line, a turn, the moment before a reveal |
| **Cutout over a scene** | Cutout at one head size across beats (±5%), body running off the bottom edge, never over the scene's figures or focal object | A full-frame generated or illustrated scene with the space for him planned when it's made (the bottom, or a named corner) | Mock documentary (`shapes.md`), a "you in this world" gag |

- **Cutout over a scene:** soft edge fade only where the source frame ends; a contact shadow on the scene's ground line. Placement in a prompt is unreliable, so plan the empty space by generation or crop, then check it on the still.
- **Backdrop** built tall (the brand's tall backdrop), never a crop of the 16:9 plate. Cutouts sit on it at the framing above.
- **Graphics keyed to a word** start on its measured onset, not Whisper's time: `tools/onsets.py <take> words.json words_onsets.json --words "<anchor words>"`, then `remap_words.py` onto the cut. Words it marks `rise` (connected speech) get one listen at the anchor.
- **Hook text** y ~210–520, above the face, on screen from frame 1 for at least 2 s, never colliding with captions or the face. **Place it from the face, not a fixed y:** measure the top of the head on the frames it's up and keep the text's largest box (its pop-in scale included) clear of it; a pop-in from 1.6× that clears at rest can still cover the chin or beard for 4 frames. List it in `work/overlays.json`.

**Safe zones on every layout or split change.** Before building any layout change or a requested split (55/45, a lower band, a bigger speaker), measure the mouth and chin on the real frames of that layout against the bottom line (y 1500): run `tools/draft_checks.py` on a short test render, or measure the face on 3–5 frames of the take at the new scale and offset. If the request breaks the line, say so before building, with the measured numbers and a safe alternative ("at 55/45 your mouth sits at y 1540, under the caption rows; 50/50 lifted 50 px keeps it at 1480"). Fix with the smallest change that clears it, measured, not guessed: a 170 px lift overcorrects where 50 px was right. Re-measure per frame on the draft, since the speaker moves.
- **Text sizes** at least 44 / 34 / 30 px (headline / body / label); overlays stay at least 2 s.
- **One size per text block.** A title or hook block of several lines uses one font size and one fixed line height in px; emphasis is color only (never a bigger line, never fitting each line to the width). On a text-only still, every line's letter height and every gap between lines match within 2 px. Give the block `class="hook"` / `class="title"` (or `data-text-block`) so the glitch gate checks sizes, line heights and line gaps.
- **Words behind the speaker** (LAY-06): use the bundled talking-head tools first (`tools/talking-head/`, the text-behind look in `reference/looks.md`, `subject.py occlusion`); hand-build only what they can't do.
- Graphics follow the rest of `craft/layout.md` (lead room, one focal point, nothing touching edges) re-decided per scene; the beat brief's boxes are checked on stills and by `tools/tech_review.py` before any render.

## Captions

- **Style comes from the brand's caption spec** (`vertical.md` or `look.md` "Caption spec": case, font and weight, size, plate, lines, box and centering, key word). Stock samples: CAP-01..06.
- **No spec, no captions.** If a field is missing (the case most of all), ask the creator in one question box before building any caption, sentence case recommended, and write the answer back into the spec. The hook's style and Title Case are never the fallback.
- **Chunks:** 2–3 words, one line (two at most), one key word per phrase in the brand's accent.
- **Every spoken beat is captioned** unless the beat brief gives a reason (`"captions_off": "<why>"` in `work/beats.json`, e.g. the line is already on screen as big type). When a beat's own on-screen text is up, captions hide.
- **Placement is decided per beat:** the best free spot on that beat's layout, clear of the face, the graphic's box, the top 210 px, the bottom zone (y > 1500) and the right-side buttons (x > 930 from y 900 down). Write it in the beat's row as a caption box.
  - Default spot: centered around y 1150–1400, below the chin.
  - Split top and half and half: on the seam between the picture and the speaker (y ≈ 860 and ≈ 960), clear of the head. Over their page and corner bubble: up or right of the cutout, clear of the part of the page being read.
- **Moving between beats** is right when another spot is clearly freer or reads better; a caption never moves within one line. A line-by-line caption (one sentence shown across several chunks) stays in one spot until the sentence ends.

## Brand-kit pieces

- No sting, no sound logo, no end card, no name tag on a Short.
- A series tag only as "Part N", folded into the hook text or small after the hook; never before or competing with it.
- Corner mark off unless the brand turns it on for vertical.

## Graphics and motion

Graphic beats cost the most draft rounds. Build them with this loop; it held quality at a fraction of the build cost.

**Read before planning any graphic beat,** and list what was read at the top of the plan:
- `craft/graphic-jobs.md` (the beat's job) and `craft/stock.md` (picking by id, restyling)
- `craft/spatial/README.md`, with its "Tall frame" boxes
- the brand's swipe library "Visual devices" and style ledger (what the creator saved, kept and dropped)
- the brand's rendered 3D packs in `07 Asset Library/graphics/`: watch them and port from their sources

**The loop, every round that has graphic beats:**
1. **Plan** (build tier): a short graphics plan in `work/GRAPHICS-PLAN.md`, one row per beat: time, the line, the stock id or saved source file it ports from, what appears on which word, its boxes; plus what must not change. Each later round's plan lists only the changes from the last one.
2. **Build to stills** (mechanical tier): port each beat from its named source into `hf/` (a comment on each beat names the file it came from), take stills at the plan's check times (`hyperframes snapshot --at`), and stop. No taste calls, no renders, no paid calls.
3. **Check the stills against the plan:** whoever wrote the plan reads them row by row. A still that misses gets one rebuild; a second miss sends the plan back.
4. **Measured checks, then the live preview** (S5d). The creator judges in motion, never from stills alone.

**Rules for every graphic beat**
- **Pick by stock id** from the manifest (`craft/stock.md`): 2–3 candidates per beat from the beat's job, the picked one written in the beat brief. Restyle by swapping the brand file, never by redrawing the sample.
- **The first take is never the plain card.** A flat card with the line typed on it is a breather at most, and only when the beat brief says so. A first take is a look-real prop (`craft/graphics-library.md` §15), a move in space, or the subject's real material.
- **Tall frame:** a 16:9 source is re-framed, never squeezed: port its tween numbers (depth, rotation, ease, duration), not its pixel layout, into the boxes in `craft/spatial/README.md` "Tall frame".
- Build in HyperFrames at 1080×1920 (or the bundled engine over the cut, `tools/talking-head/`), restyled from the brand's vertical motion row.
- **Re-plan, don't keep fixing.** When draft 3 isn't approved, or one beat is rejected twice, stop fixing that beat. Re-plan it as a picker row of 2–3 stock samples the creator hasn't rejected for it, or switch its build type. Two more rounds after the re-plan; then the creator decides: ship, park or rebuild.
- Any device built new for this video joins the stock library at close-out (`craft/stock.md` "New builds become stock").

## Transitions and camera in 9:16

Shots in a Short last 1–2.5 s, so a transition's time comes out of the shot it sits in.
- **Hard cut** for nearly every change (TRN-01): on the new idea's first word, or the moment the last word ends (CUT-01).
- **Cut on the eye trace:** put the incoming shot's focal point (the face, the word, the object) where the viewer's eye already is at the end of the outgoing shot, or where it is moving to. A cut that makes the eye jump across the frame reads as a glitch.
- **Jump cuts inside one take:** punch in 10–15% (1.10–1.15×) on the incoming side, or cut away. Two shots at the same size with the head a little off reads as a glitch (the glitch gate flags it with the head-jump number); a punch-in of the brand's bigger scale (below) is for key lines.
- **Read well tall,** at about 0.4 s or less: match cut on shape or motion (TRN-02), whip between screens (TRN-03), an object passing the lens (TRN-04), a color sweep (TRN-06), zoom-through into a screen (SPA-07).
- **Too slow for most Shorts:** dissolve (TRN-08) and soft rise (TRN-09); keep them for a planned mood change. Strips, page tear, film burn and the like are wildcards: one per Short at most.
- Never the same transition twice in a row.
- **Punch-ins move inside the shot.** Cut in at the brand's scale (default 1.15–1.4×, CAM-01), then keep a slow push toward the face across the line (CAM-02, about 1.08× over the line) instead of a still scale step; hard cut back on the next line. Emotional beats get the bigger move. A brand whose motion row says the camera is static keeps the cut-in only.
- At every scale the eyes stay near y 640 and the mouth above y 1500.
- **Crash zoom** (CAM-06): one per Short at most, on the pivot word, with something new right after it.

## Sound

Voice-led: music ducked about 15–25 dB under the voice, master at −14 LUFS unless the brand sets its own (`craft/sound.md`). Sparse, dry SFX; on a deadpan beat, silence or one small sound lands harder than a stack of whooshes. Music rights per platform in `platforms.md`.

**Sound step (before the creator approves any draft's sound):** bake one mix file for the whole Short and place it as the composition's only audio clip, then:
```
python3 $SKILL/tools/sound_check.py hf/assets/mix.wav --comp hf --target <brand LUFS> --bed <bed as placed> \
  --voice <voice stem> --music <ducked music stem> --sources <gained voice files> --listen _review/listen-r<N>.m4a
```
It checks loudness on target, true peak at or under −1 dBTP, no clipped samples (sources gained before the limiter clip silently), the bed running to the end, and the voice over the bed; and writes a listen file. The creator hears the listen file (on the decision page or the preview) before the sound is approved; never approve a mix nobody has heard. After the final render, `--render out/<final>.mp4`: if its sound is off the mix by more than 1 LU (HyperFrames renders have come out ~5 dB low), remux the mix onto the render with the printed command; never re-render for sound.
