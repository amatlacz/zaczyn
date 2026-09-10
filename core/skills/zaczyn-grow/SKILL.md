---
name: zaczyn-grow
description: Adapt a user's working process from real examples or explicit preferences. Use when asked to make recurring work reusable, remember a scoped practice, change a template, retire a rule, or reduce unnecessary process. Propose the smallest useful change and try it. Not for one-off content edits, automatic learning after every task, or installing tools merely because work repeats.
---

# Grow

Help the user own a process that fits their work. Improvement may mean removing an instruction. Read [workspace conventions](../../references/workspace.md). Revisit the saved setup and relevant current practices; use [customization guidance](../../references/customization.md) for selected additions, installation, verification, or removal.

1. **Locate a real need.** Read the relevant example, current rule/template, or explicit preference. Ask what keeps needing explanation or what feels wasteful only if unclear. Repetition is a signal, not proof that a skill is needed. No need to invent a failure to capture a useful practice.
2. **Choose the smallest adaptation.** A one-time need stays a prompt. A stable working preference goes into AGENTS or the existing authoritative rule file. A repeated shape becomes a checklist/template. A repeatable procedure with a clear trigger may deserve a skill. An added tool is justified only by an unmet capability. Reuse or revise an existing adaptation before adding another.
3. **Make the proposal concrete.** State the intended behavior, scope/exceptions, file to change, an example to try, and how to undo it. Explain why it is worth maintaining. For a material change to the user's process, present alternatives and a recommendation if their preferences require a choice. If the user already requested the exact rule or reversible edit, implement that scope without another approval ritual. Otherwise resolve the proposed durable change with them before applying it.
4. **Preserve ownership.** Edit the user's existing authoritative rule or create a workspace-local recipe/template under `zaczyn/` only when needed. Never edit the installed base to store project preferences. For a copied default, record its source/version if known (otherwise unknown), purpose, and how it is selected. Preserve the prior form or a reversible diff. Mark superseded rules inactive and retain enough history to explain the change; do not leave both contradictory rules active.
5. **Try and assess it.** For a procedure or template, try a representative case and a case where it should not apply. For a simple preference, check its scope and an exception; do not turn a one-line rule into a test project. Report actual results, unresolved limitations, and the user-visible difference. Keep, revise, or undo according to evidence and the user's decision. A draft is not a validated skill.

For a skill, capture trigger/non-trigger, expected inputs/output, steps, checks, and non-goals. Hand that contract to an available skill creator; if none is available, write a usable Markdown recipe and explain how to invoke it explicitly. Do not call it installed or discoverable without checking the host. Update the selected-procedures pointer in AGENTS and any existing setup record when the change affects them; keep capability status honest.

Finish by explaining what changed and how to use or undo it. A helpful outcome may be “keep doing this with a prompt”; no new file or skill is required.
