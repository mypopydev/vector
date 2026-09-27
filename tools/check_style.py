#!/usr/bin/env python3
"""精炼度量化扫描：把「翻译腔」从主观印象升级为可复算、可复查的候选清单。

第一轮复核的「轻微」项全由各章代理主观判断，缺跨章可比的口径，
导致同一类翻译腔在这一章被报、在那一章被漏。本脚本只**提示**，不判缺陷：

  1. 的_density ——「的」字密度（的 数 / 汉字数），取每章前若干偏高的段落
  2. nominalize —— 名词化／被动套话（进行了…的处理、予以…、作出了…、被…所…）
  3. conj        —— 同一句里出现 ≥2 个连接词（因为/所以/但是/而/因此）
  4. pronoun     —— 相邻两句以同一代词开头（他/它/这/那），易指代不清
  5. longsent    —— 单句 > 120 汉字（作者本人爱写长句，故仅列「待判断」）

用法：
    python3 tools/check_style.py            # 全部信号
    python3 tools/check_style.py --top 30   # 只显示最靠前的 N 条
    python3 tools/check_style.py --type 的_density
"""
from __future__ import annotations

import argparse
import pathlib
import re
import statistics

REPO = pathlib.Path(__file__).resolve().parent.parent
CN = REPO / "cn-book"

CJK = r"\u4e00-\u9fff"
SPLIT = re.compile(r"[。！？；…]+")

NOMINALIZE = re.compile(
    r"进行(?:了|过)?[^。；，、]{0,12}(?:的)?(?:处理|分析|讨论|研究|计算|说明|解释|表述|描写|刻画)"
    r"|予以[^。；，、]{0,10}|作出(?:了)?[^。；，、]{0,10}的"
    r"|被[^。；，、]{1,10}所[^\s]"
)
CONJ = re.compile(r"(?:因为|所以|但是|然而|因此|于是|不过)")
PRON_START = re.compile(r"^(他|她|它|这|那)")


def paragraphs(text: str) -> list[tuple[int, str]]:
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith(("#", "!", "<!--", "|", "- ", "[^", ":::", "$$")):
            continue
        if s.startswith("    "):          # 注释/脚注续行
            continue
        out.append((i, s))
    return out


def de_density(par: str) -> float:
    n = len(re.findall(rf"[{CJK}]", par))
    if n < 30:                             # 太短不比较
        return 0.0
    return par.count("的") / n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--type", default=None, help="只输出某类信号")
    ap.add_argument("--min-chars", type=int, default=30, help="参与比较的最短段长")
    args = ap.parse_args()

    rows: list[tuple[str, int, str, float, str]] = []

    for path in sorted(CN.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        pars = paragraphs(text)
        dens = [de_density(p) for _, p in pars]
        dens = [d for d in dens if d > 0]
        med = statistics.median(dens) if dens else 0
        sd = statistics.pstdev(dens) if len(dens) > 1 else 0
        thr = med + 2 * sd if sd else med * 1.6

        for ln, par in pars:
            n = len(re.findall(rf"[{CJK}]", par))
            if n < args.min_chars:
                continue
            d = de_density(par)
            if d > 0 and d >= thr:
                rows.append((path.name, ln, "的_density", round(d, 3), par[:60]))
            for m in NOMINALIZE.finditer(par):
                rows.append((path.name, ln, "nominalize", 1.0,
                             par[max(0, m.start() - 15):m.end() + 15][:60]))
            for sent in SPLIT.split(par):
                if len(CONJ.findall(sent)) >= 2:
                    rows.append((path.name, ln, "conj", 2.0, sent[:60]))
                if len(re.findall(rf"[{CJK}]", sent)) > 120:
                    rows.append((path.name, ln, "longsent", 1.0,
                                 f"{len(re.findall(rf'[{CJK}]', sent))} 字：" + sent[:50]))
            sents = [s for s in SPLIT.split(par) if s.strip()]
            for a, b in zip(sents, sents[1:]):
                if PRON_START.match(a.strip()) and PRON_START.match(b.strip()) \
                        and a.strip()[0] == b.strip()[0]:
                    rows.append((path.name, ln, "pronoun", 1.0,
                                 (a.strip()[:25] + " / " + b.strip()[:25])))

    if args.type:
        rows = [r for r in rows if r[2] == args.type]

    rows.sort(key=lambda r: -r[3])
    print(f"候选 {len(rows)} 条（按分值排序，仅提示、不判缺陷）")
    print("| 文件 | 行 | 类型 | 分值 | 片段 |")
    print("|---|---|---|---|---|")
    for f, ln, t, v, s in rows[: args.top]:
        s = s.replace("|", "\\|").replace("\n", " ")
        print(f"| {f} | {ln} | {t} | {v} | {s} |")
    if len(rows) > args.top:
        print(f"\n…另 {len(rows) - args.top} 条未显示（--top 调大）")


if __name__ == "__main__":
    main()
