---
name: video-genome
description: "Make polished, on-brand YouTube episodes plus Shorts, Reels and TikTok cutdowns from any idea, brief, script, plan or footage, with any brand kit or none (included kits, or a Brand Genome if one exists). Runs a fixed step-by-step flow: word decisions asked one at a time in chat, visual and sound decisions on one page each, always with a main and a backup; plans from story libraries, builds spatial agency-level motion for screen demos, lays out every scene with real layout rules, tracks asset debt, builds graphics first or footage first, runs four gates of checks and logs results. Use for any channel video, cutdown or thumbnail."
---

# Video Genome

*video-genome by jfships · [youtube.com/@jfships_ai](https://youtube.com/@jfships_ai) · free (MIT)*

Make a creator's videos look, move and sound like their brand, and get them past a harsh review before anyone else sees them. The bar is professional and polished, with a look that's the creator's own, never a template.

## The flow is the product

This skill is worth its steps. Without them it's a chat that improvises, and that's useless here.
- **Start on the flow, every time.** The first message of a session says which step this is and starts it, even when the creator arrives with a finished plan, a handoff or a script. Those fill steps (`plan/intake.md`); they never skip them. A resumed episode runs Step 0 in one line and jumps to the first step whose gate hasn't passed (`plan/intake.md`, "A previous plan…").
- **Chat can wander.** Answer questions, ad-lib, follow the work where it needs to go. Then steer back: use the step, its decision pages and its gate. If a conversation produced a decision, write it into the step it belongs to.
- **Tracker line** at the top of every reply that moves the work: "Plan · decision 4 of 13 · about 30% done". Stage hand-offs in plain words: what was just locked, what's next, about how long.
- **One decision at a time.** Each decision is one question in chat or one page (`decision-pages.md`). Words are decided in chat; pages are only for what has to be seen or heard. Never two decisions on one page, never the next page before the current one is reviewed.
- **Know what the video is about.** Before planning, one confirmed line: the topic, who it's for, the demo subject and the output, kept apart (`plan/intake.md`). When the creator says the plan has drifted, recheck that line first.
- **Plain words.** Internal labels (step codes, beat or layout codes, slugs, catalog letters) never reach the creator. Say where (time + the line they say there) and what changes.

## The brand file

Every brand decision comes from **the brand file**: `Brand Genome.md` if the brand folder has one, otherwise `Brand Sheet.md`, made in Step 0 from the creator's own kit or an included kit (`setup/brand-intake.md`). Both use the same headings; wherever this skill says "the brand", read that file: packs (colors, fonts), grade, title styles, motion table, sound lanes, kit placements, vertical rules, voice, break-from-reality moments, run sheet, house rules.

This skill brings the craft (plan, lay out, build, time, mix, check); the brand brings the taste; the Idea Record brings the what and why. Where they differ, the brand wins on colors, fonts, kit pieces and house rules. When none of the brand's graphics fit a moment, propose your own inside those limits and label them (`craft/brand-fit.md`); at session close they go to the brand review (`review/session-close.md`).

**Content personality is a rule, not a vibe.** It's in the brand file, ranked. Every beat must earn its seconds by delivering it. Judge like a stranger scrolling, not like the person who built it.

**Demo creators** (made-up personas) can't film; `setup/tools.md` §1 has the three ways to give them a voice or face.

## Where this sits

```
brand          →  brand-genome: Brand Genome.md (or a Brand Sheet made in Step 0)   once per brand
content idea   →  idea-genome: IDEA NNN <slug>.md                                   per video: what and why
content plan   →  video-genome: intake → plan → asset debt                          per video
editing        →  video-genome: build → sound → checks → deliver → results log
```
Publishing is done by hand for now; this skill stops at finished files and picks up again for the results log.

**No Idea Record?** Whatever they brought goes through intake (`plan/intake.md`). With nothing at all, offer idea-genome (Recommended); if they want to go straight on, draft the Idea Record fields yourself and confirm them on one page (`plan/intake.md`), then save it to `04 Ideas/` with the next ID before planning. Every episode has an `idea.md`.

## Flow

| Step | File | Gate |
|---|---|---|
| 0a. Brand | `setup/brand-intake.md` | A brand file exists and is read (Genome, Sheet, or picked kit) |
| 0b. Tools | `setup/tools.md` | Brand folder found, tools ready, HyperFrames up to date, render capacity stated |
| 0c. What they brought | `plan/intake.md` | The "this video is about" line confirmed; every run-sheet item marked taken or open; taken items confirmed in chat |
| 1. Plan | `plan/run-sheet.md` + `plan/story-libraries.md` | Every open item decided, one question or page each; gate 1 passes |
| 2. Asset debt | `plan/asset-debt.md` + `craft/asset-library.md` | Everything owed listed, library searched, creator's list sent |
| 3a. Graphics first | `paths/graphics-first.md` | Draft reviewed → recording → cut → placement → rebuild |
| 3b. Footage first | `paths/footage-first.md` | Shoot brief → footage → cut → style of the edit → moments → build |
| 4. Sound | `craft/sound.md` | Levels metered, mix to target |
| 5. Checks | `review/checks.md` | Gates 2–4 pass, debt is zero, fresh reviewer scores 8+ |
| 6. Deliver | `craft/deliverables.md` + `review/session-close.md` | Every file meets its platform's spec; brand review done |
| 7. Results | `learn/results-log.md` | 48 h and 28 d numbers logged after the creator publishes |

Every session ends with `review/session-close.md`, whatever step it stopped on.

**Pick the order in Step 1** (one AskUserQuestion):
- **Graphics first:** build a polished motion draft, the creator records over it from bullet cues, then the video is rebuilt around their real words. Best when the video is mostly graphics, or when the creator is new to camera and needs a pacing guide.
- **Footage first:** they film first (a talking head, a vlog, a screen recording), then graphics are built around the footage. Best when they already film, when the story happens on camera, or for quick turnarounds.

Recommend one from the format and video type. Steps 0–2 and 4–7 are the same for both.

Read when their part starts:
- `decision-pages.md` and `page-template/`: every decision page (read before the first one of a session)
- `plan/story-libraries.md`: the story stack libraries and how to combine them
- `craft/layout.md`: where things sit on screen; read before building any scene
- `craft/brand-fit.md`: when the brand's graphics don't fit a moment
- `craft/asset-library.md`: the brand's central asset library and index
- `craft/motion.md`: timing, layers, camera, music grid, transitions, text sizes, anti-slideshow
- `craft/graphics-library.md`: the catalog of moves, with each one's fit
- `craft/spatial/README.md`: spatial moves (3D camera, depth, screens in space) with working sources; read before planning the look of any screen demo or explainer
- `craft/uniqueness.md`: how a video stays recognizably theirs
- `craft/vertical.md`: Shorts, Reels and TikTok
- `craft/thumbnails.md`
- `craft/sound.md`
- `craft/deliverables.md`
- `setup/gotchas.md`: known traps; read before the first build of a session

## Principles

1. **Follow the flow; decide one thing at a time.** Every open decision is one AskUserQuestion (anything decided in words) or one page (only when it has to be seen or heard), with a Recommended option and one line of why. Several options → Main, Backup and Alternatives, all written to `plan.md`.
2. **Show, don't describe.** Pair every script with a rough draft video. People react line by line and can't picture the whole from text.
3. **Plain words, always with context.** Where in the video (time + the line said there), what's on screen now, what the decision changes. No internal labels.
4. **Proof before admission.** Open on the best real material, then the humble line.
5. **Never invent.** No made-up numbers, quotes, prices, results or testimonials. Claims trace to Proof in the identity doc. Illustrative stand-ins are labeled in the plan.
6. **Show the real thing.** When the script says they built, made or decided something, show the real artifact (screens, pages, footage, the object), each one visibly different.
7. **Every scene is laid out, not placed.** Placement is re-decided per scene from what's on screen (`craft/layout.md`); every still passes its check.
8. **Every graphic must be readable on a phone and earn its place.** A graphic that illustrates a line literally (boxes for "tools") is cut or replaced with something funny or concrete.
9. **Converge on stills, not renders.** Stills take seconds and renders take minutes. Fix layout in stills first.
10. **Score harshly, fix the worst three, repeat.** A fresh reviewer that didn't build the video scores it before the creator sees it.
11. **Money and credits.** Before any paid generation (music, voices, images, video), name the tool, what it makes and the cost from the tool's own price check, and wait for approval unless the brand's budget pre-approves it.
12. **Disclose what must be disclosed.** Realistic synthetic people, voices or events get the platform's label (check current rules).
13. **Keep everything.** Old renders are versioned (`-v1`, `-v2`), never overwritten. Each episode keeps `log.md`: decisions, tool versions, review scores, anything outside the brand.
14. **Reuse before making.** Search the brand's asset library before shooting, generating or building anything; file every reusable result back into it.
15. **No build without a record.** Every episode has an `idea.md`, a `plan.md` with a story stack, and a `debt.md`.
16. **Entertaining first; motion carries what jokes can't.** When a beat is hard to make entertaining without forcing it, spatial motion carries it (brand file §2 fallback, `craft/spatial/`). The bar is a top agency's launch film, not a slideshow with easing.
17. **Use it, log it, fix it.** Anything this skill got wrong or lacked during real work goes in the creator's skill-issues log (`review/session-close.md`) the moment it shows up, so the skill improves before the next release.

## Brand folder and where to look

All brands live side by side under `Content Creation/Brands/`; each brand folder has the same layout and is found by its brand file (`Brand Genome.md` or `Brand Sheet.md`). Switching brands means pointing at a different brand folder; nothing else changes.

```
Content Creation/
  Brands/
    <Brand>/
      Start Here (read me).md   ← for the creator
      START-HERE.md             ← Claude's resume file; sections: ## Brand, ## Ideas, ## Videos
      Brand Genome.md | Brand Sheet.md   ← the brand file
      Who I Am.md
      00 Decisions/             ← brand decision docs, house-rules.md, genome-deviations.md
      01 Brand Kit/             ← wordmark, sting, sound logo, end card, page sources
      02 Research/              ← channel-playbook.md
      03 Videos/
        results-log.md
        EP NN <slug>/
          idea.md               ← copy of the Idea Record
          plan.md               ← run sheet + story stack, approved
          debt.md               ← asset debt
          RECORDING.md | SHOOT.md
          log.md                ← decisions, tool versions, review scores
          work/                 ← sources, transcripts, scripts, build files
          _review/              ← stills, contact sheets, review-log.md
          out/                  ← renders, versioned
          shorts/  thumbs/
      04 Ideas/                 ← idea-bank.md, IDEA NNN <slug>.md (idea-genome)
      05 Style Gallery/
      06 Profiles/
      07 Asset Library/         ← asset-index.md + footage/ screens/ images/ people/ audio/ scenes/ graphics/ docs/
```

**Find the brand, in this order:**
1. **Claude Project attached:** read its `START-HERE.md`. It names the brand, the brand folder path and where each skill stopped.
2. **Computer linked:** look in `Brands/` inside the connected folder; each subfolder with a brand file is a brand. With no `Brands/` folder, search the connected folders (depth ≤ 3) for `Brand Genome.md` or `Brand Sheet.md` (older layouts). One brand: use it. Several: ask which (AskUserQuestion, labeled by the Creator name in each brand file). None: a new brand folder, and Step 0 makes its Brand Sheet (`setup/brand-intake.md`).
3. **Neither:** keep the text files as project docs under the same relative paths (`03 Videos/EP 04 cheap-tacos/plan.md`) and say once that files should be saved locally. Media can't live in the project.

**Folder rules:**
- Match folders by name and ignore the number. Older layouts may number them differently; use what exists. Never rename or move the creator's folders without asking.
- Create a missing folder with its number from the map; if taken, the next free number. Episode numbers continue from the highest `EP NN` in `03 Videos/`.
- Masters live on the computer. The project keeps copies of `START-HERE.md`, the brand file, `Who I Am.md`, `07 Asset Library/asset-index.md`, and the active episode's `idea.md`, `plan.md` and `debt.md`. Update the copy in the same turn as the master. If they disagree, the newer wins; say which.
- One Claude Project per brand. If the project's `START-HERE.md` names a different brand than the folder found, stop and ask.
- Write only the `## Videos` section of `START-HERE.md`: active episode, step, open decision page link, debt summary line, next action, date.

## Bundled tools (`tools/`)

| Tool | Does |
|---|---|
| `grade.py` | Applies the brand's grade recipe to footage or stills |
| `brand_check.py` | Lists colors and fonts in a build that aren't in the brand's pack |
| `remap_words.py` | Moves word times from the raw take onto the cut |
| `mix.py` | Voice clean-up, music ducked under voice, SFX, sound logo, loudness master |
| `reframe_vertical.py` | 16:9 footage → 9:16, following the speaker's head |
| `talking-head/` | Transcription, inspection, background blur/zoom, mattes, speaker-to-side, captions, composite, thumbnails, motion engine |

## Credits

Layout rules from EBU R95 safe areas, platform safe-zone guides, cinematography framing references and compositional-balance guides (sources in `craft/layout.md`). Decision pages adapted from a brand-building page template by the same author. Story libraries compiled from public creator and marketing references (hook, script and UGC guides, retention-editing guides, story-structure references, YouTube packaging research). Craft rules adapted from a creator's own production skill, from iart-ai/motion-design-skills (MIT), LottieFiles' motion-design skill, bang-motion's anti-slideshow rules and hculap's scored critique loop. The bundled talking-head tools in `tools/talking-head/` are built on motion-broll by Barty-Bart (MIT); its license and the Geist font license (SIL OFL 1.1) ship with them. HyperFrames by HeyGen is fetched at run time, not bundled.

## Credit line

What this skill hands the creator carries one line: `Made with video-genome by jfships · youtube.com/@jfships_ai` (footer of every decision page). It's on by default. If the creator asks to drop it, drop it: pages take `"credit": false`, files leave the line out, and `credit: off` goes in `START-HERE.md` so later outputs skip it too. Never put it inside a video, thumbnail, post or profile the creator publishes.
