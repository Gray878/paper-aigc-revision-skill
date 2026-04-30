# paper-aigc-revision-skill

[English](README.en.md)

用于中文论文 AIGC 报告复核与合规修订的 Agent Skill。

这个仓库不是应用程序或普通脚本库。核心文件是：

```text
skills/chinese-paper-aigc-revision/SKILL.md
```

## 功能

- 解读知网、维普、万方、Turnitin 等 AIGC 检测报告。
- 解释困惑度、突发度、概率秩、分类器等检测信号可能对应的文本问题。
- 定位高风险段落中的真实缺陷：模板化表达、弱证据、方法缺口、引用风险、逻辑跳跃、风格过度均匀。
- 将“降 AIGC”请求转为合规修订：补充真实研究材料、重建证据链、核验引用、保留作者责任。
- 生成修改依据、复核说明、AI 使用披露草稿和多平台发布包。

## 边界

这个 skill 不承诺检测分数，也不提供绕过检测的方法。

不会做：

- 隐藏字符、错别字污染、随机标点、翻译循环。
- 同义词洗稿、伪装“人类化”、按检测逻辑反向规避。
- 编造数据、访谈、实验、案例、政策条文或参考文献。

会做：

- 把 AIGC 分数当作复核线索，而不是学术不端结论。
- 把高风险表达还原为具体写作问题。
- 用用户提供的真实材料补强论文的论证链。
- 对无法核验的信息标注 `[待核验]`。

## 安装

安装到 Codex：

```bash
npx skills add Gray878/paper-aigc-revision-skill --skill chinese-paper-aigc-revision -a codex -g
```

安装到 Claude Code：

```bash
npx skills add Gray878/paper-aigc-revision-skill --skill chinese-paper-aigc-revision -a claude-code -g
```

从本地仓库安装：

```bash
npx skills add ./skills/chinese-paper-aigc-revision -a codex -g
```

如果使用 ChatGPT / GPTs，请使用 `dist/` 中的 instructions kit：

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
使用 chinese-paper-aigc-revision 处理我的中文论文 AIGC 检测报告。请先解释报告字段和检测信号，再逐段诊断高风险原因，最后给出合规修订稿、需要我补充的材料和学术诚信检查清单。
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

重新生成 `dist/` 中的 Claude、Codex、ChatGPT/GPTs 发布产物：

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

主要依据整理在 `skills/chinese-paper-aigc-revision/references/sources.md`，包括 GLTR、DetectGPT、LLM-generated text detection survey、Turnitin AI writing detection guide、中文 AIGC 检测平台说明和学术出版 AIGC 使用边界指南。
