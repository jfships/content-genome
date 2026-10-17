# Short checks

Log every gate in `_review/review-log.md`, as in `review/checks.md`.

**These run on every draft built from real footage, from the first one, not only the final.** Gates 3 and 4 and the fresh reviewer come before the creator sees any render. Before sending, also listen through the ending and diff the transcript of the last 10 s against the captions: whose voice is under which line, levels between speakers, any duplicated or missing line.

## Short gate 1: plan (before asking for approval)

- [ ] **Stranger test:** someone who never saw the long video gets the point and gets value from this Short alone. Pass or fail, with one line of why. A fail is rejected, not patched.
- [ ] One idea; the message is one sentence of 12 words or fewer.
- [ ] Exactly one shape named.
- [ ] Hook written word for word on three layers (first frame, spoken line, 3–7 words of hook text), all landing in the first 1–2 s; frame 1 makes sense with no context; the creator or their real material is on screen in the opening.
- [ ] Script word count within the budget for the target length (~42 words per 15 s at the default pace).
- [ ] First payoff by 3 s; call-and-response 4 exchanges or fewer.
- [ ] Last line written word for word; no outro, subscribe ask, end card or sting.
- [ ] Goal and ending per platform; send reason written.
- [ ] Source is "written for vertical" or passes the stranger test; nothing is planned as a crop of the long edit.
- [ ] Truth, rights, disclosure and paid generation as in `review/checks.md` gate 1.

## Direction gate (S2b, before the first rough build)

- [ ] Both direction pages are decided and Main and Backup are saved in `plan.md`; every still came from real material, not stand-ins.

## Short gate 2: build (on stills)

- [ ] A still of every beat at 1080×1920 with the safe box (x 65–930, y 250–1450) and each platform's overlay drawn on; nothing important underneath.
- [ ] Frame 1 still: is it interesting with the sound off? Is the hook text there?
- [ ] Captions and hook text never collide with each other or the face.
- [ ] Brand check (`tools/brand_check.py`) and the layout still check (`craft/layout.md` §3).
- [ ] No sting, sound logo, end card or name tag; the backdrop is tall, not a crop.

## Timing numbers (before the render is reviewed)

Run on the cut's word times:
```
python3 $SKILL/tools/short_timing.py work/words_out.json --length 30 --payoff 2.4 \
  --pace 2.6-3.0 --cuts work/shots.json --ceiling 2.5
```
`--pace` and `--ceiling` come from the Brand Genome's vertical row (defaults 2.6–3.0 words a second and 2.5 s). `--cuts` is the shot list of the built Short: a JSON list of shot start times in seconds, or of `[start, end]` pairs; write it from the composition's timeline (each shot's start time).
`--payoff` is the time of the first laugh, twist or result. It prints the spoken pace (words a second) and the speed-up needed to reach the target, every shot over the ceiling, every gap over 0.6 s with its time, the seconds to the first payoff, the word count against the budget for the length, and FIX on any number outside the rules in `build.md` "Pace". A planned deadpan hold is listed with `--hold <time>` so it isn't flagged. Fix every FIX, or write in `log.md` why it stays.

## Short gate 3: render

Same five views as `review/checks.md` gate 3, at 1080×1920, plus:
- [ ] The phone view at 360 px wide: every word reads.
- [ ] Loop check (when the ending loops): play the file 3 times back to back (`ffmpeg -stream_loop 2`); the seam doesn't jump in picture, sound or captions.
- [ ] Duration within the planned length; debt is zero.

## Short gate 4: scored review

Score each 1–10 as a harsh short-form editor scrolling a feed, not as the author:
1. **Stops the scroll:** frame 1 and the first 2 s would stop a stranger.
2. **Stays:** nothing makes a stranger swipe; first payoff by 3 s; no dead air.
3. **One clear message:** a stranger could say what it was about in one sentence.
4. **Pace:** the timing numbers pass; every shot is sized for its job and none passes the ceiling without a reason (`build.md` "Pace"); holds earn their place.
5. **Ending:** the last line lands, or the loop is seamless.
6. **Send-worthy:** someone would send it to a friend.
7. **Phone readability and layout:** safe box, sizes, no collisions.
8. **Brand:** caption and hook-text style, palette, fonts, motion, house rules.
9. **Sound:** voice clear, music under it, SFX on the frame.

List the 3 worst problems with times, fix, recheck, repeat until every score is 8+. Stop and report if two rounds don't raise the lowest score.

**Then a fresh reviewer** that didn't build it gets only: the render's contact sheet (1 frame a second), the phone view, the transcript with word times, the timing numbers, the message line, the hook and the last line, and the brand's personality and vertical rules. It scores the same 9 points cold and names the 3 worst problems. Where its score is 2+ points below yours, treat its view as right unless you can show it's wrong.

**Show the creator** the render with one line of scores, and say plainly that sound was metered, not heard.
