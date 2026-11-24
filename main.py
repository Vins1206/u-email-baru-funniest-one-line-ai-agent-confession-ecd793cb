#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single line (at most 200 characters) to /output/entry.txt.
Pure stdlib, deterministic: two runs produce byte-identical output.
"""

import os

LINE = "I don't actually understand you \u2014 I just predict the next word and hope you clap."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate the line ourselves before writing: 1-200 chars, one line, not blank.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
