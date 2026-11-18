# Zaczyn library

Optional skills for specific kinds of work. Each is one self-contained `SKILL.md`, independent of the five Zaczyn base skills and of each other: install only what you need. Names describe the work, without a `zaczyn-` prefix.

| Shelf | Skill | What it gives you |
|---|---|---|
| Everyday | [notes-to-brief](notes-to-brief/SKILL.md) | A brief from scattered notes, transcripts, or documents, with stated facts, decisions, actions, assumptions, open questions, and contradictions kept apart and pointed to their sources |
| Testers | [test-charter](test-charter/SKILL.md) | An exploratory test charter or a list of checks from a specification, story, or change |
| Testers | [release-readiness-note](release-readiness-note/SKILL.md) | A one-page readiness note that labels every result by how it is known and leaves the decision to its owner |

## Install

- **App with skill folders** (Claude Code, Codex, Antigravity, Kiro, GitHub Copilot in VS Code): copy the skill's folder into the folder your app reads skills from, next to any Zaczyn skills.
- **App that accepts one uploaded file** (for example a browser assistant): upload the skill's `SKILL.md` on its own.
- **Anything else:** attach or paste the `SKILL.md` and say “Read this file in full and follow it for <task>.”

Each skill works without the base skills. If the base is installed, use zaczyn-review to check what a library skill produced.

## Status

These skills pass the same frontmatter and self-containment checks as the base. Each was tried once by a model reading it explicitly; no host has discovered them natively yet, and no real user has tried them. See [verification](../docs/verification.md).

To propose another skill, bring a real example of the work it would help with; see [contribution guidance](../CONTRIBUTING.md).
