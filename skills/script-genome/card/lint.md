# Script card lint

Mechanical checks run on every script card (job A before handing off; job B before the report). Each item: test, how to check, severity, false-positive note.

Severity:
- **FAIL** only for K15 (no invented facts). It maps to the accuracy gate in `check/gates.md`; a FAIL blocks "clear to record".
- **WARN** for everything else. A WARN is a craft observation with a suggested fix, never a block. The creator can keep the line.
- Report WARNs grouped, ≤5 fixes, biggest retention risk first. Never compute a score.

Numbers are defaults from `card/schema.md` §8 "Edit codes" (flagged craft). Scale per-30 s budgets linearly with runtime (×runtime/30).

## Checks

### K1 · Connectives at beat starts (the but-therefore lint)
This is the but-therefore connective lint the selector always runs: beats join with "but" / "so" / "therefore"-type links, not "and then".
Test: no beat opens with "and then", "next", "also", "after that", "plus", "another thing".
How: read the first clause of each beat (B2…Bn, not sub-rows). Flag if it starts with a listed phrase. Suggest "but", "so", "which means", "because", "until".
Severity: WARN.
False positive: list shapes and progress devices where "Two:" / "Step 3" are labels, not joins; "and" inside a beat; ABT's first part. Accept numbered labels.

### K2 · Beat size
Test: every beat ≥5 s and ≥12 spoken words, except the hook row inside B1 (≤8 words, ~3 s). Beat count fits runtime: 15–30 s 3–4 · 31–45 s 4–5 · 46–60 s 5–6 (7 for ladders/lists).
How: sum rows per beat id (B1.1 + B1.2 = B1); compare seconds and words.
Severity: WARN.
False positive: silent demo beats (few words, long seconds) are fine if `info_new` is visual; a 1–2 s button inside the last beat; deadpan endings.

### K3 · Words vs runtime
Test: spoken words ≤ budget +10%; the timed read-aloud decides. Budget = (runtime − planned silent seconds) × the video's pace (`write/budget.md` Pace: this video's take > the creator's pace log for the mode > mode default). Flag a row above ~4.5 w/s after the edit, or a plan that needs >~12% speed-up.
How: count words in `line` cells; compare to the budget in the header (at 2.4 w/s: 20 s ≈ 48 · 30 s ≈ 72 · 45 s ≈ 108 · 60 s ≈ 144; scale for the video's pace). Order: subtract planned silent seconds from the budget first (~2.4 words per silent second), then add the 10–15% pause allowance to the estimated time (words ÷ pace).
Severity: WARN.
False positive: Reels with long silent visual beats (budget is for spoken words); a creator whose measured pace is faster or slower; deliberate fast-talk rows in fast-talk-slow-show.

### K4 · Hook three layers filled
Test: header `hook` has `spoken`, `text` and `image` filled; all three carry the same idea in different words; `image` makes sense with sound off; nothing is asked of the viewer in the first 3 s.
How: check the three fields are non-empty; compare the text layer to the spoken line (not identical); read `image` alone and ask "does a muted stranger get the topic?".
Severity: WARN.
False positive: wordless-gesture or sound-cue openings where one layer is deliberately empty (hook catalog marks these); text layer may echo one key word of the spoken line.

### K5 · Overlay ≠ line
Test: no `overlay` repeats the spoken sentence; in-body overlays (POP) are 1–4 words (hook screen text is 3–7 words, header `text`, checked in K4/K6); no CARD-L duplicates its row's line.
How: compare overlay text to `line`; flag if >4 words or if overlay ⊂ line and covers >50% of it.
Severity: WARN.
False positive: a quoted on-screen element (the label on a jar, a typed instruction in a screen recording) shown because it is the proof, not a caption.

### K6 · No POP/caption or hook-text/caption word overlap at the same moment
Test: when a POP or the hook screen text is on screen, the caption chunk at that moment does not contain the same word(s).
How: for each POP, find its trigger word's time; check the `caption` cell says the chunk is hidden or shows only the remaining words. For the hook screen text (header `text`), compare it with the caption chunks shown while it is up (usually B1); flag any shared word ("it started" in both counts).
Severity: WARN.
False positive: hook text in `mirror` mode with captions hidden for the hook line (no overlap by design); captions off by brand choice (nothing to overlap); a number shown as a numeral in CARD-N while the caption is hidden for that second.

### K7 · Every edit move has a trigger
Test: every code in `edit`, `sound` and `overlay_on` has `@word` (present in that row's line) or `@event`.
How: parse codes; flag any without `@`; flag `@word` whose word is not in the line.
Severity: WARN.
False positive: always-on moves (JUMP tightening) may be listed once in the header instead of per row.

### K8 · Effect budgets
Test: per 30 s: unrelated cuts ≤6–8; PUNCH ≤3–5; SFX only on information events (≤1 per event); stickers ≤1 per 10 s; one INT; one held SIL.
How: count `cut_type: unrelated`, PUNCH codes, SFX codes (each must sit on an @event or a POP), INT and SIL across the card.
Severity: WARN.
False positive: montage/result rows under cut-to-beat; relentless pacing in the first 3–5 s; the brand's own house limits (read from the brand folder) override these.

### K9 · info_new not empty
Test: every row's `info_new` names something new: a fact, a picture, a turn.
How: flag empty cells and cells that restate the previous row ("more about X").
Severity: WARN.
False positive: a deliberate one-beat silence or reaction row whose new information is the reaction; the button that compresses (new form, same idea).

### K10 · Re-hook present at 40–70%
Test: Reels ≥30 s have at least one `rehook` row starting between 40% and 70% of runtime; rhythm roughly a new reason every 8–12 s.
How: read `t + %` of rows with `rehook` ≠ `no`.
Severity: WARN.
False positive: Reels under 30 s; single-shot loops where the whole Reel is shorter than one re-hook interval; a viewer-job question opened early whose reveal sits in that window (counts).

### K11 · Peak in the last third; last beat not sad
Test: the strongest moment (biggest payoff, reveal, or highest felt state) sits in the last third; the last beat's felt state is ≥ +1 (relief, surprise, practical use, laughter), not sadness or regret.
How: read `V` if filled, else `role: payoff` position and the last line's tone.
Severity: WARN.
False positive: cautionary tales whose last beat turns the loss into a rule (practical use counts as high arousal); hook-first demos where the result shows in frame 1 and the last third holds the bigger second payoff.

### K12 · Competence before failure
Test: any failure, mistake or "I was wrong" beat comes after a competence signal (a result, a number, a credential, a finished thing on screen).
How: find rows with failure language ("broke", "ruined", "I was wrong", "messed up"); check an earlier row shows proof of skill.
Severity: WARN.
False positive: comedy or relatable shapes where the failure is the joke and no teaching claim follows; a hook that shows the finished result counts as the competence signal.

### K13 · Myth stated after the fact
Test: in myth-bust shapes, the fact comes first, a warning precedes the myth ("people say…"), the myth is stated once, and ≤3 counter-arguments follow.
How: find the myth line; check a fact line precedes it and that it is not repeated.
Severity: WARN.
False positive: a hook that quotes the myth as a contrarian opener and corrects it within the hook beat (fact lands within ~3 s); a reaction to a clip where the myth is the clip.

### K14 · Ask allowed by stage
Test: the `ask` slug is in `asks open` for the stage read; at most one ask; no ask in the first 3 s; no outro, sign-off or end card; send lines are situational (no "share this", quotas or gates).
How: compare the header `ask` to endings §4.2 and the strategy block's CTA policy; scan the last two rows for sign-off phrases; scan send lines for "share", "send this", numbers of people, "to find out".
Severity: WARN (the outro/end-card ban is a design decision; report it first).
False positive: an engagement-bait scan flagging a relevant situational send line (human decides); a series label ("#7") read as a follow ask.

### K15 · No invented facts
Test: every number, price, time, result, quote, tool feature or claim of experience in the script has a source pointer in the header `sources` (the creator's own notes, a measured test, a primary source with date). No experience is invented for the creator.
How: extract numbers, named products, superlatives and "I did/tested/found" lines; match each to a `sources` entry. Unmatched = FAIL. Perishable facts carry "as of <month>".
Severity: **FAIL**.
False positive: opinions framed as opinions ("I prefer…"); made-up examples labeled as examples in a demo or template (never in a script to be recorded as true); round illustrative numbers clearly spoken as hypothetical ("say you have ten minutes").

### K16 · Visual change gap
Test: no stretch over ~6 s without a new visual (WARN at >5 s). A related cut, POP, CUTAWAY, SCREEN or PUNCH counts as a change; a face-only run counts as no change.
How: walk the rows in time order; list the moments a new visual starts (row `visual` changes, `cut_type` related/unrelated, POP/CUTAWAY/SCREEN/PUNCH triggers); flag any gap >5 s, and any face-only run >5 s.
Severity: WARN.
False positive: a deliberate held beat (the one SIL, a deadpan-hold, a confession on the face) written as such in the card; a demo shot where the action on screen is the change.

## Output line

Write the result to the card header:
`lint: pass K1–K13 | WARN K3 (+8%), K8 (PUNCH 6/5) | FAIL none`
Then list each WARN as: `K# · row · what · suggested fix` (≤5, biggest retention risk first). A FAIL lists every unsourced claim with its row.
