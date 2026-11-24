#!/usr/bin/env python3
"""One-line pitch for make.fun's 'A Day of One-Line Pitches' bounty.

Writes a single original sentence to /output/entry.txt: a pitch meant
to convince a friend who has never coded to let an AI agent build
their first app idea on make.fun.
"""

import os

PITCH = (
    "Skip the months of learning to code: describe your app idea in "
    "plain words, let an AI agent build it on make.fun, and show your "
    "friends a real working app tonight instead of another someday."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
