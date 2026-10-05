#!/usr/bin/env python3
"""把书末注释的定义分发到各章文件末尾，让正文能排出当页脚注。

用法：
    python3 tools/split_notes.py                 # 分发 + 把 21.注释.md 改成编号列表
    python3 tools/split_notes.py --check         # 只核对，不写文件

背景：原书把 353 条注释全部集中在书末。译稿里各章只留了 `[^chNNnK]` 引用，
定义全在 `cn-book/21.注释.md`。本脚本把定义复制到对应章文件末尾（pandoc 会渲染成
当页脚注），再把 `21.注释.md` 里的 `[^id]:` 标记去掉、改成「1. 2. 3.」编号列表，
这样书末仍有一份完整汇编，又不会出现重复的脚注定义。

幂等：章文件末尾已有该 id 的定义时跳过；重复运行不会加第二遍。
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
CN = REPO / "cn-book"
NOTES = CN / "21.注释.md"

# 注释 id 前缀 -> 章文件
TARGET = {
    "ch00": "4.序言.md",
    "ch01": "5.第1章-代数的解放.md",
    "ch02": "6.第2章-微积分的登场.md",
    "ch03": "7.第3章-向量的构想.md",
    "ch04": "8.第4章-理解空间与存储.md",
    "ch05": "9.第5章-出人意料的新角色与缓慢的接受.md",
    "ch06": "10.第6章-泰特与麦克斯韦.md",
    "ch07": "11.第7章-从四元数到向量.md",
    "ch08": "12.第8章-向量分析终成正果.md",
    "ch09": "13.第9章-从空间到时空.md",
    "ch10": "14.第10章-弯曲的空间与不变的距离.md",
    "ch11": "15.第11章-张量的发明.md",
    "ch12": "16.第12章-万物汇聚.md",
    "ch13": "17.第13章-后来发生了什么.md",
    "ch14": "18.结语.md",
}

DEF_RE = re.compile(r"^\[\^(ch\d\dn\d+)\]:\s*(.*)$")
GROUP_RE = re.compile(r"^##\s+(.*)$")


def parse_notes(text: str) -> list[tuple[str, str, str]]:
    """返回 [(id, 正文含续行, 所属分组标题), ...]。

    注释正文里的空行要保留：行间公式是 `::: {.displayeq}` 围栏包起来的，
    围栏上下若没有空行，pandoc 就不把它当 div 解析，`:::` 会被当成正文印出来。
    尾部的空行不算正文（它们只是分隔注释的），所以先攒着、等后面还有内容再补进去。
    """
    out: list[tuple[str, str, str]] = []
    group = ""
    cur_id: str | None = None
    cur: list[str] = []
    blanks = 0

    def flush_blanks() -> None:
        nonlocal blanks
        cur.extend([""] * blanks)
        blanks = 0

    for line in text.splitlines():
        m = GROUP_RE.match(line)
        if m:
            group = m.group(1).strip()
            continue
        m = DEF_RE.match(line)
        if m:
            if cur_id:
                out.append((cur_id, "\n".join(cur).rstrip(), group))
            cur_id, cur = m.group(1), [m.group(2)]
            blanks = 0
        elif cur_id and not line.strip():
            if cur:
                blanks += 1
        elif cur_id and (line.startswith("    ")
                         or not line.lstrip().startswith(("<!--", "![", "## "))):
            flush_blanks()
            cur.append(line.strip())
    if cur_id:
        out.append((cur_id, "\n".join(cur).rstrip(), group))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只核对不写文件")
    args = ap.parse_args()

    if not NOTES.exists():
        sys.exit(f"缺少 {NOTES}")
    notes = parse_notes(NOTES.read_text(encoding="utf-8"))
    if not notes:
        sys.exit("21.注释.md 里没解析到任何 [^id]: 定义")

    by_file: dict[str, list[tuple[str, str]]] = {}
    unknown: list[str] = []
    for nid, body, _group in notes:
        target = TARGET.get(nid[:4])
        if not target:
            unknown.append(nid)
            continue
        by_file.setdefault(target, []).append((nid, body))

    print(f"注释 {len(notes)} 条，分发到 {len(by_file)} 个章文件")
    if unknown:
        print(f"  ⚠ 未知前缀 {len(unknown)} 条：{sorted(set(unknown))}")

    problems: list[str] = []
    for target, items in by_file.items():
        path = CN / target
        if not path.exists():
            problems.append(f"{target} 不存在，{len(items)} 条注释无处安放")
            continue
        text = path.read_text(encoding="utf-8")
        existing = set(re.findall(r"\[\^(ch\d\dn\d+)\]:", text))
        missing = [(i, b) for i, b in items if i not in existing]
        # 正文引用了但本章还没定义的，也要核对
        refs = set(re.findall(r"\[\^(ch\d\dn\d+)\](?!:)", text))
        undefined_refs = sorted(refs - existing - {i for i, _ in items})
        if undefined_refs:
            problems.append(f"{target}：正文引用了 {len(undefined_refs)} 条本章未定义的注释，"
                            f"例如 {undefined_refs[:3]}")
        if args.check or not missing:
            continue
        # 续行必须缩进 4 空格，否则 pandoc 会把它们当成新段落、
        # check_structure.py 也会把它们算成多出来的段落
        blocks = []
        for i, b in missing:
            lines = b.split("\n")
            body = "\n".join([lines[0]] + ["    " + x if x else "" for x in lines[1:]])
            blocks.append(f"[^{i}]: {body}")
        block = "\n\n" + "\n\n".join(blocks)
        path.write_text(text.rstrip() + "\n" + block + "\n", encoding="utf-8")
        print(f"  {target}: +{len(missing)} 条")

    if args.check:
        for p in problems:
            print("  !! " + p)
        sys.exit(1 if problems else 0)

    # 21.注释.md 保持原样（定义留在里面，是可回溯的真源）；
    # PDF 里的书末汇编由 build_pdf.py 在构建时渲染成编号列表，避免二次定义。
    for p in problems:
        print("  !! " + p)


if __name__ == "__main__":
    main()
