# Example: a small attendance summary

This is a hand-authored teaching example with invented data, not an additional agent test. All inputs and the output are included so you can inspect the checks yourself.

A coordinator asks: “Summarize this week's attendance for our internal update. Check the count and flag missing information. Save the work so we can continue later.”

1. **Setup** needs only the purpose and constraints in [PROJECT.md](PROJECT.md).
2. **Work** reads [the attendance data](attendance.csv), produces [the summary](summary.md), and records useful state in [one task note](work/2026-09-05-attendance/task.md). It does not need a separate plan.
3. **Review** checks the arithmetic, units, caveat, and action against the source. The checks live in the same task note. A pause before review would keep it open; here the completed example is closed.
4. Later, the coordinator asks **grow**: “Please remember this shape for weekly internal summaries.” A short scoped rule in [AGENTS.md](AGENTS.md) is sufficient. Its prior state and undo instruction are retained there. No new skill or template folder is needed.

A one-off summary without a need to retain agreement or progress could omit the task note entirely. The useful result matters more than matching this folder tree.
