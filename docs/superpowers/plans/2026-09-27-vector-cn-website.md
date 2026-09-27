# 《向量》中文版 · 接入 mypopydev.github.io 实施计划

**目标**：把已完成的中文译本作为新板块接入现有站点 `mypopydev-web`（remote = `git@github.com:mypopydev/mypopydev.github.io.git`），发布到 `https://mypopydev.github.io/`。

**已确认**：技术栈 = MkDocs Material；发布 = 公开。

## 一、目标站点现状（已核实，省掉大量工作）

仓库：`/Users/barryjzhao/Sources/AI/mypopydev-web`，站点名 Barry's Tech Notes。

| 已有设施 | 状态 | 对我们的意义 |
|---|---|---|
| KaTeX（CDN + `docs/assets/javascripts/katex.js`） | ✅ 已配置 `$$…$$` / `$…$` | **公式不用做任何处理**，原样搬过去就渲染 |
| `footnotes` 扩展 | ✅ | `[^ch01n1]:` 脚注直接可用 |
| `attr_list` / `md_in_html` / `admonition` / `pymdownx.details` | ✅ | 原始 HTML 能穿透，自定义 div 可用 |
| 中文搜索（jieba 分词） | ✅ 已启用 | 全站可检索，含正文 |
| GitHub Actions（`deploy-pages.yml`） | ✅ push main 即构建部署 | **不用再写 CI** |
| `docs/assets/images/` 共享图片约定 | ✅ | 书的插图放在 `docs/assets/images/vector/` |
| `mkdocs build --strict` 基线 | ✅ 通过（2.63s） | 现有站点健康 |

**结论**：不需要新建 mkdocs.yml、不需要写 workflow、不需要配数学、不需要 CNAME。只差三件事：把 Markdown 转成 Python-Markdown 能吃的格式、加导航、补少量 CSS。

## 二、产出位置

```
mypopydev-web/
├── docs/
│   ├── books/vector-zh/          # 【生成】23 篇章节 Markdown
│   │   ├── index.md              # 书的落地页（封面/简介/目录/PDF/版权）
│   │   └── 00-译本说明.md … 22-索引.md
│   └── assets/images/vector/     # 【生成】57 张插图
├── docs/assets/stylesheets/extra.css   # 【追加】infobox / displayeq / origpage 样式
└── mkdocs.yml                    # 【追加】nav 里加「向量（中译本）」板块
```

`vector/` 侧只新增一个脚本 `tools/build_site.py`，用 `--target <站点仓库路径>` 指定输出位置（默认 `/Users/barryjzhao/Sources/AI/mypopydev-web`）。

## 三、Markdown 适配：pandoc 方言 → Python-Markdown

只改输出副本，不动 `cn-book/`：

| 原文 | 转换后 | 说明 |
|---|---|---|
| `$…$` `$$…$$` | 原样 | KaTeX 已配好 |
| `[^ch01n1]: 译文` + 4 空格续行 | 原样 | 同上 |
| `# 第 1 章 …` / `## 节` | 原样 | |
| `![](images/x.jpg){width="50%"}` | `<img src="../../assets/images/vector/x.jpg" style="width:50%">`，包进 `<figure markdown="1">` + `<figcaption>` | `attr_list` 不支持行内图片属性，会显示成字面文字 |
| `::: {.infobox}` / `:::` | `<div class="infobox" markdown="1">` / `</div>` | 需 CSS |
| `::: {.displayeq}` / `:::` | `<div class="displayeq" markdown="1">` / `</div>` | 居中公式段 |
| `<!--p123-->` | `<span class="origpage" title="英文原版第 123 页">123</span>` | 上标灰字，悬停给说明 |
| `*斜体*` `**粗体**` | 原样 | |
| `^**2**^` / `~1~`（pandoc 上/下标） | `<sup>2</sup>` / `<sub>1</sub>` | |
| 裸长 URL | 包成 `<URL>` | 脚注里的 URL 要能换行 |
| `• • •` | 原样（CSS 居中） | 章节分隔符 |

## 四、任务

### 任务 1：`vector/tools/build_site.py`
- 复用 `build_pdf.py` 的 `CHAPTER_NO` 顺序（网页与 PDF 顺序一致，单一真源）
- 参数：`--target`、`--check`
- 流程：生成 `docs/books/vector-zh/` → 逐文件转换 → 复制 `images/` 到 `docs/assets/images/vector/` → 生成 `index.md` 落地页 → 打印统计（文件数/图数/公式数）
- 落地页（对标 mml-book）：封面图、简介、23 章目录链接、PDF 下载、**原书版权 + 非商业声明 + 异议即下架说明**

### 任务 2：CSS（追加到站点 `extra.css`）
- `.infobox`：浅灰底 + 圆角 + 左侧色条，观感贴近 Material 的 admonition
- `.displayeq`：居中 + 上下留白
- `.origpage`：小号灰字上标，不影响行距
- 图注居中、图片最大宽度

### 任务 3：nav（追加到站点 `mkdocs.yml`）
- 在「关于」板块前插入 `向量（中译本）` 分组，23 个条目指向 `books/vector-zh/*.md`
- 改前备份 `mkdocs.yml`；nav 片段由脚本生成，避免手写出错

### 任务 4：验收
- `tools/build_site.py --check`：
  - 每个章节存在、非空、H1 与 PDF 侧一致
  - 所有 `<img src>` 目标文件真实存在（防 404）
  - 转换残留检测：不得再出现 `{width=`、`{.infobox}`、`<!--p`、裸露的 `:::`、`` ^** ``
  - 公式数（复用 `check_math.formulas()`）与 PDF 侧逐章一致
- 站点仓库 `mkdocs build --strict` 必须 0 warning
- 浏览器检查：目录可点、公式渲染、脚注回链、图显示、搜索命中正文词汇
- 按站点约定在 `docs/resources/CHANGELOG.md` 记一条

### 任务 5：发布
```bash
cd /Users/barryjzhao/Sources/AI/mypopydev-web
git add docs/books/vector-zh docs/assets/images/vector docs/assets/stylesheets/extra.css mkdocs.yml docs/resources/CHANGELOG.md
git commit -m "feat(translation): 新增《向量》中文译本"
git push origin main     # Actions 自动构建部署
```
Pages 来源已是 GitHub Actions（见 `docs/resources/deployment.md`），无需再改设置。

## 五、⚠️ 公开发布的合规项（必做）

公开站点提供整本译稿，性质比个人 PDF 重。必须：

1. 书的落地页页首：原书名、Robyn Arianrhod、UNSW Press / NewSouth Publishing、© 2024 + 「本中文译本为学习与非商业用途，著作权归原作者及原出版社所有」
2. 落地页显著位置：权利人提出异议即下架
3. README / 仓库 About 同步注明
4. 先本地 `mkdocs serve` 通读确认无误后再 push

## 六、不做的事 / 待确认

- 不改现有站点的主题、配色、既有导航结构（只在末尾板块前插入一组）
- **待确认**：站点仓库根目录有一份 7.6MB 的 `Vector … .epub`（原书），公开仓库里放整本原书 epub 风险不小，建议删除或确认保留
- 站点仓库已有 `site/` 被 gitignore，不提交
