# Zaczyn

*Say “ZAH-chin” — Polish for sourdough starter.*

**Build a way of working with AI that fits you. Start small, and grow it at your pace.**

Zaczyn is a starter for native AI agent workspaces, targeting Claude Code, Codex, Antigravity, and Kiro. It helps you set up a project, recurring professional workflow, or personal assistant. It asks useful questions, suggests possibilities you may not know to request, and helps turn your choices into working context, practices, and tools.

You do not need to know which skills or libraries to install. You explain your work; Zaczyn helps you explore the options and decide how far to go. Like a sourdough starter, the base stays small while what you make with it can grow.

## Download, install, and start

You need your AI app installed and working. Download the **0.5.1 package for that app** below; you do not need Git or Python to use it. GitHub's “Code → Download ZIP” contains the source repository, not these ready-to-install packages.

| App | Download | Installation guide | Verification |
|---|---|---|---|
| Claude Code | [Claude ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.5.1/zaczyn-0.5.1.zip) | [Claude guide](adapters/claude/README.md) | Bounded plugin, setup, and context checks |
| Codex | [Codex ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.5.1/zaczyn-codex-0.5.1.zip) | [Codex guide](adapters/codex/README.md) | Discovery, setup artifacts, and context checks |
| Antigravity | [Antigravity ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.5.1/zaczyn-antigravity-0.5.1.zip) | [Antigravity guide](adapters/antigravity/README.md) | Experimental; runtime unverified |
| Kiro | [Kiro ZIP](https://github.com/amatlacz/zaczyn/releases/download/v0.5.1/zaczyn-kiro-0.5.1.zip) | [Kiro guide](adapters/kiro/README.md) | Experimental; runtime unverified |

1. **Download and extract.** Keep the extracted package somewhere convenient, such as Downloads. Keep its folders complete.
2. **Install in your work environment.** Open or create your own work folder, such as “My workshops.” For Codex, open it in the app and give the agent the extracted package's README with this request: “Follow this README to install Zaczyn in my current work folder. Preserve my existing files.” It copies the four complete skills into `.agents/skills/`. For Antigravity or Kiro, follow the linked host guide. For Claude Code, use the terminal command below from your work folder.
3. **Start setup.** In Codex, start a fresh task in that same work folder and invoke `$zaczyn-setup`. In the Claude session, invoke `/zaczyn:zaczyn-setup`. Describe your work using the prompt below, then choose quick, guided, or deep. Setup saves your preferences and context before you choose whether to start a task.

Claude Code's terminal launch command (replace the example with your extracted framework folder):

```bash
claude --plugin-dir /absolute/path/to/extracted/zaczyn
```

This loads Zaczyn for that terminal session. Use the command again when starting another session; it does not configure a separate Claude app window.

First setup prompt:

> Help me customize this workspace for my work. Show me quick, guided, and deep setup options. Ask about my needs and suggest useful improvements before starting a task.

Your work stays in your own folder. Zaczyn saves `AGENTS.md` for working preferences and `PROJECT.md` for project facts; Claude Code also gets a `CLAUDE.md` pointer. Additional tools, templates, and procedures are added only when selected. Later, use work to plan or execute, review to assess a result, and grow to adjust your setup.

[START.md](START.md) provides more detail. The [release page](https://github.com/amatlacz/zaczyn/releases/tag/v0.5.1) includes checksum files and the optional chat edition. Read the [verification scope](docs/verification.md) for the exact tested versions and limitations. A source checkout is also usable through the Claude plugin path; contributors can build every package locally.

## Choose your depth

| Depth | What happens |
|---|---|
| Quick | A short exchange, essential context, and a small recommendation. Aim for roughly two minutes for a simple setup. |
| Guided | Explore responsibilities, recurring work, existing tools and material, then choose useful improvements. |
| Deep | Develop a richer professional or personal assistant in resumable sessions, using selected background, examples, and specialist procedures. |

You can skip questions, stop, or deepen the setup later. An example task helps explain your needs; setup does not silently execute it. When ready, choose to start work, customize further, or stop. If you explicitly asked for setup followed by execution, it can proceed without asking again.

A tester might choose an issue-report checklist; a founder might choose an interview-synthesis procedure; an analyst might choose source-reconciliation checks. Your actual work determines the recommendation. There is no compulsory profession pack or default tool stack.

## Four intents

| Intent | Responsibility |
|---|---|
| [Setup](core/skills/zaczyn-setup/SKILL.md) | Discover needs, propose a personalized environment, and implement selected additions where supported. |
| [Work](core/skills/zaczyn-work/SKILL.md) | Plan, execute, pause, resume, and organize work using your selected practices. |
| [Review](core/skills/zaczyn-review/SKILL.md) | Check actual evidence, including artifacts with no prior task note. Review-only leaves the result unchanged. |
| [Grow](core/skills/zaczyn-grow/SKILL.md) | Add, revise, or remove practices as your needs develop, with appropriate checks and undo guidance. |

These are intents, not four mandatory phases. Planning and archiving do not require extra skills. Normal completion includes review; a pause keeps unfinished work open. A quick job needs no task note.

## Your setup belongs to you

For a new local workspace, Zaczyn saves:

- `AGENTS.md`: how the assistant should work and when to use your selected procedures.
- `PROJECT.md`: purpose, facts, material, and scope; unfinished setup can keep a short checkpoint here.
- Only the context wrapper required by your host. For Claude Code, `CLAUDE.md` imports `AGENTS.md`.

Long profiles, templates, skills, and task records appear only when they help. Existing workflows and legacy files stay authoritative until you choose a migration. See [migration and updates](docs/migration.md).

In a chat project, the equivalent documents are uploaded sources. Prepared text is not automatically saved: the assistant explains what to replace and how to continue in a new chat. Moving hosts is an explicit transfer of selected context, not automatic memory synchronization.

A rich assistant can have many skills and a long profile. Zaczyn keeps a concise index and consults relevant material when needed. It distinguishes suggestions, configured capabilities, and actual successful trials; a tool is never called installed merely because it was recommended.

[See a guided setup example](examples/guided-setup/README.md), [a small work record](examples/attendance-summary/README.md), or [learn what deserves a skill](docs/field-guide/what-is-a-skill.md).

## For contributors

The source clone is the contributor path. `core/` contains portable behavior; `adapters/` explains host differences; the builder generates native and chat editions from that source. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

To create the ZIPs from this checkout, run `python3 scripts/build_bundle.py`. Find them in `dist/`; generated downloads are not committed to the repository. Python 3.9 or newer is required for building, not for using the skills.

[MIT license](LICENSE).
