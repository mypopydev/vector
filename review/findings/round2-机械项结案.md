# 机械项结案（第二轮）

核验对象：`review/terms.md` 的 18 条「中等」项（check_terms.py 输出：严重 0、中等 18）。

方法：对每一条，先从 `docs/术语表.md` 取规定译名，再用 `grep -n` 在 `en/<章>.md` 定位该英文词的**全部**出现（出现次数已逐条与 terms.md 的计数核对一致），然后到 `cn-book/<章>.md` 对应位置取译文片段，判断该处词义是否为术语表规定的那一个。

说明：出现次数按 `en/` 原文统计（check_terms.py 的计数口径）；表中「cn 行号」为译文所在行。本轮未改动任何 `cn-book/`、`docs/`、`tools/` 文件。

## 一、术语校验 18 项中等

| # | 章 | 英文词 | 表定译名 | 该词在本章的实际用法（行号 + 片段） | 结论 | 处理 |
|---|---|---|---|---|---|---|
| 1 | 4.序言 | power | 幂（乘方） | en 08_Prolog L9「this awesome power」、L11「the physical power of vectors and tensors」、L18「the power of vector language」、L29×2「their power」「their practical power」、L36「the full power of these mathematical ideas」、L44「the economic and administrative power」。cn 4.序言 L9「这种惊人力量的一个来源」、L11「物理威力」、L18「向量语言威力」、L29「它们的威力」「实际威力」、L36「全部威力」、L44「经济与行政权力」。7 处无一为数学的「幂」 | 误报 | 无需改动 |
| 2 | 6.第2章-微积分的登场 | power | 幂 | en 10_Chapter02 L96「an exceptional intellectual or creative power」、L113「the special power of symbolic thinking」、L132「the remarkable power of being able to represent…」。cn L88「创造力量」、L105「符号思维的特殊力量」、L124「非凡威力」 | 误报 | 无需改动 |
| 3 | 6.第2章-微积分的登场 | translation | 平移 | en 10_Chapter02 L164 四处同段，均指迪沙特莱翻译《原理》：「her translation of *Principia* from Latin to French」「the first such translation into an everyday language」「the original English translation」「du Châtelet's translation」。cn L156「把《*Principia*》从拉丁文译成了法文」「最初的英译本」「埃米莉·迪沙特莱的译本」。无一处为几何「平移」 | 误报 | 无需改动 |
| 4 | 7.第3章-向量的构想 | power | 幂 | en 11_Chapter03 L33 是《牛津英语词典》对 force 的释义「power; exerted strength or impetus」、L144「massive computer power」、L191「the power of the suggestive Leibnizian differentials *dx, dy*」。cn L29「力量；施加出的力气或冲力」、L140「庞大的计算机能力」、L187「所具有的力量」 | 误报 | 无需改动 |
| 5 | 8.第4章-理解空间与存储 | curl | 旋度 | en 12_Chapter04 L124×2、L126 三处均为**动词**：「curl the fingers of your right hand」「turn your right hand upside down to curl your fingers clockwise」「when you curl your fingers in the direction from vector *p* to vector *q*」（右手定则）。cn L124「把右手的手指顺着…方向弯曲」「让手指顺时针弯曲」、L126「把手指顺着…方向弯曲」。无一处为向量分析的「旋度」 | 误报 | 无需改动 |
| 6 | 8.第4章-理解空间与存储 | couple | 二元组 / 数偶 | en 12_Chapter04 L7「multiplying by a complex 'couple' of real numbers (*x, y*)」为术语义；L35「for a couple of years between 1840 and 1842」、L310「a couple of months after…」为数量义。cn L7 已作「用一个由实数组成的复数“二元组（couple）”(*x, y*)」、L35「在 1840 年至 1842 年之间的几年里」、L310「几个月」。术语义已落地 | 误报 | 校验器缺陷：规定译名含「 / 」时做整串字面匹配，永不可能命中（详见第二节第 1 条） |
| 7 | 8.第4章-理解空间与存储 | telegraphy | 电报术 | en 12_Chapter04 L165「the brand-new invention of electromagnetic telegraphy」、L199「uniting the world via telegraphy」、L278「the basis of the first telegraphy systems」——三处**都是**术语表所定义的术语义（电报技术），不是别的词义。cn 却一律作「电报」：L161「用电磁电报这一崭新发明来协调列车运行」、L187「通过电报把世界连成一体」、L266「最早的电报系统的基础」。同书另有第三种译法：cn 12.第8章 L107「关于电报学以及相关的实用电磁理论的众多论文」（en 16_Chapter08 L119「papers on telegraphy」），而 10.第6章 L102 与 22.索引 L148 用「电报术」。同一英文词在全书出现「电报 / 电报术 / 电报学」三种译法 | **真问题** | 见第三节「待你定夺的改动」 |
| 8 | 9.第5章-出人意料的新角色与缓慢的接受 | power | 幂 | en 13_Chapter05 L4「disclaimed the power of setting any limit」、L18「believed in the power of his new method」、L32「the power of algebra and calculus in physics」、L77「the power of symbols」。cn L4「我可没有本事给犯错误的本领设下任何界限」、L18「相信自己的新方法能简化计算」、L32「代数与微积分在物理学中的威力」、L77「符号的力量」 | 误报 | 无需改动 |
| 9 | 10.第6章-泰特与麦克斯韦 | action | 作用量 | en 14_Chapter06 L139×3、L153、L180、L185 六处全在「action-at-a-distance」这一固定短语里（L139 另有「all the action happened at the two points」）。cn L127×3、L141、L168、L173 一律作「超距作用」。无一处为变分原理的「作用量」 | 误报 | 无需改动 |
| 10 | 11.第7章-从四元数到向量 | power | 幂 | en 15_Chapter07 L28「the power of nabla」、L38「the power of Hamilton's nabla operator」、L40 小节标题「THE POWER OF NAMES」、L42「The great power of mathematics」、L111 小节标题「THE POWER OF WHOLE VECTORS」、L115「helping power the Industrial Revolution」（动词）、L127「the power of the mathematical 'vector field'」、L192「earthly power」。cn L28「纳布拉算子威力」、L38「∇ 的威力」、L40「## 名字的威力」、L42「巨大威力」、L111「## 整体向量的威力」、L115「帮助为工业革命提供了动力」、L127「的威力」、L192「世俗的权力」 | 误报 | 无需改动 |
| 11 | 12.第8章-向量分析终成正果 | power | 幂 | en 16_Chapter08 L160「appreciation of the power of quaternion analysis」、L173「a man of 'genuine power and originality'」、L175「the simplicity and power of the vectorial approach」。cn L148「四元数分析的威力」、L161「真正的力量与原创性」、L163「简洁与威力」 | 误报 | 无需改动 |
| 12 | 13.第9章-从空间到时空 | contraction | 缩并 | en 17_Chapter09 L79「Such a physical 'length contraction'」、L87「the necessary 'length contraction' to support the ether hypothesis」、L90「'length contraction' in special relativity」、L171「Lorentz's 'length contraction' was a real physical effect」、L226「a literal, physical contraction of moving objects」。cn L79「物理上的“长度收缩（length contraction）”」、L87、L90、L159「长度收缩」、L206「物理收缩」。全为相对论的长度收缩义 | 误报 | 符合项目既定口径（相对论＝长度收缩，张量语境＝缩并；「缩并」在 15.第11章、16.第12章、17.第13章、21.注释 均有正确使用） |
| 13 | 14.第10章-弯曲的空间与不变的距离 | work | 功 | en 18_Chapter10 12 处全为「工作／研究／推导」义：L13「relished the chance to work once again with his old classmate」、L18「Riemann's work on curved surfaces」、L22「built on Riemann's work」、L29「Gauss's work on a related problem」、L111「during his own work on mapmaking」、L141「the work of Gauss's students」、L155「understand the work of…Riemann」、L161「adapt Gauss's work on curved 2-D space」、L234「Riemann's working doesn't show it」、L256「Riemann's pioneering work on curvature」、L259「Christoffel published his work in 1869」、L268「seized upon Riemann's work」。cn 对应：L13「再次与老同学共事」、L18/22/29/95/121/135/141/232/235/244「…的工作」、L223「黎曼的推导」。无一处为物理学的「功」 | 误报 | 无需改动 |
| 14 | 17.第13章-后来发生了什么 | tangent | 切线 | en 21_Chapter13 L145「a vector tangent to the side *AC*」、L147×2「the pencil is tangent to the ball at *A*」「keeping it tangent」、L156「a curve with tangent vector *U***」。cn L121「从一条与边 *AC* 相切的向量出发」、L123×2「铅笔在 *A* 点与球相切」「始终让它与球面相切」、L132「以 ***U*** 为切向量」。四处均为形容词／定语用法，无一处指「切线」这条线本身 | 误报 | 术语表缺「相切」「切向量」两个义项，建议补（见第二节第 3 条） |
| 15 | 21.注释 | natural philosophy | 自然哲学 | en 25_Notes L110、L142 为书名 *Mathematics, Exploration, and Natural Philosophy in Early Modern England*；L574、L578 为论文题名 “Thomson and Tait: The Treatise on Natural Philosophy”。cn L58、L75、L264、L266 均保留英文原题 | 误报 | 依《译本说明》「注释中的书名、期刊名与论文题名保留英文原文，说明性文字译为中文」，此处保留原文是正确的。正文中该词已正确译出（6.第2章 L139「自然哲学（natural philosophy）」、22.索引 L636） |
| 16 | 21.注释 | Philosophical Transactions | 《哲学汇刊》 | en 25_Notes L506、L508、L671、L811 四处全为期刊名 *Philosophical Transactions of the Royal Society (A / London)*，均为文献引注。cn L239、L240、L315、L376 保留英文原刊名 | 误报 | 同上（注释保留原文）。正文中该刊名已正确使用《哲学汇刊》：10.第6章 L177、15.第11章 L166、22.索引 L622 |
| 17 | 22.索引 | power | 幂 | en 26_Index L414「power of names and」、L479 同、L578×2「computational power of」「power of」、L610「power of」。cn L261、L459「名称的力量与它」、L540「它的力量」、L618×2「它的计算能力」「它的力量」 | 误报 | 无需改动 |
| 18 | 22.索引 | action | 作用量 | en 26_Index L7「action-at-a-distance」、L171 同、L366「action-at-a-distance vs. fields」。cn L110「超距作用（action-at-a-distance）」、L152「超距作用与它」、L612「超距作用与场之争」 | 误报 | 无需改动 |

## 二、结论

- **真问题 1 条**：#7（`telegraphy`，8.第4章）。
- **误报 17 条**：#1–6、#8–18。
- 因此 `review/acceptance-report.md` 第 54 行「中等 18 项已逐条核验，全部是多义词误报」这一断言**需要修正**：17 条确为误报，但 #7 并非多义词误报——该词三处都是术语义，问题在于译名与全书不统一。

### 对 check_terms.py 判据的调整建议（按优先级）

1. **多候选译名必须拆开匹配（结构性缺陷，必改）**。术语表 474 条中有 48 条的中文侧含「 / 」（如 `couple → 二元组 / 数偶`、`telegrapher / telegraphy → 电报员 / 电报术`、`tangent plane / tangent space → 切平面 / 切空间`）。当前代码 `if cn not in cn_text` 是把整串「二元组 / 数偶」当字面量找，永远不可能命中 → 这类条目 **只要英文出现 ≥3 次就必然误报**。建议按「 / 」切分成候选列表，任一候选命中即视为已落地。#6 正是被这条判据触发的。
2. **区分「多义词」与「真未落地」**。本轮 17 条误报里，只有 #6 是判据缺陷，其余 16 条都是同一个根因：英文词高频多义（power 7 章、work、action、translation、curl、contraction、tangent），校验器只看「英文出现次数 ≥3 且译文中没有规定译名」，无法判义。建议在术语表加一列「义项／豁免标记」（例如 power 标 `多义：幂｜能力`），命中时降级为「提示」而不是「中等」，可让中等项从 18 降到 1–2 条，噪声基本消失。
3. **术语表自身需消歧**：`tangent` 在 L97 规定「切线」，而 L121 `sine / cosine / tangent` 又规定「正切」，两者冲突；且缺「相切（形容词）」「切向量」两个实际使用的义项。`power`、`work`、`action`、`translation`、`curl`、`contraction` 同样建议按义项分行。
4. **注释章应区别对待**。`cn-book/21.注释.md` 里的书名／刊名／论文题名按《译本说明》一律保留英文原文，术语校验在这类章节上必然误报（#15、#16）。建议对 `21.注释.md` 跳过术语校验，或只对说明性文字跑。
5. **判据输出加一列「该词在本章的中译集合」**。本轮为判定 18 条，全部靠人工 `grep` 找出每处译法再逐处比对。若校验器在报错时顺带列出该章该英文词对应的中文译法分布，人工一眼即可定性，可大幅降低复核成本。

### 附：与本节无关但顺带确认的一项

用户提到的 `scalar product` 口径已核实无误：全书 `数量积` 已清零（仅 docs 术语表 L147 作为「亦称」保留），正文统一用「标量积」（11.第7章 9 处、21.注释 9 处、13.第9章 8 处等）。本轮 terms.md 中不含 scalar 项，无需处理。

## 三、待你定夺的改动（#7 telegraphy，我不擅自修改）

同一英文词 `telegraphy` 在全书有三种译法：8.第4章作「电报」、12.第8章作「电报学」、10.第6章与索引作「电报术」。两个收敛方向，请选一个：

**方案 A（以术语表为准，改译文）**
- `cn-book/8.第4章-理解空间与存储.md` L161：「用电磁电报这一崭新发明来协调列车运行」→「用电磁电报术这一崭新发明来协调列车运行」
- `cn-book/8.第4章-理解空间与存储.md` L187：「通过电报把世界连成一体」→「通过电报术把世界连成一体」
- `cn-book/8.第4章-理解空间与存储.md` L266：「最早的电报系统的基础」**建议保留**（此处 telegraphy 作定语，「电报系统」是正确中文；「电报术系统」不通）
- `cn-book/12.第8章-向量分析终成正果.md` L107：「关于电报学以及相关的实用电磁理论的众多论文」→「关于电报术以及相关的实用电磁理论的众多论文」

**方案 B（放宽术语表，改表不改文）**
- `docs/术语表.md` L370：`| telegraphy | 电报术 |` → `| telegraphy | 电报术（作定语时用「电报」） |`，并按上述第 1 条让校验器接受多候选；同时把 12.第8章 L107 的「电报学」改掉，保留 8.第4章三处现状。

我倾向 **方案 A 的半程版**：保留 L266「电报系统」，改 L161、L187 为「电报术」，并把 12.第8章 L107「电报学」统一为「电报术」；同时在术语表注明「作定语时用『电报』」，这样既满足术语表又不制造拗口的中文。
