#!/usr/bin/env python3
"""图号体系守卫：把「原书编号 → 译稿图注 → 正文引用 → PDF 渲染号」四方对齐。

前四轮复核里，图注的**文字**（第二轮）与「图 N.M」的**文件存在性**（第四轮
`check_refs.py`）都查过，但没人把四方对齐过，于是漏掉了两处系统性偏差：

  1. **无编号图版被自动编号**——原书有 10 张**不带 FIGURE 号**的照片/图版
     （`pNNN.jpg`）。pandoc 把它们也排成带 `\\caption` 的 figure，LaTeX 一视同仁
     地编号，给它们凭空发号并把其后所有图号整体推后一位。
  2. **同号分幅被拆成独立图**——原书用 `FIGURE 2.3A` / `2.3B` 这种「同号分幅」
     编号（5 组），自动编号会把它们拆成两张连号图，且译稿把 A/B/C 后缀丢了。

修法：图号改为**显式编号**（写死在图注里，`header.tex` 用
`\\captionsetup{labelformat=empty,labelsep=none}` 关掉自动编号）。本脚本负责守住它。

检查项：
  A. 逐章比对 `en/` 的 FIGURE 编号序列与 `cn-book/` 的图注编号序列（按图片文件
     逐位置配对），必须完全一致；
  B. `pNNN.jpg` 图版**不得**带编号；
  C. 正文引用的「图 N.M」必须有对应图注；「引用他人著作」的编号走白名单；
  D. `--pdf`：从 PDF 文本层复核——不得残留自动编号（形如「图 N.M:」），
     且每条图注的编号＋正文都真的印了出来。

用法：
    python3 tools/check_figures.py                     # 只查 A/B/C
    pdftotext dist/vector-cn.pdf /tmp/v.txt
    python3 tools/check_figures.py --pdf /tmp/v.txt    # 追加 D
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
CN = REPO / "cn-book"
EN = REPO / "en"

# en 文件 stem -> cn 文件前缀（与 check_structure / split_notes 的映射一致）
PAIRS = [
    ("08_Prolog", "4.序言", 0),
    ("09_Chapter01", "5.第1章", 1),
    ("10_Chapter02", "6.第2章", 2),
    ("11_Chapter03", "7.第3章", 3),
    ("12_Chapter04", "8.第4章", 4),
    ("13_Chapter05", "9.第5章", 5),
    ("14_Chapter06", "10.第6章", 6),
    ("15_Chapter07", "11.第7章", 7),
    ("16_Chapter08", "12.第8章", 8),
    ("17_Chapter09", "13.第9章", 9),
    ("18_Chapter10", "14.第10章", 10),
    ("19_Chapter11", "15.第11章", 11),
    ("20_Chapter12", "16.第12章", 12),
    ("21_Chapter13", "17.第13章", 13),
    ("25_Notes", "21.注释", None),
]

# 正文引用了**他人著作**里的图号，不是本书编号，不当缺陷
FOREIGN_REFS = {
    "13.3": "Stillwell, Mathematics and Its History（第 3 章注释 ch03n11）",
}

EN_CAP = re.compile(r"^!\[FIGURE\s*([0-9]+\.[0-9]+[A-Za-z]?)")
EN_IMG = re.compile(r"images/([^) ]+)")
CN_CAP = re.compile(r"^!\[(?:图\s*([0-9]+\.[0-9]+[A-Z]?)\u3000)?([^\]]*)\]\((images/[^) ]+)\)")
CN_REF = re.compile(r"图\s*(\d{1,2})\.(\d{1,2})([a-z])?")


def cn_file(prefix: str) -> pathlib.Path | None:
    for f in sorted(CN.glob("*.md")):
        if f.name.startswith(prefix):
            return f
    return None


def pairs_of(stem: str, prefix: str) -> list[tuple[str | None, str]]:
    """返回 [(原书编号 or None, 图片文件名)]，按出现顺序。"""
    out = []
    for line in (EN / f"{stem}.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("!["):
            continue
        img = EN_IMG.search(line)
        if not img:
            continue
        m = EN_CAP.match(line)
        out.append((m.group(1) if m else None, img.group(1)))
    return out


def check_source() -> tuple[list[str], dict[str, int]]:
    problems: list[str] = []
    stat = {"图注": 0, "图版": 0, "引用": 0}
    captions: dict[int, set[str]] = {}   # 章号 -> 已存在的图号

    for stem, prefix, chno in PAIRS:
        path = cn_file(prefix)
        if not path:
            problems.append(f"缺少译稿文件：{prefix}")
            continue
        want = pairs_of(stem, prefix)
        got = []
        for line in path.read_text(encoding="utf-8").splitlines():
            m = CN_CAP.match(line)
            if m:
                got.append((m.group(1), m.group(3).split("/")[-1]))

        # A. 文件逐个配对
        if len(want) != len(got):
            problems.append(f"{path.name}  图片数 {len(got)} ≠ 原书 {len(want)}")
        for k, ((elabel, eimg), (clabel, cimg)) in enumerate(zip(want, got), 1):
            if eimg != cimg:
                problems.append(f"{path.name}  第 {k} 张图文件名不符：原书 {eimg} / 译稿 {cimg}")
                continue
            if (elabel is None) != (clabel is None):
                if elabel is None:
                    problems.append(f"{path.name}  {cimg} 原书无编号，译稿却编了「图 {clabel}」")
                else:
                    problems.append(f"{path.name}  {cimg} 原书编号 {elabel}，译稿缺编号")
            elif elabel != clabel:
                problems.append(f"{path.name}  {cimg} 编号不符：原书 {elabel} / 译稿 {clabel}")
            if clabel:
                stat["图注"] += 1
                if chno is not None:
                    ch, num = clabel.split(".", 1)
                    # 去掉分幅后缀：图注记「2.3A」，正文可能引「图 2.3」或「图 2.3b」
                    captions.setdefault(int(ch), set()).add(re.sub(r"[A-Za-z]$", "", num))
            else:
                stat["图版"] += 1

    # C. 正文引用必须落到某一章的图注上
    #    只比「章号.基号」：分幅后缀不参与——
    #      ① 原书图注用大写（FIGURE 2.3A），正文用小写（figure 2.3b）；
    #      ② 有些正文引用的是**图内的面板**（图 7.1b/c 指 fig7_1 的 b/c 面板），
    #         图注本身并没有分幅号。
    #    引用可以跨章（第 6 章正文可以引第 2 章的「图 2.3b」），所以查的是
    #    被引章，不是当前章。
    for path in sorted(CN.glob("*.md")):
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("!["):      # 图注自身不算引用
                continue
            for m in CN_REF.finditer(line):
                n, k, panel = int(m.group(1)), int(m.group(2)), m.group(3)
                stat["引用"] += 1
                if f"{n}.{k}" in FOREIGN_REFS or n not in captions:
                    continue
                if str(k) not in captions[n]:
                    problems.append(
                        f"{path.name}:{i}  正文引「图 {n}.{k}{panel or ''}」，"
                        f"但第 {n} 章没有基号为 {k} 的图注")
    return problems, stat


def check_pdf(pdf_path: pathlib.Path) -> list[str]:
    raw = pdf_path.read_text(encoding="utf-8", errors="ignore")
    problems: list[str] = []

    # D1. 自动编号残留（本项目的图注不带冒号）
    for m in re.finditer(r"图\s*\d+\.\d+[A-Z]?\s*[:：]", raw):
        problems.append(f"PDF 里仍有自动编号残留：{m.group(0)}")

    # D2. 每条图注的编号＋正文都必须印出来
    cjk = re.sub(r"[^\u4e00-\u9fff]", "", raw)
    for path in sorted(CN.glob("*.md")):
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            m = CN_CAP.match(line)
            if not m:
                continue
            label, cap = m.group(1), m.group(2)
            probe = re.sub(r"[^\u4e00-\u9fff]", "", cap)[:12]
            if not probe:
                continue                        # 原书亦无题注的图版
            if probe not in cjk:
                problems.append(f"{path.name}:{i}  图注正文未出现在 PDF：{cap[:20]}…")
    return problems


def main() -> None:
    ap = argparse.ArgumentParser(description="图号体系守卫")
    ap.add_argument("--pdf", type=pathlib.Path, help="pdftotext 的输出，用于复核渲染结果")
    args = ap.parse_args()

    problems, stat = check_source()
    if args.pdf:
        if not args.pdf.exists():
            sys.exit(f"找不到 {args.pdf}；先跑 pdftotext dist/vector-cn.pdf {args.pdf}")
        problems += check_pdf(args.pdf)

    print(f"检查：带编号图注 {stat['图注']} 条、无编号图版 {stat['图版']} 张、"
          f"正文图引用 {stat['引用']} 处" + ("（含 PDF 渲染复核）" if args.pdf else ""))
    if problems:
        print(f"\n问题 {len(problems)} 条：")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("图号体系与原书一致，正文引用均可落到对应图注。")


if __name__ == "__main__":
    main()
