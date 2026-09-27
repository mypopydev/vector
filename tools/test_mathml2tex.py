#!/usr/bin/env python3
"""mathml2tex 的单元测试。

用例全部取自本书 epub 的真实片段（不是编造的），跑法：
    python3 tools/test_mathml2tex.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mathml2tex import convert  # noqa: E402

M = '<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline">{}</math>'

# (片段, 期望的 LaTeX 定界符内内容)
CASES: list[tuple[str, str]] = [
    # 第 1 章 fig. 1.1 图注：ab/2
    ("<mfrac><mrow><mi>a</mi><mi>b</mi></mrow><mn>2</mn></mfrac>", r"\frac{ab}{2}"),
    # 第 1 章：c^2 = (a+b)^2 − 4ab/2 = a^2 + b^2
    (
        "<msup><mi>c</mi><mn>2</mn></msup><mo>=</mo>"
        "<msup><mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced><mn>2</mn></msup>"
        "<mo>−</mo><mfrac><mrow><mn>4</mn><mi>a</mi><mi>b</mi></mrow><mn>2</mn></mfrac>",
        r"c^{2}=\left(a+b\right)^{2}-\frac{4ab}{2}",
    ),
    # 第 1 章：虚数单位
    ("<msqrt><mrow><mo>−</mo><mn>1</mn></mrow></msqrt>", r"\sqrt{-1}"),
    ("<msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mn>−1</mn>", r"i^{2}=-1"),
    # 尾注：三次根号
    (
        "<mroot><mrow><mfenced><mrow><mn>2</mn><mo>+</mo><mn>11</mn><mi>i</mi></mrow></mfenced></mrow>"
        "<mn>3</mn></mroot>",
        r"\sqrt[3]{\left(2+11i\right)}",
    ),
    # 尾注：速度上加横线
    ('<mover accent="true"><mi>b</mi><mo stretchy="true">¯</mo></mover>', r"\bar{b}"),
    # 第 11 章：列向量
    (
        "<mfenced><mtable columnalign=\"left\">"
        "<mtr><mtd><msub><mi>u</mi><mn>1</mn></msub></mtd></mtr>"
        "<mtr><mtd><msub><mi>u</mi><mn>2</mn></msub></mtd></mtr>"
        "</mtable></mfenced>",
        r"\left(\begin{matrix} u_{1} \\ u_{2} \end{matrix}\right)",
    ),
    # 第 11 章：2×2 矩阵（外层带圆括号）
    (
        "<mfenced><mtable equalcolumns=\"true\" equalrows=\"true\">"
        "<mtr><mtd><msub><mi>a</mi><mn>11</mn></msub></mtd><mtd><msub><mi>a</mi><mn>12</mn></msub></mtd></mtr>"
        "<mtr><mtd><msub><mi>a</mi><mn>21</mn></msub></mtd><mtd><msub><mi>a</mi><mn>22</mn></msub></mtd></mtr>"
        "</mtable></mfenced>",
        r"\left(\begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{matrix}\right)",
    ),
    # 第 11 章：爱因斯坦求和约定
    (
        "<munderover><mo>∑</mo><mrow><mi>σ</mi><mo>=</mo><mn>1</mn></mrow><mn>2</mn></munderover>",
        r"\sum_{\sigma=1}^{2}",
    ),
    # 第 11 章：张量分量记号 A^1_1
    ("<msubsup><mi>A</mi><mn>1</mn><mn>1</mn></msubsup>", r"A_{1}^{1}"),
    # 第 11 章：偏导与逗号下标
    (
        "<mfrac><mrow><mo>∂</mo><msup><mi>u</mi><mtext>μ</mtext></msup></mrow>"
        "<mrow><mo>∂</mo><msup><mi>x</mi><mtext>λ</mtext></msup></mrow></mfrac>"
        "<mo>≡</mo><msup><mi>u</mi><mtext>μ</mtext></msup>"
        "<msub><msub><mrow/><mo>,</mo></msub><mi>λ</mi></msub><mo>.</mo>",
        r"\frac{\partial u^{\mu}}{\partial x^{\lambda}}\equiv u^{\mu}_{,\lambda}.",
    ),
    # 第 11 章：nabla 算子（bold-italic 的 i/j/k）
    (
        "<mo>∇</mo><mo>=</mo><mfrac><mo>∂</mo><mrow><mo>∂</mo><mi>x</mi></mrow></mfrac>"
        '<mstyle mathsize="normal" mathvariant="bold-italic"><mi>i</mi></mstyle>',
        r"\nabla=\frac{\partial}{\partial x}\boldsymbol{i}",
    ),
    # 尾注：极限
    (
        "<munder><mrow><mi>lim</mi></mrow><mrow><mi>x</mi><mo>→</mo><mi>α</mi></mrow></munder>"
        "<mi>f</mi><mfenced><mi>x</mi></mfenced><mo>=</mo><mi>L</mi>",
        r"\lim_{x\to\alpha}f\left(x\right)=L",
    ),
    # 三角函数与角度
    (
        "<mi>sin</mi><mn>45</mn><mo>°</mo><mo>=</mo><mi>cos</mi><mn>45</mn><mo>°</mo>"
        "<mo>=</mo><mfrac><mn>1</mn><mrow><msqrt><mn>2</mn></msqrt></mrow></mfrac>",
        r"\sin 45^{\circ}=\cos 45^{\circ}=\frac{1}{\sqrt{2}}",
    ),
    # 撇号（prime）
    ("<msup><mi>x</mi><mo>′</mo></msup>", "x'"),
    ("<msup><mtext>μ</mtext><mo>′</mo></msup>", r"\mu'"),
    # bra-ket
    ("<mo>|</mo><mi>A</mi><mo>〉</mo>", r"|A\rangle"),
    # mtext：英文单词要进 \text{}
    ("<mtext>Area of triangle</mtext>", r"\text{Area of triangle}"),
    # mtext：单词 + 希腊字母混合
    ("<mtext>sin\xa0θ</mtext>", r"\sin \theta"),
    # mfenced 竖线定界符
    ('<mfenced open="|" close="|"><mi>A</mi></mfenced>', r"\left|A\right|"),
    # mfenced 方括号
    ('<mfenced open="[" close="]"><mi>a</mi></mfenced>', r"\left[a\right]"),
]


def test_all_cases() -> None:
    errors: list[str] = []
    for src, want in CASES:
        got = convert(M.format(src))
        expect = "$" + want + "$"
        if got != expect:
            errors.append(f"  输入: {src}\n  期望: {expect}\n  实际: {got}")
    assert not errors, "转换结果与期望不一致：\n" + "\n\n".join(errors)


def test_display_delimiter() -> None:
    got = convert(M.format("<msup><mi>c</mi><mn>2</mn></msup>"), display=True)
    assert got == r"$$c^{2}$$", got


def test_inline_delimiter() -> None:
    got = convert(M.format("<msup><mi>c</mi><mn>2</mn></msup>"), display=False)
    assert got == r"$c^{2}$", got


def test_unknown_tag_raises() -> None:
    try:
        convert(M.format("<mystery><mi>a</mi></mystery>"))
    except ValueError as exc:
        assert "mystery" in str(exc), exc
    else:
        raise AssertionError("未登记的标签应当抛 ValueError")


def test_no_mathml_residue() -> None:
    """输出里不许残留 MathML 标签名（防止漏转换被静默放过）。"""
    for src, _want in CASES:
        got = convert(M.format(src))
        for residue in ("<mfrac", "<msup", "<mi>", "<mo>", "<mrow", "<mtext"):
            assert residue not in got, f"{residue} 残留在 {got}"


def collect_book_formulas() -> list[tuple[str, str]]:
    """把 epub 里全部 <math> 抽出来转换，返回 (出处, LaTeX)。"""
    import glob
    import re
    import zipfile

    epubs = glob.glob(str(Path(__file__).resolve().parent.parent / "*.epub"))
    assert epubs, "仓库根目录找不到 epub"
    out: list[tuple[str, str]] = []
    with zipfile.ZipFile(epubs[0]) as z:
        for name in sorted(z.namelist()):
            if not name.startswith("OEBPS/xhtml/"):
                continue
            text = z.read(name).decode("utf-8")
            for m in re.finditer(r"<math\b.*?</math>", text, re.S):
                out.append((name.split("/")[-1], convert(m.group(0))))
    return out


def test_whole_book() -> None:
    """全书 262 处公式：不许抛错、不许残留标签、不许残留未映射字符。"""
    formulas = collect_book_formulas()
    assert len(formulas) == 262, f"公式数量应为 262，实际 {len(formulas)}"
    for where, tex in formulas:
        assert tex.startswith("$") and tex.endswith("$"), f"{where}: {tex}"
        for residue in ("<math", "<mi", "<mo", "<mtext", "<mrow", "<mfrac"):
            assert residue not in tex, f"{where} 残留 {residue}: {tex}"
        # 未映射的 Unicode 数学符号（拉丁字符与 ASCII 之外）
        for ch in tex:
            if ord(ch) > 0x2200 and ch not in "′″":
                raise AssertionError(f"{where} 含未映射字符 {ch!r}: {tex}")


def write_formula_tex(out_path: str) -> None:
    """把全书公式写成一个可编译的 tex，供 xelatex 冒烟测试。"""
    formulas = collect_book_formulas()
    lines = [
        r"\documentclass[11pt]{article}",
        r"\usepackage{amsmath,amssymb}",
        r"\usepackage{unicode-math}",
        r"\setmathfont{Latin Modern Math}",
        r"\begin{document}",
    ]
    lines += [tex for _where, tex in formulas]
    lines.append(r"\end{document}")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"已写出 {len(formulas)} 条公式 -> {out_path}")


if __name__ == "__main__":
    failed = 0
    for name, fn in sorted(list(globals().items())):
        if not name.startswith("test_") or not callable(fn):
            continue
        try:
            fn()
            print(f"PASS  {name}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL  {name}\n{exc}")
    print(f"\n{len(CASES)} 条转换用例 + 4 项检查，失败 {failed} 项")
    sys.exit(1 if failed else 0)
