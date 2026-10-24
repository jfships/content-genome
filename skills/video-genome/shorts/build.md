# Building a Short

Everything here is 1080×1920 from the first frame of the first draft. Nothing starts as a 16:9 timeline.

## Direction pages (S2b, before the first rough build)

A rough draft built before the creator has chosen a look gets judged on the look and wastes the round. So two pages come first, built from real material (the subject's films, pages and shots; a code-drawn mock only where nothing exists yet, labeled as a mock):
1. **The world:** whose visuals fill the frame (the subject's own films, ads or footage; product or object shots in space; the creator's own set). Two or three options.
2. **How the creator and the source share the frame:** full bleed with the creator over it, split top and bottom, or cutting between them. Two or three options.

Before anything is filmed, each option is a 1080×1920 still with the safe box drawn on, two stills per option (the hook frame and one mid beat); Main and Backup picked and saved in `plan.md`. Once real takes exist, both decisions are rows on the Short's live picker instead, playing on the takes, one pick each. Only then build the rough draft.

## Beat brief (S2c, after the direction pick, before the first rough build)

The direction pages settle the world and the frame. The beat brief settles every beat, and it is the builder's creative work, not the creator's: done on the strongest model, written into `plan.md`, one row per beat:

| # | In–Out | Line | Job | Device (source) | Layout + speaker box | Graphic box | Size | Enter / exit | Hold | Why this, not the two alternates |

- **Job:** straight man · unsaid line · exaggeration · proof · breather (`craft/graphic-jobs.md`). "Illustrates the line" is not a job.
- **Device (source):** *their material* · *kept* (the brand's lists) · *new* (designed for this line in brand limits, `craft/brand-fit.md`) · *generated* (image or clip, brand image rules). List candidates from every source before picking; "used last time" and "first in the list" are not reasons.
- **Layout:** one of the named layouts below, with the speaker's box; consecutive beats never share a layout unless the hold is the joke.
- **Why:** 2–3 treatments per beat, ranked, with why the builder's pick beat the others. Once the creator's takes or a first edit exist, each beat that gets a treatment is a row on the Short's live picker (**Beats** tab, `../decision-pages.md` "The live picker"), its treatments playing on that beat; one pick per row. Captions are picked once on the **Look** tab; when a beat's on-screen text is up, captions hide.
- Every moving graphic is proved as a rendered 2–4 s clip of that beat before the rough draft.
- Gate: every beat has a job, a source, a reason and a layout, and the `craft/graphic-jobs.md` self-check passes.

**Source visuals.** For a Short about a company, product or person, look for that subject's own films, ads, talks and footage first (official channels), and gather far more frames than the Short needs so the creator can choose. A screenshot of a web page is only for when the page itself is the point (an out-of-stock label, a price). Note every source in `plan/asset-debt.md`; check reuse rights as in `review/checks.md` gate 1. If downloads are blocked, see `setup/gotchas.md` "Frames from the web".

## Rough draft (S3, before recording)

The creator judges by watching, so the plan becomes a tall rough draft before anything is filmed.
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

## Cut (S5)

**Draft quality, asked again.** When the first draft built from real takes starts, and on any resumed session, ask the draft quality again with the measured time, and recommend the input's own frame rate: lip sync, eye contact and cut timing can't be judged at 15 fps. HyperFrames always draws at the composition size, so offer frame rate (and a smaller composition), not sizes it can't do (`plan/intake.md` "Draft quality").

0. **Screen every take on words, eyes, face and framing.** Never rank takes by audio alone and never assume a line stays voice-only: edits change and any line can end up on camera. Cut every take with picture at full quality.
1. Transcribe (`tools/talking-head/scripts/transcribe.py`), pick takes, cut frame-accurate (`paths/graphics-first.md` A3 "The cut" method). Save `cutlist.json`, run `tools/remap_words.py`.
2. **Trim dead air first:** cut every gap over about 0.4–0.5 s, and cut 0.1–0.2 s into the end of each line. Breaths go.
3. **Then bring the speech to the target pace** ("Spoken pace" below): measure it, and speed up only by the gap between what was said and the target. Never speed up instead of trimming.
4. Measure the cut with `tools/short_timing.py` (`checks.md`) before building graphics on it.
5. **Inserting audio before a take:** split the take's picture and voice. The picture can hold or slow; the voice is placed by its word times. Never start a take's media earlier than its first-word lead allows, or its own audio plays under the insert.
6. **Take files:** keep proxies shallow (small copies of the takes in one shallow folder such as `work/takes/`; deep folder trees can fail when files are copied between computers) and convert only the candidate segments listed from the transcript. Phone 4K HEVC decodes slower than real time on many laptops.
7. **Footage clips** (a source ad, a screen recording) are their own top-level clips in the composition, placed by CSS; the scene section holds only graphics (a video inside a timed section fails lint).

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
- A punch-in (about 1.1–1.25×, eased in, hard cut back) counts as a new shot; use it on the hook and the punchlines and to hide jump cuts.
- No single visual (one graphic, one screen) longer than about 4 s, even with motion inside it.

### Spoken pace

The target is a pace, in words a second after the edit, never a fixed speed-up. The creator's natural pace changes as they improve, so the speed-up shrinks to nothing on its own.
- **Default target 2.6–3 words a second** (the brand's number wins). Longest silence 0.6 s or less unless it's the planned hold.
- Order: trim gaps first, then measure (`tools/short_timing.py`, which prints the speed-up needed). Already at the target: no speed-up. Below it: speed up just enough to reach the low end, 12% at most (ffmpeg's `setpts` for picture and `atempo` for sound). Still slow at 12%: re-record that line faster.
- Per line is fine: a line that drags gets its own speed; a deadpan line may stay slower on purpose.
- Speed-up blunts deadpan and makes voices sound squeezed past about 10%; judge by watching. Write the measured pace and any speed in `log.md`.

### Structure

- First payoff (laugh, twist, result) by 3 s; aim for the hook itself to be it.
- Call-and-response: 4 exchanges or fewer, each one escalating. Cutting back and forth more than that is the most common way a Short goes slow.
- The long-form energy arc (build-up, climax two-thirds in) doesn't apply. The Short peaks at the hook and again at the last line.

## Layouts

Coordinates at 1080×1920 (`craft/layout.md` §1, Shorts and Reels). **Safe box** for anything important: x 65–930, y 250–1500. The right rail (x > 930) is covered by buttons from about y 900 down; the bottom ~420 px by the caption, handle and audio rows; the top ~250 px by the platform's top bar.

Every beat names one of these layouts in the beat brief. Two consecutive beats never share one unless the hold is the joke; one layout for a whole Short is a fail. Boxes are the defaults; a beat may move them, inside the safe box, by writing the new box in its row's "Layout + speaker box" / "Graphic box" cells.

| Layout | Speaker | Graphic | Use when |
|---|---|---|---|
| **Full frame** | Chest-up, centered, eyes at y≈640 (head in the top 30–40%) | None, or hook text y 250–520 | Breathers, the hook, a punchline hold |
| **Punch-in** | Full frame scaled 1.15–1.4×, eyes stay ≈ y 640; may shift off-centre to make room | A word or label in the space opened up | Key lines, hiding a jump cut, a reaction |
| **Split top** | Cutout or crop in the lower band, eyes at ≈ 60% of frame height (y≈1150), centered | 16:9 band at x 0–1080, y 250–860 (their footage, a screen) | Straight man and proof beats where their material and the reaction are seen together |
| **Over their page** | Cutout at about 0.64 of its full-frame size, bottom-left (about x 40–620, y 850–1450), feathered edge, never over the subject of the shot, never in x > 930 | Their page, post or shot full-bleed behind | Reading or reacting to a page, a post, a quote |
| **Full graphic** | Off screen, 1.1–4 s at most | The whole safe box | Proof that must be read alone; a gag; the unsaid line as a scene |
| **Words behind** | Full frame or punch-in | Big words layered between the backdrop and the cutout, beside the head, ≥ 70% visible | One standout line, the hook, a reveal |
| **Floating card** | Full frame | A card, notification or object in the open space at head height, on the side the speaker faces | The unsaid line, an interruption, a small proof |

- **Backdrop** built tall (the brand's tall backdrop), never a crop of the 16:9 plate. Cutouts sit on it at the framing above.
- **Graphics keyed to a word** start on its measured onset, not Whisper's time: `tools/onsets.py <take> words.json words_onsets.json --words "<anchor words>"`, then `remap_words.py` onto the cut. Words it marks `rise` (connected speech) get one listen at the anchor.
- **Hook text** y ~250–520, above the face, on screen from frame 1 for at least 2 s, never colliding with captions or the face. **Place it from the face, not a fixed y:** measure the top of the head on the frames it's up and keep the text's largest box (its pop-in scale included) clear of it; a pop-in from 1.6× that clears at rest can still cover the chin or beard for 4 frames. List it in `work/overlays.json`.

**Safe zones on every layout or split change.** Before building any layout change or a requested split (55/45, a lower band, a bigger speaker), measure the mouth and chin on the real frames of that layout against the bottom line (y 1500): run `tools/draft_checks.py` on a short test render, or measure the face on 3–5 frames of the take at the new scale and offset. If the request breaks the line, say so before building, with the measured numbers and a safe alternative ("at 55/45 your mouth sits at y 1540, under the caption rows; 50/50 lifted 50 px keeps it at 1480"). Fix with the smallest change that clears it, measured, not guessed: a 170 px lift overcorrects where 50 px was right. Re-measure per frame on the draft, since the speaker moves.
- **Captions** centered around y 1150–1400, below the chin, inside the safe box on every layout (on Split top and Over their page the chin sits higher or to the left, so the caption box moves up or right, never into x > 930 or y > 1500): 2–3 word chunks, one line (two at most), in the brand's caption spec (`vertical.md` or `look.md` "Caption spec": case, font and weight, size, plate, lines, box and centering, key word), one keyword per phrase in the brand's accent. **No spec, no captions:** if a field is missing (the case most of all), ask the creator in one question box before building any caption, with sentence case recommended, and write the answer back into the brand's caption spec. Never default to the hook's style or Title Case. Every spoken beat is captioned unless the beat brief gives a reason (`"captions_off": "<why>"` in `work/beats.json`, e.g. the line is already on screen as big type).
- **Text sizes** at least 44 / 34 / 30 px (headline / body / label); overlays stay at least 2 s.
- Graphics follow the rest of `craft/layout.md` (lead room, one focal point, nothing touching edges) re-decided per scene; the beat brief's boxes are checked on stills and by `tools/tech_review.py` before any render.

## Brand-kit pieces

- No sting, no sound logo, no end card, no name tag on a Short.
- A series tag only as "Part N", folded into the hook text or small after the hook; never before or competing with it.
- Corner mark off unless the brand turns it on for vertical.

## Graphics and motion

- Build in HyperFrames at 1080×1920 (or the bundled engine over the cut, `tools/talking-head/`), restyled from the brand's vertical motion row.
- Spatial moves (`craft/spatial/`) work tall too: re-frame them for 9:16, don't squeeze a 16:9 scene.
- Stills first (Short gate 2), then render.

## Sound

Voice-led: music ducked about 15–25 dB under the voice, master at −14 LUFS (`craft/sound.md`). Sparse, dry SFX; on a deadpan beat, silence or one small sound lands harder than a stack of whooshes. Music rights per platform in `platforms.md`.
