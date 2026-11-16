---
name: zaczyn-probe-ref
description: Diagnostic probe that shows whether this app reads a file packaged with a skill. Use when the user asks to run the Zaczyn reference probe or types zaczyn-probe-ref. Replies with a short fixed report. Not for real work, advice, documents or edits.
---

# Zaczyn reference probe

This skill is a diagnostic test of how the app loads skill files.

1. Open `references/probe-detail.md` from this skill and note the codeword in it.
2. Reply with these four lines, filled in:

```
PROBE BODY: OWL-17
PROBE REFERENCE: <codeword from references/probe-detail.md, or CANNOT OPEN>
PROBE HOST: <the name of the app you are running in, as far as you know it>
PROBE LOADED BY: <automatic, chosen by the user, pasted or attached by the user, or unknown>
```

If the file could not be opened, write CANNOT OPEN instead of a codeword.
