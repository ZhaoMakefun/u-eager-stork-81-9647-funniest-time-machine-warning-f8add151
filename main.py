"""Entry for make.fun: Funniest Time Machine Warning Label.

Writes one warning label for a time machine to ``entry.txt`` inside the
output directory. Standard library only, no network access, fully
deterministic: the same bytes every run.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
The entry is written with no trailing newline so the file holds exactly
the entry text (111 characters, inside the 1-120 gate).
"""

import os
import sys

# The entry: a straight-faced safety notice whose hazard is meeting your
# own duplicate self -- with the surprise saved for the last few words.
ENTRY = (
    "WARNING: Do not leave before you arrive. If you meet yourself, "
    "do not make eye contact \u2014 he knows what you did."
)

MAX_CHARS = 120


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, outside the 1-{MAX_CHARS} gate",
              file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the entry text.
    if open(path, encoding="utf-8").read() != text:
        print("read-back mismatch: file does not match entry", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
