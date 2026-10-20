# Spatial moves

Screens and words moving in 3D space: the camera flies, things sit at different depths, focus shifts, cards turn. This is the family that makes a screen demo or an explainer look like a top agency made it, and the usual fallback when a topic is hard to make entertaining without forcing a joke (Stage 1b). Stage 5c shows these as rendered clips; video-genome uses the same sources when it builds.

Every move below has a working source in `src/<move>/index.html`: a 6-second HyperFrames composition (1920×1080, one paused GSAP timeline, CSS 3D, no WebGL). They were built for one creator's episode and kept by that creator; the words and screens in them are examples.

## Use one

1. Copy `src/<move>/` and `src/shared/` into a working folder (link `shared` into each move folder; the linter rejects `../` paths).
2. Set the brand in `shared/base.css` `:root`: background tones, pop color, second color, pale, ink, and put the brand's display and text fonts in `shared/` as `display.woff2` and `text.woff2`. A few sources still carry one or two literal colors inside their scripts (glows, sparks); change those to the pack's colors too,
3. Add `gsap.min.js` to `shared/` (from npm, never a CDN).
4. Put the creator's real screens in `assets/` as `screen-1.png`, `screen-2.png`… (and `video-frame.jpg` where a move shows a video). No screens yet → neutral stand-ins drawn in code, labeled as stand-ins on the page.
5. Change the words to the creator's, then `npx hyperframes lint` → `snapshot --at 3` → `render -q draft -f 15 -o clip.mp4`, plus a poster still for the card.

## The moves

| Move | What happens | Use when | Source |
|---|---|---|---|
| Fly through the pipeline | Camera flies through a chain of screens, landing on each in turn | Showing steps that lead into each other | `fly-through-pipeline` |
| Screen floating in space | One page floats, tilted; a light sweeps the glass, words come from depth, chips pop off it | Introducing a tool or page | `floating-screen` |
| Scroll, click, lock | Camera scrolls a long page, zooms to one target, brackets lock on | Pointing at one detail on a long page | `scroll-click-lock` |
| Exploded layers | A page splits into its layers in depth, then they stack back | "What it's made of" | `exploded-layers` |
| Pipeline on a glowing floor | Steps stand on a floor; light runs along a circuit between them | A process with stages | `glowing-floor-pipeline` |
| Rises out of the pile | One thing rises out of a pile of many | The one result from a mess of inputs | `rises-out-of-pile` |
| Stepping orbit ring | Screens on a ring turn one step per beat (never a lazy spin) | Listing parts that belong to one whole | `stepping-orbit-ring` |
| Tunnel fly-through | Camera flies down a tunnel of screens | Many items, fast; a "how much there is" beat | `tunnel-fly-through` |
| Fanned screens | Screens fan out like cards from one point | Showing a set side by side | `fanned-screens` |
| Dolly zoom | The subject holds its size while the world behind stretches | A surprise or "wait" beat | `dolly-zoom` |
| Rack focus | Focus moves from one depth to another | Shifting attention between two things | `rack-focus` |
| Phones in a fan | Phones rise and fan out in depth; the middle one comes forward | Vertical videos, apps, social posts | `phones-fan` |
| Dolly zoom, frames | Nested frames rush outward while the screen holds | A reveal that pulls you in | `dolly-zoom-frames` |
| Card depth stack | Cards stacked in depth; the front one peels away each beat | Going through items one by one | `card-depth-stack` |
| Orbit ring | Screens orbit a title on a tilted ring; back ones blur | A hub with many parts | `orbit-ring` |
| Color tunnel | Frames in the brand's colors; the camera spins down to a title | Chapter openers | `color-tunnel` |
| Parallax zoom | Grid, screens and words zoom at different speeds | Adding depth to a flat moment | `parallax-zoom` |
| Bokeh rack focus | Lights fall out of focus as the page sharpens | Opening on a page | `bokeh-rack-focus` |
| Push into a card | A grid of panels; the camera drives into one and it becomes the full view | Choosing one from many | `push-into-card` |
| 3D card flips | The screen flips in 3D to the next step | Before/after, step to step | `card-flips-3d` |
| Real app in 3D | The page tilts and its panels lift off the surface | Showing how a page is built | `app-in-3d` |
| Whip pan | A fast sideways whip with motion blur between screens | Fast cuts between screens | `whip-pan` |
| 3D title opener | Big extruded title flies in, turns, a glint passes | Episode or chapter title | `title-opener-3d` |

**More in the HyperFrames registry** (search `npx hyperframes catalog --query "<move>"`, then rebuild in the brand): camera-rig-depth-stack, browser-device-stage, ui-3d-reveal, exploded-stack, parallax-device-dive, zoom-through-transition, cinematic-zoom, tracing-beam, light-sweep-pass, vfx-iphone-device, vfx-portal, glass-hero. About half of the catalog demos don't render offline (pages inside pages, CDN fonts, WebGPU) and some show blank placeholders: treat them as references to rebuild, not finished pieces.

**Other sources worth checking each time** (new ones appear monthly): HyperFrames' own launch films (creativeclaw.co motion-design collection) as the quality bar; charlie947/motion-graphics-skills; VisualxIntelligence/motion-tools-and-skills (film-style prompts and a study of agent-made videos); Claude Motion; real 3D scenes through a 3D tool (costs credits; ask first).

## Real 3D (Three.js), the second round

CSS 3D moves above are flat layers posed in space. Some looks need a real 3D renderer: glass that bends light, particles, liquid surfaces, a wireframe drawing itself, bars as solid blocks, a screen burning away. Render them with Three.js in a headless browser (Playwright/Chromium with the software GPU flags `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`), frame by frame into ffmpeg: no GPU and no HyperFrames needed, about 1–2 minutes per 6-second draft at 1280×720, 15 fps. Run it where there is room (a cloud workspace is fine; clips come back at under 1 MB each).

| Move | What it shows | Use when | Slug |
|---|---|---|---|
| Glass box | A rounded glass cube with the subject inside; the background bends through it | One idea or object made precious | `glass-box` |
| Glass layers fly-through | Camera passes through a stack of glass panes, one screen each | Steps or layers of a process | `glass-stack` |
| Floating slab | A thick white screen turns in space, a light sweeps it, chips with words lift off | Introducing a tool or result | `floating-slab` |
| Particles form the words | Thousands of dots gather into the mark, a sphere, then a word | Opener or reveal | `particle-morph` |
| Blueprint build | Boxes draw themselves as wireframe on a grid, fill in, link up, get labels | How something is put together | `blueprint-build` |
| 3D bar wave | A field of solid bars ripples, then settles into the chart with the winner in the pop color | A number or trend | `bar-wave` |
| Liquid blobs | Ray-marched blobs in the pop color merge and split | Mood beat or background | `liquid-blobs` |
| Screen burns into dust | A screen burns away along a noise edge into sparks; the next screen forms | Scene change, "it's gone" | `dissolve` |
| Hologram phone | A see-through phone scans in over glowing rings | Product or app reveal | `hologram-phone` |

Rules that held in the first run: give every basic (unlit) material `toneMapped:false` or the brand colors drift; with bloom, keep white UI below the threshold (scale the texture to about 0.8, threshold 1.0) or the whole screen blooms; ray marching renders at half size and scales up; draw stand-in screens in code and label them as stand-ins. The page is built like any other library page with clip cards (`page-template/README.md`). Keep the source next to the clips with a one-line re-render command so the library can be regenerated at final quality.

**Tried and skipped by the first creator** (taste, not quality; still offer them): words on a tilted track, isometric blocks, dark keynote reveal, hologram projection, paper pop-up.

## Rules (from HyperFrames' product-launch-video skill and our own tests)

- Smooth long-tail easing (power3/expo out). No bounce, no elastic.
- Reveal on the voice: each thing appears on the word that names it; the big reveal lands in the back half of the line.
- Nothing drifts or "breathes" while nothing is being said about it. Every move is a step with a reason.
- Cuts between spatial shots match speed: the outgoing move's velocity carries into the next. Motion blur scales with the subject: about 10px for words, 18–20px for whole screens.
- No `repeat`/`yoyo`, no `Math.random`; entrances use `fromTo`.
- Depth needs three layers (background, subject, foreground detail); one flat plane in 3D still reads as a slide.
- Build gotchas: a CSS `filter` on a 3D parent flattens it (blur only the flat screen inside); opacity on a `preserve-3d` parent flattens it too (fade the faces); a `fromTo` placed later shows its start state at time 0 unless `immediateRender:false`; tilted screens cut through flat words in the same space (put words in their own layer); tween `y`, never `top`.
