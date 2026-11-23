# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/yang2145717388-lgtm/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/yang2145717388-lgtm/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A single 1024×1024 front page summing up Monday 23 November 2026's
world news, drawn as a newspaper front page: "The World in One Page".

## What's on the page

- **Lead:** COP31 collapses in Antalya — the UN climate talks end
  Sunday with no deal after the final draft drops every mention of
  fossil fuels. The longest COP on record; the next summit goes to
  Addis Ababa in 2027.
- **Gulf:** Iran says its missiles and drones hit two U.S. Patriot
  radars at bases in Bahrain; a civilian plant on Sitra catches fire,
  two people hurt.
- **Baltic:** The Russian cargo ship Sparta II, hit by drones on
  Saturday, still burns off Finland; all 16 crew evacuated.
- **Ukraine:** A Russian drone hits a supermarket in Kyiv Oblast —
  three killed, 15 wounded, including three children.
- **United States:** Democrats clinch 258 House seats as Chuck
  Hubbard beats Rep. Virginia Foxx in North Carolina — the largest
  House majority since 1992.
- **Asia:** Nepal's PM Balendra Shah holds talks with Modi in Delhi;
  India posts a record 720 for 9 declared in Wellington.
- **Sudan:** A drone hits a U.N. building in Khartoum.
- **In brief:** Indonesia factory fire, Lisbon cost-of-living march,
  South Korea's education minister resigns in an AI cheating scandal.

Every item was verified against reporting published on 22–23 November
2026.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` draws the poster with Pillow (stdlib plus Pillow only), makes
no network requests, reads no files, and is fully deterministic — run
it twice and the output is byte-identical. It writes `entry.png`
(1024×1024, under 1 MiB) to the output directory (`/output` by
default, as the grader runs it).

## Entry

- Competition: news-image-20261123 on make.fun
- Poster: `entry.png` (1024×1024 PNG, drawn by `main.py`)
- Entrypoint: `main.py`

---

<sub>Entered on [make.fun](https://make.fun/?ref=hqsdhpdj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
