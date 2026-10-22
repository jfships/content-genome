# Script card schema

The script card is the contract between script-genome and the skills that read it (video-genome plan/build, the brand's dressing). One header block + one row per beat (a beat may split into rows at a visual change). Audio is written first; the visual side may not repeat what the line already says.

Format basis: two-column A/V script, one row = one synchronized moment, runtime and word count per row (Celtx, StudioBinder, Boords agree). Fields: `pass2` script-edit research §8 + beat-sheet header from arc research §4.4. Edit moves use the brand-neutral codes in §8 "Edit codes" (video-genome + the brand dress them). Lint: `card/lint.md`. Trigger rules: `card/triggers.md`.

## 1. Header block

```
card: <slug-of-idea> | schema: 1 | runtime: <s> | words: <n> (budget <n> @ <pace> w/s) | beats: <n>
shape: <shape slug> | arc: <arc slug|none> | operator: <slug|none> | line-rule: but-therefore|ABT|none
pacing: <pacing slug: `card/triggers.md` §5> | idea-type: demo|tip|opinion|story|comparison|news|list | feeling: <slug>
hook: <hook slug> | spoken: "<≤8 words>" | text: "<3–7 words>" | image: "<what frame 1 shows>"
ending: <ending slug> | ask: <slug|none> | ask_place: mid-peak|after-payoff|caption|none | peak-in-last-third: yes|no
stage read: <stage|unknown> | asks open: <slugs> | source: strategy block|default (no strategy block)
captions: full|emphasis|off (default full, chunk 3–4 words) | pop style: brand
cover: <frame: time or row id> | line: "<cover text>"
sources: <S1: claim → source pointer> …  (every number/claim in the script; empty only if the script has none)
lint: <K-ids passed / WARN list / FAIL list>
```

Field notes:
- `runtime` target in seconds. `words` = spoken words only; budget = (runtime − planned silent s) × this video's pace; header `pace: <w/s> · <mode> · <source: take | log | default>` (`write/budget.md`).
- `shape / arc / operator / line-rule`: the stack the selector picked. An arc can take one ORDER operator (in-medias-res, full-circle, reversal) and one line rule.
- `hook` has three layers carrying the same idea; no layer ranked first. Screen text is `own words` or `mirror` (the spoken line word for word, captions hidden for that line), picked per video (`catalog/hooks.md`); write which in the header (`text_mode`); `image` must make sense with sound off. `text` (hook screen text) is 3–7 words; in-body POP overlays are 1–4 words. No word of `text` sits in the caption chunk on screen at the same time (K6).
- `cover`: the frame used as the cover (a time or row id) and the cover line, in its own words.
- `stage read`: copied from the strategy block, or `default` (endings §4).
- `sources`: pointers, not prose. A claim with no pointer fails lint K15.

## 2. Beat row fields

| Field | Content | Rule |
|---|---|---|
| id | B1…Bn; sub-rows B1.1, B1.2 when one beat holds two visual moments | lint counts beats, not rows |
| t + % | start–end seconds and % of runtime | contiguous; last row ends at runtime |
| role | hook · context · claim · step · proof · turn · payoff · rehook · ending · ask | hook only inside B1 |
| speaker | main · second | a second voice gets its own caption style (per brand) |
| src | take · memo · chat · new | `take`/`memo` (performed) are the wording source; `chat` lines get said aloud by the creator before they're kept; `new` = Claude's line (`write/passes.md`) |
| line | exact spoken words; notation: `/` micro-beat, `//` pause before payoff, one CAPS stress word max | ≤ budget for the row |
| words | spoken word count | vs seconds: 2.2–3.0 w/s; flag >3.3 |
| purpose | one verb phrase ("show the crowded pan") | one idea per beat |
| key_word | the single word the edit stresses; must appear in `line` | one per row |
| info_new | what is new in this beat (fact, picture, turn) | never empty |
| overlay | POP: 1–4 key words, or `none` | never the sentence; never ≡ line |
| overlay_on | @key_word, @event or @cut | fires on the spoken word |
| visual | face · screen · broll · graphic · split · pip; what exactly | a named thing is shown when named; a new visual at least every ~6 s (a related cut, POP, CUTAWAY, SCREEN, PUNCH counts; face-only does not) (K16) |
| edit | moves with triggers: `CODE @trigger [offset_ms] [amount]` | every move has a trigger |
| cut_type | related · unrelated · none (entering this row) | unrelated ≤6–8 per 30 s |
| sound | `CODE @trigger [offset] [level]` or `none` | own field (sound-only fix = remix + remux) |
| caption | full · emphasis · off; chunk rule §5 | no word in both caption and POP at once |
| rehook | `no` or the new reason to keep watching | ≥1 between 40–70% at ≥30 s |

Optional per-row fields: `V` (felt state −2…+2, for arcs), `in` (connective that opens the beat: but / so / because / until), `layout` (video-genome layout name), `safe_ok` (overlay inside the brand's safe box).

## 3. Two notations

### 3.1 Compact one-line (for chat, logs, and quick edits)
```
<id> | <t>s <pct>% | SPK <main|second> | SRC <take|memo|chat|new> | "<line>" (<words>w) | KEY=<word> | POP "<1–4 words>" @<word> | VIS <visual> | EDIT <CODE @trigger; …> | CUT <rel|unrel|none> | SND <CODE @trigger|none> | CAP <full|emphasis|off> | RH <no|reason>
```
Example:
`B2 | 8.0–13.0s 27–43% | SPK main | SRC memo | "So cook it in two batches. One layer, high heat, hands off." (12w) | KEY=batches | POP "ONE LAYER" @layer; "HIGH HEAT" @heat; "HANDS OFF" @off | VIS face | EDIT CUT-M @So; PUNCH @batches | CUT unrel | SND SFX tick @each-pop +0–80ms | CAP full (hide chunks under pops) | RH no`

### 3.2 Table (for review and handoff to video-genome)
Columns in this order: id · t · % · role · speaker · src · line · words · key_word · info_new · overlay (@trigger) · visual · edit (@triggers) · cut · sound · caption · rehook. Audio-side columns left, visual-side right. Worked example in §4.

## 4. Worked example (30 s, home cooking; made-up example, numbers are illustrative)

Topic: "Your stir-fry steams instead of searing." Shape before-after: the after first (hook), then the before, the bridge, the after in the same frame.

```
card: stir-fry-sear | schema: 1 | runtime: 30 | words: 67 (budget 72 @ 2.4 w/s, −7% ok) | beats: 4
shape: before-after | arc: none | operator: none | line-rule: but-therefore
pacing: front-loaded | idea-type: tip | feeling: relief
hook: result-first | spoken: "Same pan, same veg, cooked half at a time." | text: "BROWN, NOT SOGGY" | image: close-up of browned, crisp pieces lifting off the pan
ending: visual-loop (last frame = frame 1) | ask: none (send-line optional, see note) | ask_place: none | peak-in-last-third: yes
stage read: unknown | asks open: payoff-stop, button, deadpan-hold, callback, verbal-loop, visual-loop, send-line (optional) | source: default (no strategy block)
captions: full, 3–4 word chunks | pop style: brand
cover: B1 at 1.0 s (browned close-up) | line: "The soggy stir-fry fix"
sources: S1 "ninety seconds" → creator's own test (made-up here)
lint: K1–K16 pass
```

| id | t (s) | % | role | speaker | src | line | w | key_word | info_new | overlay (@trigger) | visual | edit (@triggers) | cut | sound | caption | rehook |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B1 | 0.0–3.0 | 0–10 | hook | main | new | "Same pan, same veg, cooked half at a time." | 8 | half | the after, shown first | hook text "BROWN, NOT SOGGY" on frame 1 | close-up: browned, crisp pieces lifting off the pan | PUSH 5% @Same | none | room sizzle; no music (voice first) | full: "Same pan, same veg," / "cooked half at a time." (no word shared with the hook text) | open loop: how |
| B2 | 3.0–9.0 | 10–30 | context | main | memo | "Last week, all in at once. The pan went cold and the veg just sweated." | 15 | cold | the before: crowding kills the heat | POP "COLD PAN" @cold | overhead, same angle as frame 1: crowded pan, steam, pale wet veg | SMASH @Last; L 0.3 s on steam after "sweated" | unrel | MUS-LOW @Last; weak sizzle up; SFX tick @pop +0–80 ms | full; hide the chunk "the pan went cold" while the POP is up | no |
| B3.1 | 9.0–15.0 | 30–50 | step | main | memo | "So, two batches. One layer, high heat, then hands off for ninety seconds." | 13 | batches | the change as a three-part rule | POP "ONE LAYER" @layer · "HIGH HEAT" @heat · CARD-N "90 SEC" @ninety (hold 1.5 s) | overhead: half the veg in one layer, timer in frame | CUT-M @So; PUNCH @batches | unrel | SFX tick @each-pop +0–80 ms, light; MUS-LOW | full; chunks under pops hidden | no |
| B3.2 | 15.0–24.0 | 50–80 | proof + rehook | main | memo | "Don't stir. Listen for the sizzle when I lift it. That sound means the pan stayed hot." | 17 | sizzle | proof you can hear; a reason to stay (the lift) | none | close on the pan; the lift @lift; face @That | PUSH 8% @Listen; hold 0.5 s on the lift; related cut to face @That | related | natural sizzle up @lift; DROP @That (no music under the key sentence) | emphasis (keep the pan clear) | yes: "listen for the sizzle when I lift it" |
| B4 | 24.0–30.0 | 80–100 | payoff + ending | main | memo | "Same pan, and now every piece browns. Tonight: cook half, then the other half." | 14 | browns | the after in the same frame + the first step | POP "HALF, THEN HALF" @other | same frame: crowded pale → browned; ends on frame 1's close-up | WIPE @Same (hold ≥1.5 s on the after); PUNCH @browns (≤108%); MATCH @end → frame 1 | related | SFX @wipe; MUS-LOW lifts under the last line only; room tone continuous @join | full; hide the chunk "then the other half" while the POP is up | loops to "Same pan, same veg…" |

Checks on the example: beat order matches the before-after shape (after → before → bridge → after + first step); 4 beats (15–30 s: 3–4 ✓); B1 is the hook beat (3 s, 8 words), B2–B4 each ≥5 s and ≥12 words; 67 words vs 72 budget (within +10%); hook text is 3 words in its own words, sharing no word with the spoken hook or the caption on screen; POPs 1–3 words, each with its caption chunk hidden; unrelated cuts 2 (≤6–8 ✓); PUNCH 2 (≤3–5 ✓); SFX 5, each on an information event; longest stretch without a new visual ~3.5 s (K16 ✓); re-hook at 50% ✓; peak (the same-frame reveal) in the last third ✓; no ask (default stage). Optional send line if one fits: "Your friend who keeps buying a bigger pan needs this." (would go after the last line and break the visual loop: choose one).

## 5. Captions + POP rule

Captions on by default (muted viewers, non-native viewers, accessibility). POP overlays carry 1–4 key words on top. They work together:

1. **Captions:** chunked 3–4 words, timed to speech, one line (two at most), inside the brand's caption box. No full-sentence blocks.
2. **POP:** 1–4 key words, fires on the spoken word (`@word`), holds 0.8–1.5 s (a number 1.5 s).
3. **No overlap:** the same word never appears in the caption chunk and the POP (or the hook screen text) at the same moment. When a POP fires, the caption either hides that chunk entirely, or shows only the rest of the chunk (the words not in the POP). Write which one in the `caption` cell.
4. **No sentence as big text:** a full spoken sentence never becomes a POP, CARD-L or big text. If a sentence must be on screen, it lives in the caption only.
5. **Demo moments:** keep the key on-screen detail free of text (caption `emphasis` or moved); viewers who read more understand the demo less.
6. **Caption speed:** chunk shown <1 s must stay under ~17 characters per second.

Why (graded): Mayer redundancy, spoken text plus identical on-screen text lowers learning (d ≈ 0.72, lab; boundary-sensitive) RESEARCH. Yue, Bjork & Bjork 2013: verbatim text hurt recall, abridged key-term text helped; viewers preferred the worse verbatim version RESEARCH (other medium). Fenesi & Kim 2014: verbatim text with narration lowered applied comprehension while raising felt understanding RESEARCH (other medium). Key-term displays beat verbatim text (57-study meta-analysis) RESEARCH. Captions help comprehension, most for non-native listeners (100+ studies) RESEARCH. Word-by-word karaoke captions: untested.

## 6. Rules R1–R6 (enforced by lint)

- **R1 Redundancy / coherence.** `overlay` ≠ `line`; every edit move has a trigger; every effect serves an `info_new`. If not, delete it. (lint K5, K7, K9)
- **R2 Signaling / contiguity.** A visual that names a thing starts on, or up to 0.2 s before, its `key_word`; text pops on the spoken word. (triggers.md)
- **R3 Segmenting.** One idea per beat; the boundary is a cut (related or unrelated); add a 0.3–0.5 s hold at the boundary if the next idea is new. (lint K2)
- **R4 Budget.** Unrelated cuts ≤6–8 per 30 s; PUNCH ≤3–5 per 30 s; SFX ≤1 per information event; stickers ≤1 per 10 s. Scale linearly with runtime. (lint K8)
- **R5 Re-hook.** At least one `rehook` row between 40% and 70% of runtime for Reels ≥30 s. (lint K10)
- **R6 Sound isolation.** Sound lives in its own field so a sound-only fix changes one column (remix + remux, no redraw).
- **R7 Visual change.** No stretch over ~6 s without a new visual; a face-only run counts as no change. (lint K16)

## 7. What reads the card

| Reader | Reads | Ignores |
|---|---|---|
| video-genome gate 1 / variety rule | header lines 2–5 | rows |
| video-genome plan/build + brand dressing | rows: visual, edit, cut, sound, caption, overlay | arc mechanics |
| creator (recording) | line column, `//` pauses, CAPS stress | codes |
| learn log (post-publish) | row timestamps ↔ retention drops | — |

## 8. Edit codes

Brand-neutral vocabulary; video-genome (if installed) and the brand dress them (look, motion, sound files). Without video-genome, the codes are the edit brief as written.

- Cuts: `CUT-S` change every 3–4 s · `CUT-M` 2–3 s · `CUT-F` 1–2 s · `CUT-X` <1 s burst · `JUMP` remove pause, same angle · `J` voice leads picture 0.2–0.5 s · `L` picture holds after voice 0.3 s · `SMASH` hard contrast cut · `MATCH` shape/motion/frame match (loops).
- Camera: `PUSH` slow push 5–10% over a beat · `PUNCH` 105–115% on the key word · `CUTAWAY` b-roll of the named thing · `SCREEN` screen recording · `PIP` face in corner · `SPLIT` two things side by side · `FREEZE` · `RAMP` speed ramp · `WIPE` same-frame before/after.
- Text: `POP` 1–4 key words on the spoken word (in-body; hook screen text is 3–7 words, header `text`) · `CARD-L` one-line card · `CARD-N` big number/result, hold ≥1.5 s · `WARN` warning style · `STEP` step/timer label · `CAPTION full|emphasis|off`. A word shown in a POP or the hook screen text is never in the caption chunk on screen at the same moment.
- Sound: `MUS-LOW` bed ducked · `RISE` riser · `HIT` impact · `DROP` music cuts out · `SIL` 0.3–1.0 s silence (one held pause per Reel by default) · `TICK` clock · `BEAT` cut on music hit · `SFX` light click/ding on an information event, 0 to +100 ms after the visual.
- `INT` = the one pattern interrupt; place it at the turn (valley to climb, expectation flip). Not two in a row.
- Triggers are written `@word` (fires on that spoken word) or `@event` (on-screen event). Example: `POP "BEATS" @beats; PUNCH @beats; SFX @slide-in`.

Budgets (defaults, flagged craft):
- Planning pace 2.4 words/s (use the creator's measured pace if known): 20 s ≈ 48 · 30 s ≈ 72 · 45 s ≈ 108 · 60 s ≈ 144. After-edit spoken pace 2.6–3.0 w/s is video-genome's measure.
- Beat ≥ 5 s and ≥ 12 words, except the hook beat (≤8 spoken words carry the point in the first ~3 s). 15–30 s: 3–4 beats · 31–45 s: 4–5 · 46–60 s: 5–6 (7 for ladders/lists).
- Unrelated cuts ≤ 6–8 per 30 s; PUNCH ≤ 3–5 per 30 s; SFX only on information events; music never under the key sentence. A new visual at least every ~6 s (K16).
