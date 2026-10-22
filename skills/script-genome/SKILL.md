---
name: script-genome
description: Write and check short-video scripts. Turns a creator's raw words (notes, voice memo, transcript, a long video) into a 20–60 s Reel/Short script card, beat by beat, with hook, shape or story arc, retention, ending and the edit intent per line; and checks a finished script (legal, platform, accuracy and clarity gates, craft notes, no score). Use when someone asks to write, tighten, restructure or check a script, hook, rehook, loop or ending for a Reel, Short or TikTok, or says "make this a script" or "check my script". video-genome and idea-genome call it for the script step.
---

# script-genome: raw words → a script card, and a check for finished scripts

*script-genome by jfships · [youtube.com/@jfships_ai](https://youtube.com/@jfships_ai) · free (MIT)*

The script step of the package:

```
brand          →  brand-genome   →  Brand Genome.md
content idea   →  idea-genome    →  IDEA NNN <slug>.md
script         →  script-genome  →  script card (one row per beat)   ← this skill
content plan   →  video-genome   →  plan → debt → build → review → deliver
```

**Routes.** Route 1: vertical short video, 20–60 s (Instagram Reels first; Shorts and TikTok use the same cards). Route 2: long-form YouTube scripts: not built yet; say so and fall back to video-genome's long-form run sheet (if video-genome is installed; otherwise stop at a beat outline).

**Two jobs.**
- **Write (job A):** organize and tighten the creator's own words into a script card. `write/`.
- **Check (job B):** read a finished script and return a verdict, gates first, craft as notes. `check/`.

Works on its own (no brand folder needed) and inside the package.

## What it believes (read once)
1. **Nothing here is a rule except the gates and one design rule (no outro, thanks, subscribe ask or end card).** Lines written as "never" or "max" are strong defaults: break one with a reason written in the card. Hooks, shapes, arcs, endings are options with mechanics. Pick by the idea, the material and the stage the account is at.
2. **Nobody has tested any of this on 20–60 s Reels.** Every card carries an evidence grade. Use the creator's own Insights to decide (`learn/log.md`).
3. **The creator's words first.** Draft from their phrasing; new lines are marked `new`; never invent a fact, number, experience or quote.
4. **Judge functions, not shapes.** Is it for someone within ~3 s? Is the promise paid off? Is there proof? One ask or none?
5. **The edit is part of the script.** Every beat names what the screen and sound do and which spoken word fires it (`card/schema.md`). video-genome and the brand dress those codes.

## Evidence voice
Use grades internally. Tell the creator only when a pick rests on a weak basis (grade SINGLE, VENDOR or INFERENCE: card line `Flag: weak`), in one plain line: "This one is one creator's habit, not tested. Fine to try; we'll see in your numbers." Never cite folklore as fact (list in `sources.md`).

## Brand folder: what to read (if present)
Same map as the other genome skills (`Brands/<Brand>/`). Read only what the step needs:
| File | Why |
|---|---|
| `00 Decisions/house-rules.md` | Hard no's for this brand (beat card lint reads them) |
| `00 Decisions/voice-kit.md`, `Who I Am.md` (Voice, Proof) | Voice, signature phrases, real proof; voice-kit's **Pace log** (date · video · mode · words/s) sets the planning pace (`write/budget.md`). Create the section on first use |
| `00 Decisions/line-ledger.md` | Lines the creator kept or cut before, with reasons |
| `04 Ideas/swipe-library.md` | Only entries marked CRAFT or matching this video's type; borrow only what the creator flagged (swipe-file skill) |
| `00 Decisions/growth-plan.md`, section `## Growth state` (written by growth-genome; a YAML block) | `stage`, `post_job_now`, `audience`, `offers`, `cta_allowed_now`, `cta_not_yet`, `house_bans`. Endings and asks come only from `cta_allowed_now`; `house_bans` always win; the slot's job in the Idea Record overrides `post_job_now` for that post (`catalog/endings.md` §4) |
| `03 Videos/results-log.md` | Last 3 shapes/arcs/hooks (variety), past results |
| The Idea Record (`IDEA NNN`) | Message, angle, feeling, shape if already picked |
No growth plan → say once that growth-genome set-up would set this, then use the default stage "no audience yet": endings payoff-stop, button, deadpan-hold, callback, verbal-loop, visual-loop, plus an optional situational send-line. No comment-a-word, follow or lead asks unless the creator asks for one.

## Job A: write (flow)
Tracker line on every reply that moves the work: "Script · step 3 of 7".
| Step | What | File |
|---|---|---|
| 1. Intake | Take the raw words verbatim. Ask at most 3 things if missing: who it's for, the one thing they'll know or can do after, the proof. Fill the worksheet. | `write/intake.md` |
| 2. One idea | Core claim in one sentence ≤20 words; one-idea tests; extra ideas go to a parked list (or a series), never smuggled in. | `write/intake.md` |
| 3. Pick | Selector: 2 candidates + 1 wildcard, each offered as shape/arc (plus optional operator and line rule) + a two-line example in their topic + what it changes. Creator picks (AskUserQuestion). After the pick: load the chosen card(s) (skeleton, twin arc if any, hook, ending) and fill the full selector header (hook, ending, clash checks) for the chosen candidate only. Hook: write 2–3 three-layer versions, ranked. | `catalog/selector.md` + `catalog/hooks.md` + `catalog/endings.md`; then the chosen card(s) |
| 4. Outline | Beats with % / seconds / word budget; hook, re-hook, payoff and ending marked. Re-hook beat for runtimes ≥30 s. | `write/budget.md`, the card, `catalog/retention.md` (re-hook device card, ≥30 s) |
| 5. Draft | Build each beat from the creator's own phrases; every line tagged `src` (take / memo / chat / new). | `write/passes.md` |
| 6. Passes | cut → specifics → show → verbs → hedges/AI-tells → hook → ending → facts → read-aloud timing → keep-voice diff | `write/passes.md`, `voice/` |
| 7. Card | Script card with edit intent per beat; run lint; show the creator the card + the before/after list + parked ideas + facts to verify. | `card/schema.md`, `card/triggers.md`, `card/lint.md` |
Then: if a video is being made, hand the card to video-genome (Shorts track item 6 / long-form run-sheet step 6) if it is installed; otherwise the card is the edit brief for the creator or editor. Save the card to the video folder as `script.md` (or `04 Ideas/SCRIPT NNN <slug> vN.md` before a video folder exists). Each new version is a new file (`v2`, `v3`); never overwrite.

## Job B: check (flow)
1. Read the script as given (any format). Convert to beats internally; don't rewrite it.
2. Load `check/gates.md`, `check/craft.md`, `check/report.md`, `write/budget.md` (for C3), `voice/tells.md` (for S4) and the brand's `house-rules.md` if present. Run the gates (hard), then the function read, then craft notes, then house rules, then the `card/lint.md` items that apply to a plain script: K1–K4, K6 (hook screen text vs caption, if both are given), K11, K12, K14 (K5, K7–K10, K15 need card fields; K15's facts are covered by gate A3).
   - Alternatives (several hooks or endings): count the main one (first listed) for words and C3; report the alternatives separately, one line each.
   - Elided text ("…", "[line here]"): C3 = NEEDS-INFO; count what is written and say what's missing.
   - An ask outside the stage policy (`catalog/endings.md` §4.2): a craft note + a house flag, not a gate, unless it is L9 engagement bait.
3. Report in `check/report.md` format. Verdict: FIX FIRST / NEEDS YOU / CLEAR TO RECORD. ≤5 fixes, smallest first, gate items first. Never a score, never "wrong shape".
4. After a fix round, re-check only the changed lines.

## Load order (token budget)
Load only the cards you need: find a card by its `### <slug> ·` heading and read that card, not the whole file (`catalog/selector.md` has a card index). Never load all catalogs. `sources.md` only when asked where something comes from.

## Files
- `write/`: `intake.md` (worksheet, one-idea tests, converting lists and long videos), `passes.md` (the passes, keep-voice rules), `budget.md` (pace, words per runtime, beats per runtime).
- `catalog/`: `selector.md`; hooks (`hooks.md`, `hooks-psych.md`, `hooks-unusual.md`); `shapes.md`; arcs by family (`arcs-setback.md`, `arcs-fall.md`, `arcs-rise.md`, `arcs-curiosity.md`, `arcs-ladder.md`, `arcs-argument.md`, `arcs-containers.md`, `arcs-operators.md`); `retention.md`; `endings.md`.
- `card/`: `schema.md` (the script card, the contract with video-genome), `triggers.md` (edit move ↔ script trigger, timing, sound, pacing patterns), `lint.md`.
- `check/`: `gates.md`, `craft.md`, `report.md`.
- `voice/`: `delivery.md` (spoken-copy rules, notation), `tells.md` (sounds-like-AI / sounds-like-a-script flags).
- `learn/log.md`: what to log per posted video and how to compare hooks fairly at small numbers.
- `sources.md`: where the cards come from; folklore not to repeat.

## Who calls it
- **idea-genome** `short-form.md` S4–S8: shape (selector), hook (three layers), word budget, last line, send reason.
- **video-genome** Shorts track item 6 and long-form run-sheet step 6: the script card; gate 1 reads the card header; the beat brief reads each beat's edit intent and dresses it in the brand.
- Called on its own: "write me a Reel about…", "tighten this script", "check my script".

## Model
Write (picks, hooks, drafts) on the strongest model available; checks, lint and fix rounds on the everyday model.

## Credit line
What this skill hands the creator carries one line: `Made with script-genome by jfships · youtube.com/@jfships_ai` (last line of a saved script card or check report). On by default; drop it when asked (`credit: off` in `START-HERE.md`). Never inside a video, caption or post.
