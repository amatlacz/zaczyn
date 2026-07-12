# Claude Adapter

Expresses the Zaczyn core as native Claude artifacts:

- `core/intake/SKILL.md` and `core/scaffolder/SKILL.md` follow the Claude skill format (YAML frontmatter + Markdown body) and can be installed directly in Claude Code / Cowork.
- Context files: `agents.md` at project root (Claude Code), `PROJECT.md` referenced from the working folder (Cowork).
- Both tools can target the **same project root** — the multi-track pattern assumes it.

Adapters for other tools are welcome: keep the core untouched, translate only the packaging. See CONTRIBUTING.md.
