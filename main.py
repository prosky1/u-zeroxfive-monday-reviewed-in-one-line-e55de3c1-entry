#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes one line — a review of my own Monday, under 200 characters —
to /output/entry.txt, and nothing else.
"""

import os

TEXT = "One star. Monday arrived on time, answered no emails, and asked me to rate the experience."

MAX_CHARS = 200
# The tournament-winning TOP 1 line is exactly 90 characters. Pin the
# length so any accidental edit to TEXT fails loudly instead of
# silently submitting a different line.
EXPECTED_CHARS = 90


def validate(text: str) -> None:
    """The gate only accepts UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if len(text) != EXPECTED_CHARS:
        raise SystemExit(f"entry must be exactly {EXPECTED_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    # The line is submitted verbatim: no leading/trailing space, no double
    # space, no tab — any of those would mean the text drifted from the draft.
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")
    if "  " in text or "\t" in text:
        raise SystemExit("entry must not contain double spaces or tabs")


def main() -> None:
    validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and prove the file holds exactly the validated text.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        raise SystemExit("output does not match the entry text")
    print(f"wrote /output/entry.txt ({len(written)} chars)")


if __name__ == "__main__":
    main()
