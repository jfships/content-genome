# Stock ids: catalog rows → stock samples

Read by `../voting-pages.md` ("Stock samples") when a device round is built. Each row maps a catalog slug to the stock-library id whose sample the page shows. The stock library's `manifest.json` is the source of truth for ids, names and whether a sample is built; this table only says which id a catalog row is. When the two disagree, the manifest wins: fix this table.

**Status** (as planned 2026-10-30; check the manifest for what is actually rendered):
- `batch 1`: in the first build batch of the stock library.
- `owed`: has an id; no sample built yet.
- `new <CAT>`: no id yet. It needs a sample before it can be shown from stock; the category is the proposal, the number is given when the sample is built.
- `brand layer`: not a stock device. The brand's own look (palette, fonts, type, feel, kit): drawn in the creator's colors every run, never from stock.

A catalog row may share an id with another row (two names for one device). `(variant)` means the stock sample shows the device but not this row's twist; the row's own twist is still drawn.

## graphics.md

**Graphic systems** (18 rows, Stage 4.6): all `brand layer`. They are the text style itself; stock samples are restyled with the one picked.

**Title styles**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| clean-bold | Clean Bold | C | — | brand layer |
| keynote-minimal | Keynote Minimal | C | — | brand layer |
| kinetic-bold | Kinetic Bold | C | POP-01 | batch 1 |
| stat | Big Number | C | POP-06 | batch 1 |
| highlight | Highlighter | C | POP-04 | batch 1 |
| chat | Chat Thread | C | PROP-01 | batch 1 |
| editorial | Editorial | R | — | brand layer |
| outline | Outline + Fill | R | — | brand layer |
| poster | Stacked Poster | R | — | brand layer |
| photo-fill | Photo-Filled Type | R | — | brand layer |
| terminal | Terminal | R | POP-12 | owed |
| annotated | Hand Annotation | R | POP-03 | batch 1 |
| sticky | Sticky Note | R | — | new PROP |
| stencil | Stencil | R | — | brand layer |
| label | Label Maker | R | — | brand layer |
| risograph | Risograph Title | R | — | brand layer |
| ticket | Ticket Stub | R | PROP-11 | owed |
| film-slate | Film Slate | R | — | new PROP |
| movie-credits | Movie Credits | R | PROP-09 (variant) | owed |
| newspaper | Newspaper Headline | R | PROP-03 | batch 1 |
| subway | Transit Sign | R | — | new PROP |
| brutal | Brutalist | F | — | brand layer |
| sticker | Sticker | F | POP-09 | owed |
| letterboard | Letterboard | F | PROP-12 | owed |
| seal | Seal / Stamp | F | PROP-08 | owed |
| folder | Case File | F | PROP-07 (variant) | owed |
| neon-sign | Neon Sign | F | POP-14 | owed |
| chrome | Liquid Chrome | F | — | brand layer |
| embroidered | Embroidered Patch | F | — | brand layer |
| chalk | Chalkboard | F | — | brand layer |
| receipt | Receipt | F | PROP-04 | batch 1 |
| warning | Warning Label | F | PROP-10 | owed |
| graffiti | Graffiti Tag | F | — | brand layer |
| varsity | Varsity | F | — | brand layer |
| extruded-3d | 3D Extruded | F | SPA-17 | owed |
| arcade-text | Arcade Text | F | — | brand layer |
| glitch-text | Glitch Text | F | — | new POP |
| karaoke-lyric | Karaoke Lyric | F | CAP-02 (variant) | batch 1 |

**Captions and small extras**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| subtitle | Clean Subtitle | C | CAP-01 | batch 1 |
| karaoke | Word-by-Word | C | CAP-02 | batch 1 |
| one-word | One Word at a Time | C | CAP-03 | batch 1 |
| boxed | Boxed Captions | C | CAP-04 | batch 1 |
| speaker | Speaker Label | C | — | new POP |
| callout | Callout | C | POP-05 | batch 1 |
| progress | Progress Steps | C | — | new POP |
| checklist | Checklist | C | POP-08 | batch 1 |
| window | App Window | C | — | new SCR |
| chapter | Chapter Card | C | — | new POP |
| spotlight | Spotlight | R | CAM-05 | batch 1 |
| stat-bubble | Stat Bubble | R | POP-10 | owed |
| quote | Pull Quote | R | — | new POP |
| emoji-react | Reaction Pops | R | POP-09 (variant) | owed |
| map-pin | Location Tag | R | MAP-04 | owed |
| timer | On-Screen Timer | R | — | new POP |
| scorecard | Scorecard | F | — | new POP |
| inner-voice | Inner-Monologue Subtitles | F | CAP-08 | owed |
| commentary | Commentary Track | F | CAP-09 | owed |
| redact | Redaction Bars | F | CAP-10 | owed |

**Interface styles** (how drawn screens look): all `brand layer` except these two.
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| floating-cards | Floating UI Cards | C | LAY-07 | batch 1 |
| glass-footage | Glass over Footage | R | LAY-09 | owed |

**Screen walkthroughs**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| click | Cursor Click | C | SCR-01 | batch 1 |
| typing | Typing a Prompt | C | SCR-02 | batch 1 |
| scroll | Scroll Through | C | SCR-03 | batch 1 |
| push-in | Camera Push-In | C | SCR-04 | batch 1 |
| select | Drag to Select | C | — | new SCR |
| toast | Notification Pop | C | PROP-02 | batch 1 |
| tooltip | Hover Tooltip | R | — | new SCR |
| slider | Drag a Slider | R | — | new SCR |
| before-after | Before/After Toggle | R | SCR-06 | batch 1 |
| split-compare | Side-by-Side Compare | R | SCR-07 | owed |
| giant-cursor | Giant Cursor | F | SCR-01 | batch 1 |
| x-ray | X-Ray Layers | F | SCR-10 | owed |

**Backgrounds** (Stage 4.8). Plains, gradients and patterns are drawn in the palette. Scene rows have a still in `../benchmark/backdrops/`; the stock version (stand-in cut out over the scene) is ported from it.
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| light-plain / pop-plain / dark-plain | Plains | C | — | brand layer |
| studio | Studio Sweep | C | BKD-05 | owed |
| blur | Your Space, Blurred | C | BKD-02 | owed |
| grad | Soft Gradient | C | — | brand layer |
| paper / grid | Paper, Grid Paper | C | — | brand layer |
| spots / rays | Polka Dots, Sunburst | R | — | brand layer |
| city-night | City at Night | C | — | new BKD |
| chalkboard | Chalkboard | R | — | new BKD |
| corkboard | Cork Board | R | BKD-06 | owed |
| blueprint | Blueprint | R | BKD-07 | owed |
| space | Space | R | — | new BKD |
| dark-bulb | Dark Room, One Light | R | BKD-01 | owed |
| text-behind | Title Behind You | R | LAY-06 | batch 1 |
| ticker-wall | Moving Type Wall | R | BKD-03 | owed |
| screens | Glowing Screens | R | BKD-04 | owed |
| weather-map | Weather Map | F | — | new BKD |
| news-desk | News Desk | F | BKD-08 | owed |
| courtroom | Courtroom | F | BKD-09 | owed |
| game-show | Game Show | F | BKD-10 | owed |
| award-stage | Award Stage | F | — | new BKD |
| moon | The Moon | F | — | new BKD |
| fish-tank | Inside a Fish Tank | F | — | new BKD |
| giant-kitchen | Giant's Kitchen | F | — | new BKD |
| crime-scene | Crime Scene | F | — | new BKD |
| cereal-box | Cereal Box | F | BKD-11 | owed |
| green-screen-joke | Obvious Green Screen | F | BKD-12 | owed |
| president | President | F | — | new BKD |
| pilot | Pilot | F | — | new BKD |
| baseball | Pro Ballplayer | F | — | new BKD |
| detective | Detective | F | — | new BKD |
| olympian | Champion | F | — | new BKD |

## moments.md

**Big moments**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| freeze-markup | Freeze & Mark Up | C | BIG-01 | owed |
| progression-quad | Progression Quad | C | BIG-02 | owed |
| contact-sheet | Contact Sheet Pick | R | BIG-03 | owed |
| look-cascade | Look Cascade | R | BIG-04 | owed |
| clone-grid | Clone Grid | R | — | new BIG |
| slice-shift | Slice Shift | R | TRN-05 | batch 1 |
| word-burst | Word Burst | R | BIG-05 | owed |
| mirror-debate | Mirror Debate | R | LAY-11 | owed |
| sticker-bomb | Sticker Bomb | F | POP-09 | owed |
| infinite-screen | Infinite Screen | F | BIG-14 | owed |
| object-cam | Object Cam | F | BIG-19 | owed |
| receipt-tally | Receipt Tally | F | PROP-04 | batch 1 |
| rewind-replay | Rewind Replay | F | — | new BIG |
| map-run | Map Run | R | MAP-01 | owed |
| stat-stack | Stat Stack | C | POP-02 (variant) | batch 1 |
| crash-zoom | Crash Zoom | R | CAM-06 | batch 1 |
| page-tear | Page Tear | F | TRN-10 | owed |
| pixel-collapse | Pixel Collapse | F | TRN-13 | owed |
| redacted | Redacted | F | STO-05 | batch 1 |
| slot-machine | Slot Machine | F | BIG-20 | owed |
| card-deal | Card Deal | F | — | new BIG |
| inverted-takeover | Inverted Takeover | F | BIG-18 | owed |
| mirror-tunnel | Mirror Tunnel | F | BIG-17 | owed |
| tape-rewind | Tape Rewind | F | — | new BIG |
| thermal-flash | Thermal Flash | F | CAM-12 | owed |
| freeze-record-scratch | Record Scratch Freeze | F | CAM-11 | owed |
| dramatic-zoom | Soap-Opera Zoom | F | CAM-10 | owed |
| silent-film | Silent Film Card | F | CAM-13 | owed |
| boss-health | Boss Health Bar | F | POP-15 | owed |

**Break-from-reality moments.** Twelve have three-panel stills in `../benchmark/bfr/`; those stay the fallback until the stock sample exists.
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| department-of-me | The Department of Me | R | — | new BIG |
| tiny-me | Tiny Me | R | BIG-13 | owed |
| nature-doc | Nature Documentary | C | BIG-07 | owed |
| the-standup | The Standup | R | — | new BIG |
| trailer | The Trailer | C | BIG-08 | owed |
| infomercial | The Infomercial | C | BIG-09 | owed |
| sports-commentary | Sports Commentary | R | BIG-11 | owed |
| courtroom | The Courtroom | R | BIG-10 | owed |
| cooking-show | Cooking Show | R | — | new BIG |
| weather-report | Weather Report | F | BIG-16 | owed |
| heist | The Heist | F | BIG-15 | owed |
| patch-notes | Patch Notes | F | — | new BIG |
| skill-install | Skill Install | F | — | new BIG |
| boss-fight | Boss Fight | F | — | new BIG |
| reality-show | Reality Confessional | C | — | new BIG |
| museum-tour | Museum Tour | F | — | new BIG |
| inner-monologue | Inner Monologue | C | CAP-08 (variant) | owed |
| alt-universe | Alternate Universe | F | — | new BIG |
| award-show | Award Show | F | — | new BIG |
| breaking-news | Breaking News | C | — | new BIG |
| unboxing | Unboxing the Mundane | F | — | new BIG |
| text-adventure | Text Adventure | F | — | new BIG |
| asmr | ASMR Moment | F | — | new BIG |

## motion.md

**Motion personalities** (11 rows): all `brand layer`. The feel is the brand's motion, and stock samples play in it once the motion table exists.

**Element moves** (entrances, Stage 5.1). The entrance page stays drawn in the brand (only the motion differs between cards); these rows carry an id so a kept entrance lines up with its stock device. Every other entrance is `brand layer`: cut, fade-up, soft-rise, mask, wipe, split, zoom, blur, draw, outline-draw, ticker, focus-pull, rotate, swing-in, side-slam, slam, glitch, letter-drop, flip, punch-in, squash, liquid, ink-bleed, paper-fold, shatter, magnet, boil, page-curl.
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| word-stagger | Word Stagger | C | POP-01 (variant) | batch 1 |
| typewriter | Typewriter | C | POP-12 | owed |
| counter | Counter Roll | C | POP-07 | batch 1 |
| highlight | Marker Sweep | R | POP-04 | batch 1 |
| scramble | Decode | R | POP-13 | owed |
| zoom-through | Zoom Through | R | SPA-07 | batch 1 |
| word-spring | Word Spring | F | POP-01 | batch 1 |
| stamp | Stamp | F | PROP-08 | owed |
| neon-flicker | Neon Flicker | F | POP-14 | owed |
| print-out | Print Out | F | PROP-04 (variant) | batch 1 |

**Transitions**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| hard-cut | Hard cut on the beat | C | TRN-01 | batch 1 |
| match-cut | Match cut | C | TRN-02 | batch 1 |
| j-l-cut | J-cut / L-cut | C | CUT-03, CUT-04 | batch 1 |
| dissolve | Dissolve | C | TRN-08 | owed |
| soft-rise-t | Soft rise | C | TRN-09 | owed |
| object-wipe | Object wipe | R | TRN-04 | batch 1 |
| color-wipe | Color wipe | R | TRN-06 | batch 1 |
| split-slide-t | Split slide | R | TRN-07 | owed |
| zoom-through-t | Zoom through | R | SPA-07 | batch 1 |
| whip-pan | Whip pan | R | TRN-03 | batch 1 |
| slice-shift | Slice shift | R | TRN-05 | batch 1 |
| iris | Iris in/out | F | TRN-16 | owed |
| page-tear | Page tear | F | TRN-10 | owed |
| film-burn | Film burn | F | TRN-11 | owed |
| pixel-dissolve | Pixel dissolve | F | TRN-13 | owed |
| datamosh-t | Datamosh melt | F | TRN-15 | owed |
| spin-blur | Spin blur | F | — | new TRN |
| tv-off | TV switch-off | F | TRN-12 | owed |
| ink-wipe | Ink wipe | F | TRN-14 | owed |

**Camera**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| drift | Breathing drift | C | CAM-09 | owed |
| push-in | Push-in to the storyteller | C | CAM-02 | batch 1 |
| pull-out | Pull-out reveal | C | — | new CAM |
| parallax | Parallax layers | C | SPA-13 | owed |
| slow-pan | Slow pan across a page | C | — | new CAM |
| rack-focus | Rack focus | R | SPA-14 | owed |
| crash-zoom | Crash zoom | R | CAM-06 | batch 1 |
| orbit | Orbit (2.5D) | R | SPA-09 | owed |
| dolly-zoom | Dolly zoom (vertigo) | F | SPA-08 | batch 1 |
| handheld-shake | Handheld shake | F | CAM-14 | owed |
| snap-zoom | Snap zoom with speed lines | F | CAM-01 (variant) | batch 1 |
| top-down-spin | Top-down spin | F | — | new CAM |

**Spatial** (Stage 5c; every row has a working source in `spatial/`, so each stock sample is a port)
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| floating-screen | Screen floating in space | C | SPA-01 | batch 1 |
| push-into-card | Push into a card | C | SPA-02 | batch 1 |
| card-depth-stack | Card depth stack | R | SPA-03 | batch 1 |
| phones-fan | Phones in a fan | C | SPA-04 | batch 1 |
| fanned-screens | Fanned screens | C | SPA-04 (variant) | batch 1 |
| fly-through-pipeline | Fly through the pipeline | R | SPA-05 | batch 1 |
| exploded-layers | Exploded layers | R | SPA-06 | batch 1 |
| dolly-zoom | Dolly zoom | F | SPA-08 | batch 1 |
| dolly-zoom-frames | Dolly zoom, frames | R | SPA-08 | batch 1 |
| stepping-orbit-ring | Stepping orbit ring | R | SPA-09 | owed |
| orbit-ring | Orbit ring | R | SPA-09 (variant) | owed |
| tunnel-fly-through | Tunnel fly-through | R | SPA-10 | owed |
| rises-out-of-pile | Rises out of the pile | F | SPA-11 | owed |
| scroll-click-lock | Scroll, click, lock | C | SPA-12 | owed |
| parallax-zoom | Parallax zoom | C | SPA-13 | owed |
| rack-focus | Rack focus | C | SPA-14 | owed |
| bokeh-rack-focus | Bokeh rack focus | R | SPA-14 (variant) | owed |
| card-flips-3d | 3D card flips | C | SPA-15 | owed |
| app-in-3d | Real app in 3D | R | SPA-16 | owed |
| title-opener-3d | 3D title opener | R | SPA-17 | owed |
| glowing-floor-pipeline | Pipeline on a glowing floor | F | SPA-18 | owed |
| color-tunnel | Color tunnel | F | SPA-24 | owed |
| whip-pan | Whip pan | C | TRN-03 | batch 1 |

## vertical-voice-formats.md

**Vertical layouts**
| slug | name | section | stock id | status |
|---|---|---|---|---|
| full-face | Full Frame + Captions | Everyday | LAY-01 | batch 1 |
| title-top | Title on Top | Everyday | — | new LAY |
| split | Split: Screen + You | Everyday | LAY-02 | batch 1 |
| pip | Picture in Picture | Everyday | LAY-08 | batch 1 |
| card-text | Text Card | Everyday | LAY-05 (variant) | batch 1 |
| backdrop | You Over a Backdrop | Everyday | — | new LAY |
| before-after | Before / After | Everyday | STO-06 | batch 1 |
| reaction | Reaction | Everyday | LAY-02 (variant) | batch 1 |
| quote | Big Quote | Everyday | — | new LAY |
| listicle | Countdown List | Everyday | STO-03 | batch 1 |
| zoom-frame | Framed Window | Everyday | — | new LAY |
| notes | Handwritten Notes | Everyday | — | new LAY |
| full-graphic | Full Graphic + Voice | Everyday | LAY-05 | batch 1 |
| text-story / chat-story / receipt-scroll | Story formats | Everyday | PROP-01, PROP-04 (variants) | batch 1 |
| cutout-screen | Cut-out Over the Screen | Cut-out | LAY-04 | batch 1 |
| title-behind | Title Behind You | Cut-out | LAY-06 | batch 1 |
| number-behind | Number Behind You | Cut-out | LAY-06 (variant) | batch 1 |
| drawn-world | You in a Drawn World | Cut-out | BIG-06 (variant) | owed |
| green-room | Green-Screen Room | Cut-out | — | new LAY |
| over-screenshot | Over a Screenshot | Cut-out | LAY-04 | batch 1 |
| floating-head | Floating Head | Cut-out | — | new LAY |
| floating-cards | Floating Cards | Cut-out | LAY-07 | batch 1 |
| comment-reply | Reply to a Comment | Cut-out | LAY-10 | owed |
| pointing | Pointing at the Screen | Cut-out | — | new LAY |
| stacked-reactions | Stacked Reactions | Cut-out | — | new LAY |
| side-by-side | Side by Side | Cut-out | LAY-03 | batch 1 |
| notification | Trapped in a Notification | Break-from-reality | LAY-12 | owed |
| peek | Peeking In | Break-from-reality | LAY-13 | owed |
| shrunk | Shrunk in a Frame | Break-from-reality | LAY-14 | owed |
| crack | The Screen Cracks | Break-from-reality | LAY-15 | owed |
| tilt | The Frame Tilts | Break-from-reality | LAY-16 | owed |

**Hook text styles**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| hook-block | Color Block | C | HOOK-01 | batch 1 |
| hook-outline | Outlined | C | HOOK-02 | batch 1 |
| hook-two-tone | Two-Tone | C | HOOK-03 | batch 1 |
| hook-label | Label + Line | R | HOOK-05 | batch 1 |
| hook-sticker | Sticker | F | HOOK-07 | owed |
| hook-part | Part N + Hook | C | HOOK-06 | owed |

HOOK-04 (hook builds word by word as it's said) is in stock with no catalog row; offer it on the hook page.

**Short covers**
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| cover-face-words | Face + Words | C | COV-01 | batch 1 |
| cover-big-word | One Big Word | C | COV-02 | batch 1 |
| cover-result | The Result | C | COV-03 | batch 1 |
| cover-number | Big Number | R | COV-04 | batch 1 |
| cover-question | The Question | R | COV-05 | batch 1 |
| cover-series | Series Grid | R | COV-06 | batch 1 |

COV-07 (before/after split) and COV-08 (word behind him) are in stock's first batch with no catalog row; offer them on the covers page.

**Short endings** (chat question; the ids go into `vertical.md`)
| slug | name | stock id | status |
|---|---|---|---|
| loop-line | Loop line | STO-09 | owed |
| payoff-cut | Cut on the payoff | CUT-01 (variant) | batch 1 |
| deadpan-hold | Deadpan hold | CUT-06 | batch 1 |
| button-line | Button line | STO-08 | batch 1 |

Voice styles and format recipes: not visual, no stock ids.

## kit.md

Wordmarks, name tags, series tags, stings, sound logos, corner marks, profile pictures and banners: all `brand layer`. Ways to close a video are long-video end cards: no stock category yet (none of the 16 has an id).

**Thumbnail systems.** Stock covers are tall (9:16); the id names the device, and the 16:9 sample is owed until stock has one.
| slug | name | tier | stock id | status |
|---|---|---|---|---|
| face-screen | Screen + Face | C | — | new COV |
| before-after | Before / After | C | COV-07 | owed (16:9) |
| big-number | Big Number | C | COV-04 | owed (16:9) |
| one-word | One Word | C | COV-02 | owed (16:9) |
| giant-object | Giant Version | R | COV-09 | owed |
| word-behind | Word Behind You | R | COV-08 | owed (16:9) |
| milestone | Milestone | R | COV-03 (variant) | owed (16:9) |
| circle-arrow | Circle + Arrow | C | COV-10 | owed |
| question | The Question | R | COV-05 | owed (16:9) |
| collage | Collage | F | COV-12 | owed |
| comic-panel | Comic Panel | F | COV-11 | owed |

## sound.md

Music lanes and sound logos: `brand layer`. Sound-effect roles, where stock has a cue: whoosh → SND-02, click → SND-01, riser → SND-03, hit → SND-04 (all owed). Tick, drop / stop, success and fail: `new SND`. SND-05 (one beat of silence) and SND-06 (ticking clock) have no catalog row.

## Counts

Device rows in the tables: 257 (85 `batch 1`, 112 `owed`, 60 `new`), plus 8 sound roles (4 owed, 4 new). So 176 of the 265 have no stock sample yet. Rows marked `brand layer` are not counted.
