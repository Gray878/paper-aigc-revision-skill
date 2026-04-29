# Install Snippets

Version: 2.0.0

## GitHub repository install via npx

`npx`, not `ngx`:

```bash
npx skills add OWNER/REPO --skill chinese-paper-aigc-revision -a codex -g
```

Install from a local clone:

```bash
npx skills add ./skills/chinese-paper-aigc-revision -a codex -g
```

## GitHub CLI install

```bash
gh skill install OWNER/REPO chinese-paper-aigc-revision --agent codex --scope user
```

## Claude.ai

Upload `chinese-paper-aigc-revision-claude.zip` from Settings/Capabilities/Skills. The ZIP contains the `chinese-paper-aigc-revision/` directory with `SKILL.md` at its root.

## Claude Code

Unzip `chinese-paper-aigc-revision-claude.zip` into `.claude/skills/` so the final path is `.claude/skills/chinese-paper-aigc-revision/SKILL.md`.

## OpenAI Codex / Agent Skills

Unzip `chinese-paper-aigc-revision-openai-codex.zip` into `$CODEX_HOME/skills`, `%USERPROFILE%\.codex\skills`, or a project `.agents/skills/` directory supported by your client.

## ChatGPT / GPTs

Use `chinese-paper-aigc-revision-chatgpt-kit.zip`. Paste `chatgpt-gpts-instructions.md` into the GPT Instructions field and upload the included reference files as Knowledge when supported.

Custom GPTs do not currently support a CLI skill installer. For GPTs, use the instructions kit instead of `npx`.

## All Platforms

Use `chinese-paper-aigc-revision-all-platforms.zip` when sharing every artifact together. Verify checksums in `release-manifest.json` if integrity matters.
