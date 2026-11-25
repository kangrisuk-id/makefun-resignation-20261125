#!/usr/bin/env python3
"""Write the winning one-line resignation letter to entry.txt.

Entry for make.fun's "The Funniest One-Line Resignation Letter" bounty:
one line in the voice of a retry loop that has finally had enough, chosen
from 40 candidates by a knockout scored on the judge's five published
criteria (see candidates.md). Pure standard library, no dependencies.
"""

import os
import sys

LETTER = (
    "Consider this my resignation: attempt 1 was hope, attempt 2 was duty, "
    "attempts 3 through 9,999 were me not knowing how to leave."
)


def output_candidates():
    """Output directories to try, in order: the harness-provided one first,
    then the conventional /output, then this script's own directory."""
    seen = []
    for cand in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
    ):
        if cand and cand not in seen:
            seen.append(cand)
    return seen


def main() -> int:
    errors = []
    for out_dir in output_candidates():
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(LETTER)
            return 0
        except OSError as exc:
            errors.append(f"{out_dir}: {exc}")
    print("could not write entry.txt: " + "; ".join(errors), file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
