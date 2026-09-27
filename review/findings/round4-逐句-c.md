# 第四轮逐句精读（区段 c）：第 7–9 章

## 覆盖范围与方法

- `cn-book/11.第7章-从四元数到向量.md` ↔ `en/15_Chapter07.md`
- `cn-book/12.第8章-向量分析终成正果.md` ↔ `en/16_Chapter08.md`
- `cn-book/13.第9章-从空间到时空.md` ↔ `en/17_Chapter09.md`

按 `。！？` 切句后**句对句**核对，共约 360 组句对（第 7 章约 110、第 8 章约 120、第 9 章约 130，含 fig 9.3 知识框整段逐句核）。每句过三问：信息是否完整、意思是否准确、是否精炼。

**不在本次范围**：各章末尾的 `[^chNNnN]` 脚注正文（`cn-book` 中它是 `21.注释-*.md` 的副本，另有批次覆盖）、公式本体、`<!--pNNN-->` 标记。
行号均为 **cn-book 文件行号**。

## 已逐句确认无误的重灾区术语（记录备查，不需改）

- `whole vector(s)` → 「整体向量」全书一致（第 7 章 L26/L65/L91/L109/L111、第 8 章 L9/L71/L83/L98、第 9 章 L173/L248 等均正确）。
- `scalar product` → 「标量积」一致（第 7 章 L9/L47/L63/L91、第 8 章 L31/L111/L121、第 9 章 L15/L20/L36/L210/L214/L223）。
- `length contraction` → 「长度收缩」（第 9 章 L79/L90/L159），未误作「缩并」；本区段正文无张量语境的 `contraction`。
- `rank`／`order` 仅在 `cn-book/13` 脚注 ch09n27 出现：「反对称的二阶（second-rank 或 second-order）张量，其中「秩」（rank）或「阶」（order）指其分量上指标的数目」——**秩/阶分工正确，勿动**。
- 图注开头的 `FIGURE N.N.` 全书统一不译出（fig 7.1/7.2/8.1/9.1/9.2/9.4/9.5 一致），属既有约定，非漏译。

## 意见（按严重度排序）

### 中等

| 文件 | 行号 | 类型 | 英文原句 | 中文现译 | 建议改法 |
|---|---|---|---|---|---|
| 11.第7章 | 94 | 误译（结构错位） | with his wicked wit he made great fun of endless “British Ass” discussions among “our witless nobs.” | 他把“英国蠢驴（British Ass，谐“英国科学促进会”）”之间没完没了的讨论大加取笑，说那是“我们那些没脑子的阔佬” | 被取笑的是**阔佬之间**的“英国蠢驴”讨论，不是“蠢驴之间”。改：他大加取笑“我们那些没脑子的阔佬”之间没完没了的“英国蠢驴”讨论 |
| 11.第7章 | 123 | 误译 | “Tait is the man to enable him to do it by thinking, a nobler though more expensive occupation…” | ……这是一种更高贵、也更费力的消遣 | `occupation`＝从事的事／活计，不是“消遣（pastime）”；`expensive`＝代价高。改：这是一种更高贵、也更费心力的事 |
| 11.第7章 | 139 | 指代不清 | …the secular university where De Morgan had taught, in protest at the Anglican vows needed for a position at Oxford and Cambridge. | 那所世俗的大学正是德摩根任教的地方，他之所以去那里，是为了抗议在牛津和剑桥任职所需的安立甘宗宣誓。 | 紧邻主语是克利福德，“他”易被读成克利福德；抗议者是德摩根。改：……德摩根当年之所以到那里任教，是为了抗议…… |
| 11.第7章 | 19 | 翻译腔 | their friend Maxwell—“a rising star of the first magnitude,” as Thomson put it | 用汤姆森的说法，他是“一等星等的一颗新星” | `of the first magnitude` 是“一流／最上乘”的天文比喻，不是“星等”术语。改：一颗一等的新星（或：一颗光芒夺目的新星） |
| 12.第8章 | 131 | 翻译腔／歧义 | So Gibbs seems rather ungenerous in denying public credit where it was due. | 所以，吉布斯在该给公众的承认上显得相当吝啬。 | 现译可误读为“公众给他的承认”。改：在抹杀本应给予他人的公开致谢这一点上，吉布斯显得相当吝啬 |
| 13.第9章 | 44 | 术语 | the coordinate-free, **invariant** way of writing equations that he championed | 他所倡导的那种无坐标的、不变量的写方程方式 | `invariant` 是形容词“不变的”，非名词“不变量”。改：无坐标的、不变的写方程方式 |
| 13.第9章 | 67 | 翻译腔 | her extensive study at the Poly made her, at the very least, a worthy and important sounding board for him | ……至少使她成为他一个称职而重要的共鸣板 | `sounding board`＝试想法的倾听者／商讨对象。改：至少使他有了一个称职而重要的商讨对象（sounding board，字面“共鸣板”） |

### 轻微

| 文件 | 行号 | 类型 | 英文原句 | 中文现译 | 建议改法 |
|---|---|---|---|---|---|
| 11.第7章 | 94 | 术语 | Cayley had developed the mathematics of “scrolls” or “skew surfaces”—like the twisted ruled surfaces… | 关于“卷筒（scroll）”或“直纹曲面（skew surface）”的数学……那种扭曲的直纹面 | skew surface（不可展直纹面／斜曲面）与后文 ruled surface（直纹面）在中文里撞名。改：“斜曲面（不可展直纹面）” |
| 11.第7章 | 169 | 增译 | the Italian mathematician Giuseppe Peano would **also discover** Grassmann’s *Ausdehnungslehre* | ……也会重新发现格拉斯曼的《扩张论》 | 原文无“重新”。改：也会发现（若确要表达“重新发现”，宜加注说明） |
| 11.第7章 | 192 | 增译（可选保留） | his “better ½” agreed to it | 他的“更好的 ½”（指他的妻子）同意了这件事 | 释义为译者所加。可保留，但更稳的是移到脚注或删去括注 |
| 12.第8章 | 83 | 漏译（限定语） | Maxwell had, in fact, reduced his twenty component equations to **just** five whole-vector ones | 麦克斯韦……其实已经把他的二十条分量方程归结成了五条整体向量方程 | 补 `just`：归结成了仅仅五条 |
| 12.第8章 | 161 | 误译（语气） | proved perfect clickbait—**to use a pointed anachronism**—for a cover story in *Nature* | ……完美点击诱饵（clickbait）——请原谅这个有意的时代错置—— | `pointed`＝尖锐／有意为之，无致歉义。改：——这里是有意用一个时代错置的说法—— |
| 12.第8章 | 155 | 冗余 | to assume an **easy** path from Maxwell to Einstein and from vectors to tensors | 并假定……有一条平坦的坦途 | “平坦的”与“坦途”重复。改：一条顺理成章的坦途 |
| 13.第9章 | 67 | 漏字／别扭 | she would have gotten her diploma and the doctorate she was planning | 她本会拿到她的文凭和她所计划的那博士学位 | 补量词并顺语序：她计划中的那个博士学位 |
| 13.第9章 | 146 | 冗余 | …and **associativity** (of the group “product”—in this case, the composition of two transformations) are the other key features. | 结合性（群“乘积”——在这里即两个变换的复合——的结合性）是另外两个关键特征 | 括注内重复“结合性”。改：结合性（指群“乘积”——这里是两个变换的复合——满足结合律） |

## 统计

| 项 | 数 |
|---|---|
| 核对句对 | 约 360 |
| 严重 | 0 |
| 中等 | 7 |
| 轻微 | 8 |
| 合计 | 15 |

## 需定夺的全局问题

1. **“better ½”式的译者括注**（第 7 章 L192）：全书对双关（`positive`、`pot`/`sin`）已有“（译者注：…）”先例，括注释义属同一风格，建议统一保留而非逐条删除。
2. **`discover` 是否可译“重新发现”**（第 7 章 L169）：格拉斯曼长期被忽视，Peano 属再度发现，语义上成立；但严格对照属增译。是否统一按原文只译“发现”，需你定调。
3. 图注 `FIGURE N.N.` 不译出已确认为全书约定，本轮未报为漏译。
