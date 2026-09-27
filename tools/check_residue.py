#!/usr/bin/env python3
"""英文残留守卫：扫「中文句里夹 ASCII 单词」的未译残留。

风格指南第六节禁止译文里残留大段未译英文（技术术语、人名、书名、公式除外）。
本脚本扫出候选，由人工判定：
  - 保留：缩写（GPS/NASA/ETH/NLP/…）、专有名、术语表/人名表已收的词、
          原文双关或有译者注的词
  - 待改：说明性行文里本该译出却留着英文的词（如 wrangler）

用法：
    python3 tools/check_residue.py [--all]     # 默认排除已知白名单
"""
from __future__ import annotations

import argparse
import glob
import os
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
CN = REPO / "cn-book"
DOCS = REPO / "docs"

SKIP = ("![", "[^", "    ", "#", "|", "- ", "::", "$$", "<!--", ">")
# 中文（或中文标点）紧邻的 ASCII 词
PAT = re.compile(r"(?<![A-Za-z*])([A-Za-z][A-Za-z\-']{2,})(?![A-Za-z*])")
CJK = re.compile(r"[\u4e00-\u9fff]")

# 已知保留项：缩写、专有名、作者双关（带译者注）、原文地名拼写
WHITELIST = {
    "GPS","NASA","ETH","NLP","MICROSCOPE","PageRank","Tensorlab","Instagram",
    "OpenAI","Python","TensorFlow","JCMF","DIY","NOT","AND","OR","ETH-Bibliothek",
    "scaler","Szcezcin","Tripos","wrangler",
}


def known_terms() -> set[str]:
    out = set()
    for f in glob.glob(str(DOCS / "*.md")):
        for line in open(f, encoding="utf-8"):
            if line.startswith("|"):
                cells = [c.strip() for c in line.strip("|\n").split("|")]
                if cells and re.match(r"^[A-Za-z]", cells[0]):
                    out.update(re.findall(r"[A-Za-z][A-Za-z\-']{2,}", cells[0]))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="连白名单与表内词也列出")
    args = ap.parse_args()
    terms = known_terms()

    # 先剥掉这些再扫，否则人名括注、书名、引文会把结果淹没
    STRIP = [
        re.compile(r"（[^）]*）"),          # 中文括注里的英文原名
        re.compile(r"\([^)]*\)"),
        re.compile(r"\*[^*\n]+\*"),         # 斜体（书名/术语）
        re.compile(r'\*\*[^*\n]+\*\*'),
        re.compile(r"\$\$?[^$\n]+\$\$?"),   # 公式
        re.compile(r'"[^"\n]{3,}"'),        # 英文引文
        re.compile(r"“[^”\n]{3,}”"),        # 中文引文
        re.compile(r"《[^》]*》"),
        re.compile(r"\[[^\]]*\]"),          # 链接/图注
    ]

    rows = []
    for path in sorted(CN.glob("*.md")):
        for i, line in enumerate(open(path, encoding="utf-8"), 1):
            s = line.strip()
            if not s or s.startswith(SKIP) or not CJK.search(s):
                continue
            for rx in STRIP:
                s = rx.sub(" ", s)
            for m in PAT.finditer(s):
                w = m.group(1)
                if w in WHITELIST or w in terms:
                    if not args.all:
                        continue
                rows.append((os.path.basename(path), i, w,
                             s[max(0, m.start() - 28):m.end() + 28]))
    rows.sort(key=lambda r: (r[2], r[0]))
    print(f"英文残留候选 {len(rows)} 条（含白名单则 --all）")
    print("| 文件 | 行 | 词 | 上下文 |")
    print("|---|---|---|---|")
    for f, i, w, c in rows[:80]:
        print(f"| {f} | {i} | {w} | {c.replace('|', chr(92)+'|')} |")


if __name__ == "__main__":
    main()
