# Lessons

> Append-only. What this workspace has learned about working with its agent — rules that should change how future sessions behave.
> Entries are added by zaczyn-finish-session ("record as lesson") or by you: say *"remember this"* and your agent adds one.
> Skills read this file **before** asking questions, so a rule written here is a question you never answer twice.

Two tests before adding an entry: is this a *class* of situation, not a one-off? Would the agent break the rule without being told? If either answer is no, it isn't a lesson — fix the prompt or the file instead.

### 2026-09-03 — Cap the slide count, not just the minutes
- **Context:** Symposium talk work item. The brief's SC-1 said "timed read ≤ 19 minutes".
- **Problem:** Nothing in the brief limited the number of slides, so the outline grew to 14 at the gate; the timing check then failed at Phase 2 (22 minutes) and cost an extra trim step in Phase 3.
- **Rule:** For talks, put a slide cap in the brief right next to the time limit — roughly one slide per 1.5 minutes — and check it at the outline gate, where cutting is cheap.
- **Applies to:** start-session
