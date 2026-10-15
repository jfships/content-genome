# Building a Short

Everything here is 1080×1920 from the first frame of the first draft. Nothing starts as a 16:9 timeline.

## Rough draft (S3, before recording)

The creator judges by watching, so the plan becomes a tall rough draft before anything is filmed.
- Build it 9:16 in HyperFrames at draft quality, at the planned length, with the shape's beats on the planned times.
- Voice: the creator's existing words if the Short reuses them, otherwise a temp voice reading the script at the target pace (2.3–3 words a second). Label it "temp voice".
- On screen: the hook text from frame 1, captions in the brand's style, the layout, the backdrop, placeholders for what isn't shot yet.
- Show it with the script beside it. The creator says what changes; the plan is updated before recording.
- Building over budget on length is fine; cuts are made after watching.

## Recording (S4)

Shoot for the tall frame:
- **Native vertical** (phone upright) by default. Or **4K horizontal framed for a center crop** (the center 1215×2160 becomes 1080×1920). A 1080p horizontal crop is too soft for a full-frame face; use it only for a small inset.
- **Framing:** chest-up, head in the top 30–40% of the frame, eyes near the upper third line (y≈640), centered. Same distance, light and backdrop as the brand's vertical setup.
- **Record the hook fresh,** 3–6 ways, Main and Backup first. Then the lines, each new thought opening with its own hook sentence.
- **Delivery:** about 150 words a minute, eyes on the lens, one idea. Energy comes from the writing and the cut, not from shouting. A deadpan read lands on a tight cut.
- Write the prompter or `RECORDING.md` in plain words, with the exact words that must be said (names, numbers, the hook, the last line).

## Cut (S5)

1. Transcribe (`tools/talking-head/scripts/transcribe.py`), pick takes, cut frame-accurate (`paths/graphics-first.md` A3 "The cut" method). Save `cutlist.json`, run `tools/remap_words.py`.
2. **Trim dead air first:** cut every gap over about 0.4–0.5 s, and cut 0.1–0.2 s into the end of each line. Breaths go.
3. **Then, only if it still drags,** speed the speech up, 12% at most (`setpts`/`atempo` on the cut). Never speed up instead of trimming; never past 12%; judge it by watching. Note the speed in `log.md`.
4. Measure the cut with `tools/short_timing.py` (`checks.md`) before building graphics on it.

## Pace

- First payoff (laugh, twist, result) by 3 s; aim for the hook itself to be it.
- Something changes on screen every 3–5 s: a cut, a punch-in, a graphic, text, a screen. No single visual on screen longer than about 8 s.
- One held deadpan beat (1.5 s or less) allowed per punchline; that's the joke, not dead air.
- Punch-ins of about 1.1–1.25× on the hook and the punchlines: eased in, hard cut back.
- Spoken pace after the edit about 2.3–3 words a second; longest silence 0.6 s or less unless it's the planned hold.
- Call-and-response: 4 exchanges or fewer, each one escalating. Cutting back and forth more than that is the most common way a Short goes slow.
- The long-form energy arc (build-up, climax two-thirds in) doesn't apply. The Short peaks at the hook and again at the last line.

## Layout

Coordinates at 1080×1920 (`craft/layout.md` §1, Shorts and Reels):
- **Safe box** for anything important: x 65–930, y 250–1450. The right rail (x > 930) is covered by buttons from about y 900 down; the bottom ~470 px by the caption, handle and audio rows; the top ~250 px by the platform's top bar.
- **Layouts:** full-frame face with captions; stacked (a 16:9 screen or graphic band on top, face below); 60/40 content and face; the creator's face in a corner over full content. A split only when both have to be seen at the same moment.
- **Backdrop** built tall (the brand's tall backdrop), never a crop of the 16:9 plate. Cutouts sit on it at the framing above.
- **Hook text** y ~250–520, above the face, on screen from frame 1 for at least 2 s, never colliding with captions or the face.
- **Captions** centered around y 1150–1400, below the chin: 2–3 word chunks, one line (two at most), heavy sans, caps unless the brand says otherwise, one keyword per phrase in the brand's accent.
- **Text sizes** at least 44 / 34 / 30 px (headline / body / label); overlays stay at least 2 s.
- Graphics follow the rest of `craft/layout.md` (lead room, one focal point, nothing touching edges) re-decided per scene.

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
