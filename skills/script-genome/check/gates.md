# Hard gates (job B, and lint before a card is handed on)

The only things that FAIL a script. Everything else is a note. Each finding quotes the line, says what fails in one sentence, gives the smallest fix, says confidence (H/M/L) and who decides. Platform rules drift: re-check items marked ⟳ against the platform's current pages every quarter.

Status per gate: PASS · FAIL · N/A · NEEDS-INFO (the script can't show it; ask the creator).

## Legal and platform
| ID | Test | How to check | Basis | Ignore if |
|---|---|---|---|---|
| L1 | Any material connection to a brand or tool mentioned (paid, free product/plan/credits, affiliate link, equity, job, family/friend) is disclosed **spoken and on screen**, early, near the endorsement. | Ask (worksheet line 9); then find the line. | US FTC endorsement guides: in-video disclosure, audio and/or on screen; caption-only or vague tags (sp, collab, ambassador) don't count; free products count. | No connection (no need to say "not sponsored"). |
| L2 | Branded content uses the platform's paid-partnership label ⟳. | NEEDS-INFO at script stage; on the publish checklist. | Instagram branded content policy. The label does not replace L1. | No brand deal. |
| L3 | Every "I use / I tried / I love" claim is true (used it, when, which version); nothing praised that the creator didn't find good. | Creator confirms. | FTC: no endorsing experience you didn't have. | Opinion clearly marked as hearsay. |
| L4 | Every performance, speed, savings, accuracy, income or "replaces X" claim is backed by the creator's own shown test or a cited source. "AI" gets no exemption. | List claims; each needs a proof pointer. | FTC actions on AI claims ("no AI exemption"); substantiation rules. | Pure opinion ("I like it"). |
| L5 | A result that isn't typical says so, or is framed as "my result". | Find result numbers. | FTC guidance on atypical results. | No result number used. |
| L6 | No fabricated reviews, testimonials, comments, DMs, reactions or tool outputs. | Ask where each came from. | FTC rule on fake reviews (2024); platform authenticity direction. | Clearly labeled skit or example. |
| L7 | Realistic AI-generated or altered voice, face or event is labeled in-platform and not deceptive ⟳. | Worksheet line 10. | Meta AI-label requirement; EU AI Act deepfake disclosure (from Aug 2026). | AI used only for scripting, captions, color, spelling; obviously fantastical art. |
| L8 | Original: the creator's own footage, demo or commentary; no other app's watermark; not mostly someone else's clip. ⟳ | Script: is the commentary the content? File: on the publish checklist. | Instagram originality rules (recommendation eligibility; extended to all formats April 2026). | Remix/reaction with real added commentary. |
| L9 | No engagement bait or clickbait: no "tag a friend", "like if", "comment X to…" built to inflate reach, "share to find out"; no promise the video doesn't keep. ⟳ | Scan + human ruling. | Instagram recommendation guidelines list clickbait and engagement bait; 2024 statement on explicit asks for comments/shares (then clarified: sincere questions are fine). | A situational "send this to the friend who…" line is allowed (decision of the skill): flag only if generic or a quota. Keyword-for-resource asks: UNCERTAIN → creator decides with the stage. |
| L10 | No income or side-hustle claims ("make $X with this") unless substantiated and typical. | Scan. | Instagram "misleading business models"; FTC earnings claims. | None. |

## Accuracy and clarity
| ID | Test | How to check | Ignore if |
|---|---|---|---|
| A1 | Every concrete fact (feature, plan, price, limit, date, version, number) is checked against a current primary source; perishable ones carry "as of <month>". | Fact list with source + date. | Opinions. |
| A2 | Claim strength matches the evidence: uncertain things carry one calibrated qualifier; certain things aren't hedged into mush. | Read. | — |
| A3 | Nothing invented: no number, quote, result or experience the creator didn't give. | Compare with raw words + worksheet. | Lines marked `new` that are wording only, no new fact. |
| C1 | The core claim can be said in one sentence a stranger could repeat. | Try it. | A two-part script where part two IS the payoff. |
| C2 | Whatever the opening promises is delivered inside the runtime. | Trace the promise to a later line. | — |
| C3 | Spoken words fit the runtime at the creator's pace for this video's mode (`write/budget.md` Pace: take > pace log > mode default): spoken words ≤ budget +10%; the timed read-aloud decides. Order: subtract planned silent seconds from the budget first (budget = (runtime − silent s) × pace), then add the 10–15% pause allowance to the estimated time (words ÷ pace). | `write/budget.md`. Alternatives: count the main (first-listed) hook/ending. Elided text ("…") → NEEDS-INFO. | Silent demo beats (already subtracted from the budget). |
| C4 | No sentence that can't be said in one breath: flag >25 words, 3+ nested clauses, tongue-twisters, unpronounced tool names. | Count + read. | A deliberate long build-up. |
| C5 | Every term the target viewer may not know is glossed in ≤5 words or cut. | Read as the audience. | Audience is expert. |
| C6 | One next step, or none; it matches the payoff. | Count asks. | — |
| C7 | Captions planned and matching the spoken words; on-screen text readable (contrast ≥4.5:1, 3:1 for large text) and inside the safe box. | Card fields / design. | — (benchmark: WCAG captions and contrast) |

## Never gates
Shape, hook type, arc, ending type, "has a CTA", "has a question", sentence style, power words, AI-word counts, readability scores (Flesch is invalid for speech). These are notes at most (`craft.md`).
