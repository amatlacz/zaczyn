# Zaczyn

*Say “ZAH-chin” — Polish for sourdough starter.*

**Build a way of working with AI that fits you. Start small, and grow it at your pace.**

Zaczyn is a starter for native AI agent workspaces, targeting Claude Code, Codex, Antigravity, and Kiro. It helps you set up a project, recurring professional workflow, or personal assistant. It asks useful questions, suggests possibilities you may not know to request, and helps turn your choices into working context, practices, and tools.

You do not need to know which skills or libraries to install. You explain your work; Zaczyn helps you explore the options and decide how far to go. Like a sourdough starter, the base stays small while what you make with it can grow.

## Start in the app you use

Start with [START.md](START.md) for your actual agent environment:

| Your environment | Current delivery status |
|---|---|
| Claude Code | Native plugin loaded into a terminal session; setup and owner-reported fresh-session context recovery checked in bounded cases. |
| [Codex](adapters/codex/README.md) | Four workspace skills discovered; owner quick-setup artifacts reviewed and fresh-session context recovery checked. |
| [Antigravity](adapters/antigravity/README.md) and [Kiro](adapters/kiro/README.md) | Experimental workspace packages and guides; package integrity checked, actual host behavior unverified. |

Version 0.5 provides a Claude plugin plus separate native skill ZIPs for Codex, Antigravity, and Kiro. Each exported skill carries its own linked resources, so importing one folder keeps them intact. Codex and Antigravity can share the same installed skill files. Your work and customizations live in your own workspace. A source checkout can also load the Claude plugin directly. There is no need to upload project files to a browser to follow the native path.

[Adapters](adapters/README.md) explain current support and the explicit-read fallback. The optional chat edition and Cowork path remain available separately. Local ZIPs are prepared artifacts, not a published release. See [verification scope](docs/verification.md) for exact evidence and limits.

Start by saying:

> Help me set this up for my work. I want to understand what AI could help with and choose how much to customize before we start a task.

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
