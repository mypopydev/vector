# 《向量》中文译本 · 第五轮细致复核 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在四轮复核（tag `v1.0.6`）之上，修正一个**已经上线、影响 7 章全部图注与图号引用**的严重缺陷——图号体系错位；并补齐五个从未检查过的维度（引文块、括注纪律、交叉引用语义、标点体例、图内文字），最终产出 `v1.0.7`。

**Architecture:** 沿用已验证有效的做法——**开工前先跑实测探针定位真盲区 + 并行子代理逐条核对 + 主代理独立回原文核实 + 机械守卫兜底**。本轮新增守卫 `check_figures.py`（图号体系三方对齐：原文编号 / 译稿图注 / 正文引用）。

**Tech Stack:** Markdown 译稿（唯一真源）、Python 校验脚本（`tools/check_*.py`）、pandoc + XeLaTeX（PDF）、Lua filter（`tools/infobox.lua`）、MkDocs Material（站点）、子代理并行复核。

**Spec:** `docs/superpowers/plans/2026-09-27-vector-cn-review-round4.md`（第四轮，六任务已全绿）、`review/quality-report.md` / `-round2/3/4.md`（历轮结论）、`docs/翻译风格指南.md` + `docs/术语表.md`（443 条）+ `docs/译名表-人名.md`（硬约束）。

## Global Constraints

以下要求对**每一个任务**都生效：

- **禁用译名**：`vector` 全书只译「向量」，禁止「矢量」；`scalar product` 统一「**标量积**」。
- **人名/专名体例**：首现「中文名（English Full Name）」，其后只写中文；文献条目里的作者名/题名/期刊名保留英文；注释与正文的说明性行文一律转写。
- **已归一不可回退**：Christoffel 用全名；Otto Stern＝「斯特恩」；Grace Chisholm (Young)＝「格蕾丝·奇泽姆·扬」；维度写「二维/三维/四维」；`telegraphy`＝「电报」。
- **不得改动**：公式内容、图片文件名、`<!--pNNN-->` 分页标记、脚注编号。
- **不得删减**原文限定语（maybe / seemingly / arguably / apparently）；不得为顺口改事实、数字、专名；**不得整段重写**；建议具体到「删哪几个字／换哪个词」。
- **注释真源**：`cn-book/21.注释.md` 是注释定义的唯一真源，改注释必须改真源后重跑 `python3 tools/split_notes.py` 并 `--check`。
- **交付门槛**：九道校验（`check_structure` / `check_math` / `check_terms` / `check_fidelity` / `check_refs` / `check_emphasis` / `check_residue` / `check_baseline` / `split_notes --check`）严重项必须为 0。
- **发布约定**：改动完成后**不自动** commit / push / 推站点仓；先给用户看清单。

---

### Task 1: 图号体系核对与修正（本轮最重，含已上线的严重缺陷）

**Files:**
- Create: `tools/check_figures.py`
- Modify: `tools/build_pdf.py`、`tools/infobox.lua`（或新增 lua filter）、`cn-book/*.md`（图注与正文引用）
- Create: `review/findings/round5-图号体系.md`

**为什么这是真盲区（探针实测，非推测）**：四轮复核里，图注的**文字**（round 2）与「图 N.M」的**越界/文件存在性**（round 4 `check_refs.py`）都查过，但**从来没人把「原书图号 → 译稿图注 → 正文引用 → PDF 实际渲染号」这四者对齐过**。探针一测就发现两处系统性偏差：

**（A）9 张无编号图版被 LaTeX 自动编了号**——原书这些是**不带 FIGURE 编号**的照片/图版（`en/` 里没有 `FIGURE N.M` 前缀），但 pandoc 把每张图都排成带 `\caption` 的 figure，LaTeX 一视同仁地编号，于是**其后所有图号整体后移**：

| 章 | 无编号图版（`pNNN.jpg`） | 位置 | 后果 |
|---|---|---|---|
| 第 4 章 | `p098.jpg` | 章首 | fig4_1→图 **4.2**…fig4_4→图 **4.5**；正文引用的 图 4.1–4.4 全部指错 |
| 第 6 章 | `p152.jpg` | 章中 | 图 6.1 起整体后移；正文「图 6.3a」变成 图 6.4 |
| 第 7 章 | `p186.jpg` | 章末 | 无号图版被编成 图 7.3（原书无此号） |
| 第 9 章 | `p223` `p226` `p237` | 穿插 | fig9_3→图 **9.5**、fig9_4→图 **9.7** |
| 第 10 章 | `p246.jpg` | 章首 | fig10_1→图 **10.2**…fig10_4→图 **10.5** |
| 第 12 章 | `p310.jpg` | 章末 | 无号图版被编成 图 12.2 |
| 第 13 章 | `p337.jpg` | 章首 | fig13_1→图 **13.2**；正文「图 13.1」指错 |

**（B）5 组多子图被当成独立图，且丢了 A/B/C 后缀**——原书用 `FIGURE 2.3A` / `2.3B` 这种「同号分幅」编号，译稿图注**把 A/B/C 后缀整个丢掉了**，且 LaTeX 按独立图递增：

| 章 | 原书编号 | 译稿图片 | 现在渲染成 | 应为 |
|---|---|---|---|---|
| 第 2 章 | 2.3A, 2.3B | `fig2_3a/b.jpg` | 图 2.3, 图 2.4 | 图 2.3A, 图 2.3B |
| 第 3 章 | 3.8A, 3.8B | `fig3_8a/b.jpg` | 图 3.8, 图 3.9 | 图 3.8A, 图 3.8B |
| 第 6 章 | 6.3A, 6.3B, 6.3C | `fig6_3a/b/c.jpg` | 图 6.3–6.5 | 图 6.3A, 6.3B, 6.3C |

**（C）正文引用本身也不统一**——同一组子图，第 2 章同时出现「图 2.3A」「图 2.3B」（大写，行 53/71）与「图 2.3a」「图 2.3b」（小写，行 41/121/124）；跨章引用（第 10 章行 46 引「图 2.3a」「图 2.3b」、第 11 章行 74 引「图 6.3a」、第 14 章行 74 引「图 2.3b」、注释行 220 引「图 2.2a」）都引用了**我方图注里压根不存在**的编号。

> 注：`cn-book/7.第3章...md:257` 与 `21.注释.md:87` 里的「图 13.3」是**引用他人著作**（Stillwell, *Mathematics and Its History*）的图，**不是本书编号**，不算缺陷；同类假阳性要甄别掉。

- [ ] **Step 1: 写 `tools/check_figures.py`（三方对齐守卫）**

从 `en/<章>.md` 抽取 `![FIGURE N.M` 的**编号序列**（含 A/B/C 后缀与「无编号」标记），与 `cn-book/<章>.md` 的**图片文件序列**按位置配对，输出三方对照表：

```
章 | # | 原书编号 | 译稿图片 | 译稿图注是否含编号 | 正文引用该号的次数 | 判定
```

判定口径：
- 原书**无编号** → 译稿**不得**渲染出编号（否则报「多编号」）；
- 原书 `N.MA` 类 → 译稿必须有对应 A/B/C 标识（否则报「子图后缀丢失」）；
- 原书为 `N.M` 而**正文引用**了 `N.Ma` 之类不存在的号 → 报「引用无对应图注」。

正文引用的**编号范围**检查（含跨章引用）一并纳入，取代 `check_refs.py` 里只判 `images/figN_M.jpg` 存在的那部分或与之互补。

```bash
python3 tools/check_figures.py          # 预期：报出上述 A/B/C 三类全部问题
```

- [ ] **Step 2: 定方案（需用户拍板，见文末「两处需要你定的判断」）**

- **方案 A（推荐）**：**改为显式编号**——图注里写死「图 2.3A」这类原书编号，用 `\caption*`（或非 figure 的居中块）**关掉 LaTeX 自动编号**。好处：彻底摆脱自动编号这个反复出问题的源头（round 2 的「图 0.1: 图 0.1」重复编号、本轮的错位，根因都是它），且编号可被 `check_figures.py` 逐条核对；无编号图版天然不编号。
- **方案 B**：保留自动编号，无编号图版改居中不编号块、子图用 `subcaption` 渲成「图 2.3a/b/c」。改动小，但**无法复现原书的 "2.3A/2.3B" 写法**（会变成小写 a/b），且仍依赖自动编号。

- [ ] **Step 3: 实现（按选定方案）**

涉及两个层面：
1. **构建层**：`tools/build_pdf.py` 合并后做图注预处理 / 新增 lua filter，让「无编号图版」不进 figure 编号，让子图共享一个号。
2. **译稿层**：给 5 组子图补回 A/B/C 标识；把正文里不统一的引用（大写/小写、引用不存在的号）统一到原书口径。

- [ ] **Step 4: 用 PDF 文本层复核（关键验收）**

```bash
python3 tools/build_pdf.py
pdftotext dist/vector-cn.pdf /tmp/v.txt
python3 tools/check_figures.py --pdf /tmp/v.txt    # 预期：PDF 渲染号与原文编号逐条一致，0 偏差
```

**这一条是硬验收**：本轮缺陷之所以能瞒过四轮，就是因为没人看过「PDF 里实际渲染出的编号」。修完必须从 PDF 文本层验一遍。

- [ ] **Step 5: 校验 + Commit**

```bash
for s in check_structure check_math check_terms check_refs check_figures; do python3 tools/$s.py 2>&1 | tail -1; done
git add -A && git commit -m "fix(figures): 图号体系对齐原书（无编号图版/子图后缀/正文引用）；新增 check_figures.py"
```

---

### Task 2: 引文块（blockquote）17 行逐条核对

**Files:**
- Read: `cn-book/{5,6,9,10,11,12,16}.*.md` 里的 `>` 引文块、对应 `en/*.md`
- Create: `review/findings/round5-引文块.md`

**为什么这是真盲区**：round 1 的方法明文写着「`>` 引文块…**不计入段号**」，此后四轮都沿用了这个口径——**引文块的内容从未被系统比对过**。全书共 17 行（中英各 17 行，数量一致）：第 6 章是 8 行**韵文**（诗歌，含押韵与断行），其余为数学家书信/著作摘引。

- [ ] **Step 1: 派 1 个子代理逐条核对**

要求：逐行把中英引文并排比对，回答 ① 是否逐字忠实（有无漏句/改意）② 韵文是否处理得当（断行、脚注位置）③ 引文内的括号补充（如 `［剑桥的以马内利学院］`）是否与原书一致 ④ 引文内出现「四元数（quaternion）」这类**括注是否得体**（引文里加译注要慎重）。只报可定位、可验证的问题；返回 ≤150 字摘要。

- [ ] **Step 2: 主代理回原文核实 + 应用「严重 + 中等」**

- [ ] **Step 3: 校验 + Commit**

```bash
python3 tools/check_structure.py 2>&1 | tail -1
git add -A && git commit -m "fix(quotes): 引文块逐条核对修订"
```

---

### Task 3: 括注纪律（首现/同章不重复）

**Files:**
- Read: `docs/翻译风格指南.md` §二（§14–15 条）、`docs/术语表.md`、`docs/译名表-人名.md`、全部 `cn-book/*.md`
- Create: `review/findings/round5-括注纪律.md`

**为什么这是真盲区**：风格指南规定「术语首次出现写『中文（English）』，**同章第二次起只用中文**」「人名首现写『中文名（English Full Name）』，其后只用姓」。四轮里没人系统查过这条**纪律**本身。探针实测：

- **同章内重复括注 6 处**（明确违反「同章第二次起只用中文」）：
  | 文件 | 重复项 | 行 |
  |---|---|---|
  | 第 6 章 | `vector field` | 56, 184 |
  | 第 7 章 | `divergence`（3 次）、`convergence`（2 次） | 38/63/141、63/141 |
  | 第 11 章 | `tensor product` | 41, 46 |
  | 第 12 章 | `Arnold Sommerfeld` | 125, 164 |
  | 第 4 章 | `invariant` | 156, 225 |
- **「正文出现但全书从未括注」的术语 151 条**（探针口径：术语表译名在正文出现，但该词从未带英文括注）。其中大部分是**日常词，本就不该括**（方向、负数、平方根、极限、加速度、未知数、根、幂），但有一批是**技术术语，按体例该括**，例如：`four-velocity`（四维速度）、`proper time`（固有时）、`parallel postulate`（平行公设）、`line integral`（线积分）、`surface integral`（面积分）、`de Moivre's theorem`（棣莫弗定理）、`associative law`（结合律）。

- [ ] **Step 1: 修掉 6 处同章重复括注**

逐处判断：若该词在本章**首现处已有括注**，删掉后面多余的；若首现处没括而后面有，把括注挪到首现处。

- [ ] **Step 2: 派 1 个子代理甄别 151 条**

分工要求：对每条回 `en/` 看该词在原文里的**技术含量**与**上下文**，三选一——`该括（技术术语）` / `不必括（日常词，术语表收它只是为了统一译名）` / `待定`。只报「该括」的，并给出「插在哪个文件哪一行哪个词之后」。

- [ ] **Step 3: 应用 + 校验 + Commit**

```bash
python3 tools/check_terms.py 2>&1 | tail -1
git add -A && git commit -m "fix(gloss): 括注纪律——清同章重复括注、补该括的技术术语"
```

---

### Task 4: 交叉引用的语义指向（不只越界）

**Files:**
- Read: `cn-book/*.md` 里的 `第 N 章`（164 处）、`图 N.M`（187 处，Task 1 已覆盖编号侧）、`尾注 N`（43 处）、`参见/见第`（33 处）
- Create: `review/findings/round5-交叉引用.md`

**为什么这是真盲区**：`check_refs.py` 只查**越界**（第 N 章 N≤13、图文件存在、尾注号不超本章条数）。**指向对不对**（「见第 6 章」是否真在第 6 章讲过、「见尾注 10」那一条尾注是否就是说的这件事）从未核过。round 4 已有先例：`check_refs` 初版报的 24 条越界**全是脚本假阳性**，其中包括**引用他人著作的「第 14 章」**（Apeiron 版《Ampère's Electrodynamics》）。

- [ ] **Step 1: 派 2 个子代理分段核对**

要求：对每条「见第 N 章」「参见第 N 章」「见尾注 N」，回 `en/` 找到对应英文原文，确认 ① 英文里引的就是同一个章/注 ② 中文改动的译法没把指向改掉。**特别注意甄别「引用他人著作」的情况**（如「图 13.3」指 Stillwell 书中的图），这类**不是**本书引用，不要当缺陷报。

- [ ] **Step 2: 主代理核实（重点复核「引用他书」类假阳性）+ 应用**

- [ ] **Step 3: 校验 + Commit**

```bash
python3 tools/check_refs.py 2>&1 | tail -1
git add -A && git commit -m "fix(refs): 交叉引用语义指向核对"
```

---

### Task 5: 标点体例（ASCII 直引号夹中文）

**Files:**
- Modify: `cn-book/22.索引.md`（8 处）、必要时其他文件
- Create: `review/findings/round5-标点体例.md`

**探针结论**：中文行文里的半角逗号/句号/括号**已是 0 处**（前几轮清得干净），页码标记 `<!--pNNN-->` 也**单调递增无重复**。唯一残留是**用 ASCII 直引号夹中文**：

| 位置 | 现状 | 应为 |
|---|---|---|
| 索引行 3 | `- "科学家"一词的创造（scientist），101` | `“科学家”` |
| 索引行 21 | `他的"最大错误"` | `他的“最大错误”` |
| 索引行 28 | `他提出的"四维向量"一词` | `“四维向量”` |
| 索引行 341 | `作为"科学女王"` | `“科学女王”` |

（索引里 `"Invariante Variationsprobleme"` 这类**夹英文题名**的直引号是本书体例，**保留**。）

- [ ] **Step 1: 修掉 8 处 + 复扫全书**

```bash
python3 - <<'PY'   # 复扫：ASCII 双引号里含汉字的
import re, glob, os
pat = re.compile(r'"([^"\n]*[\u4e00-\u9fff][^"\n]*)"')
...
PY
```

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "fix(punct): 索引 8 处 ASCII 直引号改中文弯引号"
```

---

### Task 6: 插图内的英文文字盘点（执行中发现的新盲区）

**Files:**
- Read: `images/*.jpg`（57 张；其中 `figN_M.jpg` 为图表，`pNNN.jpg` 为照片/图版）
- Create: `review/findings/round5-图内文字.md`
- Modify: 视裁定结果改图注 / 译本说明

**为什么这是真盲区**：执行 Task 1 时我实际**打开**了 `fig7_1.jpg`，发现它是**原书英文标注**的多面板图——图内的 `a) Positive divergence` / `b) Negative divergence (=convergence)` / `c) Examples of zero divergence` 全是英文，而全书图注都已中文化。四轮复核里没人看过图片**内容**（round 2 只核对了图注**文字**，round 4 只核对了文件存在性）。

- [ ] **Step 1: 派 3 个子代理分工看图**（每代理约 15–20 张，只报图表类，照片类可略）

要求：逐张查看图片，记录 ① 图内是否有**英文文字** ② 若有，列出文字内容 ③ 该文字是否已被**图注**覆盖（图注里是否已译出）。返回：有英文标注的图清单 + 每张的标注文字。

- [ ] **Step 2: 定处置口径**（需用户拍板）

- **方案一**：**保留原图 + 图注补译**——在图注里把图内关键标注译出（如「图中三幅分别为：a) 正散度、b) 负散度（＝收敛）、c) 零散度」），不动图片。
- **方案二**：**保留原图，仅在译本说明里声明**「插图沿用原书，图内文字为英文」。
- **方案三**：重绘图片（工作量大，且原图有版权与版式考量，**不推荐**）。

- [ ] **Step 3: 按口径落地 + Commit**

---

### Task 7: 汇总、重建、出报告

**Files:**
- Create: `review/findings/汇总-第五轮.md`、`review/quality-report-round5.md`
- Modify: `README.md`（规模数字）
- Rebuild: `dist/vector-cn.pdf`、站点 `~/Sources/AI/mypopydev-web/docs/books/vector-zh/`

- [ ] **Step 1: 写 `review/findings/汇总-第五轮.md`**（结构照 `汇总-第四轮.md`）

- [ ] **Step 2: 跑全部门槛校验**

```bash
for s in check_structure check_math check_terms check_fidelity check_refs check_emphasis check_residue check_figures; do python3 tools/$s.py 2>&1 | tail -1; done
python3 tools/split_notes.py --check && echo OK
```

- [ ] **Step 3: 重建 PDF 与站点，并做**图号**验收**

```bash
python3 tools/build_pdf.py && python3 tools/check_baseline.py 2>&1 | tail -3
pdftotext dist/vector-cn.pdf /tmp/v.txt && python3 tools/check_figures.py --pdf /tmp/v.txt
python3 tools/build_site.py && python3 tools/build_site.py --check
```

- [ ] **Step 4: 写 `review/quality-report-round5.md`、更新 `README.md`、给 `build_pdf.py` 的版本印记打 tag `v1.0.7`**

- [ ] **Step 5: Commit（不推送）**，停下来请用户决定是否 push + 建 Release

---

## Self-Review

**1. 盲区覆盖**：五个任务全部来自**开工前的实测探针**（图号三方对齐、引文块计数、同章重复括注计数、交叉引用计数、ASCII 引号计数），不是凭空设想。其中 Task 1 的缺陷**已经在线上 PDF 里**，是本轮的最高优先项。

**2. Placeholder scan**：无 TBD/TODO；每个任务给出文件、口径、命令、预期输出与派工文本。

**3. 命名一致性**：findings 统一前缀 `round5-`；新增脚本沿用 `tools/check_*.py`。

**4. 已排除的假警报（探针挡下，不进计划）**：
- `scaler`（原文双关，译稿已加译者注）、`Szcezcin`（与原文拼写一致）——第四轮已排除，本轮复扫仍保留。
- 「图 13.3」「第 14 章」类**引用他人著作**的编号——不算缺陷。
- 索引里夹**英文题名**的 ASCII 引号——本书体例。
- 页码范围标记非递增/重复——实测为 0。

**5. 三处需要你定的判断**（见下）。

---

## Execution Handoff

计划已保存到 `docs/superpowers/plans/2026-09-27-vector-cn-review-round5.md`。

### 用户已定的三项（2026-09-28）

| 问题 | 决定 |
|---|---|
| 图号方案 | **方案 A：显式编号**——图注里写死原书编号，关掉 LaTeX 自动编号 |
| 执行范围 | **Task 1–7 全做** |
| 括注尺度 | **只补技术术语**，日常词不补 |

### 方案 A 的落地细节（已勘定）

1. `tools/header.tex` 加 `\usepackage{caption}` + `\captionsetup{labelformat=empty}`——所有 `\caption` 不再自动加「图 N:」标签，编号完全由译稿文本决定。
2. `cn-book/*.md` 的图注**逐张**加回原书编号；映射关系已用脚本核实为 **53 ↔ 53 逐位置精确配对、图片文件名 0 处不一致**（其中 43 张有编号、10 张无编号）（`en/` 的 `FIGURE` 序列 ↔ `cn-book/` 的图片序列）。
3. **10 张无编号图版**（原书不带 `FIGURE` 号，全是 `pNNN.jpg`）**不加编号**：`p098`（第4章）、`p152`（第6章）、`p186`（第7章）、`p223`/`p226`/`p237`（第9章）、`p246`（第10章）、`p310`（第12章）、`p337`（第13章）、`p382`（注释）。
4. **5 组子图**用原书的大写分幅号：2.3A/2.3B、3.8A/3.8B、6.3A/6.3B/6.3C。
5. 正文引用的**大小写混用是忠实的**——原书正文用小写（`figure 6.3a`）、小标题用大写（`CALCULATIONS FOR FIGURE 2.3A`），中文照此，不算缺陷。
6. **原书自身的引用错误**：`[^ch06n8]` 原文作 `(as in fig. 2.2a)`，但图 2.2 没有 a 分幅（疑应为 2.3a）。译文忠实作「图 2.2a」。**待用户定夺**是否补译者注（同第 2 章「平方反比」的先例）。

### 执行中发现并补入的新盲区

- **Task 6：插图内文字是英文**——实际打开 `fig7_1.jpg` 才看到图内写着 `a) Positive divergence` / `b) Negative divergence (=convergence)` / `c) Examples of zero divergence`。四轮里没人看过图片**内容**。
- 同时确认：正文引「图 7.1b」「图 7.1c」是引用该图的**面板**，图片确实含 a/b/c 三个面板，**不是**缺陷。
