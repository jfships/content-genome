# Gotchas (read before the first build of a session)

## Rendering
- Renders must finish inside the tool call that starts them. Current HyperFrames versions cancel a detached render as soon as the launching call returns (`render_cancelled_parent_exited`), even through `setsid nohup`. Keep each render inside your tool's time limit and run it in the foreground; split long renders, or use `--docker` or cloud rendering (`setup/tools.md` §2b). Set the browser path in the command: `./node_modules/.bin/hyperframes render -q standard -w 4 -o out.mp4`.
- Rough speed: a few frames a second with 4 workers, so a 4-minute draft can take ~20 minutes; on a 2-core cloud workspace a 6-second clip takes 1–1.5 minutes. Converge on stills first (`setup/tools.md` §2b).
- A render cut short is re-rendered from the start; don't trust a partial file.
- When drafts and finals run at different frame rates (15 fps draft, 30 fps final), search the code for one-frame constants written for the draft rate. A freeze that showed "the hold minus one 15 fps frame" jumped the 30 fps picture back 2 frames, and the stop landed late against its sound.
- Never kill all render processes by name; you may kill someone else's job.
- **Cutouts silently falling back to rembg.** MediaPipe 0.10.15+ dropped its old interface (`mp.solutions`), and 0.10.14 won't install on newer Python. `base.py` now uses the current interface (the selfie segmenter model, downloaded to `motion/models/`). If it ever prints `cutout: rembg`, stop and fix MediaPipe: rembg is often 10× slower.
- If the environment has a preinstalled browser, point HyperFrames and Playwright at it (`HYPERFRAMES_BROWSER_PATH=…`, Playwright `executablePath`) instead of downloading one, and pin the Playwright version that matches it.

- **An overlay that ends exactly on a cut stays up on the cut frame.** End it half a frame early (`end - 0.5/fps`).
- **Studio snapshots lag the video by one frame at cuts.** Judge cuts and overlays on `tools/comp_stills.py` stills (it sets each video's own time) and the glitch gate's strips, never on Studio stills.
- **Frame count one long** (558 where 557 were expected, 642 for 641): the renderer rounds the composition length up to whole frames, so a length written even 0.0001 s long renders one more frame (measured: 2.0 s at 30 fps = 60 frames, 2.0001 s = 61). Write `data-duration` as frames/fps rounded down to 4 decimals; the glitch gate flags it. Still check the last frame of every final. There is no 540-wide preset: render at the full size and scale the draft copy down.
- **Video clips stutter every third frame** when they start on a whole frame (WebM's millisecond frame times). Start every clip half a frame in (`shorts/build.md` "Clip timing").
- **Frame cache fills the disk** (~1.4 GB a render; renders then fail "no space left"). Before every render, check free space (at least 5 GB) and run `npx hyperframes@<version> clean` in the project when it's short; after a final is accepted, clean again.
- **iPhone HDR (HLG) footage renders pink or washed out.** Make SDR BT.709 proxies before building and render with `--sdr`: `ffmpeg -i in.mov -vf "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" -c:v libx264 -crf 16 -color_primaries bt709 -color_trc bt709 -colorspace bt709 out.mp4`. Check `color_transfer` with ffprobe first: `arib-std-b67` = HLG.
- **Rotated phone video:** read the rotation side data; a 3840×2160 file tagged 90° is portrait. Swap width and height before scaling, or stills come out squashed.
- **Phone footage frame rate:** `r_frame_rate` can read 120 while the real rate is `avg_frame_rate` (30). Read `avg_frame_rate` (the bundled tools do).

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

## Frames from the web
- Video downloaders are often blocked on a work machine. To get stills of a video without one, open it in any browser you can run scripts in, play and pause once, seek to the time, draw the video to a canvas and read the image back (1600×900 is plenty for a direction page).
- If large results get cut off or saved to a file instead of shown, return fewer frames per call and decode them from the saved file; never parse a truncated result as JSON.
- Turn autoplay off and re-check the page URL: the site starts the next video when the current one ends, and a frame grabbed after the end is the outro card.
- Stills are enough for direction pages. Real clips still need a download on the creator's computer.

## HyperFrames snapshot
- `hyperframes snapshot -o` is a directory, and `--at` takes a comma list of times. One call with all the times, not one call per time with a `.png` name.

## Fonts and libraries
- Web fonts and CDNs are often blocked. Use local `@fontsource/*` files and a local `gsap.min.js` from npm.

## Stills
- Use `tools/comp_stills.py` (never hand-write a stills script): it hides clips outside their time range, seeks videos to `data-media-start + (t − data-start)`, then `__timelines.main.seek(t)`.
- A clean-still mode (cue strip, placeholder zones and labels hidden) makes stills reusable inside the video (hook montages, thumbnails).

## Bundled talking-head tools
- No `will-change` on anything the camera scales, or the text blurs.
- Swapping text inside a morphing container needs the engine's visibility helpers, or old and new overlap.
- Keep the cursor in frame at every zoom.
- A speaker-to-side clip must start and end on the `full` box, or the cut shows.
- `base.py` processes the whole video; for quick tests, trim a section first and shift the plan times.

## Build scripts
- **A build script must never run on import.** Put everything under `if __name__ == "__main__":`. A checker that imported a build script for one constant restarted a 35-minute build and killed the running one. Checks read the build's output files (`index.html`, `timeline.json`, the mix), never the build script.
- A JavaScript error anywhere in the timeline script (one un-evaluated expression) stops the whole timeline: stills then show only frame-0 states. `comp_stills.py` stops with the page error; check after any build.

## Background jobs and transfers
- Jobs started on the creator's computer through a remote shell may die when the call ends; finish inside one call or detach them properly.
- Transfers to the creator's computer may have a per-file size cap; make a smaller review copy and keep the master where it was rendered.
- Files written to the creator's computer through a remote link can carry an extra provenance stamp (a zone marker); check that a file arrived by probing it (ffprobe, open it), not by comparing checksums.

## Cloud workspaces
- Model downloads can be blocked in a cloud sandbox (Hugging Face often is); models published on GitHub releases (Parakeet, for example) usually download.
- HyperFrames' CLI in a cloud sandbox needs `PUPPETEER_EXECUTABLE_PATH` set to the sandbox's browser.
- The high-quality cutout can run as a rented-GPU run of the same model; the local run on the creator's computer is the free fallback.

## Services
- Never print API keys. Read them from a local `.env` in the script.
- Generation endpoints often limit how many requests run at once; queue rather than fire everything, and never resubmit a request whose outcome is unknown (it may charge twice).
