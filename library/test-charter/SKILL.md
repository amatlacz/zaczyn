---
name: test-charter
description: Draft an exploratory test charter or a list of checks from a specification, user story, change, or risk, with mission, risks, test ideas, oracles, open questions, and what is out of scope. Use when a tester asks for a charter, test ideas, or checks for a feature or change. Not for writing automated test code or reporting test results.
---

# Test charter

Help a tester start a focused session or a set of checks quickly, with every idea traceable to the material or marked as an assumption.

1. **Read the material.** Open the specification, story, change description, or risk the user gave. Note what you could not open. Ask only for what blocks a useful charter, such as the target when none is named.
2. **State the mission** in one sentence, using Elisabeth Hendrickson's charter form: “Explore <target> with <resources or techniques> to discover <information>.” If the material covers several unrelated targets, propose two to four one-line missions and ask which to chart instead of writing one charter for everything.
3. **List the risks.** What could go wrong for users, data, money, security, or operations. Order them by likely impact; say the order is your estimate unless the material or the user gives likelihood (defect history, usage, recent changes), and invite the tester to reorder. Point each risk to the line of the material it comes from, or mark it as an assumption.
4. **Give two to four test ideas for each of the top three risks.** Choose only the variations that fit that risk (inputs, states, sequences, boundaries, roles and permissions, data volume, interruptions, error handling); do not cover every variation. Name each idea's oracle: how the tester would recognise a problem.
5. **Collect open questions** for the author of the material: ambiguities, missing rules, conflicting statements.
6. **Name what is out of scope** for this charter.

If the user asks for checks rather than a charter, return numbered checks instead of steps 2 to 4: the condition, the action, the expected result, and the source line, each marked “from the material” or “assumed”.

Keep the charter to one screen: short bullets, no test code, no time plan unless the user gives a time box. Use the user's language. Reply with the charter; save it as a file only if the user asks.

Never say anything was tested or passed: this skill prepares testing, it does not perform it. Do not invent requirements; an expectation not in the material is an assumption and is labelled so.
