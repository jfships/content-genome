# Catalog: motion (Stage 5)

**Tier:** **C** common · **R** rare · **F** funky. Every move is shown click-to-play on the same specimen scene, in the locked palette and fonts. Energy 1 = quiet, 3 = loud.

## Feel groups (Stage 5.1: one page, the feel and the entrances together)

The entrances are shown grouped under five feels, so picking a feel and building the entrance library happen on one page. Each group opens with a card playing the feel itself (title and label together, from the personalities below).

| Group | Feel card | Entrances in it |
|---|---|---|
| Calm | glide (or drift, cinematic) | fade up, blur in, ink bleed, word by word, marker sweep |
| Smooth | editorial | mask reveal, wipe, slide in, rotate in, flip, page curl |
| Snappy | snap (or mechanical, deadpan) | hard cut, zoom in, typewriter, decode, print out, counter roll |
| Punchy | punch (or glitchy) | slam, side slam, stamp, glitch, neon flicker, reform |
| Playful | playful (or handmade) | word spring, bounce, letter drop, hanging sign, squash & stretch, unroll, boiling lines |

Every entrance must look clearly different at a glance (direction, speed or effect), never several near-identical fades.

## Motion personalities (the feel cards and the motion table)

| Slug | Name | Tier | Feel | Typical eases |
|---|---|---|---|---|
| snap | Snap | C | Fast in, hard stops, cuts on the beat | `expo.out` / `power2.in` |
| glide | Glide | C | Smooth, premium, soft rises | `power2.out` / `power2.in` |
| punch | Punch | C | Big hits, quick push-ins, cut on action | `expo.out` / `power3.in` |
| deadpan | Deadpan | R | Typewriter text, long still holds, dry cuts | `steps(n)` + `power3.out` |
| drift | Drift | R | Slow, floaty, long camera moves | `sine.inOut` |
| mechanical | Mechanical | R | Stepped, precise, counters and slides | `steps(n)` / `power1.inOut` |
| editorial | Editorial | R | Measured reveals, elegant masks, generous holds | `power3.out` |
| playful | Playful Spring | F | Springy overshoot, wobble, squash and stretch | `back.out(1.7)` / springs |
| handmade | Handmade Jitter | F | Stop-motion feel: 12 fps, boiling lines, slight shake | stepped at 12 fps |
| glitchy | Glitchy | F | Digital stutters, RGB splits, frame skips | `steps` + random offsets |
| cinematic | Cinematic | R | Slow push-ins, letterbox, long dissolves | `power2.inOut`, long durations |

## Element moves

| Slug | Name | Tier | Energy | What it does |
|---|---|---|---|---|
| cut | Hard Cut | C | 1 | Appears instantly |
| fade-up | Fade Up | C | 1 | Fades in while rising slightly |
| soft-rise | Soft Rise | C | 1 | Rises a short distance, scales 0.98 → 1 |
| mask | Mask Reveal | C | 2 | Slides out from behind an invisible edge |
| word-stagger | Word Stagger | C | 2 | Words arrive one after another |
| typewriter | Typewriter | C | 1 | Characters appear one by one |
| wipe | Wipe | C | 2 | A clean edge sweeps the element in |
| split | Split Slide | C | 2 | Two halves slide apart or together |
| zoom | Zoom In | C | 2 | Scales up into place |
| counter | Counter Roll | C | 2 | Numbers roll up to the value |
| blur | Blur In | R | 1 | Comes into focus |
| draw | Draw On | R | 1 | Lines draw themselves |
| outline-draw | Outline Draw | R | 1 | An outline draws, then fills |
| highlight | Marker Sweep | R | 2 | A highlighter stroke sweeps behind |
| scramble | Decode | R | 2 | Random characters resolve into the word |
| ticker | Ticker | R | 2 | Text scrolls past continuously |
| focus-pull | Focus Pull | R | 1 | Focus racks from one thing to another |
| rotate | Rotate In | R | 2 | Swings in on a pivot |
| swing-in | Swing In | R | 2 | Hangs and swings into place like a sign |
| side-slam | Side Slam | R | 3 | Slams in from the side and stops dead |
| slam | Slam | R | 3 | Drops in hard with a tiny shake |
| glitch | Glitch | R | 3 | RGB split and jitter |
| zoom-through | Zoom Through | R | 3 | The camera flies through the element to the next |
| word-spring | Word Spring | F | 3 | Words spring in with overshoot |
| letter-drop | Letter Drop | F | 3 | Letters fall in one by one |
| flip | Flip | F | 2 | Flips like a card |
| stamp | Stamp | F | 3 | Stamps down with a thud |
| punch-in | Punch | F | 3 | Bursts in at oversize and snaps back |
| squash | Squash & Stretch | F | 3 | Cartoon squash on landing |
| liquid | Liquid Morph | F | 2 | Melts from one shape into the next |
| ink-bleed | Ink Bleed | F | 2 | Spreads in like ink on paper |
| paper-fold | Paper Fold | F | 2 | Unfolds like paper |
| shatter | Shatter | F | 3 | Breaks into shards and reforms |
| magnet | Magnetic Snap | F | 3 | Pieces fly in and snap together |
| boil | Boiling Lines | F | 1 | Hand-drawn lines wiggle frame to frame |
| page-curl | Page Curl | F | 2 | Peels in like a page turn |
| neon-flicker | Neon Flicker | F | 2 | Flickers on like a neon tube |
| print-out | Print Out | F | 1 | Prints out line by line like a receipt |

## Transitions (between scenes)

| Slug | Name | Tier |
|---|---|---|
| hard-cut | Hard cut on the beat | C |
| match-cut | Match cut | C |
| j-l-cut | J-cut / L-cut | C |
| dissolve | Dissolve | C |
| soft-rise-t | Soft rise | C |
| object-wipe | Object wipe | R |
| color-wipe | Color wipe (often reserved for the sting) | R |
| split-slide-t | Split slide | R |
| zoom-through-t | Zoom through | R |
| whip-pan | Whip pan | R |
| slice-shift | Slice shift (strips slide away) | R |
| iris | Iris in/out | F |
| page-tear | Page tear | F |
| film-burn | Film burn | F |
| pixel-dissolve | Pixel dissolve | F |
| datamosh-t | Datamosh melt | F |
| spin-blur | Spin blur | F |
| tv-off | TV switch-off | F |
| ink-wipe | Ink wipe | F |

## Camera

| Slug | Name | Tier |
|---|---|---|
| drift | Breathing drift | C |
| push-in | Push-in to the storyteller | C |
| pull-out | Pull-out reveal | C |
| parallax | Parallax layers | C |
| slow-pan | Slow pan across a page | C |
| rack-focus | Rack focus | R |
| crash-zoom | Crash zoom | R |
| orbit | Orbit (2.5D) | R |
| dolly-zoom | Dolly zoom (vertigo) | F |
| handheld-shake | Handheld shake | F |
| snap-zoom | Snap zoom with speed lines | F |
| top-down-spin | Top-down spin | F |

## Spatial (Stage 5c: screens and ideas in 3D space)

Working sources for every row: `spatial/src/<slug>/`, rules and more sources in `spatial/README.md`. Tier: C common, R rare, F funky.

| Slug | Name | Tier |
|---|---|---|
| fly-through-pipeline | Fly through the pipeline | R |
| floating-screen | Screen floating in space | C |
| scroll-click-lock | Scroll, click, lock | C |
| exploded-layers | Exploded layers | R |
| glowing-floor-pipeline | Pipeline on a glowing floor | F |
| rises-out-of-pile | Rises out of the pile | F |
| stepping-orbit-ring | Stepping orbit ring | R |
| tunnel-fly-through | Tunnel fly-through | R |
| fanned-screens | Fanned screens | C |
| dolly-zoom | Dolly zoom | F |
| rack-focus | Rack focus | C |
| phones-fan | Phones in a fan | C |
| dolly-zoom-frames | Dolly zoom, frames | R |
| card-depth-stack | Card depth stack | R |
| orbit-ring | Orbit ring | R |
| color-tunnel | Color tunnel | F |
| parallax-zoom | Parallax zoom | C |
| bokeh-rack-focus | Bokeh rack focus | R |
| push-into-card | Push into a card | C |
| card-flips-3d | 3D card flips | C |
| app-in-3d | Real app in 3D | R |
| whip-pan | Whip pan | C |
| title-opener-3d | 3D title opener | R |
