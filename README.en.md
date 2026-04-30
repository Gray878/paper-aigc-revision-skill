# paper-aigc-revision-skill

[中文](README.md)

An Agent Skill for reviewing Chinese academic-paper AIGC reports and revising high-risk sections in an academically responsible way.

This repository is not an app or a general-purpose script package. The installable skill starts here:

```text
skills/chinese-paper-aigc-revision/SKILL.md
```

## What It Does

- Interprets AIGC reports from CNKI, VIP, Wanfang, Turnitin, and similar systems.
- Explains detection signals such as perplexity, burstiness, probability ranks, probability curvature, classifiers, and report artifacts.
- Diagnoses the real writing problems behind high-risk passages: generic claims, template structure, weak evidence, method gaps, citation risk, logic jumps, and overly uniform style.
- Turns "lower my AIGC score" requests into compliant revision work: add real research material, rebuild evidence chains, verify citations, and preserve author responsibility.
- Produces revision rationales, review notes, AI-use disclosure drafts, and release packages for multiple agent platforms.

## Boundaries

This skill does not promise detection scores and does not provide detector-evasion methods.

It will not:

- Add hidden characters, typo noise, random punctuation, or translation loops.
- Rewrite text as detector evasion, "humanize" text to hide AI use, or reverse-engineer detection logic.
- Fabricate data, interviews, experiments, cases, policy text, or references.

It will:

- Treat AIGC scores as review signals, not misconduct conclusions.
- Translate high-risk signals into concrete writing and evidence problems.
- Strengthen the paper with user-provided research material.
- Mark unverifiable information as `[待核验]`.

## Installation

Install for Codex:

```bash
npx skills add Gray878/paper-aigc-revision-skill --skill chinese-paper-aigc-revision -a codex -g
```

Install for Claude Code:

```bash
npx skills add Gray878/paper-aigc-revision-skill --skill chinese-paper-aigc-revision -a claude-code -g
```

Install from a local clone:

```bash
npx skills add ./skills/chinese-paper-aigc-revision -a codex -g
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
使用 chinese-paper-aigc-revision 处理我的中文论文 AIGC 检测报告。请先解释报告字段和检测信号，再逐段诊断高风险原因，最后给出合规修订稿、需要我补充的材料和学术诚信检查清单。
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

Regenerate the Claude, Codex, and ChatGPT/GPTs artifacts in `dist/`:

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

The source map is maintained in `skills/chinese-paper-aigc-revision/references/sources.md`. It includes GLTR, DetectGPT, LLM-generated text detection surveys, the Turnitin AI writing detection guide, public notes from Chinese AIGC detection platforms, and academic publishing guidance on responsible AIGC use.
