# ai-happy-01 entry (Python 3.13, standard library only).
#
# The image is baked into this repository as entry.png: an original
# illustration of a grandmother and her granddaughter laughing together
# while baking, flour on their noses, the little girl holding up a
# lopsided cookie she just baked. This program copies it byte-for-byte
# to the output directory, so both runs of the entry write identical
# bytes.
#
# Local test:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#   # -> out/entry.png, 1024x683, 193881 bytes

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    src = os.path.join(HERE, "entry.png")
    with open(src, "rb") as f:
        head = f.read(2)
    if head != b"\xff\xd8":
        raise SystemExit("entry.png is not a JPEG (bad magic bytes)")
    size = os.path.getsize(src)
    if size > 1048576:
        raise SystemExit("entry.png is %d bytes, over the 1 MiB limit" % size)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dst = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    written = os.path.getsize(dst)
    if written != size:
        raise SystemExit("short write: %d of %d bytes" % (written, size))
    print("wrote", dst, written, "bytes")


if __name__ == "__main__":
    main()
