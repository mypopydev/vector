# 第六轮正文 A：盲审复核意见

## 覆盖范围

先独立逐段对照并按需逐句核读以下范围：`cn-book/0.译本说明.md`（按当前仓库文件核实陈述，不作英译对照）、`cn-book/1.名家推荐.md` ↔ `en/03_Reviews.md`、`cn-book/2.作者简介.md` ↔ 项目作者简介 `en/02_Halftitle.md`、`cn-book/3.献词.md` ↔ `en/04_Dedication.md`、`cn-book/4.序言.md` ↔ `en/08_Prolog.md`、`cn-book/5.第1章-代数的解放.md` ↔ `en/09_Chapter01.md`、`cn-book/6.第2章-微积分的登场.md` ↔ `en/10_Chapter02.md`。译本说明另参照当前 README、版权页源文及仓库文件状态核查。

盲审完成后才查看 `review/findings/round6-delta.md`，仅作当前改动背景核对。七条推荐语署名文本完整；“think symbolically”四处及相关“symbolic thinking”用语在上下文中的「符号化地思考／符号化思维」语法关系一致、语义相合。未发现其他实质性遗漏、增译或限定语丢失。

## 发现（按严重度排序）

### Critical

- cn-book/0.译本说明.md:11 | Critical | 事实／权利归属 | EN证据：en/06_Copyright.md:20,24,32 标明作者版权及复制许可要求，并说明部分转载材料的版权归属未能查明 | 当前CN：「原书的文字、插图与版式之著作权均归原作者 Robyn Arianrhod 及原出版社所有」 | 建议限定为：「原书文字、插图与版式的相关权利依版权页所列信息处理；其中部分插图素材的版权归属未能查明。」

### Moderate

- cn-book/5.第1章-代数的解放.md:145 | Moderate | 错字／表达 | EN证据：en/09_Chapter01.md:157 “The visualizability is obvious … as if it were the non-visualizable concept” | 当前CN：「这种可可视化性……那个不可可视化的概念本身」 | 建议将两处分别改为「可视化性」和「不可视化的概念」。
- cn-book/5.第1章-代数的解放.md:87 | Moderate | 语义清晰度／引文 | EN证据：en/09_Chapter01.md:87 “How square is my square?” | 当前CN：「我的正方形有多方？」中文不自然且难以理解所问量 | 建议改为「我的正方形边长是多少？」

### Minor

- cn-book/6.第2章-微积分的登场.md:18 | Minor | 冗余／精炼度 | EN证据：en/10_Chapter02.md:18 “Hamilton became a sensation” | 当前CN：「哈密顿顿时轰动一时」 | 建议改为「哈密顿顿时引起轰动」或「哈密顿顿时声名大噪」。

## 数量统计

| Critical | Moderate | Minor | 合计 |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 4 |

## 未解决／不确定项

- `cn-book/0.译本说明.md:6` 的「长期为大众读者写作」：现有作者简介只确认她为普通读者写数学与科学，并未给出持续年限；属缺少直接依据，不能据此判为事实错误。若无其他来源，可删「长期」。
- `cn-book/0.译本说明.md:6`、`cn-book/2.作者简介.md:4` 的 `Affiliate（兼职研究员）`：项目作者简介只写 `Affiliate`，没有定义其具体聘任身份；「兼职研究员」的对应关系无法由现有材料核实，暂列不确定而非错误。
- `cn-book/0.译本说明.md:11` 的「个人学习与交流用途／非商业」属于译者用途声明，README 有同样表述，但仓库无法证明实际使用情况；不作为源文翻译错误计数。
- `cn-book/2.作者简介.md` 其余履历表述均与 `en/02_Halftitle.md` 的现有作者简介相符；未发现可由项目材料确认的事实错误。
