# page-template

`voting-page.html` is the one page every video-genome decision page is built from. `build.py data.json out.html` fills it; `offline.py page.html out.html` inlines every image so a built page opens offline. Rules for using pages, field reference and the chat around them: `../decision-pages.md`.

`examples/` holds the model JSON for every kind of video decision (made by `gen_examples.py`, which draws every mock in code with `mocks.py`). Sample copy is universal ("I Tried It for 30 Days"); in a real run the mocks are replaced by real stills of the creator's footage or the built scene.

Word decisions are asked in chat (`../decision-pages.md`, "When to use a page"); examples marked *chat by default* are kept for creators who ask for pages.

When you copy an example for a different use, set `stage` + `stepId` (+ `journeyIf`) to where the page really sits; the right column lists the common ones. A wrong pair stops `build.py`.

| Example | Decision | Kind | stage · stepId for its uses |
|---|---|---|---|
| `brand-kits.json` | Pick an included brand kit (no kit of their own); one-option `adjust` copy = their own kit checked | Main / Backup / Alternative | start · brand |
| `intake-confirm.json` | The style of the edit, with real stills (taken items and "Your idea": chat by default) | Confirm / Change it | start · intake; build-f · direction |
| `arc.json` | *(words: chat by default)* One story layer (kind of video, script shape, arc), one option tagged "From your brief" | Main / Backup / Alternative | plan · video-type / framework / arc |
| `story-rest.json` | *(words: chat by default)* The other story layers, picked to fit, confirmed together | Confirm / Change it | plan · story-rest |
| `hooks-pick.json` (`hooks-tiles.json` first if more than 6) | *(words: chat by default)* Opening line: main + backup | (Finalist →) Main / Backup / Alternative | plan · hooks |
| `titles.json` | Thumbnail system at feed size (titles themselves: chat by default) | Main / Backup / Alternative | plan · titles / thumbnail |
| `break-from-reality.json` | Which cutaway gags to draft, each with where it lands | Draft it / Skip | plan · break-from-reality |
| `music.json` | Kind of music per part of the video | Sounds right / Change it | plan · music |
| `vertical-moments.json` | *(words: chat by default)* Which parts become Shorts | Make a Short / Skip | plan · vertical-moments |
| `motion-pack.json` (clip cards: a rendered clip over a drawn stand-in) | Motion test pack or spatial library round: which moves to keep (`../craft/spatial/README.md`) | Keep / Skip | plan · look; build-f · moments |
| `vertical-moments.json` shape, clip cards cut to the spot's length | Outtakes or reactions for one spot (`../decision-pages.md`, "Picking clips for a spot") | Keep / Skip | build-f · moments; build-g · cut |
| `moment-look.json` | What appears in one moment (with the context block) | Main / Backup / Alternative | plan · look; build-f · moments; build-g · rebuild |
| `placement.json` | Where the creator sits next to graphics | Main / Backup / Alternative | build-g · placement |
| `cut-list.json` | Judgment calls in the cut | Keep / Cut | build-f · cut; build-g · cut |
| `draft-review.json` | One still per draft scene; also the moment plan | Looks right / Change it | build-g · draft; build-f · moments |
| `brand-review.json` | Things used outside the brand | Add to my brand / Keep as one-off / Don't use again | deliver · brand-review |

`journey.json`: the visible steps of a video, matching SKILL.md's Flow. Every page's header (stage, step, % done) is computed from it. Once the order of work is picked, pages carry `journeyIf: ["graphics-first"]` or `["footage-first"]`.

`fonts/`: every font a page can use (offline woff2, free licenses), with `fonts.json` giving each one's family, weight, jobs and width `scale`. A brand font not in this list stays in the brand folder (`01 Brand Kit/fonts/`) and is passed with `fontFiles`; never swapped silently, never added to the skill folder.

**Checks `build.py` runs:** no internal labels in anything the creator reads (step or beat codes, slugs; the build stops and names them); at most one Main pick per page (one decision per page); banned words and the brand's house rules.

**Locked pages:** after the chat review, rebuild with `"locked": true` and republish to the same link.

## Clip cards (rendered motion, e.g. spatial moves)

A card can play a rendered clip: `html` = `<video src="clips/<id>.mp4" poster="clips/<id>.jpg" preload="metadata" muted playsinline style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"></video>`, `play: "playClip"`, `playMs` = clip length + 0.3 s, and once per page in `head`:
`<script>window.playClip=function(id,el){var v=el.querySelector("video");if(v){v.currentTime=0;v.play();}};window.playClipStop=function(id,el){var v=el.querySelector("video");if(v){v.pause();}};</script>`
Publish the clips and posters with the page (`files`). Clips stay small: draft quality, 15 fps, 6 s.
