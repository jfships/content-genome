---
name: brand-genome
description: Build a creator's complete content brand from nothing (identity, formats, look, movement, sound, brand kit, vertical system, voice, profiles) into one Brand Genome that video skills read, by picking from visuals instead of describing. Works for a real creator or a made-up demo persona. Use when someone starts a channel, rebrands, says "brand genome" or "brand from zero", or wants to change or correct any part of an existing Brand Genome (colors, fonts, name, sting, interview answers…).
---

# brand-genome: build a creator's Brand Genome

*brand-genome by jfships · [youtube.com/@jfships_ai](https://youtube.com/@jfships_ai) · free (MIT)*

Take a creator who has no channel, no brand and no design vocabulary, and finish with a **Brand Genome**: one record of every decision, plus a shareable page that shows it. Any later skill can make on-brand content from the Brand Genome alone.

The Brand Genome covers:
- who they are, why the content exists, what watching it should feel like, and how far they'll go
- a name and handle
- the shows they repeat: 2–3 formats (not topics or episode ideas; those are the creator's)
- how it looks: palette, footage look, font set, how words sit on the video, captions, each with its backup and alternatives, plus libraries of filters, backdrops and moments
- how it moves: the motion language
- how it sounds: music lanes, sound effects, the sound logo
- the brand kit: wordmark, name tag, series tag, sting, sound logo, endings, thumbnails, profile picture, banner
- the vertical system for Shorts, Reels and TikTok
- the voice kit, break-from-reality moments (chosen in Stage 4, written up right after), image rules and an optional reference photo kit of the creator (sent now or later, tracked as photos owed)
- profile setup on every platform
- the run-sheet of brand checks every video passes
- what performs in their genre (the research playbook), as guidance for making videos

**Scope.** This skill builds the brand, not the content. It never proposes topics or episode ideas: the creator brings an idea, or runs idea-genome, which turns a theme or nothing into an Idea Record. video-genome plans from that record and the Genome. It does not record, edit or render videos. At the end it hands off to idea-genome and video-genome (Stage 10).

**The pipeline.** Brand: brand-genome → `Brand Genome.md` (once per brand) · Content idea: idea-genome → `IDEA NNN <slug>.md` (per video) · Content plan and editing: video-genome → plan, build, deliver, results log. Each skill reads the files of the one before; pointing the flow at a different brand folder switches brands.

**No other skill required.** Everything this skill needs to finish is in this folder. Other skills may read the Brand Genome; they never supply brand decisions.

**No assumptions.** Nothing about the creator comes from anywhere but asking them, or in demo mode, from the persona built by the interview. Never fill a gap with a guess.

**Free out of the box.** Everything up to the brand kit runs with no paid tool: test photos, art styles, backdrop scenes and break-from-reality cutaways ship in `benchmark/`, everything else is drawn in code. Tools are only discussed at the step that could use one (the brand kit, and the image question after the art-styles page), with the free path offered first.

## How to use this folder

Read this file first. When a stage starts, read its file in `stages/`, and only that one, plus the catalog files it names. `catalog/` holds every option for every round (common, rare and funky), so the creator can build a style without knowing any design words. Before any voting page, read `voting-pages.md` and build the page from `page-template/` (never by hand). Read `revisit.md` whenever the creator wants to change or correct anything already decided, including interview answers: it finds the decision from plain words, reruns only that step the way it was first built, and asks before anything downstream changes. `benchmark/` holds the test photos, pre-made art styles, backdrop scenes and cutaways for the look rounds.

| # | Stage | File | Locked output |
|---|---|---|---|
| 0 | Setup, demo and auto modes | `stages/00-setup.md` | Mode, platforms + existing accounts, rhythm, the brand folder (whole tree); the seed if demo |
| 1 | Who they are, feel, name | `stages/01-identity.md` | Identity doc (core interview), truth rules, why the content exists, content personality, name + handle; persona card if demo |
| 2 | Research | `stages/02-research.md` | Channel playbook with sources |
| 3 | Formats | `stages/03-formats.md` | 2–3 repeatable formats and the starting pair (one question, no pages) |
| 4 | Look | `stages/04-look.md` | Color editing → filters → art styles (+ image rules, photo kit) → palette (color editing tuned to it automatically) → fonts → text style → captions → backdrops → extras → break-from-reality; the look (fixed picks + backups + alternatives, libraries), house rules |
| 5 | Movement | `stages/05-movement.md` | Motion feel + entrances (one page), scene changes, spatial moves (rendered clips), the motion table |
| 6 | Sound | `stages/06-sound.md` | Music library with tempo, phrase length, sound library |
| 7 | Brand kit | `stages/07-brand-kit.md` | Wordmark, name tag, series tag, sting + sound logo (WAV), endings and thumbnail libraries, profile picture, banner |
| 8 | Vertical (only if Shorts / Reels / TikTok were picked) | `stages/08-vertical.md` | 9:16 layouts library, safe zones, captions, vertical motion and sound |
| 9 | Brand Genome | `stages/09-brand-genome.md` | Written automatically first: profiles copy (bios, descriptions, templates, highlight covers, trailer plan) and the run sheet; then `Brand Genome.md`, the Brand Genome page (highlights), its offline copy and link shortcut |
| 10 | Handoff | `stages/10-handoff.md` | The brand folder `README.md` for outside tools, photos still owed, then "bring an idea, or ask for a brainstorm, to idea-genome", or a clear stop |

The writing voice is asked in Stage 1 (1d, chat questions, no page); the voice kit, image rules and break-from-reality bank are written automatically (Stages 1 and 4). The visible journey the pages show lives in `page-template/journey.json`; keep it in step with this table.

Order matters: each stage reads the ones before it. Formats come before looks, because a look is judged by what it has to carry. The palette comes before fonts and everything after, because they are shown in it; once it's locked, the main and backup color editing are tuned to it automatically (no page). Tempo (Stage 6) comes after motion personality (Stage 5) but sets the music phrase length both use. Stages can be revisited later (`revisit.md`), not skipped; single steps marked skippable in `journey.json` can be (the chat question offers **Skip this step**).

## Brand folder and where to look

Same map in all three skills (brand-genome, idea-genome, video-genome). All brands live side by side under `Content Creation/Brands/`; each brand folder has the same layout and is found by its `Brand Genome.md`. Switching brands means pointing at a different brand folder; nothing else changes.

```
Content Creation/
  Brands/
    <Brand>/                    ← brand-genome creates this in Stage 0
      README.md                 ← for outside tools and agents: read order, folder map, rules (Stage 10)
      Start Here (read me).md   ← for the creator: plain-language index + links to every page
      START-HERE.md             ← Claude's resume file; sections: ## Brand, ## Ideas, ## Videos
      Brand Genome (visual).html ← offline copy of the Brand Genome page; + a link shortcut to the online page
      Brand Genome.md           ← Stage 9; every video skill reads it
      Who I Am.md               ← Stage 1
      00 Decisions/             ← one doc per stage (names below) + house-rules.md
      01 Brand Kit/             ← page-sources/, sound/, exports/
      02 Research/              ← channel-playbook.md
      03 Videos/                ← video-genome (episodes, results-log.md)
      04 Ideas/                 ← idea-genome (idea-bank.md, IDEA NNN <slug>.md)
      05 Style Gallery/         ← exploration images (never used in videos)
      06 Profiles/              ← banners, profile pictures, highlight covers
      07 Asset Library/         ← asset-index.md + footage/ screens/ images/ people/ audio/ scenes/ graphics/ docs/
      _archive/                 ← superseded files from an earlier run (<date>-superseded/); never used
```
Stage docs in `00 Decisions/`: `persona-card.md` (demo only), `formats.md`, `look.md`, `movement.md`, `sound.md`, `brand-kit.md`, `vertical.md`, `voice-kit.md`, `break-from-reality.md`, `image-rules.md`, `profiles.md`, `run-sheet.md`, `house-rules.md`.

**Find the brand, in this order:**
1. **Claude Project attached:** read its `START-HERE.md`. It names the brand, the brand folder path and where each skill stopped.
2. **Computer linked:** look in `Brands/` inside the connected folder; each subfolder with a `Brand Genome.md` is a brand (for brand-genome, a folder with only `START-HERE.md` or `Who I Am.md` is a partial brand to resume or start over, Stage 0). With no `Brands/` folder, search the connected folders (depth ≤ 3) for `Brand Genome.md` (older layouts). Several brands: ask which (AskUserQuestion, labeled by the Creator name in each Genome). A new brand gets a new folder `Brands/<Brand>/` (Stage 0).
3. **Neither:** keep the text files as project docs under the same relative paths (`00 Decisions/look.md`) and say once that files should be saved locally. Media can't live in the project.

**Folder rules:**
- Match folders by name and ignore the number. Older layouts may number them differently; use what exists. Never rename or move the creator's folders without asking.
- Create a missing folder with its number from the map; if that number is taken, use the next free one.
- Masters live on the computer. The project keeps copies of `START-HERE.md`, `Brand Genome.md` and `Who I Am.md`. Update the copy in the same turn as the master. If they disagree, the newer wins; say which.
- One Claude Project per brand. If the project's `START-HERE.md` names a different brand than the folder found, stop and ask.
- **`START-HERE.md` is shared.** It lives at the brand folder root (copy in the project) with three sections: `## Brand` (this skill writes only this one: mode, platforms, existing accounts, current stage, next step, how this creator decides, any tool chosen from Stage 7 on), `## Ideas` (idea-genome) and `## Videos` (video-genome). Never edit the other two.
- **Asset library.** Kit pieces stay in `01 Brand Kit/` (and profile images in `06 Profiles/`), but each final file gets a row in `07 Asset Library/asset-index.md` with `Type: kit`, its path relative to the library (`../01 Brand Kit/sound/sting.wav`). Reference photos and likeness refs go in `07 Asset Library/people/`, indexed with `Type: person`. IDs are `A` + 4 digits, never reused; a better version is a new row. Index header:
  `| ID | Type | File | Origin | Tool / cost | Rights | Tags | Used in | Added |`

## Tools this skill uses

| Need | Required? | Fallback |
|---|---|---|
| Multiple-choice questions (AskUserQuestion) | Yes | Numbered options in chat |
| Publishing voting pages with saved votes (`db`) | Yes | Pages with a "Copy answers for the chat" button whose text is pasted back |
| Web search | For Stages 1c, 2, 8 and 9 | Ask the creator to check handles and specs by hand; skip benchmarks |
| Subagents | No | Run the research passes one after another |
| A shell with Python 3 (builds pages) | Yes | None: every page is built with `page-template/build.py` |
| Headless browser (to render WAVs and stills from pages) | No | A download button on the page; the creator saves the file |
| Image, music and voice tools | No; asked about only in the brand kit (Stage 7) and the image question after the art-styles page (Stage 4) | Drawn in code, Web Audio sketches, benchmark photos and scenes |
| Node + HyperFrames (renders spatial-move clips, Stage 5c) | No | Skip 5c; the spatial library is marked owed and video-genome builds it later |
| The creator's computer | No | Everything kept in the project |

## Principles (why it works)

1. **No vocabulary needed. Picking beats describing.** Most creators have no words for styles. Show a voting page, let them vote, save the votes, read them back. Never ask "what style do you like?" in text. A page only when the choice must be seen or heard; words-only choices are questions in chat.
1a. **Fixed or library.** Every round is one of two kinds, and the page says which: a *fixed* pick (one answer, maybe a backup: palette, look, fonts, captions, kit) or a *library* (keep everything they like; the video skill picks per video: backdrops, moments, sounds, music, moves). Never make a creator pick "the one" from a library, or build a library out of a fixed pick.
1b. **Explain the consequence, then ask.** Every question, on a page or in chat, first says what the answer changes in their videos and that nothing happens without their say. A creator must never fear something will be done to their footage. The wording pattern is in `voting-pages.md`.
1c. **Never ask twice.** If two rounds would look the same to a creator ("didn't I just pick this?"), merge them or make the second a follow-up question. The round map in `voting-pages.md` is the result of that audit; keep it current.
2. **One variable per round, and the creator always knows where they are.** Never make them rule on several things at once; when a round mixes variables, split it. Every page carries the computed header (journey strip, stage, step dots, page type), a title that names the thing in plain words, one short line, the rule line above the cards, and the three-line bottom bar (what this page is for, picks so far, what's next). Nothing else above the cards (`voting-pages.md`, "Page copy and layout").
2a. **Plain hand-offs, every time.** Never say "Stage 4" or "next stage" on its own: say what just happened and what's next ("Look is done: your colors, filters and fonts are saved. Next: Movement, how things move on screen, 2 short pages."). After every page review, one recap line of what was decided. Every page is followed by the ready-for-review question in chat (`voting-pages.md`, "The chat around every page"), and every stage's first check-in says once that they can stop anytime.
2b. **Every picture shows what its name says.** Cover the name: if the picture alone doesn't give it away, rebuild the picture before publishing (`voting-pages.md`, "Before publishing any page").
3. **Lead with a recommendation.** Every option set has one marked **Our pick for you**, with one line of why. They can override.
4. **Show it where it lives.** Thumbnails at real feed size, tags over a real background, stings with their sound, vertical layouts in a phone frame. Out of context, people can't judge.
5. **No autoplay.** Motion and sound play on click only. Static mockups wherever motion isn't the question.
6. **Rejections become house rules.** Every "no" with a reason goes into `house-rules.md`, and the house rules bind every later stage.
7. **Don't assume the theme.** Ask why the content exists before naming what it's about. A channel that looks like recipes may really be a funnel for a catering business. Never frame the creator as a beginner at their own craft.
8. **The feel is a rule, not a vibe.** Once the content personality is picked (Stage 1), every plan, draft and self-review is judged against it. A scene that is clear and on-brand but not entertaining, when "entertaining" leads, has failed. When a topic can't be made entertaining without forcing it, the brand's fallback carries it (Stage 1b), most often top-tier spatial motion (Stage 5c).
8a. **Use it, log it, fix it.** Anything this skill gets wrong or lacks during a real run goes in the creator's skill-issues log (`SKILL-ISSUES.md` beside the skills' source, or `00 Decisions/skill-issues.md`) when it shows up, so the skill improves before its next release.
9. **Proof before admission.** In scripts and hooks, show the impressive thing first, then the humble line.
10. **Decisions are files, and the run can pause anywhere.** After each locked decision, update the stage doc and the `## Brand` section of `START-HERE.md` in the same turn. "Pause" saves where they are; "continue my brand" picks up from `START-HERE.md` in any new chat (`voting-pages.md`, "Pause and come back").
11. **The brand owns its language.** Motion, sound, vertical layout and voice are decided here, per creator. Video skills read them and never supply them. Where a video skill's own defaults differ, the Brand Genome wins.
12. **The brand is revisable.** Decisions are locked, not frozen. Any part can be changed later by asking in plain words: `revisit.md` locates it, reruns only that step the same way it was first decided, and changes nothing downstream without approval. When a draft shows a piece doesn't work on screen, run it rather than defending the old pick.
13. **Money and credits.** Exploration is free. Where a paid tool is an option (brand kit, generated pictures of the creator), offer the free path first; before any paid generation, name the tool, what it makes and the cost (from the tool's own price check, never a guess) and wait for approval.
14. **Every round is footage.** People will want to show how the brand was built. Build pages so a screenshot reads as a real choice: clearly different options side by side, with visible votes and notes.
15. **Current facts are checked live.** Platform specs (banner sizes, safe zones, character limits, disclosure rules) change. Look them up when the stage runs; the numbers in this folder are dated starting points.

## Auto mode, in one line

A real creator answers a short interview (who's on screen, what and why, who for, the feel, limits, name, likes and dislikes), then Claude fills every page as their proxy with a one-line why per pick, runs without waiting, and ends on the Brand Genome page for review; changes go through `revisit.md`. Full rules: `stages/00-setup.md` §6.

## Demo mode, in one paragraph

When the creator is made up (a demo, a class, a video about the skill), Stage 0 takes only a **one-line seed**. Stage 1 runs the real interview and Claude invents each answer in character as the question is asked. In Stage 1 the operator confirms each answer with one click (the interview is the footage). From Stage 2 on each round runs the same loop as for a real creator (page, persona votes, read-back, follow-ups, one-line summary), then waits for "go". The **persona card** is written at the end of Stage 1 as the interview's result. From then on Claude answers every question and fills every voting page as that persona, with votes saved under the persona's name and notes only where a person would leave one, one page at a time: never a second page before "go" (unless the operator says fast-forward). Anything the card doesn't cover is invented in character and added to it. The operator can veto anything and steers with the run controls. Full rules are in `stages/00-setup.md`. Everything else runs exactly as for a real creator, so the demo shows the real process.

## Finished means

Every row in the table is locked or skipped on purpose. `Brand Genome.md`, the Brand Genome page and its offline copy exist and match. The brand folder has its `README.md` for outside tools, and any photos still owed are listed in `07 Asset Library/people/PHOTOS-OWED.md` and under Pending in `START-HERE.md`. Every page's source is saved in `01 Brand Kit/page-sources/`. The `## Brand` section of `START-HERE.md` says what's next. Expect two long sessions for a real creator, and one for a demo.

## Credit line

What this skill hands the creator carries one line: `Made with brand-genome by jfships · youtube.com/@jfships_ai` (footer of every voting page and of the Brand Genome page; last line of `Brand Genome.md`). It's on by default. If the creator asks to drop it, drop it: pages take `"credit": false`, files leave the line out, and `credit: off` goes in `START-HERE.md` so later outputs skip it too. Never put it inside a video, thumbnail, post or profile the creator publishes.
