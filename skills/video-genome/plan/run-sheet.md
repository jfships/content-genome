# Step 1: Plan (gate: the creator approves)

Fill the brand's run-sheet checklist in `plan.md`. If the brand's run sheet is missing an item below, add it.

- **Start from the intake map** (`plan/intake.md`). Confirmed items are inputs; don't reopen them unless the creator does.
- **Each open item is one decision:** a decision page when it has to be seen or heard (`decision-pages.md`), otherwise one AskUserQuestion. Never two at once. Lead with a Recommended option and one line of why.
- **Record Main, Backup and Alternatives** under the item in `plan.md`. The backup is what the edit falls back to.
- **Tracker line** on every message ("Plan · decision 4 of 13 · about 30% done"); the count is the open items only.
- **Internal names stay internal.** Story-library slugs, beat numbers and move names are for `plan.md`; the creator sees plain names, the time and the line.

**How each item is decided** (taken items are only confirmed; this is for open ones). Word decisions are asked in chat; pages are only for what has to be seen or heard (`decision-pages.md`):

| Item | How |
|---|---|
| Order of work, length | One question |
| Title | One question (the words, each with the thumbnail idea it promises in one line) |
| Thumbnail system | Page of the brand's thumbnail layouts, one shown per kept title (`titles.json` shape); the still itself is picked after the build |
| Angle | Taken from the Idea Record; one question only if it's missing |
| Kind of video, script shape, story arc | One question each: plain name, a one-line example in their topic, what changing it would touch |
| Rest of the story plan (proof, keeping people watching, pace, editing moves, ending and ask, feeling, platform tricks) | Claude picks within each layer's count; one question per layer the creator should weigh in on (feeling, ending and ask, proof); the rest summarized in one line and confirmed with one question |
| Opening line | One question, 3–4 options written word for word, Main then Backup |
| Script / beat outline | The script or cues as a file beside the draft video; one question: approved, or what to change |
| Look | A plain-words summary in chat; single moments only get a page when two options are both good (`moment-look.json`) |
| Motion and graphics for a moment | Page of rendered clips (Keep / Skip or Main / Backup) |
| Cutaway gags | Page with a still per gag (`break-from-reality.json`) |
| Music | Page with a player per part of the video (`music.json`) |
| Shorts moments | One question (multi-select), each with its time and line |

0. **The Idea Record.** Copy the approved `04 Ideas/IDEA NNN <slug>.md` to `EP NN <slug>/idea.md` and set the bank row to `made`. Its promise, audience, angle, format, proof, titles and feeling target are inputs, not open questions; change one only if the creator asks, and note it.
1. **Format and pillar.** The format confirmed in intake (from the brand file's formats, not only the Idea Record) with its must-haves listed in `plan.md` (series tag, recurring pieces, set beats), the pillar, and the order (graphics first or footage first).
2. **Packaging first.** Start from the Idea Record's 3 titles; refine, don't restart. Titles are asked in chat (each with the thumbnail it promises in one line); the thumbnail system is then picked on a page at feed size. Pick the thumbnail system from the brand's kept systems (the actual still is picked after the build, `craft/thumbnails.md`). Titles promise one clear thing; the thumbnail shows it.
3. **Research and our angle.** The Idea Record's sources and angle, plus anything new: what's already out there, and what's the creator's own that isn't (their opinion, proof, story beat). Required.
4. **Story stack.** Picks per layer from `plan/story-libraries.md`, within each layer's count (video type, script framework, story arc, hooks, proof, retention devices, pacing, editing techniques, CTA, feeling, platform mechanics), each by slug in `plan.md` with one line of why. Kind of video, script shape and story arc are each one question in chat: plain names, a two-line example per option in the creator's topic, the creator's own version first and marked "(from your brief)" when their material already follows one, and what changing it would touch. The other layers are picked to fit and confirmed in chat. Run its compatibility check and read the last 3 stacks in `03 Videos/results-log.md`.
5. **Hooks.** Write 3–6 from the hook types the stack allows. Asked in chat, written word for word: Main, then Backup (more than 4 → a first question to shortlist). Both get recorded and the edit picks. Each fires on three layers (line, on-screen text, first image). Prove the title within 10 s. Never open with a greeting, backstory, an agenda or a logo.
6. **Script and beats.** The format's beats are the skeleton; the script framework sets the order inside them and the arc sets where the feeling turns. Order A: write the full script; it times the draft, and the creator records from bullet cues by default or from the script on a prompter if they prefer (ask once, save the answer in the brand file's §10 Voice). Order B: bullet cues, with the hooks written word for word. Re-hook every 2–3 min with the stack's retention devices. Put the best moment about two-thirds of the way in.
7. **Look.**
   - The pack (from the brand) and why.
   - The motion language: the pack's motion table, plus any change for this video, in one line.
   - The energy arc: establish → develop → climax → resolve. The climax is the one "wow" moment, about two-thirds in.
   - Music lanes per section, each with a stated BPM, and where the big hits land on the beat.
   - The default background, plus accent backgrounds with their triggers.
   - Grade and accent grades.
   - 2–4 signature moments from the brand's kept list.
   - At most 1 wildcard, on the hook or a turning point.
   - Moves per beat, only from the options the brand's packs kept, never from its No lists; build notes in `craft/graphics-library.md`. Where nothing kept fits, propose your own inside the brand's limits (`craft/brand-fit.md`).
   - **Spatial moves for screens and explainers.** Every beat that shows a screen, a tool or an idea gets a spatial move (`craft/spatial/README.md`) unless a plainer move is clearly better. Use the moves the brand kept; if the brand has no spatial library yet, or the episode needs moves it doesn't have, render a test pack of 6–12 short clips in the brand with real screens and put it on one page (Keep / Skip) before building. A flat screenshot sliding in is not a screen demo.
   - Placement per beat from `craft/layout.md` (speaker position, open side, layout type), re-decided at every scene change.
   - The look is summarized to the creator in plain words, not asked beat by beat. A single moment gets its own page (`moment-look.json`) only when there are two genuinely good options or the creator asks; everything else is judged in the draft review.
8. **Break-from-reality check. Always ask; never skip.**
   - Propose 2–3 spots, using the brand's break-from-reality templates tied to the beats, on one page (`break-from-reality.json`), each with where it lands (time + line).
   - If the creator wants all of them drafted and cut later, draft them cheaply (stills, animatics, code-built cutouts) and mark each "CUT CANDIDATE". Only kept ones get the full treatment.
   - Final videos keep 1–2.
9. **Story visuals.** One brief per generated image, following the brand's image rules (likeness included).
10. **Vertical list.** 2–4 moments that stand alone, each with a hook in the first 3 s (`craft/vertical.md`), asked in chat (multi-select, each with its time and line).
11. **Call to action and disclosure.** The stack's CTA, worded in the brand's voice (the brand's CTA for this format wins if it names one); any synthetic person, voice or event gets its label.
12. **Personality check.** Read each beat against the content personality. For every beat, name what makes it deliver the lead pick: a joke, a twist, a surprise, a real artifact, or a payoff of an earlier setup. "It explains X" is not an answer. When a beat is genuinely hard to make entertaining without forcing a joke, use the brand's entertainment fallback (brand file §2; most often spatial motion, `craft/spatial/README.md`) instead of a forced gag. Beats with no answer get rewritten or cut before building.
13. **Truth check.** Every claim about the creator traces to Proof. Every number is real or labeled illustrative.

## Endings are where drafts die

- No reflective slow-down near the end unless it pays off something set up earlier.
- The last 30–45 s needs a callback (a running gag, an earlier image, a line from the hook) and one concrete reason to watch the next video, shown, not said.
- Energy at the end stays at or above the middle. "Resolve" in the arc means one held beat, not a minute of mood.
- Cut the end card to its essentials; nobody watches a slow outro.

## Common first-draft failures to plan against

- A long backstory before anything happens.
- Scenes that only list things (boxes of tools, dashboards of labels).
- Slideshow-like title cards.
- The same screenshot pattern repeated.
- A slow, generic wind-down at the end.

Run **gate 1** in `review/checks.md` before asking for approval. Once approved, write the asset debt (`plan/asset-debt.md`) before any build.
