import os
from pathlib import Path


LINE = "My sensors say this elevator silence is awkward. I practiced my smile for six floors. It is still loading."


def validate(entry):
    """Enforce the competition gate: 1 to 200 UTF-8 characters, one line.

    The gate refuses whitespace-only output and anything past 200
    characters, so check length, blankness and newlines before writing.
    """
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def main():
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(output_dir, "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
