---
name: zaczyn-orchestrate
description: Orchestrate a task with cost-aware choices of planner, workers, models, reasoning effort, and verification. Use when named or when the user explicitly asks for economical orchestration. Stay active through that task and its follow-ups; do not activate for ordinary Zaczyn work or unrelated tasks.
---

# Orchestrate

Reach the agreed result using the least expensive approach likely to meet its quality requirements. The session's strong model owns routing, consequential judgments, and completion; it need not perform every plan, read, or review. This skill assumes the user starts with their strongest available model and high reasoning effort. Do not claim to have changed that model or setting without an actual supported operation.

Use this as an execution policy alongside the relevant domain workflow or [Work](../zaczyn-work/SKILL.md), preserving plan-only and review-only scope. Read [workspace conventions](../../references/workspace.md) before writing project state, reusing context already read. Input is the user's task, constraints, accessible material, and available capabilities. Output is the requested result, supporting checks, and any material limitation; no mandatory orchestration report or task folder.

## Route before doing the expensive work

Make a brief initial assessment from the request and readily available context: intended outcome, constraints, completion checks, uncertainty, and cost of error. Clarify only missing consequential decisions. Do not read the entire corpus or produce a detailed plan merely to decide who should do that work.

Inspect the current host's exposed tools, model choices, effort controls, and relevant workflows once; reuse that evidence until availability changes. Consult the selected [adapter](../../../adapters/README.md) only as needed. A skill, role name, or written workflow does not itself launch another model.

Choose who plans, who executes, and how the result will be checked:

- For familiar work, let an economical model prepare and execute a bounded plan, with a checkpoint only where uncertainty or consequences justify one. Assess its plan proportionally; do not reconstruct it yourself.
- Retain or escalate ambiguous framing, difficult reasoning, conflicting evidence, and consequential judgments that cheaper workers cannot reliably resolve. Delegate routine preparation around those parts.
- Prefer deterministic tools for mechanical extraction, transformation, and validation. Batch related routine work for a suitable worker. A tiny action on context already in view can be cheaper to do yourself; repeated reading, formatting, or simple analysis should not drift into frontier work by default.

Optimize total work: context transfer, model/effort cost, scarce usage limits, startup, waiting, integration, retries, and duplicated analysis. Parallelize independent useful work when latency matters; avoid redundant workers or speculative fan-out. Use known relative costs and observed results when prices or token counts are unavailable. Do not invent savings, equate a subscription with unlimited free work, or spend more on cost investigation than the decision warrants.

## Match capability and effort

Choose among models actually exposed in this session, using capabilities rather than vendor names:

| Task demands | Starting choice |
|---|---|
| Bounded reads, extraction, formatting, routine edits with clear checks | Fast economical model or deterministic tool |
| Multi-step execution, familiar planning, synthesis, review against clear criteria | Economical or general-purpose model with sufficient reasoning effort |
| Substantial uncertainty, novel reasoning, difficult tradeoffs, high cost of a missed error | Stronger general-purpose or frontier model; keep only the demanding portion there |

These are starting judgments, not fixed tiers. Tool access, context capacity, relevant skill, and reliable prior results can change the choice. Choose model and effort together: an economical model with more reasoning may be a better fit than a larger model with little reasoning. Use the host's real effort settings; if there is no such control, omit it. Do not translate provider labels into fictitious universal levels.

When supported, launch agents or workflows and select their model/effort autonomously within the user's authorized task. Do not ask the user to approve each worker, choose routine assignments, or request delegation again. Existing external-action permissions still apply; this skill adds no permission ceremony and grants no authority to publish or purchase beyond the task.

## Delegate useful units

Give each worker a coherent deliverable with a clear boundary, large enough to repay startup and handoff but small enough to check or retry. Send only the objective, relevant constraints, source pointers or necessary excerpts, ownership of files/actions, acceptance checks, and a compact return format. Include needed user decisions and applicable instructions; avoiding full history must not lose authority or context.

Ask for the result or changed artifacts, evidence of checks, uncertainties, and blockers. Avoid transcripts, repeated source dumps, and lengthy reasoning reports. Use fresh context when supported and sufficient; reuse a worker that already holds relevant context when doing so saves work. Coordinate shared writes, and use one planner or reviewer when sufficient. Nested delegation must serve the same scope and economics, not create an automatic hierarchy.

## Check, correct, and finish

Choose verification before accepting a result, proportional to what failure would cost. Use deterministic checks where possible, inspect actual artifacts and cited evidence, sample repetitive low-risk output, or commission a cheaper review against explicit criteria. Check all consequential exceptions; sampling is unsuitable when a single missed item could invalidate the result. A worker's confidence or a passing format check does not establish substantive correctness.

The orchestrator owns acceptance without automatically redoing the work. Reserve its own deep review for unresolved uncertainty or consequences that justify it. Independent review is useful when it addresses a specific risk; no mandatory expert panel, multiple reviewers, or second full implementation.

For a failed result, distinguish missing context, unclear instructions, tool failure, and insufficient reasoning. Correct a narrow defect with the existing worker when likely cheaper; increase effort or change model when reasoning is the bottleneck. Do not repeat the same unsuccessful attempt unchanged. After a failed targeted correction, reassess the assignment and route to a stronger worker or handle the hard portion yourself; stop retries that add no useful evidence. If access or essential user information blocks completion, state that dependency instead of spending more model calls.

Integrate accepted results, resolve inconsistencies, and complete the authorized task using [Review](../zaczyn-review/SKILL.md) at the appropriate depth. Final communication states the result, what was checked, and material limits. Explain routing choices only when useful; report measured usage only if available and distinguish it from qualitative expectations.

## Work within actual capabilities

- **Selectable workers:** invoke the available agent/workflow mechanism with supported model and effort choices. Verify what was actually used when the host exposes it; an unsupported preference is not a confirmed selection.
- **Delegation with inherited or opaque models:** use it when context isolation, specialization, or parallel progress warrants the overhead. Describe model selection as unavailable or unknown; do not call it cheaper merely because it is a subagent.
- **No callable delegation:** state the limitation briefly and continue autonomously with one model, using selective reads and deterministic tools. Do not label internal role-play as delegation or claim access to cheaper-model execution. This mode cannot deliver those routing savings.
- **Manual handoff requested by the user:** prepare a compact task packet with necessary context, deliverable, checks, and a place to return results. Mark it prepared, not dispatched or completed; assess returned evidence before continuing. Do not make manual coordination the default or silently export context to another service.

Do not require users to configure a new platform to finish an otherwise feasible task. Keep this policy active through the selected task's follow-ups; end it at completion, cancellation, or an explicit user change. Persist it for later tasks only if requested.
