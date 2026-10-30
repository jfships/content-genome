# Graphics library

Every move this skill knows, by family. The brand decides which are on-brand: use only options its packs kept (listed by name in the brand file), never anything on its No lists or house rules. Any option in that catalog can be built; see "Building catalog options" at the end. Before hand-building any move, search the HyperFrames registry (`npx hyperframes catalog --query "<move in plain English>"`) and reuse a component if one exists. Overlay moves on footage can use the bundled engine (`tools/talking-head/reference/looks.md`).

**Mechanics rule.** Every move here ships with its mechanics and a use-case: what it is · use when · **Trigger** (the kind of script line or beat that calls it; in a script card the move fires `@word` or `@event`) · **Hold** (typical time on screen) · fails when. No trigger in the script, no move. A new move is added only with all of these (see `plan/story-libraries.md`, rule for adding options), and with its neutral stock sample (`craft/stock.md`).

**Stock** = the move's id in the stock library (`craft/stock.md`); pick and show samples by it. "—" = no id yet. Only ids in the library's manifest have a built sample.

**Hold defaults.** Text: reading time ≈0.3 s per word + 0.5 s, never under 1.1 s; numbers ≥1.5 s. Set pieces 2–4 s. Wildcards ≤1–2 s. A word shown as a pop is never in the caption chunk on screen at the same moment.

**Fits** = the motion feels a move suits, matched to the brand's motion personality: **S** Snap · **G** Glide (also Editorial, Cinematic) · **D** Deadpan · **P** Punch (also Glitchy) · **Dr** Drift · **M** Mechanical · **all**. Playful and Handmade fit anything marked G or D, with their own springs or 12 fps stepping. These letters are internal; never show them to the creator.

**Look-real props (§15) are the device creators approve most:** reach for them first when a beat's job is the straight man, the unsaid line or proof.

## 1. Title styles

| Move | Stock | What it is | Use when | Trigger | Hold | Fits | Fails when |
|---|---|---|---|---|---|---|---|
| Stencil | — | Spray-stencil letters with slight overspray | Raw, handmade brands; chapter titles | A chapter or section-change line | Reading time | D, S | The brand is clean or premium; overspray hides letters at phone size |
| Label Maker | — | Embossed tape strip, letters punched in | Naming things, lists, deadpan labels | A line that names a thing or a list item | Reading time | D, M | The label repeats the spoken words with no twist; more than ~4 words on the tape |
| Sticky Note | — | Handwritten note slapped on the frame | To-dos, asides, plans | An aside, plan or "note to self" line | Reading time | D, G | The handwriting font is unreadable at 360 px; used for the main point instead of an aside |
| Hand Annotation | POP-03 | Marker circles, arrows and words drawn on | Pointing at something specific | Pointing words: "this", "here", "right there" | Draw-on ~0.5 s + reading time | all | Nothing specific to point at; the draw lands after the word |
| Highlighter | POP-04 | A marker stroke sweeps behind a key line | The one line to remember | The one line to remember (the beat's claim) | Reading time, ≥1.5 s | all | More than one line highlighted; the stroke covers the letters instead of sitting behind them |
| Outline + Fill | — | Outlined type that fills on the beat | Clean product brands; reveals | A reveal word; fill lands on the spoken word | Reading time | G, S | The fill lands off the word; thin outlines vanish on a busy background |
| Keynote Minimal | — | One big word, lots of space | Calm, premium statements | A one-word or short statement line | 1.1–2 s | G, Dr | The beat needs proof or a joke; on its own it reads as a plain card |
| Kinetic Bold | — | Heavy words moving on the beat | Hype openers, high energy | Hook line or a payoff on a music hit | Reading time per phrase | P, S | Calm or deadpan brand; words move faster than they can be read |
| Risograph | — | Grainy two-ink offset print type | Indie, editorial, playful | A title or section line | Reading time | G, D | Clean tech brand; grain muddies small text |
| Big Number | POP-06 | One huge number with a small label | Stats, prices, counts | A line that says a number the viewer must remember | ≥1.5 s | all | No label (the number means nothing alone); the number isn't real |
| Photo-Filled Type | — | Footage or a photo shows through the letters | Openers, place names | Opening line or a place name | 1.5–2.5 s | G, Dr | Thin letters or a busy photo make the word unreadable |
| Chat Thread | PROP-01 | Message bubbles appear in turn | Conversations, prompts, DMs | A line quoting a prompt, message or reply | Reading time per bubble | all | Bubbles look drawn, not like a real app (§15); more bubbles than the viewer can read |
| Terminal | — | Monospace text typing in a terminal | "Building", code, systems | "I built", "I ran", a command or system line | Type-on + reading time | D, M | The audience isn't technical; it becomes the generic dev look |
| Typewriter | POP-12 | Characters appear one by one, stepped | Deadpan reveals, notes | A deadpan reveal or a short note | Type-on + reading time | D, M | The line is long, so typing outlasts the beat |

## 2. Overlays and callouts

| Move | Stock | What it is | Use when | Trigger | Hold | Fits | Fails when |
|---|---|---|---|---|---|---|---|
| Word-by-word captions | — | Spoken words appear as said | Default captions for social | All speech (caption mode full) | Synced to speech | all | Words arrive ahead of or behind the voice; chunks fill the frame |
| One word at a time | CAP-03 | A single big word per spoken beat | Hooks, vertical | Fast hook lines, 3–5 words | One spoken word each | P, S | Used for a whole talking Short; fast speech flashes words too short to read |
| Clean subtitle | CAP-07 | Plain two-line captions | Calm, professional | All speech, calm delivery | Synced; chunks ≤17 characters/s | G, Dr | High-energy brand; two lines cover the face or the graphic |
| Highlight captions | CAP-02 | The spoken word turns the accent color | High energy, vertical | The beat's key word inside the caption | Synced to the word | P, S | The color change lags the voice; every word gets the accent |
| Lower third | — | Name, role or place in a bar | First appearance, guests, places | First time a person or place appears | ~2 s | all | Used on a Short (no name tags); repeats a name already known |
| Callout | POP-05 | A box with a line pointing at a detail | Explaining one part | A line about one part ("this setting controls…") | Reading time | all | The leader line points at the wrong part as it moves; several callouts at once |
| Checklist | POP-08 | Items tick off in turn | Steps, requirements, results | "Step 1/2/3", a list of requirements | Each tick on its spoken item; whole list ≥ reading time | all | Ticks land off the spoken item; more than ~5 items |
| Stat bubble | POP-10 | A small number badge pops near the subject | Supporting numbers | A supporting number said in passing | ≥1.5 s | S, P | It's the main number (use Big Number); the badge covers the subject |
| Spotlight | CAM-05 | The frame dims except one area | Focusing on a detail | "Look at this part", one detail | 1.5–3 s | G, D | The lit area is too small to read at phone size; nothing new is in it |
| Progress steps | — | A bar of steps showing where we are | Tutorials, multi-part videos | "Three steps" in the hook; "step 2" lines | Updates each step; stays while steps run | all | On a Short under ~45 s it's clutter; steps don't match the spoken count |
| App window | — | A clean window frame holding a screen | Showing tools | A line naming a tool or "watch this" over a screen | As long as the screen beat | G, M | The window is static for over ~2 s (add a move, §5 or §14) |
| Marker highlight | POP-04 | A hand-drawn stroke under or around words | Emphasis on a screen or page | The one phrase on a page or screen that matters | Draw-on + reading time | all | The marked phrase isn't the one being said |
| Hand-drawn arrow | POP-03 | An arrow draws itself to a target | Pointing, playful | Pointing words: "here", "this one" | Draw-on ~0.5 s + 1 s | D, G | Several arrows at once; the target moves away |

## 3. Placements (where the person sits)

Shorts use the named layouts in `shorts/build.md` "Layouts" (LAY ids, boxes); these are the long-form placements and the moves behind them.

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Full cutaway | LAY-05 | Graphics fill the frame; face leaves | A process, product, comparison, number. Not on personal lines | A line about a thing that can be shown fully | 3–10 s (Shorts: 1.1–4 s) | A personal or trust line loses the face; the graphic holds with nothing moving |
| Side panel | LAY-09 | A transparent graphic in empty space beside them | Footage with real empty space | A supporting point while the face keeps talking | Can run 15 s+ | No real empty space, so it overlaps the head; text too small to read |
| Speaker to side / corner | — | Their footage shrinks into a box while a graphic plays, then grows back | Personal and trust videos where the face should never leave. Beats over 4 s | A screen or proof beat in a personal video | >4 s | The beat is under ~4 s (the shrink and grow eat it) |
| Cutout beside graphics | — | Person cut out from the background, placed beside graphics | Graphics-first videos; polished explainers | Explainer beats where the person presents the graphic | Beat length | A rough cutout (hair and hand edges) at full size; the person and the graphic don't share a light |
| Corner bubble | LAY-08 | Small round or rounded face in a corner | Screen-heavy tutorials | Opinion or reaction while the screen is the subject | As long as the screen beat | The bubble covers the part being pointed at; the face is the point of the beat |
| Taking turns | — | Full face, then full graphic, alternating | Simple, fast to build | Claim line (face) then show line (graphic) | Beat length each | Every beat alternates the same way, so it reads as a slideshow |
| Voice only | — | No face; graphics carry it | Story beats, recaps, the creator off camera | Narration with nothing to gain from the face | Beat length | The opening of a Short (frame 1 needs the creator or their material) |
| Word pop | POP-01 | 1–4 of their words spring in over them | The line to remember | The beat's key word (POP @word) | Reading time; at most every ~15 s | The pop repeats the caption on screen; it covers the face through its pop-in |
| Text behind speaker | LAY-06 | A word pop passing behind their head | One standout moment, often the hook. Words stay ≥ 70% visible | The hook word or the one standout line | 1.5–2.5 s | A rough matte makes the head edge flicker; the head hides the key letters |

## 4. Footage treatments

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Background blur | CAM-08 | Shallow depth of field on the room | Messy rooms; default for home recordings | Always on for home footage | Whole shot | The matte edge shimmers around hair; the blur is so strong the room looks fake |
| Background dim | CAM-08 | Room darkened (optionally blurred) | Graphics and captions need to stand out | A beat with a graphic or text over the face | While the graphic shows | The face dims too; on and off every beat, so it flickers |
| Lights out | CAM-04 | The backdrop drops to near black; the speaker stays lit | The serious line, a turn, the moment before a reveal | The turn word or the serious line | The beat; back on the next | Used more than once or twice a video; the matte edge glows against the black |
| Background replace | BKD-01..07 | Room swapped for a brand color or image | Clean studio look; check hair and hands | Format choice, not a line | Whole shot | Hair and hand edges fail the matte; the new light doesn't match the face |
| Ease zoom | CAM-02 | Gentle push-in on a word (1.06–1.12) | Emphasis in calm videos; 4 s+ apart | A key word or the end of a thought (PUSH) | Over the beat; snap back at the next idea | Constant slow zoom on every shot (lazy breathing, `motion.md` §6) |
| Punch zoom | CAM-01 | Instant cut-in (1.15–1.25) | Emphasis in high-energy videos | Key word, number or opinion line (PUNCH); 3–5 per 30 s | Until the next sentence | On every line, so nothing stands out; a soft source goes blurry at the scale |
| Pack grade | — | The brand's base grade on all footage | Always | Always | Whole video | Skin tones shift; one clip graded differently from the next |
| Accent grade | — | The brand's accent grade on its trigger | Flashbacks, late nights, payoffs, as the brand says | The brand's named trigger (flashback line, payoff) | The triggered beat | Used without its trigger, so it reads as a mistake |
| Freeze frame | CAM-03 | Footage stops on a frame; graphics take over | Before a mark-up, a reveal or a joke | "Look at this", "wait", a moment to label | 1.5–3 s | The frozen frame catches a blink or open mouth; nothing is added to it |

## 5. Screen walkthroughs

Use whenever a screen is shown. Blur or crop private data first. Pause before a click so the viewer sees where the cursor lands; one callout per click.

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Cursor click | SCR-01 | An oversized cursor moves and clicks with a ripple | Showing where to click | "Click", "hit", "open" | ≥1 beat after the click | Cursor waves around; click out of sync with the word |
| Typing a prompt | SCR-02 | Text types into a field, character by character | Showing the exact input | A line quoting the prompt or "type this" | Type-on + reading time of the key part | Text too small at phone size; typed too fast to read |
| Scroll through | SCR-03 | A page scrolls with easing and pauses on the key part | Long pages, results lists | "Scroll down to…", "look further down" | Pause ≥ reading time on the key part | No pause; scrolls past the point |
| Camera push-in | SCR-04 | The camera pushes into the part of the screen that matters | Small UI details | Line names the detail; start ~0.2 s before the word | Over the beat; 8–15% push | Hides the context the viewer needs |
| Drag to select | — | A selection box drags over content | Choosing a range or items | "Select", "grab these" | ~1–1.5 s | Selection unrelated to the line |
| Notification pop | PROP-02 | A toast or banner slides in | Something arrives or finishes | "Then this comes in", "done" | Reading time | Covers the key UI |
| Hover tooltip | — | A tooltip appears on hover | Explaining a control | "What this button does" | Reading time | Tooltip text unreadable |
| Drag a slider | — | A slider moves and something responds | Showing a setting's effect | "Turn it up", "lower the…" | Until the response is visible, ~1.5–2 s | Response too small to see |
| Real screenshot in shape | SCR-05 | The real screen inside the morphing shape, a highlight ring on the key word | A real screen as proof inside a designed scene | "Here's the real one", proof lines | Reading time on the ringed word | Screenshot blurry or private data visible |
| Before / after toggle | SCR-06 | One switch flips the screen between two states | Same screen, two states | "Before … after", "with and without" | ~2 s on each state | Difference not visible at phone size |
| Side-by-side compare | SCR-07 | Two screens or results next to each other | Comparing tools or outputs | "This one vs this one" | ≥2 s; reading time per side | Text unreadable at half width |
| Chart with tooltip | — | A chart draws; a tooltip reads one value | One value in a trend | A line naming one number in a trend | ≥1.5 s on the value | Chart has no clear single point |
| Search / filter list | SCR-09 | A list filters as text is typed | Finding one item in many | "Search for", "filter by" | Until the result shows + 1 s | Typed term not readable |
| File drag and drop | — | A file drags into a drop zone | Uploading or importing | "Drop the file in", "upload" | ~1–1.5 s | File name unreadable |
| Live status island | SCR-08 | A small pill shows a live status changing | Waiting, running, done states | "It's running", "now it's done" | Each state ≥1 s | Status change not tied to the line |

## 6. Signature moments (set pieces)

Use 2–4 per long video, from the brand's kept list. Hold 2–4 s.

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Clone Grid | — | A grid of copies of the creator (or object), each doing a different role | Showing many jobs, versions or options at once | "I do five jobs", "every version of…" | 2–4 s | The copies don't differ enough to read at phone size; lighting differs between takes |
| Look Cascade | BIG-04 | The same shot flips through several looks in a fast cascade | Showing choices, styles, variations | "Same shot, ten styles", a list of options | 2–4 s | Looks too alike to tell apart; flips faster than ~0.2 s each |
| Progression Quad | BIG-02 | Four panels showing stages of progress side by side | Before → after, versions, growth | "From version 1 to 4", growth lines | 2–4 s | The panels are too small to see the change (tall frame: stack 2×2, not 4 across) |
| Freeze & Mark Up | BIG-01 | Footage freezes; hand annotations draw over it | Explaining what's happening in a frame | "Look at this part", "see what happened here" | 2–4 s | More than ~3 marks; the marks land after the words that name them |
| Slice Shift | TRN-05 | The frame splits into strips that slide to reveal the next scene | Chapter changes, reveals | A chapter change or "here's what it became" | 1–2 s | Used between related shots as decoration; used twice in a video |
| Contact Sheet Pick | BIG-03 | A contact sheet of frames; one gets circled and pulled out | Choosing the best of many | "Out of all of these, this one" | 2–4 s | The picked frame isn't visibly better than the rest |
| Word Burst | BIG-05 | One word explodes into many related words | Brainstorms, overwhelm, lists | A line about too many options or ideas | 2–3 s | The burst words are filler; the core word gets lost |
| Mirror Debate | LAY-11 | Split screen: the creator argues with themself | Pros and cons, doubts, two sides | "Part of me says … the other part says" | Beat length | Each side isn't clearly a different stance (wardrobe, framing); too much of the creator on screen |
| Sticker Bomb | POP-09 | Labels or stickers slap onto the frame in a burst, styled to the pack | Playful lists, reactions | A playful list or a verdict line | 1.5–3 s | Stickers cover the face or the proof; more than ~5 |

## 7. Wildcards (at most one per video, on the hook or a turning point)

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Crash Zoom | CAM-06 | A violent zoom into a face or object, with a whoosh | A shock or realization | The pivot word ("wrong", "wait") | ≤1 s | Nothing new follows it |
| Page Tear | TRN-10 | The frame tears like paper to reveal the next scene | A hard switch of scene or view | "But then", a reversal line | ≤1.5 s | Used as decoration between related shots |
| Pixel Collapse | TRN-13 | The image collapses into pixels and rebuilds | Something breaks or rebuilds | "It all broke", "rebuilt from scratch" | ≤1.5 s | The line isn't about breaking or rebuilding |
| Redacted | STO-05 | Black bars slam over words, then lift on the reveal | Hiding then revealing a word or number | A secret or "the one word they don't say" | Bars ≤1–2 s, then the reveal at reading time | Reveal never comes or is smaller than promised |
| Slot Machine | — | Reels spin and land on the answer | Picking one answer from many | "Which one won?", random pick | ≤2 s spin | Answer predictable |
| Thermal Flash | CAM-12 | 1–2 s of thermal-camera look on a pressure moment | Heat, pressure, stress moments | A line about pressure or panic | 1–2 s | No pressure in the line |
| Tape Rewind | — | The video rewinds with tape artifacts to replay a moment | Replaying a missed detail | "Wait, watch that again" | ≤1.5 s, then the replay | Replays something already clear |

## 8. Data and number moves

Real numbers only; illustrative ones are labeled as such in the plan.

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Counter roll | POP-07 | Digits roll up to the number | A total or result | A line that says the final number | Roll ≤1 s + ≥1.5 s on the number | Roll so long the number lands after the word |
| Number wheel | — | Digits spin on wheels and lock | A reveal number | A held-back number ("it came to…") | Spin ≤1 s + ≥1.5 s | Lock lands before the line names it |
| Bar race | — | Bars grow and reorder | Ranks changing over time | "Who's ahead", a ranking over time | 3–6 s | Too many bars to read on a phone |
| Stat stack | — | Numbers stack up one by one with labels | Several supporting numbers | A line listing 2–4 numbers | ≥1.5 s per number | More than 4 numbers |
| Progress ring | POP-11 | A ring fills to a percentage | One percentage | A line with a percent | Fill ≤1 s + ≥1.5 s | Percent without a label |
| Before / after split | — | A wipe divider shows two states | Two numbers or states compared | "From X to Y" | ≥2 s | Both sides unlabeled |
| Ticker | — | A strip of numbers or words scrolls past | Background sense of volume or news | A line about many items or live change | As background, beat length | Viewer is meant to read it |
| Timeline scrub | — | A playhead moves along a dated line | Events in time order | "In March … by June" | 2–4 s | Dates unreadable |

## 9. Map and place moves

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Route draw | MAP-01 | A line draws between places | A trip or path | "From A to B" | 2–4 s | Places unlabeled |
| Pin drop | MAP-02 | A pin lands with a small bounce-free settle | Naming one place | The place name | ~1.5 s | Map too zoomed out to read |
| Globe-to-street zoom | MAP-03 | The camera dives from a wide map to a place | Opening on a place | Opening line naming the place | 2–3 s | Used for a place the viewer doesn't need to locate |
| Location card | MAP-04 | A small card names the place and time | Setting the scene | First mention of where and when | Reading time | Repeats what the spoken line just said word for word |

## 10. Transitions

Shorts: which of these read in 9:16 and how long they may take, `shorts/build.md` "Transitions and camera in 9:16".

| Move | Stock | Trigger | Hold | Fits | Fails when |
|---|---|---|---|---|---|
| Hard cut on the beat | TRN-01 | A new idea starts ("So", "Now", "Step 2", a number), on or just before the first word | Instant | all | It lands mid-clause or after a tail of silence |
| Match cut | TRN-02 | Last line echoes the first, or two shots share shape or motion | Instant | all | The shapes or motion don't actually line up, so it reads as a jump |
| Object wipe | TRN-04 | A thing passes the lens as the topic changes | ~0.3–0.5 s | S, P, G | The topic doesn't change; the object has nothing to do with either scene |
| Color wipe (often reserved for the sting) | TRN-06 | The brand's sting or a section change | ~0.3–0.5 s | S, P | Used between beats of one idea; it competes with the sting |
| Soft rise | TRN-09 | A calm section change | ~0.5–0.8 s | G, Dr | High-energy brand or a Short's fast stretch: it stalls the pace |
| Split slide | TRN-07 | Moving from one item to the next in a list | ~0.4–0.6 s | G, M | Not a list; the items aren't parallel |
| Zoom through | SPA-07 | Going "into" a screen or idea ("let's look inside") | ~0.3–0.5 s | P, S | Speeds don't match between the two shots, so the cut jolts |
| Whip pan | TRN-03 | A fast jump in place or time ("meanwhile", "an hour later") | ~0.2–0.4 s | P | Used twice in a row; blur too weak to hide the cut |
| Dissolve | TRN-08 | Time passing, mood change | ~0.5–1 s | G, Dr | Used to hide bad timing; on a Short it eats half the shot |
| J-cut / L-cut | CUT-03, CUT-04 | Voice leads the next shot (payoff, question) or lingers over proof | Offset 0.2–0.5 s | all | The offset is so long the voice and picture seem out of sync |

## 11. Camera moves

For 3D camera work on screens, see §14. Shorts: punch-ins move inside the shot (`shorts/build.md` "Transitions and camera in 9:16").

| Move | Stock | Trigger | Hold | Fails when |
|---|---|---|---|---|
| Push-in to the storyteller | CAM-02 | An emotional or key line | Over the beat, 5–10% | It runs on every line, so it becomes breathing |
| Pull-out reveal | — | "Here's the whole thing", a scale reveal | 1.5–3 s | The wide view adds nothing the close one didn't show |
| Parallax layers | SPA-13 | A still that needs life on a narrated beat | Beat length | Only one or two layers, so it reads as a sliding card |
| Focus pull (rack focus) | SPA-14 | Attention moves from one thing to another in the line | ~1 s pull | The pull lands off the word that names the new thing |
| Pan across a page timed to the words | SCR-03 | The line reads or names parts of a page | Synced to the words | The pan runs ahead of or behind the words |
| Overhead (straight down) on hands or a desk | — | Hands-on steps ("first I lay out…") | Step length | The hands block what's being shown |

## 12. Textures and backgrounds

- **Textures:** film grain, vignette, paper, halftone, scanlines, light leak, dust (stock TEX-01..06). One base texture per pack; accents only on their triggers.
- **Backgrounds behind a cutout or a graphic** (stock BKD-01..07): solid brand color, moving gradient, blueprint grid, notes wall, moving type wall, real place blurred, footage behind, floating cards, studio sweep, a dark room with one light. The brand names one default per pack plus accents with triggers. Never the same flat background two scenes in a row.

## 13. Break-from-reality builds (cheap first)

- **Paper cutout animatic** (BIG-06): flat cutouts of the creator moving on a drawn set. Free, fast, on-brand. Trigger: a story beat with no footage.
- **Clone composite:** the same person filmed 2–6 times in different spots, combined with mattes. Trigger: "all the roles I play".
- **Miniature:** the creator shrunk inside a screen, a desk or a product (cutout + scale + shadow). Trigger: "inside the app", feeling small next to a task.
- **Narrator overlay** (BIG-07): a hushed documentary narrator over normal footage (generated voice described by delivery, never imitating a real person). Trigger: a mundane moment played as serious, for comedy. As a whole Short: `shorts/shapes.md` "Mock documentary".
- **Trailer card** (BIG-08): a mundane task cut like a movie trailer: title cards, booms, a release date. Trigger: a launch or a "coming soon" line.

Draft cheaply, mark "CUT CANDIDATE", give the full treatment only to the 1–2 kept. Hold: set-piece rule (2–4 s per moment).

## 14. Spatial moves (screens and ideas in 3D space)

Fly-throughs, screens floating in depth, exploded layers, orbit rings, tunnels, dolly zooms, rack focus, push into a card, 3D card flips, whip pans, 3D title openers and more, each with a working source, its stock id (SPA) and its tall-frame boxes: `craft/spatial/README.md`. The default family for screen demos and explainers, and the brand's fallback when a beat is hard to make entertaining. Trigger: a screen-demo or abstract-idea beat with nothing moving on screen for about two sentences. Hold: the beat (moves inside 1–3 s). Fits G, S, P (built with long-tail easing, never bounce).

## 15. Look-real props

The thing built to look like the real object, so the graphic plays the straight man: the line becomes a text from someone, a headline, a price tag. They work only when they look real: real typography, real details (masthead, timestamps, read receipts, the paper texture), the object's own sound. A flat card with the line typed on it is not one of these.

| Move | Stock | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|---|
| Text thread | PROP-01 | Message bubbles from a named contact, read receipts, the receive sound | A conversation, an excuse, someone's reply | A line quoting or imagining a message | Reading time per bubble | It looks drawn, not like a real app; more than ~3 bubbles on screen |
| Phone notification | PROP-02 | A banner drops in as if on the creator's phone | An interruption, a result arriving | "Then I get this", a ping, "it's done" | Reading time | The app name or styling is generic; it covers the face |
| Newspaper or classifieds | PROP-03 | A printed page with a masthead; the line is the headline or one ad | Stating something as news, a want ad for a job | A claim said as if it's public news | Reading time on the headline | The rest of the page is blank or lorem; the headline is too long for one glance |
| Receipt prints out | PROP-04 | A thermal receipt prints, itemizing the cost (money, time, sanity) | Adding up what something really costs | A list of costs, "and it cost me…" | Print ≤1.5 s + reading time on the total | More than ~4 lines; the total isn't the joke |
| Price tag / sold-out label | PROP-05 | Their real price or "out of stock", alone and readable | Proof that a price or stock state is real | A line naming a price or "sold out" | ≥1.5 s | The price isn't real; other text competes with it |
| Departures board | PROP-06 | Letters flip on a split-flap board, with the clatter | A status, a destination, a "now leaving" line | A short status line (≤3 words) | Flip ≤1 s + reading time | The line is longer than the board; the flip is silent |
| Report card / invoice / form | PROP-07 | An official-looking document filled in | Grading, billing or signing off on something | A verdict or a bill said out loud | Reading time | Too many fields to read; the filled field isn't the punchline |
| Rubber-stamp verdict | PROP-08 | A real ink stamp thuds down | A verdict: approved, denied, fired | The verdict word | Thud + ≥1 s | It's flat vector art, not ink (the flat version was killed) |
| Movie poster / trailer card | PROP-09 | A genre poster or "coming soon" card | Treating a mundane thing as an epic | A launch or "coming soon" line | Reading time | The genre isn't clear at a glance |

## Building catalog options (any option the brand kept)

The brand file names options by their name in this library. Build them with the cheapest technique that looks right, check the HyperFrames registry first, and draft any new technique on stills before animating.

| Technique | Builds | Notes |
|---|---|---|
| **Grade recipe on footage** | every film or color grade | `$SKILL/tools/grade.py` with the brand's recipe. Recipes it can't express use the next rows |
| **ffmpeg filters on footage** | VHS (chroma shift, scan lines), CRT (lenscorrection + overlay), security cam (pixelate, noise, timestamp via drawtext), night vision, thermal (`pseudocolor`), negative, solarize, tilt-shift, halftone-ish, datamosh-lite (minterpolate glitches) | Render the treated clip once, then use it as footage in the composition |
| **Canvas 2D in the composition** | duotone, tritone, posterize, 1-bit dither, pixel art, ASCII, mosaic, outline, halftone dots | Draw each frame of a still or short clip to a canvas and process pixels; pre-render to an image sequence if a scene needs many |
| **SVG filters** | paper and grain textures (`feTurbulence`), ink bleed, rough edges for stencil and riso, displacement wobble (boiling lines) | Cheap and crisp; one filter per scene, reused |
| **CSS / GSAP** | title styles, overlays, walkthroughs, interface styles, cards, tickers, counters, most transitions | Use `overflow:hidden` wrappers instead of clip-path for reveals (see `setup/gotchas.md`) |
| **Pre-rendered image sequences or video** | page tear, shatter, pixel collapse, slice shift with many strips, paper fold, film burn | Build once at full resolution (canvas or ffmpeg), then place as a clip. Avoids the clip-path limit |
| **Generated images** (image tool) | art styles and scene worlds (claymation, anime, watercolor, low-poly…), break-from-reality stills | Follow the brand's image rules; brief approved first, cost shown first |
| **Generated video** (video tool) | short animated scene-world shots, avatar demos | Only when stills + camera moves can't do it; cost shown first; label AI-generated |
| **Multi-take compositing** | Clone Grid, Mirror Debate, The Department of Me, clone composite | Needs extra locked-off takes (listed in the shoot brief or recording kit), mattes from `base.py`, and shared lighting |
| **Drawn maps** | route draw, pin drop, map run | Draw simplified SVG maps from public-domain outline data; don't screenshot map services |
| **Code-synthesized sound** | ticks, whooshes, risers, hits, 8-bit jingles | Web Audio via OfflineAudioContext, or ffmpeg `aevalsrc` |

If an option can't be built well with the tools available, say so in the plan and offer the closest kept option instead. Never swap in an option from the No lists.
