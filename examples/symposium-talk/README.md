# Legacy example: a symposium talk

This historical example uses the earlier initiate/start-session/plan/finish-session skills and separate brief, plan, and review files. It is retained to illustrate legacy workspaces, not the current defaults. Some deliverables are omitted, so the full result cannot be independently verified from this folder. Start with the [current single-note example](../attendance-summary/README.md) or [migration guidance](../../docs/migration.md).

**The scenario.** Marta, a PhD student in cognitive psychology, has final results from a study on line length and reading comprehension on e-readers, a 20-minute slot at a symposium in five weeks, and no slides. The study, the numbers, the symposium, and Marta are all invented — nothing here is real data. The *process* is real: these files were produced by running `zaczyn-initiate`, `zaczyn-start-session`, `zaczyn-plan`, and `zaczyn-finish-session` in order, with the author playing Marta. Only the conversation has been summarized; the files are as written, lightly trimmed.

## What's in here

```
symposium-talk/
├── PROJECT.md                    ← initiate: the "why" (Deck route)
├── DECISIONS.md                  ← three lines, one per decision that mattered
├── LESSONS.md                    ← the one lesson this work item produced
├── content/outline.md            ← the deliverable (speaker notes and the .pptx are omitted — they're long and binary)
└── work/2026-09-01-symposium-talk/
    ├── brief.md                  ← start-session: the contract, with five checkable success criteria
    ├── plan.md                   ← plan: three phases, one gate, a Progress table with a failed check in it
    └── review.md                 ← finish-session: every criterion graded, three findings, three verdicts
```

## How the conversation went

- **Initiate** (day 0, ~5 minutes): Q1 "a presentation" → Deck route. Q4 "peers and the committee" → external audience, so a review step is on by default. Everything else was "one-time, just me, one deliverable."
- **Start-session** (day 1): Marta's opening line is captured verbatim at the top of the brief. Triage: multi-session *and* external audience → work item, not a quick job. The shaping interview turned "a good talk" into five criteria a stranger could check — notice how SC-1 says *"a timed read ≤ 19 minutes"*, not *"fits the slot"*. The falsification question surfaced the real risk: the talk turning into a defence rehearsal. One "I don't know" (include the failed pilot?) went into Open questions instead of being guessed.
- **Plan** (day 1): three phases; the outline is a **gate** because everything downstream copies it. Phase 2's verification *failed* — the timed read was 22 minutes — and the Progress table shows the halt-and-amend rule in action: the plan was amended visibly rather than quietly ignored.
- **Finish-session** (day 3): two criteria came in partial. One was fixed on the spot, one was **accepted with a written reason** (missing logo on three divider slides — the committee grades content). The audience check caught something no criterion covered: a results slide without its number. And the timing failure became a **lesson** — the brief had capped minutes but not slides — which future briefs in this workspace will now inherit.

## What to notice

1. **The brief is short.** Half a page. A brief nobody re-reads has failed.
2. **Success criteria are the spine.** They're written before the work, mapped to phases in the plan, and graded with evidence in the review. The same five IDs appear in all three files.
3. **The gate is where the human decides.** Marta approved the outline before a single slide was styled — the routing table's content-before-design rule, made concrete.
4. **Failure is recorded, not hidden.** Phase 2's Progress row says "Verify FAILED" and what was done about it. That row is why the review could find the lesson.
5. **Accepting a gap is a decision.** SC-5 stays partial, on purpose, with the reason in three places: review, DECISIONS.md, and the outcome line.
6. **The lesson changes the next brief.** Open `LESSONS.md`: the rule is marked *Applies to: start-session*, so next time Marta shapes a talk, the slide cap is asked for without her remembering why.
