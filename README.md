# Zaczyn

> *(say: "ZAH-chin" — Polish for sourdough starter)*
>
> **A sourdough starter for AI agent projects.**

Zaczyn is a clonable starter kit that turns a blank agent workspace (Claude Cowork, Claude Code, and similar tools) into a well-structured project — by **interviewing you** instead of assuming you already know what to ask for.

Like a sourdough starter: clone the living base, feed it your own flour, grow your own bread.

## Why this exists

Agent tools ship raw capabilities — a skill creator, an empty folder, a blinking cursor. If you're new to agents, you're at the *"don't know what you don't know"* stage: you can't see the potential, and when you try, it's easy to misuse. The capabilities aren't too generic. They're **unrouted**.

Zaczyn routes them. A short intake interview asks about *your* world — what should exist when we're done? one-off or recurring? where does the raw material live? — and maps your answers to a curated, opinionated setup: folder structure, context files for your agents, and recommended frameworks, MCP servers, and skills.

## The founding story

Zaczyn's author built a conference workshop with a companion app. The app — a general, reusable product — lived in one repo with a spec-driven development framework (similar to [spec-kit](https://github.com/github/spec-kit)). The workshop content — exercises, character portraits, slides, a one-time instance — lived in a separate folder with custom skills. Content constantly fed between them, and with two disconnected workspaces he became the **human message bus**: an evening spent manually copy-pasting artifacts that neither agent could see.

The failure wasn't in either workflow. It was the missing setup: no shared root, no `shared/` bridge between tracks, no product/instance split, no `scratch/` zone to contain the brainstorm mess. Zaczyn exists so *your* first evening isn't spent as a highly overqualified clipboard.

## How it works

1. **Clone** this repository (or copy it into your workspace).
2. **Run the intake** — point your agent at `core/intake/SKILL.md` and say "help me set up my project."
3. **Answer up to six plain-language questions.** No jargon; the routing table translates.
4. **Get a scaffolded workspace** — folders, `PROJECT.md`, `DECISIONS.md`, agent context files, and recommendations — with every step explained in plain language, because the scaffolding *is* the curriculum.

## Repository map

```
core/        the portable heart: intake skill, scaffolder, routing table, templates (plain Markdown)
packs/       audience overlays: tester-pack, founder-pack (vocabulary, examples, extra routes)
adapters/    thin per-tool wrappers (Claude today; your favorite tool tomorrow — PRs welcome)
docs/        concept document, field guide, brainstorm logs
```

## Status

Early. The concept is locked (see [docs/brainstorm/session-01.md](docs/brainstorm/session-01.md)); the skills are stubs growing into their final shape. Expect the glassware to be unpolished — feedback and real-world messy project stories are the most valuable contribution right now.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The fastest ways to help:
- **Suggest a project type** or **an entry for the routing table** (issue templates provided)
- Share a real "my workspace turned into chaos" story — failures design the fixes here
- Add a pack for your profession

## License

[MIT](LICENSE) — clone it, feed it, bake freely.
