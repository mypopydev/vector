# 第五轮复核 · 交叉引用语义指向（范围 A：序言 ～ 第 6 章）

生成于 2026-09-28。只做研究，未改动任何 `cn-book/`、`docs/` 文件。

## 覆盖证据

**已核对 23 处** —— 覆盖 `4.序言.md`、`5.第1章`～`10.第6章` 全部「第 N 章」与「见尾注 N」引用：

| 项 | 数量 |
|---|---|
| 「第 N 章」引用（含章标题行之外的正文+尾注） | 22 |
| 「见尾注 N」引用 | 1 |
| 合计 | **23** |

其中：**书内互引 18 处**（17 处章引用 + 1 处尾注引用）、**引用他书 5 处**。

**结论：未发现「指向错」「指代不清」「原书如此」三类缺陷（0 条）。** 18 处书内互引的指向全部正确，且都能在 `en/` 找到同一指向（同章同注），即原书如此、译文忠实。5 处「引用他书」非缺陷，单列于第二节。

> 说明：下表中 严重度 `—`、类型「指向正确」表示该处经核对无缺陷（不属于四个缺陷类型）；仅「引用他书」项使用题面给定的类型名。

---

## 一、书内互引逐条核对（18 处，全部指向正确）

| 文件 | 行号 | 严重度 | 类型 | 中文引用 | 该指向处的实际内容 | 英文原文对应 | 建议 |
|---|---|---|---|---|---|---|---|
| 4.序言.md | 59 | — | 指向正确 | 「翻到后面第 3 章的图 3.4」 | `7.第3章:118` 图 3.4 正是 sinθ/cosθ 与毕氏定理的单位圆图 | `en/08_Prolog.md:57` "(…look ahead to fig. 3.4 in chap. 3.)" | 无需改动 |
| 4.序言.md | 144 | — | 指向正确 | 「我们将在第 2 章遇到的、原始微积分的穷竭法」 | `6.第2章:39` 讲"穷竭法（method of exhaustion）"与阿基米德 | `en/25_Notes.md:17`（ch00n6）"…method of exhaustion that we'll meet in chap. 2" | 无需改动 |
| 4.序言.md | 151 | — | 指向正确 | 「不可交换性，我们将在第 1 章和第 4 章看到」 | `5.第1章:9` 讲打破交换律；`8.第4章:71-79、126` 讲不可交换/反交换 | `en/25_Notes.md:26`（ch00n9）"…noncommutativity, which we'll see in chaps. 1 and 4" | 无需改动 |
| 5.第1章 | 9 | — | 指向正确 | 「我们要到第 4 章才正式认识它（右手定则）」 | `8.第4章:124` 图 4.1「叉积的右手定则」；`:126` 由它导出不可交换 | `en/09_Chapter01.md:9` "…we'll meet it properly in chapter 4…" | 无需改动 |
| 5.第1章 | 192 | — | 指向正确 | 「或第 3 章的图 3.4、图 3.6 及相关讨论」 | `7.第3章:118` 图 3.4；`:152` 图 3.6（阿尔冈平面/复平面） | `en/25_Notes.md:84`（ch01n20）"…figs. 3.4 and 3.6 and related discussion in chap. 3" | 无需改动 |
| 6.第2章 | 69 | — | 指向正确 | 「也可以用二重积分…（我们在第 6 章会简短地遇到它）」 | `10.第6章:46` 正文出现"二重积分"；尾注 ch06n8 `:266` 再提 | `en/10_Chapter02.md:73` "…with a double integral (which we'll meet briefly in chap. 6)." | 无需改动 |
| 6.第2章 | 170 | — | 指向正确 | 「正如我在上一则尾注，即尾注 15 中所例示的」 | 本章尾注 15（`6.第2章:216`）用现代符号演示牛顿几何微积分，含代数推演 | `en/10_Chapter02.md:178` "…in the previous endnote, i.e. no. 15." | 无需改动 |
| 6.第2章 | 187 | — | 指向正确 | 「麦克斯韦最终会给出答案（第 6 章）」（光波中什么在起伏） | `10.第6章:191-196` 麦克斯韦的电磁波理论统一电、磁与光 | `en/25_Notes.md:92`（ch02n1）"…Maxwell would eventually provide the answer (chap. 6)." | 无需改动 |
| 7.第3章 | 73 | — | 指向正确 | 「邦贝利的 $2+11\sqrt{-1}$——我们在第 1 章也遇到过它」 | `5.第1章:114` 正是邦贝利与 $2+11\sqrt{-1}$ 的推导 | `en/11_Chapter03.md:77` "…which we also met in chapter 1." | 无需改动 |
| 7.第3章 | 116 | — | 指向正确 | 「求第 1 章提到过的复数的平方根、立方根…」 | `5.第1章:134、192`（尾注 ch01n20）讲复数的三个立方根 | `en/11_Chapter03.md:120` "…roots of complex numbers mentioned in chapter 1." | 无需改动 |
| 7.第3章 | 187 | — | 指向正确 | 「在第 2 章里，我提到过莱布尼茨那些富有暗示性的微分 $dx,dy$…」 | `6.第2章:167、170` 对比莱布尼茨记号与牛顿点记号 | `en/11_Chapter03.md:191` "In chapter 2, I mentioned the power of the suggestive Leibnizian differentials…" | 无需改动 |
| 8.第4章 | 101 | — | 指向正确 | 「从哈密顿的向量到现代向量…那场充满火药味的过渡，是第 8 章的故事」 | `12.第8章:2、107-118` 标题即"四元数之'战'"，亥维赛/吉布斯转向现代向量分析 | `en/12_Chapter04.md:101` "…the surprisingly acrimonious transition…is a story for chapter 8…" | 无需改动 |
| 8.第4章 | 349 | — | 指向正确 | 「（四元数积中 $p\cdot q$ 前的负号引起争议）我们将在第 7 章看到」 | `11.第7章:63` 明确讲哈密顿标量积与现代标量积"唯一的差别就是前面那个负号" | `en/25_Notes.md:280`（ch04n14）"…which will prove controversial, as we'll see in chap. 7." | 无需改动 |
| 9.第5章 | 7 | — | 指向正确 | 「哈密顿关于锥形折射的数学预言（我们在第 2 章见过）」 | `6.第2章:4、16、18` 详述锥形折射预言与劳埃德的实验证实 | `en/13_Chapter05.md:7` "…conical refraction (which we saw in chap. 2)…" | 无需改动 |
| 9.第5章 | 62 | — | 指向正确 | 「我们将在第 10 章看到，高斯还开创了如今所谓'微分几何'」 | `14.第10章:25、36` 小节"弯曲曲面的数学：卡尔·弗里德里希·高斯"，讲度规/微分几何 | `en/13_Chapter05.md:62` "…as we'll see in chapter 10, Gauss also initiated…'differential geometry.'" | 无需改动 |
| 9.第5章 | 77 | — | 指向正确 | 「在第 3 章里，我提到过牛顿在用模与方向两者来表达物理量方面的开创作用」 | `7.第3章:9、16` 牛顿把力/速度/动量定义为"同时具有方向和模" | `en/13_Chapter05.md:77` "In chapter 3, I mentioned Newton's pioneering role…both magnitude and direction…" | 无需改动 |
| 10.第6章 | 91 | — | 指向正确 | 「正如我在第 2 章讲 $\frac{d}{dx}$ 时提到过的（'算子'）」 | `6.第2章:167` $\frac{d}{dx}$ "是一个作用在函数 $y(x)$ 上的算子（operator）" | `en/14_Chapter06.md:103` "As I mentioned in chapter 2 in connection with $\frac{d}{dx}$…operator…" | 无需改动 |

---

## 二、引用他书（非缺陷，5 处）

以下「第 N 章」指的是**别的书的章节**（见括号内书名），不是本书章节，回查方向正确、不构成译文缺陷：

| 文件 | 行号 | 严重度 | 类型 | 中文引用 | 该指向处的实际内容 | 英文原文对应 | 建议 |
|---|---|---|---|---|---|---|---|
| 5.第1章 | 184 | — | 引用他书 | 「见他的 *Ars Magna* 第 12 章」 | 指卡尔达诺（Cardano）本人著作《大衍术》第 12 章 | `en/25_Notes.md:75`（ch01n16）"…in chap. 12 of his *Ars Magna*…" | 保留；非本书章节 |
| 8.第4章 | 326 | — | 引用他书 | 「MacFarlane, *Lectures on Ten British Mathematicians*…第 3 章」 | 指 MacFarlane 1916 年那本书的第 3 章 | `en/25_Notes.md:236`（ch04n6）"…*Lectures on Ten British Mathematicians*…chap. 3…" | 保留；非本书章节 |
| 9.第5章 | 123 | — | 引用他书 | 「Crowe, *History of Vector Analysis*…第 3 章」 | 指 Crowe 1967 年那本书的第 3 章 | `en/25_Notes.md:401`（ch05n3）"…Crowe, *History of Vector Analysis*…chap. 3…" | 保留；非本书章节 |
| 9.第5章 | 147 | — | 引用他书 | 「Assis and Chaib, *Ampère's Electrodynamics* (Apeiron, 2015), 第 14 章、16.4 节及结论，491」 | 指 Apeiron 版《Ampère's Electrodynamics》第 14 章 | `en/25_Notes.md:428`（ch05n14）"…*Ampère's Electrodynamics* (Apeiron, 2015), chaps. 14, 16.4, and conclusion, 491…" | 保留；即第四轮已识别的 Apeiron 案例 |
| 9.第5章 | 159 | — | 引用他书 | 「Crowe, *History of Vector Analysis*, 77，第 4 章」 | 指 Crowe 那本书第 4 章（页 77） | `en/25_Notes.md:443`（ch05n19）"…(*History of Vector Analysis*, 77, chap. 4)…" | 保留；非本书章节 |

---

## 三、核对方法与结论

- **方法**：对每处引用，① 用 `grep` 到被引章节确认"此处确实讲了该主题"（人物名/概念名为关键词，不要求字面复述）；② 回 `en/` 找到对应句，核对英文引的是同一章/同一注；③ 甄别是否指他书。
- **章号映射核验**：`cn-book` 第 1～6 章与 `en/09_Chapter01`～`14_Chapter06` 标题逐一对齐，无错位（`4.序言` 对应 `08_Prolog`）。
- **结果**：
  - 指向错：**0**
  - 指代不清：**0**
  - 原书如此（原书自身指向可疑）：**0**
  - 引用他书（非缺陷）：**5**
  - 书内互引指向全部正确：**18 / 18**
