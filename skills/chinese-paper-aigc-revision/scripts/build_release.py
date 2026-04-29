from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


VERSION = "2.0.0"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def skill_files(skill_dir: Path):
    ignored = {"__pycache__", ".DS_Store"}
    for path in sorted(skill_dir.rglob("*")):
        if any(part in ignored for part in path.parts):
            continue
        if path.is_file():
            yield path


def write_skill_zip(skill_dir: Path, output: Path) -> None:
    if output.exists():
        output.unlink()
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for path in skill_files(skill_dir):
            archive.write(path, path.relative_to(skill_dir.parent).as_posix())


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    marker = text.find("\n---", 3)
    if marker == -1:
        return text
    return text[marker + 4 :].lstrip()


def build_chatgpt_instructions(skill_dir: Path, output: Path) -> None:
    skill_md = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    references = [
        "references/detection-logic.md",
        "references/platform-report-guide.md",
        "references/revision-playbook.md",
        "references/rewrite-patterns.md",
        "references/sources.md",
    ]
    parts = [
        "# ChatGPT/GPTs Instructions Kit",
        "",
        "Paste the following instructions into a GPT's Instructions field. Upload the files in `references/` as Knowledge when the product supports file knowledge. Keep the academic-integrity boundaries intact.",
        "",
        "## Core Instructions",
        "",
        strip_frontmatter(skill_md),
        "",
        "## Knowledge File Map",
    ]
    for rel in references:
        parts.append(f"- `{rel}`")
    parts.extend(["", "## Bundled Reference Content"])
    for rel in references:
        parts.extend(["", f"### {rel}", "", (skill_dir / rel).read_text(encoding="utf-8")])
    output.write_text("\n".join(parts), encoding="utf-8")


def build_install_snippets(dist_dir: Path, output: Path) -> None:
    text = f"""# Install Snippets

Version: {VERSION}

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

Unzip `chinese-paper-aigc-revision-openai-codex.zip` into `$CODEX_HOME/skills`, `%USERPROFILE%\\.codex\\skills`, or a project `.agents/skills/` directory supported by your client.

## ChatGPT / GPTs

Use `chinese-paper-aigc-revision-chatgpt-kit.zip`. Paste `chatgpt-gpts-instructions.md` into the GPT Instructions field and upload the included reference files as Knowledge when supported.

Custom GPTs do not currently support a CLI skill installer. For GPTs, use the instructions kit instead of `npx`.

## All Platforms

Use `chinese-paper-aigc-revision-all-platforms.zip` when sharing every artifact together. Verify checksums in `release-manifest.json` if integrity matters.
"""
    output.write_text(text, encoding="utf-8")


def build_chatgpt_kit(skill_dir: Path, instructions: Path, output: Path) -> None:
    if output.exists():
        output.unlink()
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.write(instructions, "chatgpt-gpts-instructions.md")
        for path in sorted((skill_dir / "references").glob("*.md")):
            archive.write(path, f"references/{path.name}")


def build_all_platforms(files: list[Path], output: Path) -> None:
    if output.exists():
        output.unlink()
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.name)


def main() -> None:
    skill_dir = Path(__file__).resolve().parents[1]
    repo_dir = skill_dir.parent.parent if skill_dir.parent.name == "skills" else skill_dir.parent
    dist_dir = repo_dir / "dist"
    dist_dir.mkdir(exist_ok=True)

    release_files: list[Path] = []

    claude_zip = dist_dir / "chinese-paper-aigc-revision-claude.zip"
    codex_zip = dist_dir / "chinese-paper-aigc-revision-openai-codex.zip"
    legacy_zip = dist_dir / "chinese-paper-aigc-revision.zip"
    for output in (claude_zip, codex_zip, legacy_zip):
        write_skill_zip(skill_dir, output)
        release_files.append(output)

    instructions = dist_dir / "chatgpt-gpts-instructions.md"
    build_chatgpt_instructions(skill_dir, instructions)
    release_files.append(instructions)

    install_snippets = dist_dir / "install-snippets.md"
    build_install_snippets(dist_dir, install_snippets)
    release_files.append(install_snippets)

    chatgpt_kit = dist_dir / "chinese-paper-aigc-revision-chatgpt-kit.zip"
    build_chatgpt_kit(skill_dir, instructions, chatgpt_kit)
    release_files.append(chatgpt_kit)

    manifest_path = dist_dir / "release-manifest.json"
    manifest = {
        "name": skill_dir.name,
        "version": VERSION,
        "date": date.today().isoformat(),
        "artifacts": [
            {
                "file": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in release_files
        ],
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    release_files.append(manifest_path)

    all_platforms = dist_dir / "chinese-paper-aigc-revision-all-platforms.zip"
    build_all_platforms(release_files, all_platforms)

    # Keep the external manifest authoritative. The manifest embedded inside the
    # all-platforms ZIP cannot contain a stable checksum of the ZIP that contains
    # itself, so add the bundle checksum only after creating the bundle.
    manifest["artifacts"].append(
        {
            "file": all_platforms.name,
            "bytes": all_platforms.stat().st_size,
            "sha256": sha256(all_platforms),
        }
    )
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(dist_dir)
    for artifact in manifest["artifacts"]:
        print(f"{artifact['file']} {artifact['sha256']}")


if __name__ == "__main__":
    main()
