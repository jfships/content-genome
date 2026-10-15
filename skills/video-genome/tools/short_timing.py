#!/usr/bin/env python3
"""Timing numbers for a Short, from its cut's word times.

Usage: python3 short_timing.py words_out.json [--length 30] [--payoff 2.4] [--hold 18.2 --hold 26.0]

words_out.json : from tools/remap_words.py ({"words": [...], "duration": s}) or a plain word list.
                 Each word has "start"/"end" (or "t0"/"t1") in seconds, and "w"/"word"/"text".
--length       : target length in seconds (default: the cut's duration). Sets the word budget
                 (about 150 words a minute: ~37 per 15 s).
--payoff       : time of the first laugh, twist or result. Must be 3 s or less.
--hold         : time of a planned deadpan hold (up to 1.5 s); a gap starting within 0.3 s of it
                 isn't flagged. Repeat for several holds.

Prints the spoken pace, every gap over 0.6 s, the seconds to the first payoff and the word count
against the budget, with FIX on anything outside shorts/build.md "Pace".
"""
import argparse
import json


def load(path):
    data = json.load(open(path))
    dur = None
    if isinstance(data, dict):
        dur = data.get("duration")
        data = data.get("words", data.get("segments", []))
    words = []
    for w in data:
        s = w.get("start", w.get("t0"))
        e = w.get("end", w.get("t1"))
        t = w.get("w", w.get("word", w.get("text", "")))
        if s is None or e is None:
            continue
        words.append((float(s), float(e), str(t).strip()))
    words.sort()
    return words, dur


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("words")
    ap.add_argument("--length", type=float)
    ap.add_argument("--payoff", type=float)
    ap.add_argument("--hold", type=float, action="append", default=[])
    a = ap.parse_args()
    words, dur = load(a.words)
    if not words:
        print("no words found")
        return
    dur = dur or words[-1][1]
    length = a.length or dur
    bad = 0

    first, last = words[0][0], words[-1][1]
    speaking = last - first
    pace = len(words) / speaking if speaking > 0 else 0
    flag = "" if 2.3 <= pace <= 3.2 else "  FIX (target 2.3–3 words/s)"
    bad += bool(flag)
    print(f"cut {dur:.1f} s · target {length:.0f} s · {len(words)} words · pace {pace:.2f} words/s{flag}")

    if first > 0.5:
        print(f"  first word at {first:.2f} s  FIX (the hook should be spoken from the start)")
        bad += 1

    budget = round(length * 150 / 60)
    flag = "" if len(words) <= budget * 1.1 else "  FIX (cut words or lengthen)"
    bad += bool(flag)
    print(f"  words {len(words)} / budget ~{budget} for {length:.0f} s{flag}")

    gaps = []
    for (s0, e0, t0), (s1, e1, t1) in zip(words, words[1:]):
        g = s1 - e0
        if g > 0.6:
            held = any(abs(e0 - h) <= 0.3 for h in a.hold) and g <= 1.5
            gaps.append((e0, g, t0, t1, held))
    if gaps:
        for e0, g, t0, t1, held in gaps:
            tag = "planned hold" if held else "FIX"
            bad += not held
            print(f"  gap {g:.2f} s at {e0:.2f} s, after '{t0}' before '{t1}'  {tag}")
    else:
        print("  no gaps over 0.6 s")
    longest = max([s1 - e0 for (_, e0, _), (s1, _, _) in zip(words, words[1:])] or [0])
    print(f"  longest gap {longest:.2f} s")

    if a.payoff is not None:
        flag = "" if a.payoff <= 3 else "  FIX (first payoff must land by 3 s)"
        bad += bool(flag)
        print(f"  first payoff at {a.payoff:.2f} s{flag}")
    else:
        print("  first payoff: not given (pass --payoff <seconds>)")

    tail = dur - last
    if tail > 1.5:
        print(f"  {tail:.2f} s after the last word  FIX (end on the payoff; hold 1 s or less)")
        bad += 1

    print("OK" if not bad else f"{bad} problem(s)")


if __name__ == "__main__":
    main()
