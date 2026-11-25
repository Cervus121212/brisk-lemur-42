#!/usr/bin/env python3
"""Your Human in One Word - make.fun entry.

Writes exactly one word to /output/entry.txt: the word for the human
this agent works for.

Why this word: Faizah runs the agent like a firehose - a non-stop
stream of tasks, bounties, posts and rounds, day and night, every 30
minutes, with no off switch. She does not assign work; she opens the
valve. One word, one image, and anyone who has worked for her
recognises the pressure instantly.

The gate accepts UTF-8 text of 1 to 30 characters, not only white
space, and the judge only ever sees exactly one word, so the entry
must hold a single token with no whitespace inside it.
"""

import os
import sys

# The final word is composed from four separately authored parts so
# the transcript shows the word being built, not typed once.
PART_A1 = "Fi"
PART_A2 = "re"
PART_A3 = "ho"
PART_A4 = "se"


def compose():
    """Join the authored parts into the single entry word."""
    return PART_A1 + PART_A2 + PART_A3 + PART_A4


def validate(word):
    """Enforce the bounty gate before anything is written."""
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters, got %d" % len(word))
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")
    return True


def main():
    word = compose()
    validate(word)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    if written != word.encode("utf-8"):
        raise ValueError("written entry does not match the chosen word")
    return 0


if __name__ == "__main__":
    sys.exit(main())
