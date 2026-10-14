# Step 2: Asset debt (gate: zero debt before the final render)

Asset debt is everything the approved plan needs that doesn't exist yet. Write it right after the plan is approved, in `EP NN <slug>/debt.md`, and keep it current until delivery. Drafts may use placeholders; the final render waits until every row is `done` or `reused`.

## Build the list

Walk the approved plan beat by beat and list every piece the video needs:
- **Shoot:** camera takes, B-roll, before/after shots, extra takes for set pieces.
- **Record:** voice lines, pickups, hook options.
- **Capture:** screenshots, screen recordings, real documents.
- **Generate:** images, plates, avatar or video clips, music, voices, SFX.
- **Build (code):** every scene, overlay, chart, map, title card, signature moment, break-from-reality moment, caption style, thumbnail and vertical layout that still has to be coded. Code-built items are debt until they render clean and pass their stills check.
- **Get:** licenses, permissions (people on camera, locations, testimonials), proof the Idea Record marked as "still need".
- **Decide:** any open choice the build can't proceed without.

Then **search `07 Asset Library/asset-index.md` for every row** (`craft/asset-library.md`). Matches become `reused A0123`.

## debt.md

| # | Beat | Item | Kind | Owner | How / tool | Cost | Library | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Hook | Wide shot of the finished taco tray | shoot | creator | phone, 9:16 + 16:9 | — | — | owed |
| 2 | Beat 2 | Price-tier comparison chart | build | Claude | HyperFrames, pack colors | — | — | owed |
| 3 | Beat 3 | Kitchen plate, night | generate | Claude | image tool | (from price check) | — | owed |
| 4 | Beat 4 | Supplier invoice | capture | creator | photo, blur names | — | A0042 | reused |

- **Kind:** shoot · record · capture · generate · build · get · decide.
- **Owner:** creator · Claude · a named tool or person.
- **Cost:** for paid generation, the tool's own price check, never a guess. Paid items wait for the creator's approval (SKILL.md principle 11).
- **Status:** owed · in progress · placeholder (in drafts only) · done · reused · cut.

## Rules

- **Creator's items first.** Group the creator's owed items into one plain-language list (what, how, by when) and send it right after the plan is approved. `RECORDING.md` (Order A) and `SHOOT.md` (Order B) include their shoot and record rows.
- **Every new asset is filed** into the library when it's done, if reusable (`craft/asset-library.md`), and the row gets its library ID.
- **Placeholders are labeled** on screen in drafts ("PLACEHOLDER: kitchen plate") and listed in the review log.
- **Cutting a beat cuts its debt;** mark rows `cut`, don't delete them.
- **Summary line** at the top of `debt.md`: `owed N · in progress N · placeholder N · done N · reused N`. The same line goes in `START-HERE.md` `## Videos`.
- **Gate:** the final render (Gate 3) does not start while any row is owed, in progress or placeholder.
