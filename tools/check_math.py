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

# 已核实的英文源文公式笔误：中译按正确写法订正，因此与 en/25_Notes.md 不再逐字相同。
# 查什么：注释公式的「未经授权」改动。不查什么：这里登记过的订正（源文保留原貌以便回溯）。
# 出处：第七轮复核 review/findings/round7-notes-ch05-09.md、round7-notes-ch10-14.md。
# 新增条目必须写明出处与理由；源文若已订正，应把条目删掉（否则 test_check_note_formulas.py 会失败）。
APPROVED_NOTE_FORMULA_FIXES: dict[str, dict[str, str]] = {
    r"\text{Area}=\int _{0}^{2\pi}\int _{0}^{R}rdrd\theta=\int _{0}^{2x}\frac{1}{2}R^{2}d\theta=\pi R^{2}": {
        "cn": r"\text{Area}=\int _{0}^{2\pi}\int _{0}^{R}rdrd\theta=\int _{0}^{2\pi}\frac{1}{2}R^{2}d\theta=\pi R^{2}.",
        "reason": "ch06n8：圆面积应对 θ 积至 2π 才得 πR²，源文上限误作 2x；"
                 "句点移入公式内，否则加到显示围栏后会单独占一行。",
    },
    r"dx=\frac{\partial f}{\partial p}dp+\frac{\partial f}{\partial p}dq=adp+a'dq": {
        "cn": r"dx=\frac{\partial f}{\partial p}dp+\frac{\partial f}{\partial q}dq=adp+a'dq",
        "reason": "ch10n6：链式法则对 q 的偏导误写作 ∂f/∂p，与 x=f(p,q) 及 adp+a′dq 不符。",
    },
    r"\cos\theta=\frac{v\cdot v'}{(\sqrt{v\cdot v)(v\cdot v'})}=\frac{F}{\sqrt{EG}}.": {
        "cn": r"\cos\theta=\frac{v\cdot v'}{\sqrt{(v\cdot v)(v'\cdot v')}}=\frac{F}{\sqrt{EG}}.",
        "reason": "ch10n6：分母括号不配对且第二个范数重复 v；按 E=v·v、G=v′·v′ 应为 √((v·v)(v′·v′))。",
    },
    r"T^{\mu'v'}\equiv a^{\mu'}b^{v'}=\left(A_{\sigma}^{\mu'}a^{\sigma}\right)\left(A_{\lambda}^{v'}a^{\lambda}\right)=A_{\sigma}^{\mu'}A_{\lambda}^{v'}a^{\sigma}a^{\lambda}\equiv A_{\sigma}^{\mu'}A_{\lambda}^{v'}T^{\sigma\lambda}.": {
        "cn": r"T^{\mu'v'}\equiv a^{\mu'}b^{v'}=\left(A_{\sigma}^{\mu'}a^{\sigma}\right)\left(A_{\lambda}^{v'}b^{\lambda}\right)=A_{\sigma}^{\mu'}A_{\lambda}^{v'}a^{\sigma}b^{\lambda}\equiv A_{\sigma}^{\mu'}A_{\lambda}^{v'}T^{\sigma\lambda}.",
        "reason": "ch11n19：张量积的第二因子应是 b，源文两处误作 a。",
    },
    r"\frac{\partial V}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}=0.": {
        "cn": r"\frac{\partial X}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}=0.",
        "reason": "ch12n7：加速度分量记作 X, Y, Z，散度首项应为 ∂X/∂x，源文误作 V。",
    },
}


def apply_approved_note_fixes(en_formulas: list[str]) -> list[str]:
    """把源文中已登记为笔误的公式换成中译订正后的写法，便于与中译逐条比对。"""
    return [
        APPROVED_NOTE_FORMULA_FIXES[f]["cn"] if f in APPROVED_NOTE_FORMULA_FIXES else f
        for f in en_formulas
    ]


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
            # 注释里的公式顺序会变（见上），按多重集比；源文笔误的订正走白名单
            en_f_expected = apply_approved_note_fixes(en_f)
            if collections.Counter(en_f_expected) != collections.Counter(cn_f):
                n_severe += 1
                only_en = [x for x in en_f_expected if x not in cn_f]
                lines.append(f"- **严重**：注释公式内容不一致，仅见于英文 {len(only_en)} 条")
            else:
                lines.append(f"- 注释公式 {len(cn_f)} 条：与英文逐条一致"
                             f"（其中 {len(APPROVED_NOTE_FORMULA_FIXES)} 条为已登记源文笔误的订正）")
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
