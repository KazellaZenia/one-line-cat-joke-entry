#!/usr/bin/env python3
"""One-line cat joke entry for make.fun bounty
u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes a single original cat joke to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library, no third-party imports.
"""

import os
from pathlib import Path

JOKE = (
    "My cat stares at a blank wall for an hour, "
    "then looks at me like I'm the one wasting time."
)


def main() -> None:
    # Gate validation, in code, before writing anything.
    if not JOKE.strip():
        raise SystemExit("joke must not be blank")
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit(f"joke must be 1-200 characters, got {len(JOKE)}")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("joke must be a single line")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(JOKE, encoding="utf-8")

    # Verify the written file by reading it back.
    written = out_path.read_text(encoding="utf-8")
    if written != JOKE:
        raise SystemExit("verification failed: entry.txt does not match the joke")
    print(f"Wrote {len(JOKE)}-character joke to {out_path}")


if __name__ == "__main__":
    main()
