# 精炼度候选甄别（B 组：第 8–13 章 + 结语 / 时间线 / 致谢 / 注释）

## 覆盖证据

- 输入：`review/findings/round2-精炼度候选.md`（全书 232 条）。
- 本组负责文件：`12.第8章`、`13.第9章`、`14.第10章`、`15.第11章`、`16.第12章`、`17.第13章`、`18.结语`、`19.时间线`、`20.致谢`、`21.注释`。
- **已甄别 108 条**（其中 `12.第8章` L109 nominalize 与 `15.第11章` L58 conj 各在同一行重复命中一次，去重后 **106 处**）。
- **判为作者风格 96 处（不改）**：逐一回英文原文核对，英文原句本身就是长句／多层嵌套／带插入语与破折号／本身就连用 because–so–for–though，中文只是照译；或「的」来自「…的分量／…的系数／…的张量」这类术语搭配。
- **判为翻译腔 10 处（如下）**：其中 6 处建议改（表一），4 处仅删一个「所」字、改不改都不伤文意（表二）。
- 时间线（第 19 章）本轮无候选；注释、致谢按条目式／名录式文本放宽处理，未报可改项。
- 未改动任何 `cn-book/`、`docs/` 文件；所有建议均为「删哪几个字／换哪个词」级别，不动限定语（maybe / seemingly / arguably / apparently 之类）与整段结构。

## 表一：建议改（6 处）

| 文件 | 行号 | 类型 | 现译（片段） | 英文原文片段 | 建议改法 |
|---|---|---|---|---|---|
| 15.第11章-张量的发明.md | 189 | 的_density | 他着手的方式，是把坐标变换起作用的方式加以推广。 | “He began by generalising the way coordinate transformations work.” | 删「的方式，是」「把」「加以」三处，并把「起作用的」换为「作用」→「他从推广坐标变换的作用方式着手。」（原句「他着手的方式…方式加以推广」两个「方式」+「加以」，英文只一个 way + 动词 generalising） |
| 17.第13章-后来发生了什么.md | 16 | nominalize | 当 *L* 和 *H* 用动能与势能表达出来时，积分被极小化后所得到的那个运动方程，其解就给出通常的能量守恒方程。 | “when *L* and *H* are expressed in terms of kinetic and potential energy, the equation of motion arising when the integral is minimised has a solution that gives the usual conservation of energy equation.” | 「积分被极小化后所得到的那个运动方程」→「极小化积分后得到的那个运动方程」（删「被」与「所」二字；英文是主动分词 arising，无双重被动标记） |
| 18.结语.md | 48 | nominalize | 这些先驱中有许多人仅仅是被求知与理解的愿望所驱动，或者是被追随一个耐人寻味的模式或证明时那种颤栗般的兴奋所驱动。 | “many of these pioneers were driven simply by the desire to know and understand, or by the thrill of following through an intriguing pattern or proof.” | 最低改动：删两个「所」字→「被…驱动」。若要避免整块结构重复：把第二个「被…所驱动」缩掉五字，作「……或者只是追随一个耐人寻味的模式或证明时那种颤栗般的兴奋。」（英文只有一次 driven，两个 by） |
| 12.第8章-向量分析终成正果.md | 9 | conj | ……因为正是他把麦克斯韦的整体向量（whole-vector）进路加以扩展，并将其变成了现代的向量分析（vector analysis）。 | “…for he is the one who extended Maxwell’s whole-vector approach and turned it into modern vector analysis.” | 删「加以」二字；「并将其变成了」的「其」换为「它」→「……因为正是他把麦克斯韦的整体向量进路扩展，并把它变成了现代的向量分析。」（英文是 extended…，无「加以」这类公文式动词前缀；破折号与 for 是作者风格，保留） |
| 12.第8章-向量分析终成正果.md | 176 | 的_density | 一千年之后，古希腊人试验过这样一个想法：所表征的不只是商业与社会学的数据，还有关于*空间中的位置*的信息…… | “A thousand years later, the ancient Greeks had experimented with the idea of representing not only commercial and sociological data but information about *locations in space*…” | 删「所」字→「……这样一个想法：表征的不只是商业与社会学的数据，还有……」（英文是 of representing，无「所」字 nominal 化） |
| 13.第9章-从空间到时空.md | 164 | nominalize | ……一种字面意义上的四维空间的可能性正在被大众读物所探讨——比如数学家查尔斯·霍华德·辛顿…… | “…the possibility of a literal four-dimensional space was being tackled in popular books—such as mathematician Charles Howard Hinton’s…” | 删「所」字→「正在被大众读物探讨」；若求更顺，可改主动式「大众读物正在探讨」 |

## 表二：更轻微（4 处，仅删一个「所」字，改不改都不伤文意）

| 文件 | 行号 | 类型 | 现译（片段） | 英文原文片段 | 建议改法 |
|---|---|---|---|---|---|
| 16.第12章-万物汇聚.md | 74 | nominalize | 于是，闵可夫斯基度规必须被一个完全一般的度规所取代 | “…the Minkowski metric had to be replaced by a completely general metric…” | 删「所」→「必须被一个完全一般的度规取代」 |
| 16.第12章-万物汇聚.md | 25 | nominalize | ……会被引力所影响，因此它们会像伽利略和哈里奥特的炮弹那样沿抛物线轨迹运动 | “…which would be affected by gravity, so they would follow parabolic trajectories like Galileo’s and Harriot’s cannonballs.” | 删「所」→「会被引力影响」（或换「会受引力影响」）。注意本行 conj 命中（because…so）是作者风格，不改 |
| 15.第11章-张量的发明.md | 171 | nominalize | 此外，最优秀的学生会被这种严格所激励，而其余的人，他想，也可能从中受益…… | “Besides, the best students were inspired by such rigour, and the rest, he thought, might benefit from it…” | 删「所」→「会被这种严格激励」 |
| 12.第8章-向量分析终成正果.md | 109 | nominalize | 他越来越被电磁学的物理学所吸引——因而也被向量的语言所吸引 | “…he became increasingly drawn to the physics of electromagnetism—and, therefore, to the language of vectors.” | 删两个「所」→「被电磁学的物理学吸引——因而也被向量的语言吸引」 |

## 判为作者风格、不改的典型例（说明理由，供复核）

| 文件 | 行号 | 类型 | 判为风格的理由 |
|---|---|---|---|
| 13.第9章 | 65 | longsent | 英文原句 itself 是一句 60+ 词的长句（Much has been written…, in which…, torn apart by…and the fact that Marić…），中文照译 |
| 15.第11章 | 72 | longsent | 英文「For instance, consider the NLP programs behind such marvels as email spam filters, language translators, converting spoken words to text…, the helpful voice…, the polite text…, and the spectacularly human-like text…」本身就是一串列举长句 |
| 20.致谢 | 16 | longsent | 英文是致谢名单，逐名罗列，无从精简 |
| 14.第10章 | 16 / 34 / 100 / 125 / 174 / 212 / 226 | conj | 英文逐句都有 After all…so / for both men were…and so / Because…but / for it isn’t only / since…not least because…so / But to visualise…so / for…and… 原文本身连接词密集 |
| 15.第11章 | 74 | conj | 英文即为 “The dimension…will therefore be three, so if…”，「因此…所以…」连用来自原文 |
| 16.第12章 | 22 / 96 / 103 / 125 / 248 / 299 | conj | 英文逐句有 since / That’s because…because / Part of the reason is that…so / That’s because…since / four because… / I say “equation” because… |
| 13.第9章 | 190 | conj | 英文 “It was unusual because, as Poincaré had pointed out, physicists were used to…” 破折号插入语＋because 均为原文所有 |
| 12.第8章 | 116 / 148 | conj / pronoun | 英文 “…algebras whose symbols represent more than one number, so that…because…and so on.” 与 “He’d given a paper…and he also added his voice…He was firmly in the quaternionists’ camp” 结构与指代均与中文一致 |
| 18.结语 | 23 / 39 / 41 | pronoun | 英文连续三句均以 They’re / They / It 起头（They’re important in engineering and chemistry…They’re important in digital technologies…; They sought solace…They were curious…; It explained…it makes…），重复「它们／它」是原文排比 |
| 15.第11章 | 344 / 483、14.第10章 | 267 / 288、21.注释 387 / 408 / 466 | 的_density | 「…的分量」「…的系数」「…的张量」「相同的形式和相同的数值」「时间微分的符号与空间的各项」均为术语搭配，英文原文同样逐个对应 |
| 16.第12章 | 113 / 265 / 41、17.第13章 | 48 | 的_density | 英文 “the density of the matter that is the source of the gravity…”“the labels on arbitrary vector and tensor components…”“the energy-momentum tensor that describes…” 定语层数与中文一致 |
| 13.第9章 | 6 / 166 / 169、15.第11章 | 4 / 21 / 128 / 223 / 275 / 299 / 363 | pronoun / nominalize | 英文同样连续以 He / She / These / This / That 起句，或用被动（were allowed to study…、was being tackled…），中文照译 |
| 17.第13章 | 88 | nominalize | 英文 “science both shapes and is shaped by society” 即对举被动，中文「既塑造社会，也被社会所塑造」是修辞对仗，不宜改 |
| 17.第13章 | 72 | conj | 英文 “(The plural is because this ‘equation’ is really four equations, one for each component μ. The repeated index ν indicates a sum.)” 因果连词原样对应 |
| 21.注释 | 153 / 161 / 164 / 222 / 459 | conj / pronoun | 注释为数学推导与文献汇编，英文同样 because / so / since 连用（Geometrically…because…、I wrote…because…、because…so…for…、If the Jacobian is not familiar…），按条目式文本放宽 |
| 20.致谢 | 6 | conj | 英文 “I’m immensely grateful to Joe, not just for…but for…” 与中文「不仅因为…也因为…」一一对应 |
| 19.时间线 | — | — | 本轮无候选 |
