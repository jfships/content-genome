# Stage 0: Setup and demo mode

Run these in order. Nothing in this skill costs the creator anything until Stage 7, and even there every piece has a free path. **Don't ask about image, video or voice tools here.** Those come up only at the stage that could use one (7 brand kit, and the image question after the art-styles page in Stage 4), with the free path offered first.

Every question follows the voice in `../voting-pages.md`: say what the answer changes, then ask.

## 1. Real or demo?

Ask with AskUserQuestion:
- **Real creator:** the person answering is the creator.
- **Demo:** a made-up creator, run by an operator (for a video, a class, a test).
- **Auto:** a real creator answers a short interview, then Claude makes every call (§6).

In demo mode, run §5 (the seed) first, then §2 platforms only (marked `answered_by: operator`). Skip rhythm, language and §4 (the recommendation is always marked). Stage 1 fills rhythm and language from the persona's life.

## 2. Platforms and existing accounts

- **Target platforms** (multi-select): YouTube long, YouTube Shorts, Instagram Reels, TikTok, others. Stages 1c, 7, 8 and 9 build for exactly these.
- **For each platform picked, ask:** "Do you already have an account there?" Options: *No, starting fresh* · *Yes, and I want to keep it* (ask the handle and a rough follower count) · *Yes, but I'd rather start over*. Say what it changes: "If you keep an account that already has followers, we keep its name and update its page instead of inventing a new one."
  - Kept accounts: Stage 1c skips the name search for that platform and only checks the handle works elsewhere; the brand kit and the Brand Genome step update the existing picture, banner and bio rather than creating from scratch.
- **Realistic rhythm:** how often they can publish long and vertical videos. Ask; don't suggest a number they can't keep. In demo, the persona's life sets it (invented in Stage 1).
- **Content language(s)** and whether captions are in a second language.

## 3. Workspace

- **Find the brand first** (order in `SKILL.md`, "Brand folder and where to look"): project `START-HERE.md`, then `Brands/` on the computer.
  - **Which folders count.** For this skill a brand folder is any folder under `Brands/` with a `Brand Genome.md`, a `START-HERE.md` or a `Who I Am.md`; one without a `Brand Genome.md` is a partial brand. If the connected folder is `Brands` itself, its subfolders are the brands; if it's `Content Creation` or a parent, use `Brands/` inside it.
  - **Brand folder exists** (finished or partial genome): ask with AskUserQuestion: *Resume where it stopped* · *Change one thing* (runs `../revisit.md`) · *Start over (replace it)* · *This is a different brand*. If the creator's first message already names a change ("change my colors"), skip this question and go straight to `../revisit.md`. Say what it changes: "Starting over rebuilds every brand decision; your old files are kept in a dated folder, nothing is deleted."
    - **Start over (a redo):** ask before moving anything, then archive, never delete:
      - Earlier-run files (`Brand Genome.md`, the stage docs in `00 Decisions/`, `Brand Genome (visual).html`, the link shortcut, `README.md`) move to `_archive/<YYYY-MM-DD>-superseded/` at the brand folder root, keeping their relative paths.
      - Old page sources move to `01 Brand Kit/page-sources/_previous-run/`.
      - `Who I Am.md` stays where it is: Stage 1 reads it, asks only what's missing or changed, and updates it in place.
      - In `START-HERE.md`, the old `## Brand` text moves under `## Earlier notes`, headed **"HISTORY ONLY: do not act on it. Files it names may be in `_archive/`."**
      - Existing files in `01 Brand Kit/` (sound, exports) stay; new kit files are written beside them and `brand-kit.md` lists the old ones as earlier versions. Leave `03 Videos/`, `04 Ideas/` and `07 Asset Library/` alone (except creating what's missing): they belong to the other skills.
      - **Flag stale docs:** list any project docs or other files that still name the old picks (old palette, old fonts, old kit) and tell the creator in one line each; ask before editing or archiving them.
      - The photo kit is asked again in Stage 4 even if photos exist; their look may have changed.
    - **An older `START-HERE.md`** without the three sections: add `## Brand`, `## Ideas`, `## Videos` at the top and keep the old text below them under `## Earlier notes`, unchanged.
  - **No folder for this brand:** ask whether they want the files on their computer (a folder) or kept in the project only.
- **Create the whole tree** in `Content Creation/Brands/<Brand>/`, every folder in the map, so idea-genome and video-genome find the structure in place: `00 Decisions/` through `07 Asset Library/` (with `footage/ screens/ images/ people/ audio/ scenes/ graphics/ docs/`), `01 Brand Kit/page-sources/ sound/ exports/`. Write `07 Asset Library/asset-index.md` with only the header row, and `START-HERE.md` with the three headings `## Brand`, `## Ideas`, `## Videos` (the last two empty). Create only what's missing; never rename or move what exists.
- **Folder name:** the brand or channel name if they have one (or the kept account's name), else the creator's first name (demo: the persona's first name). If Stage 1 lands on a different name, ask before renaming the folder.
- If the connected folder is `Content Creation` itself or a parent of it, use `Brands/` inside it; if `Brands/` isn't reachable, ask the creator to connect `Content Creation` (or `Brands`).
- Check that `../benchmark/` has its 12 photos and the folders `looks/` (art styles), `backdrops/` (backdrop scenes) and `bfr/` (cutaways). If anything is missing, say so and stop; the look rounds depend on them.

## 4. How they decide

One question: "When I show you options, do you want my recommendation marked, or would you rather pick blind?" Default: marked. Record it in the `## Brand` section of `START-HERE.md` under "How this creator decides."

## 5. Demo mode: the seed, and nothing more

Ask the operator for **one line**: "a dog groomer in Austin who hates how other groomers look on YouTube." Offer 3 seeds if they want one. Optionally a first name. **That's all that exists before Stage 1.** No persona card yet: the interview in Stage 1 builds the person, question by question, the way it would for a real creator. The card is written at the end of Stage 1 as the interview's result.

**Answering as the persona (from Stage 1 on).**
- Claude answers every question and fills every voting page as the persona, inventing each answer in character at the moment the question is asked, consistent with everything answered so far.
- **Picks must have bite.** Left alone, a picker drifts toward safe, generic options. The persona has opinions and uses them, even against the recommended option. Disagreeing with a recommendation is fine and good on camera.
- Votes go into the page's saved data with `answered_by: persona`; the page shows nothing on the cards; the header says "Answered as <name> (demo)". Notes behave like a person's (rules in `../voting-pages.md`, "Demo mode on a page").
- **One round at a time, the same loop as a real creator, then wait.** For each round: (1) publish the page, (2) fill the persona's votes and notes, (3) read the decisions back, (4) redo a round if a pick needs it, (5) answer the follow-up questions in character, (6) one-line summary, then **wait for "go"**. Never publish more than one page before "go". `fast-forward` skips the waiting when the operator asks for it.
- **The operator can veto** at any time ("back up", or just say what to change). A veto replaces the vote and is marked `answered_by: operator`.
- Live checks still run (handle availability, name clashes), because they make good footage. Nothing gets registered.
- **Approvals.** Each page is one publish approval and one data-write approval. Pre-approve the Artifact and ArtifactData tools for the session, or expect a prompt per page.
- **The ready-for-review question** after each page (`../voting-pages.md`) is answered by the operator's "go"; don't ask it separately in demo.
- **Waits.** Before any live check or research, say in one line what is running and about how long (handle checks ~1 min; research ≤5 min). Nothing else is asked while it runs.
- A resumed chat answers from the persona card (once it exists), never from memory.

**Run controls.** The operator steers the run with plain words. Show this list once, right after the seed is given, and again whenever they ask "controls":

| Say | What happens |
|---|---|
| **pause** | Finish the current step, then stop and wait (for a real creator, "pause" saves to `START-HERE.md`; see `../voting-pages.md`, "Pause and come back"). |
| **go** | Start the next round (after each round's summary), or resume after a pause. |
| **back up** | Reopen the last round so picks can change; then update every later stage that used it (stage docs, `look.md`, Brand Genome) and say in one line what changed. |
| **redo [round]** | Run the same round again with new options; the old page stays readable. |
| **fast-forward** / **fast-forward to [stage]** / **fast-forward N** | Run rounds back to back without waiting for "go", and skip the per-round summaries too; give one summary at the end (all remaining, up to that stage, or N rounds). |
| **why?** | The persona's reason for the last pick, in one line, in their voice. |
| **Marker: …** | No action. It marks a moment for the edit; log it with the time in the `## Brand` section of `START-HERE.md`. |

Default: recap line, then wait for "go". The only things that stop the run on their own are a question the persona can't answer in character (rare) and, from Stage 7 on, a paid generation waiting for approval. These controls work for any operator (a teacher, a tester), not only a recorded demo.

## 6. Auto mode: a short interview, then Claude decides

For a creator who wants a finished brand fast and trusts Claude's calls. Offered in §1 as a third option (*Auto: ask me a few things, then you decide*). Like demo mode, Claude answers every page; unlike demo mode, the answers come from the real creator's direction, not an invented persona.

- **The short interview** (one or two AskUserQuestion calls, each answer one line or a pick): who's on screen · what the channel is about and why it exists · who it's for · the content personality (rank the top 2) · how far they'll go · the name or handle (if they have one) · 2–3 channels or creators they like, and one look they can't stand · platforms (§2). Optional free text: "Anything else I should know?" Write the answers into `Who I Am.md` (marked "short interview") and `START-HERE.md` (`## Brand`: mode auto).
- **The model nudge** (auto and demo, right after the mode is picked), unless you're already on their strongest model: "For best results, run this on your strongest model (today: Fable), if you have it. In this mode I make every brand decision for you, so the quality of each call matters most. It costs more credits; I'll tell you when it's done so you can switch back." A nudge, not a question: you can't switch the model; the creator does it in the model picker. Say it once and carry on either way.
- **Stage 1 in auto:** the short interview replaces 1a and 1b; Claude proposes the name check (1c) and writing voice (1d) as the creator's proxy and confirms each with one click.
- **Then run every stage as usual**, building and publishing every page, and fill each one as the creator's proxy: votes saved with `answered_by: claude (auto)`, picks reasoned from the short interview, the research and the stage's recommendation, with one short note per pick saying why ("Bright and calm, matches 'friendly, then useful'"). Skippable steps are filled with their defaults unless the interview points clearly at keeping something. Paid generation still stops for approval (Principle 13); live checks (handles, specs) still run.
- **No waiting between pages.** Auto runs like fast-forward: no "go" between rounds, no ready-for-review question, no per-round summaries; each reviewed page is still locked. It stops only for a paid generation, a question the short interview can't answer (ask it, in one line, then continue), or a pick that would break a house rule.
- **At the end, one review:** the Brand Genome page with every pick and its one-line why, each section linked to its page (votes visible). Then: "Anything you'd change? Name it in plain words." Each change runs through `../revisit.md` in change mode, as with any finished brand.
- The creator can stop auto at any time ("let me pick from here"); the run continues in the normal real-creator loop from that step.

## Output

The brand folder with the whole tree, an empty `asset-index.md`, and `START-HERE.md` (three headings; the `## Brand` section filled with the brand folder path, mode, platforms, existing accounts, rhythm, language, folder choice, how they decide; in demo, the seed and the run-controls note; rhythm and language are filled by Stage 1).
