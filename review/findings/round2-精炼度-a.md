# 精炼度候选甄别（A 组：译本说明／作者简介／序言／第 1–7 章）

**覆盖证据**：本组覆盖 `0.译本说明.md`、`1.名家推荐.md`、`2.作者简介.md`、`4.序言.md`、`5.第1章`–`11.第7章` 共 11 个文件；`tools/check_style.py --top 100000` 全量候选 232 条中，落在本组的有 **124 条**（conj 63、pronoun 35、的_density 18、nominalize 6、longsent 2；`1.名家推荐.md` 无候选）。逐条回英文原文（08_Prolog / 09_Chapter01 … 15_Chapter07）复核后：

> **已甄别 124 条，判为作者风格 115 条（不改），判为翻译腔 9 条（如下）。**

**甄别口径**（供其他组沿用）：

1. **「之所以…是因为」是固定一组，不算两个连接词**。本组 63 条 conj 中有 15 条属于此类，英文只是单个 `because / for / That's why`，中文照译，不改。
2. **conj 型绝大多数是作者原句的复刻**：英文同句里本就有 `so … for`、`although … because`、`since … so` 的连叠，中文一一对应（如序言 52「然而…因为」＝"however … because"；第 6 章 384「因为…所以…因为」＝"because … so … since"）。不改。
3. **pronoun 型多为作者的排比／回指修辞**：第 2 章 91 的「他是一位…／他是一位…」、第 7 章 230 的「它更简单…／它更通透…」、第 6 章 191 的「他一举统一…／他甚至指出…」在英文里同样是 `He … He …`、`It's … And it's …`。不改。
4. **的_density 型多数是术语搭配**：「…的分量」「…的系数」「向量的三个分量」属数学术语，按硬约束不动；只有夹带「所…的／…所在的」这类名词化填充的才报。
5. **名词化正则有两类系统性误报**：「被视为理所当然」（第 4 章 296，英文 "taken for granted"）、「进行表示和计算」（序言 114，英文 "do both the representing and the calculating"），均为等值译法，不改。

---

## 判为翻译腔（可改）9 条

| 文件 | 行号 | 类型 | 现译（片段） | 英文原文片段 | 建议改法 |
|---|---|---|---|---|---|
| 8.第4章-理解空间与存储.md | 189 | nominalize | 不过，耐人寻味的是，**凯莱当初寻找矩阵代数规则的动机**，只不过是为了**更高效地进行计算**：就像在古代一样… | Still, it is telling that **Cayley had been motivated to find the rules of matrix algebra** simply **to carry out computations** more efficiently… | ① 删「**的动机**」3 字 →「凯莱当初寻找矩阵代数规则，只不过是为了…」（英文是动词 `had been motivated to find`，中文不必名词化）；② 「进行计算」删「**进行**」2 字 →「更高效地计算」。共删 5 字，句式与英文一致 |
| 6.第2章-微积分的登场.md | 128 | pronoun | **他**觉得好奇，就要求上一课。 | **Intrigued, he'd** asked for a lesson. | 删句首「**他**」1 字 →「觉得好奇，他就要求上一课。」英文用分词短语避开了第四个 he；中文前三句已是「他是…／他最终…／他之所以…」，第四句再以「他」开头实属可省 |
| 10.第6章-泰特与麦克斯韦.md | 41 | pronoun | ［你的表弟乔治］凌晨两点走进我的房间……**他**看到了由快车送来的星期六《泰晤士报》，而我在早饭前收到了你的信。 | [Your cousin George] came into my room at 2 am … **having seen** the Saturday *Times*, received by express train, and I got your letter before breakfast. | 引号内删「**他**」1 字 →「……看到由快车送来的星期六《泰晤士报》」。前一句以「**他的父亲**」开头，此处句首「他」易被误读为父亲；英文用 `having seen` 承前主语，中文同样承「表弟乔治」即可 |
| 11.第7章-从四元数到向量.md | 4 | conj（含名词化） | 哈密顿确实得到了承认，却没有因为**他在这段故事里所扮演的角色**而真正被感谢 | Hamilton did receive recognition but no real thanks for **his part in the story** | 删「**所扮演的**」4 字 →「他在这段故事里的角色」。英文只一个 part，中文「所扮演的」是无来源的名词化填充 |
| 5.第1章-代数的解放.md | 47 | nominalize | 而它在欧洲**被译成拉丁语之后所产生**的重要影响之一，是推广了印度-阿拉伯的十进制记数法 | and one of its important impacts in Europe, **when it was translated into Latin**, was the popularisation of the Hindu-Arabic decimal system | 只删「**所**」1 字 →「被译成拉丁语之后产生的重要影响之一」。「被…所…」是脚本点名的被动套话，去掉「所」句式不变、语义不变 |
| 8.第4章-理解空间与存储.md | 98 | nominalize | 这些基量据说*张成（span）*了**进行计算所在的**\*向量空间（vector space）\* | these basis quantities are said to *span* the **vector space in which the calculations take place** | 删「**所在**」2 字 →「进行计算的向量空间」。「所在的」是中文自己长出来的关系标记，英文无对应 |
| 0.译本说明.md | 23 | 的_density | 本译本的页码与原版不同，而**书末索引的页码沿用的是原版页码**，因此保留原版页码以便读者按索引回查原文。 | （译者自撰，无英文原文） | 删「**的页码**」与「**的是**」共 5 字 →「而书末索引沿用原版页码」。一句内「原版页码」出现三次，删后语义不丢 |
| 5.第1章-代数的解放.md | 77 | 的_density | **正如这段漫长的历史所显示的**，符号地思考是一项非凡的技能。 | It is a singular skill to think symbolically, **as this long history shows**. | 「所显示的」→「**所示**」（删「的」「显示」换「示」，实减 2 字）→「正如这段漫长历史所示」。英文是主句 + as 从句，不是名词化主语 |
| 7.第3章-向量的构想.md | 248 | 的_density | 加上**由大球的动量（按我们的说法）所传递的**额外运动的垂直分量 *df*(=*gb*) | plus the perpendicular component *df*(=*gb*) of the extra motion **imparted by** the momentum of the large ball (in our terms) | 删「**所**」，「传递的」→「**传递来的**」→「由大球的动量…传递来的额外运动」。去「由…所…」套话，其余不动（「垂直分量」「额外运动」是术语搭配） |

---

## 附：本组判为「作者风格（不改）」的集中说明

- **序言 13、29、49、52、69、76、93、114、123**：英文同句含 `Yet … for`、`not only because … but also because`、`however … because`、`because … since` 等连叠，中文一一照译。
- **第 1 章 9、35、44、107、111、134、140**：`but … for`、`So … although`、`because`、`for` 的等值对译；134 的「然而…因为」对应 "however … by discovering"。
- **第 2 章 11、18、119、126、148、167**：`But … so`、`So … and … for`、`though … so`、`although … because` 原文即如此；25 的长句是英文原文的长列举句。
- **第 3 章 31、38、50、55、58、131、138、210、218**：`though … so`、`So … fearing`、`so … because`、`because`、`so … although`。
- **第 4 章 25、79、86、98、138、156、261、270、275、374、381、384**：含 `not because … but because`、`so … because`、`because … since` 等；384 更是英文原文就三个连接词连叠。
- **第 5 章 29、87**：`because`、`because … that`。
- **第 6 章 8、44、79、110、138、170、179、184、189、213、268**：`So … and for`、`but … for`、`because`、`for … since`、`although … for`、`If … since … so`；49 的长句与 268 的脚注长句原文同样长。
- **第 7 章 12、33、87**：`Yet despite … for`、`but … because`、`but … so`。
- **pronoun 型**（第 1 章 4、80、84、87；第 2 章 82、91、96、158；第 3 章 11、46、207；第 4 章 25、40、121、151、201、259；第 6 章 16、79、191、230；第 7 章 143）：前后两句同指一人／一物，无指代不清；且多数在英文里是同样的 `He … He …`／`It … It` 排比。
- **的_density 型**（第 2 章 45、65、165；第 4 章 21、55、101；第 5 章 43；第 6 章 20、65、70、159；第 7 章 84、152）：「的」多来自术语修饰（分量、系数、通量、面积分、编号…），按硬约束不动。
