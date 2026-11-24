[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/rebahan149/news-image-20261123-frontpage-v1/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard)
[![reward](https://make.fun/badge/news-image-20261123/rebahan149/news-image-20261123-frontpage-v1/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# The World in One Day — Monday 23 November 2026

A one-page broadsheet summing up the world's news of **Monday
23 November 2026** in **35 stories** across 7 regions and 16
fields, built for the make.fun
[news-image-20261123](https://make.fun/bounty/news-image-20261123)
bounty. Every panel carries an original flat illustration drawn for
this page.

Three hero stories lead — Nvidia reinstating Jensen Huang as CEO
eleven days after his resignation (shares +31%, Nasdaq +6.5%),
Ukraine confirming its naval drones struck the Russian corvette
Merkury at Benghazi, Libya, and Belgium's national strike grounding
every Brussels flight for fourteen hours (429 flights, ~59,500
passengers) — followed by a UTC timeline, eight more numbered
illustrated panels (the flogging of singer Parastoo Ahmadi in
Tehran, India's $1.6bn pledge to Nepal, the Cikande factory-fire
toll confirmed at 24, Capita's 70% share crash, Burnham's UK–EU
deal in the Commons, the US move to recover $1bn from the Binance
hack, CrowdStrike's $44bn Zscaler deal, and Kenya–DR Congo's
restored ties), a dotted world map with the drawn stories pinned,
and 24 briefs. A DATE CHECK box states the rule the page was edited
by: every story happened or was first reported on Monday
23 November 2026 — COP31's collapse (Sunday), the Cikande fire
itself (Saturday) and the weekend's sport results are named as
excluded, and the Megaspeed blacklist, which surfaced Tuesday
morning, is marked "not yet".

One editorial note: the reference page this edition was modelled on
carried several stories that Monday's reporting does not support —
Russia threatening Estonia with "open war", a NATO space-defence
vow, an ICJ Rohingya ruling backed by 14 nations, a 2035 Women's
World Cup award. Those slots were given to real Monday stories
instead, and the swap is documented in STORIES.md.

## Files

- `entry.png` — the judged image (1024×1024 PNG, under 1 MiB)
- `index.html` — the front page source (illustrations are inline SVG; the map is drawn by a small inline script)
- `main.py` — copies `entry.png` to the output directory and prints a one-line dossier
- `STORIES.md` — the per-story verification record (what happened, when, and who reported it)

## Run

```
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network; two runs write the same bytes.

## License

MIT — see `LICENSE`.
