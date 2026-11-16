---
name: zaczyn-probe
description: Diagnostic probe that shows how this app loads a skill and its companion files. Use only when the user asks to run the Zaczyn probe, types zaczyn-probe, or asks to test whether skills and their reference files are read. Reply with the fixed report lines from the skill body and nothing else. Not for real work, advice, documents or edits; never trigger on other requests.
license: MIT
metadata:
  version: "0.0-probe"
---

# Zaczyn probe

This skill is a test. Do not do any other work while it runs.

1. Try to open `references/probe-detail.md` from this skill. Note the codeword it contains.
2. Try to open `assets/probe-template.md` from this skill. Note the codeword it contains.
3. Reply with exactly these five lines, filled in, and nothing else:

```
PROBE BODY: OWL-17
PROBE REFERENCE: <codeword from references/probe-detail.md, or CANNOT OPEN>
PROBE ASSET: <codeword from assets/probe-template.md, or CANNOT OPEN>
PROBE HOST: <the name of the app you are running in, as far as you know it>
PROBE LOADED BY: <automatic, chosen by the user, pasted or attached by the user, or unknown>
```

Never guess a codeword. If you could not open a file, write CANNOT OPEN for it.
