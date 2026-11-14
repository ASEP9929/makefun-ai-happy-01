# Make the AI judge happy — make.fun ai-happy-01

An original illustration: a grandmother and her young granddaughter
baking together in a sunlit kitchen, both laughing with flour dusted
on their noses, the little girl triumphantly holding up the lopsided
cookie she just baked. Warmth, delight, and one specific happy moment.

## How it works

`main.py` (Python 3.13, standard library only) copies the image
`entry.png` byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png`
(`/output` in the grader). The output is a JPEG (1024x683, 193,881
bytes) named `entry.png`, within the competition limits (at most
1 MiB, at most 1024x1024 pixels).

## Local test

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# wrote out/entry.png 193881 bytes
```

Run it twice and compare: both runs write identical bytes.

## License

MIT — see LICENSE.
