# Decision pages

A decision page lets the creator decide by looking, not by reading a description. It mirrors how the brand was built: one thing at a time, visual options, a recommended pick, main + backup, and the picks saved for later.

## When to use a page, when to ask in chat

Pages are for things the creator judges by looking or listening. Everything decided in words is an interview, and interviews happen in chat.

- **Page (visual or sound only):** thumbnails, the look of a moment, motion and graphics options (rendered clips), where the creator sits on screen, cutaway gags drawn as stills, the style of the edit, music, the cut's judgment calls, a draft review, the brand review at the end.
- **Chat (AskUserQuestion, one decision per question):** every word decision. The idea fields, what they brought, kind of video, script shape, story arc, the rest of the story plan, titles (the words; the thumbnail they promise goes on a page), opening lines, the beat outline, order of work, length, yes/no, a follow-up after a page. Put the options' wording, a one-line example and what each changes in the option labels and descriptions; mark one "(Recommended)" with one line of why.
- **Shorts:** the look of a moment, layout per beat and how creator and source share the frame go on pages as 1080×1920 stills of real material; gags and timing-dependent moments as 2–4 s clip cards (`shorts/README.md` checklist item 11).
- **Shorts this video can feed** are words in chat (each with its time, line and message); a page only when a still is needed to judge one. Each kept one becomes its own Short (`shorts/README.md`).
- Never both for the same decision. A page's look follows the brand file (colors, fonts, house rules); that rule is for visual pages and never turns a word decision into a page.

The page examples for word decisions (`arc.json`, `story-rest.json`, `hooks-*.json`, the title half of `titles.json`, `intake-confirm.json`) stay only for creators who ask for pages; the same shapes work as AskUserQuestion options.

## The live picker (visual decisions once there's footage or a built edit)

Once real footage or a first HyperFrames edit exists, the visual decisions of a video go on **one living picker page** (`picker/README.md`), not one page per decision. Every option plays the real edit live on the creator's footage, on top of everything already picked, so they see combinations without a render, and what they pick is exactly what renders.

- **One page per video, same link all the way through.** Tabs are groups of decisions that appear when their step comes: **Look** → **Beats** → later **Fixes**, **Sound**, **Thumbnail**. **Watch** plays the whole video with every pick stacked.
- **Decisions get added, never restarted.** A later round adds rows marked "New" to the same page. Earlier picks stay visible and can still be changed. When a change affects another pick, that row is marked "Check again" (`dependsOn`), never silently kept or wiped.
- **Captions are one style for the whole video.** Picked once, on the Look tab.
- **On-screen text changes per beat.** Important moments get their own treatment, chosen for how that moment should feel. Beats with no special treatment just show captions and get no row.
- **When on-screen text is up, captions are hidden.** The two never show together (`hideCaptions`).
- **When each tab opens.** Look: after the script is locked and footage or a first edit exists, before the beats are built (caption style once; colors and fonts too only without a Brand Genome). Beats: after the beat brief, one row per beat that gets a treatment, 2–3 treatments each playing on that beat's own footage. Fixes: from the draft review, only the beats the creator flagged, each showing the current version next to 2 alternatives. Sound and thumbnail when their steps come.
- **One pick per row, no backup.** The creator sees every option moving and combined, so a visual pick on the picker is a single pick; the other options are recorded as "also offered". Word decisions in chat keep Main and Backup.
- **The page is the decision log.** Each row is one stored record (what was picked, what else was offered, which round). Write `plan.md` from it and read back only what changed since the last read.
- **Watch replaces render rounds that only show combinations.** Real renders are for checking timing and for the final.
- **Options come from the effects library**: `tools/talking-head/reference/looks.md`, `craft/graphics-library.md`, the spatial library and the swipe-library entries marked visual, inside the brand's limits. Every effect added to the library is built so it can be a picker option (a fragment over the creator's own take).
- **What stays off the picker:** word decisions (chat, one at a time), Keep / Cut lists, the cut, and the checks. Before footage or an edit exists (brand building, plan-stage mocks), the static pages below are still used.

Ask after publishing, like any page: "Are your picks in on *<video>*?" → **Ready, review it** · **I have a question** · **Pause for now**. On Ready: read the `picks` collection, write `plan.md`, and say the recap line ("Opening line: Two-tone stack · Ending: Name pills · 4 more unchanged").

## One decision per page. Never two.

This is the rule for the static pages; on the live picker each row is one decision and the page holds the video's rows. A page decides one thing. "The look of the 38% moment" is one decision; "the look of every moment" is many, so it's many pages (or one moment plan page in `adjust` kind, where each row is only confirmed or changed). `build.py` stops a page where more than one section picks a Main.

A library page (keep as many as you like: break-from-reality spots, Shorts moments) is one decision: what's kept.

## Plain words only

The creator never sees internal labels: no step codes (A4, B5), no beat or layout codes (L1, C3), no slugs, no catalog letters. Name things the way the brand file names them; without a brand term, use plain words ("cutaway gags", not "break-from-reality moments"). Every page and question says **where** and **what**:
- `context` on the page: the time, the line the creator says there, what's on screen now, and what this decision changes. "2:14 · You say: 'and my focus went up thirty-eight percent' · On screen now: you, center-left."
- `at` on an option when options sit at different places ("1:40, after 'I almost quit'").
- Names are 1–3 plain words a stranger understands. `build.py` stops on anything that looks like an internal label.
The same goes for chat: never "approve B5" or "L1 or C3?". Say "the moment right after you say '…' (1:24): the big number, or the bar chart?"

## Shapes (copy the nearest example; `page-template/README.md` lists them)

| Kind | Use | Buttons |
|---|---|---|
| **Pick** (`fixed` + `single` + `singleFallback` + `altValue`) | One answer with a backup: kit, story layer, title, the look of a moment, placement | **Main · Backup · Alternative · Discard**. Untouched options count as Alternative. |
| **Finalists → pick** | More than 6 options (hooks, thumbnails): page 1 tiles **Finalist / Discard**, page 2 the finalists large with Main · Backup · Alternative · Discard | |
| **Library** | Keep any number: break-from-reality spots, Shorts moments | e.g. **Draft it / Skip** |
| **Check** (`adjust`) | Confirm or change each row: what was taken from their plan, the cut, a draft review, the moment plan, the brand review | e.g. **Confirm / Change it**, **Keep / Cut**, **Looks right / Change it** |

Main + Backup + Alternatives are written to `plan.md` under the decision, so the backup is on record for the edit: "Opening line: Cold open · backup Confession · alternatives One number."

Every option can take a note (the box appears once it's voted). Notes are read with the votes and acted on.

**Tags on cards:** `pick: true` + `why` = "Our pick for you" (exactly one per pick page, with one line of why). `taken: true` (or a source, `"your brief"`) = "From your plan": the option already chosen by what they handed in. `outside: true` = "Outside your brand" (`craft/brand-fit.md`).

## What goes on the cards

- **Real material first.** Once footage or a draft exists, cards show real stills: the creator's frame with the graphic built over it (Playwright stills for HyperFrames scenes, `beats.js` for engine clips). Code-drawn mocks (`page-template/mocks.py`) only before anything is filmed or built.
- **In the brand.** Mocks use the brand's colors and fonts (Genome, Brand Sheet or kit). An option that stretches the brand says so with `outside`.
- **Laid out right.** Every mock passes the still check in `craft/layout.md`.
- **Clearly different side by side.** Two options that look alike get merged or made distinct.

## Picking clips for a spot (outtakes, reactions, B-roll)

- First say how many clips the spot holds and how long each can be ("the cold open fits 3 hits of 1–2.5 s").
- Cut every candidate to its best moment at that length before it goes on a card. Never show a 10 s take for a 2 s spot. Put the length on the card (`at`: "1.8 s").
- A spot that takes longer clips (an end blooper reel) is its own round on its own page, cut to that spot's length.
- Clips play as clip cards (`page-template/README.md`).

## Build and publish

```
python3 $SKILL/page-template/build.py <decision>.json <decision>.html
```
Publish as a private artifact with `capabilities: {db: {}}` and the images it references in `files`. Never design a page by hand. Fields: the template's standard fields (`round`, `stage` + `stepId` + `part` + `journeyIf`, `kind`, `title`, `what`, `next`, `buttons`, `keepValues`, `keepWord`, `single`, `singleFallback`, `altValue`, `layout`, `aspect`, `sections`, `options[]` with `id`, `name`, `line`, `images[]` or `html`, `swatches`, `play`, `pick`, `why`, `fonts[]`, `head`, `houseRules`, `locked`), plus:
- `context`: `{time, said, now, changes}`, shown under the title.
- option `at`: where in the video this option lands.
- option `taken`: `true` or the source's name.
- option `outside`: `true`.
- `fontFiles`: brand fonts kept in the brand folder (`01 Brand Kit/fonts/`), `[{family, path, weight}]`, inlined like bundled fonts.
- `allowWords`: real-world codes the plain-words check should let through ("Q3").

Copy every page's JSON and HTML into the episode's `_review/pages/` before the session ends.

## The chat around every page

After publishing, ask straight away (AskUserQuestion), with the tracker line above it ("Plan · decision 4 of 13 · about 30% done"):
"Are your picks in on *<page title>*?" → **Ready, review it** · **I have a question** · **Pause for now**, plus **Skip this step** on steps marked `required: false` in `journey.json`.
- **Ready:** read the votes (artifact data tool, collection `votes-<round>`; on a pick page a finalist with no vote is an Alternative), act on notes, ask for a Main if missing, say the recap line, write the result to `plan.md`, lock the page (`locked: true`, same link), go on.
- **Question:** answer, ask again.
- **Pause:** save the step and the open page link to `START-HERE.md` `## Videos`; one line on how to resume.
- **Skip:** record the default, lock, go on.

**One page at a time.** Never publish the next page before the current one is reviewed.

**Recap line** after every review: "Opening line: Cold open, backup Confession, 1 alternative."

**Step hand-offs** when a stage ends or starts: what was just locked, what's next and roughly how long, in plain words.

## Demo creators

The persona fills the page (`answered_by: persona`); the header says "Answered as <name> (demo)". The operator says "go" before the next page.
