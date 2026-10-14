# Change something (revisit a locked decision)

Use when the creator (or a video skill, or a draft review) wants to change or correct any part of the Brand Genome, at any time after it was decided: "change my colors", "my handle is wrong", "the sting is too long", "I don't film outside anymore", "redo the captions", "I want a different backup font". This includes the interview (`Who I Am.md`).

**The rule: change only what was asked, the same way it was first decided, and nothing downstream without approval.**

## 1. Locate it

The creator names the change in plain words. Find the decision in the table below (decision → where it was decided → where it's written). If two decisions fit ("the text looks wrong" could be fonts, text style or captions), ask once with AskUserQuestion, naming each in plain words with the current pick ("Your fonts: Bebas Neue + Inter" · "How text sits on video: Color blocks" · "Captions: Bottom strip"). Then say in one line what will change and that everything else stays.

## 2. Run that decision's flow, exactly as in the first build

- Read the stage file for that step and run **only that step**, the same way: the same chat question for interview and words-only answers; the same voting page for anything seen or heard (copy the same example JSON, same kind, same buttons, the finalist flow where the first build had it).
- **Change mode on the page:** add `"change": "<the decision in plain words>"` to the page data. The header then says "Changing only: … Everything else stays as it is" and the journey shows every other stage as done. The ready-for-review question in chat offers **Keep what I have** (no change) in place of Skip. Put the current pick first with `"current": true` (tag "What you have now"; on a library round every kept item is `current` and starts as Keep in library (unvoted = still kept when you read back), followed by the new options); keep "Our pick for you" on the recommendation. Build it with `page-template/build.py` as usual (example: `examples/change-palette-tiles.json`).
- **Interview answers:** re-ask only the questions that cover the change (one AskUserQuestion, current answer shown first). Never rerun the whole interview. In demo mode, the persona answers in character and the persona card is updated.
- A real problem with the step itself (the options don't fit any more) can redo the step with fresh options, as in "redo [round]". Old pages stay readable.
- Keep the scope: if the creator starts naming other changes mid-flow, finish this one, then take the next one the same way.

## 3. Check what it touches, and ask

Before writing anything, look up the decision's downstream rows in the table. Split them:
- **Updates by itself:** the pick stays, only its colors, fonts or name change (new palette → the wordmark redraws in the new colors).
- **May need a new pick:** the old pick might not fit any more (switching to "no face on screen" → the profile picture and the vertical layouts).

Show both lists in one AskUserQuestion (multi-select, everything unticked by default; "Updates by itself" items marked Recommended). Say what each changes in their videos. Nothing downstream changes without a tick. Ticked "may need a new pick" items each run their own step in change mode, one at a time, after this one. Unticked items stay exactly as they are; note the mismatch under Changes ("Palette changed; wordmark kept in the old colors, by choice").

## 4. Write it everywhere, in the same turn

- The stage doc in `00 Decisions/`: the new pick, and a dated line under **Changes** (what changed, why, in the creator's words). The old pick is marked retired, never deleted.
- `Who I Am.md` (interview and identity changes) and the persona card (demo).
- `house-rules.md`, if a rejection with a reason came out of it.
- `Brand Genome.md`: the affected headings, plus a dated line under **Changes** (heading 16) so video skills see what moved; then rebuild the Brand Genome page, **republish it to the same link with its images, and overwrite `Brand Genome (visual).html`** (`page-template/offline.py`). If a file or link moved, update the brand folder's `README.md`.
- New kit files are new rows in `07 Asset Library/asset-index.md`; the old row notes `superseded by A0xxx`.
- The `## Brand` section of `START-HERE.md`: what changed and the date.

## 5. Close

One line: what changed and what didn't ("Palette changed to Warm clay. Wordmark and name tag redrawn. Everything else stays."). If photos are still owed (`07 Asset Library/people/PHOTOS-OWED.md`), add one line saying which. Videos already made aren't touched; video-genome uses the change from the next video on. If the change came from a video skill mid-episode, rebuild only what that episode needs.

## Where each decision lives, and what it touches

| The creator says something about… | Decision | Decided in | Written in | Touches (downstream) |
|---|---|---|---|---|
| who they are, their story, audience, why the content exists, proof | Core interview | Stage 1a | `Who I Am.md` | formats (may need a new pick), voice kit, bios, run sheet |
| being on camera or not, hands only, voice only | Who's on screen | Stage 1a | `Who I Am.md` | Look steps that run (route), text over photos, profile picture, vertical layouts, image rules (may need new picks) |
| how far they'll go, what's off limits | Limits | Stage 1a | `Who I Am.md` | formats, break-from-reality moments, run sheet |
| the feel, entertaining vs informative | Content personality | Stage 1b | `Who I Am.md`, Genome | motion feel, music, voice kit, formats (may need new picks); self-review scoring (updates by itself) |
| the name, the handle | Name + handle | Stage 1c | `Who I Am.md`, Genome | wordmark, name tag, sting, sound logo card, closing card, profile picture, banner, bios (update by themselves; the brand folder is renamed only if they say so) |
| how they write, tone of captions and titles | Writing voice | Stage 1d | `voice-kit.md` | bios, descriptions, run sheet (update by themselves) |
| what they love or can't stand, where and how they film | Taste + filming setup | Stage 4 (start) | `Who I Am.md` | color editing, filters, backdrops (may need new picks); recommendations on later pages |
| platforms, accounts, how often they post, language | Setup | Stage 0 | `START-HERE.md` (Brand), Genome | Vertical stage (added or dropped), profiles, banners, captions language |
| what works in their genre | Research | Stage 2 | `02 Research/channel-playbook.md` | advice only; nothing downstream changes by itself |
| the shows they repeat | Formats | Stage 3 | `formats.md` | series tag name, thumbnails, trailer plan, run sheet |
| how their footage looks, color editing, "the colors look off" | Color editing (incl. how strongly it's tuned to the palette) | Stage 4.1 (tuning: after 4.4) | `look.md` | the Genome page |
| filters for special scenes | Scene filters | Stage 4.2 | `look.md` | nothing |
| drawn or generated scenes, art styles | Art styles + image rules | Stage 4.3 | `look.md`, `image-rules.md` | break-from-reality moments |
| photos of me for image or video tools, likeness, "here are my photos" | Photo kit (add, replace or remove photos) | Stage 4, after art styles | `image-rules.md`, `07 Asset Library/people/` (`PHOTOS-OWED.md`) | page mocks and the Genome page use the new photos (update by themselves); other skills use the new set from the next picture on |
| colors | Palette | Stage 4.4 | `look.md` | color editing tuning, fonts preview, text style, captions, backdrops, extras, wordmark, name tag, series tag, sting, closing cards, thumbnails, profile picture, banner, vertical (all update by themselves) |
| fonts | Font set (and caption font) | Stage 4.5 (caption font: 4.7) | `look.md` | text style, captions, wordmark, name tag, series tag, sting, thumbnails, banner (update by themselves; wordmark may need a new pick if it was built on the old title font) |
| how text sits on video | Text style | Stage 4.6 | `look.md` | name tag, series tag (may need a new pick to match) |
| captions | Captions | Stage 4.7 | `look.md` | vertical captions (update by themselves) |
| backgrounds, extras, cutaways | Backdrops / Extras / Break-from-reality | Stage 4.8–4.10 | `look.md`, `break-from-reality.md` | nothing (libraries) |
| how things move, too slow, too bouncy | Motion feel (and the entrances on the same page) | Stage 5.1 | `movement.md` | scene changes (may need new picks), sting animation, music tempo |
| transitions | Scene changes | Stage 5.2 | `movement.md` | nothing (library) |
| music | Music library | Stage 6.1 | `sound.md` | sting and sound logo (may need a new pick if the key or tempo clashes) |
| sound effects | Sound effects | Stage 6.2 | `sound.md` | nothing (library) |
| the logo, the name graphic | Wordmark | Stage 7.1 | `brand-kit.md` | sting, closing cards, profile picture, banner, Genome page |
| the name label on screen | Name tag | Stage 7.2 | `brand-kit.md` | nothing |
| the show label, episode number | Series tag | Stage 7.3 | `brand-kit.md` | thumbnails (may need a new pick) |
| the intro, opener | Sting | Stage 7.4 | `brand-kit.md` | sound logo (it plays with the sting) |
| the jingle, the notes | Sound logo | Stage 7.5 | `brand-kit.md` | nothing |
| endings, outros | Ways to close a video | Stage 7.6 | `brand-kit.md` | nothing (library) |
| thumbnails | Thumbnail layouts | Stage 7.7 | `brand-kit.md` | nothing (library) |
| profile picture, banner | Profile picture / Banner | Stage 7.8–7.9 | `brand-kit.md`, `06 Profiles/` | profiles copy (highlight covers) |
| Shorts, Reels, TikTok layouts | Vertical layouts | Stage 8 | `vertical.md` | nothing |
| bios, descriptions, the checklist | Profiles copy / Run sheet | Stage 9 | `profiles.md`, `run-sheet.md` | nothing |

The visible stages and steps match `page-template/journey.json`; if that file changes, update this table.
