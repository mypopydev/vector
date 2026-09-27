#!/usr/bin/env python3
"""把直角引号「」『』换成中文标准引号“”，嵌套层用‘’。

用法：
    python3 tools/fix_quotes.py            # 改写 cn-book/ 与 docs/
    python3 tools/fix_quotes.py --check    # 只统计

遇到「」时，若此时已在一对未闭合的“”之内，就降级成‘’，避免出现两层双引号。
"""

from __future__ import annotations

import argparse
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
TARGETS = sorted(REPO.glob("cn-book/*.md")) + sorted(REPO.glob("docs/*.md"))


def convert(text: str) -> str:
    out: list[str] = []
    stack: list[str] = []
    for ch in text:
        if ch == "「":
            out.append("‘" if '"' in stack else "“")
            stack.append("'" if '"' in stack else '"')
        elif ch == "」":
            kind = stack.pop() if stack else '"'
            out.append("’" if kind == "'" else "”")
        elif ch == "『":
            out.append("‘")
            stack.append("'")
        elif ch == "』":
            if stack:
                stack.pop()
            out.append("’")
        elif ch == "“":
            out.append(ch)
            stack.append('"')
        elif ch == "”":
            if stack and stack[-1] == '"':
                stack.pop()
            out.append(ch)
        elif ch == "‘":
            out.append(ch)
            stack.append("'")
        elif ch == "’":
            if stack and stack[-1] == "'":
                stack.pop()
            out.append(ch)
        else:
            out.append(ch)
    return "".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    total = 0
    for p in TARGETS:
        t = p.read_text(encoding="utf-8")
        n = t.count("「") + t.count("『")
        if not n:
            continue
        total += n
        if not args.check:
            p.write_text(convert(t), encoding="utf-8")
        print(f"  {p.name:34s} {n} 处")
    print(("（只统计，未改动）" if args.check else "已改写") + f"，合计 {total} 处")


if __name__ == "__main__":
    main()
