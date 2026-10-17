# Motion craft: how and when things move

The brand's motion table decides the eases, timings, transitions and phrase length. This file is the craft that turns that table into good motion. Durations here are scaled for 1080p video; web and UI durations are too short.

## 1. One motion language per video

Write it in the plan before animating: the pack's motion table, plus any change for this video. Reuse it everywhere; consistency reads as confidence, variety reads as noise.

**Fallback rows** (only when the brand file leaves the motion table open; the brand's table always wins):

| Feel | Entrance | Exit | On-screen move | Overshoot | Base unit | Stagger | Default transitions | Hold |
|---|---|---|---|---|---|---|---|---|
| Snap | `expo.out` | `power2.in` | `power3.inOut` | 0 | 0.35 s | 50 ms | hard cut on the beat | ≥ 0.3 s |
| Glide | `power2.out` | `power2.in` | `power2.inOut` | 0; scale 0.98 → 1 | 0.5 s | 80 ms | hard cut, soft rise, dissolve | ≥ 0.5 s |
| Deadpan | `power3.out` + `steps(n)` text | `power2.in` | `power3.inOut` | 0 | 0.4 s | 60 ms | hard cut, match cut | ≥ 0.6 s |
| Punch | `expo.out` | `power3.in` | `power4.inOut` | 0–small | 0.3 s | 40 ms | cut on action, crash zoom | ≥ 0.25 s |
| Drift | `sine.out` | `sine.in` | `sine.inOut` | 0 | 0.8 s | 120 ms | dissolve, slow push | ≥ 0.8 s |
| Mechanical | `steps(n)` / `power1.inOut` | `power1.in` | `power1.inOut` | 0 | 0.4 s | 60 ms | slide, wipe, counter roll | ≥ 0.4 s |
| Handmade | `steps(3)` then `back.out(1.4)`, 12 fps on twos | hard cut | `steps(n)` / `power1.inOut` | small (back.out) | 0.25 s | 60 ms | hard cut, freeze + record scratch, whip pan | ≥ 0.5 s |

GSAP names: power1 = quad, power2 = cubic, power3 = quart, power4 = quint. Cubic-bezier strings need CustomEase, so prefer the names. Two eases do 90% of the work: one out (entrances), one in (exits). A third must justify itself. Never use `linear`/`none` on anything moving through space; keep it for ambient loops, progress bars and camera drift.

## 2. Timing

- Exits run at 65–75% of the entrance duration (fast out, deliberate in).
- Duration grows with distance: `duration ≈ base × √(distance / base distance)` (0.4 s at 200 px → 0.8 s at 800 px). Same easing for a big and a small element, different duration.
- Stagger math: `(count − 1) × offset + item duration` stays under ~0.8 s. For more items, shrink the offset or stagger outward from the focal point.
- Key text stays on screen at least 0.3 s per word after it lands.

## 3. Three layers, one hero

Every scene has:
- **Hero:** the one thing it's about. The boldest, most-eased move, landing on the beat.
- **Support:** smaller and faster, and it gets out of the way.
- **Texture:** grain, ghost type, drift. Slow loops at ≤ 20% of the hero's energy, never hard cuts.

If two things compete for the eye in one frame, demote one. Attention order inside a scene: the line first, then the main object, then details; never the reverse.

## 4. Anticipation and follow-through

A big hit gets a 60–120 ms wind-up or a held beat before it. Attached parts (shadow, label, underline, caption) settle 40–80 ms after the hero, as a cascade, not on the same frame. Organic moves follow a slight arc, not a straight line.

## 5. The two one-third rules

- Nothing travels more than a third of the screen without a stop, a scale change or a direction change.
- With 3+ elements in play, no more than a third move at once; element 1 settles as element 3 starts.

## 6. Camera

- **No lazy breathing or slow drift.** A hold stays alive through steps with a reason (a push to the word being said, a focus shift, the next element landing), not through a constant slow zoom. On talking-head footage a gentle push across a whole line is fine when the brand's motion table asks for it.
- **Shot sizes change on purpose.** When one element is telling the story (a click, a number, a word), push to it (1.4–2.2× over 0.6–0.9 s, `power3.inOut`), then pull back when the composition needs the whole frame. A few-percent breathing zoom does not count as a shot change.
- **Parallax by depth:** foreground 1.0×, mid 0.5×, background 0.2× displacement. A small counter-motion in the background (20–30% of the hero's move, opposite direction) adds weight.
- Never move the world so far that its edge shows. No preset-style spin or zoom-plus-blur on every cut.

## 7. Rhythm and the music grid

- Ask for an exact BPM in every music prompt. `frames_per_beat = (60 / BPM) × fps`. Find beat 1's offset in the file (the first strong onset) and round each *cumulative* beat to a frame, so cuts don't drift.
- Structural changes land on the beat. Scene changes land on phrases of the brand's phrase length (usually 8 beats long-form, 4 vertical, tightening toward the climax). Small accents land on the half-beat. Never cut on every beat.
- **Energy arc (long videos):** establish (long holds) → develop (shots shorten) → climax (fastest changes, the biggest visual on the music's drop) → resolve (one long hold). Uniform pacing reads flat. A Short has no build-up: it peaks at the hook and the last line, with each shot sized for its job (`shorts/build.md` "Pace").
- One "wow" moment per piece; a second one cancels the first. Silence and stillness before a big line are tools.
- Once there's a voice, it's the grid: retime beats to the words first, then nudge hits onto the nearest music beat.

## 8. Transitions with a reason

- The hard cut is the default for most brands (around 90% of cuts). Cut on action: mid-move, while velocity is high, not after things settle.
- **Match cut** (outgoing and incoming share a shape, position or motion direction): the strongest transition. Plan 1–2 per video.
- **Object wipe:** an element passes close to the lens and the scene changes behind it.
- **With footage and voice:** J-cut (the next scene's sound starts 4–12 frames early) and L-cut (sound trails 12–24 frames).
- Never the same transition twice in a row. Dissolves don't fix bad timing.
- Only transitions the brand allows; reserved ones stay with their component.

## 9. Anti-slideshow test

Screenshot any frame and ask:
- Could this be a corporate slide without changes? Rebuild it.
- Does the eye know where to look within 0.2 s? If not, remove elements.
- Is something moving because the camera moves, not only because elements animate themselves? Required at every transition.
- One shot, one statement: at most 2 text sizes per scene, and on-screen claims of 6 words or fewer. Longer: split into two beats or make it visual (an icon, a number, a real screen).
- Separate scenes switched on and off read as a deck. A camera and a hero that carry across scenes make it one film.

## 10. Text

Placement, margins, line length and size tiers: `craft/layout.md`. The minimums below are the floor.

- Nothing under 28 px on 16:9 at 1080p (phones watch YouTube). On 9:16 at 1080×1920: at least 44 / 34 / 30 px for headline / body / label.
- Check that long one-line headlines fit the frame in the pack's headline font, at its real width.
- Never loop-animate text the viewer is still reading.
