# chinese-paper-aigc-revision

Agent Skill for ethically revising Chinese academic papers with AIGC report interpretation, citation checks, author-evidence reconstruction, and disclosure support.

## Repository layout

This repository follows the Agent Skills convention expected by GitHub and common skills CLIs:

```text
skills/chinese-paper-aigc-revision/SKILL.md
```

## Install from GitHub

Use `npx`, not `ngx`.

Install to Codex globally:

```bash
npx skills add OWNER/REPO --skill chinese-paper-aigc-revision -a codex -g
```

Install to Claude Code globally:

```bash
npx skills add OWNER/REPO --skill chinese-paper-aigc-revision -a claude-code -g
```

Install with GitHub CLI:

```bash
gh skill install OWNER/REPO chinese-paper-aigc-revision --agent codex --scope user
```

## Local testing

Install from a local clone:

```bash
npx skills add ./skills/chinese-paper-aigc-revision -a codex -g
```

Or install from the whole repository:

```bash
gh skill install . chinese-paper-aigc-revision --from-local --agent codex --scope user
```

## Release artifacts

Build packaged outputs:

```bash
python skills/chinese-paper-aigc-revision/scripts/build_release.py
```

Artifacts are written to `dist/`, including:

- Claude upload ZIP
- Codex/OpenAI Agent Skills ZIP
- ChatGPT/GPTs instructions kit
- Release manifest with SHA256 checksums

## ChatGPT / GPTs note

Custom GPTs do not currently support installing Agent Skills from a CLI command. Use the generated instructions kit in `dist/` for GPTs instead.
