# Stage 8: Vertical system (Shorts, Reels, TikTok)

Runs only if Shorts, Reels or TikTok were picked in Stage 0. Every page here is built from `../page-template/` with the words in `../voting-pages.md`. One page and two chat questions. Open the stage with its plain hand-off (what it is, one page and two questions, about 5 minutes, they can stop anytime).

Vertical is not the long video cropped. It's watched on a phone, with the sound often off, behind platform buttons. This stage adapts the brand to 9:16.

**Check live first:** each platform's current safe zones (where captions, buttons and the profile row cover the video) and length limits. As a starting point (Oct 2026): keep text out of roughly the bottom 20% and the right 15%, and keep key content inside the center ~4:5.

1. **Layouts** (library). `vertical-layouts.json`, three sections, ~30 layouts from `../catalog/vertical-voice-formats.md`, each a real 9:16 test frame inside a phone, with the app's buttons and caption ghosted over it:
   - **Everyday:** full frame + captions, title on top, split screen + you, picture in picture, text card, you over a backdrop, before / after, reaction, big quote, countdown list, framed window, handwritten notes.
   - **Cut-out and green screen:** cut-out over the screen, title behind you, number behind you, you in a drawn world, green-screen room, over a screenshot, floating head, floating cards, reply to a comment, pointing at the screen, stacked reactions, side by side.
   - **Break-from-reality:** trapped in a notification, peeking in, shrunk in a frame, the screen cracks, the frame tilts.
   Built from the face test photo (or the creator's own photo once it exists), drawn graphics and a plain gray silhouette for cut-outs: never another person's photo, and never an art-style image with someone else in it as "your drawn world". Keep in library / Discard; each Short picks one. Mark the one that fits each Stage 3 format in its "For:" line. Show the layouts that fit how they film first (a green-screen layout leads if they said green screen).
2. **Captions.** The caption style was picked in Stage 4 (step 7). If captions are on in Shorts and Reels, reuse it at vertical sizes (minimum ~44 px headline / 34 px body at 1080×1920, max 2 lines, 3–5 words per line). Ask one chat question only if they set captions to long videos only: "Same caption style on Shorts, or none?" No new page.
3. **Vertical rules.** One AskUserQuestion call with three questions: *The sting on Shorts and Reels?* (cut it / under 1 s) · *Faster motion for vertical?* (yes, shorter holds and 4-beat phrases / show me first) · *Music under vertical?* (pick from the kept lanes). Fixed, no question: the series tag in the first 2–3 s, smaller; no closing card (vertical loops).
4. **The first 3 seconds.** Write the rule: a visual hook, a spoken hook and a text hook together, no logo first.

Covers for Shorts and Reels are not decided here; video-genome makes one per Short from the kept layouts.

## Output

`vertical.md`: the kept layouts with their use-when, caption spec, tag placement, motion and sound for vertical, safe-zone numbers with the date checked, the page's artifact URL.

**Hand-off at the end of Vertical** (one line): "Shorts and Reels are done. Next: your Brand Genome, everything you picked in one place."
