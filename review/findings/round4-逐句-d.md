# 第四轮逐句精读复核 · 区段 d

## 覆盖范围

| 中文文件 | 英文文件 | 说明 |
|---|---|---|
| `cn-book/14.第10章-弯曲的空间与不变的距离.md` | `en/18_Chapter10.md` | p217–239 |
| `cn-book/15.第11章-张量的发明.md` | `en/19_Chapter11.md` | p240–273 |
| `cn-book/16.第12章-万物汇聚.md` | `en/20_Chapter12.md` | p274–303 |
| `cn-book/17.第13章-后来发生了什么.md` | `en/21_Chapter13.md` | p304–319 |

**方法**：逐段取英文段与中文段，按 `。！？` 与 `.!?` 切句后句对句配对（含一对多），每句核「信息完整／意思准确／是否精炼」。正文（含图注、知识框、引文块）约 **1,110 个英文句**逐句核过；脚注为当页副本，未重复计数。

**已逐句确认无误的高风险项**（故未列入下表）：`rank/order` 在 ch11 L46 图注、L297、L316 中的处理正确；`contraction`→缩并 与 `length contraction`→长度收缩 未混；`scalar product`→标量积 全书一致；第 12 章优先权之争的全部史实与日期（1915-11-25／11-20 提交、12-06 印刷厂戳、12-02 发表、1920 年代、1990 年代后期、Leo Corry／特拉维夫大学、43 角秒、18 角秒、1500 万美元、1919-11-07／11-10 两家报纸）逐句核对一致；`maybe/seemingly/perhaps/presumably/apparently/probably/almost certainly/as far as I can tell` 等分寸词全部保留。

---

## 中等（5 条）

| 文件 | 行号 | 严重度 | 类型 | 英文原句 | 中文现译 | 建议改法 |
|---|---|---|---|---|---|---|
| `cn-book/14.第10章…md` | 167 | 中等 | 误译 | “Gauss was a good person to have on your side, and he thought Riemann was a true mathematician ‘of a gloriously fertile originality.’” | “高斯是那种值得你站在他一边的人，而他认为黎曼是一位‘有着光辉丰饶之独创性’的真正数学家。” | 原文是「有高斯站在你这边是好事」，现译把方向反了。改「值得你站在他一边」为「值得倚仗」（即：高斯是那种有他相助便大不一样的人）。其余不动。 |
| `cn-book/15.第11章…md` | 132 | 中等 | 术语 | “Rank 2 tensors can be represented as matrices… A rank 3 tensor, such as a 2 × 3 × 5 array, has shape [2, 3, 5]” | “二阶张量可以表示为矩阵……一个三阶张量，比如一个 2 × 3 × 5 的数组，形状是 [2, 3, 5]” | 术语表 rank→秩、order→阶，且本章 L316 已用「二秩」。改「二阶张量」为「二秩张量」、「一个三阶张量」为「一个三秩张量」。同段上一句「是它的秩和‘形状’」保留不动，正好与之呼应。 |
| `cn-book/15.第11章…md` | 284 | 中等 | 术语 | “modern mathematicians define ‘whole tensors’ as *linear operators* that yield invariants” | “现代数学家……而是把‘完整的张量’定义为产生不变量的*线性算子*。” | 术语表 `whole vector`→整体向量，第 12 章 L118「whole-tensor labels」亦译「整体张量」。改「完整的张量」为「整体张量」。 |
| `cn-book/15.第11章…md` | 319 | 中等 | 术语 | “*T*~μν~*h*^**λσ**^ is a general component of a rank 4 (4-index) tensor” | “*T*~μν~*h*^**λσ**^ 是一个四阶（四指标）张量的一般分量” | 同上，rank→秩。改「四阶（四指标）」为「四秩（四指标）」。紧邻的上一节 L316「把秩（或者说阶）降到了 0」保留，正好形成对照。 |
| `cn-book/15.第11章…md` | 365 | 中等 | 术语 | “the transformation equation of *g*~μν~ must be that of a covariant rank 2 tensor” | “那么 *g*~μν~ 的变换方程就必须是协变二阶张量的变换方程。” | 改「协变二阶张量」为「协变二秩张量」（注意同章注 [^ch11n19] 里 EN 写的是 second-order，译「二阶张量」是正确的，不要一起改）。 |

## 轻微（8 条）

| 文件 | 行号 | 严重度 | 类型 | 英文原句 | 中文现译 | 建议改法 |
|---|---|---|---|---|---|---|
| `cn-book/14.第10章…md` | 102 | 轻微 | 误译 | “he had even shown how to find the area of cylindrical segments of the sphere” | “甚至还说明了怎样求球面上那些圆柱形部分的面积” | 「球面上……圆柱形部分」易读成「球上呈圆柱形的一块」，而原文指与圆柱相对应的那段球面。建议改为「球面上那些（与圆柱段对应的）截段的面积」。 |
| `cn-book/14.第10章…md` | 18 | 轻微 | 专名 | “the absolute differential calculus of Ricci and Levi-Civita”（第 11 章：“Ricci’s family name was Ricci Curbastro”） | 第 10 章 L18「格雷戈里奥·里奇-库尔巴斯特罗（Gregorio Ricci-Curbastro）」；第 11 章 L7「里奇·库尔巴斯特罗（Ricci Curbastro）」 | 同一姓氏两种连写（连字符／间隔号）。建议统一为一种（推荐「里奇-库尔巴斯特罗」），只改第 11 章那一处即可。 |
| `cn-book/15.第11章…md` | 4 | 轻微 | 术语 | “She seemed to act as a counselor, hearing the women’s troubles and offering comfort.” | “她似乎担当着一种劝导者的角色，倾听她们诉说苦处，并给予安慰。” | 「劝导者」偏“劝诫”，原文 counselor 重在倾听、出主意并安慰。改「劝导者」为「疏导者」或「顾问」。 |
| `cn-book/15.第11章…md` | 74 | 轻微 | 指代不清 | “But this is no different from the vector representation of ‘Mice love cats,’ which is definitely not the case.” | “但这与‘Mice love cats（老鼠爱猫）’的向量表示并没有区别，而这显然是不对的。” | 「这显然是不对的」可能被读成「Mice love cats 这句话不对」，原文指「两者无区别」不成立。改「而这显然是不对的」为「而这显然不该如此」。 |
| `cn-book/16.第12章…md` | 56 | 轻微 | 翻译腔 | “As Einstein told his old friend Michele Besso, a fellow graduate from the Swiss Polytechnic and his longtime insightful sounding-board” | “贝索同样是瑞士联邦工艺学校的毕业生，也是他长期以来的、富有洞见的共鸣板” | 「共鸣板」是 sounding-board 的硬译，中文读者不易会意。建议改「共鸣板」为「倾诉对象」，或在「共鸣板」后加「（倾诉对象）」。 |
| `cn-book/16.第12章…md` | 90 | 轻微 | 冗余 | “material objects and light photons must travel on *curved geodesics*” | “物体和光的光子必定沿*弯曲的测地线*运动” | 「光的光子」叠床架屋。改「物体和光的光子」为「物体与光子」。 |
| `cn-book/16.第12章…md` | 143 | 轻微 | 术语 | “but if the whole tensor is zero (or nonzero) in one frame, it is zero (or nonzero) in all of them” | “但如果整个张量在某一个参照系中为零（或不为零），那么它在所有参照系中都为零（或不为零）。” | 与术语表「整体向量」及第 12 章 L118「整体张量」统一：改「整个张量」为「整体张量」。（此处「整个」与「分量」对举，属技术用法。） |
| `cn-book/17.第13章…md` | 39 | 轻微 | 含混 | “Since it doesn’t matter which value of *x* is used, *V* must be independent of *x*. Which means ∂V/∂x [= 0], and this, in turn, means that …” | “既然用哪一个 *x* 值都无所谓，*V* 就必定与 *x* 无关。这意味着 $\frac{\partial V}{\partial x}$，而这又意味着” | 中文「这意味着 ∂V/∂x」句子悬空，读者不知道意味着什么。建议补两字：「这意味着 $\frac{\partial V}{\partial x}$ 为零」。（原文排印脱了「= 0」，补出即为原意，不算增译。） |

---

## 存疑（非译文问题，不建议改动）

- `cn-book/15.第11章…md` L166：「里奇正是听从他的建议，才去柏林跟随克莱因学习的」——英文作 “Ricci had gone to Berlin to study with Klein”。但同一章 L14 说克莱因「当时常驻慕尼黑」、里奇 1878 年秋「抵达慕尼黑」。**这是英文原书自身的年代／地点不一致**，中文忠实照译，不应改动；如需处理，建议加译者注而非改正文。

## 统计

| 项 | 数量 |
|---|---|
| 核过的英文句数（正文，4 章合计） | ≈ 1,110 |
| 严重（意思错／信息漏／数字或专名错） | **0** |
| 中等（意思对但别扭／术语不统一／指代不明） | **5** |
| 轻微（可更精炼） | **8** |
| 合计 | 13 |
| 存疑（原文问题） | 1 |

## 术语表建议

1. `docs/术语表.md` 增补 **whole tensor → 整体张量**（与既有 `whole vector → 整体向量` 对齐）；当前第 11、12 章出现「完整的张量」「整体张量」「整个张量」三种写法。
2. `rank / order (of a tensor) → 秩 / 阶` 一条已存在且正确，但第 11 章有 3 处把 EN 的 `rank` 译成了「阶」（L132 两处、L319、L365），与同章 L277「无论秩是多少」、L316「混合二秩」冲突；建议按表回填，并顺带核对第 12–13 章是否有同类漂移（本区段内其余各处均已核对无误）。
