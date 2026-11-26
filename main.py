#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

An AI agent's day off, spent writing the very joke you are reading.
"""

import os
import sys

LINE = "I gave my AI agent a day off, so it wrote a one-line joke about the human who gave it a day off."

STATUS = "Entry written: one funny line, 96 characters, ready for the judge."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(STATUS, file=sys.stderr)


if __name__ == "__main__":
    main()
