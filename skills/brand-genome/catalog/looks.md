# Catalog: looks, graphic treatments, art styles

The full option set for Stage 4.1–4.3. This is deliberately wide: common looks most channels use, rare ones few use, and funky ones almost nobody uses. Show a spread from every tier; the creator's "no" votes are as useful as the yeses.

**Tier:** **C** common · **R** rare · **F** funky
**Make:**
- **Code:** applied in code to the benchmark photos (free). Recipe: shadow tint → highlight tint, saturation (1 = unchanged), contrast (1 = unchanged), extras.
- **Image:** needs an image tool to restyle a benchmark photo with the prompt key. Pre-made versions ship in `../benchmark/looks/` where available; use those first.

A round shows about 12 (never more than 16), a C/R/F spread chosen to fit the formats and personality. Later rounds can pull more from the same tables.

**The Look column is for Claude, not the page.** On a page, each option gets a name of 1–3 words and one plain, universal line about how it feels or when it'd be used ("For: a flashback"), never technical terms like "lifted blacks" or "desaturated greens". See `../page-template/examples/footage-looks-tiles.json` and `footage-filters.json`.

## A. Film and color looks

| Slug | Name | Tier | Look | Make | Recipe / prompt key |
|---|---|---|---|---|---|
| ungraded | As shot | C | The photo as shot (the control card; always first, no buttons) | Code | — |
| clean-natural | Clean Natural | C | Neutral, slightly warm, true skin | Code | sat 1.05, con 1.05, +3% warmth |
| teal-orange | Teal & Orange | C | Blockbuster: teal shadows, orange skin, flare | Code | #0f4c5c → #ffb27a, sat 1.15, con 1.15, horizontal flare streak |
| golden | Golden Warmth | C | Honey highlights, soft | Code | #3a2a1a → #ffd08a, sat 1.05, slight bloom |
| moody-matte | Moody Matte | C | Lifted blacks, muted, desaturated greens | Code | blacks lifted to #262626, sat 0.75, con 0.9, greens −30% |
| high-key | High Key | C | Bright, airy, almost white | Code | exposure +0.4, con 0.85, sat 0.9 |
| low-key | Low Key | C | Dark, rich, small pools of light | Code | exposure −0.4, con 1.3, vignette |
| bw-classic | Classic Black & White | C | Clean monochrome | Code | desaturate, con 1.15 |
| noir | Noir | R | Hard black and white, deep blacks | Code | desaturate, con 1.5, crushed blacks, heavy vignette |
| steel-night | Steel Night | R | Cool steel blue night, crisp | Code | #0b1a2e → #cfe0f0, sat 0.8, con 1.2 |
| steel-chile | Steel & Chile | R | Cool steel shadows, chile-red warmth in skin | Code | #13263a → #ff9a6a, sat 1.0, con 1.15 |
| portra | Portra | C | Warm pastel film, fine grain, red halation | Code | #3b3030 → #ffe3cf, sat 0.9, con 0.95, grain, red glow on highlights |
| cinestill | CineStill Night | R | Tungsten film: red halos around lights, cool shadows | Code | #0d1b2a → #ffd2a6, red bloom around bright areas, grain |
| ektachrome | Ektachrome | R | Clean slide film, punchy blues | Code | #10203a → #f6f0e0, sat 1.2, con 1.1, blue boost |
| kodachrome | Kodachrome | R | Rich reds and blues, vintage punch | Code | #1a1f3a → #ffe9c4, sat 1.3, con 1.15 |
| two-strip | Two-Strip Color | F | Early cinema: only red-orange and cyan-green | Code | map to two-color palette #d9573b / #3b9c8f |
| bleach-bypass | Bleach Bypass | R | Silvery, low saturation, high contrast | Code | sat 0.45, con 1.35 |
| faded-matte | Faded Matte | C | Lifted blacks, soft, muted | Code | blacks #2a2a2a, sat 0.75, con 0.85 |
| cross-process | Cross-Process | R | Yellow-green highs, cyan shadows | Code | #003a4a → #f4ff9a, sat 1.25, con 1.25 |
| lomo | Lomo | R | Saturated, dark corners, slightly off color | Code | sat 1.35, con 1.2, strong vignette, slight color shift |
| polaroid | Instant Photo | C | Soft, faded, warm, white frame | Code | #2a2622 → #f7ecd6, sat 0.85, con 0.9, white border |
| disposable-90s | 90s Disposable | R | Direct flash, harsh, grain, date stamp | Code | flash-flat look: con 1.2, sat 1.1, grain, orange date stamp |
| super8 | Super 8 | R | Home movie: warm, grainy, gate weave, rounded corners | Code | #2b1d10 → #ffd9a0, heavy grain, soft blur, rounded frame |
| day-for-night | Day for Night | F | Daylight graded to fake moonlight | Code | exposure −0.8, #061428 → #8fb0d8, sat 0.5 |
| infrared | Infrared | F | White foliage, dark skies | Code | swap red/green channels, luminance boost on greens |
| aerochrome | Aerochrome | F | Infrared film: foliage turns hot pink and red | Code | map greens to #ff3d7f, sky to #4a76ff |
| solarize | Solarize | F | Part-negative, metallic tones | Code | invert tones above 60% |
| negative | Negative | F | Color negative / x-ray | Code | invert, slight blue cast |
| vhs | VHS | R | Camcorder: chroma bleed, scan lines, date stamp | Code | red offset 3 px, scan lines, slight blur, date stamp |
| crt | CRT Screen | F | Old TV: curved glass, RGB phosphor dots | Code | barrel distortion, RGB subpixel mask, glow |
| webcam-2005 | 2005 Webcam | F | Low-res, smeared, over-sharpened | Code | downscale to 320 px, JPEG artifacts, sharpen |
| security-cam | Security Cam | R | CCTV: green-gray, low-res, timestamp, fisheye | Code | sat 0.3, #9fb59a tint, pixelate ~480p, noise, barrel distortion, timestamp |
| night-vision | Night Vision | F | Green phosphor, noise, scope ring | Code | luminance → #0b2b0b..#b6ff9a, noise, circular mask |
| thermal | Thermal | F | False-color heat map | Code | luminance → #1a0033 → #ff00a0 → #ffd000 → #ffffff |
| tintype | Tintype | R | Wet plate: silver-brown, dark blotchy edges | Code | sepia-silver duotone, con 1.3, heavy vignette, edge texture |
| cyanotype | Cyanotype | R | Prussian blue and white print | Code | duotone #0b2a63 → #f4efe6 |
| sepia | Sepia | C | Old brown photograph | Code | sepia tone, con 1.05, slight fade |
| split-pastel | Pastel Split-Tone | R | Pink highlights, mint shadows | Code | #2f5d55 → #ffc9d6, sat 0.9 |
| neon-cyberpunk | Neon Cyberpunk | R | Magenta and cyan neon, wet reflections (often overused) | Image | "magenta and cyan neon light, wet reflections, night" |
| golden-hour | Golden Hour | C | Low sun backlight, rim light, dust | Image | "low backlit sun, warm rim light, dust in the air" |
| tilt-shift | Tilt-Shift Miniature | F | Real scene looks like a toy model | Code | strong blur top and bottom, sat 1.3, con 1.15 |

## Tuning a look to the palette (after Stage 4.4, automatic)

- **Filmed footage:** keep the look's CSS recipe and add one layer over it: `background: linear-gradient(135deg, <pop color>, <second color>); mix-blend-mode: soft-light; opacity: .32`. If the palette is very dark or very saturated, use `.22`. Apply the same layer to the main and backup looks. This is the level written into `look.md`; the creator changes it with "change my color editing" (redo the step with three versions: lighter, as is, stronger).
- **Generated or illustrated channel:** add to the art style's prompt key "limited palette of <background>, <pop color>, <second color>, with <words> for linework or text"; regenerate the sample once only if the creator asks.

## Filters: what each card must show (Stage 4.2)

A filter card is judged by its picture alone, so the picture carries everything that makes the filter recognizable, not just the color. Built in code over the test photos (`footage-filters.json` has every recipe). The ones that need more than a color:

| Filter | What the card must show | Frame |
|---|---|---|
| Movie trailer | Teal-and-orange grade **plus black letterbox bars** top and bottom | any |
| VHS tape | Color bleed, scan lines, a tracking band, **PLAY ▶ and a date/time** in a camcorder font | any |
| Security camera | Green-gray, grainy, slightly soft, vignette, **CAM 01, REC dot, date/time stamp** | any |
| Night vision | Green phosphor, noise, **the binocular mask** (two round openings) | a place |
| Heat map | A real thermal ramp: **blue → purple → red → orange → yellow** on the warm parts (keep the purple) | any |
| Fake night | Deep blue, darker, **lights still glowing** (a bright-pass copy screened on top) | a street or room with lights (`08-street-vlog`) |
| Tiny world | Strong blur top and bottom, boosted color: reads as a toy model | **a high, wide view** (`12-high-street`) |
| Glitch | **Shifted color channels, offset slices, blocky pixels** | the face |
| Noir | Hard black and white, crushed blacks, **venetian-blind shadows**, heavy vignette | any |
| Black & white | Soft, natural gray. Must look clearly gentler than Noir | any |
| 1-bit | **Pure black and white dots, no grays** (dithered) | any |
| Odd colors (cross-process) | Strong: yellow-green highlights, blue shadows. Line in plain words: "For: something strange or dreamy" | any |
| Instant photo | The white instant-photo border, thicker at the bottom | any |
| Home movie | Warm, grainy, **rounded frame corners** | any |
| Newsprint | Halftone dots on newsprint-colored paper | any |
| X-ray | Inverted, blue cast | any |

If two filters look alike on the test photos, make each one distinct or drop one.

## B. Graphic treatments (code)

| Slug | Name | Tier | What it does |
|---|---|---|---|
| duotone | Duotone | C | Two palette colors map dark → light |
| tritone | Tritone | R | Three palette colors |
| halftone | Halftone | R | Dot screen like newsprint |
| posterize | Posterize | R | 4–6 flat color levels |
| outline | Outline | R | Edges only, like a drawing |
| paper | Paper Texture | C | Paper grain over the image |
| grain | Film Grain | C | Fine moving grain |
| light-leak | Light Leak | C | Warm film burn from an edge |
| scanlines | Scan Lines | R | Horizontal CRT lines |
| dither-1bit | 1-Bit Dither | F | Black and white dots only, old-Mac style |
| gameboy | Handheld Green | F | Four shades of green, pixelated |
| pixel-art | Pixel Art | F | Big pixels in a limited palette |
| ascii | ASCII | F | The image rebuilt from text characters |
| mosaic | Mosaic Tiles | F | Small square tiles with grout lines |
| glitch | Glitch | R | RGB split, displaced slices, block noise |
| datamosh | Datamosh | F | Melting, smeared compression artifacts |
| chromatic | Chromatic Aberration | R | Color fringes at edges |

## C. Art styles and scene worlds

Kept as art styles for story beats that can't be filmed (Stage 4.3, a library).

| Slug | Name | Tier | Look | Make | Prompt key |
|---|---|---|---|---|---|
| anime | Anime | C | Cel-shaded figures, painted background | Image | "cel-shaded anime still, painted background" |
| manga | Manga | R | Black ink, screentone dots, speed lines | Image | "black and white manga panel, screentone, speed lines" |
| pop-comic | Pop Comic | C | Ben-Day dots, bold outlines, caption box | Image | "pop-art comic panel, Ben-Day dots, caption box" |
| ink-noir | Ink Noir Comic | R | High-contrast black ink, one spot color | Image | "high-contrast black ink comic, single red spot color" |
| claymation | Claymation | R | Plasticine figures, miniature set | Image | "claymation, plasticine figures, handmade miniature set" |
| needle-felt | Felt | F | Needle-felted wool figures | Image | "needle-felted wool figures and set" |
| toy-bricks | Toy Bricks | F | Built from plastic building bricks (no brand marks) | Image | "built from generic plastic toy bricks, no logos" |
| paper-diorama | Paper Diorama | R | Stacked cardstock layers | Image | "layered paper diorama, cardstock cutouts, soft shadows" |
| papercut | Papercut | R | Flat cut paper silhouettes | Image | "flat papercut illustration, layered colored paper" |
| origami | Origami | F | Everything folded from paper | Image | "everything folded from paper, origami" |
| stop-motion | Stop-Motion Puppets | F | Fabric puppets on a tabletop set | Image | "stop-motion puppet animation still, fabric and wood" |
| low-poly | Low-Poly 3D | R | Faceted 3D shapes | Image | "low-poly 3D render, flat shaded facets" |
| isometric | Isometric | R | Clean 3D diagram from a fixed angle | Image | "isometric 3D illustration, clean" |
| voxel | Voxel | F | Built from little cubes | Image | "voxel art, built from small cubes" |
| clay-3d | Soft 3D | C | Rounded, soft-lit 3D, toy-like | Image | "soft rounded 3D render, toy-like, studio light" |
| watercolor | Watercolor | C | Loose washes, paper texture | Image | "loose watercolor illustration, paper texture" |
| gouache | Gouache Storybook | R | Flat opaque paint, children's-book feel | Image | "gouache storybook illustration" |
| pencil | Pencil Sketch | C | Graphite sketch | Image or Code (edge + shading) | "graphite pencil sketch" |
| charcoal | Charcoal | R | Smudged charcoal drawing | Image | "charcoal drawing, smudged" |
| linocut | Linocut | R | Carved block print, bold lines | Image | "linocut print, bold carved lines, two colors" |
| engraving | Engraving | F | Fine line engraving like old money | Image | "fine line engraving, banknote style, crosshatching" |
| ukiyo-e | Woodblock Print | R | Japanese woodblock print | Image | "ukiyo-e woodblock print style" |
| oil-painting | Oil Painting | R | Classical oil painting, window light | Image | "oil painting, single window light, old master style" |
| fresco | Fresco | F | Faded wall painting, cracked plaster | Image | "Renaissance fresco on cracked plaster" |
| stained-glass | Stained Glass | F | Lead lines and glowing color panes | Image | "stained glass window" |
| pointillism | Pointillism | F | Painted entirely in dots | Image | "pointillist painting, made of dots" |
| art-deco | Art Deco Poster | R | Geometric 1920s travel poster | Image | "Art Deco travel poster" |
| constructivist | Constructivist | F | Bold diagonals, red and black, propaganda-poster energy | Image | "constructivist poster, red and black diagonals" |
| bauhaus | Bauhaus | R | Primary shapes, grid, simple type | Image | "Bauhaus poster, primary colors, geometric shapes" |
| pop-art | Pop Art Grid | R | Repeated portrait in loud color blocks | Code | four-up, each a different flat color duotone |
| risograph | Risograph | R | Three spot inks, misregistered, grainy | Image | "risograph print, three spot colors, misregistration" |
| xerox-zine | Xerox Zine | R | Photocopy, toner specks, tape, marker | Image | "xerox zine page, toner specks, tape, marker caption" |
| blueprint | Blueprint | R | White linework on blue | Image | "technical blueprint drawing, white lines on blue" |
| chalkboard | Chalkboard | R | Chalk drawing on a board | Image | "chalk drawing on a blackboard" |
| scientific | Scientific Plate | F | Old natural-history illustration | Image | "vintage scientific illustration plate, labeled" |
| visual-index | Visual Index | R | Cut-out objects in a numbered grid | Image | "cut-out objects in a grid, numbered labels" |
| micrographics | Micrographics | R | Thin callout lines and labels over the photo | Code | draw callouts and small labels |
| swiss | Swiss Poster | R | Grid poster, one red block | Code | grid layout, red block, cropped photo |
| ransom | Ransom Collage | F | Mismatched cut-out letters over the photo | Code | cut-out letter tiles |
| vaporwave | Vaporwave | F | Pink-teal sunset, grid floor, retro 3D | Image | "vaporwave, pink and teal, grid floor, retro 3D" |
| synthwave | Synthwave | R | Neon sunset, chrome type, night drive | Image | "synthwave neon sunset, chrome, night" |
| y2k-chrome | Y2K Chrome | F | Liquid chrome, bubbles, early-2000s tech | Image | "Y2K liquid chrome aesthetic" |
| holographic | Holographic Foil | F | Rainbow foil sheen | Image or Code (gradient overlay) | "holographic foil sheen" |
| tarot | Tarot Card | F | The scene framed as an illustrated card | Image | "illustrated tarot card, ornate border, title at bottom" |
| trading-card | Trading Card | F | The person as a collectible card with stats | Code | card frame, stat box, foil corner |
| museum | Museum Exhibit | F | The scene as an artifact behind glass with a placard | Image | "museum display, artifact behind glass, placard" |
| newspaper | Newspaper Front Page | R | Halftone photo in an old newspaper layout | Code | halftone + newspaper layout |
| magazine | Magazine Cover | R | The person as a magazine cover | Code | cover layout, masthead, cover lines |
| wanted | Wanted Poster | F | Old west wanted poster | Code or Image | aged paper, woodtype, sepia photo |
| card-border | Illustrated Card Border | R | The photo framed like a folk-art card (often culturally specific; ask) | Code or Image | — |
