#!/usr/bin/env python3
"""把 cn-book/ 译稿转成 MkDocs 用的 Markdown，输出到个人站点仓库。

用法：
    python3 tools/build_site.py                       # 生成到默认站点仓库
    python3 tools/build_site.py --target <站点路径>
    python3 tools/build_site.py --check               # 只校验已生成的内容
    python3 tools/build_site.py --nav                 # 打印要插入 mkdocs.yml 的导航片段

为什么需要转换：cn-book/ 是 pandoc 方言，站点用的是 Python-Markdown。
两边语法一致的（公式 $…$、脚注 [^id]:、标题）原样保留；
pandoc 特有的（图片 {width=} 属性、::: 围栏 div、^x^/~x~ 上下标）必须转换，
否则会显示成字面文字。

输出的图编号按「章.序号」显式写入（PDF 由 LaTeX 自动编号，网页没人给编号），
并把正文里的「图 N.M」引用做成锚点链接。
"""

from __future__ import annotations

import argparse
import pathlib
import posixpath
import re
import shutil
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
from build_pdf import CHAPTER_NO, linkify_urls, render_notes  # noqa: E402

DEFAULT_TARGET = pathlib.Path("/Users/barryjzhao/Sources/AI/mypopydev-web")
BOOK_DIR = pathlib.Path("docs/books/vector-zh")
IMG_DIR = pathlib.Path("docs/assets/images/vector")

# (cn-book 文件名, 网页 slug, 导航标题, 章号)
PAGES = [
    ("0.译本说明.md", "00-about-this-translation.md", "译本说明", 0),
    ("1.名家推荐.md", "01-praise.md", "名家推荐", 0),
    ("2.作者简介.md", "02-about-the-author.md", "作者简介", 0),
    ("3.献词.md", "03-dedication.md", "献词", 0),
    ("4.序言.md", "04-prologue.md", "序言", 0),
    ("5.第1章-代数的解放.md", "05-ch01-liberation-of-algebra.md", "第 1 章　代数的解放", 1),
    ("6.第2章-微积分的登场.md", "06-ch02-arrival-of-calculus.md", "第 2 章　微积分的登场", 2),
    ("7.第3章-向量的构想.md", "07-ch03-ideas-for-vectors.md", "第 3 章　向量的构想", 3),
    ("8.第4章-理解空间与存储.md", "08-ch04-space-and-storage.md", "第 4 章　理解空间（与存储）", 4),
    ("9.第5章-出人意料的新角色与缓慢的接受.md", "09-ch05-new-player-slow-reception.md",
     "第 5 章　出人意料的新角色与缓慢的接受", 5),
    ("10.第6章-泰特与麦克斯韦.md", "10-ch06-tait-and-maxwell.md", "第 6 章　泰特与麦克斯韦", 6),
    ("11.第7章-从四元数到向量.md", "11-ch07-quaternions-to-vectors.md", "第 7 章　从四元数到向量", 7),
    ("12.第8章-向量分析终成正果.md", "12-ch08-vector-analysis.md",
     "第 8 章　向量分析终成正果", 8),
    ("13.第9章-从空间到时空.md", "13-ch09-space-to-spacetime.md", "第 9 章　从空间到时空", 9),
    ("14.第10章-弯曲的空间与不变的距离.md", "14-ch10-curving-spaces.md",
     "第 10 章　弯曲的空间与不变的距离", 10),
    ("15.第11章-张量的发明.md", "15-ch11-inventing-tensors.md", "第 11 章　张量的发明", 11),
    ("16.第12章-万物汇聚.md", "16-ch12-everything-comes-together.md", "第 12 章　万物汇聚", 12),
    ("17.第13章-后来发生了什么.md", "17-ch13-what-happened-next.md", "第 13 章　后来发生了什么", 13),
    ("18.结语.md", "18-epilogue.md", "结语", 0),
    ("19.时间线.md", "19-timeline.md", "时间线", 0),
    ("20.致谢.md", "20-acknowledgments.md", "致谢", 0),
    ("21.注释.md", "21-notes.md", "注释（353 条）", 0),
    ("22.索引.md", "22-index.md", "索引（636 条）", 0),
]

# 图：带 {width="N%"} 的（多数）和不带的（注释里有一张）都要处理
IMG_RE = re.compile(
    r'^!\[(.*?)\]\((images/[^)]+?)\)(?:\{width="(\d+)%"\})?\s*$'
)
FIG_REF = re.compile(r"图\s?(\d+)\.(\d+)")
SECBREAK = re.compile(r"^•\s*•\s*•$", re.M)
PAGE_MARK = re.compile(r"<!--p([^>]+)-->")
FENCE_OPEN = re.compile(r"^:::\s*\{\.(infobox|displayeq|attribution)\}\s*$")
FENCE_CLOSE = re.compile(r"^:::\s*$")
# 网页转换用的数学保护：只求把 $…$ 整段挡在外面，不需要 build_pdf 那套
# 「防货币符号」的收紧规则（那套会漏掉以数字开头的数学，反而让 ^ 暴露给上标正则）
MATH_ANY = re.compile(r"(\$\$.+?\$\$|\$[^$\n]+?\$)")
FN_REF = re.compile(r"\[\^[A-Za-z0-9]+\]")
SUP_BOLD = re.compile(r"\^\*\*([^*]+?)\*\*\^")
SUP = re.compile(r"\^([^^\n]+?)\^")
SUB = re.compile(r"~([^~\n]+?)~")


def inline_fixes(line: str) -> str:
    r"""行内的 pandoc 特有语法 -> Python-Markdown（图注也要走这一步）。

    必须跳过数学环境：$T_{\mu}^{\mu}$ 里的 ^ 会被上标正则当成 pandoc 上标，
    一路吃到后面的脚注引用 [^ch12n41]，把引用吞掉。
    """
    def fix(seg: str) -> str:
        # 脚注引用先藏起来：一行里有两个 [^a]、[^b] 时，上标正则会把它们
        # 的两个 ^ 当成一对 pandoc 上标，把引用整段改坏
        refs: list[str] = []

        def stash(mm: re.Match) -> str:
            refs.append(mm.group(0))
            return f"\x00{len(refs) - 1}\x00"

        seg = FN_REF.sub(stash, seg)
        seg = PAGE_MARK.sub(
            lambda mm: f'<span class="origpage" title="英文原版第 {mm.group(1)} 页">{mm.group(1)}</span>',
            seg,
        )
        seg = SUP_BOLD.sub(r"<sup>\1</sup>", seg)
        seg = SUP.sub(r"<sup>\1</sup>", seg)
        seg = SUB.sub(r"<sub>\1</sub>", seg)
        return re.sub(r"\x00(\d+)\x00", lambda mm: refs[int(mm.group(1))], seg)

    parts = MATH_ANY.split(line)
    for i in range(0, len(parts), 2):      # 偶数下标是非数学段
        parts[i] = fix(parts[i])
    return "".join(parts)


def convert_page(text: str, chapter: int) -> str:
    """pandoc 方言 -> Python-Markdown。"""
    out: list[str] = []
    fig_no = 0
    for line in text.splitlines():
        m = FENCE_OPEN.match(line)
        if m:
            out.append(f'<div class="{m.group(1)}" markdown="1">')
            out.append("")
            continue
        if FENCE_CLOSE.match(line):
            out.append("")
            out.append("</div>")
            continue
        m = IMG_RE.match(line.strip())
        if m:
            caption, src = m.group(1), m.group(2)
            width = m.group(3) or "80"
            fig_no += 1
            # 页面由 MkDocs 按目录 URL 输出到 /books/vector-zh/<slug>/，需三级回到站点根。
            rel = "../../../" + IMG_DIR.relative_to("docs").as_posix() + "/" + src.split("images/", 1)[1]
            label = f"图 {chapter}.{fig_no}"
            # 图注必须写成 markdown 段落：包在 <figcaption> 里的话，
            # Python-Markdown 会把整块当原始 HTML，里面的 $公式$ 和 *斜体* 不会被解析
            out.append(f'<figure id="fig-{chapter}-{fig_no}" markdown="1">')
            out.append("")
            out.append(f'<img src="{rel}" style="width:{width}%">')
            out.append("")
            out.append(f"@@CAP@@{label}　{inline_fixes(caption)}")
            out.append("{: .figcap }")
            out.append("")
            out.append("</figure>")
            continue
        # 独占一行的原版页码：后面必须空一行。否则接下来的 markdown 会被当成
        # 同一块原始 HTML（Python-Markdown 的块级规则），整个列表就渲染不出来了
        if PAGE_MARK.fullmatch(line.strip()):
            out.append(inline_fixes(line.strip()))
            out.append("")
            continue
        out.append(inline_fixes(line))

    body = "\n".join(out)
    body = SECBREAK.sub('<p class="secbreak">• • •</p>', body)
    body = linkify_urls(body)
    # 正文里「图 N.M」的引用做成锚点（图注里那个用 @@CAP@@ 标记跳过）
    body = FIG_REF.sub(lambda m: f'<a href="#fig-{m.group(1)}-{m.group(2)}">图 {m.group(1)}.{m.group(2)}</a>', body)
    # 图注自己的那个「图 N.M」不要变成指向自己的链接（@@CAP@@ 是它的标记）
    body = re.sub(r'@@CAP@@<a href="#fig-(\d+)-(\d+)">图 \1\.\2</a>', r"图 \1.\2", body)
    body = body.replace("@@CAP@@", "")
    return body


def build_index(target: pathlib.Path) -> str:
    items = "\n".join(
        f"{i}. [{title}]({slug})"
        for i, (_cn, slug, title, _no) in enumerate(PAGES, 1)
    )
    return f"""# 向量：一个关于空间、时间与数学变换的惊奇故事

![封面](../../assets/images/vector/cover.jpg){{: .book-cover }}

> *Vector: A Surprising Story of Space, Time, and Mathematical Transformation*
> Robyn Arianrhod（罗宾·阿里安罗德）著 · UNSW Press / NewSouth Publishing, 2024

从巴比伦泥板上的乘法表，到哈密顿在布鲁姆桥上刻下的四元数公式，再到麦克斯韦的电磁场、
闵可夫斯基的时空，以及爱因斯坦借张量写下的广义相对论——这本书讲向量与张量穿越五千年的故事。

- **中文译稿**：23 篇，汉字 26.3 万字
- **PDF 版**：[下载 vector-cn.pdf（A4，330 页，8.4 MB）](../../assets/pdf/vector-cn.pdf)
- 页边/行内的灰色小字是**英文原版页码**，供按索引与注释回查原书

## 目录

{items}

---

## ⚠️ 版权与非商业声明

原书 *Vector: A Surprising Story of Space, Time, and Mathematical Transformation*，
© 2024 by Robyn Arianrhod，由 UNSW Press / NewSouth Publishing 出版
（美国版由 The University of Chicago Press 首版发行）。原书文字、插图与版式的著作权
归原作者与原出版社所有。

**本中文译本为个人学习与非商业交流用途。** 本译本不主张任何权利，也不得用于任何商业用途。
如权利人提出异议，请与本站联系，我将立即下架相关内容。
"""


def build(target: pathlib.Path) -> None:
    book = target / BOOK_DIR
    img = target / IMG_DIR
    if book.exists():
        shutil.rmtree(book)
    book.mkdir(parents=True)
    img.mkdir(parents=True, exist_ok=True)

    total_fig = 0
    for cn_name, slug, _title, chapter in PAGES:
        src = REPO / "cn-book" / cn_name
        if not src.exists():
            print(f"  ⚠ 缺少 {cn_name}，跳过")
            continue
        text = src.read_text(encoding="utf-8")
        if cn_name == "21.注释.md":
            # 注释在网页上排成编号列表；脚注定义已分发到各章，重复定义会让
            # Python-Markdown 的 footnotes 扩展报错
            text = render_notes(text)
        out = convert_page(text, chapter)
        (book / slug).write_text(out.rstrip() + "\n", encoding="utf-8")
        total_fig += out.count("<figure ")

    (book / "index.md").write_text(build_index(target), encoding="utf-8")

    n_img = 0
    for p in sorted((REPO / "images").glob("*")):
        if p.is_file():
            shutil.copy2(p, img / p.name)
            n_img += 1

    # PDF 一并放进站点：落地页的下载链接才不依赖另一个仓库
    pdf = REPO / "dist" / "vector-cn.pdf"
    pdf_out = target / "docs/assets/pdf"
    if pdf.exists():
        pdf_out.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf, pdf_out / pdf.name)
        print(f"  PDF {pdf.stat().st_size / 1e6:.1f} MB -> {pdf_out / pdf.name}")
    else:
        print("  ⚠ 未找到 dist/vector-cn.pdf，先跑 python3 tools/build_pdf.py")

    print(f"  章节 {len(list(book.glob('*.md')))} 个（含落地页）｜图 {total_fig} 处引用｜复制图片 {n_img} 张")
    print(f"  -> {book}")


def nav_block() -> str:
    lines = ["  - 向量（中译本）:", "      - 开始阅读: books/vector-zh/index.md"]
    for _cn, slug, title, _no in PAGES:
        lines.append(f"      - {title}: books/vector-zh/{slug}")
    return "\n".join(lines)


def check(target: pathlib.Path) -> int:
    book = target / BOOK_DIR
    img = target / IMG_DIR
    problems: list[str] = []

    if not book.exists():
        return 1

    for _cn, slug, _title, _no in PAGES:
        p = book / slug
        if not p.exists():
            problems.append(f"缺少页面 {slug}")
            continue
        t = p.read_text(encoding="utf-8")
        if len(t.strip()) < 50:
            problems.append(f"{slug} 内容过短")
        for bad in ("{width=", "{.infobox}", "{.displayeq}", "{.attribution}", "<!--p", "^**", "@@CAP@@"):
            if bad in t:
                problems.append(f"{slug} 残留未转换的标记：{bad}")
        page_url = f"/books/vector-zh/{pathlib.Path(slug).stem}/"
        expected_asset_root = "/" + IMG_DIR.relative_to("docs").as_posix() + "/"
        for m in re.finditer(r'<img src="([^"]+)"', t):
            rel = m.group(1)
            filename = pathlib.PurePosixPath(rel).name
            resolved_url = posixpath.normpath(posixpath.join(page_url, rel))
            expected_url = expected_asset_root + filename
            if resolved_url != expected_url:
                problems.append(f"{slug} 图片 URL 无法解析到站点资源：{rel} -> {resolved_url}")
            if not (img / filename).exists():
                problems.append(f"{slug} 图片文件不存在：{filename}")

    index_text = (book / "index.md").read_text(encoding="utf-8")
    cover = re.search(r'!\[封面\]\(([^)]+)\)', index_text)
    if not cover:
        problems.append("落地页缺少封面图片")
    else:
        rel = cover.group(1)
        filename = pathlib.PurePosixPath(rel).name
        resolved_url = posixpath.normpath(posixpath.join("/books/vector-zh/", rel))
        expected_url = "/" + IMG_DIR.relative_to("docs").as_posix() + "/cover.jpg"
        if filename != "cover.jpg" or resolved_url != expected_url:
            problems.append(f"落地页封面 URL 错误：{rel} -> {resolved_url}")
        if not (img / "cover.jpg").exists():
            problems.append("落地页封面文件不存在：cover.jpg")

    for p in (REPO / "images").glob("*"):
        if p.is_file() and not (img / p.name).exists():
            problems.append(f"图片未复制：{p.name}")

    if not (target / "docs/assets/pdf/vector-cn.pdf").exists():
        problems.append("PDF 未复制到 docs/assets/pdf/vector-cn.pdf")
    if "assets/pdf/vector-cn.pdf" not in (book / "index.md").read_text(encoding="utf-8"):
        problems.append("落地页的 PDF 链接不是站内相对路径")

    for p in problems:
        print("  !! " + p)
    print(f"检查 {len(PAGES)} 页，问题 {len(problems)} 个")
    return 1 if problems else 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", type=pathlib.Path, default=DEFAULT_TARGET)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--nav", action="store_true")
    args = ap.parse_args()

    if args.nav:
        print(nav_block())
        return
    if args.check:
        sys.exit(check(args.target))
    if not args.target.exists():
        sys.exit(f"目标站点不存在：{args.target}")
    build(args.target)


if __name__ == "__main__":
    main()
