# Stage 8: Vertical system (Shorts, Reels, TikTok)

Runs only if Shorts, Reels or TikTok were picked in Stage 0. Every page here is built from `../page-template/` with the words in `../voting-pages.md`. Three pages and three short chat questions, one decision at a time. Open the stage with its plain hand-off (what it is, three pages and a few questions, about 10 minutes, they can stop anytime).

A Short is not the long video cropped. It's its own video: written for vertical, watched on a phone, often with the sound off, behind platform buttons, judged in the first second. This stage adapts the brand to 9:16. Ideas, scripts and edits of each Short belong to idea-genome and video-genome.

**Check live first:** each platform's current safe zones, cover crops and length limits. The numbers below are starting points (Oct 2026) on a 1080×1920 frame; write the date checked into `vertical.md`.

## Fixed rules (said once in chat, in two plain lines; never asked)

- **Safe box:** anything important stays inside x 65–930, y 250–1450. The top ~250 px is the platform's top bar; the right rail (x > 930) is covered by buttons from about y 900 down; the bottom ~470 px by the caption, handle and audio rows. **Instagram grid crop:** the grid shows a centered 3:4, so only y 240–1680 survive. Both are drawn on every vertical mock, on every page.
- **The hook:** lands in the first 1–2 s on three layers together: the creator (or their real material) on screen in frame 1, a spoken line, and 3–7 words of hook text visible from frame 1. Frame 1 makes sense with no context. Nothing comes before it.
- **Openers:** no sting, no sound logo, no name tag on Shorts. Corner mark off.
- **Series tag:** only as "Part N", for series formats, folded into the hook text (or a small tag right after the hook). Never before the hook, never competing with it.
- **Endings:** no subscribe ask, no end card or closing card, no sting, no outro, no words that announce the end. Each Short ends on one of the kept Short endings (step 6).

## 1. How they shoot Shorts (chat, before any page)

One AskUserQuestion. Say what it changes: "This decides how your Shorts are framed, and which layouts lead on the next page." Options:
- *Phone upright* (native vertical; sharpest and simplest). Recommended unless they film on a camera.
- *Camera sideways in 4K, framed for a center crop* (one shoot gives both: the center 1215×2160 becomes the Short, so the face stays in the middle third of the wide shot).
- *Mostly from my long videos.* Say plainly: each Short is still written for vertical with its hook recorded fresh; long footage only goes in as parts (a reaction, a screen, a clip) rebuilt in a tall frame. A 1080p sideways shot cropped to vertical is too soft for a full-frame face, so those clips only fit small insets.
- Other.

Then write the **framing marks** into `vertical.md` (no question): chest-up medium close-up; head in the top 30–40% of the frame; eyes on or near the upper third line (y ≈ 640); center-weighted; nothing important outside the safe box. In demo, the persona answers from its filming setup.

## 2. Your backdrop, built tall (automatic, no question)

The default backdrop (Stage 4, step 8) gets a 1080×1920 version, **built tall, never a crop of the 16:9 plate**:
- Plains, gradients and patterns: redrawn tall in the palette. Free.
- A scene (a backdrop photo, or the room they're cut out over): rebuilt tall with the same objects and light, open space behind the head (y 250–900) and nothing busy behind the captions. Free path until it exists: the palette plain, tall. The tall scene comes from the creator's own upright photo of the space, or an image tool if they want one (name it and the cost from its own price check; run only on a yes).

Say it in one line: "I built your backdrop tall for Shorts." It sits behind the backdrop and cut-out layouts on the next page and on the Brand Genome page. Save it to `01 Brand Kit/exports/` with a `Type: kit` row in `07 Asset Library/asset-index.md`.

## 3. Layouts (library page)

`vertical-layouts.json`, three sections, ~30 layouts from `../catalog/vertical-voice-formats.md`, each a real 9:16 test frame inside a phone, with the app's buttons and caption ghosted over it and the safe box and 3:4 grid crop drawn on:
- **Everyday:** full frame + captions, title on top, split screen + you, picture in picture, text card, you over a backdrop, before / after, reaction, big quote, countdown list, framed window, handwritten notes.
- **Cut-out and green screen:** cut-out over the screen, title behind you, number behind you, you in a drawn world, green-screen room, over a screenshot, floating head, floating cards, reply to a comment, pointing at the screen, stacked reactions, side by side.
- **Break-from-reality:** trapped in a notification, peeking in, shrunk in a frame, the screen cracks, the frame tilts.

Built from the native vertical test photo (`../benchmark/10-car-vertical.jpg`, or the creator's own upright photo once it exists; never a 16:9 photo cropped to 9:16), drawn graphics for "the screen", the tall backdrop, and a plain gray silhouette for cut-outs: never another person's photo, and never an art-style image with someone else in it as "your drawn world". Keep in library / Discard; each Short picks one. Mark the one that fits each Stage 3 Short format in its "For:" line. Show the layouts that fit how they film first (a green-screen layout leads if they said green screen; screen-first layouts lead for screen recordings).

**Then, automatically: a framing spec per kept layout** (no question), by its family (`../catalog/vertical-voice-formats.md` names each layout's family), into `vertical.md`:

| Family | Face | Content | Captions | Hook text |
|---|---|---|---|---|
| Full face | chest-up, head in the top 30–40%, eyes y ≈ 640, centered | none, or graphics beside the face | y 1150–1400, below the chin | y 250–520, above the head |
| Stacked | below the band: chest-up, eyes about y 1050, chin above y 1250 | a 16:9 band on top, full width, y 250–858 (1080×608) | y 1280–1400, below the chin | over the top of the band, y 250–520 |
| 60/40 split | the lower 40% (from y 1152): head and shoulders, eyes a third down the panel, face inside y 1152–1450 | the top 60% | centered on the seam (y ≈ 1150), never across the eyes | over the top of the content, y 250–520 |
| Corner face | a box about 360×480 at lower left (x 65–425, y 970–1450), never on the right rail | full frame | beside or above the face box, inside the safe box | y 250–520 |

A split (stacked or 60/40) only when both must be seen at the same moment.

## 4. Hook text (fixed, one pick page)

The 3–7 words on screen from frame 1 that tell a stranger why to stay. Built like `vertical-layouts.json` (phone frames), title "Hook text", 6–10 options: the locked text style (Stage 4, step 6), its backup and alternatives at hook size, plus a few hook-only styles from `../catalog/vertical-voice-formats.md` ("Hook text styles"). Say in one line that it starts from their text style. Each option sits at y 250–520 above the face on the full-face layout, with the vertical captions below the chin; one option folds "Part 2" into the hook to show the series-tag rule. One page, no finalists (the text style was already narrowed in Stage 4): **Main** · **Backup** · **Alternative** · **Discard**. Rules written with it: 3–7 words, on screen from frame 1 for at least 2 s, never touching the captions or the face, inside the safe box, at least 44 px.

The same page shows one reference card with no buttons (`control: true`), **Your captions on a Short**: the Stage 4 caption style at the vertical spec, in a phone frame with the safe box drawn on:
- 2–3 word chunks, one line (two at most)
- heavy sans: the caption font if it is one; otherwise the heaviest sans in the font set, said once in chat
- caps, unless a house rule says otherwise
- one keyword per phrase in the pop color (never default yellow)
- centered around y 1150–1400, below the chin, inside the safe box; at least 44 / 34 px headline / body

## 5. Covers (library page, skippable)

The still a viewer sees in the grid and on the Shorts shelf. Built like `vertical-layouts.json`: 8–12 cover templates from `../catalog/vertical-voice-formats.md` ("Short covers") plus tall versions of the kept thumbnail layouts (Stage 7, step 7), each in a phone frame beside its 3:4 grid crop, so the creator sees what survives. Cover text 3–5 words, inside y 400–1300, clear of the face, in the thumbnail text spec's font, colors and outline (Stage 7, step 7). Keep in library / Discard; video-genome makes each Short's cover from the kept ones. YouTube Shorts custom thumbnails are a desktop upload (check live). Skipped → frame 1 with its hook text moved inside y 400–1300.

## 6. Vertical rules (chat, one AskUserQuestion call)

Up to four questions, each saying what it changes:
- **Ways to end a Short** (library, multi-select; keep any): *Loop line* (the last line runs into the first, so the replay feels seamless) · *Cut on the payoff* (it ends the instant the point lands) · *Deadpan hold* (a flat look to camera, 1 s or less, then cut) · *Button line* (one short last line that tops the payoff). Recommend from the content personality (deadpan or calm → deadpan hold; entertaining → loop line). Each Short's plan picks one and writes its exact last line.
- **Music under Shorts:** one of the kept lanes, or none (voice only).
- **Trending sounds on TikTok** (only if TikTok was picked): *Yes, added in the TikTok app, low under my voice* · *No, my own music only*. Fixed, no question: YouTube and Instagram masters stay clean (nothing trending or commercial baked in).
- **Captions on Shorts** (only if captions were set to long videos only in Stage 4, step 7): "Same caption style on Shorts, or none?"

## 7. Vertical pacing (stated, one confirm)

Show the vertical row of the motion table (Stage 5d) as plain lines, then ask once: **Keep all** / **Change one (say which)**.
- a visual change every 3–5 s (a cut, punch-in, graphic, text or B-roll); no single visual over ~8 s
- punch-ins of about 1.1–1.25× on the hook and each punchline, eased in, hard cut back
- one held deadpan beat (1.5 s at most) allowed per punchline
- music phrases of 4 beats

## Output

`vertical.md`: how they shoot Shorts and the framing marks; the tall backdrop (file path); the kept layouts with their use-when and framing spec; hook text (Main, Backup, alternatives, rules); the caption spec; the kept Short endings; covers (kept, or the skipped default); the fixed rules (hook, openers, series tag, endings); safe box and 3:4 crop numbers with the date checked; the audio policy per platform and the music lane; the vertical pacing row; the pages' artifact URLs.

**Hand-off at the end of Vertical** (one line): "Shorts and Reels are done. Next: your Brand Genome, everything you picked in one place."
