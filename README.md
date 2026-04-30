# paper-aigc-revision-skill

[English](README.en.md)

一个帮中文论文降 AIGC、去“AI 味”的 Agent Skill。

它可以直接看论文，也可以结合检测报告一起处理。核心文件是：

```text
skills/chinese-paper-aigc-revision/SKILL.md
```

## 功能

- 看懂知网、维普、万方、Turnitin 等 AIGC 检测报告。
- 没有检测报告时，直接从论文文本里找“AI 味”重的地方。
- 识别常见问题：空话套话、模板化表达、证据不足、方法写得太空、引用关系不清、整段太平。
- 把段落改得更像作者自己写的：更具体、更有材料支撑、更有研究痕迹。
- 在需要时补充修改依据、复核说明和 AI 使用披露草稿。

## 边界

这个 skill 不是绕检测工具，不承诺具体分数。

不会做：

- 隐藏字符、错别字污染、随机标点、翻译循环。
- 同义词洗稿、伪装“人类化”、按检测逻辑反向规避。
- 编造数据、访谈、实验、案例、政策条文或参考文献。

会做：

- 把“降 AIGC”转成真正的论文优化。
- 把高风险表达拆成具体写作问题。
- 用你提供的真实材料补强论文内容。
- 对无法核验的信息标注 `[待核验]`。

## 安装

最简单的安装命令：

```bash
npx skills add Gray878/paper-aigc-revision-skill
```

如果你已经 clone 到本地，也可以：

```bash
npx skills add ./skills/chinese-paper-aigc-revision
```

如果要给 ChatGPT / GPTs 用，再看 `dist/` 里的 instructions kit：

```text
dist/chinese-paper-aigc-revision-chatgpt-kit.zip
dist/chatgpt-gpts-instructions.md
```

## 使用示例

英文调用：

```text
Use $chinese-paper-aigc-revision to interpret my Chinese thesis AIGC report, explain the detection signals, revise high-risk sections ethically, and prepare citation checks and disclosure notes.
```

中文调用：

```text
使用 chinese-paper-aigc-revision 帮我优化这篇中文论文，重点帮我降 AIGC、去 AI 味。请直接找出空话套话、模板化表达、证据不足、方法细节不够和风格过于均匀的地方，并给出修改稿、修改依据和需要我补充的真实材料。
```

建议同时提供：

- 论文题目、学科、学历层次或投稿类型。
- 学校、学院或期刊关于 AI 辅助写作的要求。
- AIGC 报告截图、文字版或标红片段。
- 被判高风险的原文段落。
- 真实研究材料：数据、案例、访谈、实验、阅读笔记、参考文献等。

## 目录

```text
skills/chinese-paper-aigc-revision/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── detection-logic.md
│   ├── platform-report-guide.md
│   ├── revision-playbook.md
│   ├── rewrite-patterns.md
│   └── sources.md
└── scripts/
    ├── build_release.py
    └── package_skill.py
```

## 构建发布包

重新生成 `dist/` 中的发布文件：

```bash
python skills/chinese-paper-aigc-revision/scripts/build_release.py
```

生成文件包括：

- `dist/chinese-paper-aigc-revision-claude.zip`
- `dist/chinese-paper-aigc-revision-openai-codex.zip`
- `dist/chinese-paper-aigc-revision-chatgpt-kit.zip`
- `dist/chatgpt-gpts-instructions.md`
- `dist/release-manifest.json`

## 参考资料

参考依据整理在 `skills/chinese-paper-aigc-revision/references/sources.md`，包括检测原理、平台说明和学术使用边界资料。
