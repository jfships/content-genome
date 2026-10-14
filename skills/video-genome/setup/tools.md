# Step 0: Load, set up, update

Do this at the start of every video, before any plan or code. The brand file comes first (`setup/brand-intake.md`), then this file, then intake (`plan/intake.md`). Open the session by naming the step: "Start · your brand".

## 1. Load the brand

- Find the brand folder (`SKILL.md`, "Brand folder and where to look") and read `START-HERE.md` `## Videos`.
- Read the brand file in full (`Brand Genome.md` or `Brand Sheet.md`; none → `setup/brand-intake.md` first), then the identity doc it links, if any (`Who I Am.md`), then the Idea Record (`idea.md` in the episode, or the `04 Ideas/` record being started), then the episode's plan and `debt.md` if they exist, then `03 Videos/results-log.md`. Where two docs disagree, the newer one wins; say which you followed.
- Pull these into working memory for the whole episode:
  - the content personality (ranked)
  - truth rules and Proof
  - the format this episode uses
  - the packs (main and backup kit, for a Sheet made from included kits)
  - the motion table
  - the sound lanes and phrase length
  - kit placements and timings
  - the vertical rules
  - the voice kit
  - the break-from-reality bank
  - the run sheet
  - house rules
- **Demo creators:** if the brand says `mode: demo`, answer creator questions as the persona card in the brand, mark answers `answered_by: persona`, and let the operator veto. Use only the card's fictional Proof. A made-up creator can't film, so pick one with the operator (AskUserQuestion) before planning:
  - **Voice-only, graphics-led** (Recommended, free): Order A without a face; the narration is a generated voice described from the persona card (never imitating a real person). Placement: voice only.
  - **Avatar:** an avatar or video tool animates the persona's face references from the brand, speaking the cut script. Show the cost first. Label it as AI-generated everywhere it's posted.
  - **Operator stands in:** the operator records the lines; the persona stays the brand.
  In every case the result is labeled as a demo with a fictional creator.
- Brand assets (sound logo, SFX, page sources, fonts) live in `01 Brand Kit/`; everything else reusable lives in `07 Asset Library/` (`craft/asset-library.md`). Reuse their code and files; never redraw a kit component from memory.

## 2. HyperFrames: fetch fresh, check for updates

HyperFrames (HTML + GSAP compositions rendered to video, by HeyGen) is the main build tool. It changes often, so it's fetched each run, never bundled.

- **Use the local CLI** (`npx hyperframes`). The hosted "HyperFrames by HeyGen" connector is a different product (hosted projects); don't use it to build.
- **Get its craft skills.** If `hyperframes`, `hyperframes-core` and so on appear in this session's skill list, invoke them. Otherwise read them from the repo, skills only (a full clone is slow):
  `git clone --depth 1 --filter=blob:none --sparse https://github.com/heygen-com/hyperframes ~/hf && cd ~/hf && git sparse-checkout set skills`
  Run it wherever GitHub is reachable (the cloud, or the creator's computer).
- **Update check, every video:**
  - `npx hyperframes@latest upgrade --project . --check`
  - `npx hyperframes --version`, and `npx hyperframes usage --json` (report "unknown" if either fails)
  - Write the version and date in the episode log. If the version changed since the last episode, skim the changelog or release notes for breaking changes and **say so before building**.
- **Required reading, in order:**
  1. `hyperframes`: the front door.
  2. `general-video`: the workflow for long, multi-scene pieces. Follow its production loop: blocks and assets → audio → frames → assembly → verify.
  3. `hyperframes-core`: composition rules.
  4. `hyperframes-cli`: `check` (the gate before any render), `snapshot`, `timeline`.
  5. `hyperframes-animation`: motion rules, scene blueprints, transitions.
  6. `hyperframes-creative`: its house style and video composition notes (scale, depth, density).
  7. `motion-graphics`.
  8. `hyperframes-registry`: search `npx hyperframes catalog --query "<the move in plain English>"` **before** hand-building any named look; install with `npx hyperframes add <name>` and reuse its code.
  9. `hyperframes-audio`: mixing, ducking, groups, carve.
  10. `media-use`: SFX library, music, grades.
  11. `hyperframes-keyframes`: zoom, punch and pan on footage.
  12. `embedded-captions`.
  13. `talking-head-recut`: patterns for laying graphics over a person.
  14. `product-launch-video`: the motion doctrine behind HyperFrames' own launch films (long-tail easing, reveals timed to the voice, no lazy drift, velocity-matched cuts). It's the quality bar for anything spatial; its rules are summarized in `craft/spatial/README.md`.
  15. The registry's spatial pieces, by name: camera-rig-depth-stack, browser-device-stage, ui-3d-reveal, exploded-stack, parallax-device-dive, zoom-through-transition, tracing-beam, light-sweep-pass, vfx-iphone-device, vfx-portal, glass-hero. Look at them before planning any screen demo.

  If a skill name no longer exists, find its replacement in the repo's skills list.
- The brand overrides HyperFrames defaults on colors, fonts and motion vocabulary.

## 2b. Render capacity: say it up front

Rendering is the slow part. Before planning, measure and say it in one line: "Renders here take about N minutes per 6-second clip; a test pack of 12 is about M minutes."
- Time one short draft (`render -q draft -f 15`) on the machine that will render. A small cloud workspace (2 cores, no graphics card) renders roughly 1–1.5 minutes per 6-second clip; a creator's own computer is often several times faster.
- Draft menus and test packs at 15 fps; render finals one at a time.
- **When renders will be long** (a test pack over ~20 clips, or a full episode), offer HyperFrames' cloud rendering (AWS Lambda or Google Cloud Run, from its docs) as a one-time setup, with its cost, or rendering on the creator's computer. Ask once; save the answer in the brand file's Creator section (tools and budget).

## 3. Bundled tools and folders

**Paths.** `$SKILL` = this skill's folder. All script paths in this skill are relative to it (e.g. `$SKILL/tools/grade.py`). Each episode works inside its own folder (see `SKILL.md`). The talking-head engine expects a `motion/` folder inside the episode's `work/`:
```
EP NN <name>/work/
  source.mp4          ← raw take(s)
  cut.mp4             ← the approved cut (plan.json "video" points here)
  words.json          ← transcript of the raw take
  cutlist.json        ← kept spans [[in, out], ...]
  words_out.json      ← word times on the cut ($SKILL/tools/remap_words.py)
  motion/             ← plan.json, clips/, dist/, out/, brand/, inputs/, models/
  hf/                 ← HyperFrames project for full-graphic scenes
```

**Brand → engine brand.** Before building any engine clip, write `motion/brand/brand.json` from the brand's pack:
| Engine key | From the brand |
|---|---|
| `canvas` | the pack's dark (or light, for light packs) background |
| `surface`, `inset`, `line` | 1, 2 and 3 steps lighter (dark packs) or darker (light packs) than canvas |
| `ink` | the pack's light/text color |
| `muted`, `faint` | ink at ~65% and ~45% toward canvas |
| `accent`, `accentSoft` | the pack's accent; accentSoft = accent at 18% opacity |
| `ok`, `warn`, `bad` | the pack's extra colors if it has them, otherwise keep the defaults |
| `fonts.display` / `fonts.ui` / `fonts.mono` | headline / text / notes font files from the pack |
The engine animates with springs. Match the brand's motion feel: Snap/Punch → stiff springs with no overshoot; Glide/Drift/Editorial → softer, slower springs, no overshoot; Playful → allow the small overshoot; Deadpan/Mechanical → use stepped text reveals and short, stiff springs. Pass `--brand motion/brand/brand.json` to `captions.py` so captions use the pack's fonts and accent.

**Grading footage.** `python3 $SKILL/tools/grade.py recipe.json in.mp4 out.mp4` applies the brand's grade recipe (shadow tint, highlight tint, saturation, contrast, grain, vignette). Grade the cut before the base treatment, so everything downstream uses graded footage.

**Talking-head tools.**

`tools/talking-head/` has the scripts for transcription, inspection, cutout, background blur and zooms, speaker-to-side frames, captions, compositing and thumbnails, plus a small motion engine. First run:
`bash $SKILL/tools/talking-head/scripts/setup.sh work/motion`
It needs Node 18+, Python 3 and ffmpeg (with prores_ks and libass). It installs Playwright + Chromium and the Python packages (numpy, opencv, mediapipe, fonttools, sherpa-onnx, faster-whisper). Run engine scripts with `NODE_PATH=./motion/node_modules`. On Windows, use Git Bash; if `python3` is missing, use `python`. Full reference: `tools/talking-head/README.md` and `tools/talking-head/reference/`.

## 4. Optional services (from the brand's Creator section: tools and budget)

- **Music, sound effects, narrator voices:** e.g. ElevenLabs (API or connector). Keep the API key in a local `.env` file that a script reads; never print it, never paste it into chat.
- **Images and video clips:** e.g. Higgsfield, Black Forest Labs, Runway. Follow the brand's image rules (brief approved first, likeness references, log every round).
- **Transcription:** the bundled `transcribe.py` (faster-whisper; Parakeet as a fallback when Hugging Face is blocked). Word times are accurate to about ±0.05 s. Pass the brand's content language (`--lang es`, etc.); the Parakeet fallback is English-only, so for other languages faster-whisper must be reachable.

## 5. Plumbing check (once per session)

Test each service the episode needs with its cheapest read-only call (version, list models, balance), from where the work will run. Fonts and script libraries come from npm (`@fontsource/*`, `gsap`) as local files, because web font and CDN links are often blocked. List anything blocked and the domain to allow before planning.
