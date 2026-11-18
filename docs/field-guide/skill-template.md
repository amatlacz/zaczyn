# Skill template

Copy the block below into a file named `SKILL.md`, inside a folder with the same name as the skill. Replace every line in angle brackets and delete what you do not need. This page is not a skill itself.

````markdown
---
name: <lowercase letters, digits and single hyphens, at most 64 characters, same as the folder>
description: <What it does, in one sentence. Use when <the situations and words that should trigger it>. Not for <the nearby requests it should ignore>.>
---

# <Skill title>

<One sentence: the result the user gets.>

1. **<First step>.** <What to read or ask, and what to do if it is missing.>
2. **<Next step>.** <...>
3. **<Check>.** <How to know the result is good before handing it over.>

<Output: shape and length, for example "one screen, bullets, the user's language".>

<Never: what this skill must not do, such as sending, deleting, or claiming a check passed.>
````

If your app does not load skills by itself, attach or paste the file and say: “Read this file in full and follow it for <task>.” Keep that sentence in your notes or README, not in the skill: the model reads every line of the skill.

Keep the description on one line, under 1,024 characters, without a colon followed by a space; some apps reject the file otherwise. See [your first own skill](first-own-skill.md) for how to test it.
