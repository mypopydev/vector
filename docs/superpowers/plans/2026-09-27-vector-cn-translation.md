# 《Vector》中文译本 + LaTeX 排版 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 `/Users/barryjzhao/Sources/AI/vector` 下的 epub《Vector: A Surprising Story of Space, Time, and Mathematical Transformation》全书中译为 Markdown 译稿，并用 pandoc + XeLaTeX(ctexbook) 排成一本可打印/可阅读的中文 PDF。

**Architecture:** 三段式流水线，中间产物全部落在仓库里、可复查可重跑：
1. **抽取** —— `tools/extract_epub.py` 把 epub 的 XHTML 转成带结构锚点的英文 Markdown（`en/`），其中 MathML 由 `tools/mathml2tex.py` 转成 LaTeX，图片落到 `images/`；
2. **翻译** —— 先产出术语表/风格指南与「样本章」确立基线，再由并行子代理按章把 `en/` 逐段译为 `cn-book/`，每章译完立刻过结构/术语/公式三道机器校验；
3. **排版** —— `tools/build_pdf.py` 合并 `cn-book/` → pandoc → XeLaTeX(ctexbook) → `dist/vector-cn.pdf`，并用 `check_baseline.py` 守住缺字形、越界裁切、内容被吞等事故。

**Tech Stack:** Python 3（标准库为主）、pandoc 3.11、XeLaTeX (TeX Live 2026)、ctexbook + xeCJK + unicode-math + tcolorbox、pandoc Lua filter（infobox）、系统 `sort`（`LC_ALL=zh_CN.UTF-8` 做中文拼音排序，避免引入 pypinyin 依赖）。

**Spec:** 本 Plan 即设计文档（已含全局约束与验收标准），无独立 spec 文件。

## Global Constraints

- **原文不可改**：`*.epub` 只读；所有加工产物写到 `en/`、`cn-book/`、`images/`、`dist/`。
- **Markdown 是唯一真源**：中文正文只维护 `cn-book/*.md` 一份，PDF 由脚本生成；手改 PDF 或 `.tex` 中间文件一律无效。
- **不跳译、不概括**：逐段逐句翻译，段数/图数/公式数/尾注数必须与 `en/` 严格对齐（由 `check_structure.py` 强制）。
- **公式只转不译**：MathML → LaTeX，符号、变量名保持原文，只翻译公式前后的说明文字。
- **术语一致性**：所有译名以 `docs/术语表.md` 为准，术语表是全项目硬约束。
- **索引页码 = 英文原版页码**（用户已确认），正文页边用灰色小字标出原版页码以便对照。
- **尾注全部翻译**（用户已确认，353 条），文献题名保留英文原文。
- **页边页码标记可用 `--no-page-marks` 关闭**；Markdown 源里只存 `<!--p123-->` 注释，原始 TeX 只在构建时注入。
- **构建必须离线可复现**：字体集钉死为 `fontset=macold`，`CJKmainfont=Songti SC`，数学字体 `Latin Modern Math`。
- 本机 `pip install` 受 PEP 668 限制，**不新增 Python 依赖**；需要拼音排序时调用系统 `sort`。

---

### Task 1: 仓库骨架与译本说明

**Files:**
- Create: `.gitignore`
- Create: `cn-book/0.译本说明.md`
- Create: `README.md`（骨架，Task 12 补全）

**Interfaces:**
- Produces: `cn-book/` 目录约定、`0.译本说明.md`（后续 `build_pdf.py` 的 `FRONT` 列表第一项）。

- [ ] **Step 1: 建立目录**

```bash
mkdir -p cn-book en images docs/superpowers/plans tools dist
```

- [ ] **Step 2: 写 `.gitignore`**

```
dist/build/
__pycache__/
.DS_Store
```

- [ ] **Step 3: 写 `cn-book/0.译本说明.md`**
  内容必须包含（中文，约 300 字）：
  - 原书名《Vector: A Surprising Story of Space, Time, and Mathematical Transformation》、作者 Robyn Arianrhod（罗宾·阿里安罗德）、原版页码说明；
  - **版权声明**：本译本为个人学习用途的非商业翻译，原文版权归原作者与出版社所有，不得用于任何商业用途；
  - 译本说明：术语处理方式（首次出现「中文（English）」）、人名保留英文、索引页码为英文原版页码、页边灰色数字为原版页码。

- [ ] **Step 4: 写 README 骨架**：项目一句话简介 + 目录结构 + 构建命令占位（Task 12 填内容）。

- [ ] **Step 5: 校验**：`ls -R` 确认目录齐备，`cn-book/0.译本说明.md` 中含「非商业」四字。

---

### Task 2: epub 抽取器（XHTML → Markdown + 图片）

**Files:**
- Create: `tools/extract_epub.py`
- Create: `en/manifest.json`（脚本生成）

**Interfaces:**
- Produces: `en/<stem>.md`（`08_Prolog.md`、`09_Chapter01.md` … `26_Index.md`）、`images/*.jpg`（59 张，排除 `mathjax/images/`）、`en/manifest.json`（段数/图数/公式数/尾注数统计，供 Task 8 的 `check_structure.py` 消费）。

**已勘察的 epub 结构（照此实现，勿凭猜测）：**
- 章节文件：`OEBPS/xhtml/{01_Cover,02_Halftitle,03_Reviews,04_Dedication,05_Titlepage,06_Copyright,07_Contents,08_Prolog,09_Chapter01 … 21_Chapter13,22_Epilog,23_Timeline,24_Acknowledgments,25_Notes,26_Index,26_Index_a,26_Index_b}.xhtml`
- 章标题：`<h1 class="chno"><span … id="page_1"/>(1) <span class="chtitle">THE LIBERATION OF ALGEBRA</span></h1>`
- 节标题：`<h2 class="head2">`、`h2.head2bm`；章副标题：`<p class="subh">On the Way to Tensors</p>`
- 段落：`p.indent`（缩进段）、`p.noindent`、`p.noindentt`、`p.indent-r`
- 行间公式：`p.eqn`（可带 `id="eq1"`），公式编号：`<span class="eqno">(1)</span>`
- 分隔符号：`p.star`（`• • •`）
- 图：`<figure><div class="image"><img class="wid50" id="f1_1" src="../images/fig1_1.jpg"/></div><figcaption><p class="figcap"><span class="bsans">FIGURE 1.1</span>. 图注…</p></figcaption></figure>`
  - 宽度类：`wid20/wid50/wid60/wid80` → `{width="20%"}` …
- 知识框：`<div class="box"><p class="boxhead">标题</p>…</div>`
- 引文：`<p class="extract">`、`<blockquote>`
- 尾注：`<p class="nlist"><span class="n-no"><a … id="ch01fn1">1</a>.</span>正文</p>`，续段 `p.nlist2` / `p.nlist2a`
- 索引：`<p class="index1"><span epub:type="index-term">词条: 子项, <a epub:type="index-locator" href="09_Chapter01.xhtml#page_4">4</a>, …</span></p>`
- 时间线：`<p class="hang_1a">ca. 3000 BCE, …</p>`
- 原版分页：`<span aria-label="pagebreak" … id="page_4" role="doc-pagebreak" title="4"/>` → 输出 `<!--p4-->`
- 行内标记：`<i>`→`*`、`<b>`→`**`、`<sup>`→`^…^`、`<sub>`→`~…~`、`span.sc`（小型大写报纸标题）→ 保留原文并加 `**`
- 脚注引用：`<sup><a href="25_Notes.xhtml#ch01fn1" id="ch01rfn1">1</a></sup>` → `[^ch01n1]`

- [ ] **Step 1: 写 `tools/extract_epub.py`**（参考 `ai-agents-in-action-2nd-edition-cn/tools/extract_epub.py` 的 HTMLParser 骨架，按上面的类目表重写规则），要点：
  - CLI：`python3 tools/extract_epub.py [--epub PATH] [--out en] [--images images]`
  - 按上面的映射表输出 Markdown；`26_Index*.xhtml` 三个文件按字母序合并为单个 `en/26_Index.md`。
  - `<math>` 节点交给 `mathml2tex.convert(math_xml)`（Task 3 提供，先定义函数签名 `convert(math_xml: str, display: bool) -> str`）。
  - 每个文件尾部写 `<!--stats: p=NN fig=NN eq=NN note=NN -->`，并汇总进 `en/manifest.json`。

- [ ] **Step 2: 抽取图片**：只取 `OEBPS/images/` 下 59 张（`cover.jpg`、`fig*.jpg`、`p*.jpg`、`logo.jpg`），跳过 `OEBPS/mathjax/images/`；附带打印尺寸以便核对宽高比。

- [ ] **Step 3: 跑脚本**

```bash
python3 tools/extract_epub.py
```

- [ ] **Step 4: 校验**：`en/manifest.json` 中 Prolog/13 章/Epilog/Notes 的词数与实测一致（Prolog 6437、Ch11 12688、Notes 25625，允许 ±3%）；`images/` 下 59 个 jpg。

- [ ] **Step 5: 目视抽查** `en/09_Chapter01.md` 前 60 行：章标题、节标题、公式、图注、脚注引用、分页锚点是否都对。

---

### Task 3: MathML → LaTeX 转换器（全书公式的正确性命门）

**Files:**
- Create: `tools/mathml2tex.py`
- Create: `tools/test_mathml2tex.py`

**Interfaces:**
- Consumes: Task 2 传入的 `<math …>…</math>` 原始 XML 字符串。
- Produces: `convert(math_xml: str, display: bool) -> str`；全书 262 处公式依赖它；Task 11 的 `check_math.py` 调用它做可编译性校验。

**已勘察的 MathML 标签全集（19 个，逐个列出，不允许遗漏）：**
`math, mrow, mi, mn, mo, mtext, mspace, msup, msub, msubsup, mfrac, msqrt, mroot, mfenced, mtable, mtr, mtd, mstyle, mover, munder, munderover`

- [ ] **Step 1: 写失败用例** `tools/test_mathml2tex.py`，至少覆盖以下 8 个真实样本（全部取自 epub 原文）：

```python
CASES = [
    # (MathML, 期望 LaTeX)
    ('<mfrac><mrow><mi>a</mi><mi>b</mi></mrow><mn>2</mn></mfrac>', r'\frac{ab}{2}'),
    ('<msup><mi>c</mi><mn>2</mn></msup>', r'c^{2}'),
    ('<msqrt><mrow><mo>−</mo><mn>1</mn></mrow></msqrt>', r'\sqrt{-1}'),
    ('<mroot><mrow><mi>r</mi><msup><mi>e</mi><mrow><mi>i</mi><mtext>θ</mtext></mrow></msup></mrow></msup></mroot>'.replace('</msup></mroot>','</mroot>'), r'\sqrt[3]{re^{i\theta}}'.replace('re','r e')),  # 见下注
    ('<mfenced><mrow><mi>a</mi><mo>+</mo><mi>b</mi></mrow></mfenced>', r'\left(a+b\right)'),
    ('<mover accent="true"><mi>b</mi><mo stretchy="true">¯</mo></mover>', r'\bar{b}'),
    ('<msub><mi>u</mi><mn>1</mn></msub>', r'u_{1}'),
    ('<mi>sin</mi><mn>45</mn><mo>°</mo>', r'\sin 45^{\circ}'),
]
```

  > 注：第 4 条以 epub 中 `25_Notes.xhtml` 的真实片段为准（`<mroot><mrow>...<msup><mi>e</mi><mrow><mi>i</mi><mtext>θ</mtext></mrow></msup></mrow></mfenced>` 结构），期望值按实际结构写，禁止用「TBD」占位。

  另加两条结构用例：`mtable/mtr/mtd` 包在 `mfenced` 里（列向量）→ 期望 `\begin{pmatrix} u_{1} \\ u_{2} \end{pmatrix}`；`mtable` 内嵌（矩阵）→ 期望 `\begin{matrix} … \\ … \end{matrix}`。

- [ ] **Step 2: 跑测试确认失败**

```bash
python3 tools/test_mathml2tex.py
```
Expected: FAIL（`convert` 未定义）。

- [ ] **Step 3: 实现 `tools/mathml2tex.py`**（`xml.etree.ElementTree` 递归，去掉 MathML 命名空间）：

| MathML | LaTeX |
|---|---|
| `mi`/`mn` | 字面量；`mi` 若是 `sin/cos/tan/ln/log/exp/lim/det/dim/grad/div/curl` → `\sin` 等 |
| `mo` | 查符号表：`−`→`-`、`×`→`\times`、`·`→`\cdot`、`±`→`\pm`、`≤`→`\le`、`≥`→`\ge`、`≠`→`\ne`、`→`→`\to`、`∞`→`\infty`、`∂`→`\partial`、`∇`→`\nabla`、`°`→`^{\circ}`、`′`→`'` |
| `mtext` | `\text{…}` |
| `mspace` | `\;`（`width` 属性 > 0.5em 时） |
| `msup` | `{}^{}`（base 为 `mfenced`/`mrow` 时给 base 加 `\left…\right` 之外的花括号保护） |
| `msub` / `msubsup` | `_{}` / `_{}^{}` |
| `mfrac` | `\frac{}{}`（`bevelled="true"` → `{}/{}^{}` 的 `{}^{}`… 直接写 `{}^{ }/{}^{ }` 形式：`a/b`） |
| `msqrt` | `\sqrt{}`；`mroot` → `\sqrt[3]{}` |
| `mfenced` | 按 `open`/`close` 属性，缺省 `\left( … \right)`；`open="["`→`\left[`；`open=""`→ 不输出定界符 |
| `mtable/mtr/mtd` | `\begin{pmatrix}…\\…\end{pmatrix}`（外层已是 `mfenced` 圆括号时用 `matrix` 避免双重括号 —— 由 `convert` 的 `parent_fenced` 参数决定） |
| `mstyle` | 透传子节点 |
| `mover`+`accent="true"` | `¯`→`\bar{}`、`^`→`\hat{}`、`~`→`\tilde{}`、`→`→`\vec{}`、`.`→`\dot{}`；否则 `\overset{}{}` |
| `munder` / `munderover` | `\underset{}{}` / `\underset{}{\overset{}{}}` |

  输出包装：`display=True` → `$$…$$`，否则 `$…$`。

- [ ] **Step 4: 跑测试确认通过**

```bash
python3 tools/test_mathml2tex.py
```
Expected: PASS（全部用例）。

- [ ] **Step 5: 全量自检** —— 遍历 epub 全部 262 处 `<math>`，逐条转换并断言：
  - 转换结果不含 `None` / 空串；
  - 不含未映射的 MathML 标签名（正则查 `m(?!ath)[a-z]+` 残留在输出里）；
  - 生成的 LaTeX 全部汇总写入 `dist/build/all-formulas.tex`，用 `xelatex` 编译一次（`-halt-on-error`），**缺字形与报错均为 0**。

- [ ] **Step 6: 抽样目视** —— 从第 9、11、19 章各取 3 条转换结果，与原文语义对照，确认 `mtable` 列向量、`mfenced` 括号、`mover` 重音无误。

---

### Task 4: 术语表、译名表与翻译风格指南

**Files:**
- Create: `docs/术语表.md`
- Create: `docs/译名表-人名.md`
- Create: `docs/翻译风格指南.md`

**Interfaces:**
- Produces: 三份文档，是 Task 5–9 所有子代理的**强制输入**；Task 10 的 `check_terms.py` 直接读 `docs/术语表.md` 做一致性校验。

- [ ] **Step 1: 建 `docs/术语表.md`**（Markdown 两列表格，先按本书主题预填，后续每译完一章增补）：

| English | 中文 |
|---|---|
| vector | 向量 |
| scalar | 标量 |
| quaternion | 四元数 |
| versor | 旋量（四元数术语，首次出现加注原词） |
| tensor | 张量 |
| matrix | 矩阵 |
| determinant | 行列式 |
| dot product / scalar product | 点积 / 数量积 |
| cross product / vector product | 叉积 / 向量积 |
| gradient / divergence / curl | 梯度 / 散度 / 旋度 |
| (vector) field | （向量）场 |
| magnitude | 模（长） |
| component | 分量 |
| imaginary number / complex number | 虚数 / 复数 |
| manifold | 流形 |
| curvature | 曲率 |
| parallel transport | 平行移动 |
| geodesic | 测地线 |
| metric (tensor) | 度规（张量） |
| covariant / contravariant | 协变 / 逆变 |
| covector / one-form | 余向量 / 一次形式 |
| bra / ket | 左矢 / 右矢 |
| qubit | 量子比特 |
| spacetime | 时空 |
| frame of reference | 参照系 |
| invariant | 不变量 |
| index notation | 指标记号 |
| inner/outer product | 内积 / 外积 |
| eigenvalue / eigenvector | 特征值 / 特征向量 |
| commutative / associative / distributive | 交换律 / 结合律 / 分配律 |
| calculus / fluxion | 微积分 / 流数术 |
| completion and balancing | 还原与对消（al-Khwārizmī 术语） |

- [ ] **Step 2: 建 `docs/译名表-人名.md`**：Hamilton 哈密顿、Maxwell 麦克斯韦、Grassmann 格拉斯曼、Gibbs 吉布斯、Heaviside 亥维赛、Tait 泰特、Riemann 黎曼、Levi-Civita 列维-奇维塔、Minkowski 闵可夫斯基、Einstein 爱因斯坦、Newton 牛顿、Leibniz 莱布尼茨、Descartes 笛卡尔、Gauss 高斯、Euler 欧拉、Lagrange 拉格朗日、Laplace 拉普拉斯、Wessel 韦塞尔、Argand 阿尔冈、Warren 沃伦、Peacock 皮科克、De Morgan 德摩根、Boole 布尔、Cayley 凯莱、Clifford 克利福德、Voigt 沃伊特、Ricci 里奇、Grossmann 格罗斯曼、al-Khwārizmī 花拉子米、Ptolemy 托勒密、Euclid 欧几里得、Archimedes 阿基米德、Eudoxus 欧多克索斯、Faraday 法拉第、Armstrong 阿姆斯特朗、Carroll 卡罗尔。
  **规则**：正文首次出现写「威廉·罗恩·哈密顿（William Rowan Hamilton）」，之后只写「哈密顿」。

- [ ] **Step 3: 写 `docs/翻译风格指南.md`**，明确：
  1. 逐段翻译，不合并、不拆分、不省略；一段英文 = 一段中文。
  2. 作者第一人称 `I` 译「我」；语气保留原书的口语化与设问。
  3. 长定语从句拆为中文短句，但信息量不减。
  4. 术语首次出现「中文（English）」，人名首次出现「中文（English）」。
  5. 公式原样保留 `$…$` / `$$…$`，不改写符号；公式编号 `(1)` 保留。
  6. 交叉引用本地化：`chapter 4` → 「第 4 章」，`figure 9.3` → 「图 9.3」，`fig. 0.2` → 「图 0.2」，`chap. 2` → 「第 2 章」。
  7. 图注：`<span class="bsans">FIGURE 1.1</span>. 说明` → `![说明](images/fig1_1.jpg){width="50%"}`（编号交给 LaTeX 自动排，Markdown 里不写死「图 1.1」）。
  8. 知识框（`div.box`）：`::: {.infobox}` + 首行 `**框标题**（原文全大写标题的中文）` + `:::`。
  9. 引文（`p.extract` / `blockquote`）→ `>` 引用块。
  10. 分隔符 `p.star`（`• • •`）→ 独占一行的 `*　*　*`（Markdown 水平分隔用 `***` 会与斜体冲突，统一写 `• • •` 并由构建脚本替换为 `\asterism`）。
  11. 尾注：正文 `[^ch01n1]`，章节文件末尾集中给出 `[^ch01n1]: 译文`。
  12. 索引词条：格式 `中文词条（English）` + 页码原样保留。
  13. 禁用：机器腔、无依据的扩写、删减引文。

- [ ] **Step 4: 校验**：三份文档齐备，术语表 ≥ 30 行。

---

### Task 5: 样本章 —— 序言 + 第 1 章（确立风格基线，需人工确认）

**Files:**
- Create: `cn-book/1.序言.md`
- Create: `cn-book/2.第1章-代数的解放.md`

**Interfaces:**
- Consumes: `en/08_Prolog.md`、`en/09_Chapter01.md`、`docs/术语表.md`、`docs/译名表-人名.md`、`docs/翻译风格指南.md`
- Produces: 两份译稿 + **风格基线**（后续所有章的模板）

- [ ] **Step 1: 译 `cn-book/1.序言.md`**（6437 词）：H1 `# 序言`，结构、段数、图 0.1–0.3、尾注与 `en/` 严格对齐。

- [ ] **Step 2: 译 `cn-book/2.第1章-代数的解放.md`**（6079 词）：H1 `# 第 1 章　代数的解放`，H2 节标题、图 1.1–1.2、公式、尾注全部保留。

- [ ] **Step 3: 立即跑结构校验**（Task 8 的脚本此时应已可用；若未就绪，先手工核对段数/图数/公式数）

```bash
python3 tools/check_structure.py --only 1.序言,2.第1章-代数的解放
```
Expected: 段数、图数、尾注数三项差值均为 0，仅「字符数」允许偏离。

- [ ] **Step 4: 提交给用户确认风格**：把两章译文前 30 段贴给用户，明确请其确认「语感/术语/人名处理」后再批量开译。**用户未确认前不得进入 Task 6。**

---

### Task 6: 并行翻译 第 2–7 章

**Files:**
- Create: `cn-book/3.第2章-微积分的登场.md`
- Create: `cn-book/4.第3章-向量的构想.md`
- Create: `cn-book/5.第4章-理解空间与存储.md`
- Create: `cn-book/6.第5章-出人意料的新角色.md`
- Create: `cn-book/7.第6章-泰特与麦克斯韦.md`
- Create: `cn-book/8.第7章-从四元数到向量.md`

**Interfaces:**
- Consumes: `en/10_Chapter02.md` … `en/15_Chapter07.md` + 三份 docs + 样本章基线
- Produces: 六份中文章稿，编号与 `build_pdf.py` 的 `CHAPTERS` 列表前六项一致

- [ ] **Step 1: 派发 6 个子代理**（每章一个，并行）。每个子代理的 prompt 必须包含：源文件路径、目标文件路径、`docs/` 三份文档路径、样本章路径、以及「逐段翻译 + 段数对齐 + 公式原样 + 尾注落地」四条硬要求。
- [ ] **Step 2: 回收后逐章跑 `python3 tools/check_structure.py --only <章节>`**，差值非 0 的退回重译。
- [ ] **Step 3: 跑 `python3 tools/check_terms.py`**，术语表外的新术语补进 `docs/术语表.md` 并回写译稿。
- [ ] **Step 4: 校验**：六章段数/图数/公式数/尾注数全部对齐；无残留英文段落（`grep -c '^\s*[A-Z][a-z]\{20,\}'` 级别抽查）。

---

### Task 7: 并行翻译 第 8–13 章

**Files:**
- Create: `cn-book/9.第8章-向量分析终成正果.md`
- Create: `cn-book/10.第9章-从空间到时空.md`
- Create: `cn-book/11.第10章-弯曲空间与不变距离.md`
- Create: `cn-book/12.第11章-张量的发明.md`
- Create: `cn-book/13.第12章-万物汇聚.md`
- Create: `cn-book/14.第13章-后来发生了什么.md`

**Interfaces:** 同 Task 6；源文件 `en/16_Chapter08.md` … `en/21_Chapter13.md`。第 11 章含 39 处公式（全书最多），公式必须逐条保留。

- [ ] **Step 1: 派发 6 个子代理并行翻译**
- [ ] **Step 2: 逐章 `check_structure.py` + `check_math.py`**
- [ ] **Step 3: 合并术语新增项到 `docs/术语表.md`**
- [ ] **Step 4: 校验**：六章全部对齐；第 11 章公式数 = 39。

---

### Task 8: 结构校验工具（在 Task 5 之前就需要可用，此处固化）

**Files:**
- Create: `tools/check_structure.py`
- Create: `tools/check_terms.py`
- Create: `tools/check_math.py`

**Interfaces:**
- Consumes: `en/manifest.json`、`en/*.md`、`cn-book/*.md`、`docs/术语表.md`、`tools/mathml2tex.py`
- Produces: `review/structure.md`、`review/terms.md`、`review/math.md`；被 Task 5/6/7/9 与最终验收调用

- [ ] **Step 1: `tools/check_structure.py`** —— 对齐维度（**严重**级）：章内段数、图数、行间公式数、尾注数、节标题数；比对 `en/<stem>.md` 尾部 `<!--stats: …-->` 与译文实测值，任一不等即报 **严重**。
- [ ] **Step 2: 同上脚本** —— 软信号（**轻微**级）：字符数比（中文/英文期望 1.4–2.2）、列表项数差异（中文常拆条，仅提示）。
- [ ] **Step 3: `tools/check_terms.py`** —— 对每章扫描术语表中每个 English 词是否以约定的中文译名出现；发现同一 English 词在译文中出现 ≥2 种中文译法即报 **严重**；译文中出现术语表未收录的高频技术词（出现 ≥3 次且不在表内）即报 **中等** 并列出候选。
- [ ] **Step 4: `tools/check_math.py`** —— 统计译文 `$…$`/`$$…$$` 数量并要求与 `en/` 相同；把全部公式体抽出来写进一个临时 `.tex`，用 `xelatex -halt-on-error` 编译，**编译失败或 Missing character 即报严重**。
- [ ] **Step 5: 跑一遍全量，产出 `review/*.md`**

```bash
python3 tools/check_structure.py && python3 tools/check_terms.py && python3 tools/check_math.py
```

---

### Task 9: 后附部分 —— 结语 / 时间线 / 致谢 / 注释 / 索引

**Files:**
- Create: `cn-book/15.结语.md`
- Create: `cn-book/16.时间线.md`
- Create: `cn-book/17.致谢.md`
- Create: `cn-book/18.注释.md`
- Create: `cn-book/19.索引.md`
- Modify: `tools/check_structure.py`（跳过索引的段数硬对齐，索引按词条数对齐）

**Interfaces:**
- Consumes: `en/22_Epilog.md`、`23_Timeline.md`、`24_Acknowledgments.md`、`25_Notes.md`、`26_Index.md`
- Produces: 五份译稿；`19.索引.md` 供 Task 10 的 `build_index.py` 进一步处理

- [ ] **Step 1: 译结语**（2132 词）与**致谢**（727 词）
- [ ] **Step 2: 译时间线**（3107 词）：`p.hang_1a` → Markdown 无序列表，年代（`ca. 3000 BCE`）原样保留在句首，译后面说明。
- [ ] **Step 3: 译注释**（25625 词，353 条）：按 `h2.head2bm`（PROLOGUE / CHAPTER 1 …）分组为 `## 注释：序言`、`## 注释：第 1 章` …；每条 `[^chNNnK]:` 定义搬进对应**章节文件**末尾（当页脚注），`cn-book/18.注释.md` 保留一份**完整汇编**（便于通读与检索）。书名/期刊/论文题名保留英文原文，说明性文字译中文。
- [ ] **Step 4: 译索引**（约 3000 词条）：词条译为中文、附英文原词，**页码原样保留**（含 `365n14` 这类「页码+注释号」写法）；子项结构（`,` 与 `;` 分层）保留。
- [ ] **Step 5: 排序** —— 用系统 `sort` 做中文拼音排序（已验证 macOS `LC_ALL=zh_CN.UTF-8 sort` 对「向量/张量/哈密顿」排序正确）：

```bash
LC_ALL=zh_CN.UTF-8 sort -o /tmp/idx_sorted.txt /tmp/idx_raw.txt
```
- [ ] **Step 6: 校验**：注释 353 条一条不缺；索引词条数与 `en/` 一致（允许 ±0）。

---

### Task 10: LaTeX 排版与 PDF 构建

**Files:**
- Create: `tools/build_pdf.py`
- Create: `tools/header.tex`
- Create: `tools/infobox.lua`
- Create: `tools/build_index.py`
- Create: `dist/vector-cn.pdf`（脚本生成）

**Interfaces:**
- Consumes: `cn-book/*.md`（Task 1/5/6/7/9）、`images/`、`docs/术语表.md`
- Produces: `dist/vector-cn.pdf`、`dist/build-report.json`（供 Task 11）

- [ ] **Step 1: `tools/infobox.lua`** —— pandoc Lua filter，把 `Div` class `infobox` 转成 LaTeX 环境（pandoc 默认会丢弃该 div，已实测确认）：

```lua
function Div(el)
  if el.classes:includes('infobox') then
    return { pandoc.RawBlock('latex', '\\begin{infobox}'),
             pandoc.RawBlock('latex', '\\textbf{' .. (el.attributes.title or '') .. '}') ,
             unpack(el.content),
             pandoc.RawBlock('latex', '\\end{infobox}') }
  end
end
```

- [ ] **Step 2: `tools/header.tex`** —— 关键配置（全部实测依赖已确认可用）：

```tex
\usepackage{amsmath,amssymb}
\usepackage{unicode-math}
\setmathfont{Latin Modern Math}
\usepackage{tcolorbox}
\newenvironment{infobox}{\begin{tcolorbox}[colback=gray!5,colframe=gray!40,boxrule=0.4pt,arc=2pt]}{\end{tcolorbox}}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RE]{\nouppercase{\leftmark}}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}
% 原版页码：页边灰色小字（可用 --no-page-marks 关闭）
\newcommand{\origpage}[1]{\marginpar{\raggedleft\footnotesize\sffamily\color{gray}#1}}
\usepackage{marginnote}
\usepackage{multicol}
\usepackage{fvextra}
```

  说明：章号由 `build_pdf.py` 写入 H1，LaTeX 不再自动编号（沿用参考项目的做法，避免 ctex `\chaptermark` 取到「第零章」）；`\xeCJKsetup{CJKspace=true}` 保住中文与西文间的空格。

- [ ] **Step 3: `tools/build_pdf.py`** —— 合并与构建：
  - 章序常量：`FRONT = ["0.译本说明.md"]`，`MAIN = ["1.序言.md", "2.第1章-代数的解放.md", … "14.第13章-后来发生了什么.md"]`，`BACK = ["15.结语.md","16.时间线.md","17.致谢.md","18.注释.md","19.索引.md"]`
  - 合并时把 `<!--p123-->` 替换为 `\origpage{123}`（`--no-page-marks` 时直接删除），把 `• • •` 替换为 `\asterism`
  - 兜底：记录每个文件的「输出/输入字符比」，< 0.95 即告警（防正文被吞，沿用参考项目的经验）
  - pandoc 调用：

```bash
pandoc dist/build/book.md -o dist/vector-cn.pdf \
  --pdf-engine=xelatex --resource-path=. \
  --lua-filter=tools/infobox.lua \
  -H tools/header.tex \
  --toc --toc-depth=2 \
  -V documentclass=ctexbook -V classoption=fontset=macold \
  -V CJKmainfont="Songti SC" \
  -V papersize=a4 -V geometry:"margin=2.5cm,inner=3.3cm,marginparsep=3mm,marginparwidth=1.1cm" \
  -V fontsize=11pt -V linestretch=1.2 \
  -V title="向量：一个关于空间、时间与数学变换的惊奇故事" \
  -V subtitle="Vector: A Surprising Story of Space, Time, and Mathematical Transformation" \
  -V author="罗宾·阿里安罗德 著" \
  -V titlepage=true -V colorlinks=true
```

- [ ] **Step 4: 索引排版 `tools/build_index.py`** —— 读 `cn-book/19.索引.md`，按拼音分 A–Z 组，输出 `\begin{multicols}{2}` + `\textbf{词条}（English）` + 页码的两栏 LaTeX 片段；由 `build_pdf.py` 以 `-H` 之后的 `--include-after` 注入正文末尾。
- [ ] **Step 5: 首次构建并修错**

```bash
python3 tools/build_pdf.py --keep
```
Expected: 无 `Missing character`、无 `Undefined control sequence`；否则回到 Step 2/3 修补（多数会是数学符号缺字形或 `mfenced`/`mtable` 转出的环境缺失）。

- [ ] **Step 6: 校验**：PDF 生成成功；页数在 380–520 之间（对应约 20 万汉字 + 59 图）；目录含序言/13 章/结语/时间线/致谢/注释/索引。

---

### Task 11: PDF 基线检查（防「构建成功但内容错了」）

**Files:**
- Create: `tools/check_baseline.py`
- Create: `review/baseline.md`

**Interfaces:**
- Consumes: `dist/vector-cn.pdf`、`dist/build-report.json`、`cn-book/*.md`
- Produces: `review/baseline.md`；最终验收依据

- [ ] **Step 1: 缺字形检查** —— 解析构建日志中 `Missing character` 条数，要求 **0**。
- [ ] **Step 2: 越界裁切检查** —— 用 `pdftotext -bbox` 或 `pdfplumber`（若不可用则用 `mutool draw -F txt`）逐行取 xMax，> 版心右边界的行全部列出（参考项目中此项曾抓到 8 行被切的代码，纯字符比对发现不了）。
- [ ] **Step 3: 内容完整性** —— 从 PDF 抽取文本，与 `cn-book/*.md` 做字符差集比对，缺失字符数 > 0 即报严重（重点防省略号 `…`、箭头、重音符号等被字体替换后丢字）。
- [ ] **Step 4: 结构完整性** —— PDF 中「图 N.M」编号连续且与 `images/` 引用一致；脚注编号每章从 1 开始。
- [ ] **Step 5: 跑检查并写报告**

```bash
python3 tools/check_baseline.py
```
Expected: 严重项 0；有轻微项则在 `review/baseline.md` 记录并逐条处理。

---

### Task 12: README 与最终验收

**Files:**
- Modify: `README.md`
- Create: `review/acceptance-report.md`

- [ ] **Step 1: 补全 README** —— 原书信息（作者/出版社/原书链接）、**版权与非商业声明**、章节目录（含 13 章 + 序言/结语/时间线/注释/索引的中文标题）、构建方式（`python3 tools/extract_epub.py` → 翻译 → `python3 tools/build_pdf.py`）、工具说明、术语表链接。
- [ ] **Step 2: 全量验收**

```bash
python3 tools/check_structure.py && python3 tools/check_terms.py && python3 tools/check_math.py && python3 tools/build_pdf.py && python3 tools/check_baseline.py
```
Expected: 全部通过，严重项 0。

- [ ] **Step 3: 写 `review/acceptance-report.md`** —— 记录：字数统计（英文/中文）、各章段数对齐结果、术语表规模、PDF 页数与大小、已知遗留问题。

---

## 执行顺序与并行边界

```
Task 1 ──> Task 2 ──> Task 3 ──┐
                  └─> Task 4 ──┴──> Task 5 ──(用户确认风格)──> Task 6 ──> Task 7 ──> Task 9
                                                                                    ↓
                        Task 8（工具需在 Task 5 校验时可用）─────────────────────> Task 10 ──> Task 11 ──> Task 12
```

- Task 2 与 Task 3 可并行开发（`extract_epub.py` 只依赖 `convert()` 签名）。
- Task 8 的 `check_structure.py` **必须在 Task 5 之前可用**。
- Task 6、Task 7 内部各章可并行；两批之间串行（便于中途校准术语）。

## 已知风险

| 风险 | 应对 |
|---|---|
| MathML 转换有未覆盖标签导致公式错 | Task 3 Step 5 全量编译自检 + Step 6 抽样目视，标签全集已列明 |
| 子代理并行导致术语漂移 | 术语表为硬约束 + `check_terms.py` 每章拦截 + 分批串行校准 |
| 图片含英文文字（如 p098.jpg 整页图） | 保留原图，在图注下补一行中文说明（`(图中文字为原文)`） |
| 缺字形（如 〈〉、⟨bra-ket⟩、⦵） | `check_baseline.py` Step 1 强制为 0，逐个用 `newunicodechar` 兜 |
| PDF 里公式溢出 | `check_baseline.py` Step 2 逐行测 xMax |
