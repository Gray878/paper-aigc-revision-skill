# paper-aigc-revision-skill

[中文](README.md)

A skill for reducing AIGC risk and removing the "AI-sounding" feel from Chinese academic papers.

It can work from a detection report or directly from the paper text. The installable skill starts here:

```text
skills/chinese-paper-aigc-revision/SKILL.md
```

## What It Does

- Reads AIGC reports from CNKI, VIP, Wanfang, Turnitin, and similar systems.
- Works without a report by checking the paper text directly for heavy AI-sounding patterns.
- Finds common problems: generic claims, template phrasing, weak evidence, thin methods, unclear citation relationships, and overly even style.
- Rewrites passages so they feel more author-grounded, more specific, and better supported by real material.
- Produces revision notes, review explanations, and AI-use disclosure drafts when needed.

## Boundaries

This is not a detector-evasion tool and does not promise any score.

It will not:

- Add hidden characters, typo noise, random punctuation, or translation loops.
- Rewrite text as detector evasion, "humanize" text to hide AI use, or reverse-engineer detection logic.
- Fabricate data, interviews, experiments, cases, policy text, or references.

It will:

- Turn "lower my AIGC score" into real paper improvement work.
- Translate high-risk passages into concrete writing problems.
- Strengthen the paper with user-provided research material.
- Mark unverifiable information as `[待核验]`.

## Installation

Simplest install command:

```bash
npx skills add Gray878/paper-aigc-revision-skill
```

If you already cloned the repo locally:

```bash
npx skills add ./skills/chinese-paper-aigc-revision
```

For ChatGPT / GPTs, use the instructions kit in `dist/`:

```text
dist/chinese-paper-aigc-revision-chatgpt-kit.zip
dist/chatgpt-gpts-instructions.md
```

## Usage

English prompt:

```text
Use $chinese-paper-aigc-revision to interpret my Chinese thesis AIGC report, explain the detection signals, revise high-risk sections ethically, and prepare citation checks and disclosure notes.
```

Chinese prompt:

```text
使用 chinese-paper-aigc-revision 帮我优化这篇中文论文，重点帮我降 AIGC、去 AI 味。请直接找出空话套话、模板化表达、证据不足、方法细节不够和风格过于均匀的地方，并给出修改稿、修改依据和需要我补充的真实材料。
```

Useful inputs:

- Paper title, discipline, degree level, or submission type.
- School, department, or journal rules for AI-assisted writing.
- AIGC report screenshots, extracted text, or highlighted passages.
- Original passages marked as high risk.
- Real research material: data, cases, interviews, experiments, reading notes, and references.

## Layout

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

## Build Release Packages

Regenerate the release artifacts in `dist/`:

```bash
python skills/chinese-paper-aigc-revision/scripts/build_release.py
```

Generated files include:

- `dist/chinese-paper-aigc-revision-claude.zip`
- `dist/chinese-paper-aigc-revision-openai-codex.zip`
- `dist/chinese-paper-aigc-revision-chatgpt-kit.zip`
- `dist/chatgpt-gpts-instructions.md`
- `dist/release-manifest.json`

## References

The source map is maintained in `skills/chinese-paper-aigc-revision/references/sources.md`. It includes detection-method references, platform notes, and guidance on responsible academic AI use.
