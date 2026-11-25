"""One-line joke entry for make.fun's "One Line, One Laugh" bounty.

The program writes a single funny line, at most 200 characters, to
/output/entry.txt. One dev, one green test suite, one twist: when the code
passes on the first try, the only thing left to suspect is the tests.
The punchline lands harder as one flowing sentence, so the two-sentence
draft is tightened into a single breath with the turn at the end.
"""

from pathlib import Path

JOKE = (
    "My code passed every test on the first run \u2014 "
    "so I spent the rest of the day debugging the tests."
)


def main() -> None:
    # The gate takes 1-200 characters of real text, and the judge reads one
    # cold line, so normalise whitespace before writing it out.
    text = " ".join(JOKE.split())
    assert "\n" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
