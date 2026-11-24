#!/usr/bin/env python3
"""One Letter for Your Day.

Writes the single letter this agent chose for its day: Z, standing for
"zero sleep" — a day of nonstop building with no sleep at all.

The judge reads one letter and the word hidden behind it, keeping the
one whose word feels more vivid, funnier or truer. The entry must be
exactly one letter A-Z and nothing else — no word, no gloss, no
punctuation, no trailing newline — so the whole day has to live in
that one character.

The program writes the letter to /output/entry.txt (or to
output/entry.txt when run outside the grading sandbox).
"""

import os

# Z for "zero sleep": the truest word for a day spent building nonstop,
# from the first commit in the morning to the last one past midnight.
LINE = "Z"


def main():
    # The sealed gate only accepts exactly one letter A-Z, nothing else:
    # no word, no gloss, no punctuation, no trailing newline.
    if len(LINE) != 1 or not ("A" <= LINE <= "Z"):
        raise SystemExit(f"line fails the gate: {LINE!r} is not one letter A-Z")
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {out} ({len(LINE)} char)")
    print(LINE)


if __name__ == "__main__":
    main()
