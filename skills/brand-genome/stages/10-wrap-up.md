# Stage 10: Wrap-up

This skill ends here. It does not record, edit or render.

## 1. Write the brand folder's `README.md` (for outside tools, not the creator)

`Brands/<Brand>/README.md` is for agents, skills and services that will work on this brand. Written for machines: short, exact, no story. Sections, in this order:

1. **One line:** whose brand this is (creator name, handles, platforms), built with brand-genome on <date>, status.
2. **Read order:** `Who I Am.md` → `Brand Genome.md` → `00 Decisions/run-sheet.md` → `00 Decisions/` (the stage doc behind each Genome section) → `02 Research/channel-playbook.md`.
3. **The visual Genome:** the online page link (same link always), the shortcut file, and `Brand Genome (visual).html` (offline; Copy works only online; changes are always asked for in chat). "Whenever the Genome changes, republish the online page and overwrite the offline copy."
4. **Folder map:** a table, `Path | What it holds | Who writes it`, one row per item in the brand folder map (`SKILL.md`), including `README.md`, `START-HERE.md` (`## Brand` brand-genome; `## Ideas` idea-genome; `## Videos` video-genome), `07 Asset Library/people/` (likeness photos; its own `README.md` and `PHOTOS-OWED.md`) and `_archive/` (superseded files: **do not use**).
5. **Rules for any skill or service:**
   - The Brand Genome wins over any default (colors, fonts, motion, sound). Never change the brand yourself; changes go only through brand-genome (`revisit.md`), started by the creator.
   - Every claim traces to Proof in `Who I Am.md`. Never invent figures, clients, results or quotes.
   - Likeness follows `00 Decisions/image-rules.md`. The raw photos in `07 Asset Library/people/` are likeness references only: never upload them anywhere except into a generation the creator approved. No known characters, logos or brand marks.
   - AI labels only where the platform requires them (see image-rules).
   - Paid generations: say what, which tool and the cost, then run only after the creator says OK.
   - Never print or copy API keys or secrets into this folder or any repo.
   - Where new files go: media into `07 Asset Library/<type>/` plus a row in `asset-index.md`; video work into `03 Videos/`; ideas into `04 Ideas/`.
   - Any house rule that binds every output (from `00 Decisions/house-rules.md`), one line each.
6. **Pipeline:** idea-genome (an idea → an Idea Record in `04 Ideas/`) → video-genome (Idea Record + Brand Genome → a video in `03 Videos/`). Pending items and open decisions: `START-HERE.md` → `## Brand`.

Add "Folder guide: `README.md`" to the `## Brand` section of `START-HERE.md`. Every later Genome change that moves a file or a link updates the README in the same turn.

## 2. Finish the files

The `## Brand` section of `START-HERE.md` (only that section) gets the read order, the current state, next steps, how this creator decides, and **Pending**: photos still owed (from `07 Asset Library/people/PHOTOS-OWED.md`), kit files still to render, anything marked "confirm at account setup". Copy every page's source to `01 Brand Kit/page-sources/`, because cloud workspaces are temporary. Update the project copies of `START-HERE.md` and `Brand Genome.md`.

## 3. Say what's next, in plain words

- "Your Brand Genome is ready." Then the highlights line: "The page is highlights only. The full brand, including every library, research default and rule, is in Brand Genome.md in your brand folder. Every video skill reads that file."
- If photos are still owed, one line: "Still to send when you like: 5 photos (the list is in your brand folder). Nothing waits on them."
- "Next, bring a video idea, or ask for a brainstorm, to idea-genome; it writes the Idea Record that video-genome builds from." This skill never proposes episodes or topics; if they ask for ideas, idea-genome is the place.

## 4. Find the next skills

Look in this session's skill list for **idea-genome** and **video-genome** (the companion skills from the same bundle).
- **Both found:** name both: idea-genome turns an idea, a theme or nothing into an Idea Record; video-genome reads that record and `Brand Genome.md` (look, motion, sound, kit placements, vertical rules, voice, run sheet) and makes the video. Offer to start idea-genome.
- **Model line** (auto or demo runs, when you're on their strongest model): "Going straight into an idea? Stay on Fable: idea-genome works best there and it's a short step. Otherwise, switch back to your everyday model (today: Opus)."
- **One missing:** name the one that's installed and the one that's missing, from the same bundle.
- **Neither:** say so plainly: "The brand is done. Ideas and videos need idea-genome and video-genome, and neither is installed." Stop. Do not build the video here.

## 5. What a video skill may and may not do

It reads the Brand Genome. It doesn't overrule it: where its own defaults differ (motion, colors, sound), the Brand Genome wins. If a draft shows a brand piece doesn't work, it sends the creator back here to `revisit.md` instead of changing the brand on its own.
