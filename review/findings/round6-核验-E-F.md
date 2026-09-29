# Round 6 E/F findings — independent adjudication

按每个 finding 的英文原文与中文译文逐项核对；F 项逐一对照所标注的尾注 ID（不以章节正文代替）。遵循 `docs/翻译风格指南.md:7-9,46` 的忠实度要求，并核对术语表及项目决策记录。

## Findings

| ID | Finding / exact context | Classification | Evidence | Minimum correction if valid |
|---|---|---|---|---|
| E1 | 时间线 `en/23_Timeline.md:31` / `cn-book/19.时间线.md:31`：乘以 *i* 是“绕这个平面旋转 90°”。 | valid | 复数乘以 *i* 所表示的是在复平面内作 90° 旋转；“绕平面旋转”易读成以平面为旋转轴。英文的 `around this plane` 在这里也是几何表达不严谨，译成“在平面内”保留其意图而非曲解字面。原文未指定方向，不应补方向。 | “乘以 *i* 很快被解释为在这个复平面内旋转 90°。” |
| E2 | 结语 `en/22_Epilog.md:7` / `cn-book/18.结语.md:7`：PET 的 `used routinely` 译为“已被常规使用”。 | subjective preference | 含义正确；“常用于”更简洁自然，但不是忠实度错误。 | —（可润为“如今已常用于……”） |
| E3 | 时间线 `en/23_Timeline.md:89` / `cn-book/19.时间线.md:89`：`image of (the shadow of) a black hole` 译为“黑洞（阴影的）直接图像”。 | partly valid | 英文括号本身嵌套生硬；中文照搬后“阴影的”留在括号内，修饰关系不顺。建议把“的”移到括号外可改善可读性，但不是黑洞/阴影事实误译。 | “首张黑洞（阴影）的直接图像……” |
| E4 | 时间线 `en/23_Timeline.md:90` / `cn-book/19.时间线.md:90`：`shares the Nobel Prize` 译为“分享诺贝尔物理学奖”。 | subjective preference | “分享”能表达共同获奖；“共同获得”较符合中文颁奖习惯，是措辞偏好。 | —（可润为“共同获得诺贝尔物理学奖”） |
| E5 | 时间线 `en/23_Timeline.md:91` / `cn-book/19.时间线.md:91`：`announces new accuracy for the equivalence principle` 译为“宣布了等效原理的新精度”。 | valid | “新精度”直接归属于“等效原理”，使测量精度的对象不清；语境指等效原理检验达到的精度。原文是科学简写，中文需显出“检验”。 | “宣布等效原理检验达到新的精度。” |
| E6 | 时间线 `en/23_Timeline.md:76` / `cn-book/19.时间线.md:76`：`the first successful new test` 译为“第一次成功的新检验”。 | subjective preference | 译文传达了“首次成功的新检验”；“第一次成功的新检验”略显生硬，问题主要是语序/文风，不是事实或限定语错误。 | —（可润为“这是首次成功开展的一项广义相对论新检验。”） |
| E7 | 致谢 `en/24_Acknowledgments.md:6` / `cn-book/20.致谢.md:6`：`ongoing editorial skill` 译为“持续的编辑技巧”。 | subjective preference | 基本意思在；“持续的编辑技巧”搭配较直译，建议的“编辑功力”更地道，但属于文风润色。 | —（可润为“他始终展现出的编辑功力”） |
| E8 | 致谢 `en/24_Acknowledgments.md:11` / `cn-book/20.致谢.md:11`：`my affiliation with the School of Mathematics` 译为“我与……的隶属关系”。 | false positive | `affiliation` 可指正式的机构/学术隶属关系，“隶属关系”并非误译；改成笼统的“联系”反而弱化正式机构关系。现译略正式，不足以认定为实质问题。 | — |
| F1 | **尾注 ch06n9**：`en/25_Notes.md:472` / `cn-book/21.注释.md:223`。英文说园地的保留与宅邸、附属建筑的修复都主要归功于庄园主人；中文将“得以保存”连到“修复”，造成修饰错接。 | valid | 已核对 ch06n9 本条完整 EN/CN 注释；问题就在这条注释自身。 | “这片园地得以保留、格伦莱尔宅邸及附属建筑得以修复，主要归功于……” |
| F2 | **尾注 ch06n18**：`en/25_Notes.md:506` / `cn-book/21.注释.md:239`。`Reid ... stated that Tait was a candidate` 译为“确认泰特确为候选人”。 | valid | 已核对 ch06n18 本条。`stated` 是“称/说”，`确认确为` 把陈述升级成了证实；前文 `it was believed` 也保留了原文的证据层次。 | 将“确认泰特确为候选人”改为“称泰特是候选人”。 |
| F3 | **尾注 ch11n22**：`en/25_Notes.md:1002` / `cn-book/21.注释.md:453`。`scalar (or inner) product` 现译“数量（内）积”。 | valid | 此尾注的术语确实过时：项目记录明确决定全书 `scalar product` 用“标量积”（`review/findings/汇总-批次1.md:100`）；术语表分别列 `scalar product＝标量积`、`inner product＝内积`（`docs/术语表.md:147,150`）。检查的是 ch11n22 尾注本身，不是第 11 章正文。 | “列向量与行向量的标量积（或内积）”。 |
| F4 | **尾注 ch14n1**：`en/25_Notes.md:1233` / `cn-book/21.注释.md:563`。中文在“阴性结果”后加“（即未发现新粒子的结果）”。 | valid | 已读完 ch14n1 的完整英文尾注：其先谈标准模型、科学与社会收益及对科学收益的质疑，再说 Quora 帖子认为 LHC 的 `negative results` 对科学重要，意义在于排除流行理论。原文没有“未发现新粒子”；这会把更广的阴性/排除结果过窄限定成一种结果，且风格指南要求不扩写（`docs/翻译风格指南.md:9`）。术语“阴性结果”本身符合术语表 `docs/术语表.md:518`。 | 删除“（即未发现新粒子的结果）”。 |

## Summary

| Classification | Count |
|---|---:|
| valid | 6 |
| partly valid | 1 |
| false positive | 1 |
| subjective preference | 4 |
| **Total** | **12** |

## Uncertainties / prior decisions

- **Geometry:** the English timeline’s `around this plane` is itself imprecise. The intended complex-plane geometry supports “在复平面内旋转 90°”; no rotation direction is stated, so none is added.
- **Negative-results parenthetical:** `review/findings/汇总-批次4.md:78` records the earlier change to “阴性结果（即未发现新粒子的结果）”, but no explicit user approval for that parenthetical was found in the accessible project records. It is not source-safe against the full ch14n1 note; only “阴性结果” is supported. The configured persistent memory index/path was unavailable in this environment, so no separate memory decision could be checked.
- **Scalar / inner product:** the explicit 2026-09-27 user decision is present in repository context (`review/findings/汇总-批次1.md:100`); ch11n22 is stale relative to it.
