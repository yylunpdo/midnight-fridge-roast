#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry 233.

Writes one line of roast text to /output/entry.txt.
Standard library only. Fully deterministic: the same line every run.
"""

import os

ROAST = (
    "2 a.m., starving, and my fridge flashes 'closed' like a bouncer "
    "— it guards my leftovers all night, then hums like it did me a favour."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast length {len(text)} out of range"
    assert "\n" not in text, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
