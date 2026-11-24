#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 stdlib only, deterministic, no network.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"

ENTRY = (
    "My therapist says I avoid the spot by the door because it reminds "
    "me of my ex, the broom. I am working on it."
)


def validate(text):
    """Reject anything the gate would refuse: empty, whitespace-only,
    over 200 characters, or spanning more than one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be encodable as UTF-8
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(entry.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        sys.exit("error: %s" % exc)
