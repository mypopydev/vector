# Round 6 正文 C/D 独立核验

## 结论与计数

逐项回查两份 findings 所列 **28 项**，并对照英文正文/尾注、中文段落、翻译风格指南、术语表及译名表；未改动译文。

| 范围 | 有效 | 部分有效 | 误报 | 主观偏好 | 合计 |
|---|---:|---:|---:|---:|---:|
| C（原报 18 项 Moderate、3 项 Minor） | 12 | 5 | 1 | 3 | 21 |
| D（原报 1 项 Critical、6 项 Moderate） | 3 | 3 | 1 | 0 | 7 |
| **合计** | **15** | **8** | **2** | **3** | **28** |

“有效”指有可证实的语义、术语或忠实度问题；“部分有效”指问题成立但所引位置、解释或所提改法不完全成立；“误报”指所批内容不是译文错误；“主观偏好”指原译可成立，建议主要是风格取舍。定位简称：C7–C9 分别为 `cn-book/11.第7章-从四元数到向量.md` 至 `cn-book/13.第9章-从空间到时空.md`；D10–D13 为 `cn-book/14.第10章-弯曲的空间与不变的距离.md` 至 `cn-book/17.第13章-后来发生了什么.md`。英文 E7–E13 分别为 `en/15_Chapter07.md` 至 `en/21_Chapter13.md`；N 为 `en/25_Notes.md`。

## C 组（21 项）

| # | 定位／提案 | 分类 | 核对证据与最小可辩护动作 |
|---|---|---|---|
| C1 | C7 p154：删去图注末尾的面板标签译文 | **误报** | 中文括注对应图内 `Positive divergence / Negative divergence (=convergence) / Examples of zero divergence`（图注见 C7 p154；图内抄录见 `review/findings/round5-图内文字-b.md` §二）。虽 `docs/翻译风格指南.md` §四第11条通常只要求译图注，但第五轮质量报告明确记录“按用户决定”在图注补出图中文字中文对照（`review/quality-report-round5.md` §二）；这是已授权的新增，不是本轮可据风格指南判为错误的擅加。**保留括注。** |
| C2 | C7 p156：“与纳布拉的向量积和转动有关” | **部分有效** | EN E7 p156 为 “the vector product with nabla has something to do with rotations”；原译大意成立，但主语/关系略含混。所提“与纳布拉作向量积的运算和转动有关”可澄清，不是唯一必要译法。**可小幅改成“与纳布拉作向量积这一运算和转动有关”。** |
| C3 | C7 p158：“社会交往与就业互动正变得日益复杂” | **有效** | EN E7 p158 为 “the increasing complexity of our social and employment interactions”；“就业互动”是生硬搭配。**最小改为“社会交往和工作往来越来越复杂”。** |
| C4 | C7 p165：“没脑子的阔佬” | **有效** | EN E7 p165 为 “our witless nobs”。“nobs”指有地位/显贵人物，不必然只指富人；“阔佬”缩窄为财富特征。**改“没脑子的显贵/权贵”即可。** |
| C5 | C8 p173：带电粒子速度句 | **部分有效** | EN E8 p173 限定为 “any charged particle **whose motion is contributing to a magnetic field** that in turn contributes to the electric field”。原译保留了该限定，但长定语和“贡献着”难读；提案“任何带电粒子……运动会产生磁场”则可能删掉“其运动正在贡献该磁场”的限制。**理顺句法，保留原限定；勿泛化为所有带电粒子。** |
| C6 | C8 p174：“替亥维赛说话的说法并不完全是真实图景” | **有效** | EN E8 p174 “This claim on behalf of Heaviside is not quite the true picture”；“真实图景”直译不自然，提案把语境中的归功说清。**改为“这种替亥维赛邀功的说法并不完全符合事实”一类表达。** |
| C7 | C8（吉布斯致谢段，CN finding 引行131） | **有效** | EN E8 对应句为 “rather ungenerous in denying public credit where it was due”；“public credit”是公开认可/功劳，不是“公开致谢”。**把“公开致谢”改成“公开认可/应有的公开肯定”。** |
| C8 | C8 p186：“拨开自我与优先权的问题” | **有效** | EN E8 p186 “cutting through questions of ego and priority”意为越过/不纠缠这些争论；“拨开问题”搭配不自然。**改“不纠缠于自我与优先权之争”。** |
| C9 | C8（CN finding 引行185）：“领头为向量向四元数发起冲锋” | **主观偏好** | EN E8 的 “led the charge for vectors over quaternions”本身就是冲锋隐喻，原译保留修辞且意思可懂；“率先推动向量分析取代四元数”是更平直的写法，也弱化了原文比喻。**无需改；若统一成平实文风，再按全书口径处理。** |
| C10 | C9 p189：“取得了相当于一等学位的资格” | **部分有效** | EN E9 p189 “qualified for the equivalent of a first-class degree”；后文说明当时女性不能取得正式学位。原译没有明说正式获授学位，但“资格”略容易被读成取得某项正式资格。**可改“达到相当于一等学位的水平”，无需扩展背景。** |
| C11 | C9 p192：JWST “保持在位” | **部分有效** | EN E9 p192 “keeping the James Webb Space Telescope in place”；原译“保持在位”较直译，所提“稳定指向”则把 *in place* 具体化为 pointing，原文并未限定这个含义。**仅改为“维持詹姆斯·韦布空间望远镜的位置稳定”等不增义表达。** |
| C12 | C9 p197：“它比他们两个人更大” | **有效** | EN E9 p197 “it was bigger than the two of them”，上下文指父权文化及整段关系史远超两人个人；原译字面但指代含混。**改为“这段经历/背后的问题牵涉的远不止他们两人”。** |
| C13 | C9 p197：考官性别歧视句 | **有效** | EN E9 p197 “what I believe is the sexism of the examiners who failed Marić twice”；原译“我相信存在性别歧视的那些考官”容易把“我相信”挂到考官身上。**改句法，使“我认为”修饰考官判她两次不及格时的性别歧视，保留作者限定。** |
| C14 | C9（相对论“real”段）：“提出可检验的预言来检验他的理论” | **有效** | EN E9 “make it ‘real’ by suggesting testable predictions to check his theory”；原译“可检验／检验”重复且“让它变真”生硬。**重排成“爱因斯坦提出可用于检验理论的预言，使它变得‘真实’”。** |
| C15 | C9 p211：“标量（或点）积” | **有效** | EN E9 p211 “the scalar (or dot) product”；`docs/术语表.md` §五分别规定 *scalar product*＝“标量积”、*dot product*＝“点积”（第146–148行）。原译括号范围不清，也未按两条词项配对。**改“标量积（或点积）”。** |
| C16 | C9 p213：“平衡这些‘应力’力”；“额外应力冲击” | **有效** | EN E9 p213 “balance these ‘stress’ forces”及“potential additional stress impacts”；“应力力”重复，“应力冲击”不自然。**改“平衡这些‘应力’”及“可能带来的额外应力影响”。** |
| C17 | C9 p214：“为一个单一量的分量给出了一个简明的定义” | **部分有效** | EN E9 p214 “give a concise definition of the components of a single quantity”；原译语义大体在，但“一个单一量”冗余且结构拗口。提案“定义了一个整体量的各个分量”可读，但不要把原文“给分量下定义”的关系改成“定义整体量”。**精简为“简明地给出了一个整体量各分量的定义”。** |
| C18 | C9 尾注 ch09n27（finding 标 C9:336）：“二阶（second-rank 或 second-order）张量” | **有效** | 这条不是按邻近正文猜测：中文尾注与 N 的 `[^ch09n27]` 对照，EN 明确为 “antisymmetric second-rank or second-order tensors”，并说明 rank/order 是分量指标数；`docs/术语表.md` 第435、535行分别规定“秩/阶”及“二秩/二阶”。当前把两词都括成“二阶”，错失区别。**改“二秩（second-rank）或二阶（second-order）张量”。** C finding 称 `en/17_Chapter09.md` 没有对应尾注，但只看章文件不够；英文尾注在 N（p383）中，故原“不确定”应撤销。 |
| C19 | C8 p174：“围绕着……而生长出来的那个流行传说” | **有效** | EN E8 p174 “the popular legend that has grown up around the previously long-neglected Heaviside”；“生长出来的传说”是英语结构直搬。**改“围绕这位长期被忽视的亥维赛形成的流行传说”。** |
| C20 | C8（CN finding 引行119）：“绝对的必需” | **主观偏好** | EN E8 对应 “a positive necessity”；“绝对的必需”表达必要性，提案“绝对必要”更简洁但属词性/节奏取舍。**不构成必须修正。** |
| C21 | C9（CN finding 引行261）：“把脚趾伸进了张量分析” | **主观偏好** | EN E9 对应 “dipped his toe into tensor analysis, too”；原译保留原文涉足隐喻，提案“初涉”更自然但取消隐喻。**按全书修辞口径决定，不作硬性改动。** |

## D 组（7 项）

| # | 定位／提案 | 分类 | 核对证据与最小可辩护动作 |
|---|---|---|---|
| D1 | D11 p240：标题遗漏 “AND WHY THEY MATTER” | **有效** | EN E11 标题完整为 `INVENTING TENSORS—AND WHY THEY MATTER`；中文只有“张量的发明”，既没有把后半句译为副标题，也没有另列对应小标题。不是全书统一省略：第8章中文保留英文标题的破折号后半（C8 p168），第10、12章还保留了独立副标题（D10/D12章首）。风格指南 §一第2条禁止删减。**补“——以及它们为何重要”。** |
| D2 | D10 p219：“传奇老师高斯”应写全名 | **误报** | EN E10 p219 确为 “his legendary teacher, Gauss”，但 Gauss 早在第3章 p53 已出现；CN `cn-book/7.第3章-向量的构想.md` 该处译作“高斯……”，故第10章这里不是首次出现。风格指南 §二第6条及 `docs/译名表-人名.md` 第27行要求首现用全名，后文只用中文姓；若要补救，**应核实/修正第3章首现，而不是在此再次加全名**。 |
| D3 | D10 p225：`“高斯”曲率，即内蕴曲率` 未附英文 | **有效** | EN E10 p225 说球面曲率为 its “‘Gaussian’ or intrinsic curvature”；C9/D10之前英文没有该术语，中文第10章后文也在 p228 才出现“高斯曲率（Gaussian curvature）”。`docs/术语表.md` 第131行规定 *Gaussian curvature*＝“高斯曲率”，第14行规定术语首现中文后附英文。**在 p225 首现处补“高斯曲率（Gaussian curvature）”，并保持“内蕴曲率”对译。** |
| D4 | findings 引 D11:4，称 “his tensor calculus” 首现未加英文 | **部分有效** | 引用位置和英文短语不对应：D11 p240 第4行谈里奇童年；“his tensor calculus”实际在 E12 p274，中文 D12 p274 已写“张量微积分（tensor calculus）”。但同章真正首现位于 E11 p241 的 “paper on tensor calculus”，对应 D11 p241“关于张量微积分的里程碑式论文”，确实未附英文；词表 `docs/术语表.md` 第143行将 *tensor calculus* 定为“张量微积分”，风格指南 §二第5条要求术语首现附英文。**若修正，锚定 D11 p241 首现，补“张量微积分（tensor calculus）”；纠正 finding 的行号/引文，不在 D11 p240 另加。** |
| D5 | D12 p281：“富有洞见的共鸣板” | **有效** | EN E12 p281 “his longtime insightful sounding-board”指可供交流想法、听取反馈的人，不是共鸣板。当前直译确有误导性。**改“他长期以来交流想法、获得反馈的对象”等。** |
| D6 | D12 p291：“同时在耍许多只不同的球……融进最终的最终方程里” | **部分有效** | EN E12 p291 有意用 “juggling many different balls that all had to meld into the final equations”作比喻；原译保留了比喻，但“耍球”不自然且“最终的最终”重复。提案“彼此牵连的问题”增添了源文没有的彼此关联判断。**可改为“同时抛接着许多不同的球，而这些球最终都必须汇入方程”，保留原比喻并删冗。** |
| D7 | D13 p305：“她的存在又是如此独特” | **部分有效** | EN E13 p305 “her presence was so singular”承接她的特殊身份/处境，以致同事仍称她“Miss”而非“Doctor”。原译“存在”较直译；提案“情况”泛化，未明确这种特殊性。**可改“她的身份/处境又如此特殊”，保留语境关联。** |

## 指定陷阱与范围缺口

- **Szcezcin：**C/D 两份列表中没有一项提出该拼写，但已核查：`en/13_Chapter05.md` 原文确实写 “Stettin—now spelled Szcezcin”；中文第5章也照录为“如今拼写为 Szcezcin”。`docs/译名表-人名.md` 第255行列的是标准形式 `Stettin / Szczecin` 及译名“斯德丁 / 什切青”；第3行说明地名首现可附英文。故这处不是译者凭空拼错，不能仅凭外部常识将它算作译文错误。若要改源文的错拼，应作为编辑性更正另行决定；**C/D 计数不含此项。**
- **D 尾注范围：**D 审校明示没有检查中文尾注，四个章节文件元数据均为 `note=0`。本报告只裁定 D 列出的 7 条正文问题；尾注审校仍是范围缺口，应把 `cn-book/21.注释.md` 与集中保存英文尾注的 `en/25_Notes.md` 对照另审。此缺口不并入 28 条计数。
- **C 对尾注范围的说明需更正：**C 所列 ch09n27 的英语文本确在 `en/25_Notes.md`，而不是 `en/17_Chapter09.md`；因此该条已可核验，并按术语表判为有效，不再保留为不确定项。

## 优先级最高的已确认项

1. **D1 标题漏译（原报 Critical）**：补齐 “AND WHY THEY MATTER”。
2. **D4 张量微积分首现漏注英文（原报 Moderate，需把 finding 定位从 D11:4 改到 p241）**。
3. **C18 二秩/二阶术语混同（原报 Moderate）**：源英文尾注与术语表均清楚区分两者。
4. **D5 sounding-board 误译（原报 Moderate）**：将人比作“共鸣板”属实质误译。
