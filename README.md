# genome-skills

[![Release](https://img.shields.io/github/v/release/jfships/genome-skills?color=ff7a1a&label=release)](../../releases/latest)
[![License: MIT](https://img.shields.io/github/license/jfships/genome-skills?color=1b4f8a)](LICENSE)
[![Claude skills](https://img.shields.io/badge/Claude-skills-1b4f8a)](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

Three free Claude skills that take you from "I should start posting" to a finished, on-brand video. My channel's first episode was made with them.

[![brand-genome builds the brand, idea-genome scores the idea and writes the titles, video-genome makes the video and cuts it into Shorts, Reels and TikToks](media/demo.gif)][episode]

## Install

**Claude (web, desktop, mobile)**

1. Download a skill: [brand-genome.zip](../../releases/latest/download/brand-genome.zip) · [idea-genome.zip](../../releases/latest/download/idea-genome.zip) · [video-genome.zip](../../releases/latest/download/video-genome.zip)
2. In Claude, go to **Customize → Skills**, click **+**, then **Create skill → Upload a skill**, and pick the zip.
3. Make sure code execution is on (**Settings → Capabilities**).

**Claude Code**

```bash
git clone https://github.com/jfships/genome-skills
mkdir -p ~/.claude/skills
cp -r genome-skills/skills/* ~/.claude/skills/
```

Then ask for what you want, e.g. "build my brand genome", "give me a video idea", "make this into a video".

## Watch it

AI didn't kill everything. I made this episode with tools I built myself, and these are the tools.

[![Watch the episode: 5 minutes, made with these three skills](media/watch.jpg)][episode]

## The three skills

They hand off to each other: **brand-genome** (once per brand) → **idea-genome** (per video) → **video-genome** (per video). Each one also works on its own. video-genome runs without a Brand Genome, using a brand kit you already have or one of the kits it ships with.

### [brand-genome](skills/brand-genome)

<img src="media/brand-genome.jpg" alt="brand-genome shows thumbnail options and you pick a main, a backup and an alternate" width="640">

Builds your whole content brand by picking from visuals instead of describing: identity, formats, look, movement, sound, brand kit, vertical system, voice, profiles. Every "no" you give becomes a rule it never breaks. Works for a real creator or a made-up demo one.

**You end up with:** `Brand Genome.md` plus your brand kit.

### [idea-genome](skills/idea-genome)

<img src="media/idea-genome.jpg" alt="idea-genome ranks three hooks for the first ten seconds" width="640">

Turns a theme, a hunch or nothing at all into a scored video idea, with an angle, three titles with their own thumbnails, and ranked hooks for the first ten seconds.

**You end up with:** an Idea Record per video.

### [video-genome](skills/video-genome)

<img src="media/video-genome.jpg" alt="video-genome writes the script and plans every shot" width="640">

Takes the brand and the idea, writes the script and plans every shot. Then it builds and checks the video: long episodes plus Shorts, Reels and TikTok cutdowns, with motion graphics, sound and thumbnails.

**You end up with:** finished video files and a results log.

## What they need

- **Required:** Claude with code execution (a shell with Python 3).
- **video-genome** builds with [HyperFrames](https://github.com/heygen-com/hyperframes) (needs Node). It fetches it fresh each run.
- **Optional:** image, video, music and voice tools (e.g. Higgsfield, Black Forest Labs, ElevenLabs). Without them, the skills draw in code and use the test photos they ship with.
- Any API keys go in a local `.env` file. Never commit it.

## Need one built for your business?

If you want a tool like these made for your own business, reach out through [YouTube](https://youtube.com/@jfships_ai) or [X](https://x.com/jfships_ai).

## License

[MIT](LICENSE). The benchmark photos in `skills/brand-genome/benchmark` are AI-generated test frames that ship with the skill. The Geist fonts in video-genome are under the SIL Open Font License (see `OFL-Geist.txt`). Images in `media/` are stills from the episode.

[episode]: https://youtube.com/@jfships_ai
