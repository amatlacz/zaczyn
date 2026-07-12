# Zaczyn — Concept Document

> **Zaczyn** *(say: "ZAH-chin"; Polish for sourdough starter)* — a sourdough starter for AI agent projects.
>
> Session 01: 2026-07-12 · Adam Matłacz + Claude · Status: concept locked, ready for repo skeleton

---

## 1. What it is

A clonable starter kit that turns a blank agent workspace (Claude Cowork, Claude Code, and similar) into a well-structured project — **by interviewing the user instead of assuming they already know what to ask for.**

**The problem:** agent tools ship raw capabilities (like a generic skill-creator), but beginners are at the "don't know what they don't know" stage — they can't see the potential, and when they try, they misuse it. The capability isn't too generic; it's *unrouted*.

**The core mechanism:** the intake interview is the front door; the **routing table** behind it — curated, opinionated mappings from "what kind of work is this?" to a full setup (folder structure, context files, recommended frameworks/MCPs/skills) — is the actual product.

Like a sourdough starter: you clone the living base, feed it your own flour, and grow your own bread.

## 2. Decisions

| # | Decision |
|---|----------|
| D1 | **Audiences:** software testers + startup founders. Framework general, customized via packs. |
| D2 | **Claude-first for v1**, architected for later portability. |
| D3 | **Distribution:** GitHub repo. |
| D4 | **Fully open source**, collaboration-friendly, modeled on spec-kit. Monetization = the human (trainings, consulting, custom packs as services), not the files. |
| D5 | **License: MIT.** DCO for contributions (no CLA). |
| D6 | **Name: Zaczyn.** Tagline: *"a sourdough starter for AI agent projects."* |
| D7 | **Domain: zaczyn.dev** (register zaczyn.io as backup). |

## 3. Architecture: core + packs + adapters

- **Core (portable):** all opinions in plain Markdown — intake questions, routing logic, folder conventions, context-file templates. No tool-specific syntax.
- **Packs (customization):** domain overlays — `tester-pack/`, `founder-pack/` — adding project types, vocabulary, and recommended MCPs/frameworks per audience. Kept in separate directories from day one.
- **Adapters (thin):** per-tool wrappers expressing the core as native artifacts — Claude skills + `agents.md` now; other tools' formats later. Porting = writing an adapter, not rewriting the framework.

## 4. The intake interview

Design principles: ask about the user's world, not our tech · deliverable over discipline · max 5 questions with concrete examples · every action narrates its *why*.

> **Q1. When this is done, what should exist that doesn't exist now?**
> a) Working software · b) A document · c) A presentation · d) Answers (research) · e) A repeatable helper for a recurring task · f) Not sure yet → fallback mini-dialog
>
> **Q2. One-time, or something you do repeatedly?** (recurring → Workflow route)
>
> **Q3. Where will the raw material come from?** (my files / the web / a system we use / my head) → drives MCP recommendations and `sources/` scaffolding
>
> **Q4. Who is the audience?** (me / my team / clients-investors-public) → drives tone notes and review steps
>
> **Q5. Will this produce more than one kind of deliverable?** (yes → multi-track workspace)
>
> **Q6. Is this a one-off, or the first instance of something you'll reuse?** (reusable → product/instance split)

## 5. Routing table (v0.2)

| Route | Trigger | Scaffold | Context files | Add-ons |
|---|---|---|---|---|
| **Build** | Q1=a | `specs/current/`, `src/`, `docs/` | `agents.md`, `specs/current/spec.md` | spec-kit; immutable-spec-history pattern |
| **Research** | Q1=d | `sources/`, `notes/`, `findings/` | `PROJECT.md`, living `findings/summary.md` | web-search MCP; source-logging convention |
| **Deck** | Q1=c | `content/`, `assets/`, `exports/` | `PROJECT.md` (+audience/tone), `content/outline.md` | pptx skill; content-before-design checklist |
| **Document** | Q1=b | `drafts/`, `sources/`, `final/` | `PROJECT.md` (+style notes) | docx/pdf skill; audience review loop |
| **Workflow** | Q1=e or Q2=recurring | `workflow/`, `examples/` | `workflow/task-description.md` (pre-filled from interview) | skill-creator, handed off *with context* |

**Universal base (every route):**

```
project-root/
├── PROJECT.md      # goal, audience, constraints, glossary — the "why"
├── DECISIONS.md    # append-only log of choices
├── scratch/        # licensed mess (see §6)
└── <route scaffold>
```

## 6. Workspace patterns

**Multi-track (Q5=yes).** One project producing several deliverable kinds gets one root, multiple tracks, and a `shared/` bridge:

```
project/
├── PROJECT.md          # single "why" — every track's agent reads it
├── DECISIONS.md
├── shared/             # canonical artifacts, owned by no track
├── <track-a>/          # e.g. app/ — Build route inside
└── <track-b>/          # e.g. workshop/ — Deck/Document route inside
```

Rules of the bridge: `shared/` is the single source of truth · tracks *reference* it, never copy · each track's context file explicitly points into `shared/`.

**Product/instance split (Q6=reusable).** A long-lived general product with concrete uses:

```
product/
├── app/ or core/       # the general, clean, long-lived part
├── templates/          # the contract: what every instance must provide
└── instances/
    └── 2026-conference-x/   # concrete, disposable-ish; own shared/, tracks, scratch/
```

Instance #2 = a new folder conforming to the contract, not a copy-paste marathon. `instances/` can be gitignored or split out later.

**Licensed mess: `scratch/`.** Fear of chaos is solved by zoning, not separation. Rules: anything goes · excluded from agents' canon (*"truth lives in `shared/`; never cite `scratch/` as decision"*) · optionally gitignored · promotion ritual: graduated ideas move to `shared/` + a line in DECISIONS.md.

## 7. Education layer

Beginners are at "don't know what they don't know" — so the scaffolding *is* the curriculum:

1. **Scaffold-and-explain:** every framework action narrates its why in plain language ("Creating `shared/` because your app and your slides both need the characters — prevents copy-pasting later").
2. **Field guide** (`docs/field-guide/`): what a skill is, when a task deserves one, and misuse patterns — skill-as-one-shot-prompt, skills too broad to trigger sensibly, write-once-never-iterate, skills-as-magic. Includes the pattern "avoiding structure out of fear of mess."
3. **Teachable moments over lectures:** guidance surfaces exactly when relevant (the Workflow route explains skills at the moment a recurring task justifies one).

## 8. Founding story (for the README)

Adam built a conference workshop with a companion app. The app (a general, reusable product) lived in a Claude Code repo with a spec-kit-like framework; the workshop content (exercises, character portraits, slides — a one-time instance) lived in a separate Cowork folder with custom skills. Content constantly fed between them, and with two disconnected workspaces Adam became the **human message bus** — manually copy-pasting artifacts neither agent could see.

The failure wasn't in either workflow; it was the missing setup: no shared root, no `shared/` bridge, no product/instance split, no `scratch/` zone to contain brainstorm mess. Zaczyn exists so the next person's first evening isn't spent as a highly overqualified clipboard.

## 9. Community setup

- `LICENSE` (MIT), `CONTRIBUTING.md` (how to propose a pack, a routing rule, a template), `CODE_OF_CONDUCT.md`
- **DCO** sign-offs for contributions (no CLA)
- Issue templates: "suggest a project type," "suggest an MCP/framework for the routing table" — the community feeds the routing table

## 10. Open questions

1. Q1=f ("not sure yet") — design the fallback mini-dialog.
2. Pack boundaries — do packs change only interview vocabulary/examples, or also routes and scaffolds?
3. DECISIONS.md — automatic (agent appends) or a taught habit?
4. Persona dry runs passed (tester ×2, founder ×3, all routed cleanly) — needs testing against more real, messy requests.
