#!/usr/bin/env python3
"""把原书 epub 的 XHTML 抽成 Markdown，供翻译与结构校验使用。

用法：
    python3 tools/extract_epub.py [--epub PATH] [--out en] [--images images]

产物：
    en/<stem>.md        每个 xhtml 一个 Markdown（含 <!--p123--> 原版分页锚点）
    en/manifest.json    各文件的字数/段数/图数/公式数/尾注数统计
    images/*.jpg        原书插图

规则依据 epub 实际使用的 CSS 类（见 tools/extract_epub.py 顶部 CLASS_MAP 注释），
不是猜的：p.indent/p.noindent 段落、p.eqn 行间公式、p.figcap 图注、
p.nlist 尾注、p.index1 索引、div.box 知识框、p.hang_1a 时间线。
MathML 交给 tools/mathml2tex.py 转成 LaTeX。
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import zipfile
from html.parser import HTMLParser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mathml2tex import convert  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parent.parent

MATH_RE = re.compile(r"<math\b.*?</math>", re.S)
# 行间公式段（p.eqn）里的公式要排成 $$…$$
EQN_RE = re.compile(r'<p\b[^>]*class="[^"]*\beqn\b[^"]*"[^>]*>.*?</p>', re.S)
PAGEBREAK_RE = re.compile(
    r'<span[^>]*epub:type="pagebreak"[^>]*title="([^"]*)"[^>]*/>', re.S
)

MATH_PLACEHOLDER = "\x00MATH{}\x00"


# ---------------------------------------------------------------------------
# XHTML -> Markdown
# ---------------------------------------------------------------------------
class Extractor(HTMLParser):
    def __init__(self, latex_by_id: dict[int, str], images_dir: str) -> None:
        super().__init__(convert_charrefs=True)
        self.latex = latex_by_id
        self.images_dir = images_dir
        self.lines: list[str] = []
        self.buf: list[str] = []
        self.stats = {"p": 0, "fig": 0, "eq": 0, "note": 0}
        self.block: str | None = None        # 当前块类型
        self.heading: int | None = None
        self.in_figcaption = False
        self.caption: list[str] = []
        self.pending_page: str | None = None
        self.in_box = False
        self.list_stack: list[dict] = []
        self.quote_depth = 0
        self.notes_file = False
        self.skip_text = False        # 尾注编号里的数字由 id 决定，正文数字要丢掉
        self.pending_note_id: str | None = None
        self.sup_open = False

    # ---------- helpers ----------
    @staticmethod
    def _attr(attrs, name: str) -> str:
        for k, v in attrs:
            if k == name:
                return v or ""
        return ""

    def _text(self) -> str:
        s = "".join(self.buf)
        self.buf = []
        return re.sub(r"\s+", " ", s).strip()

    def _emit(self, text: str = "") -> None:
        self.lines.append(text)

    def _emit_page(self) -> None:
        if self.pending_page:
            self.lines.append(f"<!--p{self.pending_page}-->")
            self.pending_page = None

    def _push(self, text: str) -> None:
        """图注里的内容（含行内标记）也要进 caption，不能漏进正文缓冲。"""
        if self.in_figcaption:
            self.caption.append(text)
        else:
            self.buf.append(text)

    def _open_inline(self, marker: str) -> None:
        self._push(marker)

    def _close_inline(self, marker: str) -> None:
        self._push(marker)

    def _flush_paragraph(self, prefix: str = "") -> str:
        text = self._text()
        if not text:
            return ""
        self._emit_page()
        self.lines.append(prefix + text)
        self._emit()
        return text

    # ---------- tags ----------
    def handle_starttag(self, tag, attrs):
        cls = self._attr(attrs, "class")
        clss = set(cls.split())
        ident = self._attr(attrs, "id")

        if tag == "span" and "pagebreak" in self._attr(attrs, "epub:type"):
            self.pending_page = self._attr(attrs, "title")
            return
        if tag == "span":
            return
        if tag == "img":
            src = os.path.basename(self._attr(attrs, "src"))
            width = self._width_attr(clss)
            self._emit_page()
            self.lines.append(f"![]({self.images_dir}/{src}){width}")
            self._emit()
            return
        if tag == "figure":
            self.block = "figure"
            self.caption = []
            return
        if tag == "figcaption":
            self.in_figcaption = True
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading = int(tag[1])
            return
        if tag == "blockquote":
            self.quote_depth += 1
            return
        if tag in ("ul", "ol"):
            self.list_stack.append({"ordered": tag == "ol", "index": 0})
            return
        if tag == "div" and "box" in clss:
            self.in_box = True
            self._emit_page()
            self.lines.append("::: {.infobox}")
            self._emit()
            return
        if tag == "div":
            return
        if tag == "p":
            self.block = self._block_kind(clss)
            return
        if tag in ("i", "em"):
            self._open_inline("*")
        elif tag in ("b", "strong"):
            self._open_inline("**")
        elif tag == "sup":
            # 先放占位符：若紧跟的是尾注引用，这对 ^ 要一并去掉
            self._open_inline("\x01")
        elif tag == "sub":
            self._open_inline("~")
        elif tag == "a":
            self._handle_anchor(ident, self._attr(attrs, "href"))
        elif tag == "br":
            self.buf.append(" ")

    def handle_endtag(self, tag):
        if tag == "span":
            return
        if tag == "img":
            return
        if tag == "a":
            self.skip_text = False
            return
        if tag == "figure":
            cap = re.sub(r"\s+", " ", "".join(self.caption)).strip()
            # 图注里出现 $$行间公式$$ 会被 pandoc 塞进 \caption{} 而编译失败
            # （原书 fig 7.1 / fig 8.1 的图注就是如此），图注只能用行内公式
            cap = cap.replace("$$", "$")
            if cap:
                for i in range(len(self.lines) - 1, -1, -1):
                    if self.lines[i].startswith("!["):
                        self.lines[i] = self.lines[i].replace("![](", f"![{cap}](")
                        break
            self.block = None
            self.in_figcaption = False
            self.stats["fig"] += 1
            return
        if tag == "figcaption":
            self.in_figcaption = False
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = self._text()
            if text:
                self._emit_page()
                level = self.heading or 1
                self.lines.append("#" * level + " " + text)
                self._emit()
            self.heading = None
            return
        if tag == "blockquote":
            self.quote_depth = max(0, self.quote_depth - 1)
            return
        if tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
                self._emit()
            return
        if tag == "li":
            text = self._text()
            if text and self.list_stack:
                frame = self.list_stack[-1]
                frame["index"] += 1
                marker = f"{frame['index']}. " if frame["ordered"] else "- "
                self._emit_page()
                self.lines.append(marker + text)
            return
        if tag == "div":
            if self.in_box:
                self.in_box = False
                self.lines.append(":::")
                self._emit()
            return
        if tag == "p":
            self._close_block()
            return
        if tag in ("i", "em"):
            self._close_inline("*")
        elif tag in ("b", "strong"):
            self._close_inline("**")
        elif tag == "sup":
            self._close_inline("\x01")
        elif tag == "sub":
            self._close_inline("~")

    def handle_data(self, data):
        if self.skip_text:
            return
        self._push(data)

    def _handle_anchor(self, ident: str, href: str) -> None:
        """尾注引用/定义都挂在 <a> 的 id 上：ch01rfn1 / ch01fn1。"""
        m = re.fullmatch(r"(ch\d\d)rfn(\d+)", ident)
        if m:  # 正文里的引用
            self.buf.append(f"[^{m.group(1)}n{m.group(2)}]")
            self.skip_text = True
            return
        m = re.fullmatch(r"(ch\d\d)fn(\d+)", ident)
        if m:  # 注释文件里的定义
            self.pending_note_id = f"{m.group(1)}n{m.group(2)}"
            self.skip_text = True
            return

    # ---------- block classification ----------
    @staticmethod
    def _width_attr(clss: set[str]) -> str:
        for c in ("wid20", "wid50", "wid60", "wid80"):
            if c in clss:
                return '{width="%s%%"}' % c[3:]
        return ""

    def _block_kind(self, clss: set[str]) -> str:
        if "nlist" in clss:
            return "note"
        if "nlist2" in clss or "nlist2a" in clss:
            return "note-cont"
        if "eqn" in clss:
            return "eqn"
        if "figcap" in clss:
            return "figcap"
        if "boxhead" in clss:
            return "boxhead"
        if "star" in clss:
            return "star"
        if "subh" in clss:
            return "subh"
        if "hang_1a" in clss:
            return "timeline"
        if "index1" in clss or "index1t" in clss:
            return "index"
        if "extract" in clss or "extract100" in clss:
            return "quote"
        if "tlist" in clss:
            return "toc"
        return "para"

    def _close_block(self) -> None:
        kind = self.block or "para"
        text = self._text()
        prefix = "> " if (self.quote_depth or kind == "quote") else ""

        if kind == "figcap":
            self.block = None
            return
        if not text:
            self.block = None
            return

        if kind == "eqn":
            self.stats["eq"] += 1
            self._emit_page()
            # 公式编号（<span class="eqno">(1)</span>）紧跟在公式后。
            # 这一类里有的含 MathML（已转成 $$…$$），有的只是样式化文本
            # （<i>/<sub>/<sup>），后者要单独包一层，否则会排成左对齐的普通段落，
            # 而原书是居中的行间公式。
            if "$$" in text:
                self.lines.append(text)
            else:
                self.lines.append("::: {.displayeq}")
                self.lines.append("")
                self.lines.append(text)
                self.lines.append("")
                self.lines.append(":::")
            self._emit()
        elif kind == "note":
            self.stats["note"] += 1
            self._emit_page()
            # 「1.Letter from …」里的编号来自 <a id="ch01fn1">，转成 pandoc 脚注定义
            text = re.sub(r"^\s*\.\s*", "", text)
            prefix = f"[^{self.pending_note_id}]: " if self.pending_note_id else ""
            self.pending_note_id = None
            self.lines.append(prefix + text)
            self._emit()
        elif kind == "note-cont":
            self.lines.append("    " + text)
            self._emit()
        elif kind == "boxhead":
            self.lines.append("**" + text + "**")
            self._emit()
        elif kind == "star":
            self.lines.append("• • •")
            self._emit()
        elif kind == "subh":
            self.lines.append("**" + text + "**")
            self._emit()
        elif kind in ("timeline", "index", "toc"):
            self.lines.append("- " + text)
        elif kind == "para":
            self.stats["p"] += 1
            self._emit_page()
            self.lines.append(prefix + text)
            self._emit()
        else:
            self.lines.append(prefix + text)
            self._emit()
        self.block = None

    # ---------- output ----------
    def result(self) -> str:
        text = "\n".join(self.lines)
        # <sup> 的占位符：包住尾注引用的那对 ^ 要去掉，其余还原成 ^
        text = re.sub(r"\x01\[\^([A-Za-z0-9]+)\]\x01", r"[^\1]", text)
        text = text.replace("\x01", "^")
        for key, tex in self.latex.items():
            text = text.replace(MATH_PLACEHOLDER.format(key), tex)
        # 图注里的行间公式要降级成行内公式：pandoc 会把 $$…$$ 塞进 \caption{} 而编译失败。
        # 两个前提：①必须在占位符替换之后做（替换前图注里只有 \x00MATHn\x00，看不到 $$）；
        # ②必须在 text 上做，不能回头用 self.lines 重建——self.lines 里还是占位符。
        text = "\n".join(
            re.sub(r"\$\$", "$", line) if line.startswith("![") else line
            for line in text.splitlines()
        )
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
        return text


def html_to_markdown(html: str, images_dir: str = "images", notes: bool = False) -> tuple[str, dict]:
    """返回 (Markdown, 统计字典)。"""
    latex_by_id: dict[int, str] = {}

    def _stash(m: re.Match, display: bool = False) -> str:
        idx = len(latex_by_id)
        latex_by_id[idx] = convert(m.group(0), display=display)
        return MATH_PLACEHOLDER.format(idx)

    # <head> 里的 <title> 与 MathJax 配置脚本会被当成正文，必须整段去掉
    html = re.sub(r"<head\b.*?</head>", "", html, flags=re.S)
    html = re.sub(r"<script\b.*?</script>", "", html, flags=re.S)
    html = EQN_RE.sub(lambda m: MATH_RE.sub(lambda mm: _stash(mm, True), m.group(0)), html)
    html = MATH_RE.sub(_stash, html)
    parser = Extractor(latex_by_id, images_dir)
    parser.notes_file = notes
    parser.feed(html)
    return parser.result(), parser.stats


# ---------------------------------------------------------------------------
# 驱动
# ---------------------------------------------------------------------------
SKIP = {"00_Nav", "01_Cover", "05_Titlepage", "07_Contents"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", default=None)
    ap.add_argument("--out", default=str(REPO / "en"))
    ap.add_argument("--images", default="images")
    args = ap.parse_args()

    epubs = [args.epub] if args.epub else sorted(REPO.glob("*.epub"))
    if not epubs:
        raise SystemExit("仓库根目录未找到 epub")
    epub = epubs[0]

    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    img_dir = REPO / args.images
    img_dir.mkdir(parents=True, exist_ok=True)

    manifest = []
    with zipfile.ZipFile(epub) as z:
        names = sorted(n for n in z.namelist() if n.startswith("OEBPS/xhtml/"))
        # 索引被拆成三个文件，合并成一个
        order = [n for n in names if not re.search(r"26_Index_[ab]\.xhtml$", n)]
        for name in order:
            stem = pathlib.Path(name).stem
            if stem in SKIP:
                continue
            html = z.read(name).decode("utf-8", errors="replace")
            if stem == "26_Index":
                parts = [html]
                for suffix in ("a", "b"):
                    p = f"OEBPS/xhtml/26_Index_{suffix}.xhtml"
                    if p in z.namelist():
                        parts.append(z.read(p).decode("utf-8", errors="replace"))
                html = "\n".join(parts)
            md, stats = html_to_markdown(html, args.images, notes=stem == "25_Notes")
            md += f"\n<!--stats: p={stats['p']} fig={stats['fig']} eq={stats['eq']} note={stats['note']}-->\n"
            (out_dir / f"{stem}.md").write_text(md, encoding="utf-8")
            manifest.append({
                "stem": stem,
                "path": f"en/{stem}.md",
                "chars": len(md),
                "words": len(re.sub(r"\s+", " ", md).split()),
                **stats,
            })

        for info in z.infolist():
            if not info.filename.startswith("OEBPS/images/"):
                continue
            base = os.path.basename(info.filename)
            if not base:
                continue
            (img_dir / base).write_bytes(z.read(info.filename))

    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    for m in manifest:
        print(f"{m['stem']:22s} words={m['words']:6d} p={m['p']:4d} "
              f"fig={m['fig']:3d} eq={m['eq']:3d} note={m['note']:4d}")


if __name__ == "__main__":
    main()
