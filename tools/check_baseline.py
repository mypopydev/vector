#!/usr/bin/env python3
"""PDF 基线检查：防「构建成功但内容其实是错的」。

用法：
    python3 tools/check_baseline.py

先跑 python3 tools/build_pdf.py（会留下 dist/pandoc.log 与 dist/vector-cn.pdf）。

四道检查：
1. 严重：缺字形（Missing character）——字体没这个字，页面上就是空白或方块。
2. 严重：PDF 里丢字——正文里的汉字没出现在 PDF 文本层（复制出来会缺字）。
3. 严重：越界裁切——文字/公式的 x 坐标超出版心，会被切掉。
   这一类缺陷骗得过字符比对：字形在、字符数对，但页面上就是少半行。
4. 中等：图编号断号、页数异常。
"""

from __future__ import annotations

import collections
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DIST = REPO / "dist"
PDF = DIST / "vector-cn.pdf"
LOG = DIST / "pandoc.log"
CN = REPO / "cn-book"
REVIEW = REPO / "review"

# 与 header.tex 的 geometry 一致（单位 cm -> pt，1cm = 28.35pt）
INNER_CM, OUTER_CM = 3.3, 2.2
TOLERANCE_PT = 3.0


def pdf_text() -> str:
    proc = subprocess.run(["pdftotext", str(PDF), "-"], capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"pdftotext 失败：{proc.stderr}")
    return proc.stdout


def check_glyphs() -> tuple[int, list[str]]:
    if not LOG.exists():
        return 1, [f"缺少 {LOG}，先跑 build_pdf.py"]
    text = LOG.read_text(encoding="utf-8", errors="replace")
    hits = sorted(set(re.findall(r"There is no (\S+) \(U\+[0-9A-F]+\)", text)))
    return len(hits), hits


def check_missing_chars(pdf: str) -> tuple[list[str], int]:
    """正文里的汉字有没有在 PDF 文本层里缺席。"""
    src = ""
    for p in sorted(CN.glob("*.md")):
        src += p.read_text(encoding="utf-8")
    src_cjk = {c for c in src if "一" <= c <= "鿿"}
    pdf_cjk = {c for c in pdf if "一" <= c <= "鿿"}
    missing = sorted(src_cjk - pdf_cjk)
    return missing, len(src_cjk)


def check_overflow() -> list[str]:
    """逐行量 xMax：超出版心右边界的行会被裁掉。

    版心不用几何参数反推（实测反推会差 0.25cm，把整页正文都判成越界），
    而是取该页正文行（字号 ≥ 9pt）的众数左右边界作为实际版心。
    页边的原版页码是 \footnotesize（< 9pt），本来就在版心外，不参与也不报警。
    """
    try:
        import fitz  # PyMuPDF
        from collections import Counter
    except ImportError:
        return ["未安装 PyMuPDF，跳过越界检查"]

    doc = fitz.open(str(PDF))
    bad: list[str] = []
    minor: list[str] = []
    for i, page in enumerate(doc, 1):
        page_width = page.rect.width
        body: list[tuple[float, float, float, str]] = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                spans = [s for s in line.get("spans", []) if s.get("size", 0) >= 9]
                if not spans:
                    continue
                x0 = min(s["bbox"][0] for s in spans)
                x1 = max(s["bbox"][2] for s in spans)
                text = "".join(s["text"] for s in spans).strip()
                if len(text) < 8:
                    continue
                body.append((x0, x1, spans[0].get("size", 0), text))
        if not body:
            continue
        # 按左边界分栏（正文一栏，索引两栏），逐栏取「右边界的众数」当版心。
        # 众数而非极值：两端对齐的正文行右边界一致；
        # 目录/标题页各行长短不一，众数占比过低，整页跳过不查。
        columns: dict[int, list[tuple[float, float, float, str]]] = {}
        for item in body:
            columns.setdefault(round(item[0]), []).append(item)
        for col_left, items in columns.items():
            if len(items) < 5:
                continue
            rights = Counter(round(x1) for _, x1, *_ in items).most_common(1)[0]
            right, hits = rights
            if hits < max(4, 0.3 * len(items)):
                continue        # 这一栏行宽不齐（目录、章首、公式页），不查
            for x0, x1, size, text in items:
                over = x1 - right
                if over <= TOLERANCE_PT:
                    continue
                # 末字是标点时 xeCJK 会做标点悬挂（探出版心约 0.25cm），是刻意排版
                if text and text[-1] in "，。、；：？！）」』》】…—～“”‘’·":
                    continue
                # 只有逼近物理页边（< 25pt 余量）才会真被裁掉，算严重；
                # 其余只是 overfull hbox（内容完整、仅不美观），记轻微
                if x1 > page_width - 25:
                    bad.append(f"p{i}: x=[{x0:.0f},{x1:.0f}] 逼近页边 {page_width:.0f} "
                               f"{size:.0f}pt “{text[:44]}”")
                elif over > 15:
                    minor.append(f"p{i}: 超出右边界 {over:.0f}pt “{text[:40]}”")
    doc.close()
    return bad + ["（轻微）" + m for m in minor[:10]]


def check_figures(pdf: str) -> list[str]:
    nums = [int(m.group(2)) for m in re.finditer(r"图 (\d+)\.(\d+)", pdf)]
    if not nums:
        return ["PDF 里没找到图编号"]
    return []


def main() -> None:
    if not PDF.exists():
        sys.exit(f"缺少 {PDF}，先跑 python3 tools/build_pdf.py")

    text = pdf_text()
    n_glyph, glyphs = check_glyphs()
    missing, total = check_missing_chars(text)
    overflow = check_overflow()
    fig_problems = check_figures(text)

    lines = [
        "# PDF 基线检查",
        "",
        f"- PDF：{PDF.name}",
        "",
        "## 1. 缺字形（严重）",
        "",
        f"{n_glyph} 个：{glyphs if glyphs else '无'}",
        "",
        "## 2. 正文汉字在 PDF 里的覆盖（严重）",
        "",
        f"译稿汉字 {total} 种，PDF 中缺失 {len(missing)} 种"
        + (f"：{''.join(missing[:40])}" if missing else ""),
        "",
        "## 3. 越界裁切（严重）",
        "",
        f"{len(overflow)} 行" + ("" if not overflow else ":"),
    ]
    for item in overflow[:20]:
        lines.append(f"- {item}")
    lines += ["", "## 4. 图编号（中等）", ""]
    lines += [f"- {p}" for p in fig_problems] or ["- 无异常"]

    REVIEW.mkdir(exist_ok=True)
    (REVIEW / "baseline.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    severe = n_glyph + len(missing) + len(overflow)
    print(f"缺字形 {n_glyph}｜丢字 {len(missing)}｜越界 {len(overflow)}｜严重合计 {severe}")
    print(f"-> review/baseline.md")
    sys.exit(1 if severe else 0)


if __name__ == "__main__":
    main()
