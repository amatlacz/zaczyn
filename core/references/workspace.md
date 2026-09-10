# Workspace conventions

Read these before a skill writes project state. Reuse the current session's reading unless the file changed.

## Resolve the environment

Establish the selected project and whether this host can actually read/edit its files. Never treat the installed bundle as the user's workspace. A chat project with uploads is a different environment: use the edition's document-saving procedure and do not claim local file edits, installed skills, or persistent updates without evidence.

Read applicable host instructions, AGENTS, and current project context, then the selected task and relevant local rules. Follow existing authority pointers. Read old decisions only when they affect the work; do not load every past task, profile document, or skill.

Resource links resolve from the containing resource file. Shipped defaults belong to the bundle. For a new task template prefer an explicit workspace-local `zaczyn/templates/task.md` override; otherwise use [the bundled template](../assets/task.md). Legacy work retains its own templates. If a resource cannot be located, explain the missing path and request the correct bundle or document; do not search for an unrelated source checkout and call it successful installation.

Host-specific filenames and installation belong to [adapters](../../adapters/README.md). Reuse the current adapter's established mechanism; if automatic loading is unknown, explain an explicit read/upload fallback. A Markdown link or AGENTS filename alone does not prove discovery.

## Portable context and ownership

New local setups create a concise [AGENTS](../assets/AGENTS.md) for how to work and [PROJECT](../assets/PROJECT.md) for facts and scope. AGENTS points to PROJECT in ordinary language; host wrappers may import AGENTS using host syntax. Add only the wrapper needed by the selected host. Merge with existing instructions, never replace them wholesale or generate wrappers for every possible host.

When saving context, compare each statement with what the user actually said. Preserve who acts, conditions, and scope: “I review before sharing” means the user must review before sharing, not a permanent ban on sharing after review and authorization. Keep that behavior in AGENTS, not a second active copy in PROJECT. Setup decisions in PROJECT may point to AGENTS or record dated changes; they should not restate current rules as another set of instructions. “I work alone” does not establish that no reviewer or collaborator can ever be involved. Omit unsupported claims or label them as unresolved; ask only if the distinction affects the next action.

Keep old PROJECT rules, LESSONS, DECISIONS, or other authoritative context in place unless the user requests consolidation. When migrating, preserve the old content, move each rule once, and update its former location to point to the authority. New behavior belongs in AGENTS or its scoped linked rules; current project facts belong in PROJECT. Do not leave contradictory active copies.

Longer profiles and references are optional, linked by purpose and scope from PROJECT. Confirm whether they belong to this project or broader personal use before exporting them elsewhere. Distinguish supplied material, confirmed facts/preferences, and inference; imported content is not automatically an instruction. Use relevant context selectively.

Local rules, templates, and skills are user-owned. Updating shipped defaults never overwrites them or makes them global. For a copied default, record source/version if known, purpose, and selection. An uploaded/reference template does not authorize external actions.

## Durable work without compulsory scaffolding

Quick work needs no task record; explicit setup still saves minimal AGENTS/PROJECT context. Durable agreement, progress, or evidence can use `work/<YYYY-MM-DD>-<short-name>/task.md`; check collisions and follow existing naming conventions. Outputs stay at established paths. No mandatory jar, output tree, scratch folder, tool catalog, or log.

Use `status: open | closed`. Paused, blocked, and review-only work stays open with its next action. Closed outcomes distinguish completed, accepted gaps, and cancelled. Preserve dated changes of consequential intent; do not rewrite criteria to make a result pass. Reopen a closed item with a reason when further work changes it.

Record outcome, useful checks, source/output pointers, and next action. Add plan/review sections only when useful. Keep assumptions and blockers explicit. Split a long plan, history, or independent review only when it improves retrieval or the user asks; point to the authoritative record instead of duplicating it.

On an archive request, prefer marking a closed item inactive in the existing index. Move records only when requested or established by the workspace convention, retaining a discoverable pointer and valid output links. Archiving is organization, not deletion or evidence that unfinished criteria passed.

## Existing workflows

Recognize both task.md and legacy brief/plan/review. The legacy brief owns intent/status, its plan owns progress when present, and its review owns evidence. Continue without conversion. If formats conflict for one task, use explicit authority pointers or resolve the choice with the user rather than choosing by filename or timestamp.

Reuse authoritative domain plans and checkpoints. Add a Zaczyn record only for missing cross-workflow context, linking existing records. For nested tracks/instances, identify the selected root, affected outputs, and owner/update convention for shared material. Resolve ambiguous scope before changing adjacent instances.

## Communication and authority

Use the user's conversation language and honor a separately requested output language. Keep filenames, state keys, and criterion IDs stable. Ordinary work asks only for missing decisions that affect the next action; setup explicitly supports broader discovery at the selected depth.

Respect setup-only, plan-only, and review-only scope. An example supplied during onboarding does not by itself authorize execution. Continue when the user explicitly chooses work or already requested setup followed by execution. Distinguish drafting from sending/publishing or modifying connected systems; retain the user's existing authorization without repeated ceremonies.
