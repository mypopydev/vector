#!/usr/bin/env python3
"""把 epub 里的 Presentation MathML 转成 LaTeX。

用法：
    from mathml2tex import convert
    convert('<math …>…</math>')            # -> '$…$'
    convert('<math …>…</math>', display=True)  # -> '$$…$$'

覆盖范围依据本书 epub 全量统计（262 处公式、19 种标签）：
mi(1430) mo(1038) mrow(775) mn(607) msup(306) mfrac(206) mtext(170)
msub(149) mtd(145) mfenced(127) msqrt(95) mtr(93) msubsup(71) mstyle(70)
mtable(40) mover(15) mroot(13) munder(3) munderover(1)

遇到未登记的标签直接抛 ValueError —— 宁可让构建失败，也不要静默产出错误的公式。
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET

NS = "{http://www.w3.org/1998/Math/MathML}"

# 希腊字母（mi / mtext 里都会出现，必须转成命令，否则 xelatex 报缺字形）
GREEK = {
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon",
    "ζ": "zeta", "η": "eta", "θ": "theta", "ι": "iota", "κ": "kappa",
    "λ": "lambda", "μ": "mu", "ν": "nu", "ξ": "xi", "ο": "omicron",
    "π": "pi", "ρ": "rho", "σ": "sigma", "τ": "tau", "υ": "upsilon",
    "ϕ": "phi", "φ": "varphi", "χ": "chi", "ψ": "psi", "ω": "omega",
    "Γ": "Gamma", "Δ": "Delta", "Θ": "Theta", "Λ": "Lambda", "Ξ": "Xi",
    "Π": "Pi", "Σ": "Sigma", "Υ": "Upsilon", "Φ": "Phi", "Ψ": "Psi",
    "Ω": "Omega", "ε": "epsilon", "ϑ": "vartheta", "ϖ": "varpi",
    "ς": "varsigma", "ℓ": "ell",
}

# 函数名（mi / mtext 里出现，必须转成 \sin 这类命令）
FUNCS = {
    "sin": r"\sin", "cos": r"\cos", "tan": r"\tan", "cot": r"\cot",
    "sec": r"\sec", "csc": r"\csc", "log": r"\log", "ln": r"\ln",
    "exp": r"\exp", "lim": r"\lim", "det": r"\det", "dim": r"\dim",
    "max": r"\max", "min": r"\min", "sup": r"\sup", "inf": r"\inf",
    "grad": r"\operatorname{grad}", "div": r"\operatorname{div}",
    "curl": r"\operatorname{curl}", "mod": r"\bmod",
}

# 运算符（mo 的全部取值，按出现频次排列）
MO = {
    "=": "=", "+": "+", "−": "-", "-": "-", "±": r"\pm", "×": r"\times",
    "⋅": r"\cdot", "∙": r"\bullet", "∗": r"*", "÷": r"\div", "/": "/",
    "∂": r"\partial", "∇": r"\nabla", "∆": r"\Delta", "Δ": r"\Delta",
    "∑": r"\sum", "∏": r"\prod", "∫": r"\int", "∬": r"\iint",
    "∭": r"\iiint", "∮": r"\oint", "√": r"\sqrt",
    "≡": r"\equiv", "≈": r"\approx", "∼": r"\sim", "≅": r"\cong",
    "≠": r"\neq", "≤": r"\leq", "≥": r"\geq", "≪": r"\ll", "≫": r"\gg",
    "→": r"\to", "⇒": r"\Rightarrow", "⇔": r"\Leftrightarrow",
    "←": r"\leftarrow", "↦": r"\mapsto", "⊗": r"\otimes", "⊕": r"\oplus",
    "⊲": r"\vartriangleleft", "⊳": r"\vartriangleright",
    "∈": r"\in", "⊂": r"\subset", "∪": r"\cup", "∩": r"\cap",
    "∞": r"\infty", "∝": r"\propto", "〈": r"\langle", "〉": r"\rangle",
    "|": "|", "‖": r"\|", "°": r"^{\circ}", "′": "'", "″": "''",
    ",": ",", ";": ";", ":": ":", ".": ".", "!": "!", "?": "?",
    "(": "(", ")": ")", "[": "[", "]": "]", "{": r"\{", "}": r"\}",
    "^": r"\hat{}", "~": r"\tilde{}", "¯": r"\bar{}", "˙": r"\dot{}",
    "¨": r"\ddot{}", "…": r"\dots", "⋮": r"\vdots", "⋯": r"\cdots",
    "": "",
}

# 上标位置的重音符号：\dot{x} 比 x^{\dot{}} 正确
SUPTENUS_ACCENT = {
    "˙": "dot", "¨": "ddot", "¯": "bar", "^": "hat", "~": "tilde",
    "→": "vec", "⃗": "vec",
}

# mover/munder 的重音底座
ACCENT_CMD = {
    "¯": "bar", "˙": "dot", "¨": "ddot", "^": "hat", "~": "tilde",
    "→": "vec", "⃗": "vec", "⏞": "overbrace", "⏟": "underbrace",
}

# 左右定界符（mfenced 的 open/close 属性）
DELIM = {"(": "(", ")": ")", "[": "[", "]": "]", "|": "|", "‖": r"\|",
         "{": r"\{", "}": r"\}", "⟨": r"\langle", "⟩": r"\rangle", "": ""}

# 需要 \left…\right 的运算符底座
BIG = {r"\sum", r"\int", r"\iint", r"\iiint", r"\oint", r"\prod", r"\lim"}


def _tag(el: ET.Element) -> str:
    return el.tag.replace(NS, "")


def _text(el: ET.Element) -> str:
    """元素自身的文本内容（不含子元素）。"""
    return (el.text or "").strip()


def _cat(a: str, b: str) -> str:
    """拼接两个数学片段；命令紧挨字母/数字会吞成命令名，需要补空格。

    \\equiv + u 会变成 \\equivu（未定义命令，编译失败），
    所以只在「前一个片段以命令名结尾」且「后一个片段以字母数字开头」时补空格。
    以 }、)、' 等结尾的片段不受影响，因此 \\frac{ab}{2} 不会被拆坏。
    """
    if not a or not b:
        return a + b
    if re.search(r"\\[a-zA-Z]*$", a) and re.match(r"[A-Za-z0-9]", b):
        return a + " " + b
    return a + b


def _join(parts) -> str:
    out = ""
    for p in parts:
        out = _cat(out, p)
    return out


def _kids(el: ET.Element) -> str:
    return _join(_node(c) for c in el)


def _mtext(s: str) -> str:
    """mtext 内容：希腊字母转命令，英文单词进 \\text{}，单字母/运算符原样。

    本书 mtext 里既有 θ、μ 这样的希腊字母，也有 'Area of triangle' 这样的
    英文短语，还有 'α|0'、'θdθ' 这种混合片段，需要按字符流逐段处理。
    """
    out: list[str] = []
    buf = ""

    def flush() -> None:
        nonlocal buf
        if not buf:
            return
        core = buf.strip()
        if core in FUNCS:
            out.append(FUNCS[core])
        elif len(core) >= 2 and re.fullmatch(r"[A-Za-z][A-Za-z\s]*", core):
            out.append(r"\text{" + buf.strip() + "}")
        else:
            out.append(buf)
        buf = ""

    for ch in s:
        if ch in GREEK:
            flush()
            out.append("\\" + GREEK[ch])
        elif ch == "∫":
            flush()
            out.append(r"\int ")
        elif ch == "∂":
            flush()
            out.append(r"\partial ")
        elif ch in MO and MO[ch].startswith("\\"):
            # 〉、⊗、≡ 这类运算符原书有时也标成 mtext
            flush()
            out.append(MO[ch])
        elif ch == "\xa0":
            flush()
            out.append(" ")
        else:
            buf += ch
    flush()
    return _join(out)


def _mi(el: ET.Element) -> str:
    s = _text(el)
    variant = el.attrib.get("mathvariant", "")
    if s in FUNCS:
        body = FUNCS[s]
    elif s in GREEK:
        body = "\\" + GREEK[s]
    elif s == "∞":
        body = r"\infty"
    else:
        body = "".join("\\" + GREEK[c] if c in GREEK else c for c in s)
    if "bold" in variant:
        body = r"\boldsymbol{" + body + "}"
    return body


def _mn(el: ET.Element) -> str:
    s = _text(el)
    if s == "...":
        return r"\dots"
    if s == "∫":  # 原书把积分号误标成了 mn
        return r"\int"
    if s == "...":
        return s
    return s.replace("−", "-")  # U+2212 减号在 math 里要写成 ASCII 减号


def _mo(el: ET.Element) -> str:
    s = _text(el)
    if s in MO:
        return MO[s]
    return s


# 只含一个下标组的字符串，例如 '_{,}' —— 空底座下标留下的中间态
SUB_ONLY = re.compile(r"^_\{([^{}]*)\}$")


def _render_sub(base: str, sub: str) -> str:
    """空底座的下标要挂到左侧相邻原子上，并合并连续下标。

    原书用 <msub><mrow/><mo>,</mo></msub> 表达「u^μ_{,λ}」这种逗号下标；
    若照字面生成 x_{a}_{b}，LaTeX 会报 Double subscript 而编译失败。
    """
    if not base:
        return "_{" + sub + "}"
    m = SUB_ONLY.match(base)
    if m:
        return "_{" + m.group(1) + sub + "}"
    return base + "_{" + sub + "}"


def _render_sup(base: str, sup: str) -> str:
    if sup in ("'", "′"):
        return base + "'"
    if sup in ("''", "″"):
        return base + "''"
    if sup in SUPTENUS_ACCENT:
        return "\\" + SUPTENUS_ACCENT[sup] + "{" + base + "}"
    if sup == r"\circ":
        return base + r"^{\circ}"
    return base + "^{" + sup + "}"


def _mfenced(el: ET.Element) -> str:
    open_ = el.attrib.get("open", "(")
    close_ = el.attrib.get("close", ")")
    body = _kids(el)
    # open="" 表示不定界（原书用来表达「无括号的分组」）
    if not open_ and not close_:
        return body
    return r"\left" + DELIM.get(open_, open_) + body + r"\right" + DELIM.get(close_, close_)


def _mtable(el: ET.Element) -> str:
    rows: list[str] = []
    for tr in el:
        if _tag(tr) != "mtr":
            continue
        cells = [_node(td) for td in tr if _tag(td) == "mtd"]
        rows.append(" & ".join(cells))
    return r"\begin{matrix} " + r" \\ ".join(rows) + r" \end{matrix}"


def _mstyle(el: ET.Element) -> str:
    body = _kids(el)
    variant = el.attrib.get("mathvariant", "")
    if "bold" in variant:
        return r"\boldsymbol{" + body + "}"
    return body


def _mover(el: ET.Element) -> str:
    kids = list(el)
    if len(kids) != 2:
        return _kids(el)
    base, over = _node(kids[0]), _node(kids[1])
    raw = _text(kids[1])
    if el.attrib.get("accent") == "true" or raw in ACCENT_CMD:
        return "\\" + ACCENT_CMD.get(raw, "bar") + "{" + base + "}"
    return r"\overset{" + over + "}{" + base + "}"


def _munder(el: ET.Element) -> str:
    kids = list(el)
    if len(kids) != 2:
        return _kids(el)
    base, under = _node(kids[0]), _node(kids[1])
    if base in BIG:
        return base + "_{" + under + "}"
    return r"\underset{" + under + "}{" + base + "}"


def _munderover(el: ET.Element) -> str:
    kids = list(el)
    if len(kids) != 3:
        return _kids(el)
    base, under, over = _node(kids[0]), _node(kids[1]), _node(kids[2])
    if base in BIG:
        return base + "_{" + under + "}^{" + over + "}"
    return r"\underset{" + under + r"}{\overset{" + over + "}{" + base + "}}"


def _node(el: ET.Element) -> str:
    tag = _tag(el)
    if tag == "mi":
        return _mi(el)
    if tag == "mn":
        return _mn(el)
    if tag == "mo":
        return _mo(el)
    if tag == "mtext":
        return _mtext(_text(el))
    if tag == "ms":
        return r"\text{" + _text(el) + "}"
    if tag == "mrow":
        return _kids(el)
    if tag == "math":
        return _kids(el)
    if tag == "mspace":
        return r"\;"
    if tag == "mstyle":
        return _mstyle(el)
    if tag == "msup":
        kids = list(el)
        if len(kids) != 2:
            return _kids(el)
        return _render_sup(_node(kids[0]), _node(kids[1]))
    if tag == "msub":
        kids = list(el)
        if len(kids) != 2:
            return _kids(el)
        return _render_sub(_node(kids[0]), _node(kids[1]))
    if tag == "msubsup":
        kids = list(el)
        if len(kids) != 3:
            return _kids(el)
        base = _node(kids[0])
        return _render_sub(base, _node(kids[1])) + "^{" + _node(kids[2]) + "}"
    if tag == "mfrac":
        kids = list(el)
        if len(kids) != 2:
            return _kids(el)
        num, den = _node(kids[0]), _node(kids[1])
        if el.attrib.get("bevelled") == "true":
            return num + "/" + den
        return r"\frac{" + num + "}{" + den + "}"
    if tag == "msqrt":
        return r"\sqrt{" + _kids(el) + "}"
    if tag == "mroot":
        kids = list(el)
        if len(kids) != 2:
            return _kids(el)
        return r"\sqrt[" + _node(kids[1]) + "]{" + _node(kids[0]) + "}"
    if tag == "mfenced":
        return _mfenced(el)
    if tag == "mtable":
        return _mtable(el)
    if tag in ("mtr", "mtd"):
        return _kids(el)
    if tag == "mover":
        return _mover(el)
    if tag == "munder":
        return _munder(el)
    if tag == "munderover":
        return _munderover(el)
    if tag in ("maction", "semantics", "annotation", "mpadded", "mphantom", "menclose"):
        return _kids(el)
    raise ValueError(f"未登记的 MathML 标签：<{tag}>")


def convert(math_xml: str, display: bool = False) -> str:
    """把 <math>…</math> 字符串转成 LaTeX（含 $ 或 $$ 定界符）。"""
    root = ET.fromstring(math_xml)
    body = _join(_node(c) for c in root) if _tag(root) == "math" else _node(root)
    body = re.sub(r"\s{2,}", " ", body).strip()
    delim = "$$" if display else "$"
    return delim + body + delim


if __name__ == "__main__":
    import sys

    src = sys.stdin.read()
    print(convert(src, display="--display" in sys.argv))
