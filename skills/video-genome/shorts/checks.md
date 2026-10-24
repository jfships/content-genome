# Short checks

Log every gate in `_review/review-log.md`, as in `review/checks.md`.

**These run on every draft built from real footage, from the first one, not only the final.** Gates 3 and 4 (the technical review) come before the creator sees any render. Before sending, also listen through the ending and diff the transcript of the last 10 s against the captions: whose voice is under which line, levels between speakers, any duplicated or missing line.

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

- [ ] A still of every beat at 1080×1920 with the safe box (x 65–930, y 250–1500) and each platform's overlay drawn on; nothing important underneath.
- [ ] Frame 1 still: is it interesting with the sound off? Is the hook text there?
- [ ] Captions match the brand's caption spec on the first draft, not only the final: every chunk in the spec's case and centered on its x (`tools/tech_review.py --case <spec case> --center <spec x>` with caption boxes), and no spoken stretch without a caption unless its beat has `captions_off` with a reason.
- [ ] `tools/draft_checks.py` clean on every draft (`review/checks.md` gate 4): lips above the bottom line on every frame, no blank flashes, no word ending clipped over 30 ms, no move out of delivery before a cut, angle changes on sentence boundaries, overlays clear of the face through their whole animation. Every linger sheet looked at.
- [ ] Captions and hook text never collide with each other or the face; every beat sits in its named layout's boxes (`build.md` "Layouts"), checked with `tools/tech_review.py` run on `work/beats.json` (the beat brief as JSON, see `review/checks.md` gate 4) before any render.
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

## Short gate 4: Technical review

Same as `review/checks.md` gate 4, at 1080×1920: the builder's own look check is the beat brief self-check (`craft/graphic-jobs.md`), never a score; then a separate agent that didn't build it runs the technical review with `tools/tech_review.py` on the render, `words_out.json`, `work/shots.json`, the caption file and `work/beats.json`, plus by eye on the contact sheet (1 frame a second), the strips and the 360 px phone view. Vertical specifics: the safe box x 65–930, y 250–1500 and each platform's overlay; the named layout per beat and its boxes (`build.md` "Layouts"), with no layout on two consecutive beats unless the hold is in the brief; hook text on from frame 1 for 2 s; the loop seam; every word readable at 360 px; the last 10 s diffed against the captions.

Output is a pass/fail list with times and fixes. Nothing reaches the creator with an open item. Log it in `_review/review-log.md`.

**Show the creator** the render with the one-line result and the beat page (clip cards for beats that move), and say plainly that sound was metered, not heard. Taste questions go to the creator on rendered clip cards, never stills, never scores.
