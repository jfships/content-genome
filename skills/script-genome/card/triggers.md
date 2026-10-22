# Script triggers → edit moves

Which line or beat calls which edit move, what job it does, how good the evidence is, and when it fails. Load when filling the `edit`, `overlay`, `cut_type` and `sound` fields of the script card. Codes are the brand-neutral vocabulary in `card/schema.md` §8 "Edit codes"; video-genome (if installed) + the brand dress them (look, motion, sound files).

Evidence grade in this file (from the script-edit research): **A** controlled study on the mechanism · **B** indirect theory or research · **C** craft/practitioner only · **0** nothing found. Every A/B is from other media (lessons, TV, ads, film); none is from Reels.

## 1. Technique × trigger × job × evidence × fails when

| Technique (code) | Script trigger | Job | Ev. | Fails when |
|---|---|---|---|---|
| Jump cut (`JUMP`) | any pause, filler, restart or trailing breath inside a beat; always on | compress time, remove dead air | C | every sentence cut at the same frame size; breaths all removed so it sounds panicked |
| Hard cut on new idea (`CUT-S/M/F`) | line starts with "So", "Now", "But", "Step 2", a number, or a question | mark the segment boundary | A/B | cut lands mid-clause |
| J-cut (`J`) | next beat opens on a payoff, question or surprising number; face → demo jumps | prime the next shot; smooth the jump | C | overlap so long voice and picture contradict; used on every cut |
| L-cut (`L`) | beat ends on a claim that needs proof, or a reaction/proof shot while the sentence finishes | proof under voice; keep the thought alive | C | picture goes to something unrelated to the words still playing |
| Smash cut (`SMASH`) | hard contrast: "You'd think it works. [cut] It doesn't."; script marks `[cut to opposite]` | surprise, reversal | 0 (B: orienting response) | used as a joke with no teaching point |
| Match cut (`MATCH`) | last line echoes the first, or last frame matches the first (loops, callbacks) | closure, replay pull | 0 (B: match cuts least noticed) | loop makes the ending abrupt before the point lands |
| Punch-in (`PUNCH`) | key word, number, opinion line; "here", "this"; the sentence's last stressed word | emphasis: which line mattered | C (B: change on an attention cue is least intrusive; signaling) | >3–5 per 30 s; on every sentence; no key word; hides context on a screen recording |
| Slow push (`PUSH`) | a beat that builds: the turn, a reveal approaching, a demo the viewer must watch | sustained attention over a beat | C | on every beat (stops meaning anything) |
| Speed ramp (`RAMP`) | a step that is slow in real life (resting, drying, baking) or a jump between demo steps | time compression with a sense of progress | 0 | hides the one step the viewer must see; used on a talking face |
| Cutaway / b-roll (`CUTAWAY`) | line names a showable thing ("a crowded pan", "the hollow wall") | concrete picture for a noun | A (multimedia, temporal contiguity) | shown after the word; decorative; unrelated stock |
| Screen insert (`SCREEN`) | procedural line ("click", "type", "set") or "watch this" | proof and procedure | B (signaling, cueing) | text unreadable on a phone; voice and cursor out of sync; no highlight |
| Picture-in-picture (`PIP`) | creator's opinion or reaction matters while the screen/object is the subject | trust and presence | B (face mainly a trust device) | covers the UI/object; sits in the right rail or bottom zone |
| Split screen (`SPLIT`) | before/after, A vs B, two products | direct comparison in one frame | B (spatial contiguity) | both halves change at once; text unreadable at half width |
| Same-frame wipe (`WIPE`) | "before → after" on the same framing | the arc is the edit: change is visible | C | framing differs between halves |
| Freeze (`FREEZE`) | "this one number / this setting / this moment" | hold a still for reading | 0 | nothing to read on the frozen frame |
| Rewind / replay | "wait, watch that again", a missed detail | redo at slower speed | 0 | replays something already clear |
| Word emphasis (POP color/size) | the row's `key_word` | direct attention to one word | B (signaling) | more than one key word per row; emphasis on a filler word |
| Captions, chunked (`CAPTION full`) | default for all speech | muted viewing, comprehension, accessibility | A/B (most for non-native) | over-reading during the demo moment; sits in an unsafe zone |
| Captions, word-by-word / karaoke | fast-delivery beats only | rhythm | 0 (vendor claims) | slow delivery; long Reels |
| Text pop (`POP`) | key term, number or label spoken in the line | label, structure, step number | B (key terms beat verbatim; contiguity) | pops before/after the word; sentence-length text; competes with the demo |
| Big number (`CARD-N`) | a result or number the Reel turns on | make the number readable | B (signaling) | number not spoken too (say it simply AND show it) |
| One-line card (`CARD-L`) | a rule or a label that needs a full short line | name the rule | B | it duplicates the spoken sentence (redundancy) |
| Warning style (`WARN`) | a mistake, risk or "don't" | flag danger | C | used for mild preferences (cries wolf) |
| Step label (`STEP`) | "one", "two", "step 3", timer | orientation, progress | 0 (Instagram has a native bar) | competes with the native bar's screen area |
| Sticker / emoji | emotion or yes/no verdict; ≤1 per 10 s | quick emotion read | 0 (B: seductive details hurt recall) | decorates without meaning; covers the object |
| Highlight / circle / dim-the-rest | pointing words: "this", "here", "right there" | direct the eye to one element | B (relation-showing cues beat plain highlights) | highlight shown while the line talks about something else |
| SFX (`SFX`) | information events only: something slides in, a number appears, a cut to full-screen proof | mark "something changed here" | B (sync window) / C | under the key claim; on every line; louder than voice |
| Music bed (`MUS-LOW`) | tone under hook and ending; low under explain | mood | B (engagement up; verbal recall down when it competes with narration) | competes with narration; lyrics; same loudness as voice |
| Music hit / drop (`BEAT`, `DROP`, `HIT`) | payoff line or reveal, once | punctuation | 0 | forces cuts mid-clause |
| Riser (`RISE`) | the second before a reveal | anticipation | 0 | no reveal follows |
| Clock (`TICK`) | ticking-clock arcs, timed steps | visible/audible pressure | 0 | no real time limit |
| Silence (`SIL`) | after a claim; before the payoff; max one held pause per Reel | weight, lets it land | C (B: segmenting) | silence that is just a gap |
| Pattern interrupt (`INT`) | the turn: valley to climb, expectation flip | reset attention with new information | B (orienting response) | two in a row; decoration with no new info |

Zoom, ramp, freeze, rewind, smash, stickers, progress bars: no controlled evidence for teaching. Treat as style, tie each to a trigger, cap them (R4).

## 2. Mayer principles → script rule + edit rule

Effect sizes are medians from lesson research (other medium), quoted to rank, not to promise.

| Principle | Evidence | Script rule | Edit rule |
|---|---|---|---|
| Multimedia (words + pictures) | strong, d ≈ 1.35 | every teaching claim gets a visual line | no face-only teaching beat when the claim can be shown |
| Temporal contiguity | strong, d ≈ 1.31 | line and its picture start together; write the trigger word | visual on the word that names it, or ≤0.2 s before; POP on the spoken word |
| Spatial contiguity | strong, d ≈ 0.82 | label sits next to what it labels | overlay near the thing, inside the safe box, not in a corner |
| Coherence | strong, d ≈ 0.86–0.97 | cut tangents, jokes and asides that don't carry the point | no decorative b-roll, no music under the key claim, no sticker without a job |
| Signaling | moderate–strong, d ≈ 0.38–0.70 | name the key word; verbal signposts ("this", "here", "step 2") | highlight/circle/zoom the exact element; one highlight style per Reel |
| Redundancy | strong in lab, boundary-sensitive, d ≈ 0.72 | no on-screen text that duplicates the line | overlay = 1–4 key words; captions separate and chunked (schema §5) |
| Segmenting | moderate, d ≈ 0.67 | one idea per beat; 3–6 beats per Reel by runtime | cut or visual reset at every idea boundary; 0.3–0.5 s hold before a new idea |
| Modality | strong, d ≈ 1.02 | the voice carries the explanation | the screen carries the object; printed words OK for technical terms and numbers |
| Pre-training | listed, no numbers read | define the one new term first | show the term/tool name as an overlay at first mention |
| Personalization | listed | talk like a person: "you", contractions | no robotic synthetic voice as the main voice |
| Image (speaker on screen) | weak for learning; mainly trust | face in hook, opinion and trust beats | face for opinion/emotion, screen or object for procedure |

## 3. Beat rhythm defaults (craft starting points; check on the creator's chart)

| Item | Default | Basis |
|---|---|---|
| Planning pace | 2.4 w/s overall (creator's measured pace overrides) | `card/schema.md` §8; research range 2.2–2.7 incl. demo beats |
| Talking beats | ~2.5–2.8 w/s (150–170 wpm) | template default 130 wpm; faster speakers held MOOC viewers longer (correlational) |
| Demo beats | ~1.5–2.2 w/s (90–130 wpm) | viewers need reading time |
| Words per 30 s | 65–80 spoken, keeping ≥3 s of non-speech | arithmetic |
| Beat length | hook row 2–4 s; beats ≥5 s and ≥12 words; explain/demo 5–8 s | `card/schema.md` §8; Boords, CapCut |
| Beats per runtime | 15–30 s: 3–4 · 31–45 s: 4–5 · 46–60 s: 5–6 (7 for ladders/lists) | arc research (inference) |
| Idea per beat | exactly 1 | segmenting |
| Visual change | something new on screen every ~2–5 s; a related cut, PUNCH or POP counts | craft; novelty over cut speed |
| Unrelated cuts | ≤6–8 per 30 s | ad research threshold ~10, with margin (inference) |
| Cut alignment | on, or ≤0.2 s before, the first word of the new idea; trim ~0.2 s into the previous line's tail | attentional cut theory; craft |
| Mid-sentence cuts | only PUNCH on the key word, or L to proof while the sentence finishes | craft |
| Pause after a claim | 0.3–0.5 s voice silence, picture holds | craft; size is inference |
| Breath | keep one short natural breath per beat (<0.2 s); remove loud inhales | craft |
| Text hold | 0.8–1.5 s for 1–4 words; a number 1.5 s | reading ~4 words/s + lag (inference) |
| Re-hook | a new reason to keep watching every ~8–12 s; ≥1 at 40–70% for ≥30 s | inference from long-form (retention §2) |
| Sentence rhythm | alternate a short claim (≤6 words) with a longer explanation (10–16); never three long lines in a row | inference |

Pace conflict, settled: the script budgets spoken words at the planning pace (2.4 w/s); video-genome measures 2.6–3.0 w/s after the edit trims gaps. Both are true of the same Reel.

## 4. Sound timing rules

1. Voice is the main channel for the explanation; everything else ducks under the key claim.
2. SFX fires on the information event (a new thing appears), 0 to +100 ms after the visual. A sound slightly after the cut feels less wrong than one before it. Lab sync windows: roughly −80 ms (audio early) to +190 ms (audio late) go unnoticed.
3. Music: low under explain beats; allowed louder in the hook (0–2 s) and under the button/ask; never under the one sentence the Reel exists to teach.
4. Silence: 0.3–0.5 s after a claim; one held `SIL` (up to 1.0 s) per Reel. A hard cut from quiet to loud is a deliberate tool, not a default.
5. Audio across the cut: `J`/`L` offsets 0.2–0.5 s on a talking head; up to ~2 s only for a big shift.
6. Voice-over-screen Reels: record the VO after the cut so narration matches the picture.
7. Sound sits in its own card field: a sound-only fix is remix + remux, no redraw (R6).
8. Loops: continuous room tone or music across the join; no tail silence.

## 5. Pacing patterns → 30 s timelines

video-genome pacing slugs (`plan/story-libraries.md` §7, if video-genome is installed; otherwise this table is the full slug list for the card's `pacing` field), mapped to a 30 s Reel. Scale times proportionally (×2 for 60 s). "Ev." = support for teaching.

| Slug | 30 s timeline | Script needs | Edit per beat | Ev. / risk |
|---|---|---|---|---|
| front-loaded | 0–8 s ≈ half the value (claim + proof); 8–30 s remaining steps + ending | result first, then how | 2–3 visual changes in 0–8 s, then settle (CUT-F → CUT-S) | B (value early) |
| calm-bursts | calm 0–4, burst 4–7, calm 7–14, burst 14–17, calm 17–25, burst 25–30 | calm = explain (≤2.3 w/s, one hold); burst = payoff line, 3–5 words | effects (PUNCH, POP, SFX) only on bursts; calm rows none | B (segmenting, coherence) |
| return-hook | 0–3 hook opens a loop; middle answers parts; 21–27 s returns to the hook visual/words with the payoff | hook line and payoff line share words; keep the open loop as a card field | same framing and overlay at the payoff; optional MATCH | C |
| fast-talk-slow-show | talking rows ~3.0 w/s after edit; demo rows 1.5–2.0 w/s with little VO | claim fast, then show with few words | face = JUMP; demo = one PUSH + one highlight + one SFX | B (speaking-rate, reading time, signaling) |
| cut-on-emotion | one cut per emotional/thought shift (~4–6 per 30 s), on the stressed word or clause end | mark the opinion/emotion lines | cut or PUNCH on the opinion; hold on face for the feeling | C |
| cut-to-beat | 100–130 bpm; cut/overlay every 4th or 8th beat ≈ 2–4 s | music chosen before writing; lines fit the beat grid | cuts on the grid (`BEAT`) | 0; conflicts with "cut on new idea" and with music under narration. Use for montage/result rows, not explain rows |
| relentless | visual change every 1.3–2 s, start to end | 3–5 word sentences | PUNCH/POP/CUT-F on every phrase | C/V only; against fast-edit memory research and the long-form slowdown. Use for the first 3–5 s only, then ease |
| one-take | no cuts; intent carried by 2–3 PUNCH presets on key words, POP, caption emphasis, SFX | write 2–3 "edit hooks" (key words) into the lines | PUNCH 105–115% at the key word and back; POP; SFX | C (zoom on a speech cue feels natural; informal direct-to-camera held MOOC viewers) |

## 6. Safe zone

Do not hard-code a box here. Use the brand's safe box, or video-genome's (`shorts/build.md`, if installed; otherwise no fixed box: follow the rule below and the phone preview), for every overlay, caption and PIP; keep text out of the right-rail buttons, the top bar and the bottom caption/handle rows. Secondary sources disagree on exact pixels. Preview the draft on a real phone in the Instagram app before calling it done.
