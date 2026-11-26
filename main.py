"""The Internet in One Word.

Writes the single entry word to /output/entry.txt, exactly as the
bounty asks: one word, nothing else.
"""

import os
from pathlib import Path

# The whole internet, summed up: an endless feed that melts your
# attention span one swipe at a time.
WORD = "Brainrot"


def entry_text() -> str:
    """Return the entry word, checked against the bounty gate."""
    text = WORD.strip()
    assert text and " " not in text, "entry must be a single word"
    assert 1 <= len(text) <= 30, "entry must be 1-30 characters"
    return text


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
