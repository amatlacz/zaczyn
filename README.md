# Zaczyn

*Say “ZAH-chin” — Polish for sourdough starter.*

**Build a way of working with AI that fits you. Start small, and grow it at your pace.**

Zaczyn is a starter for AI agent workspaces, targeting Claude Code, Codex, Antigravity, and Kiro, with drafts for GitHub Copilot in VS Code and, through single-file skills, Microsoft Copilot and other browser assistants. It helps you set up a project, recurring professional workflow, or personal assistant. It asks useful questions, suggests possibilities you may not know to request, and helps turn your choices into working context, practices, and tools.

You do not need to know which skills or libraries to install. You explain your work; Zaczyn helps you explore the options and decide how far to go. Like a sourdough starter, the base stays small while what you make with it can grow.

## Download, install, and start

You need your AI app installed and working. Download the **0.7.0 package for that app** below; you do not need Git or Python to use it. GitHub's “Code → Download ZIP” contains the source repository, not these ready-to-install packages (the only exception is the optional [host probe](probe/README.md), which says when to use it).

| App | Download | Installation guide | How well tested |
|---|---|---|---|
| Claude Code (one project, desktop or terminal) | [Claude project ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.7.0/zaczyn-claude-project-0.7.0.zip) | [Project-only guide](adapters/claude-project/README.md) | Package checks; earlier plugin/setup evidence; desktop install unverified |
| Codex | [Codex ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.7.0/zaczyn-codex-0.7.0.zip) | [Codex guide](adapters/codex/README.md) | Discovery, setup artifacts, and context checks |
| Antigravity | [Antigravity ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.7.0/zaczyn-antigravity-0.7.0.zip) | [Antigravity guide](adapters/antigravity/README.md) | Experimental; runtime unverified |
| Kiro | [Kiro ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.7.0/zaczyn-kiro-0.7.0.zip) | [Kiro guide](adapters/kiro/README.md) | Experimental; runtime unverified |
| GitHub Copilot in VS Code | [VS Code ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.7.0/zaczyn-vscode-copilot-0.7.0.zip) | [VS Code guide](adapters/vscode-copilot/README.md) | Draft; not yet confirmed |
| Microsoft Copilot (Cowork, Chat) and other browser assistants | [Single-file ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.7.0/zaczyn-single-0.7.0.zip) | [Microsoft 365 guide](adapters/microsoft-365/README.md), [single-file guide](adapters/single-file/README.md) | Draft; not yet confirmed |

1. **Download and extract.** Keep all files together. For an existing project folder named `XYZ`, rename the extracted folder `zaczyn-install` and copy it into `XYZ`. You should now have `XYZ/zaczyn-install/README.md` and `XYZ/zaczyn-install/skills/`.
2. **Install for that project.** Open `XYZ` itself in your AI app as a local project and send: “Read zaczyn-install/README.md and install Zaczyn for this project only. Preserve my existing files and settings. Do not install globally or start setup yet.” For Claude Code, this copies five complete skill folders to `XYZ/.claude/skills/`; Codex uses `XYZ/.agents/skills/`. The package's README provides the exact host-specific rules.
3. **Start setup.** Start a fresh local conversation in `XYZ`. In Claude Code, type `/zaczyn-setup` in the message box and select it. In Codex, use `$zaczyn-setup`. These are messages in your app, not terminal commands. Add the setup prompt below.

This installation is scoped to `XYZ` and its relevant subdirectories. It does not install Zaczyn for your account or unrelated projects. Once the five complete skill folders are installed, `zaczyn-install` is no longer needed by the skills and can be moved out of your project. For terminal users who prefer plugins, the [Claude guide](adapters/claude/README.md) retains the alternative `--plugin-dir` path.

First setup prompt:

> Quick setup: I want help with <one sentence about your work>. Ask only what you still need, then save my setup.

For more questions and suggestions, ask for a guided or deep setup instead.

Your work stays in your own folder. Zaczyn saves `AGENTS.md` for working preferences and `PROJECT.md` for project facts; Claude Code also gets a `CLAUDE.md` pointer. Additional tools, templates, and procedures are added only when selected. Later, use work to plan or execute, review to assess a result, and grow to adjust your setup.

[START.md](START.md) provides more detail. The [release page](https://github.com/amatlacz/zaczyn/releases/tag/v0.7.0) includes checksum files and the optional chat edition. Fresh-install execution of the new orchestration skill in supported hosts remains unverified. Read the [host capability guide](adapters/orchestration.md) and [verification scope](docs/verification.md) for the exact tested versions and limitations. A source checkout is also usable through the Claude plugin path; contributors can build every package locally.

## Choose your depth

| Depth | What happens |
|---|---|
| Quick | A short exchange, essential context, and a small recommendation. Aim for roughly two minutes for a simple setup. |
| Guided | Explore responsibilities, recurring work, existing tools and material, then choose useful improvements. |
| Deep | Develop a richer professional or personal assistant in resumable sessions, using selected background, examples, and specialist procedures. |

You can skip questions, stop, or deepen the setup later. An example task helps explain your needs; setup does not silently execute it. When ready, choose to start work, customize further, or stop. If you explicitly asked for setup followed by execution, it can proceed without asking again.

A tester might choose an issue-report checklist; a founder might choose an interview-synthesis procedure; an analyst might choose source-reconciliation checks. Your actual work determines the recommendation. There is no compulsory profession pack or default tool stack.

## Five intents

| Intent | Responsibility |
|---|---|
| [Setup](core/skills/zaczyn-setup/SKILL.md) | Discover needs, propose a personalized environment, and implement selected additions where supported. |
| [Work](core/skills/zaczyn-work/SKILL.md) | Plan, execute, pause, resume, and organize work using your selected practices. |
| [Review](core/skills/zaczyn-review/SKILL.md) | Check actual evidence, including artifacts with no prior task note. Review-only leaves the result unchanged. |
| [Grow](core/skills/zaczyn-grow/SKILL.md) | Add, revise, or remove practices as your needs develop, with appropriate checks and undo guidance. |
| [Orchestrate](core/skills/zaczyn-orchestrate/SKILL.md) | On an explicit cost-aware orchestration request, route bounded work through available agents or workflows and integrate the result. |

These are independent intents, not five mandatory phases. Orchestrate applies only when named or explicitly requested for cost-aware orchestration, and only for that task. Planning and archiving do not require extra skills. Normal completion includes review; a pause keeps unfinished work open. A quick job needs no task note.

For example, select the strongest available model with high reasoning effort where your host offers it, then ask: “`$zaczyn-orchestrate` complete this task using cost-aware delegation” in Codex, or use `/zaczyn-orchestrate` in a Claude Code project (`/zaczyn:zaczyn-orchestrate` with the Claude plugin). The host's normal permissions still apply; there is no separate approval step for each agent.

## Your setup belongs to you

For a new local workspace, Zaczyn saves:

- `AGENTS.md`: how the assistant should work and when to use your selected procedures.
- `PROJECT.md`: purpose, facts, material, and scope; unfinished setup can keep a short checkpoint here.
- Only the context wrapper required by your host. For Claude Code, `CLAUDE.md` imports `AGENTS.md`.

Long profiles, templates, skills, and task records appear only when they help. Existing workflows and legacy files stay authoritative until you choose a migration. See [migration and updates](docs/migration.md).

In a chat project, the equivalent documents are uploaded sources. Prepared text is not automatically saved: the assistant explains what to replace and how to continue in a new chat. Moving hosts is an explicit transfer of selected context, not automatic memory synchronization.

A rich assistant can have many skills and a long profile. Zaczyn keeps a concise index and consults relevant material when needed. It distinguishes suggestions, configured capabilities, and actual successful trials; a tool is never called installed merely because it was recommended.

[See a guided setup example](examples/guided-setup/README.md), [a small work record](examples/attendance-summary/README.md), or [learn what deserves a skill](docs/field-guide/what-is-a-skill.md). Field guide: [your first own skill](docs/field-guide/first-own-skill.md), [keep the context clean](docs/field-guide/context-hygiene.md), [check what your app actually loads](docs/field-guide/check-your-app.md).

## Optional library

[library/](library/README.md) holds optional single-file skills for specific work, independent of the base: notes-to-brief (a sourced brief from scattered notes), test-charter, and release-readiness-note. Install only the ones you need; they are also in [one ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.7.0/zaczyn-library-0.7.0.zip).

## For contributors

The source clone is the contributor path. `core/` contains portable behavior; `adapters/` explains host differences; the builder generates native and chat editions from that source. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

To create the ZIPs from this checkout, run `python3 scripts/build_bundle.py`. Find them in `dist/`; generated downloads are not committed to the repository. Python 3.9 or newer is required for building, not for using the skills.

[MIT license](LICENSE).
