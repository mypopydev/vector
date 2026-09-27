# 《向量》中文译本 · 第四轮细致复核 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在三轮复核（tag `v1.0.3`）之上，补齐**索引词条译文质量**与**强调标记中英对应**两个从未检查过的维度，做一次**逐句级**（而非逐段）精读，并给英文残留做一次全书扫描，最终产出 `v1.0.4`。

**Architecture:** 沿用已验证有效的做法——**并行子代理逐段/逐句双语精读 + 主代理独立回原文核实 + 机械守卫兜底**。本轮新增两类机械守卫（`check_emphasis.py`、`check_residue.py`），并把 round 1 的**逐段**精读加深为**逐句**。分级处置、最小改动、不自动发布等约定不变。

**Tech Stack:** Markdown 译稿（唯一真源）、Python 校验脚本（`tools/check_*.py`）、pandoc + XeLaTeX（PDF）、MkDocs Material（站点）、子代理并行复核。

**Spec:** `docs/superpowers/plans/2026-09-27-vector-cn-review-round2.md`（前三轮方案，八个任务已全绿）、`review/quality-report.md` / `quality-report-round2.md` / `quality-report-round3.md`（历轮结论）、`docs/翻译风格指南.md` + `docs/术语表.md`（442 条）+ `docs/译名表-人名.md`（硬约束）。

## Global Constraints

以下要求对**每一个任务**都生效：

- **禁用译名**：`vector` 全书只译「向量」，禁止「矢量」；`scalar product` 统一「**标量积**」。
- **人名/专名体例**：首现「中文名（English Full Name）」，其后只写中文；文献条目里的作者名/题名/期刊名保留英文；注释与正文的说明性行文一律转写。
- **已归一不可回退**：Christoffel 用全名；Otto Stern＝「斯特恩」；Grace Chisholm (Young)＝「格蕾丝·奇泽姆·扬」；维度写「二维/三维/四维」；`telegraphy`＝「电报」。
- **不得改动**：公式内容、图片文件名、`<!--pNNN-->` 分页标记、脚注编号。
- **不得删减**原文限定语（maybe / seemingly / arguably / apparently）；不得为顺口改事实、数字、专名；**不得整段重写**，建议具体到「删哪几个字／换哪个词」。
- **注释真源**：`cn-book/21.注释.md` 是注释定义的唯一真源，改注释必须改真源后重跑 `python3 tools/split_notes.py` 并 `--check`。
- **交付门槛**：七道校验（`check_structure` / `check_math` / `check_terms` / `check_fidelity` / `check_refs` / `check_baseline` / `split_notes --check`）严重项必须为 0。
- **发布约定**：改动完成后**不自动** commit / push / 推站点仓；先给用户看清单。

---

### Task 1: 索引 636 条中文词条的译文质量与一致性

**Files:**
- Read: `cn-book/22.索引.md`（638 行，636 条）、`en/26_Index.md`、`cn-book/*.md`（正文）
- Create: `review/findings/round4-索引.md`

**Interfaces:**
- Produces: 一份 findings，每条 `索引行号 | 中文词条 | 英文词头 | 问题类型 | 正文里的对应译法 | 建议`。

**为什么这是真盲区**：第一轮只核对了索引的**条数**与**页码**（636 条全量配对、页码 633 一致），第二轮只做了术语归一（标量积等）。**索引里 636 条中文词头本身**——是否准确、是否与正文译法一致、子项是否漏译——**从未被检查过**。索引是读者回查的入口，译名与正文不一致会直接误导。

- [ ] **Step 1: 派 3 个子代理分段核对**（每代理约 212 条）

派工要求（照抄给代理）：
- 输入：`cn-book/22.索引.md` 的第 X 段 + `en/26_Index.md` + `docs/术语表.md` + `docs/译名表-人名.md`。
- 逐条核对三件事：① 中文词头是否准确对应英文词头；② 该译法与**正文**里的用法是否一致（用 grep 在 `cn-book/` 里查）；③ 子项（`代数与它`、`麦克斯韦与他` 这类）是否漏译或生硬。
- 只报**可定位、可验证**的问题：`行号 | 中文词条 | 英文词头 | 类型 | 正文对应译法 | 建议`。类型：`误译` / `与正文不一致` / `漏译` / `生硬`。
- **只做研究，不要改文件**；返回 ≤180 字摘要。

- [ ] **Step 2: 主代理独立核实**

对每条意见回 `en/26_Index.md` 原文 + 正文 grep 核实；剔除误报。

- [ ] **Step 3: 应用「严重 + 中等」**

**改索引前先确认**：同一译名在正文中也要一致（若正文才是错的，改正文而非索引）。

- [ ] **Step 4: 校验 + Commit**

```bash
python3 tools/check_terms.py 2>&1 | tail -1     # 预期：严重 0
git add -A && git commit -m "fix(review): 索引 636 条中文词头的译文质量与一致性"
```

---

### Task 2: 强调标记（斜体/粗体）中英对应 —— 新建守卫

**Files:**
- Create: `tools/check_emphasis.py`
- Create: `review/findings/round4-强调标记.md`

**Interfaces:**
- Produces: 可重复运行的守卫 + 一份候选清单；格式 `文件 | 行号 | EN 强调数 | CN 强调数 | 片段`。

**为什么这是真盲区**：探针实测，全书斜体标记**中文比英文多 346 处**：

| 文件 | EN 斜体 | CN 斜体 | 差 |
|---|---|---|---|
| 序言 | 96 | 108 | +12 |
| 第 1 章 | 133 | 210 | **+77** |
| 第 9 章 | 213 | 306 | **+93** |
| 第 11 章 | 380 | 431 | +51 |
| 第 12 章 | 200 | 301 | **+101** |
| 注释 | 1201 | 1213 | +12 |
| 合计 | 2223 | 2569 | **+346** |

其中一部分是合理的（中文给英文术语补 `*…*` 斜体、数学变量 `*x*` 两边都有），但**超出量需要逐段甄别**：哪些是作者的强调（该保留），哪些是译稿自己加上去的（可能过度强调）。

- [ ] **Step 1: 写 `tools/check_emphasis.py`**

逐段比对 EN 与 CN 的强调标记多重集（`*斜体*`、`**粗体**`），输出「CN 比 EN 多」与「CN 比 EN 少」的段落，按差值排序。复用 `tools/check_structure.py` 的段落切分，跳过公式行、图注、脚注定义续行。

```bash
python3 tools/check_emphasis.py --top 40
```

- [ ] **Step 2: 人工甄别（派 2 个子代理分工）**

要求代理：对每个候选回 `en/` 原文确认——多出来的 `*…*` 是给**英文术语**补的斜体（合理，保留），还是把原文没强调的中文词也斜体了（该去掉）；少掉的则是漏了作者的强调（该补）。

- [ ] **Step 3: 应用确认的项（中等以上）+ Commit**

```bash
python3 tools/check_structure.py 2>&1 | tail -1
python3 tools/check_math.py 2>&1 | tail -1
git add tools/check_emphasis.py review/findings/round4-强调标记.md cn-book/
git commit -m "feat(tools): 新增强调标记守卫 check_emphasis.py；修正过度/遗漏强调"
```

---

### Task 3: 英文残留与未译专名全书扫描

**Files:**
- Create: `tools/check_residue.py`
- Create: `review/findings/round4-英文残留.md`

**Interfaces:**
- Produces: 守卫 + 候选清单；格式 `文件 | 行号 | 残留词 | 上下文 | 判定`。

**探针实测（已排除两处假警报）**：

| 词 | 次数 | 判定 |
|---|---|---|
| `GPS` `NASA` `ETH` `NLP` `MICROSCOPE` `PageRank` `Tensorlab` `Instagram` `OpenAI` `Python` `TensorFlow` `JCMF` | 各 1–7 | **保留**（缩写/专有名，风格指南允许） |
| `scaler` | 1 | **保留**——原文就是双关（scaler「攀登者」/ scalar「标量」谐音），译稿已加译者注 |
| `Szcezcin` | 1 | **保留**——与原文拼写一致（原文另有 Stettin） |
| `NOT` | 1 | **保留**——布尔运算符 |
| `Tripos` | 2 | **保留**——专有考试名，术语表作「荣誉学位考试」，前文已括注 |
| **`wrangler`** | **2** | **待改**——术语表只有 `Second Wrangler | 第二名优胜者`，无通用条目；裸用「wrangler」两处（第 6 章行 16、39） |

- [ ] **Step 1: 写 `tools/check_residue.py`**

扫「中文字符夹 ASCII 单词」的模式，输出候选 + 上下文；对已知缩写作白名单，对术语表/人名表已收的词自动放行。

```bash
python3 tools/check_residue.py
```

- [ ] **Step 2: 逐条判定并修正确认的项**

`wrangler` 两处按术语表口径处理（如「优胜者」或「wrangler（优胜者）」），必要时给术语表补 `wrangler` 条目。

- [ ] **Step 3: Commit**

```bash
git add tools/check_residue.py review/findings/round4-英文残留.md cn-book/ docs/
git commit -m "feat(tools): 新增英文残留守卫 check_residue.py；处理未译专名"
```

---

### Task 4: 逐句级精读（round 1 只做到逐段）

**Files:**
- Read: 全部 `cn-book/*.md` 与对应 `en/*.md`
- Create: `review/findings/round4-逐句-{a,b,c,d}.md`

**Interfaces:**
- Produces: 四份 findings，格式与 `review/findings/13.第9章-从空间到时空.md` 一致，但**粒度到句**。

**为什么必须做**：第一轮是**逐段**双语对照（约 1,900 段），段落内部的句子对句子从未逐条核过。前三轮抓出的错误（漏译限定语、动宾不搭配、插入语隔断定语）几乎都发生在**句子内部**。

- [ ] **Step 1: 派 4 个子代理分段**（序言+第 1–3 章 / 第 4–7 章 / 第 8–10 章 / 第 11–13 章+结语+后附）

派工要求：
- 打开 `en/<章>.md` 与 `cn-book/<章>.md`，**一句一句**对照（按 `。！？` 切句后配对），不要回到段落级的整体印象。
- 每句回答：① 信息是否完整（漏译/增译）？② 意思是否准确（误译/指代/术语）？③ 是否精炼（翻译腔/冗余/语序）？
- 严重度口径不变；**只报可定位、可验证的问题**，具体到字词。
- **只做研究，不要改文件**；返回 ≤200 字摘要。

- [ ] **Step 2: 主代理独立核实 + 应用「严重 + 中等」**

- [ ] **Step 3: 校验 + Commit**

```bash
for s in check_structure check_math check_terms check_fidelity check_refs; do python3 tools/$s.py 2>&1 | tail -1; done
git add -A && git commit -m "fix(review): 逐句级精读修订"
```

---

### Task 5: 公式说明文字与知识框逐句深读

**Files:**
- Read: 各章 `::: {.displayeq}` 前后说明文字（约 67 处）、4 个 `::: {.infobox}` 块
- Create: `review/findings/round4-公式说明与知识框.md`

**Interfaces:**
- Produces: 一份 findings。

**为什么**：第二轮在图注复核时「顺带」看过这 67 处，未逐句深读。公式前后的说明文字是读者理解公式的关键，且术语密度最高。

- [ ] **Step 1: 派 1 个子代理**

要求：逐处对照 EN 与 CN 的**说明文字**（公式本身不动），检查术语、指代、数字、以及「如上/如下」这类方位词是否对应。

- [ ] **Step 2: 主代理核实 + 应用**

- [ ] **Step 3: 校验 + Commit**

```bash
python3 tools/check_math.py 2>&1 | tail -1     # 预期：严重 0
git add -A && git commit -m "fix(review): 公式说明文字与知识框逐句深读"
```

---

### Task 6: 汇总、重建、出报告

**Files:**
- Create: `review/findings/汇总-第四轮.md`、`review/quality-report-round4.md`
- Modify: `README.md`（规模数字）
- Rebuild: `dist/vector-cn.pdf`、站点 `~/Sources/AI/mypopydev-web/docs/books/vector-zh/`

- [ ] **Step 1: 写 `review/findings/汇总-第四轮.md`**

结构照 `review/findings/汇总-第三轮.md`：统计表 + 已应用修订 + 误报说明 + 轻微清单 + 待定夺项。

- [ ] **Step 2: 跑全部门槛校验**

```bash
for s in check_structure check_math check_terms check_fidelity check_refs check_emphasis check_residue; do python3 tools/$s.py 2>&1 | tail -1; done
python3 tools/split_notes.py --check && echo OK
```
预期：七道中五道「严重 0」，两道新增守卫给出候选数（仅提示）。

- [ ] **Step 3: 重建 PDF 与站点**

```bash
python3 tools/build_pdf.py && python3 tools/check_baseline.py 2>&1 | tail -3
python3 tools/build_site.py && python3 tools/build_site.py --check
```

- [ ] **Step 4: 写 `review/quality-report-round4.md` 并更新 `README.md`**

- [ ] **Step 5: Commit（不推送）**

提交后**停下来**，向用户汇报并请其决定是否 `git push` + 打 tag `v1.0.4` + 推站点仓。

---

## Self-Review

**1. 盲区覆盖**：本计划的五个任务全部来自**开工前的实测探针**（索引从未核对词头、斜体 CN 比 EN 多 346 处、`wrangler` 等英文残留），不是凭空设想。逐句级精读是为了补第一轮「只到段落」的粒度缺口。无遗漏。

**2. Placeholder scan**：无 TBD/TODO；每个任务给出命令、预期输出、产出路径与派工文本。

**3. 命名一致性**：findings 统一前缀 `round4-`；新增脚本沿用 `tools/check_*.py` 前缀（`check_emphasis.py`、`check_residue.py`），与既有 `check_refs.py`、`check_style.py` 一致。

**4. 两处需要你定的判断**：
- **Task 1 的改法取向**：索引与正文译法冲突时，以谁为准？（我倾向：**以正文为准**——索引是正文的衍生物；除非正文明显错。）
- **Task 2 的容忍度**：中文给英文术语补斜体是本书既有做法（如 `*整体向量*`），若你要保留这种做法，我会把「为英文术语补的斜体」加进白名单，只报**中文词被斜体**的项。

---

## 执行状态（2026-09-27）

| 任务 | 状态 |
|---|---|
| Task 1 索引词头 | **已完成**：报 43 条 → 应用 19 条（3 处张冠李戴）；拉普拉斯条《分析力学》经查为原文索引原样，保留 |
| Task 2 强调标记 | **已完成**：新增 `check_emphasis.py`（过程中修掉自身正则 bug，候选 288→102）；应用 12 条（8 补 4 删） |
| Task 3 英文残留 | **已完成**：新增 `check_residue.py`；`scaler`/`Szcezcin` 经核为原文如此保留；`wrangler` 补进术语表 |
| Task 4 逐句精读 | **已完成**：约 3,300 组句对；严重 1 / 中等 28（已应用）/ 轻微 42（列清单未改） |
| Task 5 公式说明与知识框 | **已完成**：68 公式块 + 5 知识框；中等 3 已应用 |
| Task 6 汇总/重建/报告 | **已完成**：`review/findings/汇总-第四轮.md`、`review/quality-report-round4.md` |

结果见 `review/quality-report-round4.md`。提交后**未推送**，等用户确认后再 push / 打 tag。

---

## Execution Handoff

计划已保存到 `docs/superpowers/plans/2026-09-27-vector-cn-review-round4.md`。两种执行方式：

**1. 子代理驱动（推荐）** —— 每个任务派新子代理，任务间我来审查，迭代快、上下文干净。

**2. 会话内执行** —— 在当前会话按任务批处理，遇检查点停下来给你看。

开工前请定两件事：

- **范围**：Task 1–6 全做，还是先做两个**新维度**（Task 1 索引词条 + Task 2 强调标记）？逐句级精读（Task 4）工作量最大。
- **Task 1 改法**：索引与正文冲突时以谁为准（我建议以正文为准）。
