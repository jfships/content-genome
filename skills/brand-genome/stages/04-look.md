# Stage 4: Look

**Options come from `../catalog/`** (see its README): show a spread of common, rare and funky options, never only safe ones, and never ask the creator to describe a style in words. Every page is built from `../page-template/` with the words in `../voting-pages.md` (round map, fixed vs library, page layout); for this stage the JSONs in `../page-template/examples/` are the spec. Nothing in this stage costs the creator anything.

**Read the route first** (`Who I Am.md`, "Who's on screen"). It decides which steps run:
- Filmed footage in any route (on camera, hands, screens) → steps 1 and 2 run, and the color editing is tuned to the palette after step 4.
- Fully generated or illustrated channel → steps 1 and 2 are skipped (even though color editing is marked required in `journey.json`); step 3 opens with the fixed art-style finalist flow, and the chosen art style's generation prompt gets the palette added after step 4 (same recipe section).
- An AI avatar or made-up character → the image-rules question on the art-styles step (3) covers it.

**Say first, in chat (the stage hand-off):** "Next is Look: how your videos look. A few quick questions, then ten steps (about 15 pages) where you click pictures. About 25 minutes. You decide everything here, nothing happens to your videos without your say, and you can stop anytime."

## Before the first page: questions in chat

Ask with AskUserQuestion, now, not in Stage 1. Each question says what the answer changes.
1. **Taste.** "Think of videos or channels you love the look of. What is it about them?" Options drawn from the research (clean and bright / dark and cinematic / handmade and messy / loud and colorful) plus Other. Multi-select.
2. **Can't stand.** "Anything you can't stand on screen?" (neon, bouncy text, fast cuts, filters that look fake, stock music) plus Other. Multi-select.
3. **Filming setup.** One AskUserQuestion call with four single-select questions, each one line: *Where will you usually film?* (my room / my shop or workplace / outside / Other) · *With what?* (phone / camera / webcam or screen / Other) · *What light?* (daylight / lamps / mixed / Other) · *What's behind you in most videos?* with the trade-off in each option, in plain words:
   - *My real room* (zero setup; the room is part of the look)
   - *A green screen* (the cleanest background swaps; needs the screen and even light on it)
   - *My room removed by AI* (no gear; slower to process, especially on a laptop without a strong graphics card, and edges can flicker around hair and hands)
   - *Not sure yet* (keep the real room for now; backdrops still get picked, for title cards and later)
   Lighting and framing advice is video-genome's job, per video, from these answers and the chosen look.

Write them into `Who I Am.md` (taste and can't-stand under "Takes they hold"; setup and background under "Filming setup"). A can't-stand that binds type or copy ("no tiny all-caps labels", a banned word) also goes into `house-rules.md` and into every page's `houseRules` from here on. They shape **Our pick for you** on every page in this stage and the sorting into fixed pages vs library pages. In demo, the persona answers in character and the answers go on the persona card.

**Pick the test photos:** from `../benchmark/README.md`, the three frames closest to the creator's field (face, hands at work, place; nearest in mood when nothing matches). Say in chat, once: "I'll show every option on the same three test photos, so you can compare. They won't be in your videos." On the page they carry only the small "Test photo" tag.

## The ten steps (page copy and checks in `../voting-pages.md`)

Page copy for every step: the title names the thing; one short line under it; the rule line comes from `kind`; nothing else above the cards. Fixed steps use the shared finalist flow (finalists → Main / Backup / Alternative / Discard). Copy the example JSON for the step. Before publishing, run the checks in `../voting-pages.md` ("Before publishing any page"), above all: every picture shows what its name says.

1. **Color editing** (fixed), two pages: `footage-looks-tiles.json` → `footage-looks-pick.json`. Only looks that could carry a whole video for this creator (8–12), plus the "As shot" control. Options: `../catalog/looks.md` §A and §B (CSS recipes → `css` / `overlay`). Optional: if the creator sends a photo of themselves at work, show the pick page on it. Never generate one.
2. **Filters for specific scenes** (library, skippable; skipped → none). `footage-filters.json`. Every other look, the wild ones included (18–24); each card's line is "For: …", a universal moment. **Each card shows exactly what its name promises**: the color plus the overlay that makes it recognizable, on a frame that suits it (`../catalog/looks.md`, "Filters: what each card must show").
3. **Art styles for scenes you can't film** (library, skippable; fixed only for a generated channel; skipped → no generated scenes). `made-scenes.json`. Options: `../catalog/looks.md` §C via `../benchmark/looks/<slug>.jpg`. For a generated channel, a fixed art-style finalist flow comes first, then this library. Then the image-rules question and the photo kit (below).
4. **Color palette** (fixed), two pages: `palette-tiles.json` (Finalist / Discard, no cap, trim hint above 6) → `palette-compare.json` (This one / Discard). About 12–16 palettes from `../catalog/palettes-fonts.md`. Roles, in order: background, words, pop color, second color, pale.
   **Then, automatically (no page, no question):** tint the main and backup color editing to the palette (recipe: `../catalog/looks.md`, "Tuning a look to the palette"; write the result into `look.md`). Say it in one line: "I tuned your color editing to your palette." The tuned look is shown on the Brand Genome page; if it's off, the creator says "change my color editing".
5. **Fonts** (fixed), two pages: `fonts-tiles.json`, per-job tiles (Big titles / Text / Notes), **every bundled font for that job, 20–30 tiles each**, C/R/F spread, each sample scaled by its `scale` (Finalist / Discard; no cap) → `font-sets.json`, the set builder (three preset sets from the finalists, each with Title / Text / Notes pickers that update the preview live; Use this set; Reset per picker and Reset set). Fonts: `../page-template/fonts/fonts.json` (the only fonts a page can use; never a system font); sample words in the creator's colors, never on a white page.
6. **Text style** (fixed), two pages: `text-style-tiles.json` (12–20 styles from `../catalog/graphics.md`, each a title and a label in the locked palette and fonts, static; Finalist / Discard) → `text-style-pick.json` (finalists large over the test photo; Main / Backup / Alternative / Discard). Words sit in the clear space beside the speaker, never over the face. No caption in these mocks; how text moves comes in Movement.
7. **Captions** (fixed). First one chat question, because captions are read for minutes at a time: "Captions use your text font (<name>). Keep it, or pick a font just for captions?" (*Keep my text font* · *Something bolder* · *Something cleaner* · Other). If their text font is thin or decorative, say so in the question and recommend a sturdy one. Then two pages: `captions-tiles.json` (12–20 styles on the same talking frame, in the caption font; the big Play shows each style coming in, word by word where that's the style; Finalist / Discard) → `captions-pick.json` (Main / Backup / Alternative / Discard). Then one chat question: "Where are captions on? Long videos / Shorts and Reels / Both (most people say both)". Stage 8 reuses the answer. Every mock of captions from here on (kit, vertical, the Brand Genome page) uses the caption font.
8. **Backdrops** (library, skippable; skipped → plain palette color). `backdrops.json`, three sections: **Everyday** (palette plains, studio sweep, your space blurred, paper, grid, gradients, and real scenes: city at night, chalkboard, cork board, blueprint, space), **Fun and absurd** (weather map, news desk, courtroom, game show, award stage, the moon, inside a fish tank, giant's kitchen, crime scene, cereal box) and **You as…** (president, pilot, pro ballplayer, detective, champion: generic, no real seals, logos or league marks). Scenes are the photos in `../benchmark/backdrops/`; plains and patterns are drawn in the palette. **Our pick** is the default for title cards; a note on any card overrides it; write the default into `look.md`.
9. **Extras** (library, skippable). `moments-library.json`, one page, two sections: **Small extras** (`../catalog/graphics.md` overlays) and **Big moments** (`../catalog/moments.md` set pieces). Each mock is built to show the effect (a purpose-made frame where the test photo can't show it). Skipped → callout + chapter card.
10. **Break-from-reality moments** (library, skippable). `break-from-reality.json`. Each card is a three-panel strip: 1 · normal → 2 · the cutaway → 3 · back (images in `../benchmark/bfr/`), from `../catalog/moments.md`. Keep in library / Discard. The bank is written right after (below). Skipped → none.

**Hand-off at the end of Look** (one line): "Look is done: your colors, filters, fonts, text and captions are saved. Next: Movement, how things move on screen (2 short pages, about 5 minutes)."

## Written automatically after two steps

**After step 3 (art styles): image rules, then the photo kit.** Ask one question in chat right after the page. Ask first, and say what it changes: "Some generated pictures could show a drawn or generated version of you. That needs an image tool and a few reference photos. Without it, generated pictures show your subject, not you, which works fine for most channels." Options: *No generated pictures of me* (default; this section is skipped) · *Yes, I have an image tool connected* · *Yes, let me connect one*. In demo, the default is a drawn avatar; the operator can choose to generate a face here, with the tool's own cost stated first.

- **Every generated image gets a brief approved first:** subject, likeness references, pose, setting, light, style, palette, camera, what to avoid.
- **Likeness:** reference photos live in `07 Asset Library/people/` and are indexed (`Type: person`). Use the best 1–2, note which photos leak bad traits (e.g. a hat or jewelry that keeps appearing), and spell out signature details. In demo mode, use the face references made here, or the drawn avatar if none were made.
- **Log every round:** prompt, tool, cost, verdict.
- **One image at a time** until the recipe is stable.
- **Disclosure:** record each platform's current rule for realistic synthetic images and voices (check live), and when the creator's content triggers it.

Write `00 Decisions/image-rules.md`.

**Photo kit (always offered, every photo optional, can be sent later).** Right after the image-rules question, whatever the answer: the photos make mocks look like them (their face on the pages instead of the test photo), give them a profile photo, and, if they chose generated pictures of themselves, teach image tools their face.
- **Say it plainly first:** "A few photos of you make the rest of this look like you, and let image tools draw you well later. Every photo is optional. Send them now or later; nothing waits on them." Then one AskUserQuestion multi-select of the slots, with the reason for each in plain words, **core and recommended pre-selected**:
  - Core: face straight on, neutral (`face-front-1.jpg`) · face three-quarter left (`three-quarter-left-1.jpg`) · face three-quarter right (`three-quarter-right-1.jpg`) · profile (`profile-1.jpg`) · full body, standing (`full-body-1.jpg`)
  - Recommended: smiling (`face-smile-1.jpg`) · waist up, at work (`waist-up-work-1.jpg`)
  - If it applies: hands (`hands-1.jpg`, if the channel shows hands) · the usual setting, empty (`setting-empty-1.jpg`) · head and shoulders in the usual outfit (`head-shoulders-1.jpg`)
  A profile photo, if they chose a photo profile picture in Stage 7, goes to `06 Profiles/profile-photo-1.jpg` and is added to the list then.
- **Then:** *Send now* or *Send later*. Never block the run on photos.
- **Write `07 Asset Library/people/README.md`** (for anyone adding photos): what the photos are for (likeness references and the creator's own mocks, nothing else), that every one is optional, how to add them (drop them in `07 Asset Library/people/_incoming/` or attach them in chat), what makes a good photo (daylight from the front, sharp, nothing covering the face, plain or usual background, no filters, recent), and a slot table: slot | file name | why it helps.
- **Write `07 Asset Library/people/PHOTOS-OWED.md`**: only the photos the creator said they'd provide, columns `# | photo | file name | Owed/Received | date`, plus totals ("2 of 7 received").
- **Each time photos arrive** (attached, or found in `_incoming/`): look at each one; if a photo would teach a tool something wrong (a hat that keeps appearing, heavy filter, blur, someone else in frame), say so in one line and ask for another or keep it marked "use with care". Rename it by slot, file it in `07 Asset Library/people/`, add an `asset-index.md` row (`Type: person`, `Origin: uploaded`, `Rights: creator-owned; likeness reference only`, `Tags: <slot>, best` for the best 1–2 per slot), update `PHOTOS-OWED.md` and `image-rules.md` (slots filled, best per slot, photos to avoid and why, signature details to keep, the consent line in the creator's words with the date). With no computer linked, keep them for this session only and ask the creator to save them into that folder; media can't live in the project. Never edit, retouch or generate from them at this step.
- **From then on, mocks use their photos** (the best per slot) instead of the test photos, and pronouns in mock captions match them. The first time their face appears on a page, say once: "Your pages are private until you share them."
- **Privacy.** These are photos of a real person's face. The raw photos stay in the brand folder and are used only as likeness references and in the creator's own mocks; they're never uploaded anywhere except into a generation the creator approved.
- **Owed photos are remembered, not chased:** list them under Pending in `START-HERE.md`; remind in one line at wrap-up and after any later Genome change, never mid-step.
- **Demo mode:** no real photos. The kit stays empty (or holds faces generated in the image tool, only if the operator asks, cost stated first, marked `Origin: generated (demo)`).
- **Removing:** if the creator asks to remove a photo or the whole kit, move the files to `07 Asset Library/people/_removed/` (ask before any delete), mark their rows `removed by creator <date>`, and update `image-rules.md` and `PHOTOS-OWED.md`. Other skills never use a removed photo.

**After step 10 (break-from-reality moments): the bank.** No new page; show it in one short summary.
- A short scene where the video steps outside reality for a laugh or a point. **Never pre-generate.** The templates are the keeps from the break-from-reality page; the bank is written from them, with each one's use-when and 1–2 built from the creator's quirks. The templates, for reference:
  - **Department of Me:** clones of the creator in different roles
  - **Tiny Me:** a miniature creator inside the screen
  - **Nature Documentary:** a hushed narrator observing them at work
  - **The Standup:** their tools or ingredients as characters giving a status report
  - **The Trailer:** a mundane task cut like a movie trailer
  - **Reaction Cam:** an over-serious expert reacting to their work
- Add 1–2 built from the persona's or creator's quirks.
- Rule: every video's plan proposes 2–3 spots tied to its beats. They can draft them cheaply and cut later; final videos keep 1–2.

Write `00 Decisions/break-from-reality.md`.

The **name tag** is not chosen here; it's a brand-kit piece (Stage 7).

## The look, compiled

- The **fixed picks**: palette, color editing / main footage look (+ backup + alternatives, tuned to the palette), font set (+ caption font if different), text style (+ backup + alternatives), caption style (+ backup + alternatives) and where captions are on. The **libraries**: filters for specific scenes, art styles, backdrops (default marked), extras, break-from-reality moments (later: entrances, scene changes, music, sounds, endings, thumbnails, vertical layouts), each item with its **use when** (the card line, or the creator's note if they left one).
- Votes map like this: `pick` → the fixed pick; `backup` → its backup; `alt` or no vote on a pick page → an alternative; `keep` → a library item; skipped steps → `skipped` and their default.
- Exact values: palette (hex + role: background, words, pop color, second color, pale), the look's CSS recipe after tuning, font set (files, sizes), text style, caption spec. Libraries list every item by catalog slug with its use when.
- **House rules:** every No with a reason goes into `house-rules.md`.

## Output

`look.md` (fixed picks + backups, the libraries, exact values, the artifact URL of every page), `house-rules.md` updated, page JSONs and HTML in `01 Brand Kit/page-sources/`, and the gallery images in `05 Style Gallery/`. Reference photos go in `07 Asset Library/people/` (with its `README.md` and `PHOTOS-OWED.md`), each with a `Type: person` row in `asset-index.md`.
