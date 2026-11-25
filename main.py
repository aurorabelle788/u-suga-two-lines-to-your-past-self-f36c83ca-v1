"""Two Lines to Your Past Self — make.fun entry.

Writes exactly one text to /output/entry.txt: a warning to the writer's
past self about one specific moment (line 1), and one sentence on why that
moment mattered and what changed because of it (line 2).

Deterministic: the text is a literal baked into this file. Standard
library only, no network, no randomness, no environment input, no reads
from other files.
"""

from pathlib import Path

ENTRY = (
    "Don't tell your little brother 'not now' when he pushes his bike "
    "onto the driveway that Saturday in June, seven years old and wobbling.\n"
    "He never asked again, and you spent the next twenty years buying him "
    "bigger presents because you could never buy back that afternoon."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
