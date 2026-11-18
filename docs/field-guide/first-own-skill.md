# Your first own skill

Write a skill when you keep explaining the same procedure and it has a clear moment when it applies. One request stays a prompt; a preference goes into AGENTS.md. See [what deserves a skill](what-is-a-skill.md).

## Write it small

Start from the [skill template](skill-template.md). Keep the first version to one file and about one screen:

- **name:** lowercase letters, digits, and single hyphens, at most 64 characters, not starting or ending with a hyphen, identical to its folder name.
- **description:** one line saying what it does, when to use it, and when not to. This line decides whether your app picks the skill, so use the words people actually say when they need it.
- **body:** the steps in order, what a good result looks like, and what the skill must never do.

Leave out background, motivation, and anything the model already does well without being told.

## Test it cold

A skill that works in the conversation where you wrote it proves little: that conversation already knows what you meant. Before you rely on it:

1. Start a fresh session without the conversation you wrote it in.
2. Give it a real case written by someone else, or one you have not shown it.
3. Give it a request where it should **not** apply, and check that it stays out of the way.
4. Ask a colleague to read only the skill and say what it will do. If they cannot, neither can the model.

Record what you tried and what happened next to the skill, with the date. A skill that passed one case is verified for that case, not in general.

## Keep a team inventory

When a team shares skills, keep one short list in a shared place:

| Skill | Owner | Where it lives | Status | Last tried |
|---|---|---|---|---|

Status uses the Zaczyn ladder: proposed, selected, available, configured, verified, or blocked. Remove skills nobody uses: every installed skill adds its description to what the app reads on each request.

## Prompt library or skill?

A shared prompt library is fine for one-off requests people copy and adapt. Move a prompt into a skill only when it has steps, checks, and a clear trigger, and someone will maintain it.
