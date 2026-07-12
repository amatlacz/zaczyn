# Contributing to Zaczyn

Thanks for feeding the starter. 🍞

## The most valuable contributions right now

1. **Routing table entries** — "for project type X, recommend framework/MCP/skill Y because Z." Use the *suggest a routing entry* issue template.
2. **New project types** — a kind of work the intake doesn't recognize yet. Use the *suggest a project type* template.
3. **Real chaos stories** — Zaczyn's best features were designed from real workspace failures. Tell us how your project turned messy; open a plain issue.
4. **Packs** — an audience overlay for your profession (see `packs/` for the shape).
5. **Adapters** — express the core for a tool we don't cover yet (see `adapters/claude/`).

## Ground rules

- **Core stays portable.** Plain Markdown, no tool-specific syntax in `core/`. Tool syntax belongs in `adapters/`.
- **Opinions need reasons.** Every routing recommendation includes a one-line *why* — the scaffolding is the curriculum.
- **Beginner-readable.** If a green user can't understand the sentence, rewrite the sentence.

## Sign-off (DCO)

We use the [Developer Certificate of Origin](https://developercertificate.org/). Add a sign-off line to your commits:

```
git commit -s -m "Add routing entry for data-analysis projects"
```

That's it — no CLA, no paperwork.
