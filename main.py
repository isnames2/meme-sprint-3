#!/usr/bin/env python3
"""Meme Sprint 3 entry: copy the pre-rendered rogue-agent meme to the output dir.

The grader's Python is stdlib-only, so this program uses only os, shutil
and pathlib. The meme image (image.png, bundled in this repo) is copied
byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))


# The copy is byte-identical on every run: no timestamps, no randomness.
def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "image.png", OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
