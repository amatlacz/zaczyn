# Claude Adapter

Expresses the Zaczyn core as native Claude artifacts:

- `core/intake/SKILL.md` and `core/scaffolder/SKILL.md` follow the Claude skill format (YAML frontmatter + Markdown body) and can be installed directly in Claude Code / Cowork.

## First step: install the skills

Claude Code and Cowork only discover skills under `.claude/skills/<name>/SKILL.md`; Zaczyn keeps them in `core/` for portability, so **you must install them once after cloning** or they won't appear when you type `/`.

**macOS / Linux** — symlink `core/` into `.claude/skills/` (single source of truth, no copies to drift):

```bash
mkdir -p .claude/skills
ln -sfn ../../core/intake     .claude/skills/zaczyn-intake
ln -sfn ../../core/scaffolder .claude/skills/zaczyn-scaffolder
```

**Windows (or if symlinks aren't available)** — copy the skill folders instead:

```powershell
mkdir .claude\skills
xcopy /E /I core\intake     .claude\skills\zaczyn-intake
xcopy /E /I core\scaffolder .claude\skills\zaczyn-scaffolder
```

Then **restart Claude Code** (skill discovery runs at startup). Typing `/` should now list `zaczyn-intake` and `zaczyn-scaffolder`, or you can just say *"help me set up my project"* to trigger the intake.

> This install is local-only — `.claude/skills/` is git-ignored so your machine-specific setup never gets committed.

- Context files: `agents.md` at project root (Claude Code), `PROJECT.md` referenced from the working folder (Cowork).
- Both tools can target the **same project root** — the multi-track pattern assumes it.

Adapters for other tools are welcome: keep the core untouched, translate only the packaging. See CONTRIBUTING.md.
