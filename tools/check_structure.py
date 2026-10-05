#!/usr/bin/env python3
"""中英结构对齐检查：译文有没有漏段、漏图、漏公式、漏尾注。

用法：
    python3 tools/check_structure.py                # 全部已译章节
    python3 tools/check_structure.py --only 4.序言   # 只查指定章节（可逗号分隔）

严重度：严重（必须修）> 中等 > 轻微（仅供参考）。
段数/图数/公式数/尾注数属于「严重」——差一个都说明译文漏了内容。
字符数与列表项数是软信号——中文常拆条、字数浮动属正常，只提示人工复核。
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
EN = REPO / "en"
CN = REPO / "cn-book"
REVIEW = REPO / "review"

# 英文抽取文件 -> 中文译稿
CN_MAP = {
    "08_Prolog": "4.序言.md",
    "09_Chapter01": "5.第1章-代数的解放.md",
    "10_Chapter02": "6.第2章-微积分的登场.md",
    "11_Chapter03": "7.第3章-向量的构想.md",
    "12_Chapter04": "8.第4章-理解空间与存储.md",
    "13_Chapter05": "9.第5章-出人意料的新角色与缓慢的接受.md",
    "14_Chapter06": "10.第6章-泰特与麦克斯韦.md",
    "15_Chapter07": "11.第7章-从四元数到向量.md",
    "16_Chapter08": "12.第8章-向量分析终成正果.md",
    "17_Chapter09": "13.第9章-从空间到时空.md",
    "18_Chapter10": "14.第10章-弯曲的空间与不变的距离.md",
    "19_Chapter11": "15.第11章-张量的发明.md",
    "20_Chapter12": "16.第12章-万物汇聚.md",
    "21_Chapter13": "17.第13章-后来发生了什么.md",
    "22_Epilog": "18.结语.md",
    "23_Timeline": "19.时间线.md",
    "24_Acknowledgments": "20.致谢.md",
    "25_Notes": "21.注释.md",
    "26_Index": "22.索引.md",
}

# 不属于「普通段落」的行前缀
NON_PARA = (
    "#", ">", "- ", "* ", "![", ":::", ":", "[^", "<!--", "    ", "|", "• • •",
)
DIGIT_LIST = re.compile(r"^\d+\.\s")


def para_lines(text: str) -> list[str]:
    out = []
    for line in text.splitlines():
        if line.startswith("    "):      # 脚注/列表的续行，不是新段落
            continue
        if line.lstrip().startswith("$$"):   # 行间公式行
            continue
        s = line.strip()
        if not s:
            continue
        if s.startswith(NON_PARA) or DIGIT_LIST.match(s):
            continue
        out.append(s)
    return out


def count(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, re.M))


def without_footnote_defs(text: str) -> str:
    """去掉由 split_notes.py 追加到章文件末尾的脚注定义（含缩进续行）。"""
    out: list[str] = []
    in_def = False
    for line in text.splitlines():
        if re.match(r"^\[\^", line):
            in_def = True
            continue
        if in_def:
            if line.startswith("    ") or not line.strip():
                continue
            in_def = False
        out.append(line)
    return "\n".join(out)


def metrics(text: str, include_indented_display: bool = False) -> dict:
    math_text = re.sub(r"(?m)^[ \t]{4,}(?=\$\$)", "", text) if include_indented_display else text
    inline_math = len(re.findall(r"(?<!\$)\$(?!\$)[^$\n]+?\$(?!\$)", math_text, re.M))
    return {
        "段": len(para_lines(text)),
        "图": count(text, r"^!\["),
        "行间公式": count(math_text, r"^\$\$"),  # 仅统计用
        "行内公式": inline_math,
        "公式": len(re.findall(r"^\$\$(.+?)\$\$", math_text, re.M)) + inline_math,
        "尾注引用": len(re.findall(r"\[\^(ch\d\dn\d+)\](?!:)", text)),
        "尾注定义": len(re.findall(r"\[\^(ch\d\dn\d+)\]:", text)),
        "节标题": count(text, r"^## "),
        "分页标记": count(text, r"<!--p[^>]+-->"),
        "列表项": count(text, r"^- "),
        # 只数汉字：LaTeX 公式、英文原词、Markdown 标记会把总字符数抬高 40% 以上，
        # 用它算出来的比值（实测 2.2–2.5）会误报「漏译/扩写」
        "汉字数": len(re.findall(r"[一-鿿]", text)),
    }


def load_manifest() -> dict:
    path = EN / "manifest.json"
    if not path.exists():
        raise SystemExit("缺少 en/manifest.json，先跑 python3 tools/extract_epub.py")
    return {m["stem"]: m for m in json.loads(path.read_text(encoding="utf-8"))}


def compare(stem: str, cn_name: str, manifest: dict) -> dict:
    en_path = EN / f"{stem}.md"
    cn_path = CN / cn_name
    if not en_path.exists():
        return {"error": f"缺少英文源 {en_path}"}
    if not cn_path.exists():
        return {"error": "尚未翻译"}

    en_text = en_path.read_text(encoding="utf-8")
    cn_text = cn_path.read_text(encoding="utf-8")
    strip = stem != "25_Notes"          # 注释文件的正文就是脚注定义本身
    include_indented_display = stem == "25_Notes"
    en_m, cn_m = (metrics(without_footnote_defs(en_text) if strip else en_text,
                           include_indented_display=include_indented_display),
                  metrics(without_footnote_defs(cn_text) if strip else cn_text,
                           include_indented_display=include_indented_display))

    severe, medium, minor = [], [], []
    keys = ("段", "图", "公式", "尾注引用", "节标题", "分页标记")
    if stem == "25_Notes":
        keys = ("图", "公式", "节标题", "分页标记")   # 注释是定义列表，段数不可比
    for key in keys:
        if en_m[key] != cn_m[key]:
            severe.append(f"**{key}数**：英文 {en_m[key]} vs 中文 {cn_m[key]}")
    # 尾注定义只在「注释」这一对上比：各章的脚注定义已由 split_notes.py 从
    # 21.注释.md 分发过去，而 21.注释.md 本身改成了编号列表（否则会和章文件重复定义）
    if stem == "25_Notes":
        cn_entries = len(re.findall(r"\[\^ch\d\dn\d+\]:", cn_text))
        if en_m["尾注定义"] != cn_entries:
            severe.append(f"**注释条目数**：英文 {en_m['尾注定义']} vs 中文 {cn_entries}")

    # 汉字数 / 英文词数：英译中通常落在 1.4–1.9 之间。
    # 注释不比：它的正文以英文文献信息（作者、书名、期刊、年份）为主，汉字占比天然偏低
    en_words = manifest.get(stem, {}).get("words", 0)
    if stem == "25_Notes":
        en_words = 0
    ratio = cn_m["汉字数"] / max(en_words, 1)
    if not (1.2 <= ratio <= 2.2):
        medium.append(
            f"**字数比**：汉字 {cn_m['汉字数']} / 英文 {en_words} 词 = {ratio:.2f}"
            f"（期望 1.2–2.2，可能漏译或过度发挥）"
        )

    if en_m["列表项"] != cn_m["列表项"]:
        minor.append(f"**列表项数量**：英文 {en_m['列表项']} vs 中文 {cn_m['列表项']}（中文常拆条，仅供参考）")

    # 译文里不该出现成段未翻译的英文：只有「英文词很多且汉字占比很低」才算可疑，
    # 否则密集公式段（含 \sqrt 之类）和夹带英文原名的段落会被误报
    long_en = []
    for line in para_lines(cn_text):
        if len(line) < 40:
            continue
        cjk = len(re.findall(r"[一-鿿]", line))
        probe = re.sub(r"（[^）]*）", "", line)
        probe = re.sub(r"\*[^*]+\*", "", probe)
        stop = sum(len(re.findall(rf"\b{w}\b", probe, re.I))
                   for w in ("the", "and", "of", "that", "which", "with", "from", "was", "were"))
        # 要同时满足「英文虚词多」和「汉字占比低」才算可疑；
        # 只含公式或夹带英文人名的中文段落（cjk 占比高）不该报警
        if stop >= 3 and cjk / len(line) < 0.5:
            long_en.append(line)
    if long_en:
        medium.append(f"**疑似未翻译段落** {len(long_en)} 段，例如：{long_en[0][:60]}…")

    return {"en": en_m, "cn": cn_m, "severe": severe, "medium": medium, "minor": minor}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None, help="只查指定中文文件名（逗号分隔）")
    args = ap.parse_args()

    manifest = load_manifest()
    only = set(args.only.split(",")) if args.only else None
    REVIEW.mkdir(exist_ok=True)

    rows = []
    for stem, cn_name in CN_MAP.items():
        if only and cn_name not in only:
            continue
        rows.append((stem, cn_name, compare(stem, cn_name, manifest)))

    lines = [
        "# 结构比对报告",
        "",
        "由 `tools/check_structure.py` 自动生成。严重度：严重 > 中等 > 轻微。",
        "（字符数/列表项为软信号，需人工复核。）",
        "",
    ]
    n_severe = n_medium = 0
    for stem, cn_name, r in rows:
        lines.append(f"## {stem} ↔ `cn-book/{cn_name}`")
        lines.append("")
        if "error" in r:
            lines.append(f"- {r['error']}")
            lines.append("")
            continue
        n_severe += len(r["severe"])
        n_medium += len(r["medium"])
        if not (r["severe"] or r["medium"] or r["minor"]):
            lines.append("无结构性问题。")
            lines.append("")
            continue
        for level, items in (("严重", r["severe"]), ("中等", r["medium"]), ("轻微", r["minor"])):
            if items:
                lines.append(f"### {level} ({len(items)})")
                lines.append("")
                for it in items:
                    lines.append(f"- {it}")
                lines.append("")

    (REVIEW / "structure.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for stem, cn_name, r in rows:
        if "error" in r:
            print(f"{stem:22s} -> {cn_name:32s} {r['error']}")
            continue
        flag = "OK " if not r["severe"] else "!! "
        print(f"{flag}{stem:22s} -> {cn_name:32s} "
              f"段 {r['cn']['段']}/{r['en']['段']}  图 {r['cn']['图']}/{r['en']['图']}  "
              f"公式 {r['cn']['行间公式']+r['cn']['行内公式']}/{r['en']['行间公式']+r['en']['行内公式']}  "
              f"尾注 {r['cn']['尾注引用']}/{r['en']['尾注引用']}")

    print(f"\n严重 {n_severe} 项，中等 {n_medium} 项 -> review/structure.md")
    sys.exit(1 if n_severe else 0)


if __name__ == "__main__":
    main()
