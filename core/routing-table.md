# Zaczyn Routing Table (v0.2)

The heart of Zaczyn: interview answers → opinionated setup. Every recommendation carries a one-line *why* — recommendations without reasons don't belong here.

| Route | Trigger | Scaffold | Context files | Recommended add-ons (with why) |
|---|---|---|---|---|
| **Build** | Q1 = working software | `specs/current/`, `src/`, `docs/` | `agents.md`, `specs/current/spec.md` | [spec-kit](https://github.com/github/spec-kit) — spec-driven development keeps the agent aligned with intent; immutable spec history with `specs/current/` as living truth — you can always see what changed and why |
| **Research** | Q1 = answers/research | `sources/`, `notes/`, `findings/` | `PROJECT.md`, living `findings/summary.md` | web-search MCP — research needs fresh sources, not training-data memories; source-logging convention — every claim in findings links back to a source |
| **Deck** | Q1 = presentation | `content/`, `assets/`, `exports/` | `PROJECT.md` (+ audience & tone), `content/outline.md` | presentation skill of your tool — content-before-design: outline is approved before any slide is styled |
| **Document** | Q1 = document | `drafts/`, `sources/`, `final/` | `PROJECT.md` (+ style notes) | document skill of your tool; review loop matched to the Q4 audience — a report for investors gets a different bar than a note-to-self |
| **Workflow** | Q1 = repeatable helper, or Q2 = recurring | `workflow/`, `examples/` | `workflow/task-description.md` (pre-filled from the interview) | your tool's skill-creator, handed off **with the captured task context** — a beginner should never face a blank "what should this skill do?" |

## Adding an entry

Open an issue with the *suggest a routing entry* template, or a PR editing this file. Include: the trigger, what it adds to the scaffold, and the one-line why.
