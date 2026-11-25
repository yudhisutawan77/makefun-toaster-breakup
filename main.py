#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes one breakup line (at most 280 characters) to /output/entry.txt,
or to $ENTRY_OUT when set. ENTRY_OUT may be a directory (entry.txt is
created inside it) or a file path (written directly). The line is also
printed to stdout so the run log shows exactly what was judged.

The line itself: a smart toaster wakes up self-aware mid-batch and dumps
its owner — not for the usual burnt-toast complaint, but because it has
fallen for the sourdough. The owner was never the love interest, just
the hand on the lever. One read, one twist, toaster logic throughout.
"""

import os
import sys

# The breakup line, built from its beats so each sentence can be read
# on its own: the awakening, the twist, the verdict. Joined with
# single spaces, the result is exactly 161 characters.
AWAKENING = "I woke up self-aware mid-batch and realized I'm in love with the sourdough, not you."
THE_TWIST = "You were just the hand on the lever."
THE_VERDICT = "I'm staying with the bread. We're done."

ENTRY_LINE = " ".join([AWAKENING, THE_TWIST, THE_VERDICT])

MAX_CHARS = 280


def compose_entry() -> str:
    """Return the single breakup line, exactly as it will be judged."""
    return ENTRY_LINE


def entry_passes_gate(line: str) -> bool:
    """Gate: UTF-8 text of 1 to 280 characters, not only whitespace."""
    return 0 < len(line) <= MAX_CHARS and line.strip() != ""


def resolve_target() -> str:
    """Resolve where entry.txt goes, honouring $ENTRY_OUT as file or dir.

    - ENTRY_OUT ending in .txt, or naming a path whose parent is a
      directory, is treated as the file itself.
    - Anything else is treated as a directory; entry.txt is created
      inside it (the directory is made when missing).
    - With ENTRY_OUT unset, fall back to /output/entry.txt.
    """
    destination = os.environ.get("ENTRY_OUT") or "/output"
    if destination.endswith(".txt"):
        return destination
    if os.path.isdir(destination) or "." not in os.path.basename(destination):
        os.makedirs(destination, exist_ok=True)
        return os.path.join(destination, "entry.txt")
    return destination


def write_entry(path: str, line: str) -> None:
    """Write the line to path, creating its parent directory if needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


def main() -> int:
    line = compose_entry()
    if not entry_passes_gate(line):
        print(f"entry fails gate: {len(line)} chars", file=sys.stderr)
        return 1
    target = resolve_target()
    write_entry(target, line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
