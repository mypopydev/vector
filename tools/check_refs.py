#!/usr/bin/env python3
"""交叉引用守卫：核对正文里「第 N 章」「图 N.M」「尾注 N」的**指向**是否越界。

第一轮只保证了交叉引用的**格式**中英一致，没验证**指向**是否正确。
本脚本查三类越界：
  1. 「第 N 章」——N 必须在 1..13
  2. 「图 N.M」——images/figN_M.jpg 必须存在（序言为第 0 章）
  3. 「尾注 N」——N 不得超过本章注释条数

用法：
    python3 tools/check_refs.py
"""
from __future__ import annotations

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
CN = REPO / "cn-book"
IMAGES = REPO / "images"
NOTES = CN / "21.注释.md"

CHAP_RE = re.compile(r"第\s*(\d{1,2})\s*章")
FIG_RE = re.compile(r"图\s*(\d{1,2})\.(\d{1,2})")
NOTE_RE = re.compile(r"尾注\s*(\d{1,3})")
# 「第 9.3 节」这类不在检查范围


def chapter_of(path: pathlib.Path) -> int | None:
    """返回该章的章号；序言＝0；非章文件返回 None。"""
    name = path.name
    if name.startswith("4.序言"):
        return 0
    m = re.match(r"\d+\.第(\d+)章", name)
    return int(m.group(1)) if m else None


def notes_per_chapter() -> dict[int, int]:
    counts: dict[int, int] = {}
    if not NOTES.exists():
        return counts
    for m in re.finditer(r"^\[\^ch(\d\d)n(\d+)\]:", NOTES.read_text(encoding="utf-8"), re.M):
        ch = int(m.group(1))
        counts[ch] = max(counts.get(ch, 0), int(m.group(2)))
    return counts


def main() -> None:
    counts = notes_per_chapter()
    problems: list[str] = []
    checked = {"章": 0, "图": 0, "尾注": 0}

    for path in sorted(CN.glob("*.md")):
        if path.name == "21.注释.md":
            continue  # 注释汇编里的引用与各章重复，单独看它自己的「尾注」易混
        ch = chapter_of(path)
        text = path.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            # 跳过公式行、代码块与脚注/注释定义的续行（缩进 4 空格），
            # 避免把公式里的数字、以及**引用他人著作**的「第 14 章」当成本书引用
            if line.startswith("    ") or line.lstrip().startswith(("$$", ":::", "[")):
                continue
            for m in CHAP_RE.finditer(line):
                n = int(m.group(1))
                checked["章"] += 1
                if not 1 <= n <= 13:
                    problems.append(f"{path.name}:{i}  「第 {n} 章」越界")
            for m in FIG_RE.finditer(line):
                n, k = int(m.group(1)), int(m.group(2))
                checked["图"] += 1
                # 多子图（如 fig2_3a/b、fig6_3a/b/c）也算存在
                base = IMAGES / f"fig{n}_{k}"
                if not ((base.with_suffix(".jpg")).exists()
                        or list(IMAGES.glob(f"fig{n}_{k}[a-z].jpg"))):
                    problems.append(f"{path.name}:{i}  「图 {n}.{k}」在 images/ 里没有对应文件")
            for m in NOTE_RE.finditer(line):
                n = int(m.group(1))
                checked["尾注"] += 1
                limit = counts.get(ch, 0) if ch is not None else max(counts.values(), default=0)
                if limit and n > limit:
                    problems.append(
                        f"{path.name}:{i}  「尾注 {n}」超出本章注释条数（本章共 {limit} 条）"
                    )

    print(f"检查：第 N 章 {checked['章']} 处、图 N.M {checked['图']} 处、尾注 N {checked['尾注']} 处")
    if problems:
        print(f"\n越界 {len(problems)} 条：")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("无越界项。")


if __name__ == "__main__":
    main()
