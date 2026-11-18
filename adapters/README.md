# Choose your agent environment

Zaczyn runs where an assistant can follow a skill: native agent workspaces (Claude Code, Codex, Antigravity, Kiro, GitHub Copilot in VS Code) and, through single files, browser and office assistants such as Microsoft Copilot. One portable core defines behavior; each host needs an adapter for instruction loading, skill discovery, shared references, and file access.

- **Claude Code:** install `zaczyn-claude-project-0.7.0.zip` into one project through the [project-only guide](claude-project/README.md), including desktop sessions without a terminal. The [Claude guide](claude/README.md) retains an optional terminal plugin path. See [verification](../docs/verification.md) for what has been observed.
- **Codex:** use `zaczyn-codex-0.7.0.zip` and the [native workspace guide](codex/README.md). Discovery of the current build was observed in a clean folder.
- **Antigravity (experimental):** use `zaczyn-antigravity-0.7.0.zip` and the [native guide](antigravity/README.md). Actual host behavior is unverified.
- **Kiro (experimental):** use `zaczyn-kiro-0.7.0.zip` and the [native guide](kiro/README.md). Actual host behavior is unverified.
- **GitHub Copilot in VS Code (draft):** use `zaczyn-vscode-copilot-0.7.0.zip` and the [VS Code guide](vscode-copilot/README.md). Not yet confirmed in a working installation.
- **Microsoft Copilot, Cowork and Chat (draft):** use `zaczyn-single-0.7.0.zip` and the [Microsoft 365 guide](microsoft-365/README.md). Not yet confirmed in a working setup.
- **Any other app that reads one file:** the [single-file edition](single-file/README.md).

The exported skill files are identical across the workspace packages; only their guides differ. Each skill carries what it needs; installing one exported folder does not depend on another skill or the source checkout. Keep all five at the same version when updating.

## One copy per folder an app reads

Before installing, look in every folder the app reads and remove older Zaczyn copies: two versions side by side make the app pick one unpredictably or list a skill twice. Each skill's `VERSION` file names its build.

| App | Project folders it reads | Personal folders it reads |
|---|---|---|
| Claude Code | `.claude/skills` | `~/.claude/skills` |
| Codex | `.agents/skills` (up to the repository root) | `~/.agents/skills` |
| Antigravity | `.agents/skills` | `~/.gemini/config/skills` |
| Kiro | `.kiro/skills` | `~/.kiro/skills` |
| GitHub Copilot in VS Code | `.github/skills`; `.agents/skills` per VS Code's migration guide (`.claude/skills` only in VS Code's Claude harness and the deprecated Local harness) | `~/.copilot/skills`, `~/.agents/skills` |
| Microsoft Copilot Cowork | none; skills are uploaded or stored in OneDrive `Documents/Cowork/skills` | — |

For delegation and model controls, read the [orchestration host guide](orchestration.md). To check what an app actually loads, use [this three-question check](../docs/field-guide/check-your-app.md). Only observed behavior in the selected host establishes installation, resource access, and persistence.

## Optional editions

[Claude Cowork](claude/README.md) (Anthropic's desktop app, not Microsoft's Copilot Cowork) has a documented graphical upload path. [ChatGPT and other chat apps](chatgpt/README.md) can use the generated chat edition with manual context saving. [Grok guidance](other-hosts.md) remains staged.
