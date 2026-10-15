# Layout: where things sit on screen

Every scene is a composition, re-decided from what's on screen at that moment. The brand decides colors, fonts and motion; this file decides placement. Read it before building any scene, and check every still against the list at the end.

Coordinates: 16:9 is 1920×1080 (thirds at x 640/1280, y 360/720). 9:16 is 1080×1920 (thirds at x 360/720, y 640/1280). Scale proportionally for other sizes.

## 1. Rules

**Around the speaker**
1. **Fill the open side.** Speaker on one third → the graphic fills the other two-thirds, sized to it, starting one gutter (≈96 px) from the speaker. Never a small box parked at the far edge with a gap in the middle (the Act One failure).
2. **Room in front.** Leave space on the side the speaker faces. Graphics go in that space or behind them, never between them and the edge they look toward (short-siding).
3. **Off face and hands.** Nothing covers the face, mouth or gesturing hands. Words behind the speaker sit beside the head, never across it.
4. **New scene, new layout.** Decide placement per scene from where the speaker is now; never inherit it. Speaker leaves → the graphic takes the frame. Speaker moves → the graphic moves to the new open side.
5. **Line up with the eyes.** Keep the eyes on or just below the top third line (y≈360 on 16:9, y≈640 on 9:16). A graphic's top edge or baseline sits on the eye line, the top margin or a third line.
6. **Head room on zoom-ins.** 5–10% of frame height above the head. When punching in, keep the eyes on the top third and the speaker on their third so the open side survives.
7. **Off-center balance.** A speaker on a third balanced by a graphic is the default. Don't center a small graphic against a centered speaker.

**Space and edges**
8. **Safe margin.** All text and graphics at least 96 px (5%) from every edge on 16:9 (EBU R95 graphics-safe). Nothing touches or crosses an edge unless it's a deliberate full-bleed.
9. **No space without a job.** Any empty area over ~15% of the frame (or wider than a quarter of it) is breathing room beside the speaker, or something fills it. Gaps between elements are no wider than the margin.
10. **Snap to the grid.** Every edge sits on the margin, a thirds line, the center or the split line. Never a few pixels off.
11. **One grid per video.** 12 columns, 96 px margins, 32 px gutters on 16:9, same corner radii, reused in every scene so nothing jumps.

**Size and reading**
12. **One star per moment.** One dominant element, 2–3× the next. Balance is visual weight, not equal area.
13. **Three text sizes at most.** Key phrase cap height ≥ 7% of frame height (≈76 px at 1080p); secondary 50–60% of that; nothing under 4% (≈43 px at 1080p, ≈40 px on 1080×1920).
14. **Short lines.** Display text ≤ 25–30 characters a line, ≤ 3 lines, block ≤ 50–60% of frame width on 16:9 (80% on 9:16). Captions ≈ 42 characters, ≤ 2 lines.
15. **Keep related things together.** A label sits within a third of its own height of what it names; unrelated items get at least twice that space.
16. **Read in order.** Top-left to bottom-right: setup first, result or punchline last (Z for sparse frames, F for text-heavy).
17. **Lower third.** Left-aligned at x=96, bottom edge at y≈900–950, 90–130 px tall, below the chin. Simple fade or slide.

**Shorts and Reels (9:16)**
18. **Safe box.** Everything important inside x 65–930, y 250–1450 (the strictest overlap of TikTok, Reels and Shorts UI). The right rail (x > 930) is covered by buttons from about y 900 down; the bottom ~470 px by the caption, handle and audio rows; the top ~250 px by the top bar. Instagram's grid shows a centered 3:4 crop: cover text inside y 400–1300.
19. **Face high, captions below.** Chest-up, head in the top 30–40% of the frame, eyes near y≈640; hook text y ~250–520; captions centered around y 1150–1400, below the chin. Full rules: `shorts/build.md` "Layout".

## 2. Standard layouts

Pick per scene; the brand's layout picks (if any) come first, these fill the gaps. Geometry at 1920×1080 with the 96 px margin.

| Layout | Geometry | Fits |
|---|---|---|
| Speaker third + graphic | Speaker in 0–640 (or 1280–1920), eyes at y≈360. Graphic x 736–1824 (speaker left) or 96–1184 (speaker right), y 96–984. | Explaining a point, a stat, a list, speaker still present |
| Full cutaway | Graphic fills the frame inside the margins; voice continues | Screens, B-roll, charts |
| Corner bubble | Speaker inset 15–25% of frame (≈480×270) in a corner at the margin; graphic fills the rest | Long graphic with ongoing narration |
| Split | Speaker x 0–954, graphic x 966–1920 (or 70/30) | Comparisons, before/after |
| Shoulder panel | ≈560×315 panel on the open side, top at eye level, ≥ 48 px from the head | A quick visual, a name, a thumbnail |
| Lower third | x=96, bottom ≈950, 90–130 px tall | Naming a person, place or topic, 3–4 s |
| Words behind | One word at 12–18% frame height on the shoulder line, speaker cut out in front, ≥ 70% of it visible | Hook line, chapter title |
| Captions | y≈70–80% on 16:9; around y 1150–1400 on 9:16 | Subtitles, emphasis |
| 9:16 stack | A 16:9 screen or graphic band on top (y ~250–860), speaker below; captions around y 1150–1400, inside x 65–930 | Shorts, Reels showing a screen |
| 9:16 full face | Chest-up, eyes near y≈640, hook text above, captions below the chin | Talking Shorts |
| 9:16 corner face | Content fills the frame; the speaker's face in a corner bubble inside the safe box | Commentary over a screen or clip |
| 9:16 side column | Speaker slightly off-center, caption column in the open side (x 60–540) | Short punchy lines |

## 3. Still check (gate 2, every scene; gate 4 hunts for misses)

Answer each for every still. Any "no" is fixed before render.
1. Every text and graphic edge ≥ 96 px from the edge (16:9), or inside x 65–930, y 250–1450 (9:16)?
2. Nothing touches or overshoots an edge by accident?
3. One clearly dominant element, ≥ 2× the next?
4. The graphic is on the open side, off the face and hands?
5. No empty area over ~15% of the frame without a job?
6. Eyes at or near the top third, 5–10% head room?
7. Edges aligned to the margin, a third, the center or the eye line?
8. Display lines ≤ 30 characters, captions ≤ 42, smallest text ≥ 4% of frame height?
9. Related items closer to each other than to anything else?
10. The layout fits this shot (speaker present, gone, or in a bubble), with no empty patch where the speaker used to be?
11. On 9:16: everything inside x 65–930, y 250–1450; captions around y 1150–1400 and clear of the right rail?
12. Squint test: balanced, no heavy side, no hollow middle?

## Sources
EBU R95 safe areas (tech.ebu.ch/docs/r/r095.pdf) · 9:16 safe zones (adaptlypost.com social-media-safe-zones guide; hopperhq.com Reels size) · lead room (neiloseman.com) · interview framing (scvo.scot) · compositional balance (Smashing Magazine, 2015) · lower thirds (TechSmith; CHOP video design guidelines) · subtitle line length (subclip.app) · 9:16 creator caption columns (choppity.com). Numbers marked as defaults in the research (grid, gutters, dead-space threshold, text tiers) are starting points to tune per brand.
