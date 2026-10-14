# Stage 9: The Brand Genome

Everything decided so far, in one place. Two forms, always in sync:

## Written automatically first (no stage, no page)

Before compiling, write these from everything decided so far, and show them on the Brand Genome page for review and edits:

**Profiles copy** (`00 Decisions/profiles.md`). **Accounts they're keeping (Stage 0):** update what's there rather than replace it. Platform facts this skill isn't sure of (character limits, link counts) are checked live; if a check fails, mark them "confirm at account setup".
- **Bios**, one per platform, written in the voice kit (who it's for, what they get, a reason to follow, one link or call to action). Ask at most one quick "pick a bio" question (3 variants + Other) only when there's a real choice.
- **Channel description and links.** The long description with keywords from the research, plus which links go where.
- **Templates:**
   - video description (hook line, what's inside, chapters slot, links, disclosure line)
   - pinned comment (a question or the free resource)
   - vertical caption with its call to action
- **Highlight covers (Instagram).** One per format, plus a few generic ones (behind the scenes, before-and-after), as icons in the brand's style.
- **Channel trailer plan.** 30–60 s, built from the recommended first format: hook, who it's for, what they'll get, a glimpse of a signature moment, follow. The plan only; making it is a video skill's job.

**Run sheet** (`00 Decisions/run-sheet.md`): the brand checks every video plan passes, whichever skill makes the video. Content steps (titles, research, angle, hooks, beats) belong to the video skill.
1. **Format:** which format from Stage 3 this video follows, or "one-off" with a reason.
2. **Look:** the main look (or backup, with a reason), backdrop, any filters for specific scenes and moments-library items with their use-when, at most one "big moments only" item, and nothing from the No lists.
3. **Movement and sound:** the motion table plus any change for this video (one line), and the music lanes per section.
4. **Personality check:** for every beat, name what makes it deliver the lead personality (a joke, a twist, a reveal, a real artifact, a payoff). "It explains X" is not an answer. A beat that's hard to make entertaining without forcing it uses the brand's fallback (§2), never a forced joke. The ending gets the hardest look: a callback and a concrete reason to watch the next one, never a slow wind-down.
5. **How far they'll go:** every effect, joke and break-from-reality moment stays inside the level picked in Stage 1.
6. **Break-from-reality check:** 2–3 spots proposed; 1–2 kept.
7. **Story-visual briefs** follow the image rules.
8. **Vertical rule:** 2–4 moments that stand alone, each with a hook in the first 3 s, in the vertical layouts.
9. **Voice check:** script and captions pass the voice kit and its AI-tell rules; every take gets the scorecard.
10. **Truth check:** every claim traces to Proof in the identity doc. **Disclosure check** for synthetic images or voices.

Pair every script with a rough draft video, because people react line by line and can't picture the whole from text.

## `Brand Genome.md` (for agents)

In the brand folder root (`Brands/<Brand>/Brand Genome.md`), with a copy in the project. Written for machines: exact values, no prose. It uses these headings, in this order, so any video skill can find what it needs:

1. **Creator:** name, handle per platform, target platforms, publishing rhythm, content language(s) (as language codes, e.g. `en`, `es`), on camera / voice only / avatar, mode (real / demo / auto), any tools the creator chose to use (from `START-HERE.md`), link to `Who I Am.md`, Proof and truth rules (copied in full), quirks and running gags. In demo: the full persona card and the avatar or face references, so a video skill can keep answering as the persona.
2. **Why and feel:** why the content exists; who's on screen (main route + secondary); what the channel is about (one line); content personality, ranked, one line each, plus the fallback line (what carries a topic that's hard to make entertaining); how far they'll go (the level and what it means in practice); filming setup (where and with what)
3. **Research:** link to `02 Research/channel-playbook.md`, its 5 most important defaults, and the benchmark channels (names + links). It guides how a video gets made; it never supplies ideas.
4. **Formats:** the kept formats (structure, length, recurring piece, default vertical layout) and the starting pair. No topics, no ideas: those come from the creator per video.
5. **Look (fixed picks + backups + alternatives):** palette (hex + role: background, words, pop color, second color, pale), main footage look (CSS recipe after tuning to the palette) + backup + alternatives, font set (files, sizes, weights, width scale) + caption font if different, text style + backup + alternatives, caption style + backup + alternatives and where captions are on. Then **Libraries:** filters for specific scenes, art styles for scenes you can't film, backdrops (default marked), small extras, big moments ("Big moments only." items marked), break-from-reality moments, each by catalog slug with its **use when** (the card line, or the creator's note). Also list each round's **No** options, so video skills never use them
6. **Movement:** motion feel (catalog slug) + backup + alternatives, the entrances library, the motion table, the moves library (transitions and camera moves by catalog slug, with any rule), the spatial library (kept spatial moves by slug, their source files in `07 Asset Library/graphics/`, skipped ones, rules), + the vertical row
7. **Sound:** the music library (each kind: mood, genre, BPM, prompt, where used), phrase length, the sound library (moment kind → files), rules, sound logo file
8. **Kit:** wordmark, name tag, lockup, series tag, sting, sound logo, corner mark (or "off"), episode-number placement, the endings library, the thumbnail library, profile picture, banner: each with exact sizes, positions, timing, when it appears, and the source file path
9. **Vertical:** layouts per format, caption spec, sting decision, tag and cover rules, the first-3-seconds rule, vertical music lane, safe zones (with the date checked)
10. **Voice:** voice kit, AI-tell rules, take scorecard
11. **Break-from-reality moments:** the kept templates (chosen in Stage 4 and written up right after)
12. **Images:** image rules, likeness references (best photo per slot), photos still owed, disclosure rules
13. **Profiles:** bios, descriptions, templates, trailer plan
14. **Run sheet:** the checklist (written in this stage)
15. **House rules:** every rejection with its reason
16. **Changes:** dated lines from `revisit.md`

Technical export settings (frame rate, resolution, loudness) are not brand decisions; the video skill owns them.

The file's last line is the credit: `Made with brand-genome by jfships · youtube.com/@jfships_ai` (unless the creator turned it off).

If a value isn't decided, write `open` and why; a skipped step is `skipped` with the default that applies. Never leave a heading out.

## The Brand Genome page (for people)

One shareable page (published as an artifact) that shows the brand at a glance. It's the "result" shot of the whole process, so it has to look finished. Build it from the template like every other page: `page-template/build.py genome.json out.html` with `"page": "genome"` (template `genome-page.html`; model data `examples/genome-<name>.json`, made by `gen_examples.py`).
- **Built from the picks themselves.** Each item copies the `html` (or image + `css`) of the option that was picked on its round's page, with its label (Main / Backup / Library), so the Genome shows exactly what was chosen, at the quality it was chosen. Sound and motion items keep `play`; put the rounds' `head` code (music, sting, sound logo) in the Genome's `head`.
- **It's highlights, and says so.** `highlights` puts this line at the top and the bottom of the page, and it's said at handoff: "Highlights only. The full brand, including every library, research default and rule, is in Brand Genome.md in your brand folder. Every video skill reads that file."
- **In order:** the opening (name, handle, one-line promise, chips for the feel and platforms, the wordmark) → who and why → formats → colors (`palette: true`) → footage look (the main look as tuned to the palette, labeled so) → fonts (`fontSet`) → words on video (text style + captions, caption mocks in the caption font) → movement → sound → brand kit → Shorts and Reels → voice → profiles (the copy written above) → run sheet (list) → **always, after the run sheet:** **Break-from-reality moments with visuals** (each kept moment as its three-panel strip from the library page, `aspect: "5/2"`; the skill's pick labeled **Our pick**; moments built from the creator's quirks get their own strip, drawn the same way, labeled **Your quirk**; each with its "Use when" line), **Images and likeness** (list, including photos still owed), **House rules** (list) → Changes.
- **The creator's photos** (once they exist) replace the test photos in every mock on this page, and pronouns in mock captions match them. A no-all-caps house rule goes in `houseRules` here too, so the page's own labels follow it.
- **Every section** has `change` (the decision in plain words) and `from` (the artifact URL of the page it was chosen on, from the stage doc): the page shows **How it was chosen →** and the words to use in chat to change it ("To change it, tell me in chat: change my color palette").
- Built in the brand's own palette (`palette`, roles in order) and fonts (`fontsCss`), so the page is itself on brand; on a dark background the cards take a lighter shade of it so light words stay readable (the template does this). Works at phone width. No autoplay. A credit line at the bottom: "Made with brand-genome by jfships · youtube.com/@jfships_ai" (on by default; `"credit": false` in the page data removes it if the creator asks, SKILL.md "Credit line"). Model to copy: `examples/genome-wren.json`.

**Keep it and come back.** The Genome page is the creator's home for the brand:
- **Same link, always.** Publish it once (no capabilities needed) and update that artifact on every change (never a new link); write the URL into `Brand Genome.md`, `README.md` and the `## Brand` section of `START-HERE.md`.
- **Pin offer.** After the first publish, offer once to pin it in their Claude sidebar; pin only on a yes.
- **An offline copy, always current.** Write `Brands/<Brand>/Brand Genome (visual).html`: the same built page, self-contained, with every image inlined as data (a small script reads each `img/…` path and swaps in a base64 data URL; keep it under ~15 MB by resizing images to 1280 px wide), so it opens offline in any browser. Set `offline` in the page data so the footer names it. Copy-as-text and Change only work online; say so in the README.
- **A shortcut to the online page,** matching the creator's computer: on Windows `Brand Genome page (online).url` (`[InternetShortcut]` / `URL=<link>`); on a Mac `Brand Genome page (online).webloc` (a plist with the `URL` key). Unsure: write both. The link is also in `README.md`.
- **Copy as text.** The keep bar's **Copy as text** gives a plain copy; the master stays `Brand Genome.md`.
- **Change something.** The page sends nothing to the chat. On first load a pop-up says: changes are asked for in the chat, naming what to change ("change my colors", "the sting is too long"); only that part changes, nothing else moves without asking, and the page updates at the same link. The keep bar's **How to change something** reopens it, and each section shows the words to use. A change request runs through `../revisit.md`: only that decision, the same way it was first decided, nothing downstream without approval, then the page is rebuilt, **republished to the same link (with its images) and the offline copy overwritten**, with a dated line under Changes.

## Output

`Brand Genome.md`, the published page (its URL in `Brand Genome.md` and `START-HERE.md`), `Brand Genome (visual).html` and the link shortcut in the brand folder root, and the page's source JSON + HTML in `01 Brand Kit/page-sources/genome/`. Highlight covers and any profile images made here go in `06 Profiles/`, each with a `Type: kit` row in `07 Asset Library/asset-index.md`.
