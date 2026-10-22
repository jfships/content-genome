# Graphics library

Every move this skill knows, by family. The brand decides which are on-brand: use only options its packs kept (listed by name in the brand file), never anything on its No lists or house rules. Any option in that catalog can be built; see "Building catalog options" at the end. Before hand-building any move, search the HyperFrames registry (`npx hyperframes catalog --query "<move in plain English>"`) and reuse a component if one exists. Overlay moves on footage can use the bundled engine (`tools/talking-head/reference/looks.md`).

**Mechanics rule.** Every move here ships with its mechanics and a use-case: what it is · use when · **Trigger** (the kind of script line or beat that calls it; in a script card the move fires `@word` or `@event`) · **Hold** (typical time on screen) · fails when. No trigger in the script, no move. A new move is added only with all of these (see `plan/story-libraries.md`, rule for adding options).

**Hold defaults.** Text: reading time ≈0.3 s per word + 0.5 s, never under 1.1 s; numbers ≥1.5 s. Set pieces 2–4 s. Wildcards ≤1–2 s. A word shown as a pop is never in the caption chunk on screen at the same moment.

**Fits** = the motion feels a move suits, matched to the brand's motion personality: **S** Snap · **G** Glide (also Editorial, Cinematic) · **D** Deadpan · **P** Punch (also Glitchy) · **Dr** Drift · **M** Mechanical · **all**. Playful and Handmade fit anything marked G or D, with their own springs or 12 fps stepping. These letters are internal; never show them to the creator.

## 1. Title styles

| Move | What it is | Use when | Trigger | Hold | Fits |
|---|---|---|---|---|---|
| Stencil | Spray-stencil letters with slight overspray | Raw, handmade brands; chapter titles | A chapter or section-change line | Reading time | D, S |
| Label Maker | Embossed tape strip, letters punched in | Naming things, lists, deadpan labels | A line that names a thing or a list item | Reading time | D, M |
| Sticky Note | Handwritten note slapped on the frame | To-dos, asides, plans | An aside, plan or "note to self" line | Reading time | D, G |
| Hand Annotation | Marker circles, arrows and words drawn on | Pointing at something specific | Pointing words: "this", "here", "right there" | Draw-on ~0.5 s + reading time | all |
| Highlighter | A marker stroke sweeps behind a key line | The one line to remember | The one line to remember (the beat's claim) | Reading time, ≥1.5 s | all |
| Outline + Fill | Outlined type that fills on the beat | Clean product brands; reveals | A reveal word; fill lands on the spoken word | Reading time | G, S |
| Keynote Minimal | One big word, lots of space | Calm, premium statements | A one-word or short statement line | 1.1–2 s | G, Dr |
| Kinetic Bold | Heavy words moving on the beat | Hype openers, high energy | Hook line or a payoff on a music hit | Reading time per phrase | P, S |
| Risograph | Grainy two-ink offset print type | Indie, editorial, playful | A title or section line | Reading time | G, D |
| Big Number | One huge number with a small label | Stats, prices, counts | A line that says a number the viewer must remember | ≥1.5 s | all |
| Photo-Filled Type | Footage or a photo shows through the letters | Openers, place names | Opening line or a place name | 1.5–2.5 s | G, Dr |
| Chat Thread | Message bubbles appear in turn | Conversations, prompts, DMs | A line quoting a prompt, message or reply | Reading time per bubble | all |
| Terminal | Monospace text typing in a terminal | "Building", code, systems | "I built", "I ran", a command or system line | Type-on + reading time | D, M |
| Typewriter | Characters appear one by one, stepped | Deadpan reveals, notes | A deadpan reveal or a short note | Type-on + reading time | D, M |

## 2. Overlays and callouts

| Move | What it is | Use when | Trigger | Hold | Fits |
|---|---|---|---|---|---|
| Word-by-word captions | Spoken words appear as said | Default captions for social | All speech (caption mode full) | Synced to speech | all |
| One word at a time | A single big word per spoken beat | Hooks, vertical | Fast hook lines, 3–5 words | One spoken word each | P, S |
| Clean subtitle | Plain two-line captions | Calm, professional | All speech, calm delivery | Synced; chunks ≤17 characters/s | G, Dr |
| Highlight captions | The spoken word turns the accent color | High energy, vertical | The beat's key word inside the caption | Synced to the word | P, S |
| Lower third | Name, role or place in a bar | First appearance, guests, places | First time a person or place appears | ~2 s | all |
| Callout | A box with a line pointing at a detail | Explaining one part | A line about one part ("this setting controls…") | Reading time | all |
| Checklist | Items tick off in turn | Steps, requirements, results | "Step 1/2/3", a list of requirements | Each tick on its spoken item; whole list ≥ reading time | all |
| Stat bubble | A small number badge pops near the subject | Supporting numbers | A supporting number said in passing | ≥1.5 s | S, P |
| Spotlight | The frame dims except one area | Focusing on a detail | "Look at this part", one detail | 1.5–3 s | G, D |
| Progress steps | A bar of steps showing where we are | Tutorials, multi-part videos | "Three steps" in the hook; "step 2" lines | Updates each step; stays while steps run | all |
| App window | A clean window frame holding a screen | Showing tools | A line naming a tool or "watch this" over a screen | As long as the screen beat | G, M |
| Marker highlight | A hand-drawn stroke under or around words | Emphasis on a screen or page | The one phrase on a page or screen that matters | Draw-on + reading time | all |
| Hand-drawn arrow | An arrow draws itself to a target | Pointing, playful | Pointing words: "here", "this one" | Draw-on ~0.5 s + 1 s | D, G |

## 3. Placements (where the person sits)

| Move | What it is | Use when | Trigger | Hold |
|---|---|---|---|---|
| Full cutaway | Graphics fill the frame; face leaves | A process, product, comparison, number. Not on personal lines | A line about a thing that can be shown fully | 3–10 s |
| Side panel | A transparent graphic in empty space beside them | Footage with real empty space | A supporting point while the face keeps talking | Can run 15 s+ |
| Speaker to side / corner | Their footage shrinks into a box while a graphic plays, then grows back | Personal and trust videos where the face should never leave. Beats over 4 s | A screen or proof beat in a personal video | >4 s |
| Cutout beside graphics | Person cut out from the background, placed beside graphics | Graphics-first videos; polished explainers | Explainer beats where the person presents the graphic | Beat length |
| Corner bubble | Small round or rounded face in a corner | Screen-heavy tutorials | Opinion or reaction while the screen is the subject | As long as the screen beat |
| Taking turns | Full face, then full graphic, alternating | Simple, fast to build | Claim line (face) then show line (graphic) | Beat length each |
| Voice only | No face; graphics carry it | Story beats, recaps, the creator off camera | Narration with nothing to gain from the face | Beat length |
| Word pop | 1–4 of their words spring in over them | The line to remember | The beat's key word (POP @word) | Reading time; at most every ~15 s |
| Text behind speaker | A word pop passing behind their head | One standout moment, often the hook. Words stay ≥ 70% visible | The hook word or the one standout line | 1.5–2.5 s |

## 4. Footage treatments

| Move | What it is | Use when | Trigger | Hold |
|---|---|---|---|---|
| Background blur | Shallow depth of field on the room | Messy rooms; default for home recordings | Always on for home footage | Whole shot |
| Background dim | Room darkened (optionally blurred) | Graphics and captions need to stand out | A beat with a graphic or text over the face | While the graphic shows |
| Background replace | Room swapped for a brand color or image | Clean studio look; check hair and hands | Format choice, not a line | Whole shot |
| Ease zoom | Gentle push-in on a word (1.06–1.12) | Emphasis in calm videos; 4 s+ apart | A key word or the end of a thought (PUSH) | Over the beat; snap back at the next idea |
| Punch zoom | Instant cut-in (1.15–1.25) | Emphasis in high-energy videos | Key word, number or opinion line (PUNCH); 3–5 per 30 s | Until the next sentence |
| Pack grade | The brand's base grade on all footage | Always | Always | Whole video |
| Accent grade | The brand's accent grade on its trigger | Flashbacks, late nights, payoffs, as the brand says | The brand's named trigger (flashback line, payoff) | The triggered beat |
| Freeze frame | Footage stops on a frame; graphics take over | Before a mark-up, a reveal or a joke | "Look at this", "wait", a moment to label | 1.5–3 s |

## 5. Screen walkthroughs

Use whenever a screen is shown. Blur or crop private data first. Pause before a click so the viewer sees where the cursor lands; one callout per click.

| Move | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|
| Cursor click | An oversized cursor moves and clicks with a ripple | Showing where to click | "Click", "hit", "open" | ≥1 beat after the click | Cursor waves around; click out of sync with the word |
| Typing a prompt | Text types into a field, character by character | Showing the exact input | A line quoting the prompt or "type this" | Type-on + reading time of the key part | Text too small at phone size; typed too fast to read |
| Scroll through | A page scrolls with easing and pauses on the key part | Long pages, results lists | "Scroll down to…", "look further down" | Pause ≥ reading time on the key part | No pause; scrolls past the point |
| Camera push-in | The camera pushes into the part of the screen that matters | Small UI details | Line names the detail; start ~0.2 s before the word | Over the beat; 8–15% push | Hides the context the viewer needs |
| Drag to select | A selection box drags over content | Choosing a range or items | "Select", "grab these" | ~1–1.5 s | Selection unrelated to the line |
| Notification pop | A toast or banner slides in | Something arrives or finishes | "Then this comes in", "done" | Reading time | Covers the key UI |
| Hover tooltip | A tooltip appears on hover | Explaining a control | "What this button does" | Reading time | Tooltip text unreadable |
| Drag a slider | A slider moves and something responds | Showing a setting's effect | "Turn it up", "lower the…" | Until the response is visible, ~1.5–2 s | Response too small to see |
| Real screenshot in shape | The real screen inside the morphing shape, a highlight ring on the key word | A real screen as proof inside a designed scene | "Here's the real one", proof lines | Reading time on the ringed word | Screenshot blurry or private data visible |
| Before / after toggle | One switch flips the screen between two states | Same screen, two states | "Before … after", "with and without" | ~2 s on each state | Difference not visible at phone size |
| Side-by-side compare | Two screens or results next to each other | Comparing tools or outputs | "This one vs this one" | ≥2 s; reading time per side | Text unreadable at half width |
| Chart with tooltip | A chart draws; a tooltip reads one value | One value in a trend | A line naming one number in a trend | ≥1.5 s on the value | Chart has no clear single point |
| Search / filter list | A list filters as text is typed | Finding one item in many | "Search for", "filter by" | Until the result shows + 1 s | Typed term not readable |
| File drag and drop | A file drags into a drop zone | Uploading or importing | "Drop the file in", "upload" | ~1–1.5 s | File name unreadable |
| Live status island | A small pill shows a live status changing | Waiting, running, done states | "It's running", "now it's done" | Each state ≥1 s | Status change not tied to the line |

## 6. Signature moments (set pieces)

Use 2–4 per long video, from the brand's kept list. Hold 2–4 s.

| Move | What it is | Use when | Trigger | Hold |
|---|---|---|---|---|
| Clone Grid | A grid of copies of the creator (or object), each doing a different role | Showing many jobs, versions or options at once | "I do five jobs", "every version of…" | 2–4 s |
| Look Cascade | The same shot flips through several looks in a fast cascade | Showing choices, styles, variations | "Same shot, ten styles", a list of options | 2–4 s |
| Progression Quad | Four panels showing stages of progress side by side | Before → after, versions, growth | "From version 1 to 4", growth lines | 2–4 s |
| Freeze & Mark Up | Footage freezes; hand annotations draw over it | Explaining what's happening in a frame | "Look at this part", "see what happened here" | 2–4 s |
| Slice Shift | The frame splits into strips that slide to reveal the next scene | Chapter changes, reveals | A chapter change or "here's what it became" | 1–2 s |
| Contact Sheet Pick | A contact sheet of frames; one gets circled and pulled out | Choosing the best of many | "Out of all of these, this one" | 2–4 s |
| Word Burst | One word explodes into many related words | Brainstorms, overwhelm, lists | A line about too many options or ideas | 2–3 s |
| Mirror Debate | Split screen: the creator argues with themself | Pros and cons, doubts, two sides | "Part of me says … the other part says" | Beat length |
| Sticker Bomb | Labels or stickers slap onto the frame in a burst, styled to the pack | Playful lists, reactions | A playful list or a verdict line | 1.5–3 s |

## 7. Wildcards (at most one per video, on the hook or a turning point)

| Move | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|
| Crash Zoom | A violent zoom into a face or object, with a whoosh | A shock or realization | The pivot word ("wrong", "wait") | ≤1 s | Nothing new follows it |
| Page Tear | The frame tears like paper to reveal the next scene | A hard switch of scene or view | "But then", a reversal line | ≤1.5 s | Used as decoration between related shots |
| Pixel Collapse | The image collapses into pixels and rebuilds | Something breaks or rebuilds | "It all broke", "rebuilt from scratch" | ≤1.5 s | The line isn't about breaking or rebuilding |
| Redacted | Black bars slam over words, then lift on the reveal | Hiding then revealing a word or number | A secret or "the one word they don't say" | Bars ≤1–2 s, then the reveal at reading time | Reveal never comes or is smaller than promised |
| Slot Machine | Reels spin and land on the answer | Picking one answer from many | "Which one won?", random pick | ≤2 s spin | Answer predictable |
| Thermal Flash | 1–2 s of thermal-camera look on a pressure moment | Heat, pressure, stress moments | A line about pressure or panic | 1–2 s | No pressure in the line |
| Tape Rewind | The video rewinds with tape artifacts to replay a moment | Replaying a missed detail | "Wait, watch that again" | ≤1.5 s, then the replay | Replays something already clear |

## 8. Data and number moves

Real numbers only; illustrative ones are labeled as such in the plan.

| Move | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|
| Counter roll | Digits roll up to the number | A total or result | A line that says the final number | Roll ≤1 s + ≥1.5 s on the number | Roll so long the number lands after the word |
| Number wheel | Digits spin on wheels and lock | A reveal number | A held-back number ("it came to…") | Spin ≤1 s + ≥1.5 s | Lock lands before the line names it |
| Bar race | Bars grow and reorder | Ranks changing over time | "Who's ahead", a ranking over time | 3–6 s | Too many bars to read on a phone |
| Stat stack | Numbers stack up one by one with labels | Several supporting numbers | A line listing 2–4 numbers | ≥1.5 s per number | More than 4 numbers |
| Progress ring | A ring fills to a percentage | One percentage | A line with a percent | Fill ≤1 s + ≥1.5 s | Percent without a label |
| Before / after split | A wipe divider shows two states | Two numbers or states compared | "From X to Y" | ≥2 s | Both sides unlabeled |
| Ticker | A strip of numbers or words scrolls past | Background sense of volume or news | A line about many items or live change | As background, beat length | Viewer is meant to read it |
| Timeline scrub | A playhead moves along a dated line | Events in time order | "In March … by June" | 2–4 s | Dates unreadable |

## 9. Map and place moves

| Move | What it is | Use when | Trigger | Hold | Fails when |
|---|---|---|---|---|---|
| Route draw | A line draws between places | A trip or path | "From A to B" | 2–4 s | Places unlabeled |
| Pin drop | A pin lands with a small bounce-free settle | Naming one place | The place name | ~1.5 s | Map too zoomed out to read |
| Globe-to-street zoom | The camera dives from a wide map to a place | Opening on a place | Opening line naming the place | 2–3 s | Used for a place the viewer doesn't need to locate |
| Location card | A small card names the place and time | Setting the scene | First mention of where and when | Reading time | Repeats what the spoken line just said word for word |

## 10. Transitions

| Move | Trigger | Hold | Fits |
|---|---|---|---|
| Hard cut on the beat | A new idea starts ("So", "Now", "Step 2", a number), on or just before the first word | Instant | all |
| Match cut | Last line echoes the first, or two shots share shape or motion | Instant | all |
| Object wipe | A thing passes the lens as the topic changes | ~0.3–0.5 s | S, P, G |
| Color wipe (often reserved for the sting) | The brand's sting or a section change | ~0.3–0.5 s | S, P |
| Soft rise | A calm section change | ~0.5–0.8 s | G, Dr |
| Split slide | Moving from one item to the next in a list | ~0.4–0.6 s | G, M |
| Zoom through | Going "into" a screen or idea ("let's look inside") | ~0.3–0.5 s | P, S |
| Whip pan | A fast jump in place or time ("meanwhile", "an hour later") | ~0.2–0.4 s | P |
| Dissolve | Time passing, mood change | ~0.5–1 s | G, Dr |
| J-cut / L-cut | Voice leads the next shot (payoff, question) or lingers over proof | Offset 0.2–0.5 s | all |

## 11. Camera moves

For 3D camera work on screens, see §14.

| Move | Trigger | Hold |
|---|---|---|
| Push-in to the storyteller | An emotional or key line | Over the beat, 5–10% |
| Pull-out reveal | "Here's the whole thing", a scale reveal | 1.5–3 s |
| Parallax layers | A still that needs life on a narrated beat | Beat length |
| Focus pull (rack focus) | Attention moves from one thing to another in the line | ~1 s pull |
| Pan across a page timed to the words | The line reads or names parts of a page | Synced to the words |
| Overhead (straight down) on hands or a desk | Hands-on steps ("first I lay out…") | Step length |

## 12. Textures and backgrounds

- **Textures:** film grain, vignette, paper, halftone, scanlines, light leak, dust. One base texture per pack; accents only on their triggers.
- **Backgrounds behind a cutout or a graphic:** solid brand color, moving gradient, blueprint grid, notes wall, moving type wall, real place blurred, footage behind, floating cards, studio sweep, a dark room with one light. The brand names one default per pack plus accents with triggers. Never the same flat background two scenes in a row.

## 13. Break-from-reality builds (cheap first)

- **Paper cutout animatic:** flat cutouts of the creator moving on a drawn set. Free, fast, on-brand. Trigger: a story beat with no footage.
- **Clone composite:** the same person filmed 2–6 times in different spots, combined with mattes. Trigger: "all the roles I play".
- **Miniature:** the creator shrunk inside a screen, a desk or a product (cutout + scale + shadow). Trigger: "inside the app", feeling small next to a task.
- **Narrator overlay:** a hushed documentary narrator over normal footage (generated voice described by delivery, never imitating a real person). Trigger: a mundane moment played as serious, for comedy.
- **Trailer card:** a mundane task cut like a movie trailer: title cards, booms, a release date. Trigger: a launch or a "coming soon" line.

Draft cheaply, mark "CUT CANDIDATE", give the full treatment only to the 1–2 kept. Hold: set-piece rule (2–4 s per moment).

## 14. Spatial moves (screens and ideas in 3D space)

Fly-throughs, screens floating in depth, exploded layers, orbit rings, tunnels, dolly zooms, rack focus, push into a card, 3D card flips, whip pans, 3D title openers and more, each with a working source: `craft/spatial/README.md`. The default family for screen demos and explainers, and the brand's fallback when a beat is hard to make entertaining. Trigger: a screen-demo or abstract-idea beat with nothing moving on screen for about two sentences. Hold: the beat (moves inside 1–3 s). Fits G, S, P (built with long-tail easing, never bounce).

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
