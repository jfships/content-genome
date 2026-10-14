# Sound: music, effects, voice, mix

The brand's sound lanes, SFX set, rules and sound logo decide what the brand sounds like. This file is how to get, place and mix it.

## Sources, in order of preference

1. **The creator's own kit:** the brand's SFX files and sound logo in `01 Brand Kit/sound/`. Always first.
2. **HyperFrames `media-use`:** a bundled SFX library that works offline (`npx hyperframes media-use resolve --type sfx`), plus a music catalog that may need a sign-in.
3. **A generation service** (e.g. ElevenLabs music and sound-effect endpoints, or its connector), with the creator's own key:
   - Every music prompt states the lane's mood, genre, exact BPM, "instrumental", and "leaves room for a speaking voice".
   - Generated beds often start quiet and fade early. Meter each bed and place it by where the music actually plays, not by file length.
   - Show the list of pieces and the cost (from the tool's own price check) before generating; check the balance after the first piece.
   - If the service's files can't be downloaded where you work, ask the creator to download the takes they pick into the episode folder.
4. **Synthesized in code:** Web Audio rendered through OfflineAudioContext to WAV, or ffmpeg `aevalsrc`, for whooshes, ticks, hits and risers timed exactly to the graphics.

**Licensing:** only the creator's kit, generated audio, or audio whose license allows the platform. Never commercial songs.

## Narrator and character voices

- Generate from a described delivery (hushed, excited, wildlife-documentary). Never imitate a real person's voice, and never prompt "in the style of" a named narrator.
- Approve the script before paying. Generate 2 takes, check each with speech-to-text for the exact words, and let the creator pick.
- For "voice of God" or echo gags, process the creator's own recorded words (echo, low-pass, slight pitch-down) rather than generating a voice.
- Realistic synthetic voices need the platform's disclosure label.

## Music

- One bed per section, from the lanes the brand assigns to that part (hook, working sections, reveal, ending).
- It switches or drops at turning points. Silence before a big line is a tool.
- Long-form and vertical can use different lanes; the brand says which.

## Sound effects

- Use them on transitions and reveals: whoosh on wipes, ticks on counters, hits on big type, plus the brand's own sounds.
- Place each on the exact frame of its action.
- Not on every cut. Start from the brand's cap (about 1 per 3 s).

## Mix

- Three groups: voice, music, SFX. Music is **carved** under the voice (a dip in the voice's frequencies, e.g. `hyperframes-audio`'s carve), not just lowered.
- Voice chain starting point: `highpass=f=80, afftdn=nf=-25, acompressor=threshold=-20dB:ratio=3`.
- Final master: `loudnorm=I=-14:TP=-1` (YouTube normalizes to −14 LUFS). Drafts without voice: −16 LUFS.
- Sound logo on the sting, every long-form episode.
- Audio-only fixes don't need a re-render: rebuild the mix from the same clip list and remux onto the video.

## Checks (part of gate 3)

- Meter every section (`ffmpeg … -af volumedetect`) to catch silent gaps and clipping.
- Measure integrated loudness of the master (`loudnorm` print mode); it must be within ±1 LU of target.
- Say plainly in the review that you can't listen: levels are metered, not heard. Ask the creator to listen once on phone speakers and once on headphones.
