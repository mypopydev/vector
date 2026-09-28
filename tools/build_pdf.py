#!/usr/bin/env python3
"""把 cn-book/ 下的 Markdown 译稿排成一本中文 PDF。

用法：
    python3 tools/build_pdf.py                  # -> dist/vector-cn.pdf
    python3 tools/build_pdf.py -o /tmp/x.pdf
    python3 tools/build_pdf.py --keep           # 保留中间产物 dist/build/
    python3 tools/build_pdf.py --no-page-marks  # 页边不标原版页码

依赖：pandoc、XeLaTeX（TeX Live + ctex）。
尚缺章节时只跳过并告警，方便中途试排。
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import shutil
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SRC = REPO / "cn-book"
TOOLS = REPO / "tools"

BOOK_TITLE = "向量：一个关于空间、时间与数学变换的惊奇故事"
BOOK_SUBTITLE = "Vector: A Surprising Story of Space, Time, and Mathematical Transformation"
BOOK_AUTHOR = "罗宾·阿里安罗德（Robyn Arianrhod） 著"

FRONT = [
    "0.译本说明.md",
]
BODY = [
    "1.名家推荐.md",
    "2.作者简介.md",
    "3.献词.md",
    "4.序言.md",
    "5.第1章-代数的解放.md",
    "6.第2章-微积分的登场.md",
    "7.第3章-向量的构想.md",
    "8.第4章-理解空间与存储.md",
    "9.第5章-出人意料的新角色与缓慢的接受.md",
    "10.第6章-泰特与麦克斯韦.md",
    "11.第7章-从四元数到向量.md",
    "12.第8章-向量分析终成正果.md",
    "13.第9章-从空间到时空.md",
    "14.第10章-弯曲的空间与不变的距离.md",
    "15.第11章-张量的发明.md",
    "16.第12章-万物汇聚.md",
    "17.第13章-后来发生了什么.md",
]
BACK = [
    "18.结语.md",
    "19.时间线.md",
    "20.致谢.md",
    "21.注释.md",
    "22.索引.md",
]

# 每个文件期望的章号：13 章依次是 1–13，其余（译本说明/序言/结语/时间线/致谢/
# 注释/索引）统一算 0 —— 正好让序言的图排成「图 0.1/0.2/0.3」，与原书一致。
CHAPTER_NO = {
    "4.序言.md": 0,
    "5.第1章-代数的解放.md": 1,
    "6.第2章-微积分的登场.md": 2,
    "7.第3章-向量的构想.md": 3,
    "8.第4章-理解空间与存储.md": 4,
    "9.第5章-出人意料的新角色与缓慢的接受.md": 5,
    "10.第6章-泰特与麦克斯韦.md": 6,
    "11.第7章-从四元数到向量.md": 7,
    "12.第8章-向量分析终成正果.md": 8,
    "13.第9章-从空间到时空.md": 9,
    "14.第10章-弯曲的空间与不变的距离.md": 10,
    "15.第11章-张量的发明.md": 11,
    "16.第12章-万物汇聚.md": 12,
    "17.第13章-后来发生了什么.md": 13,
}

H1 = re.compile(r"^#\s+(.*)$", re.M)
PAGE_MARK = re.compile(r"<!--p([^>]+)-->")
SECTION_BREAK = re.compile(r"^•\s*•\s*•$", re.M)
# split() 会把捕获组也塞进结果里，所以这里只能是「一个」非捕获组
MATH_SPAN = re.compile(
    r"(\$\$.+?\$\$|(?<!\$)\$(?![\s0-9])(?:[^$\n])+?(?<![\s])\$(?!\$))", re.S
)

# 正文（数学环境之外）出现的希腊字母：正文字体没有希腊字形，会报 Missing character。
# 交给 build_pdf.py 换成数学模式，而不是在 header.tex 里用 newunicodechar
# （活动字符会与 ctex 加载的 microtype 冲突）。
GREEK = {
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon",
    "ζ": "zeta", "η": "eta", "ο": "omicron", "θ": "theta", "ι": "iota", "κ": "kappa",
    "λ": "lambda", "μ": "mu", "ν": "nu", "ξ": "xi", "π": "pi",
    "ρ": "rho", "σ": "sigma", "τ": "tau", "υ": "upsilon", "φ": "varphi",
    "ϕ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega",
    "Γ": "Gamma", "Δ": "Delta", "Θ": "Theta", "Λ": "Lambda", "Ξ": "Xi",
    "Π": "Pi", "Σ": "Sigma", "Φ": "Phi", "Ψ": "Psi", "Ω": "Omega",
}
# 正文里出现的数学符号：Latin Modern Roman 没有这些字形（实测 ∙ U+2219 缺字形）
SYMBOLS = {
    "∙": r"\cdot", "⋅": r"\cdot", "⊗": r"\otimes", "⊕": r"\oplus",
    "≡": r"\equiv", "≈": r"\approx", "≠": r"\neq", "≤": r"\leq",
    "≥": r"\geq", "√": r"\sqrt{}", "∞": r"\infty", "∂": r"\partial",
    "∫": r"\int", "∬": r"\iint", "∭": r"\iiint", "∇": r"\nabla",
    "⇒": r"\Rightarrow", "⇔": r"\Leftrightarrow", "⟹": r"\Longrightarrow",
    "⟸": r"\Longleftarrow",
    "→": r"\to", "±": r"\pm", "′": "'", "″": "''", "´": "'", "⊲": r"\vartriangleleft", "∧": r"\wedge", "∨": r"\vee",
    # 牛顿式点记号：ẋ ẍ ẏ
    "ẋ": r"\dot{x}", "ẍ": r"\ddot{x}", "ẏ": r"\dot{y}", "Ẑ": r"\dot{Z}",
    # 黑体/空心字母还有一批独立码位，不在 U+1D504 起的那段连续区里
    "ℌ": r"\mathfrak{H}", "ℭ": r"\mathfrak{C}", "ℜ": r"\mathfrak{R}",
    "ℑ": r"\mathfrak{I}", "ℤ": r"\mathbb{Z}", "ℝ": r"\mathbb{R}",
    "ℂ": r"\mathbb{C}", "ℕ": r"\mathbb{N}", "ℚ": r"\mathbb{Q}",
}
# 格拉斯曼用的哥特体（Fraktur）字母，Latin Modern Math 有 \mathfrak
for _i, _L in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    SYMBOLS[chr(0x1D504 + _i)] = r"\mathfrak{" + _L + "}"
for _i, _L in enumerate("abcdefghijklmnopqrstuvwxyz"):
    SYMBOLS[chr(0x1D51E + _i)] = r"\mathfrak{" + _L + "}"
TEXT_MATH_RE = re.compile("[" + "".join(GREEK) + "".join(SYMBOLS) + "]")


def text_math_symbols(text: str) -> str:
    """只替换数学环境之外的希腊字母与数学符号。"""
    # ― (U+2015 横杠) 正文字体没有，换成同表破折号的 — (U+2014)
    text = text.replace("\u2015", "\u2014")
    def repl(m: re.Match) -> str:
        ch = m.group(0)
        # GREEK 的值是命令名（alpha），要补反斜杠；
        # SYMBOLS 的值已经带反斜杠（\cdot），再补就变成 \\cdot 了
        return f"$\\{GREEK[ch]}$" if ch in GREEK else f"${SYMBOLS[ch]}$"

    parts = MATH_SPAN.split(text)
    for i in range(0, len(parts), 2):  # split 后偶数下标是非数学段
        parts[i] = TEXT_MATH_RE.sub(repl, parts[i])
    return "".join(parts)


def load(name: str) -> str:
    return (SRC / name).read_text(encoding="utf-8")


def git_stamp() -> dict[str, object]:
    """取当前版本与提交，用于给 PDF 打构建印记。

    PDF 从网上流出去之后就没有来源信息了，读者（和我们自己）无法判断手上
    这份是哪一个版本，所以把 tag、commit、是否含未提交改动一并烧进 PDF：
    既印在扉页，也写进 PDF 元数据（pdfinfo 可读）。
    """
    def git(*args: str) -> str:
        try:
            p = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
        except FileNotFoundError:
            return ""
        return p.stdout.strip() if p.returncode == 0 else ""

    version = git("describe", "--tags", "--always", "--dirty")
    commit = git("rev-parse", "--short=7", "HEAD")
    dirty = version.endswith("-dirty")
    if dirty:
        version = version[: -len("-dirty")]
    return {
        "version": version or "unknown",
        "commit": commit or "unknown",
        "dirty": dirty,
    }


def stamp_line(stamp: dict[str, object], date: str) -> str:
    # 用中文逗号而不是「 · 」分隔：xeCJK 会吃掉标点与西文之间的空格，
    # 排出来是「· git」这种粘连的样子。
    s = f"译本版本 {stamp['version']}，git {stamp['commit']}，{date}"
    if stamp["dirty"]:
        s += "（含未提交改动）"
    return s


def write_metadata_tex(path: pathlib.Path, stamp: dict[str, object], date: str) -> None:
    """写一段只含 ASCII 的 \\hypersetup，把版本信息塞进 PDF 元数据。

    用 \\AtBeginDocument 是因为 pandoc 模板里 \\hypersetup 排在 header-includes
    之后，直接写会被它覆盖掉。元数据字符串保持 ASCII：中文进 pdfstring 会被
    \\pdfstringdef 转义成一串八进制，pdfinfo 里看不出是什么。
    """
    keywords = f"vector-cn; {stamp['version']}; {stamp['commit']}"
    if stamp["dirty"]:
        keywords += "; dirty"
    subject = f"vector-cn {stamp['version']} ({stamp['commit']}) built {date}"
    path.write_text(
        "% 由 tools/build_pdf.py 生成，勿手改\n"
        "\\AtBeginDocument{%\n"
        f"  \\hypersetup{{pdfkeywords={{{keywords}}},"
        f"pdfsubject={{{subject}}},"
        # 下划线在 pdfstring 里会被吞掉，所以这里不写 build_pdf.py 原样
        f"pdfcreator={{tools/build-pdf.py}}}}\n"
        "}\n",
        encoding="utf-8",
    )


NOTES_DEF = re.compile(r"^\[\^(ch\d\dn\d+)\]:\s*(.*)$")
NOTES_GROUP = re.compile(r"^##\s+")


BARE_URL = re.compile(r"(?<![<(])(https?://[^\s，。；）】〉>\"'\]]+)")


def linkify_urls(text: str) -> str:
    r"""把裸 URL 包成 Markdown 自动链接，pandoc 才会输出 \url{} 让 xurl 断行。

    脚注里的长 URL 不这么做就会冲出纸面被裁掉。
    """
    return BARE_URL.sub(lambda m: f"<{m.group(1)}>", text)


def render_notes(text: str) -> str:
    """把注释里的 [^id]: 定义渲染成「1. 2. 3.」编号列表。

    脚注定义已经分发到各章文件（正文出当页脚注），这里再排一遍会和它们重复，
    所以书末汇编只保留正文、去掉定义标记。
    """
    out: list[str] = []
    counter: dict[str, int] = {}
    for line in text.splitlines():
        if NOTES_GROUP.match(line):
            counter.clear()
            out.append(line)
            continue
        m = NOTES_DEF.match(line)
        if m:
            key = m.group(1)[:4]
            counter[key] = counter.get(key, 0) + 1
            out.append(f"{counter[key]}. {m.group(2)}")
            continue
        out.append(line[4:] if line.startswith("    ") else line)
    return "\n".join(out)


def strip_unsafe_marks(text: str) -> str:
    """去掉放在 \marginpar 会炸的位置上的分页标记。

    知识框（infobox 是 tcolorbox，内部不是 outer par mode）和脚注定义里
    出现 \marginpar 会报 "Not in outer par mode" 并中断构建。
    """
    out: list[str] = []
    in_box = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("::: {.infobox}"):
            in_box = True
        elif stripped == ":::" and in_box:
            in_box = False
        unsafe = in_box or stripped.startswith("[^") or line.startswith("    ")
        if unsafe and PAGE_MARK.search(line):
            line = PAGE_MARK.sub("", line)
        out.append(line)
    return "\n".join(out)


def build_merged(page_marks: bool) -> tuple[str, list[str], list[tuple[str, float]]]:
    """按书序合并译稿，返回 (合并文本, 缺失章节, 各文件输出/输入字符比)。"""
    parts: list[str] = []
    missing: list[str] = []
    ratios: list[tuple[str, float]] = []

    for name in FRONT + BODY + BACK:
        path = SRC / name
        if not path.exists():
            missing.append(name)
            continue
        text = path.read_text(encoding="utf-8")
        text = strip_unsafe_marks(text)
        if page_marks:
            text = PAGE_MARK.sub(r"\\origpage{\1}", text)
        else:
            text = PAGE_MARK.sub("", text)
        text = SECTION_BREAK.sub(r"\\secbreak", text)
        text = text_math_symbols(text)
        text = linkify_urls(text)
        if name == "21.注释.md":
            text = render_notes(text)
        ratios.append((name, len(text) / max(len(path.read_text(encoding="utf-8")), 1)))
        # 章号、图号、脚注号全部显式设定：secnumdepth=-1 时 \chapter 不步进计数器，
        # 这样每章的图都从「章.1」开始、脚注都从 1 开始（与原书及书末汇编一致）
        want = CHAPTER_NO.get(name, 0)
        parts.append(
            f"\\setcounter{{chapter}}{{{want}}}"
            f"\\setcounter{{figure}}{{0}}"
            f"\\setcounter{{footnote}}{{0}}\n\n" + text.strip()
        )

    # 不用插 \newpage：每个文件都以 # 开头，pandoc 会输出 \chapter{}，
    # 它本身就另起一页；两个换页叠在一起会产生整页空白
    return "\n\n".join(parts), missing, ratios


def run_pandoc(
    src: pathlib.Path, out: pathlib.Path, stamp: str, meta: pathlib.Path | None = None
) -> int:
    cmd = [
        "pandoc", str(src),
        "-o", str(out),
        "--pdf-engine=xelatex",
        f"--resource-path={REPO}",
        "--lua-filter", str(TOOLS / "infobox.lua"),
        "-H", str(TOOLS / "header.tex"),
        *(["-H", str(meta)] if meta else []),
        "--toc", "--toc-depth=1",
        "-V", "documentclass=ctexbook",
        # 钉住 fontset：不钉的话 ctex 每次按机器自动判定，换机器字体就变
        "-V", "classoption=fontset=macold",
        "-V", "CJKmainfont=Songti SC",
        "-V", "papersize=a4",
        "-V", "fontsize=11pt",
        "-V", "linestretch=1.25",
        "-V", f"title={BOOK_TITLE}",
        "-V", f"subtitle={BOOK_SUBTITLE}",
        "-V", f"author={BOOK_AUTHOR}",
        # 扉页那行「日期」改印版本印记：PDF 一旦离开仓库就没有来源信息了
        "-V", f"date={stamp}",
        "-V", "titlepage=true",
        "-V", "colorlinks=true",
        "-V", "linkcolor=black",
        "-V", "toccolor=black",
    ]
    print("  pandoc --pdf-engine=xelatex …")
    proc = subprocess.run(cmd, capture_output=True, text=True)
    # 日志要留在 dist/ 下（dist/build 会被清掉），check_baseline.py 要靠它查缺字形
    (REPO / "dist" / "pandoc.log").write_text(proc.stderr, encoding="utf-8")
    warns = [l for l in proc.stderr.splitlines() if "Missing character" in l]
    if warns:
        print(f"  ⚠ 缺字形 {len(warns)} 条：")
        for w in sorted(set(warns))[:10]:
            print("     " + w.replace("[WARNING] ", ""))
    if proc.returncode != 0:
        print(proc.stderr[-4000:], file=sys.stderr)
        sys.exit("pandoc 构建失败")
    return len(warns)


def main() -> None:
    ap = argparse.ArgumentParser(description="构建中文版 PDF")
    ap.add_argument("-o", "--output", type=pathlib.Path)
    ap.add_argument("--keep", action="store_true", help="保留中间产物")
    ap.add_argument("--no-page-marks", action="store_true", help="页边不标原版页码")
    args = ap.parse_args()

    dist = REPO / "dist"
    dist.mkdir(exist_ok=True)
    out = args.output or dist / "vector-cn.pdf"

    merged, missing, ratios = build_merged(not args.no_page_marks)
    if missing:
        print(f"  ⚠ 尚缺 {len(missing)} 个文件（本次先跳过）：{', '.join(missing)}")

    # 兜底：合并时若误吞正文，构建仍会「成功」，只有页数会悄悄变少
    thin = [(n, r) for n, r in ratios if r < 0.95 or r > 1.6]
    if thin:
        print("  ⚠ 以下文件合并后长度异常，疑似被吞或被改写：")
        for n, r in thin:
            print(f"     {n}  输出/输入 = {r:.2%}")

    work = dist / "build"
    work.mkdir(exist_ok=True)
    src = work / "book.md"
    src.write_text(merged, encoding="utf-8")

    date = dt.date.today().isoformat()
    stamp = git_stamp()
    line = stamp_line(stamp, date)
    print(f"  版本印记：{line}")
    meta = work / "stamp-metadata.tex"
    write_metadata_tex(meta, stamp, date)
    glyph_warns = run_pandoc(src, out, line, meta)

    report = {
        "built": date,
        "version": stamp["version"],
        "commit": stamp["commit"],
        "dirty": stamp["dirty"],
        "size_bytes": out.stat().st_size,
        "glyph_warnings": glyph_warns,
        "missing_files": missing,
        "min_content_ratio": min((r for _, r in ratios), default=1.0),
        "max_content_ratio": max((r for _, r in ratios), default=1.0),
    }
    (dist / "build-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    if not args.keep:
        shutil.rmtree(work, ignore_errors=True)
    print(f"\n✅ {out}  ({out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
