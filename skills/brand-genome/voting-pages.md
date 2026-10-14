# Voting pages (the core tool)

A voting page is how the creator picks by looking instead of describing. **Use one only when the choice has to be seen or heard.** If words are enough to judge it, ask with AskUserQuestion in chat.

Nothing on a page costs the creator anything: photos come from `benchmark/`, art styles from `benchmark/looks/`, backdrop scenes from `benchmark/backdrops/`, everything else is drawn in code.

## Two kinds of decision: fixed and library

Classify every round before building it. Each section shows a rule line above its cards that says what the buttons allow. The template writes it from `kind`; don't repeat it in `what`.

| Kind | What it means | Page shape | Buttons |
|---|---|---|---|
| **Fixed** | One answer, plus a backup. This is what makes the channel recognizable. | Two pages, always: **finalists** (small tiles) → **pick** (the finalists large, side by side, in context) | Page 1: **Finalist** / **Discard**. Page 2: **Main** / **Backup** / **Alternative** / **Discard** |
| **Library** | More is better, as long as the creator likes it. The right one is picked per video, later, by the video skill. | Many small tiles, each with its use-when line. No cap. | **Keep in library** / **Discard** |

Fixed (finalists → pick): color editing, text style, captions, wordmark, name tag, series tag, sting, sound logo, profile picture, banner. Three fixed rounds work differently: the **palette** (finalists → **This one** / **Discard**, one answer, no backup), **fonts** (finalists per job → the set builder, one set) and the **motion feel** (no finalists: picked by group on the one entrances page; see Stage 5).
Library: filters for specific scenes, art styles for scenes you can't film, backdrops, extras, break-from-reality moments, entrances, scene changes, music, sound effects, ways to close a video, thumbnail layouts, vertical layouts.

### The two-page finalist flow (one shared pattern; never rebuilt per step)

Every fixed round uses exactly this, so every step behaves the same:
1. **Finalists page** (`kind: "finalists"`, `layout: "tiles"`): 12–30 small tiles (as many as the catalog has that fit this creator). Buttons **Finalist** (`yes`) · **Discard** (`no`). No cap; `trimAbove: 6` shows a soft "easier with fewer" hint. The rule line tells the whole flow up front: "mark as many finalists as you like. Next, you'll pick a main and a backup from them, and keep any others as alternatives."
2. **Pick page** (`kind: "fixed"`, `single: "pick"`, `singleFallback: "backup"`, `altValue: "alt"`): only the finalists, large, in their real context. Buttons **Main** · **Backup** · **Alternative** · **Discard**. Main and Backup show as two large slots at the top; alternatives show under them as small square tiles, no limit. **A finalist nobody touched counts as an Alternative**: nothing is thrown away unless they press Discard. Swaps say so in one line ("Main is now Clean. Soft film moved to alternatives.").

Alternatives are saved in the Genome with the fixed pick (`look.md`: "Text style: Main · Backup · Alternatives"); video skills use them for a single moment or when Main and Backup don't fit. There are no separate "keep others for later" pages any more.

**Backup.** Keep the word, and don't explain it on the page. The page enforces it with the slots: at most one **Main** and one **Backup** per section. Main is needed (the chat review asks for it if missing); Backup is optional.

**Names never collide.** No two consecutive pages share an option name (text style and caption option names never repeat each other).

## The round map (the redundancy audit)

One line per round on what it decides. Test: if the creator could ask "didn't I just pick this?", it fails. Steps and required / skippable come from `page-template/journey.json`.

| Stage | Round | Kind | Decides | Shape |
|---|---|---|---|---|
| 1a | Who's on screen | Question | The channel's route. Main + secondary. | Chat |
| 1d | Writing voice | Question | How scripts and captions should sound | Chat: 8–12 styles multi-select, then the default |
| 4 | Taste, filming setup, what's behind you | Question | What they love and can't stand; where, with what, in what light they film; real room, green screen or AI cut-out | Chat, one call |
| 4.1 | Color editing | Fixed | The everyday color look of their clips | Finalists → pick, on the three test photos |
| 4.2 | Filters for specific scenes | Library | Short color changes for one scene | Tiles, each picture showing exactly what its name says |
| 4.3 | Art styles for scenes you can't film | Library (fixed first for generated channels) | Art styles for moments that can't be filmed | Tiles; then the image-rules question and the photo kit (chat) |
| 4.4 | Color palette | Fixed | The channel's colors | Finalists → compare (This one). The main and backup color editing are then tuned to it automatically (one line in chat, no page) |
| 4.5 | Fonts | Fixed | One font set | Finalists per job (20–30 tiles each) → set builder |
| 4.6 | Text style | Fixed | How titles and labels sit on the video | Finalists → pick |
| 4.7 | Captions | Fixed | The caption style; where captions are on | Caption-font question → finalists (click-to-play) → pick → 1 question |
| 4.8 | Backdrops | Library | What goes behind them and behind title cards; Our pick = title-card default | Tiles, real scenes |
| 4.9 | Extras | Library | Small extras and big moments | One page, two sections |
| 4.10 | Break-from-reality moments | Library | The cutaways the channel can use | Three-panel strips |
| 5.1 | Motion feel and how things come in | Fixed groups + library | The feel (Main + Backup group) and the entrances kept from any group | One page, entrances grouped under feel headings |
| 5.2 | Scene changes | Library | Transitions, incl. break-from-reality transitions | Click-to-play tiles, two sections; then the motion details question |
| 6.1 | Music | Library | Kinds of music, each with its use-when | Click-to-hear sketches |
| 6.2 | Sound effects | Library | A sound for each kind of moment | Click-to-hear, grouped by moment |
| 7.1 | Wordmark | Fixed | The name as a logo | Finalists → pick, each shown on a closing card, profile picture, video corner |
| 7.2 | Name tag | Fixed | The tag when they first speak | Finalists → pick, over the face frame; then lockup question |
| 7.3 | Series tag | Fixed | The show label + episode number | Finalists → pick |
| 7.4 | Sting | Fixed | The 1–2 s opener with sound | Timeline card + finalists → pick |
| 7.5 | Sound logo | Fixed | The note signature | Played after the creator's chosen sting; finalists → pick |
| 7.6 | Ways to close a video | Library | Endings for long videos | Tiles |
| 7.7 | Thumbnail layouts | Library | Layouts to choose from per video | Tiles at feed size |
| 7.8 | Profile picture | Fixed | Ask "a photo of you?" first | Yes: tips, no page · No: logo options · Not sure: photo-style and logo options on one page; finalists → pick |
| 7.9 | Banner | Fixed | One per platform that has one | Finalists → pick, on a channel-page mock |
| 8.1 | Vertical layouts | Library | Layouts for Shorts, Reels, TikTok | 9:16 test frames in phones |
| 8 | Vertical rules, captions | Question | Sting, faster motion, music under vertical; captions on vertical | Chat |
| 9 | Bios, profiles copy, run sheet | Written automatically | Shown on the Brand Genome page for edits | No page |
| any | Change something | Same as the original round | One decision, rerun in change mode (`revisit.md`) | The original page with `change` + `current` |

## Page copy and layout (applies to every page)

- **The title names the thing, in plain words** ("Color editing", "Color palette", "Fonts", "Captions"). Not a question, not a feeling.
- **One short line under the title (`what`). Nothing else above the cards.** No paragraph about test photos (the images carry a small "Test photo" tag via `photoTag`), no backup explanation, no use-when explanation.
- **The rule line** above each section's cards says what the buttons allow, written from `kind`: finalists "mark as many finalists as you like.", pick (with `altValue`) "pick a main and a backup. Every other finalist stays as an alternative unless you discard it.", library "Pick as many as you like. They'll all be added to your library.", adjust "say if it looks right." A section `title` goes in bold in front; `rule` overrides the sentence.
- **The header band is computed, never typed.** A page names only `stage` + `stepId` (+ `part`, e.g. "1 of 2"); `build.py` reads `page-template/journey.json` and draws: the journey strip (every visible stage, done ones filled, current one highlighted), the stage label ("LOOK · Stage 5 of 11"), the step dots ("Step 4 of 10 · page 1 of 2"), the colored page-type badge (**PICK ONE** blue · **FINALISTS** amber · **LIBRARY** green · **CHECK** teal; `badge` overrides the word) and "About N% done". Add or move a step in `journey.json` only.
- **The bottom bar** sits on every page: three lines, no buttons. (1) What this page is for ("You're building your library of filters for specific scenes."; computed from `kind` + `title`, `purpose` overrides). (2) Their picks so far ("3 kept · 2 discarded", "Main: Clean · Backup: Soft film · 4 alternatives"). (3) What's next: `next` + "Answer the question in chat when you're ready. You can stop anytime; your picks are saved." The "where you are" progress stays in the header, never repeated here. (The only button that can appear is **Copy answers for the chat**, and only when votes can't be saved live.)
- **Buttons toggle.** Pressing a selected button again clears it (back to no choice; on a pick page, back to Alternative). No need to pick something else to undo.
- **Discarded cards stay easy to see.** The picture keeps full strength; the card gets a dashed border and a small "Discarded" tag. Never dim a picture.
- **Pick-one pages show their limit.** Main (pick 1) and Backup (pick 1) slots above the cards; the card badges MAIN / BACKUP; with a slot full, that button on other cards reads "Swap in as Main".
- **Play is one big centered button** (▶ / ❚❚) on every card that plays; it toggles. Audio pages define `window.<fn>Stop(id, el)` so pause stops the sound.
- **Presets can always be reset.** The set builder shows **Reset** beside any changed picker and **Reset set** on the card.
- **Buttons answer the question** in plain words. Stranger test: someone reading only the header, the title and the buttons knows what they're choosing.
- **Every stage opens and closes with a plain hand-off in chat** (below). Never "Stage 4" on its own.
- Cut every word that isn't needed. No internal labels, no how-it's-made notes, no cost lines, no scaffolding headers, no unexplained placeholders.
- Same rules for chat questions: the question text carries the "what it changes" line; options are plain; "Other" always there.

## Before publishing any page: the checks

Run all of these on the built page (open it, look at every card). `build.py` enforces the copy ones; the picture ones are yours.
1. **Every tile shows what its name says.** Cover the name: could someone guess it from the picture alone? If not, rebuild the picture (the overlay that makes a filter recognizable, the real scene for a backdrop, a purpose-made frame for an extra). Never ship a flat color named after a thing.
2. **Options are clearly different side by side.** If two cards look alike, make each distinct or merge them.
3. **Universal copy.** Card names, "For:" lines and sample words never mention the creator's niche. `nicheWords` stops the build.
4. **House rules.** Anything in `house-rules.md` that binds copy or type (a banned word, "no tiny all-caps labels") goes into `houseRules`. With `noAllCaps`, `build.py` turns every all-caps word in option copy and mocks into Title Case and drops letter-spacing (it says how many mocks it changed); a banned word stops the build.
5. **Fonts fit.** Wide fonts are scaled by their `scale` in `fonts/fonts.json` and get line-height ≥ 1.2, so swapped fonts never overlap.
6. **The mock matches its person.** Pronouns in mock captions match the person pictured. Once the creator's own photos exist (`07 Asset Library/people/`, best per slot), mocks use them instead of the test photos; the first time their face appears on a page, say once in chat that pages are private until they share them.
7. **Play buttons** sit big and centered, and every animation runs through the whole line (a word-by-word caption lights one word at a time, in order, to the end).

## Build every page from the template

`page-template/` has the page, already designed: layout, buttons, saving, bottom bar, lightbox, click-to-play, set builder, phone width, dark mode. **Never design a page by hand.** Fill a data JSON and run:

```
python3 page-template/build.py <round>.json <round>.html
```

Then publish `<round>.html` as a private artifact with `capabilities: {db: {}}` and the images it references in `files`. The JSONs in `page-template/examples/` are the models to copy: one for every page in Stages 4–8, change mode and the Brand Genome page (`gen_examples.py` regenerates them).

**Copy the nearest example.** A round with no example JSON is built by copying the nearest example of the same shape (library tiles → `moments-library.json`; finalists tiles → `text-style-tiles.json`; pick page → `text-style-pick.json`; click-to-play cards → `captions-tiles.json`; phone frames → `vertical-layouts.json`) and changing only `round`, `stage`, `stepId`, `part`, `title`, `what`, `next`, `rule` and `options`. **Sample words on the mocks are standard and never rewritten:** title "I TRIED IT FOR 30 DAYS" (Title Case under a no-all-caps house rule; `build.py` does it), text "Here's what actually happened.", label "Day 1 vs Day 30", caption "and that's the part nobody tells you", list "1 · Week one / 2 · The hard part / 3 · The result", "EP 1", "Part 2", notes "start here →". Same for every creator, whatever their field (constants at the top of `gen_examples.py`). Only these change for the creator: the palette, fonts, their name (name tag, kit mocks) and, once they exist, their photos.

Fields the template reads (nothing else is read; a field not listed here does nothing):

| Field | What goes in it |
|---|---|
| `round` | slug; also names the saved collection `votes-<round>` |
| `stage` + `stepId` | Where the page sits in `page-template/journey.json` (e.g. `look` + `color-editing`); the header band is computed from it. `part`: "1 of 2" for two-page steps. `journeyIf: ["vertical"]` when Vertical is in this creator's run. |
| `nicheWords` | The creator's niche words (their trade, animals, tools, places). `build.py` stops if option copy uses any (matched at the start of a word, so "groom" also catches "grooming"; pick words that won't catch everyday ones, e.g. not "fur"). "made picture" / "made scene" are banned everywhere. |
| `houseRules` | `{"words": [...], "noAllCaps": true}` from `house-rules.md`. `noAllCaps` is applied automatically (Title Case, no letter-spacing) to option copy and mocks; a banned word stops the build. An option that imitates a real device's overlay (a camcorder's REC) can set `houseExempt: true`. On the Genome page, `noAllCaps` also drops the page's own capital labels. |
| `kind` | `fixed` · `library` · `finalists` · `adjust`; sets the rule line and the bottom bar's first line. A section's own `kind` overrides it. |
| `rule` | Optional. Overrides the rule line's sentence (page or section). Lower-case start. |
| `purpose` | Optional. Overrides the bottom bar's first line. |
| `badge` | Optional. Overrides the page-type badge word. |
| `sectionTitle` | Optional, pages without `sections`: the bold name in front of the rule line ("Main style"). |
| `change` | Change mode only (`revisit.md`): the decision being changed, in plain words. The header says "Changing only: …" and every other stage shows as done. |
| `current` | Change mode: the creator's current pick, tagged "What you have now" and shown first. On a library round, mark every kept item `current`: it starts as Keep in library (an unvoted `current` item counts as kept when you read votes back), followed by the new options. |
| `locked` | `true` after the chat review: the page is republished read-only with "Done. Your picks are saved. Continue in chat." at the top. |
| `photoTag` | Optional ("Test photo", "Test scene"): a small tag on every card image. Page, section or option. |
| `title` | The name of the thing, in plain words ("Color editing"); a pick page adds ": your finalists" |
| `what` | One short line. Nothing else goes above the cards. |
| `buttons` | `[{value, label, hint?}]`. Values in use: `pick`, `backup`, `alt`, `no`, `keep`, `yes`, `less`, `more`. |
| `keepValues` | Which values count as "kept" in the bottom bar |
| `single` + `singleFallback` | Pick page: `single` is the Main value (`pick`), `singleFallback` the Backup value (`backup`). Each may sit on only one card per section. |
| `altValue` | Pick page: `"alt"`. Untouched finalists count as this; adds the large slots and the alternatives strip. |
| `keepWord` | The bottom bar's unit, `"singular|plural"` ("finalist|finalists") |
| `trimAbove` | Soft hint only: when more than this many are kept, the page says the next step is easier with fewer. Never a hard cap. |
| `layout` | `"tiles"` for many small options |
| `aspect` | Card media shape: `"16/9"` (default), `"2/1"`, `"9/16"` (phone frames), `"1/1"`, or any ratio. Per page, section or option. |
| `next` | One line on what happens after (goes in the bottom bar) |
| `persona` | Demo only: the persona's first name. Shown once in the header ("Answered as Wren (demo)"); never on cards. |
| `fonts[]` | Slugs from `page-template/fonts/fonts.json` (the offline fonts, each with its `jobs` and width `scale`), inlined by `build.py` as woff2. An unknown slug stops the build; never substitute a system font silently. |
| `head` | One string of `<style>`/`<script>` injected into `<head>`: CSS keyframes keyed off `.card.playing`, click-to-play functions, Web Audio sketches. Never autoplay. |
| `sections[]` | Groups on one page (font jobs, extras' two groups, the feel groups). Each: `id`, `title`, `line`, `rule`, `photoTag`, `kind`, `buttons`, `keepValues`, `keepWord`, optional `single` + `singleFallback` + `altValue`, `layout`, `aspect`, `trimAbove`, `movable` (default true: cards in a later section get a "Move to [first section]" link), `options[]`. |
| `sectionPick` | One page that both picks a group and builds a library (Stage 5.1): `{word: "feel", buttons: [{value:"pick",label:"Main feel"},{value:"backup",label:"Backup feel"},{value:"alt",label:"Alternative"}]}`. Each section header gets those buttons and **Play all in this feel**; Main and Backup slots sit at the top. Saved as doc `_sec-<section id>`. |
| `options[]` | `id`, `name` (1–3 words), `line` (one short line), `images[]` (1–3 paths; 3 = face, hands at work, place) or `html` (a code-drawn mock), optional `labels[]`, `css` (CSS filter on the media), `overlay` / `overlays[]` (a layer over the image: tint, letterbox bars, a camcorder's REC, a scope mask), `swatches[]` (`{hex, role}`; roles in order: background, words, pop color, second color, pale), `aspect`, `control: true` (a reference card with no buttons, e.g. "As shot"), `play` (`true` adds a Play button; the card gets class `playing` for `playMs` ms; `play: "fnName"` also calls `window.fnName(id, cardEl)`), `houseExempt`, and on exactly one option per section `pick: true` + `why` (one line) |
| `mode: "sets"` | The set builder (fonts). Instead of `options`: `slots` (`[{id, label}]`), `choices` (`{slotId: [{id, name, css}]}`, the finalists per slot; `css` carries the font's `--fs` scale), `presets` (`[{name, line, picks, pick?}]`) and `preview` (HTML with `{{slotId}}` / `{{slotId.name}}` placeholders). Button **Use this set**; Reset per picker and Reset set. |

### Color editing, then filters (the skill sorts, the creator picks)

Color editing is fixed; every other look goes to the filters library. The skill sorts from the interview, research and taste answers; nothing is left out:
- **Color editing:** only looks that could carry a whole video for this creator, about 8–12, through the finalist flow.
- **Filters for specific scenes:** everything else, including the wild ones. Each card's `line` is "For: …", a universal moment.

### Three-photo rule

A footage look is judged on three benchmark frames: **a face, hands at work, a place**, picked from `benchmark/README.md` to match the creator's field; when no frame matches the field, pick the nearest in mood and say so once in chat. A filter that only reads on a certain kind of shot (tiny world needs a high, wide view; fake night needs windows or lights) uses a frame that suits it instead (`catalog/looks.md` names it). Verticals (Stage 8) crop the face frame to 9:16 and use drawn graphics for "the screen"; never another person's photo standing in for the creator.

## The pages, in the creator's words

The JSONs in `page-template/examples/` are the spec for their rounds. Copy the one for the round; keep the standard sample words; change options only from the catalog.

| Round | Example JSON(s) | Buttons |
|---|---|---|
| 4.1 Color editing | `footage-looks-tiles.json` → `footage-looks-pick.json` | Finalist → Main · Backup · Alternative · Discard |
| 4.2 Filters | `footage-filters.json` | Keep in library · Discard |
| 4.3 Art styles | `made-scenes.json` | Keep in library · Discard |
| 4.4 Palette | `palette-tiles.json` → `palette-compare.json` | Finalist → This one · Discard |
| 4.5 Fonts | `fonts-tiles.json` → `font-sets.json` | Finalist → Use this set (with Reset) |
| 4.6 Text style | `text-style-tiles.json` → `text-style-pick.json` | Finalist → Main · Backup · Alternative · Discard |
| 4.7 Captions | `captions-tiles.json` → `captions-pick.json` | Finalist → Main · Backup · Alternative · Discard |
| 4.8 Backdrops | `backdrops.json` | Keep in library · Discard |
| 4.9 Extras | `moments-library.json` | Keep in library · Discard |
| 4.10 Break-from-reality | `break-from-reality.json` | Keep in library · Discard |
| 5.1 Motion feel + entrances | `motion-entrances.json` | Main feel · Backup feel · Alternative (per group); Keep in library · Discard (per entrance) |
| 5.2 Scene changes | `scene-changes.json` | Keep in library · Discard |
| 5.3 Spatial moves | `motion-entrances.json` shape, one section, clip cards | Keep in library · Discard |
| 6.1 Music | `music.json` | Keep in library · Discard |
| 6.2 Sound effects | build like `music.json`, one section per moment kind | Keep in library · Discard |
| 7.1 Wordmark | `wordmark-tiles.json` → `wordmark-pick.json` | Finalist → Main · Backup · Alternative · Discard |
| 7.2 Name tag | `name-tag-tiles.json` → `name-tag-pick.json` | same |
| 7.3 Series tag | `series-tag-tiles.json` → `series-tag-pick.json` | same |
| 7.4 Sting | `sting-tiles.json` → `sting-pick.json` | same |
| 7.5 Sound logo | `sound-logo-tiles.json` → `sound-logo-pick.json` | same |
| 7.6 Ways to close a video | `close-out.json` | Keep in library · Discard |
| 7.7 Thumbnail layouts | build like `close-out.json` (feed size, sample title) | Keep in library · Discard |
| 7.8 Profile picture | `profile-picture-tiles.json` → `profile-picture-pick.json` | Finalist → Main · Backup · Alternative · Discard |
| 7.9 Banner | `banner-tiles.json` → `banner-pick.json` (one pair per platform with a banner) | same |
| 8.1 Vertical layouts | `vertical-layouts.json` | Keep in library · Discard |
| Change mode | `change-palette-tiles.json` (any page + `change`, `current`) | the round's own |

Sound pages (music, sting, sound logo, sound effects) put their Web Audio code in `head` and name it in `play`. Every sound page says plainly that these are sketches of the sound, not finished audio.

## The chat around every page

**After publishing a page, ask straight away** (AskUserQuestion), with one progress line above it ("Look, step 4 of 10 · about 28% done"):
"Are your picks in on *<page title>*?" → **Ready, review it** · **I have a question** · **Pause for now**, plus **Skip this step** on skippable steps (`required: false` in `journey.json`; in change mode it reads **Keep what I have**).
- **Ready, review it:** read the votes back (artifact data tool), say in one line what was decided, answer or act on any notes, check what's missing (no Main on a pick page → ask for it here), offer a redo if a pick needs one, ask follow-ups, then **lock the page** (rebuild with `locked: true`, republish to the same link) and go on.
- **I have a question:** answer it, then ask the same question again.
- **Pause for now:** the pause flow below.
- **Skip this step:** save the step as `skipped` in the stage doc (the default from the stage file applies), lock the page, one line ("Skipped. You can come back to this anytime."), go on.
In demo, the persona fills the page and the operator says "go" (Stage 0 run controls).

**The recap line.** After every review, one line that names what was just decided, in plain words: "Your text style: Color blocks, backup Bottom bar, 3 alternatives." Two pages later, nobody should have to remember.

**Stage hand-offs.** Whenever a stage ends or starts, say what just happened and what's next, in plain words, with the stage number only as a small extra: "Look is done: your colors, filters and fonts are saved. Next: Movement, how things move on screen (2 short pages, about 5 minutes)." Never "Stage 4" or "next stage" on its own. Every stage's first check-in also says once that they can stop anytime.

**Pages from earlier stages.** The chat can open a page but not close one. That's why every reviewed page is locked: if it's still open beside the chat, it says "Done. Your picks are saved. Continue in chat." with its buttons off.

## Pause and come back

- **Pause** ("pause", "stop for today", **Pause for now**): start nothing new. Save where they are to the `## Brand` section of `START-HERE.md` (stage, step, the open page's link and whether it was reviewed), update the project copy, and reply with one line: "Saved. When you're back, open a chat in this project and say *continue my brand*." Votes already on an open page stay saved in the page itself.
- **Continue** ("continue my brand", or any resume): read `START-HERE.md`, say in one line where they left off, then re-send the open page (if it wasn't reviewed, ask the ready question again) or publish the next one.
- **Another device:** the page links work anywhere they're signed in; the project's `START-HERE.md` carries the state. **A new chat outside the project:** find the brand (SKILL.md, "Brand folder and where to look") and resume from its `START-HERE.md`.

## Saved data

- Collection `votes-<round>`, doc id = option id. Fields: `{item, name, verdict, note, section, at, answered_by}`; `answered_by` is `creator`, `persona`, `operator` or `claude (auto)`. On a pick page, a finalist with no doc (or an empty verdict) is an **Alternative**. Set builder: doc `set`, `{item: "set", set: {slotId: choiceId}, name}`. Section picks: doc `_sec-<section id>`, `{verdict}`.
- Read back with the artifact data tool on **Ready, review it**, "check", "done" or "notes are in", or in demo right after writing.
- After reading votes back, record the page's artifact URL in the stage doc (the Genome page links to it).
- Fallback with no saved-data capability: the bottom bar's **Copy answers for the chat** button puts a tab-separated list on the clipboard.

## Follow-ups after a page

The card line is the use-when; a note changes it; the Genome records line-or-note as **use when**. Nothing else is asked about a library item. Follow-ups that remain:
- **A Discard with a note:** the note becomes a house rule. No question.
- **A question a stage file names explicitly** (captions on where, caption font, motion details, lockup).
Backup never gets a follow-up. Max 3 per page, AskUserQuestion with suggested answers + Other.

## Demo mode on a page

- Claude writes the persona's votes into `votes-<round>` with `answered_by: persona`. The page shows the vote as the selected button, exactly as a creator's would. **No name badge on cards.** The demo marking is the header ("Answered as Wren (demo)") and the saved data.
- **Notes behave like a person's.** Most votes have no note. A note appears only on a strong yes, a tweak request or a clear no, in the persona's own voice. Never analyst lines.
- One page at a time: after the recap line, wait for "go". Never publish a second page before "go".

## Design rules the template already enforces (don't undo them)

- Neutral gray page; the only chrome color is the page-type color (badge, slots, kept outlines). The options carry everything else.
- System fonts for the chrome, no CDN calls. Option fonts are the bundled woff2 files, inlined by `build.py`; no network.
- Static by default; motion and sound on click only.
- Phone width works. Dark mode follows the system.
- Tap the pictures to see them big.
- In code-drawn mocks, highlighted words on consecutive lines must not touch: line-height ≥ 1.35 and padding on highlight boxes, or one box per line.
- Stand-in people in mocks: a benchmark photo cut-out or a plain gray silhouette. Never a drawn figure that reads as an animal or object. No icons, no emoji; a pointer is an inline SVG.

## Never replace a published page

Lock it and republish to the same link, or make a new one, so earlier votes stay readable. Copy every page's data JSON and HTML into `01 Brand Kit/page-sources/` before the session ends.
