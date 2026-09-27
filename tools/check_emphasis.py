#!/usr/bin/env python3
"""强调标记守卫：逐段比对英文与中文的*斜体* / **粗体** 数量。

探针实测：全书斜体标记**中文比英文多 346 处**（第 1 章 +77、第 9 章 +93、
第 12 章 +101）。其中一部分是合理的（中文给英文术语补斜体、数学变量两边都有），
但超出量需要甄别：哪些是作者的强调（该保留），哪些是译稿自己加的（过度强调）。

本脚本只**提示**，不判缺陷。

用法：
    python3 tools/check_emphasis.py            # 全部差异段
    python3 tools/check_emphasis.py --top 40   # 按差值排序取前 N
    python3 tools/check_emphasis.py --file 9   # 只看第 9 章
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
CN = REPO / "cn-book"
EN = REPO / "en"

# 直接复用 check_structure 的中英映射与段落切分，保证两者口径一致
sys.path.insert(0, str(REPO / "tools"))
import check_structure as cs  # noqa: E402

MAP = cs.CN_MAP

# 单层 *斜体*（不含 ** 粗体**）
# 注意：后视断言只能用 [A-Za-z0-9*]，不能用 \w —— Python 的 \w 含汉字，
# 会把「如果*弯曲*曲面」这类中文夹斜体全部漏计（曾造成大量「EN→0」假警报）
ITALIC = re.compile(r"(?<![A-Za-z0-9*])\*([^*\n]+)\*(?![A-Za-z0-9*])")
BOLD = re.compile(r"\*\*([^*\n]+)\*\*")


def paras(text: str) -> list[tuple[int, str]]:
    """与 check_structure.para_lines 完全同口径，但保留行号。"""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith(" " * 4):
            continue
        if line.lstrip().startswith("$$"):
            continue
        s = line.strip()
        if not s or s.startswith(cs.NON_PARA) or cs.DIGIT_LIST.match(s):
            continue
        out.append((i, s))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--file", default=None, help="只查某个 cn 文件（给文件名片段）")
    args = ap.parse_args()

    rows = []
    for stem, cn_name in MAP.items():
        cf = CN / cn_name
        ef = EN / f"{stem}.md"
        if not cf.exists() or not ef.exists():
            continue
        if args.file and args.file not in cn_name:
            continue
        e = paras(ef.read_text(encoding="utf-8"))
        c = paras(cf.read_text(encoding="utf-8"))
        if len(e) != len(c):
            print(f"!! {stem}: 段落数不等 EN={len(e)} CN={len(c)}，按较短者对齐")
        for (eli, el), (cli, cl) in zip(e, c):
            ei, ci = len(ITALIC.findall(el)), len(ITALIC.findall(cl))
            eb, cb = len(BOLD.findall(el)), len(BOLD.findall(cl))
            if ei != ci or eb != cb:
                rows.append((cn_name, cli, eli, ei, ci, eb, cb, cl[:70]))

    rows.sort(key=lambda r: -abs((r[4] - r[3]) + 2 * (r[6] - r[5])))
    print(f"差异段 {len(rows)} 条（仅提示）")
    print("| 文件 | 行 | EN行 | 斜体 EN→CN | 粗体 EN→CN | 中文片段 |")
    print("|---|---|---|---|---|---|")
    for f, cli, eli, ei, ci, eb, cb, s in rows[: args.top]:
        s = s.replace("|", "\\|")
        print(f"| {f} | {cli} | {eli} | {ei}→{ci} | {eb}→{cb} | {s} |")
    if len(rows) > args.top:
        print(f"\n…另 {len(rows) - args.top} 条未显示（--top 调大）")


if __name__ == "__main__":
    main()
