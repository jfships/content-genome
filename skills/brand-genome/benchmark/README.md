# Benchmark photos

Test photos that ship with the skill, so every look round (Stage 4) works out of the box, for free, with no image tool. They were made once and never change, so every creator judges looks on the same frames.

**Tell the creator what they are, every time they appear:** "These are test photos so you can compare. They won't be in your videos."

## Why these frames

Each one is a frame a real creator would actually post: a real place, real light, something happening. Flat stock photos make every filter look the same; these show where a look breaks (skin under a warm grade, blown windows, dark rooms, neon, motion).

## Picking frames for a creator

A footage-look card shows the same look on **3 frames: a face, hands at work, a place.** Pick the 3 that are closest to the creator's own field from the table (a cook gets the kitchen; a coach gets the trail; a gamer gets the night desk). Use the two vertical frames for Shorts, Reels and TikTok rounds. When nothing fits, default to 01, 06 and 09.

## The set

| File | Frame | Who'd film this | Scene | What it tests |
|---|---|---|---|---|
| `01-desk-talking.jpg` | 16:9 | Most talking-head channels | Woman talking to camera at a home-office desk, shelves and plants, window light | The default creator frame: skin, mixed daylight and lamp, lower thirds |
| `02-kitchen.jpg` | 16:9 | Food | Man plating over a steaming pan, pendant light plus window | Warm/cool mix, steam, food color |
| `03-workshop.jpg` | 16:9 | Makers, DIY, trades | Woman sanding at a bench, work lamp, pegboard, sawdust | Single hard lamp, dust in the air, browns |
| `04-trail-run.jpg` | 16:9 | Fitness, outdoors | Man running a dirt trail, hard midday sun, hills | Harsh sun, skies, saturation, motion blur |
| `05-vanity.jpg` | 16:9 | Beauty, lifestyle | Woman at a bedroom vanity, ring light, products blurred | Ring-light skin, soft pastels, bokeh |
| `06-shop-counter.jpg` | 16:9 | Small business, local | Owner behind a café counter, customers blurred behind, tungsten plus storefront daylight | Interiors, warm bulbs vs. daylight, depth |
| `07-gaming-night.jpg` | 16:9 | Gaming, tech | Young man at a desk at night, purple-blue glow, monitor seen from behind | Deep shadows, colored light, crushed blacks |
| `08-street-vlog.jpg` | 16:9 | Travel, vlog | Woman vlogging at arm's length on a busy street at dusk, city lights behind | Dusk, neon bokeh, handheld feel |
| `09-podcast-two.jpg` | 16:9 | Interviews, podcasts | Two people at mics, laughing, brick wall and floor lamp | Two faces, warm lamp plus window |
| `10-car-vertical.jpg` | 9:16 | Anyone making Shorts/Reels | Woman talking to her phone from a parked car, late sun | Vertical talking head, captions, safe zones |
| `11-skate-vertical.jpg` | 9:16 | Action, sport | Skater mid-air at a skate park, overcast | Vertical motion, gray skies, cover frames |
| `12-high-street.jpg` | 16:9 | (filters only) | A sunny city street seen from a tall building | The "tiny world" filter, which only reads on a high, wide view |

People across the set differ in age, gender and skin tone. Clothing is plain, no logos or prints.

## What every photo avoids

Things generators get wrong and filters exaggerate: readable text (signs, screens, labels), logos and brands, fingers in sharp focus, anyone who looks like a real person. If a photo turns out to have one of these, regenerate it; never ship a known flaw.

## Pre-made looks

`looks/` holds the 43 art-style looks from `../catalog/looks.md` that need an image tool, each made once on the same frame (a man at a desk, from the first photo set) and named by its catalog slug. Voting pages use these directly, so a creator with no image tool still sees every look. Code-made looks (color looks, treatments) are applied live to any benchmark photo.

## Backdrop scenes

`backdrops/` holds 20 empty scenes for the backdrops page (Stage 4.8), so every backdrop looks like the real thing behind a person: city at night, chalkboard, cork board, blueprint, space, weather map, news desk, courtroom, game show, award stage, the moon, a fish tank, a giant's kitchen, a crime scene, a cereal box, and the "You as…" sets (president's office, cockpit, baseball stadium, detective's office, winners' podium). No people, no readable text, no logos, no real seals.

## Break-from-reality cutaways

`bfr/` holds the middle panel of each break-from-reality strip (Stage 4.10), made once from the face test photo.

## Rules

- These photos are for exploration only. They never appear in a creator's videos, thumbnails or profiles.
- `generation-log.md` records the tool, model, prompt and date for each file.
- The first set (11 flat stock-style photos, Oct 8 2026) is kept in the project's `_archive/`, not in the skill.
