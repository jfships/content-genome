# Short platforms: files, covers, endings, music, results

Rules change; check each platform's current limits before delivery and say what changed.

## One clean file per platform

- 1080×1920, the brand's frame rate, master at −14 LUFS.
- One master per platform, never one file cross-posted: no other app's watermark (Instagram doesn't recommend Reels carrying another app's logo; the creator's own logo is fine).
- Each file gets its own caption text, cover, hashtags or keywords, and its own ending or call to action.
- Name: `<handle>-<ep or sh>-s<n>-<platform>.mp4`, versioned (`-v2`).

## Per platform

| | YouTube Shorts | Instagram Reels | TikTok |
|---|---|---|---|
| Length | 20–45 s default (max 3 min) | 20–60 s default (max 3 min) | 25–45 s; 61–75 s only for Creator Rewards |
| Ranked on | Viewed vs swiped away; a separate recommender from long videos | Watch time, likes, and sends (sends matter most for reaching non-followers); skip rate in the first 3 s | Watch time, completion, shares |
| Goal and ending | Feeds a long video: set the Related video link to it in the upload | Reach on its own: call to action only as on-screen text over the last line (e.g. "comment TOOLS"), never an end card | As the brand says |
| Sound | Clean master | Clean master | Trending sound allowed, added in the app, low under the voice |
| Cover | Custom Shorts thumbnail (desktop upload); cover text in the middle band | The grid shows a centered 3:4 crop (y 240–1680 survive): cover text inside y 400–1300 | Cover frame picked in the app |
| Testing | — | Trial Reels go to non-followers first | — |

## Covers

A cover's job is the click from the profile grid and from YouTube's Shorts shelf, where the video doesn't play. Built after the final cut, from what was actually said. Build it with the thumbnails skill (its 9:16 cover layout) when installed, else `craft/thumbnails.md` and `tools/thumb_text.py`; the steps below decide what goes in.

1. **Frame candidates, measured, not eyeballed.** Scan the final cut for frames where the face is whole and calm, and rank them on numbers:
   - mouth closed (lip gap small against face height, from the face landmarker `tools/draft_checks.py` uses);
   - calm: eyes open, not mid-blink or mid-word, head level;
   - sharp: highest sharpness (variance of the Laplacian) among neighbors, no motion blur;
   - whole face: every face point inside the frame and clear of overlays, with room above the head for words.
   Offer the top 3 as stills with their times.
2. **Cover styles by stock id:** 2–3 from COV-01..08 (`craft/stock.md`), ranked for this video, with the brand's kept cover style first when it has one. A series keeps its layout (COV-06).
3. **Words chosen for this video and the cover's job:** 3–5 words that make a stranger on the grid want this one. They may repeat the title or the hook when that is the strongest line for the job; that is a choice with a reason, never the default.
4. **Lay out the full 1080×1920:** whole face, even spacing, nothing in the bottom zone (y > 1500); the cover line inside y 400–1300.
5. **3:4 grid crop:** draw the centered crop (y 240–1680 survive) on every option; the face and the words must read inside it.
6. **Feed-size check:** each option at phone grid size in a 3×3 grid beside the brand's recent covers or others in the niche. The subject is clear and the words read.

Options go to the creator on one page (frame × style × words, the crop drawn); they pick. Record the stock id, frame time and words picked in `log.md`.

## Music rights

- Only the creator's kit, generated music, or tracks licensed for the platform. Never commercial songs in the masters.
- YouTube: a Short over 60 s with any Content ID claim is blocked worldwide. Anything over 60 s uses the creator's own, generated or royalty-free music. Shorts Audio Library tracks have 30, 60 or 90 s limits.
- TikTok: a trending sound is added in the app at upload, not baked into the master.

## Don't

- Don't delete and re-upload an underperforming Short (YouTube may treat it as spam). Learn from it in the results log instead.
- Don't add a subscribe ask, end card or outro.

## Results

When each platform file goes live, hand its row fields to growth-genome, which writes `03 Videos/results-log.md` (`learn/results-log.md`; never write the log yourself while growth-genome is installed). Judge against the creator's own channel, not online benchmarks. Views on YouTube Shorts count every start and replay since March 2025, so compare viewed-vs-swiped and average % viewed, not raw views.
