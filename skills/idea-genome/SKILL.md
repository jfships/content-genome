---
name: idea-genome
description: Turn a theme, a half-formed thought or nothing at all into a scored, on-brand video idea with an angle and titles, saved as an Idea Record that video-genome plans from. Runs a brainstorm session when the creator arrives with no idea. Use when someone wants video ideas, topics, an angle, titles, or says "I have an idea for a video". Also plans Shorts/Reels/TikToks (new, or mined from a long video), one record per Short.
---

# idea-genome: from nothing (or a hunch) to an Idea Record

*idea-genome by jfships · [youtube.com/@jfships_ai](https://youtube.com/@jfships_ai) · free (MIT)*

The middle skill of three:

```
brand          →  brand-genome  →  Brand Genome.md      (once per brand: how it looks, moves, sounds, talks)
content idea   →  idea-genome   →  IDEA NNN <slug>.md   (per video: what it is and why anyone clicks)
content plan   →  video-genome  →  plan → debt
editing        →  video-genome  →  build → review → deliver → results log
```

**Scope.** This skill decides *what* a video is and *why it gets clicked*: theme, idea, angle, audience, the proof that backs it, the opening hook (ranked), and 3 titles, all developed with the creator. It does not write the script, pick the story arc or plan beats (video-genome's plan does that, because those depend on the video type and the footage). It never builds media.

**Shorts are the exception on shape.** For a Short / Reel the shape *is* the idea, so it is settled here (`short-form.md`): one shape, the hook word for word, the word budget and the exact last line.

**Every video starts from a developed Idea Record**, including when the creator brings their own idea. Their idea skips the brainstorm; it never skips development, the Genome cross-check, the completeness check or the record.

## Brand folder and where to look

Same map in all three skills. All brands live side by side under one root; each brand folder has the same layout and is found by its `Brand Genome.md`. Switching brands means pointing at a different brand folder; nothing else changes.

```
Content Creation/
  Brands/
    <Brand>/                ← one per brand
  (anything else here, e.g. tools, is not a brand; ignore it)

<Brand>/
  Start Here (read me).md   ← for the creator
  START-HERE.md             ← Claude's resume file; sections: ## Brand, ## Ideas, ## Videos
  Brand Genome.md
  Who I Am.md
  00 Decisions/             ← brand-genome stage docs, house-rules.md
  01 Brand Kit/
  02 Research/              ← channel-playbook.md
  03 Videos/
    results-log.md          ← written by video-genome; read here for scoring
    EP NN <slug>/           ← idea.md, plan.md, debt.md, work/, _review/, out/, shorts/, thumbs/, log.md
  04 Ideas/
    idea-bank.md            ← every candidate ever raised, with status
    IDEA NNN <slug>.md      ← one Idea Record per idea that passed
  05 Style Gallery/
  06 Profiles/
  07 Asset Library/         ← every reusable file for this brand + asset-index.md (video-genome owns it)
```

**Find the brand, in this order:**
1. **Claude Project attached:** read its `START-HERE.md`. It names the brand, the brand folder path and where each skill stopped.
2. **Computer linked:** look in `Brands/` inside the connected folder first; each subfolder with a `Brand Genome.md` is a brand. If there's no `Brands/` folder, search the connected folders (depth ≤ 3) for `Brand Genome.md` (older layouts). One brand: use it. Several: ask which (AskUserQuestion; label each by the Creator name in its Genome). None: no Genome (see below). A new brand gets a new folder `Brands/<Brand>/`, created by brand-genome.
3. **Neither:** keep everything as project docs under the same relative paths (`04 Ideas/IDEA 003 cheap-tacos.md`) and tell the creator once that files should also be saved locally.

**Folder rules:**
- Match folders by name and ignore the number (`Ideas`, `Videos`, `Research`). Older channels may number them differently; use what exists. Never rename or move the creator's folders.
- Create a missing folder with its number from the map; if that number is taken, use the next free one.
- Masters live on the computer. The project keeps copies of `START-HERE.md`, `Brand Genome.md`, `Who I Am.md`, `04 Ideas/idea-bank.md` and the active Idea Record. Update the copy in the same turn as the master. If they disagree, the newer wins; say which.
- One Claude Project per brand. If the project's `START-HERE.md` names a different brand than the folder you found, stop and ask.
- Write only the `## Ideas` section of `START-HERE.md`: active idea ID, step, next action, date. Never edit `## Brand` or `## Videos`.

**No Genome?** Recommend brand-genome first; ideas can't be scored for fit without it. If the creator declines, ask the three things scoring needs (who it's for, the ranked personality, what they can prove) and mark the record `genome: none`. Every step still runs; Steps 7 and 9 use those three answers plus the creator's own stated rules instead of the Genome.

## Read first

`Brand Genome.md` sections Creator, Why and feel, Research, Formats, Voice and House rules; `Who I Am.md` (Proof, truth rules, story beats, opinions); `02 Research/channel-playbook.md`; `04 Ideas/idea-bank.md`; `03 Videos/results-log.md` if it exists.

## Flow

| Step | File | Output |
|---|---|---|
| 0. Load + explain | this file | Channel found, Genome and bank read, flow explained to the creator |
| 1. Entry | below | Brainstorm, theme, own idea, or bank pick |
| 2. Candidates | `catalog/sources.md` | 10–20 raw candidates in the bank (brainstorm and theme paths only) |
| 3. Develop | `develop.md` (a Short: `short-form.md`) | The pick, researched and worked through with the creator (ALL paths) |
| 4. Angles | `catalog/angles.md` | Best angle + one alternative |
| 5. Titles | `catalog/titles.md` | Long video: 3 titles, each with what the thumbnail must show. A Short: cover line + working title (`short-form.md`) |
| 6. Hook concepts | `develop.md` §Hooks | Long video: 2–3 first-10-second concepts, ranked. A Short: hook text + first frame + spoken line, word for word (`short-form.md`) |
| 7. Genome cross-check | `checks.md` | Fits listed; every conflict ruled by the creator |
| 8. Completeness check | `checks.md` | Every item done, or open with an owner |
| 9. Score | `scoring.md` | Explained once, then scored with one line of evidence per criterion |
| 10. Idea Record | `templates/idea-record.md` | `04 Ideas/IDEA NNN <slug>.md` |
| 11. Handoff | below | "Take IDEA NNN to video-genome" |

No path skips Steps 3, 7, 8 or 9. Writing the idea down is not developing it.

### 0. Load + explain

After loading, tell the creator in 3–4 plain lines, before any question:
1. What this does: turns their idea (or none) into one developed, scored video idea.
2. The steps, in plain words: research it, a few rounds of questions to shape it, angle + titles + opening, check it against their brand rules, score it.
3. Claude's role: brings research and options, recommends one each time; the creator decides.
4. What they approve at the end: the Idea Record. Nothing gets made until then.

### 1. Entry (one AskUserQuestion)

- **I have an idea:** capture it in their words, then go to Step 3 (Develop) with it as the pick. Brainstorm candidates are skipped; development is not.
- **I have a theme, not an idea:** run Step 2 limited to that theme, then Develop the creator's pick.
- **Nothing, brainstorm with me:** theme check-in in `catalog/sources.md`, Step 2 across the channel's pillars, creator picks 1 (or a short queue) from the best 5, then Develop.
- **Pick from the bank:** show the top 5 `parked` ideas in `idea-bank.md` with last score and what would raise it; the pick goes to Develop.
- **A Short / Reel** (new, or a moment from a long video): go to `short-form.md`. It replaces develop.md's structure and hooks parts for this Short; checks, scoring and the record still run.

**One Idea Record per Short.** Five Shorts are five records, each with its own message, shape, checks and score. The first-10-seconds hook and the 3 titles with thumbnails are long-form rules; on a Short the hook text, first frame and cover line do that job.

### Session rules (all steps)

- **Plain setup on every option.** Each AskUserQuestion option carries a one-line plain setup of what choosing it leads to. Never assume the creator remembers a term, a file or an earlier step; name the thing.
- **Ask in rounds** of up to 4 questions, each with a Recommended option first and one line of why.
- **Look things up live, on every path.** Demand, examples, competitor videos and news are researched at run time with sources, including for the creator's own idea. Never from memory.
- **Volume, then cut** (brainstorm). Raise 10–20, show the best 5. Every candidate goes in `idea-bank.md`, kept or not, including splits.
- **Brand fit is a filter, not a vibe.** Drop anything that breaks a truth rule, and say which rule. Other Genome conflicts are not silent drops: they go to the creator in Step 7.
- **Proof-limited.** Missing proof is marked `needs proof: <what>`, not dropped. Check `07 Asset Library/asset-index.md` first: proof there counts as proof we have.
- **Likeness check before suggesting a generated creator.** Before offering any option that uses an AI-generated version of the creator (avatar, look-alike, costume swap on a generated body), check whether reference photos exist (Genome likeness section or the brand's asset index). If none, say so in the option ("needs ~10 reference photos you don't have yet") or leave it out.
- **Topic, demo subject and output stay apart.** When a video shows something being made (a tool demo, a makeover, a build), write down separately what the video is about (the topic the viewer gets), what it's shown on (the demo subject) and what comes out (the output), and confirm that line with the creator before developing. Ideas drift when the demo or the output quietly becomes the topic.
- **The creator's words for things.** Use the names the creator uses for their own steps and tools; if they correct a term once, use the corrected one everywhere after.
- **Use it, log it, fix it.** Anything this skill gets wrong or lacks during a real run goes in the creator's skill-issues log (`SKILL-ISSUES.md` beside the skills' source, or `00 Decisions/skill-issues.md`) when it shows up.
- **Formats come from the Genome.** Each idea names the kept format it fits; one that fits none is a one-off or a reason to revisit formats in brand-genome.
- **Never invent** numbers, results, quotes or customer stories. Shape examples are labeled as examples.
- **Don't build media.** Visual options for voting are reference images or quick generated sketches labeled as such, never finished assets.

### 11. Handoff

Set the record's `status: ready`, update the bank and `## Ideas` in `START-HERE.md`, then say in one line: "IDEA NNN is ready. Bring it to video-genome to plan and build." Mention any ranked hooks and the `## Versions to test` table video-genome runs first. If video-genome isn't installed, say so and stop.

## Files this skill writes

- `04 Ideas/idea-bank.md` from `templates/idea-bank.md`: one row per candidate, status `raw / shortlisted / ready / parked / rejected / made`.
- `04 Ideas/IDEA NNN <slug>.md` from `templates/idea-record.md` (long template, or its Short variant for a Short). IDs never repeat; NNN is the next number in the bank.
- `00 Decisions/genome-deviations.md` from `templates/genome-deviations.md`: created on the first approved exception if missing; one row per exception. Record only; never changes the Genome.
- `START-HERE.md` `## Ideas` section.

When video-genome turns a record into an episode it copies it to `03 Videos/EP NN <slug>/idea.md` and sets the bank row to `made` with the episode number.

## Credit line

What this skill hands the creator carries one line: `Made with idea-genome by jfships · youtube.com/@jfships_ai` (last line of every Idea Record; footer of any voting page). It's on by default. If the creator asks to drop it, drop it: pages take `"credit": false`, files leave the line out, and `credit: off` goes in `START-HERE.md` so later outputs skip it too. Never put it inside a video, thumbnail, post or profile the creator publishes.
