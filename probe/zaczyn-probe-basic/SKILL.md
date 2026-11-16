---
name: zaczyn-probe-basic
description: Diagnostic probe that shows whether this app can load and run a minimal skill. Use when the user asks to run the basic Zaczyn probe or types zaczyn-probe-basic. Replies with a short fixed report. Not for real work, advice, documents or edits.
---

# Zaczyn basic probe

This skill is a diagnostic test of how the app loads skill files.

Reply with these three lines, filled in:

```
PROBE BASIC: OWL-17
PROBE HOST: <the name of the app you are running in, as far as you know it>
PROBE LOADED BY: <automatic, chosen by the user, pasted or attached by the user, or unknown>
```
