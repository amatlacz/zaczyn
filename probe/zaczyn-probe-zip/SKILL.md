---
name: zaczyn-probe-zip
description: Diagnostic probe that shows whether this app accepts a minimal skill packaged as a ZIP. Use when the user asks to run the Zaczyn ZIP probe or types zaczyn-probe-zip. Replies with a short fixed report. Not for real work, advice, documents or edits.
---

# Zaczyn ZIP probe

This skill is a diagnostic test of how the app loads skill files.

Reply with these three lines, filled in:

```
PROBE ZIP: OWL-17
PROBE HOST: <the name of the app you are running in, as far as you know it>
PROBE LOADED BY: <automatic, chosen by the user, pasted or attached by the user, or unknown>
```
