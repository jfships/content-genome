# Retention devices (mid-video)

What keeps a viewer past the hook and through the middle of a 20–60 s Reel. Load this file when building the beat outline (job A) or when a creator's retention chart shows a dip (diagnosis table, §4).

Read before using any number here:
- No source has measured re-hook intervals, device placement or retention effects inside 20–60 s Reels. Almost every timing below comes from long-form YouTube or vendor posts and is scaled down. Scaled numbers are marked `(scaled)`; treat them as starting points to check against the creator's own retention chart.
- Instagram officially measures skip rate (left in the first 3 s), the retention chart (always slopes down; flatter is better) and watch time. It has published no benchmark and nothing on mid-video structure.
- Placement format: `pct (s@20 | s@30 | s@60)`.
- Slugs reuse video-genome retention slugs (`plan/story-libraries.md` §6, if video-genome is installed; otherwise the cards here and "Other video-genome retention slugs" below cover them) where the mechanism matches. New slugs are lowercase-hyphen. Aliases point old names to the card.

## 1. Device cards (S1–S13)

### result-then-process · Result first, then the process
Does: shows the finished result up front, so the open question changes from "what" to "how, and what did it cost". The viewer knows something the screen has not explained yet (suspense, not surprise).
Use when: demo, tip, before/after, "I tried X". Strongest when the process has a snag worth watching.
Place: result on screen 0–10% (0–2 | 0–3 | 0–3); "here's how" by 10–15% (2–3 | 3–4.5 | 6–9) (scaled). Then the process with one snag (escalating-problem, but-therefore).
Lines: `[show result]. This took [time], and the first try [broke how]. Here's what fixed it.`
  e.g. "This loaf took one change. The first one came out flat, and that's the whole lesson." / "Finished shelf, no drill. The first try fell off the wall."
Edit: frame 1 = the result (CARD-N if it's a number); CUT-M into the process; SMASH or WIPE back to the "before" if one exists.
Pairs: escalating-problem, but-therefore, payoff-ladder. Clashes: mystery-box (the result already opened the box).
Fails when: the result is the whole value (nothing left to wait for); the process is a flat click list; the result is not impressive on sight.
Evidence: RESEARCH [3] (spoiler study, Hitchcock/Lessing suspense; other medium) + MANY [3] practitioners.

### but-therefore · But / therefore chain
Full card (line rule over any arc): `arcs-operators.md#but-therefore`. This card covers its retention use.
Does: each beat either causes the next ("so", "which means") or blocks it ("but"). Removes "and then" joints where a viewer can leave.
Use when: any story-shaped Reel: a build, a fix, a test. Also the line rule over any arc (see arc catalog).
Place: at every beat boundary. At least two real "but" turns in 30–45 s; one near 40–60% (8–12 | 12–18 | 24–36) (scaled).
Lines: `[Goal]. So I [action]. But [snag]. So [fix]. But [new snag]. Which means [result].`
  e.g. "I doubled the recipe, so I doubled the salt. But salt doesn't scale like flour, so it was inedible." / "The paint covered in one coat. But it dried patchy, so I sanded and tried a roller."
Edit: a visible change at every "but": SMASH, CUT-M or a new shot @but. Without it the turn is only heard.
Pairs: escalating-problem, result-then-process. Clashes: list shapes of truly independent tips (fake causality).
Fails when: the content is a list of independent tips; the "but" is invented; every line is a "but" (no "so" to release it).
Evidence: MANY [5] craft tradition (South Park writers, Story Spine "because of that"); zero retention measurement.

### escalating-problem · Escalating problem
Full card (as an arc): `arcs-ladder.md#escalating-problem`. This card covers its retention use.
Aliases: rick-and-morty
Does: solving the first problem creates a bigger one, so the viewer's question grows instead of closing.
Use when: troubleshooting, "I tried the shortcut", honest product reviews, home repair, recipes gone wrong.
Place: first complication 25–40% (5–8 | 7.5–12 | 15–24); bigger one 55–75% (11–15 | 16.5–22.5 | 33–45) (scaled). One cascade at ≤30 s; two at 45–60 s.
Lines: `[Fix A solved P1]. But it caused [P2], which is worse. Fixing that took [step]. Now it works, but only because [price].`
  e.g. "The new filter stopped the leak. But now the tap barely runs, which is worse." / "Cheaper flour, same bread. But the crust went pale, and that's harder to fix."
Edit: INT on the second, bigger complication (the turn); CARD-L or WARN on the new problem; PUSH through the worse moment.
Pairs: but-therefore, payoff-ladder, result-then-process. Clashes: hard-stop before the price is paid (cuts the cascade short).
Fails when: the escalation is staged or untrue; the thing simply worked; the new problem is unrelated to the fix.
Evidence: MANY [4] for the pattern under other names (Story Spine, Save the Cat false victory, Story Circle "price", MrBeast escalation). Attribution note: the "Rick and Morty method" name is a creator label; no source shows Harmon or that writers' room teaching this rule. Use "escalating problem" in output; keep the old name only as an alias.

### tease-rehook · Re-hook before the dip
Does: before interest in the current point runs out, close it in one clause and tease the next, resetting the question.
Use when: 30–60 s scripts with 3+ beats; right before where the creator's chart usually dips.
Place: one near the midpoint; at 45–60 s a second shortly before the last third. At 30 s ≈ 13–18 s; at 60 s ≈ 25–30 and 36–40 (scaled). Rhythm rule in §2.
Lines: `[Close current point in one clause], [name the next thing and why it matters].`
  e.g. "That part's easy. The part that cost me a whole batch is next." / "Same grout, though, did this, and I didn't expect it."
Edit: CUT-M or related cut on the tease word; optional PUSH into the next beat; no SFX unless something appears.
Pairs: stacked-loops, payoff-ladder. Clashes: hard-stop placed right after a tease (tease never paid).
Fails when: the tease is vague and the next beat weak (viewers learn to distrust it); bolted on every few seconds; never paid off.
Evidence: MANY [8] for the idea (all long-form or generic). Interval for Reels: VENDOR, unverified. Flag: weak (interval only).

### stacked-loops · Close one question, open the next in the same breath
Aliases: hook-deliver, nested-loops
Does: attention peaks when a question resolves and fades as the viewer adapts. Opening the next question inside the answer sentence covers the weakest second, right after a payoff.
Use when: lists and step sequences at 45–60 s; any payoff beat that is not the last.
Place: at every payoff except the final one. No silence after a resolved point.
Lines: `[Answer to Q1], which raises [Q2].`
  e.g. "So the trick is resting the dough. But how long? That matters more than the recipe." / "That works for one shelf. What about six?"
Edit: no cut between answer and new question (same breath); the cut lands on the first word of the next beat.
Pairs: tease-rehook, progress. Clashes: silence held after a mid payoff (breaks the breath join).
Fails when: every beat dangles and nothing resolves; the viewer has no stake in Q2.
Evidence: INFERENCE from RESEARCH [3] (belief-resolution, goal-gradient dip after reward, curiosity and memory) + one VENDOR. Flag: weak.

### viewer-job · Give the viewer a job (guess, compare, choose)
Aliases: q-rehook
Does: asking the viewer to guess makes the uncertainty personal; people spend effort to learn answers they are curious about.
Use when: comparison, A/B tests, "which is real", price-vs-quality. Good home for the biggest reveal.
Place: question by 10–20% (2–4 | 3–6 | 6–12); reveal after 50–70% (10–14 | 15–21 | 30–42) (scaled). Not before the middle.
Lines: `Which one [won / is real / cost more]: A or B? [beat]. [beat]. B, and here's why.`
  e.g. "Two steaks, one rested ten minutes. Guess which is juicier." / "One of these was a $5 drill. Pick it. Answer at the end."
Edit: SPLIT for A vs B (the edit is the job: both visible); STEP label "A"/"B"; CARD-N or FREEZE on the answer.
Pairs: payoff-ladder, progress. Clashes: result-then-process if the result gives the answer away.
Fails when: the viewer can't judge from what's on screen; the answer is obvious; the reveal comes after most viewers leave.
Evidence: RESEARCH [3] (information-gap theory, curiosity and memory; other medium). No short-form practitioner states it as a tactic.

### progress · Visible progress cue
Aliases: countdown
Does: people speed up near a goal; a counter or numbered steps tell the viewer how close the end is.
Use when: lists, challenges, builds with countable steps.
Place: from the first beat; update at each step. Total ≤3 at 30 s, ≤4–5 at 60 s. Optionally start "1 already done".
Lines: `Three [fixes]. One: … Two: … The last one is the one that matters.`
  e.g. "Three knife mistakes. Two are easy, the third ruins the blade." / "Two coats done, the third is the tricky one."
Edit: STEP label per step ("1/3", "2/3"), same position each time; CUT-M on each step word.
Pairs: stacked-loops (covers the dip after each step), payoff-ladder. Clashes: long totals ("7 steps" in 30 s says "leave").
Fails when: the total is long; the cue is up but nothing changes between steps; the counter competes with Instagram's native progress bar for the same area.
Evidence: RESEARCH [1] (goal-gradient, loyalty cards; other medium) + SINGLE practitioner via vendor.

### interrupt-rehook · Pattern interrupt that carries new information
Does: a cut, zoom, graphic or sound change triggers an orienting response. It helps when it delivers the next fact; as decoration it costs memory, especially on complex content.
Use when: talking-head teaching where the screen can show the proof; at a topic boundary or the turn.
Place: at the turn (valley to climb, expectation flip). One INT per Reel; never two in a row.
Lines: `[New point] + [the new visual or sound shows or names it].`
  e.g. (visual) cut from face to the pan at "look at the edges". / (audio) SIL before the surprising number.
Edit: INT @turn-word, made of one of SMASH / CUTAWAY / SIL / DROP; the change must show or name the new point.
Pairs: escalating-problem (on the bigger complication), but-therefore. Clashes: relentless pacing (no contrast left).
Fails when: the change has no new information; dense topics plus many cuts overload; viewers are trained to expect it.
Evidence: RESEARCH [2] (limited-capacity model: related cuts help, unrelated cost memory) + MANY practice. Interval numbers: VENDOR (ignore).

### info-density · Every line moves it forward
Does: viewers leave when a sentence adds nothing. Each beat must carry something new: a fact, a picture, a turn.
Use when: every script, as an audit pass on the middle.
Place: whole body. Test: for each sentence, "what is new here?" Delete if nothing.
Lines: (audit, no skeleton) cut repeated points, dead air, recaps of what the screen already shows.
Edit: `info_new` field on the card is never empty (lint K9). Pacing = rate of new information, not rate of cuts.
Pairs: all. Clashes: mid-recap (repeats by design).
Fails when: you cut the setup the payoff needs; over-compression turns frantic.
Evidence: MANY [7] (Joos, Hoyos, edX MOOC data on editing out fillers, vendors).

### payoff-ladder · Partial payoff early, biggest last
Aliases: delayed-reveal
Does: the viewer stays to resolve the opening promise; the end shapes the overall judgment (peak-end). Each payoff is bigger than the last.
Use when: any Reel with more than one payoff; reveals, tests, rankings.
Place: real partial payoff by ~50% (10 | 15 | 30); biggest at 80–95% (16–19 | 24–28.5 | 48–57); closing line ≤3 s after it (scaled, INFERENCE).
Lines: `Hook promises X. [Partial win at midpoint]. [Bigger win near the end]. Stop.`
  e.g. "Before the full test, the cheap pan already beat mine on eggs. Now the steak." / "That was the easy fix. This is the one I didn't expect."
Edit: CARD-N on the big payoff (hold ≥1.5 s); keep effects off the partial payoff so the last one reads bigger.
Pairs: viewer-job, escalating-problem, tease-rehook. Clashes: result-then-process when the hook already showed the biggest result.
Fails when: the late reveal is smaller than the hook promised (clickbait); the middle gives nothing to earn the wait.
Evidence: RESEARCH (peak-end, short film clips; other medium) for end weight. Placement is contested: memo/Hoyos say end; vendors say two-thirds or spread. The partial-by-50% compromise is INFERENCE. Flag: weak (placement).

### hard-stop · Stop on the payoff (or loop back)
Does: the Reel ends when the value lands. Lingering gives a place to leave and removes the replay pull.
Use when: every Reel. Endings catalog holds the ending shapes (`catalog/endings.md`: payoff-stop, button, loops).
Place: last 1–3 s. No outro.
Lines: `[Payoff line]. [Optional: a line that returns to the hook's question.]`
  e.g. "…and that's why the cheap pan won." (cut) / "So was it the flour? Look at the first frame again."
Edit: cut on the last useful word; no fade, no end card.
Pairs: callback, verbal-loop, visual-loop. Clashes: a tease or ask placed after the payoff.
Fails when: a business ask is needed (then place it at peak, see endings §3 placement options); the loop-back is a gimmick that confuses.
Evidence: MANY [5] for stop-on-payoff. Loop advantage on Instagram: unverified (no official statement on rewatches).

### early-surprise · Early surprise in the middle
Does: an unexpected element resets attention early in the body.
Use when: personality, vlog-like or story Reels.
Place: unclear at Reel scale; try 20–35% (4–7 | 6–10.5 | 12–21) (scaled, INFERENCE).
Lines: `[Expected next step] → [the thing that wasn't supposed to happen].`
  e.g. "Then the dog ate the second batch." / "Halfway through, the wall turned out to be hollow."
Edit: SMASH or CUTAWAY @surprise; re-anchor line right after (a twist pulls attention off the storyline).
Pairs: escalating-problem. Clashes: interrupt-rehook in the same Reel (two interrupts).
Fails when: the surprise is unrelated to the topic; no re-anchor follows.
Evidence: SINGLE [2] (MrBeast memo report, one blogger). Flag: weak.

### mid-recap · Half-line recap of the premise
Does: restates the premise mid-video for late joiners.
Use when: rarely; only 45–60 s with a complex premise. Test it.
Place: one half-sentence near 50% (– | 15 | 30).
Lines: `[Premise in ≤6 words], and [next point].`
  e.g. "So, same dough, one change: the next part is the oven."
Edit: none; keep it inside the beat.
Pairs: none. Clashes: info-density (it repeats by design).
Fails when: longer than a half-line; repeats what was just shown (viewers can rewind).
Evidence: SINGLE vs SINGLE, contradicted (Hoyos teardown for; Joos against). Flag: weak.

### Other video-genome retention slugs

| Slug | Where it lives here | Mechanics |
|---|---|---|
| callback | `catalog/endings.md` callback | Opening word/object returns at the end with one thing changed. Keep it inside one video. |
| rule-of-three | arc catalog (rule-of-three-with-break) | Two set up a pattern, the third breaks it. Device-sized: one beat or three short ones. Break on the third, never the fourth. |
| silence | code `SIL` | One held pause per Reel, 0.3–1.0 s, after the claim or before the payoff. MANY craft; no controlled evidence. Silence that is just a gap is cut. |

## 2. Re-hook rhythm

Default (INFERENCE, flagged craft): give the viewer a new reason to keep watching about every 8–12 s. For Reels ≥30 s, at least one re-hook lands between 40% and 70% of runtime (card field `rehook: true`; lint K10).

| Runtime | Re-hooks | Where (scaled) |
|---|---|---|
| 20 s | 0–1 | the hook carries most of it; optional one at ~8–12 s |
| 30 s | 1–2 | one at 12–21 s (40–70%) |
| 45 s | 2–3 | ~12 s, one at 18–31 s |
| 60 s | 3–5 | ~10–12 s apart; at least one at 24–42 s |

What counts as a re-hook: a tease of the next point, a new question, a viewer-job question, a visible complication, a step counter moving to the last step, a partial payoff that raises the stakes. A cut alone does not count.

Basis: Joos (ex-MrBeast retention strategist) reports attention drops without novelty every ~10–15 s in long-form; shortened here by inference. The memo's "every ~3 minutes" is long-form and does not scale. Never write "research shows" for this interval.

## 3. Choosing devices by idea type

| Idea type | First pick | Add | Avoid |
|---|---|---|---|
| demo / how-to | result-then-process | progress, tease-rehook | mid-recap |
| tip | info-density + hard-stop | stacked-loops (if 2–3 tips) | escalating-problem (forced) |
| opinion | but-therefore | payoff-ladder | viewer-job with no real answer |
| story | but-therefore + escalating-problem | early-surprise, payoff-ladder | progress |
| comparison | viewer-job | payoff-ladder, SPLIT edit | result-then-process that spoils the answer |
| list | progress | stacked-loops | totals over 3 at 30 s |
| news | result-then-process (the fact first) | tease-rehook | invented complications |

## 4. Diagnosis: where the chart dips → devices to try

Official facts first: the line always slopes down; dips mark moments that lost viewers; a high skip rate means the opening failed. Nothing official maps a dip to a fix. The mapping is practitioner advice plus inference. Read the line and screen at the timestamp before changing anything; compare across several Reels; change one thing at a time; judge against the creator's own Reels, not a fixed target.

| Where | Likely reading | Try | Support |
|---|---|---|---|
| 0–3 s (high skip rate) | opening failed | rewrite hook (hook catalog); result-then-process | OFFICIAL on the metric; fix is practitioner |
| ~3–10 s, big drop after a good start | hook and body don't match, or the promise is delayed | deliver the promised thing fast; say what's coming (result-then-process, but-therefore) | MANY/VENDOR |
| middle dip or slow middle slide | repeated, slow or low-information stretch | info-density (cut), tease-rehook, interrupt-rehook with new info, escalating-problem | VENDOR + Joos |
| dip right after a mini-payoff | attention fades after resolution | stacked-loops (open next in the same breath) | INFERENCE |
| late drift before the last beat | best point too late, or the ending runs long | payoff-ladder (partial payoff earlier), hard-stop | VENDOR |
| a bump (rise) | rewatch, or one striking moment (or confusion) | reuse the beat; check it isn't unclear | secondary; YouTube analog |
| steady gentle slope | normal | do nothing; don't chase a flat line | OFFICIAL |

Mapping a dip to a beat: a drop at a beat boundary usually points to the beat before it. With tiny view counts, pool by beat function (e.g. "the reveal", "the snag") across Reels rather than judging one Reel.

## 5. Counter-evidence (keep in the skill's reasoning)

1. **Open loops are not remembered better.** The Zeigarnik memory claim fails: a 2025 meta-analysis (59 studies) found no overall recall advantage for unfinished tasks. What holds is the urge to resume an interrupted thing (Ovsiankina; resumed ~67% of the time). Write teases as resumption promises ("stay for the part where…"); never say "open loops stick in memory".
2. **Spoilers don't spoil.** Knowing the ending can raise enjoyment. Do not hide things only to hide them.
3. **Over-cutting.** Rapid or unrelated cuts overload viewers on complex content; teaching is complex content. Pacing is the rate of new information, not cuts. Long-form creators publicly slowed down in 2024 (causation not shown).
4. **Fake tension.** An invented "but", a staged complication or a tease that never pays is clickbait. Instagram limits engagement bait and clickbait in recommendations; YouTube enforces against overpromising titles. Every turn must be real (gates: accuracy).
5. **Best-last vs front-loaded is unresolved.** Memo/Hoyos favor a strong end; vendors say most viewers never reach it. Instagram counts watched seconds, which lowers the cost of early exit. Hence the payoff-ladder compromise.
6. **Retention is not the only driver,** and percent-watched flatters short Reels (duration predicts completion). Fixed retention targets are folklore.
7. **Unsupported numbers to never state:** "87% of viral Reels open with a pattern interrupt", "re-hook every X seconds" as fact, any retention or 3-second-hold target, unsourced benchmark ranges.
