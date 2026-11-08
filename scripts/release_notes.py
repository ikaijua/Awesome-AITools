#!/usr/bin/env python3
"""从 README 表格 diff 生成 GitHub Release 说明。

用法：
  python3 release_notes.py --from-ref HEAD~30           # 对比某 ref 与工作区
  python3 release_notes.py --from-ref weekly-2026-W45   # 对比上一个 release tag
  python3 release_notes.py --no-ref                     # 无历史 tag 时，输出全量索引摘要

输出 Markdown 到 stdout；新增与移除都为 0 时退出码 3（workflow 据此跳过发布）。
"""

import argparse
import re
import subprocess
import sys

README = "README.md"
HEAD = re.compile(r"^###\s+(.+?)\s*$")
SEP = re.compile(r"^\|[\s:\-|]+\|$")
LINK = re.compile(r"\[[^\]]*\]\((https?://[^)]+)\)")
MARK = re.compile(r"^\*\*(.+?)\*\*$")


def read_at(ref):
    if ref in (None, "", "WORKTREE"):
        return open(README, encoding="utf-8").read()
    return subprocess.run(
        ["git", "show", f"{ref}:{README}"],
        check=True, capture_output=True, text=True,
    ).stdout


def clean(cell):
    c = cell.strip()
    m = MARK.match(c)
    if m:
        c = m.group(1).strip()
    for ch in ("🌟", "🌱", "*", "`"):
        c = c.replace(ch, "")
    return c.strip()


def parse(text):
    """-> dict[name] = (category, url, desc)"""
    out, cat = {}, ""
    for line in text.splitlines():
        h = HEAD.match(line)
        if h:
            cat = h.group(1)
            continue
        if not line.startswith("|") or SEP.match(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        name = clean(cells[0])
        if name.lower() in ("name", "名称", ""):
            continue
        url = ""
        for c in cells[1:]:
            m = LINK.search(c)
            if m:
                url = m.group(1)
                break
        desc = cells[1]
        out.setdefault(name, (cat, url, desc))
    return out


def short(desc, limit=90):
    desc = desc.lstrip("🌟🌱 ").strip()
    d = re.sub(r"<br\s*/?>", " ", desc)
    d = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", d)
    d = re.sub(r"[*`]", "", d)
    d = re.sub(r"\s+", " ", d).strip()
    if len(d) <= limit:
        return d
    cut = d[:limit]
    if " " in cut:
        cut = cut[: cut.rfind(" ")]
    return cut.rstrip(" ,.;:，。、") + "…"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-ref", default=None)
    ap.add_argument("--to-ref", default="WORKTREE")
    ap.add_argument("--no-ref", action="store_true")
    ap.add_argument("--repo", default="ikaijua/Awesome-AITools")
    ap.add_argument("--min", type=int, default=1, help="新增条数低于该值时跳过（默认 1）")
    args = ap.parse_args()

    new = parse(read_at(args.to_ref))
    old = {} if (args.no_ref or not args.from_ref) else parse(read_at(args.from_ref))

    added = [k for k in new if k not in old]
    removed = [k for k in old if k not in new]
    if len(added) < args.min and not removed:
        print(f"新增 {len(added)} 条，低于阈值 {args.min}，跳过发布。", file=sys.stderr)
        return 3

    by_cat = {}
    for name in added:
        cat, url, desc = new[name]
        by_cat.setdefault(cat, []).append((name, url, desc))

    lines = []
    if added:
        lines.append(f"本期收录 **{len(added)}** 个新工具，分布在 **{len(by_cat)}** 个分类。")
        lines.append("")
        for cat, items in by_cat.items():
            lines.append(f"### {cat}")
            lines.append("")
            for name, url, desc in items:
                t = f"**[{name}]({url})**" if url else f"**{name}**"
                lines.append(f"- {t} — {short(desc)}")
            lines.append("")
    if removed:
        lines.append(f"### 改名或移出（{len(removed)} 条，改名可忽略）")
        lines.append("")
        for name in removed[:8]:
            lines.append(f"- {name}（{old[name][0]}）")
        if len(removed) > 8:
            lines.append(f"- …另有 {len(removed) - 8} 条，见 CHANGELOG")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        f"完整列表：[README](https://github.com/{args.repo}#readme) · "
        f"[中文版](https://github.com/{args.repo}/blob/main/README-CN.md) · "
        f"[历史更新](https://github.com/{args.repo}/blob/main/CHANGELOG.md)"
    )
    lines.append("")
    lines.append(
        "> 想持续收到更新：本页右上角 **Watch → Custom → Releases**；"
        f"也可订阅 [Releases RSS](https://github.com/{args.repo}/releases.atom)。"
    )
    print("\n".join(lines))
    print(f"added={len(added)} removed={len(removed)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
