---
name: zaczyn-probe
description: Diagnostic probe that shows how this app loads a skill and its companion files. Use when the user asks to run the Zaczyn probe, types zaczyn-probe, or asks to test whether skills and their reference files are read. Replies with a short fixed report. Not for real work, advice, documents or edits.
license: MIT
metadata:
  version: "0.2-probe"
---

# Zaczyn probe

This skill is a diagnostic test of how the app loads skill files.

1. Open `references/probe-detail.md` from this skill and note the codeword in it.
2. Open `assets/probe-template.md` from this skill and note the codeword in it.
3. Reply with these five lines, filled in:

```
PROBE BODY: OWL-17
PROBE REFERENCE: <codeword from references/probe-detail.md, or CANNOT OPEN>
PROBE ASSET: <codeword from assets/probe-template.md, or CANNOT OPEN>
PROBE HOST: <the name of the app you are running in, as far as you know it>
PROBE LOADED BY: <automatic, chosen by the user, pasted or attached by the user, or unknown>
```

If a file could not be opened, write CANNOT OPEN for it instead of a codeword.
