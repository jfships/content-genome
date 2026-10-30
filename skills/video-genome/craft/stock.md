# Stock library: picking, restyling and growing it

The stock library is a set of neutral samples (gray plus one accent, a stand-in presenter), one per visual device, each with a **stock id** such as `LAY-03`, `PROP-01`, `SPA-02`, `COV-05`. The creator picks from samples by watching them, never from names. The id prefixes are categories: LAY layouts · PROP look-real props · POP pop-ins · SCR screen proof · SPA 3D moves · CAM camera on the person · TRN transitions · CUT cuts and pacing · STO story devices · CAP captions · HOOK hook text · COV covers (plus later BKD backdrops, BIG set pieces, SND sounds, MAP places, TEX textures).

**Where it is.** `stock/manifest.json` in the creator's tools folder (wherever the brand files point to it). The manifest is the source of truth: for each id it lists name, category, tier (core / later / funky), source and render path. An id appears in this skill's tables (`graphics-library.md`, `shorts/build.md` "Layouts", `spatial/README.md`) whether or not a sample is built yet; only ids in the manifest have one. No stock library at all: pick from `graphics-library.md` by name as before.

## Picking by id

1. For each beat, read its job (`graphic-jobs.md`), then list 2–3 candidate ids from the manifest that can do that job, ranked, one reason each. Read the brand's style ledger and its swipe library "Visual devices" first: ids the creator kept rank up, ids they dropped are out.
2. Write the picked id in the beat brief's "Device (source)" cell as `stock <id>`; a device made for this video is `new`, a paid image or clip `generated`.
3. When the beat is a real choice, the picker row plays the candidates' samples restyled to the brand (below), one pick per row. The answer is recorded as `id → keep / drop / note`.

## Restyling a sample to the brand

A sample reads all its colors, fonts and fixed words from one brand file: `stock/brands/<brand>/brand.css` (copied from `stock/brands/neutral/brand.css`, same variable names, the brand's fonts in its `fonts/`). To restyle, point the sample at the brand's file and re-render; change nothing else in the sample. A brand with no brand file yet gets one made from its brand file's packs (colors, title/text/caption/note fonts, caption weight, size and case) before the first picker.

For the build, copy the sample's source into the video's `hf/`, keep the brand file link, then swap in the real material and the beat's words and retime to the voice.

## New builds become stock (standing rule)

Nothing built for one video stays one-off, and nothing from outside enters a library without its sample.
- **At close-out** (`review/session-close.md` 2c), list every beat whose device source was `new` or `generated`. For each: either it matches an existing id (note "first used in <video>" in the brand's ledger), or it gets a new id in its category, a plain name, a tier, and a **neutral stock version** built from the video's own source: brand file swapped to neutral, the creator swapped for the stand-in, real words and screens swapped for neutral ones. Add it to the manifest with its render path.
- **Outside inspiration** (a saved Reel, a registry piece, another creator's move) maps to an existing id or gets a proposed new id plus a sample brief. It is held, unused in any brand list, until its sample is built and in the manifest.
- Every new entry carries the mechanics `SKILL.md` principle 18 requires (trigger, timing and placement, pairs and clashes, fails when) in the row of the library table it joins.
