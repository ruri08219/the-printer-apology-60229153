#!/usr/bin/env python3
"""The Printer Apology — write the printer's apology to /output/entry.txt.

Standard library only. The line is a constant: the printer's own voice,
apologising for eating the 9 a.m. report while blaming the cheap paper.
The gate needs one single printable line of 1-120 characters, so the entry
is validated as one line before anything is written.
"""
import os

ENTRY = "Sorry I ate your 9 a.m. report, choked on a staple, and printed your resignation in colour. The cheap paper started it."
MAX_CHARS = 120


def validate(line):
    """Refuse anything the gate would refuse: empty, overlong, or not one line."""
    if not line:
        raise SystemExit("entry is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the 120-char gate")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry must be a single printable line")


def main():
    line = ENTRY.strip()
    validate(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
