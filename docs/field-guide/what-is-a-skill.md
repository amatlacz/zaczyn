# What deserves a skill?

A skill is a recipe the assistant can consult for a particular kind of work. It explains when it applies, what material it needs, what to do, and how to check the result. It is useful when it saves repeated explanation; it also creates something to maintain.

Choose the smallest thing that solves the problem:

| Your need | Start with | Example |
|---|---|---|
| One request | A prompt | “Summarize this letter in five sentences.” |
| A stable preference | A scoped project rule | “In internal weekly updates, put the requested decision first.” |
| A repeated shape or check | A template or checklist | “Each attendance update needs the period, count, missing data, and next action.” |
| A repeatable procedure | A recipe, then perhaps a skill | “Check attendance data, compare periods, draft the update, and verify every claim.” |
| A missing capability | A suitable tool or manual alternative | “We need a way to read this file format.” |

Repetition alone does not require a skill. An existing domain workflow might already solve the problem. A prompt may remain the best choice.

During setup, describe the work you expect to repeat; Zaczyn can suggest a starting practice before you have finished your first task. Later, ask grow: “This is an example of work I repeat. Help me choose the smallest reusable improvement.” It should explain where the change applies and where it does not, try it on suitable examples, and show how to undo it. Keep local changes in your workspace or chat project, separate from the installed starter. Put working preferences and selected-procedure pointers in AGENTS.md; put facts and scope in PROJECT.md. A recipe uploaded to a chat project is used by asking for it, not by assuming a native skill was installed.

If a skill is justified, give it a clear trigger, expected input and output, useful steps, checks, and non-goals. Verify that your assistant can actually find and invoke it before calling it installed. If discovery is unavailable, a Markdown recipe that you explicitly ask it to read can still be useful.

[See guided customization](../../examples/guided-setup/README.md), [a small improvement example](../../examples/attendance-summary/README.md) and [common problems](misuse-patterns.md).
