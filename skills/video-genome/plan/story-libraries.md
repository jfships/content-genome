# Story libraries

The parts a video's content is assembled from. The brand dresses the result (look, motion, sound, voice); these libraries never decide those. Every library is open to every brand: the plan picks per video, filtered by the brand's personality, formats, truth rules and house rules.

> **Mechanics live where**
> - This file is the slug registry plus edit craft. The script mechanics (beats with % and seconds, line skeletons, pairs/clashes, fails when, evidence) live in the sibling skill **script-genome**, `catalog/`:
>   §2 frameworks → `shapes.md` · §3 arcs → `arcs-setback.md`, `arcs-fall.md`, `arcs-rise.md`, `arcs-curiosity.md`, `arcs-ladder.md`, `arcs-argument.md`, `arcs-containers.md`, `arcs-operators.md` (operators and line rules) · §4 hooks → `hooks.md` (mechanism per layer: `hooks-psych.md`; odd formats: `hooks-unusual.md`) · §6 retention → `retention.md` · §9 CTAs → `endings.md` · picking across them → `selector.md`.
> - A Reel's or long video's script arrives as a **script card** (script-genome `card/schema.md`). Its header names shape, arc, operator, line rule, hook layers (spoken / screen text / first image) and ending; its beats carry edit-intent codes. **Gate 1 reads that header** instead of re-picking those layers here.
> - **Shorts:** script-genome writes the script. `shorts/shapes.md` slugs are aliases of script-genome shapes (`hook-payoff-loop`, `myth-bust`, `list-of-3`, `before-after`, `skit-pov`, `reaction-reply`).
> - Slugs here never get deleted or renamed: old plans must still resolve. Aliases sit in the row.

**Rule for adding options.** No option is added to any library in this file (or in `craft/graphics-library.md`) without its mechanics and a use-case map: what it does · the script line or beat that calls it (trigger) · timing and placement · pairs / clashes · fails when · use when (idea types, beat role). Script mechanics go in script-genome first; this file gets the row and the pointer.

## How to pick: the story stack

The plan names one **story stack** per video, by slug:

| Layer | Pick | From |
|---|---|---|
| Video type | 1 (a second only for a clear section change) | §1 |
| Script framework | 1 | §2 |
| Story arc | 1 (optionally + 1 operator + 1 line rule) | §3 |
| Hook | 3–6 options written, 1 kept in the edit | §4 |
| Proof | 1–3, the strongest first | §5 |
| Retention devices | 2–4 | §6 |
| Pacing pattern | 1 | §7 |
| Editing techniques | 3–6 allowed | §8 |
| Call to action | 1 main, at most 1 mid-video | §9 |
| Feeling target | 1 (from the Idea Record) | §10 |
| Platform mechanics | 0–2, vertical only | §11 |

When a script card exists, its header supplies framework/shape, arc (+ operator + line rule), hook and ending; the plan fills the rest.

The **angle** and **title formula** come from the Idea Record; don't re-pick them here (the plan only asks when the record has none).

**Compatibility check (gate 1).** Read the stack as one sentence: "A <type> that runs <framework> over a <arc> arc (or <arc> + <operator> + <line-rule>, as the script card header gives it), opens on a <hook> hook, proves it with <proof>, holds with <retention>, cuts <pacing>, and ends with <CTA>, to make them feel <feeling>." If any part fights another, change one. Known clashes:
- Ticking clock + calm with bursts: the clock needs pressure; pick front-loaded or relentless.
- Mystery box + result-first hook: the result kills the mystery; pick curiosity gap or mid-action.
- Text-on-screen story + talking-head techniques (J/L cuts, punch-in): pick text-native moves.
- Relentless pacing + strategic silence more than once: one held pause, max.
- Faceless voiceover + real testimonial on camera: fine, but the testimonial is the only face; say so.
- Hard ask CTA + "entertaining" leading the personality: use soft or loop instead unless the brand says otherwise.
- Hook → Context → Payoff → Loop belongs to vertical; for long-form pick another framework. Shorts don't use the story stack: they pick one shape from `shorts/shapes.md` (aliases of script-genome shapes) and get their script from script-genome.

**Vary on purpose.** Read the last 3 episodes' stacks in `03 Videos/results-log.md`. Don't repeat the same arc and hook pair twice in a row unless the log shows it over-performing.

## 1. Video types (how it's made)

| Slug | Type | What it is | Needs | Fits shapes/arcs | Script notes |
|---|---|---|---|---|---|
| talking-head | Talking head | Face to camera carries it | Camera take | claim-evidence, but-therefore, man-in-hole, reversal, myth-vs-truth | Face on hook and opinion beats; any claim that can be shown gets a CUTAWAY or SCREEN beat |
| explainer | Explainer, graphics-led | Graphic-heavy, voice over | Script, voice, many scenes | what-sowhat-nowwhat, abt, kishotenketsu-twist, mystery-box | Every line names a thing the graphic can show; one idea per beat |
| cinematic | Cinematic / B-roll essay | Mood shots, music, narration, little face | B-roll, narration | full-circle, rags-riches, origin-story, transformation-montage | Fewer, slower lines (below 2.4 w/s); narration names what's on screen |
| ugc | UGC style | Phone-shot, selfie, feels like a real person's post | Phone take, natural light | ugc-ad, bab, lesson-learned, discovery | Spoken like a message to a friend; the phone footage is the proof |
| demo | Product or screen demo | The thing working, step by step | Screen recordings or object | result-first, before-after, problem-solution-twist, experiment-test-result | Needs SCREEN beats; result first, then how; step lines are procedural ("click", "type") |
| tutorial | Tutorial / how-to | Viewer can follow along | Clear steps, close shots | hook-proof-process, mistakes-list, countdown, quest | STEP label on every step; slower pace over demo beats (90–130 wpm) |
| documentary | Documentary | Real events, interviews, narration, archive | Interviews, archive, narration | investigation, cautionary-tale, three-acts, in-medias-res | Mostly long-form; every claim traced to a real source or clip |
| vlog | Vlog | Following the creator through a day or event | Run-and-gun footage | day-in-the-life, quest, ticking-clock | The hook states a through-line; time stamps as STEP |
| pov | POV | First-person camera; the viewer is the creator | Head or chest camera | in-medias-res, ticking-clock, escalation | Hook text "POV: …" carries the setup; few spoken words |
| faceless | Faceless voiceover | Visuals and voice, no face | Voice, visuals | abt, myth-vs-truth, countdown-to-reveal, discovery | Voice carries the explanation, picture carries the object; trust comes from proof |
| interview | Interview / conversation | Two people, question and answer | Two mics, two angles | question-answer-twist, two-sides, debate-verdict | Script = question list + cut order; the guest's best line goes in the hook |
| podcast-clip | Podcast clip | A cut moment from a longer talk | Long recording | claim-evidence, reversal, lesson-learned | Open on a self-contained claim; cut any line that needs earlier context |
| reaction | Reaction / commentary | The creator's take over another clip | Rights to the clip or fair-use care | claim-evidence, myth-vs-truth, objection-answer | The take is the point; the clip is proof, shown short (PIP or SPLIT) |
| skit | Skit / sketch | Acted scene, characters, punchline | Script, takes, maybe costumes | escalation-to-absurdity, rule-of-three-with-break, reversal | Lines are dialogue; the button line is the ending |
| street | Street interview | Asking strangers one question | Consent, mic | two-truths-and-a-lie, countdown, discovery | One question asked the same way each time; best answer first or last |
| unboxing | Unboxing / first look | Opening and judging something live | The object | mystery-box, experiment-test-result, before-after | Verdict held to the last third; first image = the closed box |
| review | Review | Verdict on a product, place or tool | Hands-on time | experiment-test-result, debate-verdict, claim-evidence | Verdict with conditions ("for you if …"); proof before verdict |
| bts | Behind the scenes | How the thing really gets made | Process footage | in-medias-res, fail-fail-win, origin-story | Show the mess; one real setback makes it a story |
| process | Process / satisfying | No talk, the craft itself | Clean close-ups, sound | transformation-montage, before-after | No spoken line; screen text (or none) and sound carry it; final state held ≥2 s |
| montage | Montage / recap | Fast collection of moments to music | Many clips | transformation-montage, countdown, escalation | Music picked before the cut; text cards carry any words |
| text-story | Text-on-screen story | Words carry it, no voice | Strong copy | abt, reversal, but-therefore, two-truths-and-a-lie | No spoken line; words carry the hook; reading-time rule (§5) sets each card's hold |

## 2. Script frameworks (order of information)

The format's beats (from the brand) are the episode's skeleton; the framework sets the order inside them. Scale: long = long-form video; short = 15–60 s vertical. **Mechanics** = file in script-genome `catalog/`, anchor = slug.

| Slug | Framework | Order | Family/type | Scale | Mechanics |
|---|---|---|---|---|---|
| hook-proof-process | Hook → Proof → Process → CTA | Show result, prove it's real, show how, ask | result-first | both | `shapes.md#hook-proof-process` |
| hook-problem-solution | Hook → Problem → Solution → CTA | Core short-form order | problem-first | both | `shapes.md#hook-problem-solution` |
| pas | Problem → Agitate → Solve | Name the pain, make it hurt, fix it | problem-first | both | `shapes.md#pas` |
| bab | Before → After → Bridge | Now, the dream, the way across | transformation | both | `shapes.md#bab` |
| aida | AIDA | Attention, interest, desire, action (offers) | offer | both | `shapes.md#aida` |
| hook-context-payoff-loop | Hook → Context → Payoff → Loop | Minimal setup, payoff, end feeds the start (vertical) | loop | short | `shapes.md#hook-context-payoff-loop` |
| ugc-ad | Hook → Context → Value → Proof → CTA | UGC ad order | offer | short | `shapes.md#ugc-ad` |
| claim-evidence | Claim → Evidence → So what | Opinions, myth tests | argument | both | `shapes.md#claim-evidence` |
| what-sowhat-nowwhat | What → So what → Now what | Fact, why it matters, what to do | explain | both | `shapes.md#what-sowhat-nowwhat` |
| question-answer-twist | Question → Answer → Twist | Obvious answer, then the surprise | twist | both | `shapes.md#question-answer-twist` |
| objection-answer | Objection → Answer | Raise the viewer's doubt, settle it | argument | both | `shapes.md#objection-answer` |
| mistakes-list | Mistakes list | N errors → why → the fix | list | both | `shapes.md#mistakes-list` |

## 3. Story arcs (how the feeling moves)

The energy arc in `run-sheet.md` (establish → develop → climax → resolve) still applies on top: the arc decides *what* the climax is. **Type** says how an arc is used: CURVE (feeling path), CONTAINER (beat frame), ORDER (operator laid over another arc), LINE-RULE (how beats join), LADDER (rising steps), ARGUMENT (claims weighed). One ORDER and one LINE-RULE can sit on one CURVE / CONTAINER / LADDER / ARGUMENT arc. No arc has been tested at 15–60 s; short timings are craft.

| Slug | Arc | Shape | Family/type | Scale | Mechanics |
|---|---|---|---|---|---|
| before-after | Before / After | Mess → work → reveal | setback · ARGUMENT/CURVE | both | `arcs-setback.md#before-after` |
| man-in-hole | Man in a hole | Fine → trouble → climb out better | setback · CURVE | both | `arcs-setback.md#man-in-hole` |
| rags-riches | Rags to riches | Steady rise from nothing | rise · CURVE | both | `arcs-rise.md#rags-riches` |
| riches-rags | Riches to rags | Fall, then the lesson (cautionary) | fall · CURVE | both | `arcs-fall.md#riches-rags` |
| icarus | Icarus | Rise, then the crash | fall · CURVE | both | `arcs-fall.md#icarus` |
| cinderella | Cinderella | Rise, crash, bigger rise | setback · CURVE | long, or short ≥45 s | `arcs-setback.md#cinderella` |
| three-acts | Three acts | Setup, conflict, resolution | containers · CONTAINER | both | `arcs-containers.md#three-acts` |
| hero-short | Hero's journey, short | Leave comfort, trials, return changed | containers · CONTAINER | long, or short ≥45 s | `arcs-containers.md#hero-short` |
| in-medias-res | In the middle of it | Open mid-action, rewind, catch up, finish | operators · ORDER | both | `arcs-operators.md#in-medias-res` |
| escalation | Escalation ladder | Each step bigger than the last | ladder · LADDER | both | `arcs-ladder.md#escalation` |
| but-therefore | But / Therefore chain | Every beat joins with "but" or "therefore", never "and then" | operators · LINE-RULE | both | `arcs-operators.md#but-therefore` |
| mystery-box | Mystery box | Question up front, clues, reveal | curiosity · ORDER | both | `arcs-curiosity.md#mystery-box` |
| ticking-clock | Ticking clock | A deadline drives every beat | ladder · LADDER | both | `arcs-ladder.md#ticking-clock` |
| full-circle | Full circle | End where it began, changed | operators · ORDER | both | `arcs-operators.md#full-circle` |
| fail-fail-win | Fail, fail, win | Two honest failures before it works | setback · LADDER | both (≥30 s) | `arcs-setback.md#fail-fail-win` |
| two-sides | Two sides | The same event from two viewpoints | argument · ARGUMENT | both | `arcs-argument.md#two-sides` |
| oedipus | False fix | Fall → fake fix → worse fall → real fix + rule | fall · CURVE | both | `arcs-setback.md#oedipus` |
| abt | And, but, therefore | Shared world ("and"), the problem ("but"), the result ("therefore"); 3 beats | operators · LINE-RULE/CONTAINER | both (fits 15 s) | `arcs-operators.md#abt` |
| kishotenketsu-twist | Four-part twist | Set up, develop, new angle on the same things, tie up; no conflict needed | containers · CONTAINER | both | `arcs-curiosity.md#kishotenketsu-twist` |
| reversal | Reversal | Build an assumption → one-line pivot → reframe → button | operators · ORDER | both | `arcs-curiosity.md#reversal` |
| problem-solution-twist | Problem, solution, twist | Problem → obvious fix → why it fails → real fix | containers · CONTAINER | both | `arcs-setback.md#problem-solution-twist` |
| lesson-learned | I was wrong | Old belief → trigger → admission → new belief → what it means for you | setback · CURVE | both | `arcs-setback.md#lesson-learned` |
| transformation-montage | Transformation montage | Before → 5–12 quick flashes → final state → caption | rise · CURVE/ORDER | both | `arcs-rise.md#transformation-montage` |
| countdown-to-reveal | Countdown to reveal | Promise → lower ranks → #1 reveal → outro | ladder · LADDER | both | `arcs-ladder.md#countdown-to-reveal` |
| escalation-to-absurdity | Escalation to absurdity | Three rungs → absurd break → snap back | ladder · LADDER | both | `arcs-ladder.md#escalation-to-absurdity` |
| rule-of-three-with-break | Rule of three with a break | A, B, then the break, button; fits inside another arc | ladder · LADDER (micro) | short | `arcs-ladder.md#rule-of-three-with-break` |
| escalating-problem | Escalating problem | Each fix causes a bigger problem; one cascade at 30 s, two at 45–60 s. Aliases: rick-and-morty | ladder · LADDER | both | `arcs-ladder.md#escalating-problem` |
| two-truths-and-a-lie | Two truths and a lie | Rules → three statements → guess pause → reveal + why | argument · ARGUMENT | both | `arcs-curiosity.md#two-truths-and-a-lie` |
| debate-verdict | Debate, then verdict | Question → case A → case B → criteria + verdict | argument · ARGUMENT | both | `arcs-argument.md#debate-verdict` |
| quest | Quest / mission | Mission + stakes → obstacle → tool → final test → outcome | containers · CONTAINER | long, or short ≥45 s | `arcs-containers.md#quest` |
| mentor-wish-i-knew | What I wish I knew | Regret hook → past mistake → up to 3 lessons with "because" → gift line | argument · ARGUMENT/CURVE | both | `arcs-argument.md#mentor-wish-i-knew` |
| discovery | I found out | Everyday context → finding → verify → implication | curiosity · ORDER | both | `arcs-curiosity.md#discovery` |
| confession-redemption | Confession and repair | Confession → cost → turn → repair → redemption | setback · CURVE | long, or short ≥45 s | `arcs-setback.md#confession-redemption` |
| underdog | Underdog | Giant → limits → odd tactic → showdown result → meaning | rise · CURVE/ARGUMENT | both | `arcs-rise.md#underdog` |
| investigation | Investigation | Anomaly → wrong guess → evidence → pivot → finding | curiosity · ORDER | both (≥30 s) | `arcs-curiosity.md#investigation` |
| experiment-test-result | Experiment / test | Question → method → results → verdict + conditions | argument · ARGUMENT | both | `arcs-argument.md#experiment-test-result` |
| cautionary-tale | Cautionary tale | Someone else's want → shortcut → consequence → rule → action | fall · CURVE | both | `arcs-fall.md#cautionary-tale` |
| origin-story | Origin story | Ordinary → spark → struggle → breakthrough → now | containers · CONTAINER | long, or short ≥45 s | `arcs-rise.md#origin-story` |
| day-in-the-life | Day in the life | Hook → time-stamped scenes → tool-moment payoff → sign-off | operators · ORDER | both | `arcs-containers.md#day-in-the-life` |
| myth-vs-truth | Myth vs truth | Warning + truth → labelled myth → why people believe it → evidence → do this instead | argument · ARGUMENT | both | `arcs-argument.md#myth-vs-truth` |

## 4. Hooks (first 3 seconds)

Rules from `run-sheet.md` still apply: prove the title within 10 s; never a greeting, backstory, agenda or logo. Every kept hook fires on three layers at once: the spoken line, the on-screen text, and the first image; each carries the same idea in its own words, and the image makes sense with sound off. **Family/type** = the main mechanism (script-genome `hooks-psych.md` says which layer carries it best).

| Slug | Hook | Shape | Family/type | Scale | Mechanics |
|---|---|---|---|---|---|
| result-first | Result first | Show the outcome, then how | proof | both | `hooks.md#result-first` |
| proof-first | Proof first | Lead with the evidence | proof · authority | both | `hooks.md#proof-first` |
| bold-claim | Bold claim | Strong, surprising statement | prediction error | both | `hooks.md#bold-claim` |
| contrarian | Contrarian | Disagree with common advice | prediction error · dissonance | both | `hooks.md#contrarian` |
| question | Question | One question they need answered | curiosity | both | `hooks.md#question` |
| curiosity-gap | Curiosity gap | Name it, don't explain it yet | curiosity | both | `hooks.md#curiosity-gap` |
| number | Number / stat | A specific, real figure | concreteness | both | `hooks.md#number` |
| callout | Direct call-out | "If you run a restaurant…" | identity | both | `hooks.md#callout` |
| warning | Mistake / warning | "Stop doing this" | loss · negativity | both | `hooks.md#warning` |
| stakes | Stakes | What's at risk | loss aversion | both | `hooks.md#stakes` |
| mid-action | Mid-action | Drop in during the moment | curiosity · ORDER | both | `hooks.md#mid-action` |
| secret | Nobody talks about | Hidden or insider information | taboo · curiosity | both | `hooks.md#secret` |
| pov-setup | POV setup | "POV: you just…" | identity | short | `hooks.md#pov-setup` |
| visual-prop | Visual / prop | An object or image does the work | novelty · salience | both | `hooks.md#visual-prop` |
| interrupt | Pattern interrupt | Something odd that breaks the scroll | novelty · prediction error | both | `hooks.md#interrupt` |

## 5. Proof types

Every proof traces to `Who I Am.md` Proof or a real artifact in `07 Asset Library/`. Never invented. **Screen time** uses the reading-time rule: ≈0.3 s per word + 0.5 s, never under 1.1 s; numbers ≥1.5 s.

| Slug | Proof | Notes | Where in the script | Screen time |
|---|---|---|---|---|
| result-on-screen | Result on screen | The finished thing, visible | Before the claim (the hook beat is the claim) or on the reveal beat | ≥2 s; any number on it ≥1.5 s |
| before-after-shot | Before / after shot | Same frame, two states | Reveal beat (55–80%), after the work beat; same frame as the before | 2 s on the after; WIPE or SPLIT |
| screen-rec | Screen recording | Real dashboard, real numbers | Right after the claim, often under the line (L); procedure beats | Target held ≥1 beat after the click; labels readable at phone size |
| live-demo | Live demo | Doing it in one take | Body, after the promise; the proof beat | 4–8 s per step beat |
| numbers | Real numbers | Labeled honestly; illustrative ones say so | On the spoken number (CARD-N); as the hook or right after the claim | ≥1.5 s |
| receipts | Receipts / artifacts | Invoices, messages, documents (blur private data) | Straight after the claim ("here's the receipt") | Reading-time rule on the visible words |
| testimonial | Real testimonial | A real person, with permission; never invented | After the claim, before the ending | Quote card ≤10 words, reading-time rule |
| third-party | Third-party | Press, reviews, someone else saying it | After the claim, or as hook proof | Headline: reading-time rule |
| credentials | Credentials | Years, scale, what was run | Early (hook or beat 2), one line, before advice | Lower third ~2 s |
| show-failure | Show the failure | It breaking, then working | Setback beat, before the fix | Fail state ≥1.5 s |

## 6. Retention devices

Short = 15–60 s vertical; long = long-form. Short timings are scaled from long-form craft, not measured on Reels. **Mechanics** = script-genome `catalog/retention.md`, anchor = slug.

| Slug | Device | How | Placement (short / long) | Trigger in the script | Mechanics |
|---|---|---|---|---|---|
| stacked-loops | Stacked open loops | Close one question while opening the next | Every payoff beat / every segment end | A line that answers one question and opens the next in the same breath ("…which raises…") | `retention.md#stacked-loops` |
| q-rehook | Question re-hook | Ask the viewer something mid-video | Ask by 10–20%, answer after 50–70% / once per section | A guess or choice line ("Which one won?") the screen lets them judge | `retention.md#q-rehook` |
| tease-rehook | Tease re-hook | "In a minute, the part that broke everything" | ~Midpoint, never after ~60%; a second one before the last third at 45–60 s / before known dips | A line that closes the current point and names the next ("the next fix surprised me") | `retention.md#tease-rehook` |
| interrupt-rehook | Pattern-interrupt re-hook | Shift tone, visual or sound | Once, at the turn (valley to climb, or flip) / at topic boundaries | A new point that can be shown or heard; the INT must carry it | `retention.md#interrupt-rehook` |
| hook-deliver | Hook-deliver cycle | Every payoff followed by a new hook | Each beat boundary, ~every 8–12 s / each segment | A payoff line, then a new reason to stay | `retention.md#hook-deliver` |
| callback | Callback / running gag | Earlier setup pays off (required near the end) | Last beat / last section | An early concrete word, object or joke comes back changed | `endings.md#callback` |
| countdown | Countdown | Ranked or numbered; always "one more" | Total ≤3 at 30 s; cue updates each beat / chapters | "Three things", "number two"; STEP label | `retention.md#countdown` |
| progress | Progress markers | Chapters or a visible progress bar | Step label each beat, total small / chapters or bar | "Step 2", "last one" | `retention.md#progress` |
| rule-of-three | Rule of three | Two set up, the third breaks the pattern | Break at ~60–88% / inside a section | A list of three where item three breaks the pattern | `retention.md#rule-of-three` |
| silence | Strategic silence | One held pause after a big moment | Once per Reel, after the key claim or before the payoff (SIL 0.3–1.0 s) / once per big moment | The claim line that must land | `retention.md#silence` |
| payoff-ladder | Payoff ladder | Each payoff bigger than the last | Partial payoff by ~50%, best at 80–95% / grows per segment | Each payoff line bigger ("but this one…") | `retention.md#payoff-ladder` |

## 7. Pacing patterns (rhythm of cuts across the video)

The brand's motion table sets how things move; this sets how often cuts land. Pacing = the rate of new information, not the rate of cuts. Unrelated cuts ≤6–8 per 30 s. **⚠** = conflicts with teaching evidence (fast chaotic cutting lowers memory for complex content).

| Slug | Pattern | Shape | 30 s Reel timeline | Script requirement |
|---|---|---|---|---|
| front-loaded | Front-loaded | Fast early, eases off, late bursts | 0–8 s carries ~half the payoff (claim + proof), 2–3 visual changes; 8–30 s remaining steps + ending, settled | Result first, then how |
| calm-bursts | Calm with bursts | Steady, quick-cut bursts every few minutes | Calm 0–4, burst 4–7, calm 7–14, burst 14–17, calm 17–25, burst 25–30; effects only on bursts | Calm = explain (≤140 wpm, one hold); burst = payoff line, 3–5 words |
| return-hook | Return to the hook | Revisit the opening premise every few minutes | 0–3 s opens a loop; middle answers 2 of 3 parts; 21–27 s returns to the hook's words/visual with the payoff | Hook line and payoff line share words |
| fast-talk-slow-show | Fast talk, slow show | Quick cuts while explaining, long holds on examples | Talking beats 3.0–3.3 w/s with JUMP; demo beats 1.5–2.0 w/s, one PUSH + one highlight + one SFX | Say the claim fast, then show it with few words |
| cut-on-emotion | Cut on emotion | Cuts land on reveals, not a timer | ~4–6 cuts per 30 s, each on a stressed word or clause end | Mark the opinion/emotion lines |
| cut-to-beat ⚠ | Cut to the beat | Hard cuts on music hits (phrase length from the brand) | 100–130 bpm; cut every 4th or 8th beat (~2–4 s) | Music picked before writing; lines fit the beat grid. Montage and results beats only, never explain beats |
| relentless ⚠ | Relentless | Cut every 1–3 s, no air | Visual change every 1.3–2 s for the first 3–5 s only, then ease | Short lines, 3–5 words each |
| one-take | One take | Unbroken; tension from the lack of cuts | No cuts; 2–3 PUNCH on key words, POP, SFX | Write 2–3 edit hooks (key words) into the lines |

## 8. Editing techniques (cutting tools)

Transitions, camera moves and placements are in `craft/graphics-library.md` and the brand. These are cutting tools. Every move needs a trigger in the script; no trigger, no move. **Evidence:** A controlled study on the mechanism · B indirect research · C craft only · 0 nothing found.

| Slug | Technique | Use | Script trigger | Job | Cap per 30 s | Fails when | Evidence |
|---|---|---|---|---|---|---|---|
| jump-cut | Jump cut (JUMP) | Remove pauses, same angle; vary shot size so it looks intended | Any pause, filler, restart or trailing breath inside a beat; always on | Compress time, remove dead air | No cap; vary frame size | Same frame size every sentence; breaths removed so it sounds panicked | C |
| jl-cut | J-cut / L-cut (J, L) | Sound leads or trails the picture; smooth scene changes | J: next beat opens on a payoff, question or surprising number. L: a claim that needs proof shown while the sentence ends | Prime the next beat / proof under the voice | Not on every cut; offset 0.2–0.5 s (up to ~2 s for a big shift) | Picture under an L is unrelated to the words still playing | C |
| smash-cut | Smash cut (SMASH) | Calm to loud with no warning; comedy, shock | A hard contrast line: "You'd think it works. [cut] It doesn't." | Surprise, reversal | 1 | A joke with no teaching point | 0 (B: orienting response) |
| match-cut | Match cut (MATCH) | Two shots lined up by shape or motion | Last line echoes the first, or last frame matches the first | Closure, loop, rewatch | 1 (loop join) | Loop cuts off the ending before it lands | 0 |
| punch-in | Punch-in zoom (PUNCH) | Quick zoom on a key word | The key word, a number, an opinion line, "here" / "this" | Say which line mattered | 3–5 | Every sentence; no key word; on screen recordings it hides context | C (B: signaling) |
| speed-ramp | Speed ramp (RAMP) | Slow for drama, snap back | A step that is slow in real life ("waiting for the export"), or between demo steps | Compress time, feel of progress | 1 | Hides the step the viewer must see; used on a talking face | 0 |
| cutaway | Cutaway (CUTAWAY) | Brief shot of what's being said; hides a cut | A line names a thing that can be shown ("your dashboard") | Concrete picture for the noun | Counts toward unrelated cuts ≤6–8 | Shown after the word; decorative stock | A (multimedia, timing) |
| pip | Picture-in-picture (PIP) | Creator in a corner, other footage full | Opinion or reaction matters while the screen is the subject | Keep trust and presence | n/a | Covers the UI; sits in the unsafe right rail or bottom | B |
| split | Split screen (SPLIT) | Two things at once | Before/after, A vs B, two tools | Compare in one frame | 1–2 | Both halves change at once; text unreadable at half width | B (spatial contiguity) |
| letterbox | Letterbox moment | Bars animate in for a serious beat | A serious or high-stakes line ("this is the part that cost me") | Mark a tone shift | 1 | Used on a light line; bars crop the subject | 0 |
| freeze | Freeze frame (FREEZE) | Stop on a face or moment, label it | "This one number", "look at this setting" | Hold a still for reading | 1–2 | Nothing to read in the frozen frame | 0 |
| rewind | Rewind / replay | Run it back to show it again | "Wait, watch that again", a missed detail | Replay slower | 1 | Replays something already clear | 0 |
| word-emphasis | Word emphasis (POP) | Key word circled or colored as spoken | The beat's one key word, marked in the script | Point attention at one word | 1 per beat | More than one key word per beat; emphasis on a filler word; same word in the caption at that moment | B (signaling) |

## 9. Calls to action

Stage-aware: script-genome uses only the asks in the growth plan's `cta_allowed_now` (`00 Decisions/growth-plan.md`, `## Growth state`, written by growth-genome); with no growth plan, payoff endings and a situational send line only. **Mechanics** = script-genome `catalog/endings.md`, anchor = slug.

| Slug | CTA | Where | Family/type | Scale | Mechanics |
|---|---|---|---|---|---|
| tease-next | Tease the next video | End; shown, not said | next-video | both | `endings.md#tease-next` |
| loop | Loop to the start | End flows into the hook (vertical) | loop | short | `endings.md#loop` |
| comment | Comment prompt | A real question they want to answer | engagement · comments | both | `endings.md#comment` |
| part-two | Follow for part 2 | Series | series · follows | short | `endings.md#part-two` |
| save-share | Save / share prompt | "Send this to the person who…" | engagement · sends, saves | both | `endings.md#save-share` |
| lead | Link in bio / lead offer | Business funnel; one per video | lead · clicks | both | `endings.md#lead` |
| watch-next | Watch this next | End screen points to one video | next-video | long | `endings.md#watch-next` |
| mid-value | Mid-video value CTA | Right after a payoff | placement · mid-video | both | `endings.md#mid-value` |
| hard | Hard ask | Direct "follow"; rare | follows | both | `endings.md#hard` |

## 10. Feeling targets

One per video, chosen in the Idea Record. It must serve the brand's lead personality pick, never replace it.

Share evidence (Berger & Milkman, news articles: text, not video): awe, anger, anxiety, surprise, interest and practical usefulness went with more sharing; sadness with less. None of it is tested on short video.

| Feeling | What produces it (hook mechanisms, arcs) | Edit cues | Share evidence note | Fails when |
|---|---|---|---|---|
| curiosity | curiosity-gap, question, secret hooks; mystery-box, investigation, kishotenketsu-twist | Hold the reveal frame back; CARD-L names the gap; SIL before the answer | Interest: more sharing | The gap is vague, or never paid off |
| surprise | bold-claim, contrarian, interrupt hooks; reversal, kishotenketsu-twist, discovery | SMASH or INT on the pivot line; HIT | Surprise: more sharing; it resets attention only briefly | No payoff; a trick edit that wears off with repeats |
| laughter | interrupt, pov-setup hooks; escalation-to-absurdity, rule-of-three-with-break, escalation | Hold before the button; SMASH; deadpan hold at the end | Not in that list; high-arousal positive, untested | The joke carries no point; the button gets explained |
| relief | warning, stakes hooks; man-in-hole, fail-fail-win, problem-solution-twist | Tension beats CUT-M, release beat CUT-S + music lift | Not measured; low arousal | The problem was never felt, so the fix means nothing |
| awe | visual-prop, result-first hooks; escalation, transformation-montage, rags-riches | Long hold on scale, PUSH, RISE; few words | Awe: more sharing | Scale not visible at phone size |
| outrage-at-a-wrong | warning, contrarian hooks; riches-rags, cautionary-tale, myth-vs-truth | WARN text; CARD-N on the cost; no jokes | Anger: more sharing; truth rules first | Target unfair or unverifiable; anger with no action |
| nostalgia | visual-prop hook; origin-story, full-circle | Old footage or the accent grade on the past beat; soft music | Least evidenced for sharing | The viewer doesn't share that past |
| relatable | callout, pov-setup hooks; man-in-hole, fail-fail-win, mentor-wish-i-knew | Face, natural light, few effects; JUMP | Not measured directly | Too specific to the creator to feel "me too" |
| inspiration | result-first, number hooks; rags-riches, cinderella, underdog | Music rise into the result; CARD-N | Not measured directly; tie it to practical use (more sharing) | No setback (reads as a brag); numbers unverifiable |
| fomo | stakes, number, secret hooks; discovery, countdown-to-reveal, ticking-clock | TICK; STEP countdown; date or limit on screen | Anxiety: more sharing; the limit must be real | Fake urgency or invented limits |

## 11. Platform mechanics (vertical)

| Slug | Mechanic | Note | Script consequence |
|---|---|---|---|
| seamless-loop | Seamless loop | Last frame matches the first | Last line completes the first line (split sentence) or echoes it; the first line still works alone; no breath, sign-off or mid-line caption at the join |
| numbered-parts | Numbered parts | "Part 3" series | "Part N" in the hook text; ≤2 s recap line; end on the next part's question; only if that part will be made |
| stitch-bait | Stitch / duet bait | Invite others to respond | End on an open claim or fill-in line others can answer; hold 1–2 s as the response point |
| reply-video | Reply-to-comment video | Video answers a comment on screen | The comment on screen is the hook text; the first spoken line answers it; no backstory |
| trending-sound | Trending sound | Researched live at plan time, never stored; check rights per platform | Beats timed to the sound's drops; lines sit in its gaps; the meaning survives without the sound |
| trend-template | Trend template | Current meme format, researched live | Lines fill the template's beats; the brand's point goes in the twist slot |
| pinned-comment | Pinned comment | Context or link pinned under the video | Anything cut from the script (source, caveat, link) moves here; screen text may say "source pinned" |

## 12. Named editing styles (reference only)

Shown to the creator as reference points when describing a feel ("faster, like X"). Never applied as a preset and never copied; the brand's look and motion always win. Hormozi (word-by-word captions, cuts every 1–3 s, punch-ins) · Ali Abdaal (clean, color pop on grey, handwritten captions) · MrBeast (huge stakes, constant re-hooks) · video essay / Johnny Harris (maps, archive, narration) · Casey Neistat vlog (handheld story, time-lapses) · Tom Noske Reels (cinematic B-roll intros, 3D-shadow captions).
