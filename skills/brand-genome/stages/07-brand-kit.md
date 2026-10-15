# Stage 7: Brand kit

Options for every round: `../catalog/kit.md`, common through funky. Every page is built from `../page-template/` with the words in `../voting-pages.md`. Nine steps, in order (`../page-template/journey.json`): wordmark, name tag, series tag, sting, sound logo, ways to close a video, thumbnail layouts, profile picture, banner; each with a stage-doc update. Required: name tag, sting, sound logo; the rest can be skipped (each skip has a default). Everything is shown in the brand's colors, fonts and motion language. Every piece with real options uses the shared finalist flow (finalists → Main / Backup / Alternative / Discard; `../voting-pages.md`). Open the stage with its plain hand-off (what it is, nine steps, about 20 minutes, nothing happens without their say, they can stop anytime).

## First: how each piece gets made (the first place tools come up)

Everything here has a free path, and the free path is the default. Before the first page, say so in one line and ask one question: "Each piece of your kit can be drawn in code for free. For the sound pieces (the sting and sound logo), I can also use a sound tool if you have one connected. Free is fine for most channels. Which do you want?" Options: *Free, drawn in code* · *I have a sound tool connected (name it)* · *Let me connect one first*.
- Free path: wordmark, tags, endings, thumbnails, profile picture and banner are drawn in code; the sting is CSS/GSAP motion with a Web Audio sound; the sound logo is synthesized in Web Audio. Nothing is generated.
- With a tool: say what it would make and the cost from the tool's own price check before each run, never from memory. Each paid run is approved on the spot.
- Never ask the creator to connect a tool to finish the stage.

1. **Wordmark** (fixed, skippable), two pages: `wordmark-tiles.json` → `wordmark-pick.json`. ~12 clearly different wordmarks, designed lettering in the creator's font set and palette (never generic text in a box), each shown where it lives: a closing card, the profile picture and the corner of a video. Look for a built-in device that says something about the channel (an episode-number pill that changes every video). Quality bar: each one should look like a real channel's logo. Skipped → the name in the title font.

2. **Name tag** (fixed), two pages: `name-tag-tiles.json` → `name-tag-pick.json`. The little tag with their name (and handle or trade) when they first speak. 10–12 styles in the locked palette, fonts and text style, over the face frame, in the clear space beside the speaker. The name tag is personal: it shows the creator's own name. Never on Shorts (it would land on frame 1, over the hook).

2b. **Lockup details and corner mark**, in chat. Derive the handle form (with @) and how the wordmark and name tag sit together; show them as two lines and confirm once (AskUserQuestion: Keep / Change). The corner mark is off by default (platforms have their own watermark); turn it on only if they ask, ~5 s at the start and at chapters, never permanently.

3. **Series tag** (fixed, skippable), two pages: `series-tag-tiles.json` (12 styles over the face frame, in the clear space beside the speaker) → `series-tag-pick.json`. The episode number always sits on its own line, above or below the series name (one line rarely fits). The page says when it appears: once, ~4 s, after the sting, over the first spoken line. On Shorts only as "Part N" for series formats, folded into the hook text (or a small tag right after the hook), never before the hook (Stage 8). Lead with what a new viewer cares about: the series or format name (Stage 3) + episode; ask before making the creator's name the headline. Skipped → none.

4. **Sting** (fixed), two pages: `sting-tiles.json` → `sting-pick.json`. The page line explains it plainly: "Your sting is a 1–2 second branded opener, a tiny intro with your name and sound. It plays right after your hook, about 10–20 seconds in, in long videos only; never on Shorts." The first card ("Where your sting plays") shows hook → sting → video on a timeline. 12+ openers built from the wordmark and the motion feel, each with its sound, one big play/pause. A redo keeps the creator's combined idea as a new option **and** adds fresh ones, so a redo never shrinks to a handful.

5. **Sound logo** (fixed), two pages: `sound-logo-tiles.json` → `sound-logo-pick.json`. 12 short note patterns, each **played right after the creator's own Main sting** (set `window.BG_CHOSEN_STING` in `head` to that sting's sound; never the example's), so it's judged in place. Render the pick to WAV with OfflineAudioContext (48 kHz, peak −1 dBFS); the final note lands on the sting's last frame.

6. **Ways to close a video** (library, skippable). `close-out.json`: ~16 endings for the last 5–10 s of a long video (next video, two-video grid, subscribe + one video, centered minimal, hand-drawn arrow, credits roll, loop back to the hook, freeze-frame sign-off, blooper tag, one-line sign-off, question for the comments, next-episode teaser, series progress, fade to color, split screen, pinned-comment pointer). Keep in library / Discard; each long video picks one. Long videos only: end cards and close-outs never go on a Short. Shorts end on a payoff or a loop line, from the Short endings in Stage 8 (loop line, cut on the payoff, deadpan hold, button line). Skipped → a simple closing card (wordmark + next video).

7. **Thumbnail layouts** (library, skippable). ~8–12 layouts as tiles, shown at real feed size with a sample title, among neighboring thumbnails; tap to see full size. Keep in library / Discard. Expect several (screen + face, before/after, a milestone frame, a one-word frame); the video skill picks per video. Keep text clear of the face and of the platform's timestamp corner. Every tile is mocked with the thumbnail text spec below. Shorts covers are built tall from these in Stage 8. Skipped → one default layout.

   **Thumbnail text spec** (stated once in chat, never asked; written into `brand-kit.md` with the layouts). From real rejected rounds (approved 2026-10-15). Numbers at 1280×720.
   - **Taste (the brand's own; change through `../revisit.md`):** the font family, the colors, the outline. Defaults: the title font; the words color, with the loud element in the pop color; a white outline on the cutout.
   - **Craft (fixed for every brand, never asked):**
     - one font family; lines in the same group share one size; at most 3 size steps (context, main, hook), with only one loud element
     - 3–5 loud words; the rest is context
     - the hook names the topic for the target viewer; a pure reaction line ("Zero clue") doesn't say why to click
     - the main text is at least 15–20% of the frame height
     - the block is vertically centered on the face, left-aligned 50–60 px in from the edge, clear of the face and the bottom-right timestamp
     - loud lines fit to one shared ink width, so the right edges line up (one solid block, not a list); a small lead-in line may stay narrower
     - one fixed gap for the whole block (~26 px), from each line's baseline to the next line's top ink; descenders don't count; never scaled by font size
     - a small crisp shadow (about 3/5 px offset, 2.5 px blur), never a big soft one
     - start from the creator's best real expression (clean cutout + the brand's outline) and write the words backwards from it
     - check at 168×94 beside other thumbnails; verify the spacing by measuring the ink, not by eye
   - **Title after thumbnail:** each video's title is written after its thumbnail is locked, and never repeats the thumbnail's words.

## Profile picture and banner (last two kit steps, both skippable)

A new viewer judges the channel in about three seconds from the profile page. **Check current specs live** before building (image sizes, safe areas, character limits, highlight cover size). Starting points (Oct 2026):
- YouTube banner: 2560×1440, with text and logos inside the center 1235×338.
- YouTube profile picture: 800×800, shown as a small circle.
- Instagram profile picture: shown as a small circle (upload at least 320×320).
- Instagram highlight covers: 1080×1920, with the icon inside a center circle.

Show everything in context: a drawn mock of the real profile page, at desktop and phone size.

**Accounts they're keeping (Stage 0):** start from what's there. Ask for a screenshot or the handle, show the current picture, banner and bio as the first option on each page ("What you have now"), and propose updates next to it. Followers notice a sudden full rebrand; a kept account usually wants its picture kept and its banner and bio refreshed.

**How pictures get made:** the free path first. A profile picture is a photo they take (give them the shot list: plain background, face filling the circle, their colors in the clothing) or the wordmark drawn in code; banners are drawn in code. Only if they ask for a generated picture does an image tool come up, with its cost from the tool's own price check.

Options: `../catalog/kit.md` (profile pictures, banners).

- **Profile picture: ask first.** "Will your profile picture be a photo of you?" (*Yes* · *No* · *Not sure, show me both*)
  - **Yes** → no page; give 2–3 tips (tight crop, plain background, face fills the circle), add the profile photo to `PHOTOS-OWED.md` (file name `06 Profiles/profile-photo-1.jpg`) and, once they share it, show it in the mock channel page.
  - **No** → `profile-picture-tiles.json` with the logo options only (monogram, wordmark, seal, silhouette…).
  - **Not sure** → the same page with both groups: photo styles (plain, color ring, tinted in their colors, name badge; their photo once it exists, the test photo until then) and the logo options.
  Each option shown big and at the feed, comment and dark-screen sizes; then `profile-picture-pick.json`. In demo there is no real face: photo styles use the test photo, marked.
- **Banner(s):** `banner-tiles.json` → `banner-pick.json`, one pair per platform that has one: each option on a mock channel page (computer and phone) plus the full banner with the safe area drawn on.

## Output

`brand-kit.md`: exact fonts, colors, sizes, timings and positions for every component (Main, Backup and alternatives); when each appears; the thumbnail text spec (taste values, then the craft rules); the corner-mark answer; the source path and artifact URL of every page; and the rejected options with their reasons. Final files in `01 Brand Kit/` (exports, `sound/`), profile pictures and banners in `06 Profiles/`. Every final kit file gets a `Type: kit` row in `07 Asset Library/asset-index.md`.

**Hand-off at the end of the kit** (one line): "Your brand kit is done: logo, name tag, intro, sound logo and the rest are saved. Next: Shorts and Reels, how they look and end (3 pages, a few questions)." Without vertical: "Next: your Brand Genome, everything in one place."
