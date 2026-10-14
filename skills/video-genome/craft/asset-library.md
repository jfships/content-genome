# Asset library (one per brand)

Every reusable file the brand owns lives in `<Brand>/07 Asset Library/`, indexed in `asset-index.md`. Episodes point at library IDs; they don't keep private copies of reusable things. Before anything is generated, shot or built, the library is checked (`plan/asset-debt.md`).

```
07 Asset Library/
  asset-index.md        ← one row per asset; the only place to search
  footage/              ← camera takes, B-roll, real places and objects
  screens/              ← screenshots, screen recordings, app and page captures
  images/               ← photos, generated stills, plates, backgrounds
  people/               ← likeness references and approved avatar/face refs
  audio/
    music/  sfx/  voice/ ← licensed or generated music, effects, voice takes and clones' outputs
  scenes/               ← code-built reusable scenes and clips (HyperFrames blocks, engine clips) with their source
  graphics/             ← lower thirds, overlays, icons, charts built for this brand
  docs/                 ← receipts, documents, proof artifacts (private data blurred copy alongside)
```

Brand components (wordmark, sting, sound logo, end card, page sources) stay in `01 Brand Kit/`; the index lists them too, with `type: kit`, so one search finds everything.

## asset-index.md

| ID | Type | File | Origin | Tool / cost | Rights | Tags | Used in | Added |
|---|---|---|---|---|---|---|---|---|
| A0001 | footage | footage/2026-10-07-kitchen-wide.mp4 | uploaded | — | creator-owned | kitchen, wide, day | EP 01 | 2026-10-07 |

- **ID:** `A` + 4 digits, never reused.
- **Type:** footage · screen · image · person · music · sfx · voice · scene · graphic · doc · kit.
- **Origin:** uploaded (creator gave it) · generated (a tool made it) · built (code made it) · licensed.
- **Tool / cost:** for generated and licensed items, the tool and what it cost.
- **Rights:** creator-owned · generated (note tool terms) · licensed (license name, platforms) · permission (who, when). Unknown rights block use in a final.
- **Tags:** plain words a search would use (place, object, mood, person, shot size, orientation 16:9 / 9:16).
- **Used in:** episode numbers.

## Rules

- **Search before making.** For every debt item, search the index by type and tags. A match within reason (right subject, right orientation, good enough) is reused and the debt item closes as `reused A0123`.
- **File it when it's made.** Anything an episode produces that could serve another video (a generated plate, a built scene, a clean B-roll shot, a voice line, a screenshot of the real product) is moved into the library and indexed in the same turn. One-off pieces stay in the episode's `work/`.
- **Name files** `YYYY-MM-DD-<what>-<detail>.<ext>`, lowercase, hyphens.
- **Never overwrite.** A better version is a new ID; the old row notes `superseded by A0456`.
- **Big raw footage** can live on an external drive: index it with its drive path and mark `offline`.
- **Masters on the computer.** The project never holds media; it holds a copy of `asset-index.md` only.
- **Privacy.** Customer names, faces, phone numbers and financial details in screens or docs get a blurred copy; only the blurred copy is used in videos.
