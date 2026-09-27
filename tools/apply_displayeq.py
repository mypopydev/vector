#!/usr/bin/env python3
"""把英文稿里的 ::: {.displayeq} 标记同步到已译中文稿上。

为什么需要这个脚本：译稿是照着未加标记的英文稿翻的。中英段落数已由
check_structure.py 校验为 1:1，因此按「第 N 个段落」对齐即可精确落位。

用法：
    python3 tools/apply_displayeq.py            # 同步
    python3 tools/apply_displayeq.py --check    # 只报告
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
from check_structure import CN_MAP, NON_PARA, DIGIT_LIST  # noqa: E402

EN = REPO / "en"
CN = REPO / "cn-book"


def para_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """返回「段落类」块的行号区间 [start, end)。"""
    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        raw_ok = (not line.startswith("    ")) and line.strip() and not line.startswith("$$")
        s = line.strip()
        if raw_ok and not s.startswith(NON_PARA) and not DIGIT_LIST.match(s):
            start = i
            while i < n and lines[i].strip() and not lines[i].startswith("    "):
                i += 1
            blocks.append((start, i))
            continue
        i += 1
    return blocks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    total = 0
    for stem, cn_name in CN_MAP.items():
        en_path, cn_path = EN / f"{stem}.md", CN / cn_name
        if not cn_path.exists():
            continue
        en_lines = en_path.read_text(encoding="utf-8").splitlines()
        cn_lines = cn_path.read_text(encoding="utf-8").splitlines()

        en_blocks = para_blocks(en_lines)
        # 英文里被 ::: {.displayeq} 包住的段落，其前一行（跳空行）就是标记
        marked = []
        for idx, (start, _end) in enumerate(en_blocks):
            j = start - 1
            while j >= 0 and not en_lines[j].strip():
                j -= 1
            if j >= 0 and en_lines[j].strip() == "::: {.displayeq}":
                marked.append(idx)

        cn_blocks = para_blocks(cn_lines)
        if len(en_blocks) != len(cn_blocks):
            print(f"  !! {cn_name}: 段数不一致（英 {len(en_blocks)} / 中 {len(cn_blocks)}），跳过")
            continue
        if not marked:
            continue

        # 从后往前插入，避免行号漂移
        for idx in sorted(marked, reverse=True):
            start, end = cn_blocks[idx]
            if args.check:
                continue
            cn_lines[end:end] = ["", ":::"]
            cn_lines[start:start] = ["::: {.displayeq}", ""]
            total += 1
        if not args.check:
            cn_path.write_text("\n".join(cn_lines) + "\n", encoding="utf-8")
        print(f"  {cn_name}: {len(marked)} 处")

    if args.check:
        print("（只报告，未改动）")
    else:
        print(f"共插入 {total} 处 displayeq 标记")


if __name__ == "__main__":
    main()
