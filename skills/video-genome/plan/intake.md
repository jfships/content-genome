# Intake: what the creator brought (Step 0, part 2)

The creator can arrive with anything. Map it onto the plan before asking a single plan question, so nothing they already decided is asked again and nothing missing is skipped.

## First: the episode folder

Before mapping anything, find or create the episode folder (`03 Videos/EP NN <slug>/`, next free number; `SKILL.md` folder rules) so `plan.md` and the pages have somewhere to live. A resumed episode already has one.

## Then: say what the video is about, and get a yes

Before mapping a single row, write one plain line and confirm it with one question:
"This video is about **___**, for **___**, as **___** (the format or series). **___** is the example we show it on, and **___** is what comes out at the end."
- Keep the three apart: the **topic** (what the viewer learns or gets), the **demo subject** (the real thing it's shown on) and the **output** (what gets made on camera). Plans drift when the demo or the output quietly becomes the topic.
- **Name the format from the brand file** (§4 Formats), not from the Idea Record alone. If the record names a different format or series than the brand would, ask; the brand file's list is the menu. Once confirmed, write that format's must-haves into `plan.md` (series tag, recurring pieces, set beats, its call to action) so no later step drops them.
- Read it against the Idea Record. If they disagree, the creator's answer wins and the record is rewritten (below) before anything else.
- **Mid-plan, recheck it.** When a creator note contradicts this line ("you're focusing too much on X", "this isn't an X video"), stop. Restate the line, ask again, and recheck every decision made under the old one. Don't patch rows one by one.
- **When the output changes, change it everywhere in the same turn.** Search `plan.md`, `idea.md` and every page source for the old output's name and rewrite each row that uses it. From then on, name the output in full in every question ("the YouTube video + its Short"), never a short name that could still mean the old one.

## Accept any format

Idea Record · brief · full script · outline or bullets · notes or a voice-memo transcript · a previous plan or handoff · a link (article, video, thread) · existing footage · a half-done `plan.md` · nothing at all.
- Read every file and link yourself. For footage, run `inspect_video.py` and `transcribe.py` first (`paths/footage-first.md` B2) and treat the transcript as the script.
- Nothing at all, or just a topic → offer idea-genome (Recommended). If they'd rather go straight on, draft all the Idea Record fields yourself from what they said (promise, who it's for, angle, format, proof we have / still need, feeling), and confirm them in chat: one AskUserQuestion per field that needs the creator's call (promise, audience, angle, format), each with your draft as the Recommended option and 2–3 real alternatives; the rest in one summary question. Titles are decided in the plan.
- **An Idea Record written here** (from scratch or rewritten because the premise changed) still uses idea-genome's template and fields (`IDEA NNN <slug>.md`, next free ID in `04 Ideas/`, a row in `idea-bank.md`), with `written in: video-genome` and the date. A rewrite gets a new ID and marks the old one `superseded by IDEA NNN`; never edit the old one in place.

## Map it onto the run sheet

Walk `plan/run-sheet.md` item by item. Each item becomes one of:
- **Taken from <source>** ("taken from plan", "taken from your brief", "taken from your script"): the source decides it clearly.
- **Open:** the source doesn't say, or says it two ways.

Save the map at the top of `plan.md`:

| Run-sheet item | Status | What it says | Source |
|---|---|---|---|
| Story arc | taken from your brief | problem → turn → payoff | brief p.1 |
| Opening line | taken from your script | "Day 1, I almost quit." | script line 1 |
| Music | open | | |

## Confirm in one pass

Confirm every taken item in chat: list them in one message (item, what it says, source), then one AskUserQuestion (multi-select): "Which of these do you want to change?" with each item as an option. Nothing picked = all confirmed.
- Confirmed items are inputs from then on; the plan doesn't reopen them unless the creator does.
- Each taken story item names what it locks in, so changing it isn't free: "Your brief follows a problem → turn → payoff arc. Other arcs exist; switching would mean rewriting the middle of your script." Name the parts of their material a change would touch (script section, brief paragraph, shot already filmed).
- **Change it** → that item becomes open and is decided in the plan like any open item (chat or page, per `decision-pages.md`), with their original as the first option, marked "(from your brief)".

## A previous plan or handoff, or a resumed episode

A plan from an earlier session or chat fills steps the same way: its items are **taken from plan** and confirmed the same way. It never replaces the flow.
- **Step 0 runs, briefly.** Brand file found and read, tools checked: one line ("Start · brand and tools ready"), no questions unless something is missing.
- **Build state goes in the same confirmation.** Add a row for each part already built or filmed, with its evidence: "Act one: built, draft 10, locked · from your handoff". Confirmed rows are not rebuilt.
- **Jump to the first step whose gate has no evidence** (a locked page, a decision recorded in `plan.md`, a `_review/review-log.md` entry, a `debt.md` row, an approved file). Say which step that is and why, in one line. Run only the gates that are missing; never re-ask what passed.
- A `START-HERE.md` `## Videos` resume (same project, same episode) skips the confirmation: say in one line where it stopped and re-send the open page or question, or start the next step.
