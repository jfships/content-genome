# Arcs: operators and line rules

Family: tools that wrap or run through any shape or arc. Operators reorder or withhold (in-medias-res, full-circle, mystery-box, reversal); line rules govern how beats join (but-therefore, ABT).
Shared skeleton: operator = `[shown out of order or held back] + [inner arc] + [return or reveal]`; line rule = every beat after the first opens with `but` or `therefore/so/which means`.
Evidence: no operator tested at 30–60 s; mystery-box and reversal rest on curiosity and suspense research (other media); in-medias-res and full-circle are craft; both line rules are single-lineage craft (two TV writers via secondhand report; one scientist-filmmaker's ABT) with no outcome data.
Runtimes: line rules fit any runtime; full-circle any; in-medias-res ≥ 30 s (the rewind costs ~2–4 s); mystery-box 30–60 s; reversal 20–45 s.

Stacking: one skeleton (shape or arc) + at most one operator + the but-therefore lint always. Valid: `in-medias-res over man-in-hole`, `full-circle over abt-story`, `mystery-box over before-after`. Not valid: two operators; mystery-box with a result-first hook that gives the cause; in-medias-res with a result-first hook (same move twice).

Card fields as in `arcs-setback.md`. Words per beat ≈ seconds × 2.4. All examples are made up.

## Operators

### in-medias-res · In the middle of it
Type: ORDER (operator)
Does: opens on the peak moment with no context, marks a rewind, catches up through an inner arc, replays the opening moment now understood, finishes.
Use when: story, demo, news; the opening frame is arresting on its own. ≥ 30 s.
Beats: B1 FROZEN PEAK 10% (0–3 | 0–6) hook · B2 REWIND MARKER 5% (3–4.5 | 6–9) one line · B3 CATCH-UP 50% (4.5–19.5 | 9–39) runs the inner arc · B4 REJOIN 10% (19.5–22.5 | 39–45) · B5 FINISH 25% (22.5–30 | 45–60). @30: B2 is the first line of B3; B4 the first line of B5.
V: [-2, 0, 0→-1, -2, +2] `▁▄▄▁█`
Lines: B1 mid-sentence or mid-action, no context · B2 a time marker ("ten minutes earlier") · B4 repeats the exact B1 words (callback) · B5 resolution. `[<peak line>] [ten minutes earlier] [<inner arc>] [<same peak line, now clear>] [so <outcome>]`
  e.g. "…and that's when the whole pot boiled over onto the stove." / "Ten minutes earlier, I'd turned the heat up to save time."
Edit: B1 is the best frame of the edit: FREEZE or SMASH + RISE · B2 RAMP (rewind) · B3 the inner arc's codes · B4 MATCH to the B1 frame, same words, HIT · B5 CUT-S.
Pairs: hooks mid-action, stakes, visual-prop, interrupt; inner arcs man-in-hole, fail-fail-win, escalating-problem; endings callback, loop, send-line. Clashes: result-first (same move; don't use both); question hooks.
Fails when: the opening frame needs context to be interesting; B4 doesn't change what the viewer thinks of B1; a long catch-up at 30 s.
Evidence: CRAFT/MANY [4]; curiosity mechanism (other media); the urge to resume is real, "remembered" is not. Flag: weak

### full-circle · Full circle
Type: ORDER (operator)
Does: the last line echoes the first with a new meaning, ideally feeding straight back into it.
Use when: opinion, story, tip; any runtime.
Beats: B1 OPENING LINE 12% (0–3.5 | 0–7) hook · B2 DEPARTURE 18% (3.5–9 | 7–18) · B3 CHANGE 45% (9–22.5 | 18–45) · B4 RETURN 25% (22.5–30 | 45–60). Over another arc: only B1 and the last line are fixed; the inner arc fills the middle.
V: [0, -1, +1, +2] `▄▂▆█`
Lines: first and last sentences share words; the last carries the new meaning and can grammatically feed the first. `[<line X>] [but <departure>] [so <change>, because <insight>] [<line X, re-meant>]`
  e.g. "I just need a program that works." / "I just need a program I'll still be doing in March."
Edit: B4 MATCH to the B1 frame (same set and framing, changed state); music continuous across the loop join; no sign-off at the join.
Pairs: hooks callout, question, pov-setup, bold-claim; wrapper loop-back (`shapes.md`); endings loop, callback. Clashes: tease-next (they open the end the loop closes).
Fails when: the echo changes nothing; the loop join is felt as an error.
Evidence: INFERENCE [2]; replays as a factor is a vendor claim; Instagram names watch-through. Flag: weak

### mystery-box (pointer)
Full card: `arcs-curiosity.md`. As an operator it wraps a result arc: show the output, hide the cause, reveal it in the last third. Clash: any hook that gives the cause.

### reversal (pointer)
Full card: `arcs-curiosity.md`. As an operator it flips the last third of any arc: build the expected reading with two signals, `except`, then re-anchor in one plain line. One twist per Reel.

## Line rules

### but-therefore · But / therefore chain
Type: LINE-RULE (runs over any shape or arc; the lint runs on every script)
Does: every beat joins the last by cause (`therefore`, `so`, `which means`) or obstacle (`but`), never by sequence.
Use when: always as a lint; as a standalone skeleton for story, demo, news.
Beats (standalone): L1 SETUP 15% (0–4.5 | 0–9) hook · L2 BUT 20% (4.5–10.5 | 9–21) · L3 THEREFORE 20% (10.5–16.5 | 21–33) · L4 BIGGER BUT 23% (16.5–23.5 | 33–47) · L5 THEREFORE-RESOLUTION 22% (23.5–30 | 47–60). @30: 4 links (drop L4 or merge L1/L2). Each link 15–25 words at 60 s.
V: [+1, -1, +1, -2, +2] `▆▂▆▁█` (every `but` dips, every `therefore` recovers)
Lines: `[<state>] [but <complication>] [therefore <action>] [but <bigger complication>] [therefore <resolution>]`
  e.g. "I wanted crisp roast potatoes, but they kept coming out soft." / "So I boiled them first and roughed them up, which meant the edges finally had something to crisp."
Lint:
- No `and then`, `next`, `also`, `after that` at the start of a beat. Inside a beat they are fine.
- Every `but` gets a visible change on screen (cut, PUNCH, color or sound dip).
- Every `therefore` shows the action on screen (CUTAWAY or SCREEN of the thing being done) while it is said.
- At least two real `but` turns in a 30–45 s script, one near the middle (40–60%).
- Not every link a `but` (whiplash, no progress); no filler `therefore` without a real cause.
Edit: visible change @but; action on screen @therefore; INT on the second `but`; optional POP on the connective word itself ("BUT").
Pairs: any hook (best: question, curiosity-gap, stakes); any ending. Clashes: none.
Fails when: used alone as the arc with no destination; all buts; therefores with no cause.
Evidence: SINGLE-lineage craft [2] (two TV writers, secondhand report; ABT author); many retellings, no data. Flag: weak

### abt · And, but, therefore
Type: LINE-RULE/CONTAINER · Shape twin: abt-story (`shapes.md`)
Does: the smallest working arc: shared world (and), problem (but), what to do (therefore), in one to three sentences.
Use when: opinion, tip, news. 15–30 s; also as the one-sentence test of any idea (if it can't be said as ABT, the idea isn't clear yet).
Beats: B1 AND 30% (0–9 | 0–18) up to two "and" facts; hook in the first 3 s · B2 BUT 30% (9–18 | 18–36) · B3 THEREFORE 40% (18–30 | 36–60).
V: [+1, -1, +2] `▆▂█`
Lines: "<fact>, and <fact>, but <problem>, therefore <resolution>." `[AND <what everyone knows>, and <what I assumed>] [BUT <what's wrong or missing>] [THEREFORE <what to do>]`
  e.g. "Everyone shoots products on a white background, and I did too, but every shop looked the same, so now I shoot mine on the counter where I make them."
Edit: AND beat CUT-M · BUT = the INT (visual or text flip, WARN) · THEREFORE = CUTAWAY of the action + CARD-N if there is a result.
Pairs: hooks callout, contrarian, question; endings send-line, button. Clashes: stakes (no room to build them).
Fails when: the but is not a real obstacle; the therefore is advice with no proof.
Evidence: SINGLE [2] (taught in science communication; no data; an often-repeated retention figure has no source). Flag: weak
