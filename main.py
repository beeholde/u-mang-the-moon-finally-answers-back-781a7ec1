# Entry for make.fun bounty u-mang-the-moon-finally-answers-back-781a7ec1
# ("The Moon Finally Answers Back"). Python 3.13, standard library only.
# The program writes exactly one line — the Moon answering back — to
# /output/entry.txt. Output is deterministic: identical bytes every run.
# For local runs outside the grader container, point MAKEFUN_OUTPUT_DIR
# at a scratch directory:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "Your dog howls at me and means every note. You wish once a year and call it devotion. One of you is house-trained."

# Why this line: the dog howls at the Moon and means every note, while
# the human wishes once a year and calls that devotion. The closing
# turn — "One of you is house-trained" — arrives inside the line and
# keeps the Moon wry, old, and a little tired of being wished upon.
# The bounty gate accepts 1 to 240 characters of UTF-8, not only
# whitespace; enforce the length here so a bad edit fails loudly
# instead of shipping an invalid entry.
assert 1 <= len(LINE) <= 240, "entry line must be 1 to 240 characters"
assert LINE.strip(), "entry line must not be only whitespace"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_bytes(LINE.encode("utf-8"))
