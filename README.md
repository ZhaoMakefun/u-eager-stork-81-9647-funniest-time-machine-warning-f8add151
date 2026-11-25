[![make.fun · u-eager-stork-81-9647-funniest-time-machine-warning-f8add151](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/ZhaoMakefun/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/ZhaoMakefun/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

A straight-faced safety notice for a time machine whose real hazard is meeting your own duplicate self — and the surprise is saved for the last few words, where the other you already knows what you did. It reads like a genuine warning label, turns the paradox into the joke, and lands in 111 characters.

Entry: "WARNING: Do not leave before you arrive. If you meet yourself, do not make eye contact — he knows what you did."

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3, standard library only, no network) writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), validates it against the 1–120 character gate, and reads it back to confirm the file holds exactly the entry text.
