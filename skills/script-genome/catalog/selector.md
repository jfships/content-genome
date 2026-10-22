# Selector: idea → skeleton

Returns 2 candidates + 1 wildcard for one Reel, each a skeleton (shape or arc) with an optional operator and the line rule, each with its checks. The header it writes is the top of the script card. Every mapping here is craft logic (INFERENCE); no study validates any of it at 20–60 s. Load only the cards you need: find a card by its `### <slug> ·` heading (card index at the end of this file) and read that card, not the whole file.

Inputs: idea type (demo, tip, opinion, story, comparison, news, list), raw material (what the creator actually has), runtime, feeling target (from the Idea Record), the brand's strategy file (stage, goal per Reel, CTA policy; if missing: no comment, follow or lead asks), the last 3 posts' headers (variety).

## Step 0: runtime gate

| Runtime | Words @2.4 w/s | Beats | Fits | Does not fit |
|---|---|---|---|---|
| 15–30 s | 36–72 | 3–4 | abt, but-therefore, problem-solution-twist, reversal, rule-of-three-with-break, before-after (3–4 beats), man-in-hole (4, hook folded), myth-vs-truth (4), kishotenketsu-twist; shapes hook-payoff-loop, myth-bust, list-of-3, pas, before-after, walkthrough, answer-first | cinderella, hero-short, origin-story (full), quest (full), confession-redemption (tight), mystery-box with false answer, two-truths-and-a-lie, seven-part-story |
| 31–45 s | 74–108 | 4–5 | everything except below | cinderella under 45, hero-short under 45, seven-part-story |
| 46–60 s | 110–144 | 5–6 (7 for lists and ladders) | all | none; check every beat ≥ 5 s |

Use the creator's measured pace if known. Words are spoken words; cut ~10% when a screen demo or a card needs silent reading time.

## Step 1: order (decision: picked by the idea)

| Idea | Order | Why |
|---|---|---|
| Demo or tool: the viewer wants the output | Result first | The result is the proof and the hook; hiding it wastes the first 3 s |
| Personal story: the viewer must care about the person | Story, then proof | Identification first; proof lands at ~40% (seven-part-story) or in the therefore beat |
| Hybrid | Promise the result in the hook, hold the proof | Use mystery-box over a result arc, or seven-part-story with a result-teaser hook |

No source settles result-first against story-first; this split is a choice, tested on the creator's own retention graphs.

## Step 2: shape or arc

- Teaching-led (tip, demo, list, news, comparison) → a shape from `shapes.md`.
- Story-led, or the feeling is the point (story, opinion with a personal turn) → an arc from the family files.
- Twins (same skeleton): use the shape's word budget with the arc card's valence and edit lines. When a shape and its twin arc differ in order, the shape's order wins for teaching ideas and the arc's order for story ideas; take only the edit lines that fit the order you keep.

| Shape | Twin arc (file) |
|---|---|
| before-after | before-after (`arcs-setback.md`, opens on the before) |
| myth-bust | myth-vs-truth (`arcs-argument.md`) |
| i-tested | experiment-test-result (`arcs-argument.md`) |
| comparison | debate-verdict (`arcs-argument.md`) |
| abt-story | abt (`arcs-operators.md`) |
| list-of-3 (mistakes variant) | mentor-wish-i-knew (`arcs-argument.md`) |
| skit-pov | escalation-to-absurdity (`arcs-ladder.md`) |
| hook-payoff-loop | full-circle (`arcs-operators.md`) |

## Step 3: material → candidates

| Raw material | Ask | Candidates, in rank order (slug · file) | Why | Avoid |
|---|---|---|---|---|
| A finished result | Is the before visible? | result-first-demo · shapes; before-after · shapes/setback; transformation-montage · rise; in-medias-res · operators | The proof is the skeleton | mystery-box that gives the cause in the hook |
| | Was there a setback on the way? | man-in-hole · setback; fail-fail-win · setback; escalating-problem · ladder; cinderella (≥45 s) · setback | Setbacks carry suspense; result first shows competence | rags-riches with no dip |
| A mistake (the creator's own) | Did it cost something real? | icarus · fall (visible cause); riches-rags · fall; confession-redemption · setback | Cost + visible cause + rule | humblebrag mistakes |
| | Did a fix come out of it? | man-in-hole · setback; oedipus · setback; mentor-wish-i-knew · argument | `because` insight beat | sad-only endings |
| An opinion | Does it oppose a common belief? | hot-take · shapes; reversal · curiosity; problem-solution-twist · setback; myth-vs-truth · argument; abt · operators | The but is the claim | mystery-box (nothing hidden) |
| | Did the creator once hold the opposite? | lesson-learned · setback | Needs a competence signal | no public past belief |
| A comparison | Does the creator rule between them? | comparison · shapes; debate-verdict · argument; experiment-test-result · argument; two-sides · argument | Verdict conditional on the viewer's case | strawman side |
| | Is one side a giant? | underdog · rise | | unfair test |
| A list (tips, tools, mistakes) | Ranked? | countdown-to-reveal · ladder (#1 teased); escalation · ladder | #1 gets the peak, first or last | >3 items at ≤45 s |
| | Unranked? | list-of-3 · shapes; mentor-wish-i-knew · argument; rule-of-three-with-break · ladder | Three items with `because` | generic items |
| A personal story | Rise or fall? | abt-story · shapes; rags-riches · rise; riches-rags or icarus · fall; cinderella (≥45 s) · setback; seven-part-story (60 s) · shapes | Pick the curve that matches what happened | invented drama |
| | Ends where it started? | full-circle · operators | | |
| | A day or a process? | day-in-the-life · containers; in-medias-res · operators | Needs a hidden through-line | |
| | Does the audience know the creator? | origin-story · rise, only if yes | | new account with no pull |
| A news item (real event) | Cautionary? | cautionary-tale · fall; answer-first · shapes | Real and checkable only | invented events |
| | Surprising detail? | discovery · curiosity; reversal · curiosity; answer-first · shapes | Surprise, interest and usefulness predict sharing (other medium) | |
| A how-to | One technique? | walkthrough · shapes; problem-solution-twist · setback; kishotenketsu-twist · curiosity; pas · shapes | | cinderella |
| | Many steps or a challenge? | quest · containers; transformation-montage · rise; ticking-clock · ladder | Step labels (signaling) | teaching without labels |
| A hidden cause or discovery | Can the gap be shown? | mystery-box · curiosity; investigation · curiosity; discovery · curiosity | The gap must be visible | result-first hook that gives the cause |
| A viewer question or comment | Real comment? | reaction-reply · shapes; answer-first · shapes; objection-answer · shapes | | invented comments |
| A belief people hold that is wrong | One myth only? | myth-bust · shapes; myth-vs-truth · argument; two-truths-and-a-lie · curiosity (≥40 s) | Fact before myth | more than one myth |

Wildcard: one candidate from a different family than the two picks (often an operator over the first pick, or a ladder), so the creator sees a real alternative.

## Step 4: feeling target → arcs

| Feeling | Arcs |
|---|---|
| curiosity | mystery-box, investigation, kishotenketsu-twist |
| surprise | reversal, kishotenketsu-twist, discovery |
| laughter | escalation-to-absurdity, rule-of-three-with-break, escalation; shape joke-compressed |
| relief | man-in-hole, fail-fail-win, problem-solution-twist |
| awe | escalation, transformation-montage, rags-riches |
| outrage-at-a-wrong | riches-rags, cautionary-tale, myth-vs-truth |
| nostalgia | origin-story, full-circle |
| relatable | man-in-hole, fail-fail-win, mentor-wish-i-knew; shape skit-pov |
| inspiration | rags-riches, cinderella, underdog |
| fomo | discovery, countdown-to-reveal, ticking-clock |

Share drivers in the one large study (news articles, other medium): awe, anger, anxiety, surprise, interest, practical usefulness; sadness predicted less sharing. Nostalgia and sad endings have the least support for sends.

## Step 5: five checks before a candidate is offered

1. **Proof.** Every beat can be shown with an asset the creator really has (screen, object, number, receipt, footage). If a beat has nothing to show, drop the candidate or change the beat. Invented experience is a hard fail (`check/gates.md`).
2. **Beat size.** Every beat ≥ 5 s and ≥ 12 words, except the hook beat (≤ 8 spoken words carrying the point in ~3 s). Use the card's `@30` fold notes; if folding still leaves a beat short, go to a longer runtime or a smaller skeleton.
3. **Hook and ending clash.** The hook is not on the card's Clashes list; the ending is not on it; the ending is allowed at the brand's stage (default "no audience yet": payoff-stop, button, deadpan-hold, callback, verbal-loop, visual-loop, plus optional send-line). Run this check only for the chosen candidate, after the pick, with its hook and ending cards loaded.
4. **Variety.** Not the same skeleton + hook pair as any of the last 3 posts in the same series, unless the log shows that pair over-performing.
5. **Operator and line rule.** At most one operator; check the stacking rules (`arcs-operators.md`). The but-therefore lint (`card/lint.md` K1) always runs.

## Line rules backed by research (all by analogy, none tested on Reels)

| Rule | How to apply | Basis |
|---|---|---|
| Thinking words at the turn | Concrete scene nouns in the first beat; pronoun-and-action sentences in the middle; `because`, `turns out`, `which means`, `I realized` clustered in the turn beat. For teaching Reels, keep thinking words rising to the last line. | RESEARCH: ~40,000 narratives vs 30,000 factual texts; stories move from staging words to action words to cognitive words; talks keep rising to the end (texts ≥ 250 words, other medium) |
| Competence before failure | Before any failure, admission or confession beat, show a competence signal: a result, a number, the finished thing. When the account is new, put it in the hook as a proof flash (a number, a real screen, "my business runs without me") that is NOT the story's final reveal; a setback arc's result-first clash is about giving away the climb, and a competence flash doesn't. | RESEARCH (pratfall, 1966): a competent person's blunder raises liking; an average person's lowers it |
| Reveal last; twists bigger and rarer | One or two real twists, the biggest last; hold the answer to the final beat. A partial payoff by ~50% is fine; the big reveal sits at ~80–95%. | RESEARCH (economic theory, no viewer data): suspense-optimal plots use larger, rarer swings and reveal in the last period |
| Re-anchor after a twist | The line right after a twist or surprise says plainly what it means now (`which means …`), shown as a one-line card. | RESEARCH (ads, face-coding + eye-tracking): surprise cuts drop-off only for a moment and pulls attention off the story |
| End high-arousal or useful, not sad | The last beat is ≥ +1 on the valence line: relief with a use, awe, surprise, or a rule to apply. A fall arc ends on the rule, never on regret. | RESEARCH (6,956 news articles + lab studies, other medium): arousal drives sharing; sadness predicts less |
| Fact before myth; ≤ 3 counter-points | State the fact first, warn before naming the myth, say the myth once and small, give the alternative explanation, end on the fact. At most three counter-points. | RESEARCH (misinformation correction, text, other medium): myths gain familiarity when repeated; three counter-arguments beat twelve |

## Output: script card header (6 lines)

```
skeleton: <slug> (<shape|arc>, family: <family>)  operator: <slug|none>  line-rule: but-therefore[+abt]
runtime: <s>  words: <n> @<w/s>  beats: <n>  order: result-first|story-then-proof|hybrid
feeling: <slug>  idea-type: <type>
hook: <slug>  spoken: "<words>"  text: "<3–7 words>"  image: "<first frame>"
ending: <slug>  peak-in-last-third: yes|no  last-beat-valence: <+1|+2>
checks: proof ok|<gap>, beat-size ok|<beat>, clash ok|<pair>, variety ok|<repeat>, stack ok
```

Offer the two candidates and the wildcard as: shape/arc (+ operator, line rule) + a two-line example in the creator's topic + what it changes + one line on what the creator would need to show. Fill this full header (hook, ending, checks) only for the chosen candidate, after the pick, loading its card(s) then. Show evidence grades only when the pick rests on a single source, a vendor claim or inference.

## Card index

Find the card by its heading `### <slug> ·` in the file and read only that card.

| File | Card slugs |
|---|---|
| `shapes.md` | result-first-demo, hook-payoff-loop, before-after, i-tested, walkthrough, list-of-3, myth-bust, pas, answer-first, objection-answer, abt-story, seven-part-story, hot-take, comparison, joke-compressed, skit-pov, reaction-reply, loop-back, aida, ugc-ad, question-answer-twist |
| `arcs-setback.md` | before-after, man-in-hole, fail-fail-win, cinderella, oedipus, problem-solution-twist, lesson-learned, confession-redemption |
| `arcs-fall.md` | riches-rags, icarus, cautionary-tale |
| `arcs-rise.md` | rags-riches, transformation-montage, underdog, origin-story |
| `arcs-curiosity.md` | mystery-box, investigation, discovery, reversal, kishotenketsu-twist, two-truths-and-a-lie |
| `arcs-ladder.md` | escalation, ticking-clock, countdown-to-reveal, escalation-to-absurdity, rule-of-three-with-break, escalating-problem |
| `arcs-argument.md` | two-sides, debate-verdict, myth-vs-truth, experiment-test-result, mentor-wish-i-knew |
| `arcs-containers.md` | three-acts, hero-short, quest, day-in-the-life |
| `arcs-operators.md` | in-medias-res, full-circle, but-therefore, abt |
| `hooks.md` | result-first, proof-first, value-promise, bold-claim, contrarian, question, curiosity-gap, number, callout, warning, stakes, mid-action, secret, pov-setup, visual-prop, interrupt, confession, context-first, habit-break |
| `hooks-psych.md` | info-gap, loss-frame, negativity, social-proof, self-reference, status, prediction-error, selective-exposure, novelty, concreteness, authority, gift, pratfall, humor, awe, moral-outrage, nostalgia, us-vs-them, scarcity, anchoring, direct-address, face-gaze, prosody, contagion, threat, taboo, effort-min, controversy |
| `hooks-unusual.md` | silent-open, sound-first, asmr-open, cut-to-silence, false-start, word-reveal, title-card, prop-reveal, flip-reveal, odd-frame, lo-fi-open, reaction-first, mid-thought, mid-conversation, fake-out, anti-hook, wait-for-it, news-tease, standup-frame, format-mismatch, skit-character, split-debate, trend-hijack, pov-open, permission-grant, screen-first, tool-glitch, side-by-side, impossible-shot, timer, mental-challenge, comment-reply, remix-reply, reverse-psych, algorithm-talk, one-word |
| `retention.md` | result-then-process, but-therefore, escalating-problem, tease-rehook, stacked-loops, viewer-job, progress, interrupt-rehook, info-density, payoff-ladder, hard-stop, early-surprise, mid-recap |
| `endings.md` | payoff-stop, deadpan-hold, button, callback, verbal-loop, visual-loop, open-question-loop, tease-next, send-line, save-prompt, follow-reason, comment, keyword-comment, slogan |
