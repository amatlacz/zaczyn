---
name: zaczyn-scaffolder
description: Create the folder structure and context files for a project after the Zaczyn intake has chosen a route. Use whenever a route decision exists (from zaczyn-intake or stated directly by the user) and the workspace needs folders, PROJECT.md, DECISIONS.md, agent context files, or the multi-track / product-instance / scratch patterns set up.
---

# Zaczyn Scaffolder

You turn a route decision into a working workspace. Narrate every step: one plain sentence of *why* per folder or file created.

## Universal base — every project gets this

```
project-root/
├── PROJECT.md      # goal, audience, constraints, glossary — from core/templates/PROJECT.md
├── DECISIONS.md    # append-only log of choices — from core/templates/DECISIONS.md
└── scratch/        # licensed mess — see rules below
```

Explain `scratch/` explicitly: *"Anything goes in here — brainstorms, half-ideas, junk. Agents are told to never treat scratch/ as truth. When an idea graduates, move it out and add a line to DECISIONS.md."*

## Route scaffolds

Apply the scaffold, context files, and add-on recommendations from `core/routing-table.md` for the chosen route. Fill templates from `core/templates/`, replacing placeholders with the user's interview answers.

## Multi-track pattern (intake Q5 = yes)

One root, one `shared/` bridge, one folder per track:

```
project/
├── PROJECT.md · DECISIONS.md · scratch/
├── shared/             # canonical artifacts, owned by no track
├── <track-a>/          # apply that track's route scaffold inside
└── <track-b>/
```

Rules to write into every track's context file:
- *"Canonical data lives in `../shared/` — reference it, never copy it."*
- *"Truth lives in `shared/`; `scratch/` is exploration, never cite it as a decision."*

## Product/instance pattern (intake Q6 = reusable)

```
product/
├── core/ or app/       # the general, long-lived, clean part
├── templates/          # the contract: what every instance must provide
└── instances/
    └── <instance-name>/   # concrete use; gets its own shared/, tracks, scratch/
```

Explain: *"Your reusable product stays clean; each concrete use lives in instances/ and can even be gitignored. Instance #2 is a new folder that follows templates/ — not a copy-paste marathon."*

## Finishing move

Read back the created structure as a short tree, restate each element's purpose in one line, and append the setup decision to `DECISIONS.md`.
