#!/usr/bin/env python3
"""Entrypoint: copy the pre-drawn invitation PNG to /output/entry.png.

The image is drawn at build time and committed in this repository, so this
program needs nothing but the standard library: no fonts, no packages, no
network. It never deletes the output directory itself (the grader mounts it);
it only writes the single file inside it.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join("/output", "entry.png")


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    os.chmod(DST, 0o644)


if __name__ == "__main__":
    main()
