# Spatial moves

Screens and words moving in 3D space: the camera flies, things sit at different depths, focus shifts, cards turn. This is the family that makes a screen demo or an explainer look like a top agency made it. It's the first place to look when a topic is hard to make entertaining without forcing a joke (the brand file's entertainment fallback, §2).

Every move below has a working source in `src/<move>/index.html`: a 6-second HyperFrames composition (1920×1080, one paused GSAP timeline, CSS 3D, no WebGL). They were built for one creator's episode and kept by that creator; the words and screens in them are examples.

## Use one

1. Copy `src/<move>/` and `src/shared/` into the episode's `work/hf/` (or link `shared` into each move folder; the linter rejects `../` paths).
2. Set the brand in `shared/base.css` `:root`: background tones, pop color, second color, pale, ink, and put the brand's display and text fonts in `shared/` as `display.woff2` and `text.woff2`. A few sources still carry one or two literal colors inside their scripts (glows, sparks); change those to the pack's colors too, then run `brand_check.py`.
3. Add `gsap.min.js` to `shared/` (from npm, never a CDN).
4. Put the real material in `assets/` as `screen-1.png`, `screen-2.png`… (and `video-frame.jpg` where a move shows a video). Use the real thing on screen (`SKILL.md` principle 6).
5. Change the words, retime the beats to the voice, then `hyperframes lint` → `snapshot --at` a few times → draft render at 15 fps → final.

## The moves

**Stock** is the move's id in the stock library (`../stock.md`), whose sample is already re-framed tall. **Tall box** is where the readable part sits in a 1080×1920 Short when the move fills the frame (see "Tall frame (9:16)" below).

| Move | Stock | What happens | Use when | Source | Tall box (full frame) |
|---|---|---|---|---|---|
| Fly through the pipeline | SPA-05 | Camera flies through a chain of screens, landing on each in turn | Showing steps that lead into each other | `fly-through-pipeline` | Chain runs into depth or down the frame, never sideways off the 1080 width; each landed screen in the hero box |
| Screen floating in space | SPA-01 | One page floats, tilted; a light sweeps the glass, words come from depth, chips pop off it | Introducing a tool or page | `floating-screen` | Page in the hero box (its phone view if it has one); words above it in y 250–330 or below in y 1350–1500; chips inside x 65–930 |
| Scroll, click, lock | SPA-12 | Camera scrolls a long page, zooms to one target, brackets lock on | Pointing at one detail on a long page | `scroll-click-lock` | Page as a column about 760 wide (x 100–860), scrolling up; the locked target ends inside the hero box |
| Exploded layers | SPA-06 | A page splits into its layers in depth, then they stack back | "What it's made of" | `exploded-layers` | Page about 700×1000 at x 140–840; layers split along depth with at most 60 px of vertical offset each, all inside y 300–1450 |
| Pipeline on a glowing floor | SPA-18 | Steps stand on a floor; light runs along a circuit between them | A process with stages | `glowing-floor-pipeline` | Floor seen from higher up so the steps climb the frame (y 500–1450); 3–4 steps |
| Rises out of the pile | SPA-11 | One thing rises out of a pile of many | The one result from a mess of inputs | `rises-out-of-pile` | Pile in y 1050–1450; the riser ends in the hero box's top part (y 300–1100) |
| Stepping orbit ring | SPA-09 | Screens on a ring turn one step per beat (never a lazy spin) | Listing parts that belong to one whole | `stepping-orbit-ring` | Ring radius at most 380 px across x; tall screens about 260×460; the front screen centered near x 500 |
| Tunnel fly-through | SPA-10 | Camera flies down a tunnel of screens | Many items, fast; a "how much there is" beat | `tunnel-fly-through` | Tunnel walls bleed past the safe box (not read); the end screen lands in the hero box |
| Fanned screens | — | Screens fan out like cards from one point | Showing a set side by side | `fanned-screens` | 3 screens at most; spread x ±250 from the center (±300 pushes the outer one past x 930) |
| Dolly zoom | SPA-08 | The subject holds its size while the world behind stretches | A surprise or "wait" beat | `dolly-zoom` | Subject in the hero box; the stretching background may fill the frame |
| Rack focus | SPA-14 | Focus moves from one depth to another | Shifting attention between two things | `rack-focus` | The 2–3 depths stack as rows down the frame, not side by side |
| Phones in a fan | SPA-04 | Phones rise and fan out in depth; the middle one comes forward | Vertical videos, apps, social posts | `phones-fan` | Native tall: middle phone about 360×740 at y 400–1140; side phones spread x ±250 |
| Dolly zoom, frames | SPA-08 | Nested frames rush outward while the screen holds | A reveal that pulls you in | `dolly-zoom-frames` | Screen in the hero box; frames may bleed past the safe box |
| Card depth stack | SPA-03 | Cards stacked in depth; the front one peels away each beat | Going through items one by one | `card-depth-stack` | Front card in the hero box; cards behind step up about 40 px each, staying above y 250 |
| Orbit ring | — | Screens orbit a title on a tilted ring; back ones blur | A hub with many parts | `orbit-ring` | Title at y 800–1000; ring radius at most 380 px across x |
| Color tunnel | SPA-24 | Frames in the brand's colors; the camera spins down to a title | Chapter openers | `color-tunnel` | The title lands inside the safe box, lines at most 860 wide |
| Parallax zoom | SPA-13 | Grid, screens and words zoom at different speeds | Adding depth to a flat moment | `parallax-zoom` | Words in y 250–700, screens below them in the hero box |
| Bokeh rack focus | SPA-14 | Lights fall out of focus as the page sharpens | Opening on a page | `bokeh-rack-focus` | Page in the hero box; lights fill the frame |
| Push into a card | SPA-02 | A grid of panels; the camera drives into one and it becomes the full view | Choosing one from many | `push-into-card` | Grid 3 across × 4 down, panels about 250×250, x 85–910, y 300–1400; the chosen panel opens to the hero box |
| 3D card flips | SPA-15 | The screen flips in 3D to the next step | Before/after, step to step | `card-flips-3d` | Card in the hero box; flip around the vertical axis so it never leaves the width |
| Real app in 3D | SPA-16 | The page tilts and its panels lift off the surface | Showing how a page is built | `app-in-3d` | Page about 700×1100 at x 140–840, y 320–1420; panels lift toward the viewer |
| Whip pan | TRN-03 | A fast sideways whip with motion blur between screens | Fast cuts between screens | `whip-pan` | Each screen in the hero box; a vertical whip works as well in a tall frame |
| 3D title opener | SPA-17 | Big extruded title flies in, turns, a glint passes | Episode or chapter title | `title-opener-3d` | 2–3 stacked lines at most 860 wide, y 500–1100 |

## Tall frame (9:16)

The sources are 1920×1080. In a Short they are re-framed, never squeezed: **port the tween numbers (depth, rotation, ease, duration, stagger), not the pixel layout,** and lay the move out again in one of two frames:
- **Full frame:** the move owns the 1080×1920 frame. Anything read sits inside the safe box (x 65–930, y 250–1500); the **hero box** for the one screen or card being read is about 760×1000 at x 100–860, y 330–1330. Dust, glow, tunnel walls and background frames may bleed past the safe box.
- **Top-half panel** (Half and half or Split top, the speaker below): the move lives in 1080×960 (or the split's band); anything read sits in x 65–930, y 250–930, nothing near the head. Scale the full-frame boxes down to fit; one screen at a time, a 16:9 screenshot at most about 860×484.

The tall boxes above are starting points worked out from the safe box; check each on a still (`hyperframes snapshot --at`) before animating, and write the box used in the beat's row.

**More in the HyperFrames registry** (search `npx hyperframes catalog --query "<move>"`, then rebuild in the brand): camera-rig-depth-stack, browser-device-stage, ui-3d-reveal, exploded-stack, parallax-device-dive, zoom-through-transition, cinematic-zoom, tracing-beam, light-sweep-pass, vfx-iphone-device, vfx-portal, glass-hero. About half of the catalog demos don't render offline (pages inside pages, CDN fonts, WebGPU) and some show blank placeholders: treat them as references to rebuild, not finished pieces.

**Other sources worth checking each time** (new ones appear monthly): HyperFrames' own launch films (creativeclaw.co motion-design collection) as the quality bar; charlie947/motion-graphics-skills; VisualxIntelligence/motion-tools-and-skills (film-style prompts and a study of agent-made videos); Claude Motion; real 3D scenes through a 3D tool (costs credits; ask first).

**Tried and skipped by the first creator** (taste, not quality; offer them to others): words on a tilted track, isometric blocks, dark keynote reveal, hologram projection, paper pop-up.

## Rules (from HyperFrames' product-launch-video skill and our own tests)

- Smooth long-tail easing (power3/expo out). No bounce, no elastic.
- Reveal on the voice: each thing appears on the word that names it; the big reveal lands in the back half of the line.
- Nothing drifts or "breathes" while nothing is being said about it. Every move is a step with a reason.
- Cuts between spatial shots match speed: the outgoing move's velocity carries into the next. Motion blur scales with the subject: about 10px for words, 18–20px for whole screens.
- No `repeat`/`yoyo`, no `Math.random`; entrances use `fromTo`.
- Depth needs three layers (background, subject, foreground detail); one flat plane in 3D still reads as a slide.
- Build gotchas for 3D are in `setup/gotchas.md` ("3D scenes").
