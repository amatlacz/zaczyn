# Plan — Symposium talk

> Executes the contract in [brief.md](brief.md). Created by zaczyn-plan on 2026-09-01.

## End state

An outline, timed speaker notes, and a 13–14-slide deck in the institute template exist; a timed read of the notes comes in under 19 minutes; the take-home sentence opens and closes the talk; every result slide points at a figure in `sources/analysis/`; the committee's limitations slide is there. Marta has rehearsed once.

## Phases

### Phase 1 — Outline

- **Steps:** turn the six figures into one story with one take-home sentence · one slide per idea, section dividers between blocks · decide the pilot question (brief, Open questions) · put a provisional time next to each slide.
- **Artifacts touched:** `content/outline.md` — intent: the skeleton everything downstream copies; what must not break: exactly one message.
- **Verify:** every result slide maps to a figure (SC-3); take-home sentence on first content slide and last (SC-2).
- **Gate:** **yes** — Marta approves the outline before any notes or slides exist.

### Phase 2 — Speaker notes with timing

- **Steps:** write notes per slide from the outline · estimate at ~130 words/minute · do one timed read-through aloud.
- **Artifacts touched:** `content/speaker-notes.md` — intent: what Marta actually says; must not break: the slide order from the outline.
- **Verify:** timed read ≤ 19 minutes (SC-1).
- **Gate:** no.

### Phase 3 — Slides in the template

- **Steps:** build the deck from the outline in `sources/template.pptx` · limitations & next steps slide (SC-4) · template check on every slide · *(added 2026-09-02, see Progress)* trim to bring the timed read under 19 minutes.
- **Artifacts touched:** `exports/talk.pptx` — intent: the thing shown on the day; must not break: slide count and order match the outline.
- **Verify:** slide count = outline; logo and fonts on every slide (SC-5); SC-4 present.
- **Gate:** no — goes to `zaczyn-finish-session`.

## Success criteria → phases

| Criterion (from brief) | Satisfied by |
|---|---|
| SC-1 | Phase 2 (checked), Phase 3 (trim if needed) |
| SC-2 | Phase 1 |
| SC-3 | Phase 1 |
| SC-4 | Phase 3 |
| SC-5 | Phase 3 |

## Risks & open questions

- Scope creep into a defence rehearsal (brief, Risks) — the gate is the defence against it: nothing enters after the outline without being asked for.
- Pilot slide: resolved at the gate (see Progress, Phase 1).

## Progress

> Ledger for whoever executes — one phase at a time; verify, update, stop at gates.
> If a discovered fact changes the contract: halt, amend brief/plan explicitly, note it here, continue.

| Phase | Status | Date | Note |
|---|---|---|---|
| 1 | done | 2026-09-01 | Approved at the gate: 14 slides. Pilot included as one slide (open question resolved, logged in DECISIONS.md). |
| 2 | done | 2026-09-02 | **Verify FAILED:** timed read 22:10, over by 3 minutes. Halted. Amended plan: added a "trim to ≤ 19 min" step to Phase 3 rather than re-planning; flagged for review. |
| 3 | done | 2026-09-03 | Deck built (14 slides). Trim: methods detail moved to appendix → 13 slides, timed read 18:40. Template check: logo missing on 3 section-divider slides — the template has no divider layout. Handing to finish-session. |
