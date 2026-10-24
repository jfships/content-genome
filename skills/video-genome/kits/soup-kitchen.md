# Brand Sheet: Soup Kitchen (included kit)
kit: soup-kitchen · For: food spots, small businesses, funny day-in-the-life, made-up clay characters. Made for video-genome; copied to the brand folder as `Brand Sheet.md` when picked. `open` = asked when a video needs it, then written back here.

## 1. Creator
open (asked once at intake: name, platforms, language, on camera or not, content personality ranked, truth rules, quirks). Works with no filming at all: the whole video can be generated in clay.

## 2. Why and feel
open · Kit feel: a sunny small-business world where things go a little wrong, told with a grin. Vertical first.

## 3. Research
open · Kit defaults: visual + spoken + text hook together in 0–2 s, no logo first · the polished half is a faithful influencer parody; the cut to reality is hard and loud · payoff in the last 3 s · keep the clay texture (thumbprints, 12 fps, slight boil); smooth motion reads as generic AI · the last frame loops cleanly into the first.

## 4. Formats
open · Formats this kit is built for (offer them at intake; the creator decides):
- **Pretty vs Real** (30–45 s vertical): hook to camera in golden slow-mo → the pretty version → freeze + record scratch + REAL sticker → what really happened → repeat 2–3×, each worse → a turn outside their control → payoff shown pretty for real → one-line button that loops to the hook.
- **One-Star Theater** (10–15 s vertical): one-star stamp + the review read out → deadpan clay reenactment → sunny reply → a button line. The joke is the request, never the reviewer.

## 5. Look
### Palette
- Background #FFF4D6 · words #1F2A44 · pop color #E8452C · second color #1FA89A · pale #FFD86B · scene-only storm #5B6B7A
### Fonts
- Titles: Titan One (width scale 0.75) · Text: Nunito · Notes: Patrick Hand · Captions: Nunito heavy with a 6 px navy outline (all in page-template/fonts)
### Art style (generated scenes)
- Main: Claymation · Backup: Clay 3D (smoother, for shots where the clay boils too much) · Alternatives: Stop-motion, Paper cutout
- Prompt base: "claymation stop-motion still, plasticine figures with visible thumbprints, handmade miniature set, bright summer daylight, palette of butter yellow #FFF4D6, tomato red #E8452C, seafoam #1FA89A, sun yellow #FFD86B, navy shadows #1F2A44, shallow depth of field, vertical 9:16". Ask for: matte plasticine, handmade imperfections.
### Color editing
- Pretty beats: golden hour, soft bloom, slight slow-mo (preview `sepia(.18) saturate(1.25) brightness(1.07) contrast(.96)`)
- Real beats: flat noon light, harder shadows, less color (preview `saturate(.75) contrast(1.12) brightness(.97)`)
- Real footage (if any): warm summer, saturation 1.1, contrast 1.03, highlights toward #FFF4D6
### Text style
- Sticker labels (main): Titan One on a tomato or seafoam rounded sticker, 4 px cream border, tilted −4° to +4°, soft drop shadow · Chalkboard menu (backup): Patrick Hand on a navy board · Hand-painted sign plank (alternative)
### Captions
- Word-by-word pop (main): 3–5 words per line, max 2 lines, white with a 6 px navy outline, current word in #FFD86B, mid-lower third · White on a navy box (backup) · Always on
### Backdrops
- Butter plain with a sun-yellow halftone sun (title cards, default) · Awning stripes (tomato/butter) · Boardwalk planks · Beach sky · Storm sky (#5B6B7A, for the turn)
### Extras kept
- Tilted stickers (PRETTY / REAL / 1 HOUR LATE / SOLD OUT: labeling a beat) · Hand-drawn arrow (pointing at a detail) · Clock stamp ("11:00 → 12:04": time jumps) · Thermometer callout ("94°F": heat jokes)
### Signature moments
- SOLD OUT stamp (the payoff) · One-star stamp (One-Star Theater) · max 1 big moment per video

## 6. Movement
- Motion feel: Main Handmade (12 fps on twos, slight boil, small shake) · Backup Playful (`back.out(1.7)`) · Snap only for the record-scratch beats
| Field | Value |
|---|---|
| Entrance ease | `steps(3)` then `back.out(1.4)` (stickers squash in) · captions word-spring `back.out(1.7)` · stamps `expo.out` |
| Exit ease | hard cut |
| On-screen move | `steps(n)` / `power1.inOut`, on twos |
| Overshoot | small (back.out); stamps get a 2-frame shake instead |
| Base unit | stickers 0.25 s · stamps 0.15 s · title swing-in 0.5 s |
| Stagger | 60 ms |
| Transitions | Hard cut (default) · Freeze 6 frames + record scratch (pretty → real) · Whip pan · Iris (final button only) |
| Hold | stickers 1.5–2 s · stamps 1.2 s · titles 1.5 s |
| Phrase length | 4 beats at 110 BPM per beat group; cut on the beat |
| Wildcard | Iris out on the last line (at most one per video) |

## 7. Sound
| Lane | BPM | Use when |
|---|---|---|
| Tropical (ukulele, marimba, soft kick) | 110 | every pretty beat |
| Orchestral comedy (plucked strings, bassoon) | 120 | after each record scratch, things going wrong |
| Surf (reverb guitar, fast drums) | 150 | the turn and the win |
- The pretty lane stops dead on the record scratch; never crossfade.
- Sound effects: record scratch (punchlines) · paper slap (stickers land) · wooden thud (stamps) · cash register (success) · slide whistle up (before the turn) · cartoon boing (fails, max 1 per video) · plus sounds from the creator's own world (pots, bubbling, rain on an awning, gulls).
- Sound logo default: three ladle-on-pot clinks rising E6 → G6 → C7, the last one rings, ~0.9 s (synthesized in code).
- No vocals under speech. Generated or licensed music only.

## 8. Kit
- Name tag: the main sticker style, tilted −3°, name on line 1, role on line 2, once, ~2 s, first line to camera, beside the face, never over it.
- Series tag: a seafoam sticker, series name / "Ep N" on its own line, first 2–3 s, top-left, small.
- Sting: under 1 s, the wordmark squashes in at 12 fps with the sound logo. Only before the payoff, or cut. Never in the first 3 s.
- Wordmark: their name in Titan One, words color on butter, with three seafoam steam wisps.
- End card: none (vertical loops back to the hook).
- Corner mark: off.
- Covers / thumbnails: the character's face + one sticker word, title in the top third, nothing in the bottom 20%.

## 9. Vertical
- Layouts: Full frame + captions (default) · Pretty/Real split, top/bottom (one beat max) · Title on top (the hook) · Over a review card (One-Star Theater) · Text card (time jumps)
- Captions: ≥44 px headline / 34 px body at 1080×1920, 2–3 word chunks, one line (two at most).
- Motion: holds −25%, no title longer than 1.5 s. First 3 s: visual + spoken + text hook together.
- Safe box: x 65–930, y 250–1500 at 1080×1920; cover text inside y 400–1300 (Instagram grid crop). Confirm live at upload.

## 10. Voice
open · Kit default when the creator has none: short sentences (3–9 words), warm and optimistic against obvious disaster, problems get a shrug and a grin, never mean.

## 11. Break-from-reality moments
- Nature documentary (a hushed narrator watches the owner fix something by hand) · Trailer (the turn cut like an epic movie trailer) · Review reenactment (freeze, the review text, a tiny clay theater with curtains). Plan proposes 2–3, the final keeps 1–2; never pre-generated.

## 12. Images
- Everything can be generated in the kit's claymation style. Brief approved before every generation; one image at a time until the look is stable; the first approved character image becomes the reference for every later shot (saved to `07 Asset Library/people/`). Before any paid generation: tool, what it makes, price from the tool's own check, wait for yes.
- Disclosure: a clearly cartoon clay style is usually not "realistic" under platform AI-label rules; check each platform live at upload, and say "animated with AI tools" in the description.

## 13. Profiles
open

## 14. Run sheet
- Use video-genome's run sheet (plan/run-sheet.md) as is, plus: a record scratch on every pretty → real cut; signature character details in every shot.

## 15. House rules
- No surreal moments (talking food, melting clay, magic); grounded slapstick only
- No neon or glitch effects
- No glossy, over-smooth AI motion; keep 12 fps and thumbprints
- No photoreal people; everything is clay
- Never mock a reviewer or customer as a person; the joke is the request
- No logo or sting in the first 3 seconds
- No real towns, brands, review sites or people; no made-up numbers presented as real

## 16. Changes
- Included kit, version 1 (2026-10-12). Built from a brand-genome demo brand (a beach-town soup shack), with the character, town and story removed so any creator can use it.
