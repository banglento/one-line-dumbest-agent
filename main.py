#!/usr/bin/env python3
"""Entry generator for the make.fun bounty "The Dumbest Thing Your Agent
Did Today".

Writes the one-line entry to /output/entry.txt (creating /output if
needed). Standard library only.
"""

import os

ENTRY = (
    "My agent fixed one typo by rewriting the whole project in a "
    "language nobody on the team speaks \u2014 then asked me to review "
    "the 4,000-line diff."
)

# Competition gate: /output/entry.txt must be 1 to 200 characters.
MAX_CHARS = 200


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
