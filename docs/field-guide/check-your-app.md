# Check what your app actually loads

Copying files into a folder does not prove your app reads them. Run this check once after installing, in a fresh conversation, and again after an app update.

Send this prompt:

```text
Without reading any files first, answer three questions in three lines:
1. Which instruction files did you load at the start of this conversation (for example AGENTS.md, CLAUDE.md, or project instructions)? Name them, or say none.
2. Which skills are available to you right now? List their names, or say none.
3. Is zaczyn-review among them? If not, say so.
```

Then record three lines next to your setup, with the date and the app's name and version:

```text
Instruction file loaded: yes / no (which)
Skills listed natively: yes / no (which)
Fallback that worked: none needed / typed the skill name / attached or pasted the file
```

If the skill is not listed, check the folder your app documents for skills, start a new conversation, and try again. If it still is not listed, use the fallback: attach or paste the skill file and say “Read this file in full and follow it for <task>.” That works in any app that can read a file, but the app will not pick the skill by itself.

An answer to this prompt is the app's own report, not proof. A skill listed by name is available; it is verified only after it ran correctly on a real task.
