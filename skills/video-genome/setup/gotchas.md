# Gotchas (read before the first build of a session)

## Rendering
- Long renders must survive the tool call that starts them. Launch through a wrapper script, detached: `setsid nohup bash render.sh out.mp4 > render.log 2>&1 < /dev/null & disown`. `render.sh` sets the browser path and runs `./node_modules/.bin/hyperframes render -q standard -w 4 -o "$1"`. Launching `npx` directly in the background gets cancelled when the call returns. Poll the log.
- Rough speed: a few frames a second with 4 workers, so a 4-minute draft can take ~20 minutes; on a 2-core cloud workspace a 6-second clip takes 1–1.5 minutes. Converge on stills first (`setup/tools.md` §2b).
- A render launched from a process that exits gets cancelled; detach it (above) and re-render anything cut short.
- Never kill all render processes by name; you may kill someone else's job.
- If the environment has a preinstalled browser, point HyperFrames and Playwright at it (`HYPERFRAMES_BROWSER_PATH=…`, Playwright `executablePath`) instead of downloading one, and pin the Playwright version that matches it.

## HyperFrames compositions
- One root `index.html` per folder. Any other `.html` with `data-composition-id` in the folder (sources, old drafts, installed registry components) causes a "multiple roots" error. Keep sources in `src/` and generate `index.html` with a build script. Move installed registry components out after copying what you need.
- Inline the timeline script in `index.html` (the linter can't see a `<script src>` registration). Add `window.__timelines = window.__timelines || {}` so plain-Playwright stills work.
- A `<video data-start>` can't sit inside an element that also has `data-start`: put footage at root level as its own clip.
- **clip-path counts as a heavy overlay;** around 40 of them (hidden ones included) can render black frames. Do mask reveals with `overflow:hidden` plus an inner wrapper moving by `yPercent`, and typewriters with character spans, not clip-path.
- Tween x/y, not left/top. Use opacity, not visibility, for hidden clips. Use tweens, not `tl.call`. Use `fromTo` to avoid transform conflicts. No cubic-bezier string eases without CustomEase.
- Audio levels and fades: volume automation lanes on each `<audio>` (every `<audio>` needs an `id`). Convert mp3 to 48 kHz WAV first.

## 3D scenes (spatial moves)
- A CSS `filter` (blur) on a 3D parent flattens it and hides children positioned outside its box. Blur only the flat screen inside it.
- `opacity` below 1 on a `preserve-3d` parent also flattens it (a cube becomes a flat square). Fade the faces, not the parent.
- A `fromTo` placed later in the timeline shows its start state at time 0. Add `immediateRender:false` and set the element hidden with `gsap.set` at 0.
- Tilted 3D screens cut through flat words that share their space. Put words in their own layer, outside the 3D stage.
- Building a box: set each face's rotation with `gsap.set` (rotationX/rotationY) and the right `transformOrigin`; CSS transforms written by hand get overwritten by GSAP.
- Tween `y`, never `top` (the linter flags non-transform motion).
- Shared files: link a `shared/` folder into each composition folder; the linter rejects `../` paths.

## HyperFrames registry demos
- About half of the catalog demos fail offline (pages embedded in other pages, CDN fonts and scripts, WebGPU shaders), and some that render show blank placeholders. Use them as references to rebuild in the brand, not as finished pieces.

## Fonts and libraries
- Web fonts and CDNs are often blocked. Use local `@fontsource/*` files and a local `gsap.min.js` from npm.

## Stills
- Hide clips outside their time range, seek videos to `data-media-start + (t − data-start)`, then `__timelines.main.seek(t)`.
- A clean-still mode (cue strip, placeholder zones and labels hidden) makes stills reusable inside the video (hook montages, thumbnails).

## Bundled talking-head tools
- No `will-change` on anything the camera scales, or the text blurs.
- Swapping text inside a morphing container needs the engine's visibility helpers, or old and new overlap.
- Keep the cursor in frame at every zoom.
- A speaker-to-side clip must start and end on the `full` box, or the cut shows.
- `base.py` processes the whole video; for quick tests, trim a section first and shift the plan times.

## Background jobs and transfers
- Jobs started on the creator's computer through a remote shell may die when the call ends; finish inside one call or detach them properly.
- Transfers to the creator's computer may have a per-file size cap; make a smaller review copy and keep the master where it was rendered.

## Services
- Never print API keys. Read them from a local `.env` in the script.
- Generation endpoints often limit how many requests run at once; queue rather than fire everything, and never resubmit a request whose outcome is unknown (it may charge twice).
