# 向量：一个关于空间、时间与数学变换的惊奇故事（中文译本）

> *Vector: A Surprising Story of Space, Time, and Mathematical Transformation*
> Robyn Arianrhod（罗宾·阿里安罗德）著 · UNSW Press / NewSouth Publishing, 2024

从巴比伦泥板上的乘法表，到哈密顿在布鲁姆桥上刻下的四元数公式，再到麦克斯韦的电磁场、闵可夫斯基的时空，以及爱因斯坦借张量写下的广义相对论——这本书讲向量与张量穿越五千年的故事。

| | |
|---|---|
| 英文原书 | 158,316 词（正文 + 注释 + 索引） |
| 中文译稿 | 23 个 Markdown 文件，汉字 264,233 字（汉字/英文词 = 1.67） |
| 成书 PDF | A4，330 页，`dist/vector-cn.pdf` |

---

## ⚠️ 版权声明

**本译本为个人学习与非商业交流用途的翻译。** 原书文字、插图与版式的著作权归原作者 Robyn Arianrhod 及原出版社所有，本译本不主张任何权利，也不得用于任何商业用途。

---

## 📁 目录结构

| 路径 | 内容 |
|---|---|
| `cn-book/` | **中文译稿（Markdown，唯一真源）** |
| `en/` | 从 epub 抽取的英文 Markdown 与统计清单（对照与校验用） |
| `images/` | 原书 57 张插图 |
| `docs/` | 术语表、人名译名表、翻译风格指南 |
| `tools/` | 抽取、翻译辅助、校验、构建脚本 |
| `review/` | 结构与基线检查报告 |
| `dist/` | 生成的中文版 PDF |

## 🌐 网页版

译稿同步发布为 MkDocs Material 站点（个人站 `mypopydev.github.io`）：

```bash
python3 tools/build_site.py           # cn-book/*.md -> 站点 docs/books/vector-zh/ + 插图
python3 tools/build_site.py --check   # 校验页面/图片/残留标记
python3 tools/build_site.py --nav     # 生成要插入 mkdocs.yml 的导航片段
# 在站点仓库里：mkdocs serve（预览） / mkdocs build --strict（检查）
```

网页版的图按「章.序号」显式编号，正文里的「图 N.M」是锚点链接；
页边灰色小字同样是英文原版页码。

## 🔧 流水线

```bash
python3 tools/extract_epub.py      # epub -> en/*.md + images/
                                   # （含 MathML -> LaTeX）
python3 tools/build_pdf.py         # cn-book/*.md -> dist/vector-cn.pdf
python3 tools/split_notes.py       # 把注释定义分发到各章（正文出当页脚注）
python3 tools/sort_index.py        # 索引按拼音排序
```

校验（每章译完必跑，严重项必须为 0）：

```bash
python3 tools/check_structure.py   # 段/图/公式/尾注/节标题/分页标记 逐项中英对齐
python3 tools/check_math.py        # 公式与英文逐条一致、且能编译
python3 tools/check_terms.py       # 术语译名一致性、禁用译名
python3 tools/check_fidelity.py    # 忠实度守卫（数字/专名/引文/译名/伪公式运算符/段落长度）
python3 tools/check_baseline.py    # PDF 缺字形 / 丢字 / 越界裁切
python3 tools/test_mathml2tex.py   # MathML->LaTeX 转换器单测 + 全书公式自检
```

## 📖 章节目录

- [译本说明](cn-book/0.译本说明.md) · [名家推荐](cn-book/1.名家推荐.md) · [作者简介](cn-book/2.作者简介.md) · [献词](cn-book/3.献词.md)
- [序言](cn-book/4.序言.md)
- [第 1 章　代数的解放](cn-book/5.第1章-代数的解放.md)
- [第 2 章　微积分的登场](cn-book/6.第2章-微积分的登场.md)
- [第 3 章　向量的构想](cn-book/7.第3章-向量的构想.md)
- [第 4 章　理解空间（与存储）](cn-book/8.第4章-理解空间与存储.md)
- [第 5 章　出人意料的新角色与缓慢的接受](cn-book/9.第5章-出人意料的新角色与缓慢的接受.md)
- [第 6 章　泰特与麦克斯韦：电磁向量场的孕育](cn-book/10.第6章-泰特与麦克斯韦.md)
- [第 7 章　从四元数到向量](cn-book/11.第7章-从四元数到向量.md)
- [第 8 章　向量分析终成正果——以及一场围绕四元数的"战争"](cn-book/12.第8章-向量分析终成正果.md)
- [第 9 章　从空间到时空：向量的新转折](cn-book/13.第9章-从空间到时空.md)
- [第 10 章　弯曲的空间与不变的距离：通往张量之路](cn-book/14.第10章-弯曲的空间与不变的距离.md)
- [第 11 章　张量的发明——以及它们为何重要](cn-book/15.第11章-张量的发明.md)
- [第 12 章　万物汇聚：张量与广义相对论](cn-book/16.第12章-万物汇聚.md)
- [第 13 章　后来发生了什么](cn-book/17.第13章-后来发生了什么.md)
- [结语](cn-book/18.结语.md) · [时间线](cn-book/19.时间线.md) · [致谢](cn-book/20.致谢.md)
- [注释（353 条）](cn-book/21.注释.md) · [索引（636 条）](cn-book/22.索引.md)

## 📐 排版说明

- 引擎：pandoc + XeLaTeX（ctexbook，A4，11pt，1.25 倍行距）
- 数学：MathML 由 `tools/mathml2tex.py` 转成 LaTeX，全书 262 处公式逐条编译验证
- 图：按「章号.序号」编号，与原书 FIGURE 0.1 / 1.1 对应
- 注释：原书集中在书末，本译本改为**当页脚注**，书末另附完整汇编
- 页边灰色数字：**英文原版页码**，供按索引与注释回查原书
- 索引：中文词条 + 英文原词，按拼音排序，**页码沿用原版页码**
