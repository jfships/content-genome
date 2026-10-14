# genome-skills

Three Claude skills that take you from "I should start posting" to a finished, on-brand video. Free.

| Skill | What it does | You end up with |
|---|---|---|
| [brand-genome](skills/brand-genome) | Builds your whole content brand by picking from visuals instead of describing: identity, formats, look, movement, sound, brand kit, vertical system, voice, profiles. Works for a real creator or a made-up demo one. | `Brand Genome.md` plus your brand kit |
| [idea-genome](skills/idea-genome) | Turns a theme, a hunch or nothing at all into a scored video idea with an angle and titles. | An Idea Record per video |
| [video-genome](skills/video-genome) | Plans, builds and checks the video: long episodes plus Shorts, Reels and TikTok cutdowns, with motion graphics, sound and thumbnails. | Finished video files and a results log |

They hand off to each other: **brand-genome** (once per brand) → **idea-genome** (per video) → **video-genome** (per video). Each one also works on its own. video-genome runs without a Brand Genome, using a brand kit you already have or one of the kits it ships with.

Made by [Joseph Faulkner](https://youtube.com/@jfships_ai). You can watch them get used on the channel.

## Install

**Claude (web, desktop, mobile)**

1. Download the zip for the skill you want from [Releases](../../releases).
2. In Claude, go to **Customize → Skills**, click **+**, then **Create skill → Upload a skill**, and pick the zip.
3. Make sure code execution is on (**Settings → Capabilities**).

**Claude Code**

```bash
git clone https://github.com/jfships/genome-skills
mkdir -p ~/.claude/skills
cp -r genome-skills/skills/* ~/.claude/skills/
```

Then ask for what you want, e.g. "build my brand genome", "give me a video idea", "make this into a video".

## What they need

- **Required:** Claude with code execution (a shell with Python 3).
- **video-genome** builds with [HyperFrames](https://github.com/heygen-com/hyperframes) (needs Node). It fetches it fresh each run.
- **Optional:** image, video, music and voice tools (e.g. Higgsfield, Black Forest Labs, ElevenLabs). Without them, the skills draw in code and use the test photos they ship with.
- Any API keys go in a local `.env` file. Never commit it.

## Need one built for your business?

If you want a tool like these made for your own business, reach out through [YouTube](https://youtube.com/@jfships_ai) or [X](https://x.com/jfships_ai).

## License

[MIT](LICENSE). The benchmark photos in `skills/brand-genome/benchmark` are AI-generated test frames that ship with the skill. The Geist fonts in video-genome are under the SIL Open Font License (see `OFL-Geist.txt`).
