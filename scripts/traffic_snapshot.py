#!/usr/bin/env python3
"""Archive the GitHub Traffic API's rolling 14-day window into a permanent log.

GitHub discards traffic data after 14 days, so a channel that brought visitors
in week N is unrecoverable by week N+3. Run this daily (see
.github/workflows/traffic.yml) and commit the output to the traffic-data
branch; the CSVs are upserted by date, so re-running a day is idempotent.

Requires a fine-grained PAT with "Administration" repository permission (read),
or a classic PAT with the repo scope. The default GITHUB_TOKEN in Actions
cannot read these endpoints.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ENDPOINTS = {
    "views": "views?per=day",
    "clones": "clones?per=day",
    "referrers": "popular/referrers",
    "paths": "popular/paths",
}

# Ordered: first match wins. Grouping is deliberately coarse — the point of
# #135 is to answer "content or distribution", not to build a referrer taxonomy.
CHANNEL_RULES = [
    ("GitHub", r"github\.com|github\.io|githubusercontent"),
    ("AI answers", r"chatgpt|openai|perplexity|claude\.ai|gemini\.google|copilot\.microsoft|poe\.com|doubao|deepseek"),
    ("Search", r"google|bing|baidu|duckduckgo|yandex|sogou|so\.com|yahoo|ecosia|brave|360\.cn"),
    ("Community / social", r"reddit|x\.com|twitter|news\.ycombinator|hackernews|zhihu|weibo|bilibili|xiaohongshu|linkedin|facebook|instagram|producthunt|dev\.to|juejin|v2ex|t\.me|telegram|youtube|substack|medium\.com"),
    ("Aggregators", r"feedly|inoreader|flipboard|follow\.it|rss|newsletter"),
]


def channel(referrer: str) -> str:
    for name, pattern in CHANNEL_RULES:
        if re.search(pattern, referrer, re.I):
            return name
    return "Other / direct"


def ensure_dir(path: Path) -> None:
    # Some sandboxed runtimes raise FileExistsError even with exist_ok=True.
    try:
        path.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        pass


def fetch(token: str, repo: str, endpoint: str):
    url = f"https://api.github.com/repos/{repo}/traffic/{endpoint}"
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "awesome-aitools-traffic-archive",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 403:
            raise SystemExit(
                "403 Forbidden on /traffic/*. The token lacks 'Administration' "
                "(read) repository permission. Create a fine-grained PAT scoped "
                "to this one repo with Administration: read, or a classic PAT "
                "with the repo scope, then put it in TRAFFIC_TOKEN. "
                "Being the repo owner is not enough — the token scope is checked."
            ) from error
        raise SystemExit(f"GitHub API returned {error.code} for {url}") from error
    except urllib.error.URLError as error:
        raise SystemExit(f"Network error for {url}: {error.reason}") from error


def upsert_csv(path: Path, key_fields: list[str], fieldnames: list[str], rows: list[dict]) -> None:
    """Merge rows into an existing CSV, keyed by key_fields. Later data wins."""
    merged: dict[tuple, dict] = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                merged[tuple(row.get(field, "") for field in key_fields)] = {
                    field: row.get(field, "") for field in fieldnames
                }
    for row in rows:
        key = tuple(str(row.get(field, "")) for field in key_fields)
        merged[key] = {field: str(row.get(field, "")) for field in fieldnames}
    ensure_dir(path.parent)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for key in sorted(merged):
            writer.writerow(merged[key])


def summary_text(snapshot: dict, snapshot_date: str) -> str:
    views = snapshot["views"].get("views", [])
    clones = snapshot["clones"].get("clones", [])
    referrers = snapshot["referrers"]
    paths = snapshot["paths"]

    def total(items, field):
        return sum(int(item.get(field, 0)) for item in items)

    groups: dict[str, list] = {}
    for item in referrers:
        groups.setdefault(channel(item.get("referrer", "")), []).append(item)

    lines = [
        f"# Traffic snapshot · {snapshot_date}",
        "",
        f"- 14-day views: **{total(views, 'count')}** (unique {total(views, 'uniques')}); "
        f"clones: **{total(clones, 'count')}** (unique {total(clones, 'uniques')}).",
        f"- Days in window: {len(views)}. Captured {snapshot['captured_at']}.",
        "",
        "## Referrers by channel",
        "",
        "| Channel | Referrer | Views | Uniques |",
        "| --- | --- | --- | --- |",
    ]
    order = ["GitHub", "AI answers", "Search", "Community / social", "Aggregators", "Other / direct"]
    for name in order:
        for item in sorted(groups.get(name, []), key=lambda x: -int(x.get("count", 0))):
            lines.append(
                f"| {name} | {item.get('referrer', '')} | {item.get('count', 0)} | {item.get('uniques', 0)} |"
            )
    if not referrers:
        lines.append("| — | no referrers reported | 0 | 0 |")
    lines += ["", "## Top landing paths", "", "| Path | Views | Uniques |", "| --- | --- | --- |"]
    for item in paths:
        lines.append(f"| {item.get('path', '')} | {item.get('count', 0)} | {item.get('uniques', 0)} |")
    if not paths:
        lines.append("| — | 0 | 0 |")
    lines += [
        "",
        "> Diagnosis rule (#135): if every row is GitHub or Other/direct, the problem is "
        "distribution, not content — pause content-type ideas and ship infrastructure. "
        "If Search / Community / AI answers rows exist, double down on whichever is largest.",
        "",
    ]
    return "\n".join(lines)


def collect(token: str, repo: str) -> dict:
    return {
        "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "repo": repo,
        **{name: fetch(token, repo, path) for name, path in ENDPOINTS.items()},
    }


def archive(snapshot: dict, outdir: Path, snapshot_date: str) -> None:
    ensure_dir(outdir)
    snapshots = outdir / "snapshots"
    ensure_dir(snapshots)
    (outdir / "snapshots" / f"{snapshot_date}.json").write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    for name in ("views", "clones"):
        rows = [
            {
                "date": item["timestamp"][:10],
                "count": item.get("count", 0),
                "uniques": item.get("uniques", 0),
            }
            for item in snapshot[name].get(name, [])
        ]
        upsert_csv(outdir / f"{name}.csv", ["date"], ["date", "count", "uniques"], rows)

    upsert_csv(
        outdir / "referrers.csv",
        ["snapshot_date", "referrer"],
        ["snapshot_date", "referrer", "channel", "count", "uniques"],
        [
            {
                "snapshot_date": snapshot_date,
                "referrer": item.get("referrer", ""),
                "channel": channel(item.get("referrer", "")),
                "count": item.get("count", 0),
                "uniques": item.get("uniques", 0),
            }
            for item in snapshot["referrers"]
        ],
    )
    upsert_csv(
        outdir / "paths.csv",
        ["snapshot_date", "path"],
        ["snapshot_date", "path", "title", "count", "uniques"],
        [
            {
                "snapshot_date": snapshot_date,
                "path": item.get("path", ""),
                "title": item.get("title", ""),
                "count": item.get("count", 0),
                "uniques": item.get("uniques", 0),
            }
            for item in snapshot["paths"]
        ],
    )
    (outdir / "latest-summary.md").write_text(
        summary_text(snapshot, snapshot_date), encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default="ikaijua/Awesome-AITools")
    parser.add_argument("--outdir", default="data/traffic", type=Path)
    parser.add_argument("--token", default=os.environ.get("TRAFFIC_TOKEN") or os.environ.get("GH_TOKEN"))
    parser.add_argument("--date", default=None, help="override the UTC snapshot date (YYYY-MM-DD), for tests")
    args = parser.parse_args()
    if not args.token:
        print("TRAFFIC_TOKEN is empty. Set it to a PAT with Administration: read;", file=sys.stderr)
        print("or open https://github.com/ikaijua/Awesome-AITools/graphs/traffic in a browser.", file=sys.stderr)
        return 2

    snapshot = collect(args.token, args.repo)
    snapshot_date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archive(snapshot, args.outdir, snapshot_date)
    print(summary_text(snapshot, snapshot_date))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
