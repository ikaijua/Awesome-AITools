#!/usr/bin/env python3
"""Tests for the traffic archive. No network access."""

import csv
import io
import json
import sys
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import traffic_snapshot as ts

SAMPLE = {
    "captured_at": "2026-11-08T01:17:00+00:00",
    "repo": "ikaijua/Awesome-AITools",
    "views": {"count": 300, "uniques": 120, "views": [
        {"timestamp": "2026-11-07T00:00:00Z", "count": 100, "uniques": 40},
        {"timestamp": "2026-11-08T00:00:00Z", "count": 200, "uniques": 80},
    ]},
    "clones": {"count": 20, "uniques": 12, "clones": [
        {"timestamp": "2026-11-08T00:00:00Z", "count": 20, "uniques": 12},
    ]},
    "referrers": [
        {"referrer": "Google", "count": 90, "uniques": 50},
        {"referrer": "github.com", "count": 180, "uniques": 60},
        {"referrer": "news.ycombinator.com", "count": 15, "uniques": 14},
        {"referrer": "chatgpt.com", "count": 10, "uniques": 9},
        {"referrer": "some-unknown.site", "count": 5, "uniques": 5},
    ],
    "paths": [{"path": "/ikaijua/Awesome-AITools", "title": "repo", "count": 250, "uniques": 100}],
}


class ChannelTests(unittest.TestCase):
    def test_channels_are_classified(self):
        cases = {
            "Google": "Search", "bing.com": "Search", "baidu.com": "Search",
            "github.com": "GitHub", "ikaijua.github.io": "GitHub",
            "chatgpt.com": "AI answers", "perplexity.ai": "AI answers",
            "news.ycombinator.com": "Community / social", "zhihu.com": "Community / social",
            "feedly.com": "Aggregators", "some-unknown.site": "Other / direct",
        }
        for value, expected in cases.items():
            self.assertEqual(ts.channel(value), expected, value)


class ArchiveTests(unittest.TestCase):
    def test_files_are_written_and_referrers_carry_channels(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "traffic"
            ts.archive(SAMPLE, out, "2026-11-08")
            self.assertTrue((out / "snapshots" / "2026-11-08.json").exists())
            with (out / "referrers.csv").open(encoding="utf-8") as handle:
                rows = {r["referrer"]: r["channel"] for r in csv.DictReader(handle)}
            self.assertEqual(rows["Google"], "Search")
            self.assertEqual(rows["chatgpt.com"], "AI answers")
            with (out / "views.csv").open(encoding="utf-8") as handle:
                self.assertEqual(len(list(csv.DictReader(handle))), 2)
            self.assertIn("14-day views: **300**", (out / "latest-summary.md").read_text())

    def test_rerunning_the_same_day_is_idempotent(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "traffic"
            ts.archive(SAMPLE, out, "2026-11-08")
            updated = json.loads(json.dumps(SAMPLE))
            updated["views"]["views"][0]["count"] = 999
            ts.archive(updated, out, "2026-11-08")
            with (out / "views.csv").open(encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 2)
            self.assertEqual(next(r for r in rows if r["date"] == "2026-11-07")["count"], "999")

    def test_new_day_appends_without_losing_history(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder) / "traffic"
            ts.archive(SAMPLE, out, "2026-11-08")
            later = json.loads(json.dumps(SAMPLE))
            later["referrers"] = [{"referrer": "reddit.com", "count": 7, "uniques": 6}]
            ts.archive(later, out, "2026-11-09")
            with (out / "referrers.csv").open(encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertTrue({r["referrer"] for r in rows} >= {"Google", "reddit.com"})
            self.assertEqual(len(list((out / "snapshots").glob("*.json"))), 2)

    def test_summary_states_the_diagnosis_rule(self):
        self.assertIn("distribution, not content", ts.summary_text(SAMPLE, "2026-11-08"))


class FetchTests(unittest.TestCase):
    def test_403_explains_the_missing_permission(self):
        error = urllib.error.HTTPError("https://api.github.com", 403, "Forbidden", {}, io.BytesIO())
        with patch.object(ts.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(SystemExit) as caught:
                ts.fetch("token", "ikaijua/Awesome-AITools", "views")
        self.assertIn("Administration", str(caught.exception))

    def test_no_token_exits_with_code_2(self):
        with patch.object(sys, "argv", ["traffic_snapshot.py", "--token", "", "--outdir", "/tmp/nope"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(ts.main(), 2)


if __name__ == "__main__":
    unittest.main()
