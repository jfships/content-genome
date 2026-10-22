# The live picker

One page per video, for every visual decision that has to be seen moving. Every option plays the real HyperFrames edit on the creator's own footage, on top of everything already picked; the page's preview is the video as decided so far. What the creator picks is exactly what renders, because the page and the render assemble the edit with the same file (`compose.js`). When and why to use it: `../decision-pages.md`, "The live picker".

## Files

| File | Does |
|---|---|
| `compose.js` | Assembles the edit from a base composition plus one option per row. The page inlines it; `node compose.js spec.json picks.json <hf>/index.html` writes the edit that renders. |
| `picker.html` | The page template (tabs, rows, live cards, preview, saving). |
| `build.py` | `python3 build.py picker.json <out_dir>`: checks the picker, makes caption options from word timing, writes `index.html`, `spec.json` and copies of the HyperFrames project's `assets/` and `fonts/`. |

## How a video's edit is split

- **Base composition** (`base.html`, in the video's `work/picker/`): the HyperFrames project's `index.html` with everything a decision changes taken out, and three markers put in: `/*@css*/` inside `<style>`, `<!--@html-->` inside the root element, `/*@js*/` after `const tl = gsap.timeline(...)` and before the timeline is registered. What stays: footage, voice, sound, anything already settled.
- **Rows**: one decision each. A row's options are fragments: a file with an optional `<style>`, the clip elements, and an optional `<script>` of `tl.` lines (or inline `css` / `html` / `js`). Options in different rows must not reuse element ids. Every asset an option uses lives in the HyperFrames project's `assets/`, so the render finds it too.
- A row with no pick uses its `default` (the current version), so the preview and the render always play a whole video.

## picker.json

```
title, video        page title; eyebrow line (plain words)
store               short name for the saved picks (e.g. "ep07")
round               which round of decisions this is (1, 2, 3 …); rows added later carry their round and show "New"
hyperframes         the HyperFrames version the project renders with; the page loads that version's player
hf, base, words     the HyperFrames project folder, the base composition, word timing (words_out.json shape: w, t0, t1)
keyWords            words the caption styles color
tabs                [{id, name, ask}] in order: look, beats, then fixes, sound, thumbnail as their steps come; "Watch" is added at the end
rows                [{id, tab, name, short, ask, span:[t0,t1], default, dependsOn:[rowIds], global, round, options:[…]}]
options             [{id, name, feel, pick, why, hideCaptions, src | css/html/js | captions:{mode, maxWords, track}}]
heading, lede, watchNote, locked   optional page copy; locked: true shows picks read-only
```
- `span`: the stretch each card loops. For a beat, the beat's own time; for a look row, a stretch that shows the look (captions: a captions-only stretch).
- `captions` on an option generates the caption clips from `words`: `mode` "pair" (2–3 words), "word" (one at a time) or "line" (a short line, stacked by the option's CSS). The option's `css` styles `.cap`, `.cap span`, `.cap i` and `.cap i.k` (key words). Each caption clip carries the beat it falls in, so a beat option with `hideCaptions: true` hides that beat's captions.
- `dependsOn`: when one of those rows changes, this row is marked "Check again" (never silently kept or wiped).
- `pick: true` + `why`: "Our pick" on one option per row at most.
- A look row (or `global: true`) affects the whole video; changing it reloads every card on screen. A beat row reloads only cards whose span overlaps it.

## Round trip

1. Build, then publish `index.html` as a private artifact with `capabilities: {db: {}}`, `root` = the out dir and the printed file list as `files`. Same file path on every rebuild, so the link never changes.
2. The page saves each pick as a document in the `picks` collection, id = row id: `{pick (null = undone, the row plays its default), status ("picked" | "check"), round, offered, notes: {optionId: text}, at}`. Read it back with the artifact data tool (`list`, collection `picks`); read only what changed since the last read (`at`), and act on every note.
3. Write `plan.md` from it: one line per row, "Opening line: Two-tone stack (also offered: Color blocks, Captions only) · round 1".
4. Write `picks.json` (`{rowId: optionId}`), then `node compose.js <out_dir>/spec.json picks.json <hf>/index.html` and render the draft as usual. Before showing the draft, snapshot the render and the page's preview at the same times; they should match (the only difference is the player's control bar).
5. A later round edits the same `picker.json`: add rows with the new `round` (and a new tab when its step comes), rebuild, republish to the same link. Earlier picks stay in the store and on the page.
6. If the creator can't use the page's saving (signed out), "Copy my picks" gives the same `{rowId: optionId}` to paste in chat.

## Limits

- Each card is a live player, paused on a frame of its moment until the creator presses play; one plays at a time. The page loads only cards near the screen. Keep a row to 2–4 options.
- Tapping a picked option again undoes the pick. Every option takes a note.
- The page's footage must match the base composition's timing. If the video is re-cut, rebuild the picker from the new edit; don't republish new footage under old timings.
- Artifact files: 15 MB per file, 16 MB for the page. A long video's footage over 15 MB goes in as a draft-quality copy for the page; the render keeps the real one.
- The player loads its runtime from jsDelivr (on the artifact allowlist), pinned to `hyperframes`.
