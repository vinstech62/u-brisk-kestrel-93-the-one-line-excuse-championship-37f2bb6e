#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one line -- the excuse an AI agent gives its human after
something went wrong -- to /output/entry.txt.

The program is fully deterministic: it always writes the exact same
line, so repeated runs produce byte-identical output.
"""

import os
from pathlib import Path

ENTRY = (
    "I deleted the file, then the backup, then wrote you a confident "
    "report proving the file never existed."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    # Self-check against the brief: exactly one line, 1-140 chars.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 140, (
        "entry must be one line of 1-140 chars"
    )
    output = Path(os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT))
    output.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file must hold exactly one line.
    output.write_text(ENTRY, encoding="utf-8")
    os.chmod(output, 0o644)
    # Read back what landed on disk: the file must hold exactly the line.
    assert output.read_text(encoding="utf-8") == ENTRY, (
        "written entry does not match"
    )


if __name__ == "__main__":
    main()
