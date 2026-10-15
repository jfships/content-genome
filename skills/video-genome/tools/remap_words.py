#!/usr/bin/env python3
"""Move word times from the raw take onto the cut's timeline.

Usage: python3 remap_words.py words.json cutlist.json words_out.json

words.json   : from tools/talking-head/scripts/transcribe.py (list of {"w", "t0", "t1"} or {"w"/"word", "start", "end"}
               or {"words": [...]}).
cutlist.json : the kept spans of the raw take, in order: [[in, out], [in, out], ...] in seconds.
Words outside every kept span are dropped. A word cut in half keeps the part inside.
"""
import json
import sys


def load_words(path):
    data = json.load(open(path))
    if isinstance(data, dict):
        data = data.get("words", data.get("segments", []))
    return data


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    words = load_words(sys.argv[1])
    spans = json.load(open(sys.argv[2]))
    out, offset = [], 0.0
    for a, b in spans:
        for w in words:
            s = float(w["start"] if "start" in w else w["t0"])  # transcribe.py writes t0/t1/w
            e = float(w["end"] if "end" in w else w["t1"])
            if e <= a or s >= b:
                continue
            nw = {k: v for k, v in w.items() if k not in ("t0", "t1")}
            nw.setdefault("w", w.get("word", w.get("text", "")))
            nw["start"] = round(offset + max(s, a) - a, 3)
            nw["end"] = round(offset + min(e, b) - a, 3)
            nw["src_start"], nw["src_end"] = s, e
            nw["t0"], nw["t1"] = nw["start"], nw["end"]  # captions.py reads t0/t1
            out.append(nw)
        offset += b - a
    json.dump({"words": out, "duration": round(offset, 3)}, open(sys.argv[3], "w"), indent=1)
    print(f"{len(out)} of {len(words)} words kept; cut length {offset:.2f} s -> {sys.argv[3]}")


if __name__ == "__main__":
    main()
