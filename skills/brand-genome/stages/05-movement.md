# Stage 5: Movement language (how the brand moves)

Every page here is built from `../page-template/` with the words in `../voting-pages.md`. Open the stage with its plain hand-off (what it is, two or three pages, about 5–15 minutes, nothing happens without their say, they can stop anytime).

Two channels with the same colors feel different because of how things move. This stage decides the motion feel and writes it as a table any video skill can follow exactly.

Two steps. Options: `../catalog/motion.md` (feels with their entrances, transitions, camera), common through funky.

**Every demo is the same plain scene:** a title and a label entering on a plain background in the brand's palette and fonts, looping cleanly. No photos, no extra zoom, no image switch, so the only thing that differs between cards is the movement. One big centered play/pause per card.

## 5a. Motion feel and how things come in (one page)

`motion-entrances.json`. Picking a feel and building the entrance library happen in one place, so nobody asks "didn't I just pick this?". The entrances (28–32) are grouped under five feel headings: **Calm · Smooth · Snappy · Punchy · Playful**. Each group opens with a card that plays the feel itself (title and label together) and has **Play all in this feel**.
- **The feel** (fixed): on each group's header, **Main feel** · **Backup feel** · **Alternative**. Main and Backup slots sit at the top of the page. Recommend one from the content personality ("calm / thoughtful" → Calm or Smooth): mark that group's feel card **Our pick for you** (`pick` + `why`). No bounce or elastic as the Main feel unless they pick a playful feel on purpose.
- **The entrances** (library): **Keep in library** / **Discard** on each, from any group. A note on a kept one is its rule ("letter drop only for episode titles"). None kept → the entrances in the Main feel's group.
- Every entrance must look clearly different at a glance: a different direction, speed or effect, never five slight fades. Include the funky ones (stamp, typewriter, bounce, unroll, glitch-in, drop with a thud).
- Recap line after the review: "Your motion feel: Snappy, backup Calm. 9 entrances saved."

## 5b. Scene changes (library, skippable)

`scene-changes.json`, two sections: **Everyday** (hard cut, dissolve, match cut, color wipe, slide, push, whip…) and **Break-from-reality transitions** (record scratch freeze, page tear, cartoon whip, TV static, comic panel, TV off). Each card shows scene 1 turning into scene 2. Keep in library / Discard. Skipped → hard cut + one dissolve.

Then derive rhythm, camera and text timing from the motion feel and the keeps. Show them as plain-words lines in chat (how long shots hold, long and vertical; what the camera does; how long titles stay). Ask once with AskUserQuestion: **Keep all** / **Change one (say which)**. Never ask these as open questions. Phrase length in music beats is set in Stage 6, once tempo exists.

## 5c. Spatial moves (library; required when the fallback is motion graphics or a format shows screens, explains or teaches; otherwise offered and skippable)

Screens and ideas moving in 3D space: camera fly-throughs, screens floating in depth, exploded layers, orbit rings, tunnels, dolly zooms, rack focus, push into a card, 3D card flips, whip pans, 3D titles. This is what makes a screen demo or an explainer look like a top agency made it, and it's the usual fallback when a topic is hard to make entertaining. Working sources and rules: `../catalog/spatial/README.md`.

- **Check free disk first (at least 2 GB).** HyperFrames refuses to render with under 1 GB free. If there isn't room, build the page as poster cards (a snapshot at 3 s of each move) marked "clip owed" rather than skipping the page.
- **Build a real test pack, not mockups.** 8–12 moves from the catalog, each a 6-second clip in the creator's palette and fonts (set `shared/base.css` `:root` and the font files), showing their real screens if they have any (their site, an app they use, their notes); otherwise neutral stand-in screens drawn in code, labeled as stand-ins. Render with HyperFrames at draft quality (`npx hyperframes render -q draft -f 15`). Say how long rendering will take before starting.
- **Page:** `motion-entrances.json` shape with one section, each card a clip (`html` = a muted `<video>` with a poster, `play` = a small play function defined in `head`; `../page-template/README.md`, "Clip cards"). **Keep in library** / **Discard**, notes on each.
- **Go wide.** The creator can't ask for moves they've never seen. Include the HyperFrames registry's spatial pieces and anything new from outside it (the catalog lists where to look), rebuilt in the brand. If they ask for more, run another round; the library is meant to keep growing.
- No renderer available → skip with "Spatial library: owed" in the Genome; video-genome builds it before the first screen-demo episode.
- **Real 3D round (offered after the CSS pack, skippable).** Glass, particles, liquid, wireframe, solid bars, dust: `../catalog/spatial/README.md` "Real 3D". Render 6–9 as 6-second drafts in the brand colors with Three.js in a headless browser (no GPU needed), same clip-card page, **Keep in library** / **Discard**. Needs about 2 GB free wherever it renders (a cloud workspace is fine, the clips are small); the creator can delete the render folder afterwards, the source stays with the clips. If it looks thin, say so and run a second round before asking for picks: a creator cannot ask for moves they have never seen.
- Recap line: "Spatial library: 14 moves kept, 4 skipped; real 3D: 7 kept, 1 skipped."

## 5d. The motion table

Write one table into the Brand Genome. Use these exact fields so video skills can read it:

| Field | Meaning | Example |
|---|---|---|
| Personality | the Main feel + 3–4 words | Calm: soft, exact, unhurried |
| Entrance ease | for headlines / everything else | `expo.out` / `power3.out` |
| Exit ease | | `power2.in` |
| On-screen move ease | | `power3.inOut` |
| Text and counters | | `steps(n)` typewriter |
| Overshoot | 0 unless the brand is playful | 0 |
| Base unit | small items / headlines / camera moves | 0.4 s / 0.6–0.9 s / 0.8–2 s |
| Stagger | per item; the group finishes within | 60 ms; 0.7 s |
| Transitions | default + extras + reserved | hard cut; match cut, object wipe |
| Hold | stillness after a beat lands | ≥ 0.3 s |
| Camera | drift, push-in range, parallax | drift 1→1.05; push 1.4–2×; 1 / 0.5 / 0.2 |
| Shot hold | typical shot length, long / vertical ceiling | 4–8 s / ceiling ~2.5 s, each shot sized for its job |
| Spoken pace | target words a second after the edit, long / vertical | 2.3–2.8 / 2.6–3 |
| Phrase length | filled in Stage 6 | 8 beats / 4 beats |
| Spatial | kept spatial moves (catalog slugs) + any rule | fly-through, rack-focus, push-into-card; never on talking-head beats |
| Never | banned moves | bounce, spin, zoom-blur |

Ease names are GSAP's (power2 = cubic, power3 = quart). Write the cubic-bezier equivalents beside them for tools that don't use GSAP. Ease names and bezier values never appear in chat; they live in the table only.

**Vertical variant:** a second row for Shorts and Reels, with these values: shot lengths by job (talking lines end on the last word, usually 1–2.5 s; proof gets reading time, about 0.3 s a word + 0.5 s; cutaways 0.5–1.5 s), a ceiling of about 2.5 s a shot, no single visual over ~4 s; a spoken-pace target of 2.6–3 words a second (a target, never a fixed speed-up: the edit speeds speech only by what's missing, 12% max); punch-ins of about 1.1–1.25× on the hook and each punchline (eased in, hard cut back); one held deadpan beat (≤1.5 s) allowed per punchline; phrase length 4 beats. Stage 8 confirms it.

## Output

The motion table in `movement.md` (Main feel, backup and alternatives, the kept entrances, scene changes and spatial moves with their use-when, the pages' artifact URLs), plus the specimen page sources in `01 Brand Kit/page-sources/`.

**Hand-off at the end of Movement** (one line): "Movement is done: your feel, entrances and scene changes are saved. Next: Sound, the music and sound effects your videos use (2 pages)."
