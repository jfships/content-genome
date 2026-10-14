# page-template

`voting-page.html` is the one page every brand-genome round is built from; `genome-page.html` is the Brand Genome page (Stage 9), chosen by `"page": "genome"` in the data. `build.py data.json out.html` fills it; `offline.py page.html out.html` inlines every image so a built page opens offline (used for `Brand Genome (visual).html`). Field reference and page rules: `../voting-pages.md`.

`examples/` holds the model JSON for every page (Look, Movement, Sound, Kit, Vertical, change mode and the Brand Genome page), made for a demo creator named Wren. Fixed steps come in pairs, `<step>-tiles.json` (finalists) → `<step>-pick.json` (Main / Backup / Alternative / Discard), all made by one shared function, `finalist_flow`, in `gen_examples.py`, so every fixed step behaves the same. Card copy is universal (the 30-day-test sample set); the creator's niche lives in chat only. `python3 gen_examples.py` regenerates them. Desktop and phone screenshots are kept outside the skill, in `04 Free Tools\brand-genome previews\`.

Images in the examples are referenced as `img/<benchmark file>`, `img/looks/<slug>.jpg`, `img/bfr/<slug>.jpg` and `img/backdrops/<slug>.jpg`; copy the ones a page uses next to the built page (or map them in the artifact's `files`).

`fonts/`: every font a page can use (offline woff2, free licenses), with `fonts.json` giving each one's family, weight, jobs (title / text / notes), tier and width `scale`. `journey.json`: the visible stages and steps, and which steps can be skipped; every page's header is computed from it.

**Change mode:** add `"change": "<decision>"` to any page and `"current": true` to the creator's current pick (`examples/change-palette-tiles.json`); see `../revisit.md`.

**Locked pages:** after the chat review, rebuild with `"locked": true` and republish to the same link.

## Clip cards (rendered motion, e.g. spatial moves)

A card can play a rendered clip: `html` = `<video src="clips/<id>.mp4" poster="clips/<id>.jpg" preload="metadata" muted playsinline style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"></video>`, `play: "playClip"`, `playMs` = clip length + 0.3 s, and once per page in `head`:
`<script>window.playClip=function(id,el){var v=el.querySelector("video");if(v){v.currentTime=0;v.play();}};window.playClipStop=function(id,el){var v=el.querySelector("video");if(v){v.pause();}};</script>`
Publish the clips and posters with the page (`files`). Clips stay small: draft quality, 15 fps, 6 s.
