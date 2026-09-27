# 第四轮逐句复核　区段 A（序言 + 第 1–3 章）

## 覆盖范围

| 中文文件 | 英文文件 | 英文句数 | 中文句数 |
|---|---|---|---|
| `cn-book/4.序言.md` | `en/08_Prolog.md` | 207 | 247 |
| `cn-book/5.第1章-代数的解放.md` | `en/09_Chapter01.md` | 181 | 262 |
| `cn-book/6.第2章-微积分的登场.md` | `en/10_Chapter02.md` | 282 | 355 |
| `cn-book/7.第3章-向量的构想.md` | `en/11_Chapter03.md` | 285 | 373 |
| **合计** | | **955** | **1237** |

方法：逐段取英/中双段，按 `。！？` 切句后**句对句**配对（英文一句常对应中文一到两句），每句分别核「信息是否完整／意思是否准确／是否精炼」。

**本轮未发现「严重」级问题**（无意思错误、无信息漏译、无数字或专名错误）。第 1 章几乎全清，问题集中在序言。
已核对归一约定：`vector`→向量（四章无「矢量」、无「数量积」残留）；维度→二维/三维/四维；`impetus`→冲力、`modulus`→模、`couple`→数偶、`ordered pair`→有序对、`triple`→三元组、`fluxion`→流数、`sizar`→减费生 均已落地；引号均为弯引号，无「」。
本轮**未改动**任何 `cn-book/`、`docs/` 文件。

---

## 一、中等（9 条）

| 文件 | 行号 | 严重度 | 类型 | 英文原句 | 中文现译 | 建议改法（具体到字词） |
|---|---|---|---|---|---|---|
| `cn-book/4.序言.md` | 4 | 中等 | 用词 | “…especially now that AI has become so **sophisticated**.” | “尤其是当人工智能已经变得如此**精密**的当下。” | 「精密」多用于仪器/机械，形容 AI 不妥。改为「如此先进」或「如此高明」。 |
| `cn-book/4.序言.md` | 52 | 中等 | 语序 | “In **the earliest of these advanced Mesopotamian societies**, the estimates of field sizes…” | “在**这些先进的最早期美索不达米亚社会**里，让经济正常运转所需的田地面积估算…” | 定语顺序颠倒，易读成「先进的最早期社会」。改为「在这些发达的美索不达米亚社会中最早的那些里」。 |
| `cn-book/4.序言.md` | 67 | 中等 | 漏译 | “**Most** cultures from this time did not leave written records of their astronomical observations…” | “这一时期的**许多**文化没有留下天文观测的书面记录…” | 限定词被弱化：「Most」→「许多」，丢了「大多数」这一分寸。改为「这一时期的**大多数**文化」。 |
| `cn-book/4.序言.md` | 71 | 中等 | 插入语隔断定语 | “…it is Ptolemy who introduced the idea of **latitude and longitude** that we use today for locating places on Earth.” | “把经纬度引入——也就是我们今天用来确定地球表面位置的那套东西——的功劳属于托勒密。” | 破折号把「把……引入的功劳」这个定语拦腰截断，「的」悬空。改为「把经纬度（也就是我们今天用来确定地球表面位置的那套坐标）引入的功劳属于托勒密」——只把破折号换成括号，不动字词。 |
| `cn-book/4.序言.md` | 107 | 中等 | 插入语隔断定语 | “…the axis of **the magnetic orientation, or “spin,” of an electron** can be “up” or “down”…” | “**电子磁取向——即“自旋（spin）”——的轴**可以是“上”或“下”…” | 同上：破折号把「电子的磁取向……的轴」隔断。改为「**电子的磁取向（即“自旋”）的轴**可以是“上”或“下”」。 |
| `cn-book/5.第1章-代数的解放.md` | 56 | 中等 | 歧义 | “…he was too busy sailing the high seas, **dodging heretic hunters**, and…” | “而他忙于远航公海、**躲避搜捕异端者**，并且——首要的是——” | 「躲避搜捕异端者」可顺读成「躲避（去）搜捕异端者」，方向反了。改为「躲避那些追捕异端的人」。 |
| `cn-book/6.第2章-微积分的登场.md` | 34 | 中等 | 插入语隔断定语 | “The resulting area computation gives a surprisingly good approximation for **the constant we now call π**…” | “由此得到的面积计算，给出了**我们今天称为 π 的那个常数的、好得出奇的近似值**…” | 「的、好得出奇的」两个「的」打架，中心词被挤开。改为「……给出了**我们今天称为 π 的那个常数的一个好得出奇的近似值**」。 |
| `cn-book/6.第2章-微积分的登场.md` | 170 | 中等 | 误译 | “…he didn’t want to **make too much of** the new calculus with its disappearing differentials…” | “因而不想让这门新微积分——带着它那些会消失的微分……—**招来太多注意**。” | 「make too much of」＝对之大做文章／太过倚重，不是「引人注意」。改为「因而不想对这门新微积分大做文章」。 |
| `cn-book/7.第3章-向量的构想.md` | 85 | 中等 | 漏译（分寸词） | “…and to **inadvertently** open the way for the discovery of vectors.” | “……并**顺带**为向量的发现打开了通路。” | 「inadvertently」＝无意中／意外地；「顺带」＝incidentally，语义不同。改为「并**无意中**为向量的发现打开了通路」。 |

---

## 二、中等待定夺（1 条，涉原文疑漏字）

| 文件 | 行号 | 严重度 | 类型 | 英文原句 | 中文现译 | 建议 |
|---|---|---|---|---|---|---|
| `cn-book/6.第2章-微积分的登场.md` | 139 | 中等 | 数字（增译） | “it is proportional to the product of their masses and **inversely proportional to the distance** between them.” | “它与两者质量的乘积成正比，**与它们之间的距离的平方成反比**。” | 原文只写「与距离成反比」，但紧接的公式是 $F=\frac{GmM}{r^{2}}$，原文此处疑漏 “square”。**建议保留现译的「平方」**（否则与紧随的公式自相矛盾），并补一句译者注：「原文作“与距离成反比”，据紧随之公式应为距离之平方，译文据公式补正。——译者注」 |

---

## 三、中等｜引文断句（1 条）

| 文件 | 行号 | 严重度 | 类型 | 英文原句 | 中文现译 | 建议改法 |
|---|---|---|---|---|---|---|
| `cn-book/7.第3章-向量的构想.md` | 189 | 中等 | 引文断句 | “…the way we mark time and space is the means ‘**by which thoughts become things, and spirit puts on body, and the act and passion of mind are clothed with an outward existence, and we behold ourselves from afar**.’” | “我们标记时间与空间的方式，正是“**思想借以变成事物、精神借以穿上肉体、心灵的活动与激情借以披上外在存在**”的那种手段，“**我们由此得以从远处观看我们自己**”。” | 原文是一整句引文，现译切成两段引号，后半段「我们由此得以从远处观看我们自己」被甩出引号后无法挂靠（既非「手段」的同位语，也非并列成分）。改为并入同一引号：「……正是“思想借以变成事物、精神借以穿上肉体、心灵的活动与激情借以披上外在存在，**我们由此得以从远处观看我们自己**”的那种手段。」 |

---

## 四、轻微（11 条）

| 文件 | 行号 | 严重度 | 类型 | 英文原句 | 中文现译 | 建议改法 |
|---|---|---|---|---|---|---|
| `cn-book/4.序言.md` | 4 | 轻微 | 增译 | “a spectacular breakthrough in **our understanding of the world**” | “**我们认识世界的方式**就会出现一次惊人的突破。” | 原文无「方式」。改为「我们对世界的认识就会出现一次惊人的突破」。 |
| `cn-book/4.序言.md` | 4 | 轻微 | 指代 | “which led to wireless technology and **its** wondrous transformation of our everyday lives” | “**它**带来了无线技术，并奇妙地重塑了我们的日常生活。” | 「its」指无线技术，现译「它」回指「发现」。改为「它带来了无线技术，**而无线技术又**奇妙地重塑了我们的日常生活」。 |
| `cn-book/4.序言.md` | 38 | 轻微 | 翻译腔 | “It’s necessarily selective and **subjective**.” | “它必然是有选择的，**也带着我的主观**。” | 「带着我的主观」缺中心语。改为「也必然是**主观的**」或「也带着我的**主观色彩**」。 |
| `cn-book/4.序言.md` | 67 | 轻微 | 冗余 | “…records were **arithmetical rather than trigonometrical**…” | “埃及与美索不达米亚的天文记录似乎是**属于算术性的，而非三角学性的**…” | 删「是属于」，改为「似乎是算术性的，而非三角学性的」。 |
| `cn-book/4.序言.md` | 69 | 轻微 | 增译 | “…the **earliest** sophisticated record not just of mathematical astronomy…” | “……不仅是**现存最早**的数理天文学的精密记录…” | 原文此处无 “surviving”（57 行才有 extant）。建议删「现存」。 |
| `cn-book/4.序言.md` | 112 | 轻微 | 增译 | “**The shapes** produced in these “vector files” do “carry” lines from point to point along the shape…” | “**不过**，这些“向量文件”所产生的形状确实沿着图形把线从一个点“带”到另一个点……” | 原文此处无转折连词。删句首「不过」。 |
| `cn-book/6.第2章-微积分的登场.md` | 96 | 轻微 | 增译 | “…it came **as close to her farm as the nearby village**.” | “它最近时已经逼近到邻近的村庄，**离她的农庄只有一步之遥**。” | 「只有一步之遥」为原文所无（原文只说战火逼近到「邻近村庄那么近」）。删后半句，或改为「最近时已经逼近到邻近的村庄那么近」。 |
| `cn-book/6.第2章-微积分的登场.md` | 98 | 轻微 | 误译 | “…the radiant hope of **human** progress” | “……视之为**人道**进步之光辉希望的哲学家。” | 「human progress」应为「人类进步」，「人道」偏指 humanitarian。改「人道」为「人类」。 |
| `cn-book/7.第3章-向量的构想.md` | 20 | 轻微 | 误译 | “there *was* a practical notion of **simple** addition” | “*确实*存在一种实用的、**朴素**的加法概念” | 「simple」＝简单，非「朴素」。改为「实用的、**简单**的加法概念」。 |
| `cn-book/7.第3章-向量的构想.md` | 38（并见脚注 n3，同文件第 236 行） | 轻微 | 术语不统一 | “…such “**vituperative** and cruel” work.” | 正文：“**谩骂**而残忍的”工作；脚注 n3 小标题：*“**辱骂性**的”著作* | 同一引文两处译名不一。统一为「辱骂（性）的」（正文改作『“辱骂而残忍的”工作』）。 |
| `cn-book/7.第3章-向量的构想.md` | 55 | 轻微 | 翻译腔 | “*Proving* it’s a parabola, **with a distinctive equation of the form** *y* = −*ax*^**2**^ + *bx* + *c*, is another matter.” | “……并写出 *y* = −*ax*^**2**^ + *bx* + *c* **这种形式那个特有的方程**，则是另一回事。” | 「这种形式那个特有的方程」别扭。改为「并给出 *y* = −*ax*^**2**^ + *bx* + *c* 这样一条特征方程」。 |

---

## 统计

| 严重度 | 条数 |
|---|---|
| 严重 | **0** |
| 中等（含 1 条待定夺、1 条引文断句） | **11** |
| 轻微 | **11** |
| 合计 | **22** |

按章分布：

| 章 | 中等 | 轻微 | 小计 |
|---|---|---|---|
| 序言 | 5 | 6 | 11 |
| 第 1 章 | 1 | 0 | 1 |
| 第 2 章 | 3（含 1 待定夺） | 2 | 5 |
| 第 3 章 | 2（含 1 引文断句） | 3 | 5 |

按类型分布：增译 5、误译/用词 4、插入语隔断定语 3、漏译（含量词弱化与分寸词）3、语序 1、冗余 1、引文断句 1、术语不统一 1、数字（待定夺）1、歧义 1、翻译腔 2。

## 术语表建议

- 本区段**未发现需补表的新术语**；已有译名（向量、标量、模、冲力、数偶、有序对、三元组、有向线段、反证法、链式法则、算子、旋转体、二分点岁差、象限仪、减费生、流数）均按表落地。
- 建议核查一处跨章一致性：`vituperative` 在第 3 章正文译「谩骂」、脚注译「辱骂」，已在正文列出；若全书另有出现，请一并统一。
