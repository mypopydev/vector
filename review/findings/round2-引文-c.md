# 注释引文核对（第 10–13 章 + 结语）

区段：`cn-book/21.注释.md` 第 380–568 行（「## 第 10 章」→ 文件末尾） ↔ `en/25_Notes.md` 第 818–1245 行（`## CHAPTER 10` → 文件末尾）。

## 覆盖证据

**逐条全覆盖 117 条，无抽样。** 中英按 `[^chNnM]` 编号切块后一一配对，两侧各 117 条，编号集合完全相同（无缺条、无多出条）。

| 章 | 注释条数 | 英文成对双引号 | 中文成对双引号 |
|---|---|---|---|
| 第 10 章（ch10n1–n16） | 16 | 10 | 10 |
| 第 11 章（ch11n1–n25） | 25 | 23 | 23 |
| 第 12 章（ch12n1–n47） | 47 | 70 | 70 |
| 第 13 章（ch13n1–n24） | 24 | 18 | 18 |
| 结语（ch14n1–n5） | 5 | 4 | 4 |
| **合计** | **117** | **125** | **125** |

核对方法（脚本逐条跑，再逐条人工并排复核）：

1. **双引号逐条计数**：117 条中，每条的英文双引号对数 = 中文双引号对数（无一例外）。
2. **逐对内容比对**：把英文每一对 `“…”` 的内容拿到对应中文注释里做精确子串匹配。除「术语中译」那一类（见下）外，**每一个英文引文片段都与中文逐字符一致**——即 100+ 个英文文献题名／文章标题（`"The Mystery of Riemann’s Curvature,"`、`"MICROSCOPE Mission…"`、`"Lost in the Tensors…"`、`"Did Einstein ‘Nostrify’ Hilbert’s Final Form of the Field Equations?,"` 等）全部**原样保留并带引号**，无一处丢失、无一处截断拼错。
3. **嵌套单引号**：英文 11 对 `‘…’`（`‘Commentatio’`、`‘Zürich Notebook’`×3、`‘Digital Colonialism’`、`‘Belated Decision…’`、`‘Nostrify’`、`‘Cosmic Fossil’`、`‘Revolution in Science’` 等）中文 11 对，逐字符一致，全部保留。
4. **反向增译检查**：中文每一对引号都能在英文找到对应来源（要么原样保留英文，要么是英文术语的中译），**无凭空新增的引号内容**。
5. **整段漏译排查**：32 个 URL 两侧各 32 个、数量与内容一一对应；多段注释（ch10n6、ch11n22、ch12n21、ch12n44、ch13n11 等）的段落数在扣除英文 `::: {.displayeq}` 围栏行后完全相等；斜体书目（*Einstein*、*Ideas and Opinions*、*Nature*、*Historia Mathematica*、*Mathematische Annalen* 等）与 *Entwurf*（中文作《纲要》并括注 *Entwurf*）均在。未发现整段删落。

**「术语中译不带引号」属既定做法，不计问题**，本区段共 20 处：ch10n5 `signature`→「号差」、ch11n5 `unofficial`→「非正式」、ch11n10 `additive/subtractive/opposites`→「加色法／减色法／相反」、ch11n14（整句量子比特引语）→中译、ch11n20 `Unruh effect/quantum thermometer`→「昂鲁效应／量子温度计」、ch11n23 `cancel`→「抵消」、ch12n8 `vacuum equations`→「真空方程」、ch12n9 `Serious mistakes`→「严重的错误」、ch12n12（爱因斯坦广义相对性原理整句）→中译、ch12n16 `minimising/extremising`→「极小化／取极值」、ch12n17 `Caught fire`→「燃起来了」、ch12n21 `local`×3/`November tensor`→「局域」／「十一月张量」、ch12n22 `heavy heart`→「沉重心情」、ch12n30（爱因斯坦 1916 年整句）→中译、ch12n40 `free-falling`→「自由下落」、ch12n41 `nonrelativisitic`→「非相对论」、ch12n43 `traces/priority dispute`→「迹／优先权之争」、ch13n4 `momentum`→「动量」、ch13n5 `symmetry groups/symmetry`→「对称群／对称性」。这些均**保留了引号**，只是内容中译，语义完整。

## 结论：`check_fidelity.py` 的缺口不在本区段

全文件统计：英文 `“` 348 个，中文 251 个。按章切分后——

- 第 1–9 章：英文 223 对 vs 中文 126 对（**缺口 97 对，集中在这里**）
- 第 10–13 章 + 结语（本区段）：英文 125 对 vs 中文 125 对（**零缺口**）

即脚本报的「英文 300 段引文、中文 187 段」这一信号，在本区段不成立；本区段的中文注释对英文引文的保留是完整的。建议把复核精力放在第 1–9 章（另一批次的区段）。

---

## 问题列表（按严重度排序）

本区段**无严重、无中等**问题。仅 1 条轻微待判：

- `ch12n4` | 轻微 | 引文丢失（待判） | `Some translate “happiest” as “most fortunate.”` | `有人把“happiest”译为“最幸运的”。` | 英文两个带引号的词，中文只保留了 `“happiest”`、`“most fortunate”` 被中译掉，同一句内处理不一致。这既非题名也非漏译，语义无损（该句正是在讲这个词该怎么译），属可选项：若要与 `“happiest”` 保持对照，建议改为「有人把“happiest”译为“most fortunate”（最幸运的）」；若体例允许中译，维持现状亦可。

### 备注（非问题，仅记录）

- `ch12n37`、`ch13n2`：英文把逗号写在引号内（`“Hilbert’s Foundation of Physics,”`、`“General Covariance and the Foundations of General Relativity,”`），中文按中文标点习惯放在引号外。属标点体例差异，题名本身完整，不计问题。
- `ch12n21`、`ch12n23`：英文斜体 *Entwurf* 在中文作《纲要》（*Entwurf*），采用书名号并括注原文，符合「题名可写《…》」的体例，原文未丢失。

## 统计

- 覆盖注释：117 条（第 10 章 16 / 第 11 章 25 / 第 12 章 47 / 第 13 章 24 / 结语 5），逐条比对，无抽样
- 英文成对双引号 125 对 vs 中文 125 对：逐条 1:1，无丢失、无增译
- 严重：0
- 中等：0
- 轻微（待判）：1（ch12n4 `most fortunate` 被中译）
- 术语中译不带引号而不计问题的：20 处（分布在 20 条注释）
