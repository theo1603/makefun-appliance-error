#!/usr/bin/env python3
"""Write the entry: one line, the funniest honest error message an
appliance could show. Stdlib only, no network, deterministic output.

Revision: v1 had the washer re-washing a smelly hoodie and blaming the
owner, which was fine but generic and slightly explain-y. v2 keeps the
real fault (unbalanced load, a genuine washer error) but makes the
machine's defeat concrete and deadpan: it spent twenty minutes shaking
one hoodie, lost, and gives up with a flat shrug instead of a lecture.
Shorter, more machine-voiced, and the joke lands in the twist ("It won.")
rather than in the telling-off.
"""

import os

ENTRY = (
    "ERROR E04: Unbalanced load. I shook one hoodie for twenty minutes. "
    "It won. Please wash a full load, or don't."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
