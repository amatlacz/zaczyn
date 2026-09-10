# Example: a tester chooses a guided setup

This hand-authored example illustrates the 0.4 experience; it is not a recorded user or host test.

A tester says: “Help me customize this folder for exploratory testing. I use an existing issue tracker and keep re-explaining how I want bugs described. Guided setup, please. A checkout bug is an example; don't investigate it yet.”

The assistant reuses that context and asks about the current reporting practice and an example of a useful report. It suggests a short issue-report recipe and, optionally, a tracker integration. The tester chooses the recipe, asks for concise explanations, and defers the integration.

The resulting setup consists of [AGENTS](AGENTS.md), [PROJECT](PROJECT.md), and one [local recipe](zaczyn/recipes/issue-report.md). A host-specific context wrapper may also be needed. There is no task record, installed tracker, or invented bug report. Setup ends with a choice to begin real testing or customize further.

Quick mode could stop with a small scoped rule. Deep mode could add selected test strategy material and more procedures over later sessions. The four intents remain the same.
