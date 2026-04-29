# paper-aigc-revision-skill

这是一个可安装的 Agent Skill，不是普通脚本项目。

它面向中文论文场景，用于合规解读 AIGC 检测报告、定位高风险段落、补强作者研究痕迹、核验引用，并生成可解释的修订记录与 AI 使用披露草稿。

仓库地址：

- GitHub: [Gray878/paper-aigc-revision-skill](https://github.com/Gray878/paper-aigc-revision-skill)

## 这是什么 Skill

`chinese-paper-aigc-revision` 是一个面向 Codex、Claude Code、GitHub Copilot 等 agent 运行时的可复用 skill。

它的安装入口是：

```text
skills/chinese-paper-aigc-revision/SKILL.md
```

安装后，agent 可以通过 `Use $chinese-paper-aigc-revision ...` 这种方式调用它。

## Skill 能做什么

- 解读中文论文 AIGC 检测报告，包括知网、维普、万方、Turnitin 等常见报告字段。
- 识别高风险表达背后的真实问题，如模板化综述、弱证据、方法细节缺失、引用堆砌、风格过度均匀等。
- 不是“洗稿”或“绕过检测”，而是把“降 AIGC”转成合规的原创性重建：补真实材料、重建论证链、保留作者责任。
- 生成多平台发布包，包括 Claude ZIP、Codex/OpenAI Agent Skills ZIP、ChatGPT/GPTs instructions kit 和 release manifest。

## 仓库结构

本仓库遵循 Agent Skills 的标准目录结构，核心是一个可安装的 `SKILL.md`：

```text
skills/chinese-paper-aigc-revision/SKILL.md
```

关键文件：

- `skills/chinese-paper-aigc-revision/SKILL.md`: skill 主入口，定义名称、触发描述和执行流程。
- `skills/chinese-paper-aigc-revision/references/`: 检测逻辑、平台报告处理、改写模板、来源追溯等参考资料。
- `skills/chinese-paper-aigc-revision/scripts/build_release.py`: 生成多平台发布产物。
- `dist/`: 构建后的 ZIP、instructions 和校验清单。

## 安装方式

### 1. 从 GitHub 安装到 Codex

这里用的是 `npx`，不是 `ngx`：

```bash
npx skills add Gray878/paper-aigc-revision-skill --skill chinese-paper-aigc-revision -a codex -g
```

如果想安装到当前项目作用域，而不是全局：

```bash
npx skills add Gray878/paper-aigc-revision-skill --skill chinese-paper-aigc-revision -a codex
```

### 2. 从 GitHub 安装到 Claude Code

```bash
npx skills add Gray878/paper-aigc-revision-skill --skill chinese-paper-aigc-revision -a claude-code -g
```

### 3. 使用 GitHub CLI 安装

`gh skill` 当前是 GitHub CLI 的预览功能，命令可能随版本调整：

```bash
gh skill install Gray878/paper-aigc-revision-skill chinese-paper-aigc-revision --agent codex --scope user
```

安装到 Claude Code：

```bash
gh skill install Gray878/paper-aigc-revision-skill chinese-paper-aigc-revision --agent claude-code --scope user
```

### 4. 本地仓库测试安装

克隆仓库后，可以直接从本地目录安装：

```bash
npx skills add ./skills/chinese-paper-aigc-revision -a codex -g
```

或者从整个仓库安装：

```bash
gh skill install . chinese-paper-aigc-revision --from-local --agent codex --scope user
```

### 5. ChatGPT / GPTs

自定义 GPT 目前不支持通过 CLI 直接安装 Agent Skill，所以这里走的是“instructions kit”而不是“直接安装 skill”。请使用 `dist/` 里的 ChatGPT kit：

- `dist/chinese-paper-aigc-revision-chatgpt-kit.zip`
- `dist/chatgpt-gpts-instructions.md`

把 `chatgpt-gpts-instructions.md` 内容填入 GPT Instructions，再把 `references/` 下的知识文件作为 Knowledge 上传即可。

## 使用方式

安装完成后，可以这样触发：

```text
Use $chinese-paper-aigc-revision to interpret my Chinese thesis AIGC report, diagnose the high-risk sections, and revise them ethically with citation checks and disclosure notes.
```

也可以直接用中文：

```text
使用 chinese-paper-aigc-revision 处理我的中文论文 AIGC 检测报告。请先解读报告字段，再逐段诊断高风险原因，最后给出合规修订稿、需要我补充的材料和学术诚信检查清单。
```

建议一次性提供这些输入：

- 论文题目、学科、学历层次。
- 学校、学院或期刊关于 AIGC/AI 辅助写作的要求。
- AIGC 检测报告截图、文字版或标红片段。
- 被判高风险的原文段落。
- 你自己的真实研究材料，如数据、案例、访谈、实验、阅读笔记、参考文献。

## 设计边界

这个 skill 不做以下事情：

- 不承诺“降到某个百分比”“通过检测”“检测不出来”。
- 不编造数据、引用、访谈、案例、实验或政策条文。
- 不提供隐藏字符、错别字污染、翻译循环、同义洗稿等绕检技巧。

它会做的是：

- 把“降 AIGC”转成“补真实材料、重建证据链、恢复作者表达、准备披露说明”。
- 把高风险片段从“换个说法”升级成“能解释为什么这段话属于作者自己的研究判断”。

## 发布与构建

重新生成所有发布产物：

```bash
python skills/chinese-paper-aigc-revision/scripts/build_release.py
```

生成结果位于 `dist/`，包括：

- `chinese-paper-aigc-revision-claude.zip`
- `chinese-paper-aigc-revision-openai-codex.zip`
- `chinese-paper-aigc-revision-chatgpt-kit.zip`
- `chatgpt-gpts-instructions.md`
- `install-snippets.md`
- `release-manifest.json`

其中 `release-manifest.json` 包含 SHA256 校验信息，方便校验产物是否一致。

## 参考依据

skill 的检测逻辑、平台说明和来源追溯已整理在：

- `skills/chinese-paper-aigc-revision/references/detection-logic.md`
- `skills/chinese-paper-aigc-revision/references/platform-report-guide.md`
- `skills/chinese-paper-aigc-revision/references/rewrite-patterns.md`
- `skills/chinese-paper-aigc-revision/references/sources.md`

其中包含：

- DetectGPT
- GLTR
- LLM-generated text detection survey
- Turnitin AI writing detection guide
- 中文论文检测平台公开说明
- 《学术出版中 AIGC 使用边界指南 3.0》

## 适用对象

- 本科、硕士、博士中文论文作者。
- 需要处理学校 AIGC 报告的学生或导师。
- 想把“AI 润色”转成“合规原创性修订”的写作辅助场景。

## 说明

本仓库目前以 GitHub 分发为主。若后续技能发现站或 registry 形式更新，推荐仍以 GitHub 仓库内容和 release 产物为准。
