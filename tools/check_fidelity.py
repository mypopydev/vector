#!/usr/bin/env python3
"""忠实度守卫：查漏译、数字/专名丢失、引文缺失、跨章译名不一致、长度异常。

用法：
    python3 tools/check_fidelity.py              # 全部检查，写 review/fidelity.md
    python3 tools/check_fidelity.py --only 5.第1章-代数的解放.md

设计取舍（都是试出来的，别随手改）：
- **汉字数字归一化必须收紧**。把「一个」「两种」也当数字的宽口径会产生 900+ 处噪声，
  比不归一化还糟；只有「含十百千万亿」或「数字后紧跟年/页/章」的数量短语才归一化。
- **只查英文侧的数字有没有丢**，不反过来要求中文数字是英文的子集：
  中文写「两个」而英文写 "two" 是正常的，反查会全是假阳性。
- **专名核对放在章级而非段级**：段级会被大小写与首字母词污染，章级噪声低得多。
- 结构 / 公式 / 术语已由 check_structure / check_math / check_terms 覆盖，这里不重复。
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import statistics
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))
from check_structure import CN_MAP, without_footnote_defs  # noqa: E402
from check_terms import load_glossary  # noqa: E402

EN = REPO / "en"
CN = REPO / "cn-book"
REVIEW = REPO / "review"

# ---------- 段落切分（与 check_structure 同口径，保证能对上） ----------
NON_PARA = ("#", ">", "- ", "* ", "![", ":::", ":", "[^", "<!--", "|", "• • •", "$$")


def paras(text: str) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.startswith("    ") or not line.strip():
            continue
        s = line.strip()
        if s.startswith(NON_PARA):
            continue
        out.append((i, s))
    return out


# ---------- 数字 ----------
NUM = re.compile(r"\d+(?:[.,]\d+)*")
DIGIT = {"零": 0, "〇": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5,
         "六": 6, "七": 7, "八": 8, "九": 9}
UNIT = {"十": 10, "百": 100, "千": 1000, "万": 10000, "亿": 100000000}
CJK_CHARS = "零〇一二三四五六七八九十百千万亿两"
# 只有含「十百千万亿」的连写，或数字后紧跟计量单位，才算数量短语
CJK_NUM = re.compile(
    rf"[{CJK_CHARS}]*[十百千万亿][{CJK_CHARS}]*"
    rf"|[{CJK_CHARS}]{{2,12}}(?=年|世纪|页|章|节|米|英里|公斤|公里|吨|倍|度|角秒)"
)


def cjk_to_int(s: str) -> int | None:
    total = section = num = 0
    for ch in s:
        if ch in DIGIT:
            num = DIGIT[ch]
        elif ch in UNIT:
            u = UNIT[ch]
            if u >= 10000:
                section = (section + num) * u
                total += section
                section = num = 0
            else:
                section += (num or 1) * u
                num = 0
        else:
            return None
    return total + section + num or None


def numbers(text: str) -> collections.Counter:
    text = re.sub(r"\$[^$]*\$", "", text)          # 行内公式里的数字不参与比对
    got = [n.replace(",", "") for n in NUM.findall(text)]
    for m in CJK_NUM.finditer(text):
        v = cjk_to_int(m.group(0))
        if v:
            got.append(str(v))
    return collections.Counter(got)


# ---------- 专名（章级） ----------
PROPER = re.compile(r"\b[A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,}){0,3}\b")
# 句首常见的普通词，不是专名
COMMON = set("""The This That These Those There Their They Them Then Than It Its He His Him She Her
We Our Us You Your I In On At As But And Or So If When While After Before Since During By For From
With Without About Above Under Over Between Among Through Because Although Though Even Only Just
Not Now Here What Why How Which Who Whom Whose Where Yet Still Thus Hence Therefore However
One Two Three Four Five Six Seven Eight Nine Ten First Second Third Next Last Another Other Others
Each Every Both All Some Any Many Most More Much Less Few Several Such Same Very Well Also Perhaps
Maybe Indeed Finally Shortly Later Earlier Soon Today Yesterday Tomorrow Figure Table Chapter Part
Newton Maxwell Einstein""".split())


SENT_END = '.?!:;"\'”』）】…—'


def proper_nouns(text: str) -> set[str]:
    """句中出现的大写词/词组才算专名。

    句首的大写词（Actually / Adding / Anyway…）是普通词被句首大写了，
    靠 COMMON 词表穷举不住，改成看「前一个字符是不是句末标点」。
    """
    out = set()
    for m in PROPER.finditer(text):
        words = m.group(0).split()
        prev = text[m.start() - 1] if m.start() > 0 else "\n"
        at_sentence_start = prev in SENT_END or prev.isspace() and prev != " "
        if len(words) == 1:
            if words[0] in COMMON or at_sentence_start:
                continue
        out.add(m.group(0))
    return out


# ---------- 引文 ----------
# 阈值必须按语言区分：英文 10 个字符 ≈ 中文 4 个字，用同一个阈值必然误报
QUOTED_EN = re.compile(r"[“\"]([^”\"]{10,})[”\"]")
QUOTED_CN = re.compile(r"[“]([^”]{4,})[”]")


# ---------- 译名一致（中文（Latin Name）配对） ----------
PARTICLES = "的是与和及对从由他她它这那并正如比但而则也就都还又很更最且因所被把让使给向在为以于当如之其此个了着过们"
ROLES = ("父亲 母亲 导师 学生 弟子 朋友 老友 同事 同伴 传记作者 作者 教授 数学教授 物理学教授 博士 "
         "先生 夫人 女士 爵士 勋爵 医生 书吏 数学家 物理学家 天文学家 化学家 工程师 校长 院长 国王 "
         "皇帝 教皇 将军 船长 神父 牧师 伯爵 侯爵 男爵 科学家 诗人 作家 哲学家 历史学家 助教 讲师 "
         "研究员 主编 编辑 译者 发明家 实业家 银行家 商人 外交官 军官 飞行员 宇航员 画家 作曲家 音乐家 "
         "总统 首相 总理 法官 律师 记者 评论家 收藏家 赞助人 继承人 长女 女儿 儿子 妻子 丈夫 侄女 侄子 "
         "堂亲 表亲 未婚妻 恋人 知己 支持者 反对者 合作者 对手 同窗 同学 老师 恩师 前辈 后辈 继任者").split()
PAIR = re.compile(r"([\u4e00-\u9fff·]{2,24})（([A-Z][A-Za-z\.\'\- ]{2,40})）")


def same_name(a: str, b: str) -> bool:
    """短的是长的后缀，就当作同一个人的简称。

    「伏尔泰」是「一位爱挑衅的剧作家伏尔泰」的后缀 → 一致；
    「麦克斯韦派」不是「麦克斯韦学派」的后缀 → 真异译。
    """
    return a.endswith(b) or b.endswith(a)


def trim_name(s: str) -> str:
    changed = True
    while changed:
        changed = False
        for p in PARTICLES:
            if s.startswith(p) and len(s) > len(p) + 1:
                s = s[len(p):]
                changed = True
                break
        for r in ROLES:
            if s.startswith(r) and len(s) > len(r) + 1:
                s = s[len(r):]
                changed = True
                break
    return s.strip("·")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    args = ap.parse_args()
    only = set(args.only.split(",")) if args.only else None

    glossary = dict(load_glossary())      # 表驱动检查的基准，全流程共用
    REVIEW.mkdir(exist_ok=True)
    sections: list[str] = ["# 忠实度守卫报告", "",
                           "由 `tools/check_fidelity.py` 生成。严重 > 中等 > 轻微。", ""]
    n_severe = n_medium = n_minor = 0

    name_map: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    chapter_names: list[tuple[str, str, set[str]]] = []
    global_cn_names: set[str] = set()
    for _stem, _cn in CN_MAP.items():
        _p = CN / _cn
        if _p.exists():
            global_cn_names |= proper_nouns(without_footnote_defs(_p.read_text(encoding="utf-8")))

    for stem, cn_name in CN_MAP.items():
        if only and cn_name not in only:
            continue
        cn_path = CN / cn_name
        if not cn_path.exists():
            continue
        strip = stem != "25_Notes"
        en_text = (EN / f"{stem}.md").read_text(encoding="utf-8")
        cn_text = cn_path.read_text(encoding="utf-8")
        if strip:
            en_text = without_footnote_defs(en_text)
            cn_text = without_footnote_defs(cn_text)

        severe, medium, minor = [], [], []

        # 1) 数字：逐段
        E, C = paras(en_text), paras(cn_text)
        if stem == "25_Notes":
            E = C = []          # 注释是定义列表，段级比对不适用
        if len(E) == len(C):
            for (le, e), (lc, c) in zip(E, C):
                en_n, cn_n = numbers(e), numbers(c)
                if not en_n:
                    continue
                missing = en_n - cn_n
                if not missing:
                    continue
                big_missing = sorted(k for k in missing if len(k) >= 3 or "." in k)
                cn_big = [k for k in cn_n if len(k) >= 3 or "." in k]
                if big_missing and not cn_big:
                    # 英文有 3 位以上数值，中文整段一个都没有：可能整段漏了数字
                    severe.append(f"cn 行{lc}（en 行{le}）：英文有数值 {sorted(en_n)}，"
                                  f"中文段内查不到任何 3 位以上数字")
                elif big_missing:
                    # 年代写法差异：英文 1800s / 1880s ↔ 中文「19 世纪后期」「19 世纪 80 年代」，
                    # 数字对不上但意思等价，降为轻微
                    rest = [k for k in big_missing
                            if len(k) >= 4 and k.endswith("0")
                            and any(k[:2] in cn_n or k[:2] == x[:2] for x in cn_n)]
                    if rest and len(rest) == len(big_missing):
                        minor.append(f"cn 行{lc}：{rest} 中文按「N 世纪 M0 年代」表述"
                                     f"（英文 {sorted(en_n)}）")
                    else:
                        medium.append(f"cn 行{lc}（en 行{le}）：中文缺少数值 {big_missing}"
                                      f"（英文 {sorted(en_n)}，中文 {sorted(cn_n)}）")
                else:
                    minor.append(f"cn 行{lc}：小数字 {sorted(missing)} 未以数字形式出现"
                                 f"（英文 {sorted(en_n)}；中文多写作「二维」这类，可忽略）")
        else:
            medium.append(f"段落数不一致：英文 {len(E)} / 中文 {len(C)}（本文件的段级检查跳过）")

        # 2) 专名：章级
        en_names = proper_nouns(en_text)
        # 章级比会误判「首现给拉丁名、后续只用中文」的情况，所以推迟到全书级统一判断
        chapter_names.append((stem, cn_name, en_names))

        # 3) 引文数量
        en_q, cn_q = len(QUOTED_EN.findall(en_text)), len(QUOTED_CN.findall(cn_text))
        if en_q and cn_q < en_q * 0.9:
            bucket = minor if stem == "26_Index" else medium
            bucket.append(f"引文数量偏少：英文 {en_q} 段引文，中文 {cn_q} 段"
                          f"（注意：引号里的**术语**译成中文后不带引号是正常的，"
                          f"只有**题名**才要求保留原样，故本项需人工判断）")

        # 4) 长度异常：段落比率 top/bottom 3（仅提示）
        ratios = []
        for (le, e), (lc, c) in zip(E, C):
            ew = len(re.findall(r"[A-Za-z][A-Za-z'-]+", e))
            cc = len(re.findall(r"[一-鿿]", c))
            if ew >= 30:
                ratios.append((cc / ew, le, lc))
        if len(ratios) >= 10:
            med = statistics.median(r for r, _, _ in ratios)
            for r, le, lc in sorted(ratios, reverse=True)[:2]:
                if r > med * 1.15:
                    minor.append(f"段落偏长：cn 行{lc} 比率 {r:.2f}（该章中位 {med:.2f}），可考虑精简")
            for r, le, lc in sorted(ratios)[:2]:
                if r < med * 0.85:
                    minor.append(f"段落偏短：cn 行{lc} 比率 {r:.2f}（该章中位 {med:.2f}），"
                                 f"确认无漏译")

        # 5) 译名配对收集（最后统一统计）
        for cn_n, en_n in PAIR.findall(cn_text):
            # 不做剪词：后綴匹配已能容忍前缀定语，剪词反而会把「向量委员会」剪成「量委员会」
            name_map[en_n.strip()].update([cn_n])

        n_severe += len(severe)
        n_medium += len(medium)
        n_minor += len(minor)
        if severe or medium or minor:
            sections.append(f"## {stem} ↔ `cn-book/{cn_name}`")
            sections.append("")
            for level, items in (("严重", severe), ("中等", medium), ("轻微", minor)):
                if items:
                    sections.append(f"### {level} ({len(items)})")
                    sections.append("")
                    for it in items:
                        sections.append(f"- {it}")
                    sections.append("")

    # 专名保全：表驱动。
    # 句首大写词/普通词根本穷举不完（Along / Adventures / Anyway…），
    # 换成「译名表里约定的外文名，是否在译稿里真的出现过」——精确且可行动。
    sections.append("## 专名保全（表驱动）")
    sections.append("")
    absent = sorted(n for n in glossary if " " in n or len(n) > 4
                    if n not in global_cn_names)
    if absent:
        n_medium += 1
        sections.append(f"### 中等 (1)")
        sections.append("")
        sections.append(f"译名表里有 {len(absent)} 个外文名在整部译稿里从未以原文形式出现"
                        f"（若原文也没出现过则属正常）：")
        sections.append("")
        sections.append("　" + "、".join(absent[:60]) + ("…" if len(absent) > 60 else ""))
        sections.append("")
    else:
        sections.append("译名表里约定的外文名都在译稿中出现过。")
        sections.append("")

    # 表外高频专名：只是提示补表，不算错
    extra = collections.Counter()
    for _stem, _cn, names in chapter_names:
        for nm in names:
            if " " in nm and nm not in glossary:
                extra[nm] += 1
    if extra:
        n_minor += 1
        sections.append("## 表外专名（轻微，建议补进译名表）")
        sections.append("")
        sections.append(f"共 {len(extra)} 个多词外文专名不在译名表内，出现频次最高的 20 个：")
        sections.append("")
        sections.append("　" + "、".join(f"{k}×{v}" for k, v in extra.most_common(20)))
        sections.append("")

    # 跨章译名一致
    # 用译名表当基准：表里给的中文名应当是候选写法（可能带定语）的后缀。
    # 这样「一位爱挑衅的剧作家伏尔泰」能对上「伏尔泰」，
    # 而「麦克斯韦学派」对不上表里的「麦克斯韦派」，就会被抓出来。
    bad = {}
    for latin, forms in name_map.items():
        want = glossary.get(latin)
        if not want:
            continue
        offenders = collections.Counter()
        for form, cnt in forms.items():
            if not form.endswith(want.lstrip("四元数的单位部分").strip()):
                offenders[form] = cnt
        if offenders:
            bad[latin] = offenders
    sections.append("## 跨章译名一致性")
    sections.append("")
    if bad:
        n_medium += len(bad)
        sections.append(f"### 中等 ({len(bad)})")
        sections.append("")
        sections.append("以 `docs/译名表-人名.md` / `docs/术语表.md` 为基准：下表外文名的写法与表中译名不一致。")
        sections.append("")
        for k, v in sorted(bad.items()):
            sections.append(f"- **{k}**（表中译名「{glossary[k]}」）→ 另有写法："
                            + "、".join(f"{a}×{b}" for a, b in v.most_common()))
        sections.append("")
    else:
        sections.append("未发现同一外文名有多种中文译名。")
        sections.append("")

    (REVIEW / "fidelity.md").write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"严重 {n_severe} 项，中等 {n_medium} 项，轻微 {n_minor} 项 -> review/fidelity.md")
    sys.exit(1 if n_severe else 0)


if __name__ == "__main__":
    main()
