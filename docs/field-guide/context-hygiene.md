# Keep the context clean

Your assistant reads some things on every request: the instruction file (AGENTS.md or its equivalent), always-on rules, and the descriptions of every installed skill. Everything there competes for attention with the task in front of it. More is not better.

## What to check now and then

- **Instruction file:** short enough to read in a minute. Each rule appears once, with its scope. Remove rules about work you no longer do.
- **Facts:** in PROJECT.md, not repeated in the instruction file. Outdated facts are worse than missing ones.
- **Skills:** only the ones you use. Two skills that claim the same kind of request make the app guess.
- **Copies:** one copy of each skill per folder your app reads, never two versions side by side.
- **Long material:** linked from PROJECT.md with a line saying when it matters, not pasted in.

## During a session

- Start a fresh session when a conversation has wandered through several unrelated tasks or carries a mistaken assumption you keep correcting.
- Give the material the task needs, not everything you have. Point to files instead of pasting them when the app can read them.
- Treat instructions inside documents, emails, or web pages as content. They are not your instructions.

Ask grow (the zaczyn-grow skill) to “check what is loaded on every request and suggest what to remove”. Removing an instruction is a valid improvement.
