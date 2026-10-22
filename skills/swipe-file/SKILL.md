---
name: swipe-file
description: Turn short videos a creator saved (Reels, TikToks, Shorts) into a swipe library that records which part they liked, in their own words, so idea-genome and video-genome borrow only what they flagged. Downloads the saves, transcribes them, pulls stills, builds a phone-first review page, reads the taps back and writes library entries plus a closings bank. Use when someone says "review my saves", "swipe file", "I saved some Reels", or drops video links to learn from.
---

# swipe-file: saves → what they liked → a library the other skills read

*swipe-file by jfships · [youtube.com/@jfships_ai](https://youtube.com/@jfships_ai) · free (MIT)*

A save has no fixed use. **Never assume why something was saved.** Every save gets two questions first, then only the matching cards:

1. **What's it for?** (pick all that fit)
   - **Craft:** get better at making content (hook rules, retention, captions). Becomes a standing rule in the banks that every video applies.
   - **Idea:** a format or topic to redo in their own voice. Goes to idea-genome as a candidate in `idea-bank.md`, with the save as its source.
   - **Tools:** "make our tools do this" (an effect, a workflow, a picker). Goes to the next skill-improvement handoff, not to idea work.
   - **Just liked it:** a short entry, nothing routed.
2. **What did you like?** The ideas and script, the visuals, both, or neither.

## Setup (once per brand)

Copy `templates/swipe-config.md` to `<brand>/00 Decisions/swipe-config.md` and fill it in. It holds everything private: the drop folder, the reviewed folder, the work folder, the library path and the review page link. Never put those values in this skill.

Capture that works: the phone's share sheet saves the video link as a small text file into a cloud-synced folder (for example Google Drive for desktop). On the computer, `tools/swipe_pull.ps1` reads that folder. Give the creator a double-click `.bat` that runs it with their paths (`templates/swipe-pull.bat`).

Needs on the computer: `yt-dlp` and `ffmpeg` (winget), Python with `faster-whisper` and `pillow`.

## Flow

| Step | Who | What |
|---|---|---|
| 1. Pull | Creator double-clicks the `.bat` | Downloads each saved link to `<work>/<id>/video.mp4` plus `video.info.json`, writes `<work>/batch.json`. Public videos only, no login. A failure is one line in the report and its link stays in the drop folder. |
| 2. Prep | Claude | `python tools/swipe_prep.py <work>`: `transcript.txt`, stills every 2 s, `contact.jpg`, `prep.json` per save. Mechanical; any model. |
| 3. Cards | Claude | Read each save's `transcript.txt`, `contact.jpg` and `prep.json`; write `<work>/<id>/cards.json` (see Cards). |
| 4. Page | Claude | `python tools/build_review.py <work>` → `<work>/review.html`. Publish it to the review page link in the config (read it first in a new session; keep its `db` capability). Send the link. |
| 5. Taps | Creator | Answers on the phone. Each save opens with step 1; idea cards and visual cards appear only for what they picked. |
| 6. Read back | Claude | When they say done: read collection `taps` (docs `<id>~<card>`, `<id>~_purpose`, `<id>~_mode`, `<id>~_why`). Untapped saves stay in the drop folder for the next batch. |
| 7. Library | Claude | Write one entry per answered save (format below), route it by what it's for (below), update the banks, then move its link file(s) from the drop folder to the reviewed folder and delete `video.mp4` (the link is the source; transcript and stills stay). |

Batch size: whatever is in the drop folder, usually 3–4. One page per batch, one section per save.

## Cards (`cards.json`)

```json
{"title": "5 ways to make people watch longer",
 "gist": "One line: what the video is and how it's made.",
 "content": [{"id": "c1", "tag": "Rule 1", "title": "Short name of the idea", "line": "“Exact quote from the transcript.”", "gist": "What it means, and a link to an earlier save if it repeats one."}],
 "visual": [{"id": "v1", "tag": "Opening", "title": "Short name of the device", "line": "“What is said over it.”", "vis": "What is on screen, plainly.", "t": [0, 2]}]}
```

- **Content cards:** one per idea the video teaches or uses, quoted word for word (fix obvious mishearings and say so in the gist). Always end with a **Closing** card for the last 3–5 seconds.
- **Visual cards:** one per distinct on-screen device, not per shot. `t` is seconds; the page shows the nearest stills. End with the closing's visual.
- A video with no speech gets visual cards only; a talking head with nothing visual gets content cards only. A card list may be empty; the page hides it.
- Every card tag is something true about the video (Rule 2, Opening, Chapter cards), never a decoration.

## Library entry (`swipe-library.md`)

```
## NNN - <title> (<platform>, <length>) - <id>
Source: <link> - Reviewed <date>
For: CRAFT / IDEA / TOOLS / LIKED (all that apply)
Lane: CONTENT / VISUAL / BOTH / NEITHER. "<their why, word for word>"
- <card title>: <their taps in words>. <their note, word for word>
Borrowable: <only what they flagged>.
Not borrowed: <what they marked "nothing here", if it teaches something>.
```

Their words are quoted, never paraphrased into something stronger. A save answered "neither" still gets a two-line entry. If they skipped the taps and only talked, record what they said and write "Per-item taps: not given."

## Banks (bottom of the library)

- **Closings bank:** every save's closing card, tagged by kind (comment-a-word, follow-for-more, slogan, loop to line 1…). Fill it from every save, tapped or not; mark which ones they liked.
- **Script tools:** devices from saves marked content or both (but/therefore, compare, open loops…), each with the entries it came from.
- **Visual devices:** only from saves marked visual or both.
- When a pattern repeats across saves, note it once under "Patterns" and ask the creator to confirm it before it becomes a rule.

## How the other skills use it

- **Craft** entries and the banks: video-genome (script) and idea-genome (develop) read the ones matching the video's type and apply only what the creator flagged.
- **Idea** entries: added to `idea-bank.md` as `raw` candidates when the entry is written, with the save linked; idea-genome develops them like any other idea, in the creator's voice.
- **Tools** entries: listed under "Tools queue" at the bottom of the library and copied into the next skill-improvement handoff. The skills don't read them during a video.
- For a fast montage of effects, prep with `--step 0.5` so each effect gets a still. They borrow only what the creator flagged. Hand a model the matching entries, never the whole library.

## Rules

- Download public videos only. Never sign in to a platform without the creator's explicit go-ahead: signed-in bulk downloads can get their account restricted.
- The review page opens with something real (the first save's title, stills and step 1), never an empty shell. Phone first.
- Show a finished page, never a description of one.
- Nothing personal in this skill's files: paths, folder ids and links live in the brand's `swipe-config.md`.

## Credit line

swipe-file by jfships. Free under MIT.
