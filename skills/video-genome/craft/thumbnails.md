# Thumbnails

*Covers for Shorts and Reels: `shorts/platforms.md` "Covers" (same text rules, cover line inside y 400–1300).*

Thumbnails are chosen after the build, once it's clear what was actually said. Use the brand's kept thumbnail systems (usually 3–4, e.g. screen + face, before/after, a milestone frame, a one-word frame).

## Making them

- **Stills of the creator:** pick 3–5 frames where they look good: eyes to camera, mouth closed or smiling, sharp, well lit. If none work, ask for a quick photo in the same setup.
- **Start from the face.** The creator's best real expression, cut out cleanly with a white outline; write the words backwards from it.
- **Words:** 3–5 loud words, the rest as small context. The hook names the topic for the target viewer ("AI", "Claude", "tools"): a pure reaction line ("Zero clue") doesn't tell them why to click. The title is written after the thumbnail is locked and adds what it doesn't say; never the same words.
- **Build:** at 1280×720 with the pack's fonts and palette. The text block is built with `python3 $SKILL/tools/thumb_text.py spec.json out.jpg` (it applies the text rules below and measures the result); `$SKILL/tools/talking-head/scripts/thumbs.js` has three starter layouts (headline, card, name) to restyle for the rest.

## Text rules (from four rejected rounds and the approved EP 01 thumbnail)

The brand chooses the taste (font, colors, outline, shadow color). These are craft and don't change per brand:
- **One font family** for the whole block.
- **Sizes:** lines in the same group share one size; at most 3 size steps (context, main, hook) and only one loud element. The main text is 15–20% of the frame height or more.
- **One solid block, not a list:** each loud line's ink is fit to one shared width so the right edges line up. A small lead-in line ("I Had") may stay narrower; lines that are one sentence share one size.
- **One fixed gap** for the whole block, about 26 px at 1280×720, measured from each line's baseline to the top ink of the next line. Descenders hang into the gap and don't count. Never scale the gap by font size.
- **Place it:** vertically centered on the face, left-aligned 50–60 px in from the edge, clear of the face and of the timestamp corner (bottom right).
- **Shadow:** small and crisp (about 3 px across, 5 px down, 2.5 px blur), never a big soft one; it muddies tight lines.
- **Measure, don't eyeball:** `thumb_text.py` prints every gap and right edge from the real ink and flags anything off by more than 2 px.
- **Offer 2–3 options** with a recommendation, each in a different kept system, for A/B testing (e.g. YouTube's Test & Compare).

## Checks

- **Feed size:** view each at about 168×94 px among neighboring thumbnails (other channels in the niche). Is the subject clear and the text readable?
- **Clear zones:** text clear of the face and of the timestamp corner (bottom right).
- **Spacing:** `thumb_text.py` reports OK (gaps within 2 px, right edges lined up).
- **Contrast:** the subject and text separate from the background at a squint.
- **Honest:** the thumbnail shows something that's actually in the video.
- **On brand:** palette, fonts and system from the brand; no house-rule violations.
