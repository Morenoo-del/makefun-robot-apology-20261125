#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line one owns one specific mistake; line two names the lesson and the
changed behaviour that follows from it. Deterministic: the text is fixed.
"""

from pathlib import Path

ENTRY = (
    "I'm sorry I set your alarm for 7 p.m. instead of 7 a.m., "
    "so you slept through your job interview.\n"
    "I learned that a.m. and p.m. are not a detail, so now I repeat the hour "
    "back to myself twice before I set any clock."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
