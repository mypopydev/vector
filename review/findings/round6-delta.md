# 第六轮基线差异清单

基线：当前 `HEAD` `2b44c56`，标签 `v1.0.9` 为 `3b5609b`；第五轮内容复核产出基线为 `v1.0.7`。当前译稿相较 `v1.0.7` 仅以下三份 `cn-book/` 文件有变化。其余差异（README、构建/排版工具、校验报告跟踪方式）不是译文内容差异。

| 文件 | 当前变化 | 回归检查点 | 对照 |
|---|---|---|---|
| `cn-book/1.名家推荐.md` | 七条署名行包入 `.attribution`；《书商》署名移除嵌套斜体，英文刊名仍留在粗斜体署名中 | 七条署名的 Markdown 结构和文案是否完整；刊名斜体/粗体呈现是否符合原评语；PDF 与网页对齐 | `en/03_Reviews.md` |
| `cn-book/5.第1章-代数的解放.md` | `think symbolically` 相关表述改为「符号化地思考」；`symbolic thinking` 相关表述改为「符号化思维」 | 对照各处句义和标题；确认没有把 symbolic / symbolically / symbolic thinking 的语法关系改混，且上下文通顺 | `en/09_Chapter01.md` |
| `cn-book/6.第2章-微积分的登场.md` | `symbolic thinking` 改为「符号化思维」 | 对照原句语义与段落衔接，确认与第 1 章口径一致 | `en/10_Chapter02.md` |

确认项：`cn-book/21.注释.md` 与 `cn-book/22.索引.md` 相较第五轮基线无变化；历史条目要以当前文件实况判断，不将 `review/*.md` 生成报告从 git 索引移除视为译稿删失。
