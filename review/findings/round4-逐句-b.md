# 第四轮 逐句精读复核（B 组：第 4—6 章）

覆盖范围与口径：

- 文件：`cn-book/8.第4章-理解空间与存储.md` ↔ `en/12_Chapter04.md`；`cn-book/9.第5章-出人意料的新角色与缓慢的接受.md` ↔ `en/13_Chapter05.md`；`cn-book/10.第6章-泰特与麦克斯韦.md` ↔ `en/14_Chapter06.md`。
- **逐句核对约 894 个英文句子**（第 4 章 376、第 5 章 183、第 6 章 335，含图注），中文一侧按句号拆开的一对多小句全部逐条看过。段落层面已确认 **69 / 29 / 54 段一一对应，无跳段、无漏段、无整句丢失**（脚本比对：中文句数少于英文的段落仅 1 处，经查是 `S. PQ`、`V. PQ` 里的句点干扰计数，实无漏译）。
- 结果：**严重 1 条、中等 2 条、轻微 9 条，共 12 条**。
- 分寸词专项：对 perhaps / seemingly / apparently / presumably / barely / almost / somewhat / rather / just about / might have / I suspect 等做了逐一回查，除下面 L151/L161 的 barely 外，全部在中文里有对应（"也许""显然""大概""几乎""稍稍""仅仅""不过""我猜"等）。
- 尾注说明：三章的尾注正文在 `cn-book/` 章末是副本，正本在 `21.注释-*.md`、英文源在 `en/25_Notes.md`。本轮对 ch04–ch06 尾注做了通读比对（含 ch04n11 的模律推导、ch06n8 的面积分、ch06n21 的高斯定律微分形式），**未见句级错误**，故不单列；下表只收正文（含图注）问题。

## 待改清单

| 文件 | 行号 | 严重度 | 类型 | 英文原句 | 中文现译 | 建议改法 |
|---|---|---|---|---|---|---|
| 8.第4章 | 32 | 严重 | 数字 / 漏译（限定语） | “…which Jane Austen had highlighted in her novels **just a decade or two earlier**.” | ……而简·奥斯汀早在**几十年前**就在她的小说里凸显过这种礼仪 | 改「早在几十年前」→「**仅仅在一二十年前**」：EN 是 *a decade or two*（一二十年），且带 *just*（才、仅仅）这一分寸词；"几十年前"把时间推早了一代，也把 just 变成了反倒强调时间久的"早在" |
| 8.第4章 | 32 | 轻微 | 漏译 | “So, **with each passing decade** the stories became more and more exaggerated…” | 于是，**随着时间推移**，这些故事被传得越来越离谱…… | 补回递进："随着**每过去一个十年**"（原句强调的是"每过十年就更夸张一层"的累加，不是泛泛的"随着时间推移"） |
| 8.第4章 | 94 | 轻微 | 残留未译 | `*P* = *w* + ***p***, **where** ***p*** = *ix* + *jy* + *kz*.` | 整行原样保留 `where` | `where` →「**其中**」（第 11、15、17 章的同类 displayeq 里已有中文连词如"或者""以及"，此处体例不一致）。仅改这一个词，其余字符不动 |
| 8.第4章 | 98 | 轻微 | 误译 / 翻译腔 | “these basis quantities **are said to** *span* the *vector space*…” | 这些基量**据说***张成（span）*了进行计算的*向量空间（vector space）* | 「据说」→「**被称为**」：数学英语里 "X is said to V" 是术语定义句式（称为/叫作），不是"据别人说" |
| 8.第4章 | 109 | 轻微 | 残留未译 | `*Q* = *a* + *ib* + *jc* + *kd* (**or** *a* + *bi* + *cj* + *dk*) = *a* + ***q***.` | 整行原样保留 `(or …)` | `(or …)` →「**（或 …）**」，与第 94 行一并改；公式符号不动 |
| 8.第4章 | 126 | 轻微 | 翻译腔 / 语序 | “he wrote *S. PQ* **for** the ‘scalar part’ (our scalar product), and *V. PQ* **for** the ‘vector part’” | 而是**把 *S. PQ* 写成**"标量部分"（也就是我们的标量积），**把 *V. PQ* 写成**"向量部分"（也就是我们的向量积） | 介词方向反了：EN 是"用 S.PQ 表示标量部分"。改「他用 *S. PQ* **表示**"标量部分"（即我们的标量积），用 *V. PQ* **表示**"向量部分"（即我们的向量积）」 |
| 8.第4章 | 131 | 轻微 | 漏译（强调） | “This noncommutative vector multiplication was a **Very Big Deal** in the world of abstract algebra” | 这种不可交换的向量乘法，在抽象代数的世界里是**一件大事** | 作者用了首字母大写表强调，中文宜加重：改为「是一件\*了不起的大事\*」或「是件\*天大的事\*」，不要退回平淡的"一件大事" |
| 8.第4章 | 151 / 161 | 轻微 | 漏译（限定语） | 151: “**barely** a year after Hamilton had first announced…”；161: “had been built **barely** a decade earlier” | 151: ……距离……**仅仅一年多一点**；161: ……建成**不过十年多一点** | 两处 *barely*（差一点不到 / 勉强）都被译成了"……多一点"，方向相反。改 151「**不到一年**」、161「**才不过十年**」；若顾虑史实（1843-11→1845 实为一年余），至少把"多一点"去掉，写作「仅仅一年」 |
| 8.第4章 | 167 | 轻微 | 漏译（限定语） | “New England’s philosophical and literary back-to-nature movement—**a kind of loose** parallel to the English Romantic poets…” | 那是新英格兰一场哲学与文学上的回归自然运动，**大致平行于**哈密顿所交往的那些英国浪漫主义诗人 | 补回 loose/kind of 的分寸：改「与……**只有一种松散的平行关系**」（原文自谦地说只是"一种松散的相似"，不是断言平行） |
| 8.第4章 | 201 | 轻微 | 误译（比喻） | “for Hamilton had opened the algebraic **floodgates**” | 因为哈密顿已经**打开了代数的大门** | floodgates 是"洪水闸门"，喻指新代数成批涌出；"大门"把比喻磨平了。改「**打开了代数的闸门**」（若担心读者不解，可加"洪水般的闸门"，但勿扩写成解释句） |
| 8.第4章 | 287 | 轻微 | 术语 | “images are captured when the **radio source** is turned off and the spins return to their equilibrium state” | 当**射电源**被关掉、自旋回到它们的平衡状态时，图像就被捕捉下来 | 「射电源」是天文学专有名词（radio source，指射电天体）。此处指 MRI 的射频发射源，改「**射频源**」或「**无线电波源**」，与同段已用的"无线电波""射频脉冲"一致 |
| 10.第6章 | 13 / 39 / 41 / 76 | 中等 | 术语 | 13: “graduating as the **Senior Wrangler** of 1852”“one of the highest scoring **wranglers**”；39: “these **wranglers**”；41: “graduate as **Second Wrangler**”；76: “graduated from Cambridge as **Fourth Wrangler**” | 13: 以 **Senior Wrangler（数学荣誉学位考试第一名）** 身份毕业 / **wrangler（优胜者）**；39: 这些 **wrangler**；41: 以 **Second Wrangler（第二名）** 的成绩毕业；76: 以 **Fourth Wrangler（第四名）** 的成绩从剑桥毕业 | 与术语表（第一名优胜者 / 第二名优胜者 / 优胜者）、第 7 章（"第二名优胜者（Second Wrangler）"）及索引（"第一名优胜者（Senior Wrangler）""第四名优胜者"）三处都不一致。统一为**中文译名在前**：13 行「第一名优胜者（Senior Wrangler）」「优胜者（wrangler）」、39 行「这些优胜者」、41 行「第二名优胜者（Second Wrangler）」、76 行「第四名优胜者（Fourth Wrangler）」 |
| 10.第6章 | 20 | 中等 | 术语 | “he expressed his frustration in a long poem, ‘**A Vision of a Wrangler**.’” | 他用一首长诗表达了他的挫败感：《一个 **Wrangler** 的幻象》 | 索引（22.索引.md:572）已作「《一个优胜者的幻象》」，正文此处却留英文。改《一个**优胜者**的幻象》，与索引、术语表一致（第 6 章末尾注 ch06n4 里的英文全名照旧保留不译） |

## 附：判为正常、不改（供复核时知悉）

- **8.第4章:129（EN:129）**：叉积笑话里的 `scaler`／`scalar` 谐音双关，中文保留英文原词并加了标注"译者注"的脚注式说明，符合风格指南 §3（确需补充者放括号并标"译者注"），判正常。
- **8.第4章:9（EN:9）图注**："why Hamilton is never smiling" 译为"为什么**照片上的**哈密顿从来不笑"，增二字属必要的显化，非增译。
- **10.第6章:22–36（EN:22–36）麦克斯韦诗节**："dull November's / Fogs had stamped my torpid members" 中文拆为"正可说明十一月的阴沉／雾气如何压上我迟钝的肢体"，把 dull 从定语转成名词，属诗行内的语序调整，语义未失，判正常。
- **10.第6章:236（EN:236）**：势的分量式里的小写 `∂v/∂y`（EN 原文即为小写 v，疑为原书排印错误），中文按"公式原样搬运"照抄，未擅改，**判正常且不应改**。
- **9.第5章**：全章 29 段逐句核过，未发现需改项；限定语（seemingly undaunted、perhaps、apparently、Presumably、hardly、somewhat）均已落地。
