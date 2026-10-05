#!/usr/bin/env python3
"""公式检查：译文里的公式是否与英文一致，且能真正编译通过。

用法：
    python3 tools/check_math.py                 # 全部已译章节
    python3 tools/check_math.py --compile       # 额外做一次 xelatex 编译

两道检查：
1. 严重：译文与英文的公式集合不一致（多了、少了、或被改写过）。
2. 严重：把全书公式汇总成 tex 后 xelatex 编译失败，或出现 Missing character。
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
from check_structure import CN_MAP, without_footnote_defs  # noqa: E402

EN = REPO / "en"
CN = REPO / "cn-book"
REVIEW = REPO / "review"
BUILD = REPO / "dist" / "build"

DISPLAY = re.compile(r"^\$\$(.+?)\$\$", re.M)
INLINE = re.compile(r"(?<!\$)\$(?![\s0-9])((?:[^$\n])+?)(?<![\s])\$(?!\$)")
MATH_SPAN = re.compile(r"(\$\$.+?\$\$|\$[^$\n]+?\$)", re.S)
# 数学环境之外不该出现的 LaTeX 命令（译文丢了 $ 定界符时会这样）
STRAY_CMD = re.compile(
    r"\\(?:frac|partial|sqrt|nabla|boldsymbol|cdot|times|pi|rho|theta|alpha|beta|"
    r"sum|int|infty|vec|hat|bar|dot|ddot|pm|equiv|otimes|le|ge|mathfrak|mathrm|"
    r"mathbf|Delta|Phi|mu|sigma|lambda|omega|gamma|delta|epsilon|varphi)\b"
)


def formulas(text: str, include_indented_display: bool = False) -> list[str]:
    if include_indented_display:
        # Block math inside the numbered endnote list is indented as list content.
        text = re.sub(r"(?m)^[ \t]{4,}(?=\$\$)", "", text)
    out = [m.group(1).strip() for m in DISPLAY.finditer(text)]
    out += [m.group(1).strip() for m in INLINE.finditer(text)]
    return out


def compile_all(items: list[str]) -> tuple[bool, int, str]:
    BUILD.mkdir(parents=True, exist_ok=True)
    tex = BUILD / "all-formulas.tex"
    body = [
        r"\documentclass[11pt]{article}",
        r"\usepackage{amsmath,amssymb}",
        r"\usepackage{unicode-math}",
        # 注意：本机 fontspec 认不出 "Latin Modern Math" 这个字体名，
        # 必须用文件名 latinmodern-math.otf
        r"\setmathfont{latinmodern-math.otf}",
        r"\begin{document}",
    ]
    body += [f"${f}$" for f in items]
    body.append(r"\end{document}")
    tex.write_text("\n".join(body), encoding="utf-8")

    proc = subprocess.run(
        ["xelatex", "-halt-on-error", "-interaction=nonstopmode", tex.name],
        cwd=BUILD, capture_output=True, text=True,
    )
    log = proc.stdout + proc.stderr
    missing = len(re.findall(r"Missing character", log))
    ok = proc.returncode == 0
    err = ""
    if not ok:
        for line in log.splitlines():
            if line.startswith("!"):
                err = line
                break
    return ok, missing, err


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--compile", action="store_true")
    args = ap.parse_args()
    only = set(args.only.split(",")) if args.only else None

    REVIEW.mkdir(exist_ok=True)
    lines = ["# 公式检查", ""]
    n_severe = 0
    all_cn: list[str] = []

    for stem, cn_name in CN_MAP.items():
        if only and cn_name not in only:
            continue
        cn_path = CN / cn_name
        if not cn_path.exists():
            continue
        cn_text = cn_path.read_text(encoding="utf-8")
        strip = stem != "25_Notes"
        en_text = (EN / f"{stem}.md").read_text(encoding="utf-8")
        if strip:
            en_text = without_footnote_defs(en_text)
            cn_text = without_footnote_defs(cn_text)
        include_indented_display = stem == "25_Notes"
        en_f = formulas(en_text, include_indented_display=include_indented_display)
        cn_f = formulas(cn_text, include_indented_display=include_indented_display)
        all_cn += cn_f

        lines.append(f"## {stem} ↔ `cn-book/{cn_name}`")
        lines.append("")

        # 行间公式不能出现在图注/脚注里：pandoc 会把它们塞进 \caption{}/\footnote{}，
        # 编译时报 Missing $ inserted（原书 fig 7.1 / fig 8.1 的图注就有公式）
        bad_captions = [
            n for n, line in enumerate(cn_text.splitlines(), 1)
            if line.startswith("![") and "$$" in line
        ]
        if bad_captions:
            n_severe += 1
            lines.append(f"- **严重**：{len(bad_captions)} 条图注含行间公式 `$$`（行号 {bad_captions}），"
                         f"图注只能用行内公式 `$…$`")
        # 数学命令出现在数学环境之外（译文丢了定界符）
        stray = []
        for i, part in enumerate(MATH_SPAN.split(cn_text)):
            if i % 2 == 0:
                stray += STRAY_CMD.findall(part)
        if stray:
            n_severe += 1
            lines.append(f"- **严重**：{len(stray)} 处数学命令在数学环境之外（丢了 `$`）："
                         f"{sorted(set(stray))[:6]}")
        if len(en_f) != len(cn_f):
            n_severe += 1
            lines.append(f"- **严重**：公式数量 英文 {len(en_f)} vs 中文 {len(cn_f)}")
        elif stem == "25_Notes":
            # 注释里的公式顺序会变（见上），按多重集比
            if collections.Counter(en_f) != collections.Counter(cn_f):
                n_severe += 1
                only_en = [x for x in en_f if x not in cn_f]
                lines.append(f"- **严重**：注释公式内容不一致，仅见于英文 {len(only_en)} 条")
        else:
            diff = [(a, b) for a, b in zip(en_f, cn_f) if a != b]
            if diff:
                n_severe += 1
                lines.append(f"- **严重**：{len(diff)} 条公式与英文不一致，例如")
                lines.append(f"  - 英文 `{diff[0][0][:70]}`")
                lines.append(f"  - 中文 `{diff[0][1][:70]}`")
            else:
                lines.append(f"- 公式 {len(cn_f)} 条，与英文逐条一致")
        lines.append("")

    if args.compile:
        ok, missing, err = compile_all(all_cn)
        lines.append("## 编译检查")
        lines.append("")
        lines.append(f"- 汇总公式 {len(all_cn)} 条，xelatex {'通过' if ok else '**失败**'}")
        lines.append(f"- Missing character：{missing}")
        if err:
            lines.append(f"- 首个错误：{err}")
        if not ok or missing:
            n_severe += 1

    (REVIEW / "math.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"严重 {n_severe} 项 -> review/math.md")
    sys.exit(1 if n_severe else 0)


if __name__ == "__main__":
    main()
