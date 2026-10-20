# Order A: graphics first, voice last

*Long videos. A Short uses `shorts/build.md`: its pace, polish and layout rules are different.*

Build a polished motion draft, the creator records over it, then rebuild the video around their real words.

## A1. Polished draft (gate: the creator reviews the render on a draft-review page)

**Long videos can be built one part (act) at a time:** draft, review, record and rebuild one part, lock it, then the next. The plan names the parts; a locked part isn't reopened unless the creator asks. Work from `debt.md`: build items get built here; anything not yet shot, recorded or generated goes in as a labeled placeholder.

Build in HyperFrames: clips with `class="clip"` and `data-start`/`data-duration`, and the timeline at `window.__timelines["main"]`. Add a timeline label per beat (`tl.addLabel("s1-cards", 14.3)`) and place tweens relative to labels, so the rebuild can retime a beat to the creator's words by moving one label. The draft runs at a comfortable speaking pace, with breathing gaps between scenes. Always deliver the script beside the draft.

**The beat brief comes first (gate).** Before any scene is built, every beat is a row of the beat brief in `plan.md`:

One row per beat, in `plan.md`. The builder writes it, not the creator; it is the creative work, done on the strongest model.

| # | In–Out | Line | Job | Device (source) | Layout + speaker box | Graphic box | Size | Enter / exit | Hold | Why this, not the two alternates |

- **Job:** straight man · unsaid line · exaggeration · proof · breather (`craft/graphic-jobs.md`). "Illustrates the line" is not a job.
- **Device (source):** what it is and where it came from: *their material* · *kept* (the brand's lists) · *new* (designed in brand limits, `craft/brand-fit.md`) · *generated* (image or clip, brand image rules). Candidates from every source are listed before the pick.
- **Layout and boxes:** the named layout for the speaker (`shorts/build.md` "Layouts" for vertical; `craft/layout.md` §2 for wide) and the pixel box of the graphic. Consecutive beats never share a layout unless the hold is the joke.
- **Size, enter/exit, hold:** in px and seconds, from the brand's motion table; proof holds ≥ 1.1 s; no single graphic over ~4 s.
- **Why:** the builder writes 2–3 treatments per beat, ranks them, drops its own weakest and records why the winner beat the other two. The creator sees Main and Backup only on beats the builder marks **unsure**, as rendered clip cards (never stills for anything that moves, never a text description).
- Every moving graphic is proved as a rendered 2–4 s clip of that beat before the full build.
- Gate: every beat has a job, a source, a reason and a layout, and `craft/graphic-jobs.md` "Self-check" passes, before the first still is built.

**Polish rules. Check every scene against them.**
- **Something changes every 5–10 s**, and every 2–4 s in the first 30 s. Any hold longer than 6 s needs a reason: camera drift, parallax, a counter, a reveal or a cut. A static text card is never a scene by itself.
- **The hook proves the promise visually first.** Open on the video's own best material, then the line. The first 2 s are the most striking image, never a logo fade.
- **Laid out, scene by scene.** Every scene follows `craft/layout.md`: the graphic fills the open side, nothing hugs an edge, no empty patch without a job, placement re-decided when what's on screen changes. Every still passes its check.
- **Depth on every frame.** A background, a mid layer and a foreground layer, plus the pack's texture (grain, paper, noise) and vignette. Never the same flat background for two scenes in a row; rotate the pack's backgrounds and accents.
- **The pack's motion vocabulary only,** from the brand's motion table. Reserved transitions stay with their component (e.g. a wipe that belongs to the sting).
- **The pack's title styles.** Plain headline cards are the exception, not the default.
- **2–4 signature moments per long video,** from the brand's kept list (definitions in `craft/graphics-library.md`).
- **Walkthrough accents whenever a screen is shown:** cursor click, typing, scroll, push-in, drag, notification, tooltip, slider.
- **Brand components exactly where the brand puts them:** sting + sound logo after the hook, series tag at the first on-camera moment, end card, corner mark only if the brand turns it on, episode number where the brand says.
- **Show the real thing,** each artifact visibly different.
- **House rules** from the brand, every one.
- **Draft-only overlays:** a cue strip (SAY / SILENT + the bullet cue) and a dashed zone where the creator will probably appear (a provisional placement; A4 decides the final one). Both come out in the rebuild.
- **Temp sound:** a temp music bed and the key SFX, so the energy can be judged (`craft/sound.md`).

Run **gate 2** (build checks) on stills, then render, then **gate 3** and **gate 4** in `review/checks.md` before showing the creator. Show it with the render plus a draft-review page (`draft-review.json`): one still per scene with its time and line, **Looks right / Change it** and a note per scene. On this voiceless draft, skip the gate-3 checks that need a voice (captions, face, voice sync); they run after the rebuild. Once they've seen it, give the switch-model nudge (SKILL.md, "Which model for which part").

## A2. Recording kit (gate)

Write `RECORDING.md` in plain words:
- **Setup:** their camera, lights, mic, and the room background from the brand (generated plate, simple backdrop, or real room blurred and graded).
- **Takes:** clap, wait 2 s, play the draft, talk. Record every hook option.
- **Cue table:** video time / on screen / bullet cue. Cues by default; the full script on a prompter if the creator prefers that (brand file §10 Voice).
- **Wording that must be exact** (names, numbers, claims).
- **A practice take first,** scored with the brand's take scorecard, then the real take.
- **Everything else owed by the creator** from `debt.md` (screenshots, documents, permissions).

## A3. Transcribe, cut, claim check (gate)

- **Transcribe** with the bundled `$SKILL/tools/talking-head/scripts/transcribe.py --lang <the brand's content language>`. For long takes on a slow link, extract a 16 kHz mono WAV first and transcribe that.
- **The cut:**
  - Drop stumbles, fillers, repeats and weak asides. Never reword.
  - Pick the best hook.
  - Claim check against the truth rules and Proof.
  - Flag misheard words; ask before "fixing" anything they said.
- **Frame-accurate rough cut:**
  - Video: `fps=30`, then `select='between(n,a,b-1)+…'` with `setpts=N/30/TB`.
  - Audio: `aselect` over the same spans with `asetpts=N/SR/TB`.
  - Not trim+concat. Video and audio durations must match within 0.05 s.
- The creator approves the cut on a page (`cut-list.json`): only the judgment calls (a second take, an aside, a long pause), each with its time and line, **Keep / Cut**.

## A4. Placement and rebuild (gate: placement page first)

**Placement options.** One page (`placement.json`): a real frame of their take over a real scene for each option, with the scene's time and line in `context`, a Recommended pick, Main + Backup. Geometry for each in `craft/layout.md` §2. Single beats can still differ, decided by layout rule 4 (new scene, new layout):
- Full-frame camera with graphics over it
- Cutout beside the graphics
- Corner bubble
- Side panel
- Taking turns: creator full screen, then graphics full screen
- Voice only, over graphics

**Rebuild.**
- Map word times through the cut into output time: `python3 $SKILL/tools/remap_words.py work/words.json work/cutlist.json work/words_out.json`.
- Retime every key moment to the word that names it (move the beat's label).
- Rewrite headlines to echo their words.
- Captions in the pack's caption style (`embedded-captions` or the bundled `captions.py`), 2–7 words per phrase. Turn them off where big type already says the line.
- **Cutout:** drafts use the fast rough cutout (bundled `base.py` with `"matte": true` and the draft `"height"`; MediaPipe). Before the first final draft, the final cutout method must be decided (`plan/run-sheet.md` item 14) and its matte made; pass it as `"matte_video"` and drop `"height"`. Then soft-edge it (guided filter or a 2–3 px feather), add a soft shadow, and keyframe size per beat.
- **Real footage gets the pack grade** (`$SKILL/tools/grade.py` with the brand's recipe). Graded footage with flat graphics, or the other way round, is the most common "cheap" tell.
- Mix with `$SKILL/tools/mix.py`: music ducked under the voice, SFX and sound logo placed, master at target loudness (`craft/sound.md`).
- Rerun gates 2–4 at every beat change, and look at a full-resolution frame of each overlap.
