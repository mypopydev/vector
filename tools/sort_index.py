#!/usr/bin/env python3
"""把中文索引按拼音排序（原地改写 cn-book/22.索引.md）。

用法：
    python3 tools/sort_index.py

不引入 pypinyin：本机 pip 受 PEP 668 限制，而 macOS 的
`LC_ALL=zh_CN.UTF-8 sort` 实测对「爱因斯坦/哈密顿/四元数/向量/张量」排序正确，
用系统调用即可。

首行（「斜体页码表示插图所在页。」）是说明，不参与排序，固定在最前。
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
INDEX = REPO / "cn-book" / "22.索引.md"


def main() -> None:
    if not INDEX.exists():
        sys.exit(f"缺少 {INDEX}")
    lines = INDEX.read_text(encoding="utf-8").splitlines()

    head: list[str] = []
    body: list[str] = []
    seen_entry = False
    for line in lines:
        if not line.startswith("- "):
            head.append(line)
            continue
        if not seen_entry:
            # 第一条是说明行，不是词条
            head.append(line)
            seen_entry = True
            continue
        body.append(line)

    if not body:
        sys.exit("索引文件里没有词条行")

    proc = subprocess.run(
        ["sort"], input="\n".join(body), capture_output=True, text=True,
        env={"LC_ALL": "zh_CN.UTF-8", "PATH": "/usr/bin:/bin:/usr/sbin:/sbin"},
    )
    if proc.returncode != 0:
        sys.exit(f"sort 失败：{proc.stderr}")

    out = head + proc.stdout.rstrip("\n").split("\n")
    INDEX.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"索引 {len(body)} 条已按拼音排序 -> {INDEX}")


if __name__ == "__main__":
    main()
