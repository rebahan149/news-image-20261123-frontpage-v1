# Entrypoint for the news-image-20261123 entry (v1 page).
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page summing up Monday 23 November 2026 in 35 stories across 7
# regions and 16 fields — 3 illustrated hero panels, 8 more numbered
# illustrated panels, a UTC timeline, a dotted world map with the
# drawn stories pinned, 24 briefs and a date-check box.
# The page source is index.html; the per-story verification record is
# STORIES.md. This program copies entry.png into $MAKEFUN_OUTPUT_DIR
# (default /output) and prints a one-line dossier describing the page.
# It runs with no network, and two runs write the same bytes: the copy
# is the whole program's output.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261123"
DATE = "2026-11-23"
WEEKDAY = "Monday"
STORIES = 35
ILLUSTRATED = 11
REGIONS = 7
FIELDS = 16

HEROES = [
    "Nvidia reinstates Jensen Huang as CEO 11 days after he resigned; shares surge 31%, Nasdaq +6.5%",
    "Ukraine confirms naval drones struck the Russian corvette Merkury at Benghazi, Libya; Zelensky releases video",
    "Belgium's national strike grounds flights: all 429 Brussels flights cancelled 07:00-21:00, ~59,500 passengers",
]

REGIONS_COUNT = {
    "Europe": 14,
    "North America": 6,
    "Middle East": 3,
    "Asia-Pacific": 3,
    "Africa": 4,
    "Latin America": 1,
    "World & Sport": 4,
}

NUMBERS = {
    "nvidia_share_surge_pct": 31,
    "nasdaq_gain_pct": 6.5,
    "belgium_flights_cancelled": 429,
    "belgium_passengers_scheduled": 59500,
    "indonesia_factory_fire_dead": 24,
    "indonesia_factory_fire_missing": 30,
    "capita_share_fall_pct": 70,
    "crowdstrike_zscaler_deal_usd_bn": 44,
    "india_nepal_pledge_usd_bn": 1.6,
    "doj_binance_recovery_claim_usd_bn": 1,
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "competition": COMPETITION,
        "date": DATE,
        "weekday": WEEKDAY,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "regions": REGIONS_COUNT,
        "fields": FIELDS,
        "heroes": HEROES,
        "numbers": NUMBERS,
        "output": dst,
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier, ensure_ascii=False))


if __name__ == "__main__":
    main()
