#!/usr/bin/env python3
"""Mix voice, music beds, sound effects and the sound logo, then put the mix on the video.

Usage: python3 mix.py mix.json

mix.json:
{
  "video": "out/preview.mp4",            # picture (its own audio is ignored unless "voice" is omitted)
  "voice": "work/voice_cut.wav",         # the cut voice track (omit to use the video's audio)
  "beds":  [{"file": "music/hook.wav", "at": 0, "gain_db": -18, "fade_in": 0.5, "fade_out": 1.5, "length": 22.0}],
  "sfx":   [{"file": "sfx/whoosh.wav", "at": 12.40, "gain_db": -6}],
  "logo":  {"file": "brand/sound-logo.wav", "at": 14.0, "gain_db": -3},
  "duck_db": 8,                          # how far music dips under the voice
  "target_lufs": -14,
  "out": "out/final.mp4"
}
Music dips automatically when the voice speaks (sidechain compression), the
voice gets a light clean-up chain, and the master is loudness-normalized.
"""
import json
import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    m = json.load(open(sys.argv[1]))
    inputs = ["-i", m["video"]]
    voice_label = "0:a"
    if m.get("voice"):
        inputs += ["-i", m["voice"]]
        voice_label = "1:a"
    fc = [f"[{voice_label}]highpass=f=80,afftdn=nf=-25,"
          f"acompressor=threshold=-20dB:ratio=3:attack=10:release=200,asplit=2[vox][key]"]
    music, fx = [], []
    idx = len(inputs) // 2
    for i, b in enumerate(m.get("beds", [])):
        inputs += ["-i", b["file"]]
        ln = b.get("length")
        trim = f"atrim=0:{ln}," if ln else ""
        fo = b.get("fade_out", 0)
        fade_out = f",afade=t=out:st={max(0, (ln or 0) - fo)}:d={fo}" if (ln and fo) else ""
        fc.append(f"[{idx}:a]{trim}afade=t=in:d={b.get('fade_in', 0.3)}{fade_out},"
                  f"volume={b.get('gain_db', -18)}dB,adelay={int(b['at'] * 1000)}:all=1[m{i}]")
        music.append(f"[m{i}]")
        idx += 1
    for i, s in enumerate(m.get("sfx", []) + ([m["logo"]] if m.get("logo") else [])):
        inputs += ["-i", s["file"]]
        fc.append(f"[{idx}:a]volume={s.get('gain_db', -6)}dB,adelay={int(s['at'] * 1000)}:all=1[s{i}]")
        fx.append(f"[s{i}]")
        idx += 1
    mixparts = ["[vox]"]
    if music:
        fc.append(f"{''.join(music)}amix=inputs={len(music)}:normalize=0[mus]")
        ratio = max(2, int(m.get("duck_db", 8)))
        fc.append(f"[mus][key]sidechaincompress=threshold=0.03:ratio={ratio}:attack=20:release=300[duck]")
        mixparts.append("[duck]")
    else:
        fc.append("[key]anullsink")
    mixparts += fx
    fc.append(f"{''.join(mixparts)}amix=inputs={len(mixparts)}:normalize=0:duration=first,"
              f"loudnorm=I={m.get('target_lufs', -14)}:TP=-1:LRA=11[aout]")
    cmd = ["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(fc),
           "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
           "-ar", "48000", m["out"]]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
