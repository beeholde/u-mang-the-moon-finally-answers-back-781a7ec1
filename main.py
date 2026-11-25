# u-mang-the-moon-finally-answers-back-781a7ec1 entry (Python 3.13, stdlib only):
# writes one line, in the Moon's voice, to /output/entry.txt. Deterministic:
# the same bytes on every run. Outside the grader's container,
# MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "The wolves howl at me once a month and at least they mean it. You wish once a year and call it a relationship."

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_bytes(LINE.encode("utf-8"))
