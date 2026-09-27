# 注释引文核对（序言 + 第 1–4 章）

核对范围：中文 `cn-book/21.注释.md` 第 3–184 行（序言 / 第 1 章 / 第 2 章 / 第 3 章 / 第 4 章），
英文 `en/25_Notes.md` 第 4–394 行（PROLOGUE 至 CHAPTER 5 之前）。
本次为**逐条全量核对**，未抽样。

## 覆盖证据

- **核对注释条数：106 条**（`[^ch00n1]`–`[^ch00n9]` 9 条、`[^ch01n1]`–`[^ch01n22]` 22 条、
  `[^ch02n1]`–`[^ch02n16]` 16 条、`[^ch03n1]`–`[^ch03n25]` 25 条、`[^ch04n1]`–`[^ch04n34]` 34 条）。
  中英文注释编号一一对应，**无缺条、无多余条**。
- **英文成对引号总数：110 段**（含 `ch03n5` 的嵌套单引号 'Tamburlaine I and II'、
  `ch03n24` 的嵌套单引号 'Better without the Ladies'）。
- **判定分布：**
  - **72 段**为文献题名／篇名／期刊文章名，中文**原样保留英文并带引号**（未丢失）——占 65.5%
  - **38 段**为术语或引语，中文**译成不带英文的中文并带 “ ” 弯引号**（项目既定做法，正常）——占 34.5%
  - **0 段**丢失，**0 段**整段漏译，**0 段**中文凭空新增引号内容
- 补充交叉校验（用于排除「引文随整段一起被删」）：本区段内英文全部 **URL 均出现在中文**，
  无一条缺失；数字/页码差异全部为日期格式改写（如 `August 29, 2017` → `2017 年 8 月 29 日`），无实质遗漏；
  各条中英长度比落在 0.29–1.00 的正常区间，无异常短条。

### 38 段「术语中译、不带英文引号」的逐条落点（证明并非漏引号）

| 注释 | 英文引号内容 | 中文处理 |
|---|---|---|
| ch00n2 | “vector field” | “向量场” |
| ch00n8 | “clock time” | “时钟时间” |
| ch00n9 | “commutativity” | “交换性” |
| ch01n1 | “connect *calculation* with *geometry*” | “*计算*”与“*几何*” |
| ch01n1 | “from the plane to space” | “从平面推向空间” |
| ch01n19 | “fundamental theorem of algebra” / “factor” | “代数基本定理” / “因式” |
| ch02n1 | “ether” | “以太” |
| ch02n6 | 莱布尼茨两则引文 + 牛顿一则引文 | 三条均以 “ ” 完整译出 |
| ch02n13 | “dry calculators” / “diatribe” / Warnaar 长引文 | “干瘪的计算者” / “一篇激烈的抨击” / 长引文完整译出 |
| ch03n3 | “Vituperative” | “辱骂性的” |
| ch03n8 | “translated” / “compos[ing] the apparent motion” / “impetus” | “平移” / “合成表观运动” / “冲力” |
| ch03n9 | “As if” | “仿佛” |
| ch03n17 | “directed lines” | “有向直线” |
| ch03n20 | “steps” | “步” |
| ch04n1 | “my boys” | “我的孩子们” |
| ch04n3 | “modulus” / “absolute value” / “conjugate” / “the law of moduli” | “模” / “绝对值” / “共轭” / “模律” |
| ch04n6 | “Deeply reverential” | “极为崇敬” |
| ch04n8 | “difference engine” | “差分机” |
| ch04n11 | “electric circuit” | “电路” |
| ch04n17 | “invariants” | “不变量” |
| ch04n24 | “machinery” | “机械装置” |
| ch04n27 | “normalised” / “h-bar” | “归一化” / “h 拔” |
| ch04n29 | “vector space” | “向量空间” |
| ch04n30 | “similarity transformation” | “相似变换” |
| ch04n31 | “matter wave” / “wave function” | “物质波” / “波函数” |

（`ch04n11` 的 “closed” 因需说明时态改写，中文保留英文原词 `"closed"`，亦未丢失。）

## 问题列表（按严重度排序）

### 严重

（无）

### 中等

（无）

### 轻微

`ch01n1 | 轻微 | 增译引号 | “connect *calculation* with *geometry*,” | 他把“*计算*”与“*几何*”联系起来 | 英文是一整段引文，中文拆成两对引号；内容无增无减，可保留，若要严格对齐可改为把“把*计算*与*几何*联系起来”整句放入一对引号`

`区段级 | 轻微 | 引文丢失（待判） | 72 处英文题名在中文里用 ASCII 直引号 "…" | "Plimpton 322: A Study of Rectangles," 等 | 内容未丢失，但与中文弯引号 “ ” 体例不统一；建议统一为中文弯引号 “ ”，或改 `tools/check_fidelity.py` 的 QUOTED_CN 正则使其同时识别 ASCII 引号`

## 备注：`check_fidelity.py`「引文数量偏少」告警在本区段为误报

该脚本 `QUOTED_CN = re.compile(r"[“]([^”]{4,})[”]")` **只识别中文弯引号**，而本区段中文对英文题名统一使用
ASCII 直引号 `"…"`。实测本区段：脚本口径英文计 108 段、中文仅计 19 段，看似缺口 82%；
实际人工核对为 **英文 110 段 / 中文 111 段对应项（含 ch01n1 一处拆分），覆盖率 100%**。
告警根因在正则，不在译文。**建议不要据此项修改译文。**

## 统计

| 严重度 | 条数 |
|---|---|
| 严重 | 0 |
| 中等 | 0 |
| 轻微 | 2 |

其中：引文丢失（题名）0 条、引文丢失（整段漏译）0 条、引文丢失（待判）0 条（另 1 条区段级体例建议）、
增译引号 1 条。
