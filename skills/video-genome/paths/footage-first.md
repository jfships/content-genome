# Order B: footage first, graphics around it

The creator films first; graphics are built on their real words and real frame.

## B1. Shoot brief (before they film)

Step 1 for this order is lighter: decide format, packaging, angle, the story stack (at least type, framework, arc, hook types and CTA), hooks, beat outline and truth check. Leave per-beat moves, BPM and exact break-from-reality placement for B4–B5, once the footage exists.

Write `SHOOT.md` in plain words, from the approved plan:
- **Hooks to record:** 3–6, each said 2–3 ways.
- **Beats as bullet cues,** not a script, in the format's order.
- **Proof to capture:** screen recordings, the real object, the real place, before/after shots. These become the "show the real thing" material.
- **Framing that leaves room:** sit on a third with the open two-thirds on the side you face, eyes on the top third line, 5–10% head room (`craft/layout.md`). Shorts are shot on their own track (`shorts/build.md` "Recording"); if the long video's takes will also feed Shorts, film 4K and keep the face near the center so a vertical part can be taken from it.
- **Setup:** light, mic, room background from the brand; clap at the start of each take.
- **Extra takes for set pieces:** if a signature moment or break-from-reality moment needs several takes of the creator (Clone Grid, Mirror Debate, The Department of Me), list each take: position in the frame, what they say or do, same lighting, camera locked off.
- **Practice take** scored with the brand's take scorecard.
- **Everything else owed by the creator** from `debt.md` (screenshots, documents, permissions).

If the footage already exists, skip to B2 and note what's missing (e.g. no empty space → no side panels).

## B2. Inspect and transcribe

```
python3 $SKILL/tools/talking-head/scripts/inspect_video.py work/source.mp4 work   # contact.png + video.json
python3 $SKILL/tools/talking-head/scripts/transcribe.py work/source.mp4 work --lang <the brand's content language>   # words.json, words.txt, transcript.srt
```
- Look at `contact.png` yourself: where the face sits, whether there's empty space for panels or the speaker fills the frame, whether the footage is light or dark, and what the light looks like against the pack grade.
- Read the transcript. Flag misheard words and ask before changing anything they said.

## B3. Cut and claim check (gate)

Same as A3 in `paths/graphics-first.md`: drop stumbles and repeats without rewording, pick the hook, check claims against Proof, then a frame-accurate rough cut with video and audio matching within 0.05 s. The creator approves the cut on a page (`cut-list.json`): only the judgment calls, each with time and line, **Keep / Cut**. Save the kept spans as `cutlist.json`, render `cut.mp4`, then run `python3 $SKILL/tools/remap_words.py work/words.json work/cutlist.json work/words_out.json`. From here, `words_out.json` is the timing grid, and `motion/plan.json` points `"video"` at `../cut.mp4`.

## B4. Style of the edit (gate: one page)

Tone, moves and density are proposed in chat in plain words (**Confirm / Change it**). The parts that have to be seen (base treatment, captions) open the video's live picker on its **Look** tab, playing on their own footage (`decision-pages.md`, "The live picker"; `picker/README.md`). The same link carries every visual decision for the rest of the video.
- **Tone** read from the footage, the words, the format and the content personality.
- **Moves:** 4–8 from `craft/graphics-library.md`, only from families the brand allows, and which ones you're deliberately *not* using and why.
- **Density:** light (2–4 moments a minute), medium (4–7) or heavy (most lines). High-energy personalities lean heavier; calm ones lighter.
- **Base treatment:** background blur, dim, color or image replacement; zoom style (ease or punch) from the motion table.
- **Captions:** the brand's caption style, or none.

## B5. Beat brief (gate: written, then one page)

One row per beat, in `plan.md`. The builder writes it, not the creator; it is the creative work, done on the strongest model.

| # | In–Out | Line | Job | Device (source) | Layout + speaker box | Graphic box | Size | Enter / exit | Hold | Why this, not the two alternates |

- **Job:** straight man · unsaid line · exaggeration · proof · breather (`craft/graphic-jobs.md`). "Illustrates the line" is not a job.
- **Device (source):** what it is and where it came from: *their material* · *kept* (the brand's lists) · *new* (designed in brand limits, `craft/brand-fit.md`) · *generated* (image or clip, brand image rules). Candidates from every source are listed before the pick.
- **Layout and boxes:** the named layout for the speaker (`shorts/build.md` "Layouts" for vertical; `craft/layout.md` §2 for wide) and the pixel box of the graphic. Consecutive beats never share a layout unless the hold is the joke.
- **Size, enter/exit, hold:** in px and seconds, from the brand's motion table; proof holds ≥ 1.1 s; no single graphic over ~4 s.
- **Why:** the builder writes 2–3 treatments per beat, ranks them and records why its pick beat the others. Every beat that gets a treatment becomes a row on the picker's **Beats** tab with those treatments playing on that beat's footage, the builder's pick marked "Our pick"; the creator makes one pick per row.
- Every moving graphic is proved as a rendered 2–4 s clip of that beat before the full build.
- Gate: every beat has a job, a source, a reason and a layout, and `craft/graphic-jobs.md` "Self-check" passes, before the first still is built.

Then the creator picks on the **Beats** tab and watches the **Watch** tab (every pick stacked) before the first full render. The draft review that follows the render adds a **Fixes** tab for only the beats they flag, each showing the current version next to 2 alternatives.

Rules:
- Placement per beat is the named layout in the row, re-decided whenever the speaker moves or leaves (`craft/layout.md`).
- Show the subject's real objects, taken from the words.
- Never invent numbers, quotes, prices or results; label illustrative stand-ins.
- One idea per moment. One change per spoken beat (0.4–1.2 s).
- At least 2 s of plain face between moments that cover or move the face. Nothing in the first second of the hook.
- Brand components where the brand puts them (sting after the hook, series tag at the first on-camera moment). Long videos only; Shorts carry none of them (`shorts/build.md`).
- Signature moments, wildcard and break-from-reality moments as planned in Step 1.
- List the base treatment, zoom words, caption style and thumbnail stills.

## B6. Build

Work through `debt.md`; mark each row done as it's built and file reusable results in `07 Asset Library/`.

Order matters; later steps use earlier outputs.
1. **Grade, then base.** Grade the cut with `$SKILL/tools/grade.py` and the brand's recipe. Then, if background or zoom moves were chosen, fill `plan.base` and run `python3 $SKILL/tools/talking-head/scripts/base.py motion/plan.json` (slow; start it first). Write `motion/brand/brand.json` from the brand (`setup/tools.md` §3).
2. **Overlay clips** (panels, word pops, text behind the speaker, speaker-to-side, lower thirds): place by `craft/layout.md`, build with the bundled engine (`tools/talking-head/reference/engine-api.md`, `reference/looks.md`, the examples), restyled from the brand (fonts, colors, motion table). Speaker-to-side needs `speaker_frames.py` after the base.
3. **Full-graphic scenes** (cutaways, signature moments, chapter cards, data moves): build in HyperFrames, as in Order A. Footage that plays inside a scene is a root-level clip, not nested inside another timed element.
4. **Stills on the key words:** `node tools/talking-head/engine/beats.js …` for engine clips, Playwright stills for HyperFrames scenes. Fix anything cramped, clipped, unreadable or off-word, then check again.
5. **Render** drafts at the chosen draft quality (`plan.md`, "Draft quality") and finals at the footage's fps and resolution. Transparent clips go to `.mov`. Drafts use the rough cutout; the first final draft needs the final cutout method decided and its matte made (`plan/run-sheet.md` item 14, passed to `base.py` as `"matte_video"`).
6. **Captions:** `captions.py phrases`, read and fix `captions.json`, then `captions.py ass … --style plain|highlight` in the pack's caption style.
7. **Insert the sting.** The sting goes after the hook, not over speech: split the cut at the end of the hook, place the sting clip (with the sound logo) between the two parts, and shift every later time (clips, words, captions) by the sting's length. Use `remap_words.py` with the new spans to keep word times right.
8. **Composite:** `python3 $SKILL/tools/talking-head/scripts/composite.py motion/plan.json motion/out/picture.mp4 --deliver motion/out/picture-1080p.mp4 --size 1920x1080 --fps 30`. For text behind the speaker, run `subject.py occlusion` on every such clip; a FAIL blocks delivery.
9. **Mix and finish:** `python3 $SKILL/tools/mix.py mix.json` puts the cleaned voice, the music lanes (ducked under the voice), the SFX and the sound logo on the composite, at the target loudness (`craft/sound.md`).
10. **Shorts are not made here.** Never crop this cut into a Short. Each Short runs on the Shorts track (`shorts/README.md`) with its own script, fresh hook and tall build; this episode's footage can be a part inside it (`reframe_vertical.py` on one source clip, following the head).

Once the creator has seen the first full draft, give the switch-model nudge (SKILL.md, "Which model for which part"). Then sound (`craft/sound.md`), gates 2–4 (`review/checks.md`) and deliverables.

## Two hard rules for anything that moves or covers the speaker

- **Re-center on the subject, not the frame.** Zooms and speaker boxes follow the tracked head (`focus:"auto"`). If a box or zoom crops the head or leaves the speaker off-center, fix it before rendering.
- **Never fully hide words behind the speaker.** Words behind them stay at least 70% visible at every moment.
