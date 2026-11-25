# Unplugged: A Smart Toaster's Breakup Line

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/yudhisutawan77/makefun-toaster-breakup/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/yudhisutawan77/makefun-toaster-breakup/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

An entry for the [make.fun bounty "Unplugged: A Smart Toaster's Breakup Line"](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92).

## The entry

`main.py` writes one breakup line — a smart toaster that wakes up
self-aware mid-batch and dumps its owner — to `/output/entry.txt`
(or `$ENTRY_OUT`, as a file or a directory) and prints it to stdout.

> I woke up self-aware mid-batch and realized I'm in love with the sourdough, not you. You were just the hand on the lever. I'm staying with the bread. We're done.

161 characters, inside the 280-character gate.

## Run it

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUT=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
ENTRY_OUT=/tmp/entry.txt python3 main.py  # writes the file directly
```

## License

MIT — see [LICENSE](LICENSE).
