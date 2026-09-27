# 《向量》中文译本 · 第二轮细致复核 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在第一轮复核（tag `v1.0.1`）之上，补齐 4 处覆盖盲区、对第一轮约 250 处改动做回归复核、并把「精炼度」从主观印象升级为可量化、可复查的检查，最终产出 `v1.0.2`。

**Architecture:** 沿用第一轮已验证有效的做法——**并行子代理逐段双语精读 + 主代理独立回原文核实 + 五道机械校验兜底**。本轮新增两类工作：一是**回归复核**（把 `v1.0.0 → v1.0.1` 的 diff 逐条回原文验证），二是**覆盖盲区补齐**（前附件、图注、知识框、交叉引用语义、术语误报核验）。所有批次仍按「严重/中等直接改、轻微列清单等用户拍板」的既有约定推进，改动不自动发布。

**Tech Stack:** Markdown 译稿（唯一真源）、Python 校验脚本（`tools/check_*.py`）、pandoc + XeLaTeX（PDF）、MkDocs Material（站点）、子代理并行复核。

**Spec:** `docs/superpowers/plans/2026-09-27-vector-cn-quality-review.md`（第一轮方案与批次划分）、`review/quality-report.md`（第一轮结论与遗留项）、`docs/翻译风格指南.md` + `docs/术语表.md`（442 条）+ `docs/译名表-人名.md`（硬约束）。

## 本轮执行范围（用户 2026-09-27 决定）

**只做四项盲区补齐：Task 2、Task 4、Task 5、Task 6。**
- Task 1（回归对照基线）与 Task 3（回归复核）**本轮不做**——它服务于对 250 处改动的逐条回归，留待下一轮。
- Task 7（精炼度量化扫描）**本轮不做**——精炼度的主观判断用户已接受。
- Task 8（汇总/重建/报告）**本轮做**，但只汇总 Task 2/4/5/6 的结果。
- Task 6 里的注释引文保全改为**全量 353 条**（不是抽查 30 条）。

因此每个任务前的「确认起点干净」沿用一次性执行：五道校验严重 0、`split_notes --check` OK、工作区干净。

## 执行状态（2026-09-27 更新）

| 任务 | 状态 |
|---|---|
| Task 1 回归对照基线 | 未做（本轮范围外，留待下一轮） |
| Task 2 前附件精读 | **已完成** |
| Task 3 回归复核 | 未做（本轮范围外，**下一轮的最高优先项**） |
| Task 4 图注与知识框精读 | **已完成**（53 图注 + 4 知识框 + 67 处公式说明） |
| Task 5 交叉引用 | **已完成**（新增 `tools/check_refs.py`，0 越界） |
| Task 6 机械项结案 | **已完成**（引文 353 条全量；术语 18 项） |
| Task 7 精炼度量化扫描 | 未做（本轮范围外） |
| Task 8 汇总/重建/报告 | **已完成**（`review/findings/汇总-第二轮.md`、`review/quality-report-round2.md`；PDF 与站点已重建） |

结果：核实 61 条意见，应用 19 条；唯一严重项是序言三条图注的编号重复渲染（PDF 已复验修复）。
提交：`54cd647`（**未推送**，等用户确认后再 push / 打 tag）。


## Global Constraints

以下要求对**每一个任务**都生效，逐字来自 `docs/翻译风格指南.md` 与第一轮已确认的约定：

- **禁用译名**：`vector` 全书只译「向量」，**禁止「矢量」**；`scalar product` 统一「**标量积**」（用户 2026-09-27 决定，已全书清零「数量积」）。
- **人名体例**：首现「中文名（English Full Name）」，其后只写中文；文献条目里的作者名/题名/期刊名保留英文；**注释与正文的说明性行文一律转写**（用户决定）。
- **专名归一**：Christoffel 行文一律用全名「埃尔温·克里斯托费尔」；Otto Stern＝「斯特恩」；Grace Chisholm (Young)＝「格蕾丝·奇泽姆·扬」。
- **不得改动**：公式内容（`$…$`、`$$…$$`、`::: {.displayeq}`）、图片文件名、`<!--pNNN-->` 分页标记、脚注编号。
- **不得删减**原文限定语（maybe / seemingly / arguably / apparently 这类分寸词）；不得为顺口改事实、数字、专名；**不得整段重写**，建议要具体到「删哪几个字／换哪个词」。
- **最小改动原则**：逐条 apply，每条记录「改前 → 改后」。
- **注释真源**：`cn-book/21.注释.md` 是注释定义的**唯一真源**，各章末尾的当页脚注是其副本。改注释**必须**改真源后重跑 `python3 tools/split_notes.py` 并 `--check`（该脚本**只增不同步**）。
- **交付门槛**：五道校验全绿（`check_structure` / `check_math` / `check_terms` / `check_fidelity` / `check_baseline` 的**严重项必须为 0**），`split_notes.py --check` 通过。
- **发布约定**：改动完成后**不自动** `git commit` / `git push`、不推站点仓；先给用户看清单。

---

### Task 1: 建回归对照基线

**Files:**
- Create: `review/findings/round2-改动清单.md`
- Create: `/tmp/round2-diff.txt`（临时，不入库）

**Interfaces:**
- Produces: `review/findings/round2-改动清单.md` —— Task 3 的三个回归代理按文件名从这里取自己负责的改动条目；格式为「文件 | 行号 | 改前 | 改后 | 所属批次」。

- [ ] **Step 1: 确认起点干净**

```bash
cd /Users/barryjzhao/Sources/AI/vector
git status --short          # 预期：无输出（工作区干净）
git log --oneline -1        # 预期：a137be3 ... (tag: v1.0.1)
for s in check_structure check_math check_terms check_fidelity; do python3 tools/$s.py 2>&1 | tail -1; done
python3 tools/split_notes.py --check && echo OK
```
预期：四道校验均「严重 0 项」；`split_notes --check` 输出 `OK`。若不满足，**停止**并先向用户报告。

- [ ] **Step 2: 导出两版之间的完整 diff**

```bash
git diff -U0 v1.0.0 v1.0.1 > /tmp/round2-diff.txt
git diff --numstat v1.0.0 v1.0.1
```
记录 `--numstat` 的合计行数（预期：约 57 文件、1600+ 增 / 380 删）。

- [ ] **Step 3: 把 diff 整理成可逐条核对的清单**

按文件分组，为每个 hunk 生成一行：`文件 | 改前行号 | 改前原文 | 改后原文 | 负责批次`。
「负责批次」用 `review/findings/汇总-批次{1,2,3,4}.md` 的表格反查（多数批次表里已写明「改前 → 改后」，可与 diff 对齐）。

写入 `review/findings/round2-改动清单.md`，并在文件里给出统计：total / 按严重度 / 按文件。

- [ ] **Step 4: 自检清单完整度**

```bash
grep -c '^|' review/findings/round2-改动清单.md    # 条目数
git diff --numstat v1.0.0 v1.0.1 | wc -l            # 变更文件数
```
预期：清单条数 ≥ diff 中「`+` 行」的总数减去纯新增文件（`review/findings/`、`review/quality-report.md`）。差额要在清单里写明原因。

- [ ] **Step 5: Commit**

```bash
git add review/findings/round2-改动清单.md
git commit -m "docs(review): 建第二轮回归对照——v1.0.0→v1.0.1 改动清单"
```

---

### Task 2: 前附件精读（第一轮完全未覆盖）

**Files:**
- Read: `cn-book/0.译本说明.md`、`cn-book/1.名家推荐.md`、`cn-book/2.作者简介.md`、`cn-book/3.献词.md`
- Read（对照）: `en/01_Reviews.md`、`en/04_Dedication.md`、`en/02_Halftitle.md`、`en/06_Copyright.md`（按 `en/manifest.json` 确认实际对应关系）
- Create: `review/findings/0.译本说明.md`、`review/findings/1.名家推荐.md`、`review/findings/2.作者简介.md`、`review/findings/3.献词.md`

**Interfaces:**
- Consumes: 无（可并行于 Task 1）
- Produces: 四份 findings，格式与 `review/findings/13.第9章-从空间到时空.md` 一致（标题 + 覆盖说明 + 按严重度排序的意见 + `## 统计` + `## 术语表建议`）。

**为什么这是真盲区**：第一轮 5 个批次覆盖了 `4.序言` ~ `22.索引`，但 `0/1/2/3` 四个文件从未出现在任何 findings 里。合计约 1,600 汉字（译本说明 632、名家推荐 859、作者简介 108、献词 17）。

- [ ] **Step 1: 确认中英对应文件**

```bash
cat en/manifest.json | python3 -m json.tool | head -40
```
确认「名家推荐 / 作者简介 / 献词 / 译本说明」各自对应的 `en/*.md` 是哪一个（不一定 1:1）。

- [ ] **Step 2: 派 1 个子代理做逐段双语精读**

派工要求（照抄给代理）：
- 拿 `en/<对应>.md` + `cn-book/<对应>.md` + `docs/术语表.md` + `docs/译名表-人名.md` + `docs/翻译风格指南.md`，并以 `review/findings/13.第9章-从空间到时空.md` 为格式样板。
- 逐段对照，只报**可定位、可验证**的问题，格式：`位置 | 严重度 | 类型 | 英文原文片段 | 现译片段 | 建议改法`。
- 严重度：`严重`＝意思错了/信息漏了/数字或专名错；`中等`＝意思对但别扭/术语不统一/指代不明；`轻微`＝可更精炼。
- **特别检查 `0.译本说明.md` 里对本书自身的描述是否属实**（页数、条数、体例说明、版权声明），这类文字没有英文原文可对照，只能与仓库实际状态核对。
- **只做研究，不要改 `cn-book/`、`docs/`**；产出写到 `review/findings/<同名>.md`；返回正文 ≤180 字摘要。

- [ ] **Step 3: 主代理独立核实**

对代理报的每条意见，回 `en/` 原文核实（译本说明类条目则回仓库实测值核实）。剔除误报并记入汇总。

- [ ] **Step 4: 应用「严重 + 中等」**

逐条 Edit，最小替换。译本说明里若发现与实测不符的数字（例如仍写「索引 639 条」），一并订正为实测值。

- [ ] **Step 5: 校验 + Commit**

```bash
python3 tools/check_structure.py 2>&1 | tail -1     # 预期：严重 0
git add cn-book/ review/findings/0.译本说明.md review/findings/1.名家推荐.md review/findings/2.作者简介.md review/findings/3.献词.md
git commit -m "fix(review): 前附件精读（第一轮未覆盖的 0–3 号文件）"
```

---

### Task 3: 回归复核——逐条验证第一轮的 250 处改动

**Files:**
- Read: `review/findings/round2-改动清单.md`（Task 1 产出）、`/tmp/round2-diff.txt`
- Read（对照）: 各章 `en/*.md` 与 `cn-book/*.md`
- Create: `review/findings/round2-回归-a.md`（序言 + 第 1–5 章 + 时间线）
- Create: `review/findings/round2-回归-b.md`（第 6–9 章 + 结语 + 致谢）
- Create: `review/findings/round2-回归-c.md`（第 10–13 章 + 注释 + 索引 + 术语/人名表）

**Interfaces:**
- Consumes: Task 1 的 `round2-改动清单.md`
- Produces: 三份回归 findings，每条必须写明「这是第一轮的哪一条改动」+「复核结论：正确 / 引入新错 / 可更好」。

**为什么必须做**：第一轮应用了约 250 处改动，其中**大批量机械替换**最容易引入新错，而**改动后的文本从未被复核过**。高风险项：
- `数量积 → 标量积` 104 处（sed 全局替换）
- 时间线 31 条日期规则 + 26 处英文括注（脚本 + 代理）
- `rank/order → 秩/阶`（第 11 章 4 处 + 注释；同一段里同时出现两者，最容易换错）
- 注释定义「剥除 + 重分发」（内容应与真源逐字一致）
- `模` / `大小` 统一（第 11 章同段两词）

- [ ] **Step 1: 派 3 个子代理，各领一组文件**

派工要求（照抄给代理）：
- 输入：`review/findings/round2-改动清单.md` 里属于你那一组文件的条目 + 对应的 `en/<章>.md`。
- 对**每一条改动**回答三问：① 改后是否忠实于英文原文？② 是否引入了新错（术语、数字、专名、语病）？③ 有没有更好的改法？
- 特别留意**机械替换的副作用**：替换后是否出现语义不通、同段术语混用、指代歧义。
- 输出格式：`文件 | 行号 | 第一轮改动 | 复核结论 | 说明/建议`。
- **只做研究，不要改文件**；返回正文 ≤200 字摘要（只报「引入新错」的条目，正确的不必罗列）。

- [ ] **Step 2: 主代理核实「引入新错」的条目**

对每条「引入新错」回 `en/` 原文核实——**这一步必须自己看原文，不接受代理转述**。

- [ ] **Step 3: 应用「严重 + 中等」修正**

逐条最小 Edit。

- [ ] **Step 4: 校验 + Commit**

```bash
for s in check_structure check_math check_terms check_fidelity; do python3 tools/$s.py 2>&1 | tail -1; done
git add -A && git commit -m "fix(review): 回归复核——修正第一轮批量替换引入的问题"
```

---

### Task 4: 图注与知识框精读（第一轮明确排除的范围）

**Files:**
- Read: 各章 `![...]` 图注（共 53 条）、4 处 `::: {.infobox}` 块（`6.第2章`、`13.第9章`、`16.第12章`×2、`17.第13章`）
- Create: `review/findings/round2-图注与知识框.md`

**Interfaces:**
- Produces: 一份 findings；每条注明 `文件 | 行号 | 图号/框标题 | 严重度 | 问题 | 建议`。

**为什么这是真盲区**：第一轮方案把「公式、图注编号、脚注编号」排除在内容比对之外，只有在第 8、9 章顺带「逐句核对过图注」。53 条图注是散文（往往含术语定义），4 个知识框是整段说明文字，值得单独一遍。

- [ ] **Step 1: 抽出全部图注与知识框，便于逐条核对**

```bash
grep -n "^!\[" cn-book/*.md                                  # 53 条图注
grep -n -A3 "infobox" cn-book/*.md                           # 知识框标题
```

- [ ] **Step 2: 派 2 个子代理（图注 27 条 / 26 条），知识框并入其一**

要求同 Task 2 的派工说明，另加：图注里的 `FIGURE N.M` 编号须与 `en/` 一致；图注内行内公式（`$…$`）不得改动。

- [ ] **Step 3: 主代理核实 + 应用「严重 + 中等」**

- [ ] **Step 4: 校验 + Commit**

```bash
python3 tools/check_structure.py 2>&1 | tail -1
python3 tools/check_math.py 2>&1 | tail -1
git add -A && git commit -m "fix(review): 图注与知识框精读"
```

---

### Task 5: 交叉引用语义核对（164 + 190 + 43 处）

**Files:**
- Create: `tools/check_refs.py`
- Read: 全部 `cn-book/*.md`、`en/*.md`
- Create: `review/findings/round2-交叉引用.md`

**Interfaces:**
- Produces: `tools/check_refs.py`（可重复运行的守卫）+ 一份 findings。
- 脚本产出格式：`文件 | 行号 | 引用文本 | 引用类型 | 结论`（结论 ∈ `OK` / `越界` / `可疑`）。

**为什么这是真盲区**：第一轮只保证了交叉引用的**格式**中英一致，没验证**指向**是否正确。「第 N 章」「图 N.M」「尾注 N」共约 397 处，指错会误导读者的回查。

- [ ] **Step 1: 写 `tools/check_refs.py`**

三类引用分别校验：
1. **`图 N.M`**：N 应在 1–13（序言为 0），且该章确实存在第 M 张图（对照 `images/figN_M.jpg` 是否存在）→ 越界即报。
2. **`第 N 章`**：N 应在 1–13 → 越界即报。
3. **`尾注 N`**：该章注释条目数应 ≥ N → 越界即报。

复用 `tools/check_structure.py` 的段落切分与 `<!--pNNN-->` 处理方式，避免把标记误当引用。

```bash
python3 tools/check_refs.py        # 预期：先跑出全部越界/可疑项，再人工判定
```

- [ ] **Step 2: 人工判定可疑项**

对「未越界但可能指错」的条目（例如正文说「第 10 章讨论 X」，而 X 实际在第 11 章）派 1 个子代理抽查 30 处，回 `en/` 原文核实原书是否也这么指。

- [ ] **Step 3: 修正确认指错的条目（严重）+ Commit**

```bash
python3 tools/check_structure.py 2>&1 | tail -1
git add tools/check_refs.py review/findings/round2-交叉引用.md cn-book/
git commit -m "feat(tools): 新增交叉引用守卫 check_refs.py；修正指错的引用"
```

---

### Task 6: 术语误报核定 + 引文保全的 3 项中等项结案

**Files:**
- Read: `review/terms.md`（18 项中等）、`review/fidelity.md`（引文保全中等 3 项）、`docs/术语表.md`
- Create: `review/findings/round2-机械项结案.md`

**Interfaces:**
- Produces: 一份结案表：每项给出「误报 / 真问题」的**判定证据**（引文 + 实测），真问题进入修订。

**为什么必须做**：`review/acceptance-report.md` 断言「术语 18 项中等全是多义词误报」，但**没有留下逐条证据**；`check_fidelity` 的「引文数量偏少」中等 3 项（第 9 章 61→53、注释 300→187、索引 20→0）在第一轮方案里注明「需人工判断」，**至今未结案**。

- [ ] **Step 1: 逐条核定术语 18 项**

对每项取出英文词在正文里的**全部**出现位置，逐处判断是否该用表内译名（例：`power` 作「威力」而非「幂」即误报）。把证据写进结案表。

- [ ] **Step 2: 逐条核定引文 3 项（注释按用户要求改为全量 353 条）**

```bash
python3 tools/check_fidelity.py 2>&1 | grep -A3 "引文数量偏少"
```
第 9 章：人工比对 `en/17_Chapter09.md` 与 `cn-book/13.第9章-从空间到时空.md` 的成对引号内容，确认少掉的 8 段是「术语译成中文后不带引号」（正常）还是「真漏了题名」。
注释：**全量 353 条**逐条比对 `en/25_Notes.md` 与 `cn-book/21.注释.md` 的成对引号内容，分三个区段（序言+第 1–4 章 / 第 5–9 章 / 第 10–13 章+结语）派 3 个子代理；判定口径：① 术语译成中文后可失去引号（正常）；② 文献题名/期刊名/文章标题的引号**必须保留**（丢失即严重）；③ 引号内容被整段删掉即严重。
索引 20→0：确认中文索引确实不需要英文引号（索引条目是「中文（English）」形式）。

- [ ] **Step 3: 把真问题修掉，误报写进结案表**

- [ ] **Step 4: Commit**

```bash
git add review/findings/round2-机械项结案.md cn-book/ docs/
git commit -m "docs(review): 术语误报与引文保全中等项逐条结案"
```

---

### Task 7: 跨章精炼度量化扫描

**Files:**
- Create: `tools/check_style.py`
- Create: `review/findings/round2-精炼度.md`

**Interfaces:**
- Produces: `tools/check_style.py` + 一份按「偏离度」排序的候选清单（仅提示，不自动改）。

**为什么必须做**：第一轮的「轻微」全部来自各章代理的**主观**判断，缺少跨章可比的量化口径，导致同一类翻译腔在这一章被报、在那一章被漏。

- [ ] **Step 1: 写 `tools/check_style.py`，输出 5 类信号**

对 `cn-book/*.md` 逐段计算：
1. **「的」字密度**：`的` 数 / 汉字数，标出超章节中位 2σ 的段落。
2. **被动/名词化套话**：匹配 `进行(了)?…的处理|予以…|作出了…的|是…的|被…所` 等模式。
3. **连续连接词**：同一句出现 ≥2 个「因为/所以/但是/而」。
4. **重复指代**：相邻两句以同一代词（他/它/这）开头。
5. **长句**：单句 > 120 汉字的段落（作者本人喜欢长句，故仅列**待判断**，不判缺陷）。

```bash
python3 tools/check_style.py > /tmp/style.txt && head -40 /tmp/style.txt
```

- [ ] **Step 2: 人工筛选候选（派 2 个子代理分工）**

要求代理：对每个候选回 `en/` 原文确认是「翻译腔」（该改）还是「作者风格/分寸词」（不该动）；**只报该改的**，并给出具体到字词的改法。

- [ ] **Step 3: 应用「严重 + 中等」，其余列轻微清单**

- [ ] **Step 4: 校验 + Commit**

```bash
for s in check_structure check_math check_terms check_fidelity; do python3 tools/$s.py 2>&1 | tail -1; done
git add tools/check_style.py review/findings/round2-精炼度.md cn-book/
git commit -m "feat(tools): 新增精炼度量化扫描 check_style.py；清理翻译腔"
```

---

### Task 8: 汇总、重建、出报告

**Files:**
- Create: `review/findings/汇总-第二轮.md`
- Create: `review/quality-report-round2.md`
- Modify: `README.md`（若规模数字变化）
- Rebuild: `dist/vector-cn.pdf`、站点 `~/Sources/AI/mypopydev-web/docs/books/vector-zh/`

**Interfaces:**
- Consumes: Task 2–7 的全部 findings
- Produces: 汇总清单（供用户过目）+ 重建产物 + 报告。

- [ ] **Step 1: 写 `review/findings/汇总-第二轮.md`**

结构照 `review/findings/汇总-批次3.md`：统计表（报告 / 核实为真 / 误报 / 已应用）+ 已应用修订表 + 误报说明 + 轻微清单 + 待定夺项。

- [ ] **Step 2: 跑全部门槛校验**

```bash
for s in check_structure check_math check_terms check_fidelity; do python3 tools/$s.py 2>&1 | tail -2; done
python3 tools/split_notes.py --check && echo OK
python3 tools/check_refs.py 2>&1 | tail -3
python3 tools/check_style.py 2>&1 | tail -3
```
预期：五道校验严重 0；`split_notes --check` OK。

- [ ] **Step 3: 重建 PDF 与站点**

```bash
python3 tools/build_pdf.py && python3 tools/check_baseline.py 2>&1 | tail -3
python3 tools/build_site.py && python3 tools/build_site.py --check
```
预期：`check_baseline` 缺字形/丢字/越界均为 0；`build_site --check` 问题 0。

- [ ] **Step 4: 写 `review/quality-report-round2.md` 并更新 `README.md`**

README 里受影响的数字：汉字总数、索引条数、术语表条数、PDF 页数。

- [ ] **Step 5: Commit（不推送）**

```bash
git add -A
git commit -m "chore(review): 第二轮细致复核——汇总、重建产物、出报告"
```
提交后**停下来**，向用户汇报并请其决定是否 `git push` + 打 tag `v1.0.2` + 推站点仓。

---

## Self-Review

**1. Spec coverage（对照第一轮方案与 quality-report 的遗留项）**

| 来源要求 | 落在哪个任务 |
|---|---|
| 前附件从未复核（本次自查发现的真盲区） | Task 2 |
| 第一轮 250 处改动未回归 | Task 3 |
| 图注/知识框被排除在内容比对之外 | Task 4 |
| 交叉引用只校验格式、未校验指向 | Task 5 |
| 术语 18 项中等「断言为误报但无证据」 | Task 6 |
| 引文保全 3 项中等「需人工判断」未结案 | Task 6 |
| 精炼度缺少跨章量化口径 | Task 7 |
| 批次 5「跨章风格统一 + 汇总修订 + 重建产物 + 出报告」 | Task 7 + Task 8 |
| 「发布需用户确认」的既有约定 | Task 8 Step 5 |

无遗漏。

**2. Placeholder scan**：全文无 TBD/TODO；每个任务都给出了命令、预期输出与产出路径；派工说明写成可直接转发给子代理的文本。

**3. Type consistency**：findings 命名沿用「与 `cn-book/` 同名」的既有约定（`0.译本说明.md` … `22.索引.md`），第二轮新增文件统一前缀 `round2-`，与第一轮的 `汇总-批次N.md` 不冲突。`tools/check_refs.py`、`tools/check_style.py` 命名沿用 `tools/check_*.py` 既有前缀。

**4. 本轮已按用户决定缩范围**：只做四项盲区（Task 2/4/5/6），注释引文全量。Task 1/3/7 留待下一轮。

---

## Execution Handoff

计划已保存到 `docs/superpowers/plans/2026-09-27-vector-cn-review-round2.md`。两种执行方式：

**1. 子代理驱动（推荐）** —— 每个任务派一个新子代理，任务间我来审查，迭代快、上下文干净。

**2. 会话内执行** —— 在当前会话按任务批处理，遇到检查点停下来给你看。

另外，开工前有两件事请你定：

- **范围**：Task 2–7 是全部做，还是先做「盲区补齐」四项（Task 2/4/5/6）？回归复核（Task 3）和精炼度扫描（Task 7）工作量最大。
- **注释引文**：Task 6 里注释的引文保全，抽查 30 条还是全量 353 条？
