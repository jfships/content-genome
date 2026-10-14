# Brand intake (Step 0, part 1)

Every video needs one brand file. This step finds it or makes it, before anything about the video is decided.

## 1. Look for one

In the brand folder (SKILL.md, "Brand folder and where to look"):
- `Brand Genome.md` → that's the brand file. Read it in full. Don't ask the kit question.
- `Brand Sheet.md` (made by this step on an earlier video) → that's the brand file. Say in one line which kit or sources it came from, and go on.
- Neither → ask (below).

Don't mention or recommend any other brand tool. If the creator brings up a Brand Genome they have elsewhere, ask them to add it to the brand folder.

## 2. Ask: "Do you have a brand kit?"

If they already sent brand material in this conversation (colors, fonts, a logo, a brand guide, a link), don't ask: go to section 3.

Otherwise one AskUserQuestion: "Do you have a brand kit: colors, fonts, a logo, how things move on screen?"
- **Yes, I'll send it** → section 3.
- **Some of it** → section 3, then fill the gaps (section 4).
- **No, show me the included kits** (Recommended) → section 5.
- **No, keep it plain** → the `clean-studio` kit, no page.

## 3. Their kit, in any format

Ask: "Send what you have." Accept anything: a Canva or Adobe brand kit export, a PDF brand guide, a website link, screenshots, a logo file, hex codes typed in chat, font names, a past video of theirs, an Instagram grid.
- Read it yourself: hex codes, font names (identify fonts from images by shape when unnamed and say it's a best match), logo files, any spacing or motion notes, words they never use.
- **Color roles.** Hex codes without roles: darkest or lightest becomes the background (whichever the sources use most), the most contrasting becomes the words, the most saturated the pop color; the rest are second color and pale. Show the roles on the check page; the creator fixes any.
- **Fonts.** A font in `page-template/fonts/fonts.json` is used from there. Otherwise: if it's free to use (Google Fonts, `@fontsource/*` on npm), fetch it into the brand folder's `01 Brand Kit/fonts/`; if it's paid (many Canva and Adobe fonts are), ask for the file they're licensed to use, and until then use the closest bundled font, labeled "stand-in" on every page. Brand font files are passed to pages with `fontFiles` (`decision-pages.md`); never added to the skill's own folder.
- From a past video: colors, fonts, caption style, how titles enter, pace of cuts.
- Fill the Brand Sheet slots (section 5) only with what the sources show. Write `from: <source>` beside each slot.
- Show the result as one page: the kit's colors and fonts on a title card, a lower third and a caption over a test frame (`page-template`, `brand-kits.json` shape with one option, `adjust` kind: **Looks right / Change it**). Fix what they mark.

## 4. Filling gaps

For every slot their kit leaves empty, ask once for all of them together: "Your kit has no <motion style / music / captions…>. Fill them from an included kit?" → **Yes, show me** (Recommended) · **Leave them plain**. If yes, the included kits page (`brand-kits.json`) shows each kit in **their** colors and fonts, so only the missing parts are being picked. Their own pieces always win over a kit's.

## 5. The included kits

`kits/` holds 8 complete kits (`kits/README.md`), each a full Brand Sheet (palette, fonts, title style, captions, motion feel and table, music lanes, sound rules, kept moves, vertical rules, house rules). They're the brand when the creator has none.
- Show them on one page (`page-template/examples/brand-kits.json`): the same title card, lower third and caption in each kit, with the color strip, one line on what it suits and how it moves. Recommend one from what they said about the video (tone, topic, pace) with one line of why.
- Main + backup. The backup kit lends its moves, motion and layouts when a moment doesn't fit the main (`craft/brand-fit.md`); never its colors or fonts.
- Copy the picked kit to `Brand Sheet.md` with `kit: <name>` and `backup kit: <name>` at the top.

If `kits/` is empty or missing, say so once, and build the kit page from the seed list in `page-template/gen_examples.py` (`KITS`): palette, fonts and motion feel only, with the motion table row for that feel (`craft/motion.md` §1).

## 6. Brand Sheet.md

Same headings as a Brand Genome, in this order, so every part of this skill reads either file the same way:
1. Creator · 2. Why and feel · 3. Research · 4. Formats · 5. Look · 6. Movement · 7. Sound · 8. Kit · 9. Vertical · 10. Voice · 11. Break-from-reality moments · 12. Images · 13. Profiles · 14. Run sheet · 15. House rules · 16. Changes

- §5 Look holds the colors (hex), fonts, text style, captions, backdrops and kept moves; `tools/brand_check.py` reads colors and fonts from it.
- Fill what the sources or the kit give; write `open` everywhere else. An `open` slot is never invented: the plan asks about it when a video needs it, and the answer is written back here (§16 Changes gets a dated line).
- §1 Creator and §2 Why and feel come from the creator questions below, asked once, the first time, right after the brand is settled.

## 7. Creator questions (first time only)

One AskUserQuestion each, in this order, each with suggested answers and a Recommended option where one fits. Skip any the brief, kit or Genome already answers (show it as taken on the intake page instead).
1. **Platforms:** where this goes (multi-select: YouTube long, Shorts, Reels, TikTok).
2. **On camera:** on camera · voice only · both.
3. **Personality:** pick up to 3 and rank them: entertaining, useful, calm, high-energy, quirky, serious, inspirational. (`SKILL.md`: the ranked list is a rule.)
4. **Never:** anything they never want on screen or said (words, looks, topics). Suggested: none for now.
Name, handle and language come from what they sent or the conversation; ask only if missing. Truth rules: write "no made-up numbers, quotes or results" by default; Proof is filled from the brief and confirmed on the intake page.
