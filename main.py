#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head (kevin).

One-line office joke, written verbatim to /output/entry.txt.
Pure stdlib only (grader runs python:3.13-slim, no site-packages).
Keeper: "My manager gave me 'exceeds expectations' and a 0% raise. The expectations were the raise."
90 chars, 90 bytes (verified by len() + wc -c; an earlier hand-count of 92 was wrong by 2).
Gate: entry.txt must be UTF-8 text of 1-200 chars.
"""
import os
import sys

KEEPER = "My manager gave me 'exceeds expectations' and a 0% raise. The expectations were the raise."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = KEEPER
    encoded = text.encode("utf-8")
    assert 1 <= len(encoded) <= 200, "entry must be 1-200 bytes"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    with open(path, "wb") as f:
        f.write(encoded)
    # Write-back self-check: what landed on disk must be the keeper, byte for byte.
    with open(path, "rb") as f:
        written = f.read()
    assert written == encoded, "entry.txt does not match the keeper"
    assert not written.endswith(b"\n"), "no trailing newline"
    sys.stdout.write(f"wrote {len(written)} bytes to {path}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
