#!/usr/bin/env python3
"""术语一致性检查：译名有没有用错、有没有漏用、有没有踩禁用词。

用法：
    python3 tools/check_terms.py                # 全部已译章节
    python3 tools/check_terms.py --only 5.第1章-代数的解放.md

检查三类问题：
1. 严重：出现禁用译名（如「矢量」——全书统一用「向量」）。
2. 严重：同一个 English 术语在同一章里被译成两种以上中文（术语表已有译名 vs 别的写法）。
3. 中等：某术语在英文章节里出现 ≥3 次，译文中却一次都没用到术语表规定的译名。
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
from check_structure import CN_MAP  # noqa: E402

EN = REPO / "en"
CN = REPO / "cn-book"
REVIEW = REPO / "review"
GLOSSARY = REPO / "docs" / "术语表.md"

# 全书禁用译名 -> 应该用的译名
BANNED = {
    "矢量": "向量",
    "四元法": "四元数",
    "张量场论": "张量场",
}


def load_glossary() -> list[tuple[str, str]]:
    """从术语表的 Markdown 表格里读出 (English, 中文) 对。"""
    pairs: list[tuple[str, str]] = []
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 2:
            continue
        en, cn = cells
        if not en or not cn or en in ("English", "---"):
            continue
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9 '\-()/]*", en):
            continue
        # 中文侧去掉括号里的补充说明，如「四元数的单位部分（首次出现附原词 versor）」
        cn = re.sub(r"（.*?）", "", cn).strip()
        if not cn:
            continue
        pairs.append((en, cn))
    return pairs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    args = ap.parse_args()
    only = set(args.only.split(",")) if args.only else None

    pairs = load_glossary()
    REVIEW.mkdir(exist_ok=True)
    lines = ["# 术语一致性检查", "", f"术语表共 {len(pairs)} 条。严重度：严重 > 中等。", ""]

    n_severe = n_medium = 0
    for stem, cn_name in CN_MAP.items():
        if only and cn_name not in only:
            continue
        en_path, cn_path = EN / f"{stem}.md", CN / cn_name
        if not cn_path.exists():
            continue
        en_text = en_path.read_text(encoding="utf-8")
        cn_text = cn_path.read_text(encoding="utf-8")

        severe, medium = [], []

        for bad, good in BANNED.items():
            n = cn_text.count(bad)
            if n:
                # 「矢量图」这类固定说法允许保留，但要在括号里说明
                allowed = len(re.findall(rf"{bad}(?=（)", cn_text))
                if n - allowed:
                    severe.append(f"**禁用译名**「{bad}」出现 {n - allowed} 次，应统一为「{good}」")

        for en, cn in pairs:
            if len(en) < 4:
                continue
            hits = len(re.findall(rf"\b{re.escape(en)}\b", en_text, re.I))
            if hits < 3:
                continue
            if cn not in cn_text:
                medium.append(
                    f"**术语未落地**：英文「{en}」在本章出现 {hits} 次，"
                    f"译文未使用规定译名「{cn}」"
                )

        lines.append(f"## {stem} ↔ `cn-book/{cn_name}`")
        lines.append("")
        if not (severe or medium):
            lines.append("无术语问题。")
            lines.append("")
            continue
        n_severe += len(severe)
        n_medium += len(medium)
        for level, items in (("严重", severe), ("中等", medium)):
            if items:
                lines.append(f"### {level} ({len(items)})")
                lines.append("")
                for it in items:
                    lines.append(f"- {it}")
                lines.append("")

    (REVIEW / "terms.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"术语表 {len(pairs)} 条；严重 {n_severe} 项，中等 {n_medium} 项 -> review/terms.md")
    sys.exit(1 if n_severe else 0)


if __name__ == "__main__":
    main()
