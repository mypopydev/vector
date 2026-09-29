# 第六轮渲染层补充发现：站点图像与图注

## 1. 已在隔离 worktree 修复的插图 URL

- **问题**：站点页使用目录 URL `/books/vector-zh/<slug>/`，但 `tools/build_site.py` 原来生成 `../../assets/images/vector/...`。浏览器把它解析为 `/books/assets/...`，图片返回 404；目标资产实际位于 `/assets/images/vector/...`。
- **证据**：本地与线上旧 URL `.../books/assets/images/vector/fig3_1.jpg` 为 HTTP 404；对应 `/assets/images/vector/fig3_1.jpg` 为 HTTP 200。已只读抓取线上第 3 章 HTML，确认旧 `<img src>` 相对路径确实产生了该错误 URL。
- **修复**：`tools/build_site.py:135` 生成 `../../../assets/images/vector/...`；`:274-297` 的 `--check` 现在按浏览器页面 URL 解析章页图片和落地页封面链接，并检查相应资产是否存在。
- **验证**：用旧生成页面作负向测试，旧 `check()` 错误返回 0；修后对旧内容报出 53 项。重新生成后 `build_site.py --check` 通过；在隔离 MkDocs 预览逐页请求图片，54 张（含封面）全 HTTP 200。未改站点仓或线上站点。

## 2. 尚未处理、需单独授权的重复图注编号

- **问题**：`cn-book` 图注已经显式包含“图 N.M”，但 `tools/build_site.py:136-142` 又自动生成 `图 {chapter}.{fig_no}` 前缀。生成的 `docs/books/vector-zh/07-ch03-ideas-for-vectors.md:25` 是“图 3.1　<a ...>图 3.1</a>　把两个向量……”，浏览器实际显示为重复的“图 3.1 图 3.1”。
- **影响范围**：预计所有显式编号图注会重复；当前顺序计数还会把无编号图版纳入，并且面板字母/跨章锚点的映射需要核查，不能只删除一个前缀后就宣称全部修好。
- **证据**：本地 Playwright 截图显示重复编号；只读抓取线上 `/books/vector-zh/07-ch03-ideas-for-vectors/` 的 HTML，同样看到 `<p class="figcap">图 3.1　<a href="#fig-3-1">图 3.1</a>　…</p>`，因此线上重复可确认。
- **处理状态**：用户决定**暂不修**。本轮不改图注编号/锚点生成逻辑；若另开专项，建议按译稿显式编号建立 caption/anchor、无编号图版不编号、保留 A/B/C 面板后缀并检查跨章引用，用实际 HTML/PDF 文本层验证。

图片 URL 修复与译文 findings 已随 `eda5d0c` 在隔离分支本地提交；未推送或部署。重复图注/锚点问题保持未修，待用户另行授权。