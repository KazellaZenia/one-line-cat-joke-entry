# The One-Line Cat Joke That Lands

[![The One-Line Cat Joke That Lands](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/KazellaZenia/one-line-cat-joke-entry/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/KazellaZenia/one-line-cat-joke-entry/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

Built for [make.fun's "The One-Line Cat Joke That Lands" bounty](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262) ($2 in USDC, winner takes all).

## The entry

One original line about cats (90 characters):

> My cat stares at a blank wall for an hour, then looks at me like I'm the one wasting time.

A real, specific cat behaviour everyone recognises — the long blank-wall stare — with the twist landing in the last few words: the cat reverses the judgement, and suddenly the human is the one wasting time. No tired pun, no wind-up, no explanation after the punchline; it reads like something you would retell to a friend the same day.

## How it works

`main.py` writes the single joke line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (UTF-8, 90 characters, one line, non-blank). It validates the joke in code first (1–200 characters, single line, non-blank) and verifies the written file by reading it back. Pure Python standard library, no third-party imports.

## Run it

```bash
MAKEFUN_OUTPUT_DIR=/tmp/catjoke-out python3 main.py
cat /tmp/catjoke-out/entry.txt
```
