# Updating Zaczyn

## Claude project skills in 0.5.2

For one Claude Code project, including a desktop local session, use the new `zaczyn-claude-project-0.5.2.zip` and its [project-only guide](../adapters/claude-project/README.md). It installs four self-contained folders in that project’s `.claude/skills/`; it does not require a terminal launch or global plugin. Do not copy raw core skill folders from the earlier plugin ZIP because their references live outside those folders.

Existing AGENTS, PROJECT, CLAUDE, and outputs stay in place. If the same session also loads the Zaczyn plugin, choose one installation path to avoid confusing duplicate commands. The plugin remains an optional supported packaging format; previously published assets are unchanged.

## Native packages in 0.5

The four intents and AGENTS/PROJECT ownership stay the same. Codex, Antigravity, and Kiro gain generated workspace skill packages. Use the matching host ZIP and install the four folders from its skills directory, following the included README. Codex/Antigravity target .agents/skills; Kiro targets .kiro/skills. These are workspace installs, not automatic marketplace registration.

Each exported skill includes its linked resources. Other intent procedures have non-discoverable filenames, and bundled context templates are not named AGENTS.md. Do not install the raw source skill folders or rename supporting templates to active instruction filenames inside the installation. Codex and Antigravity exports have identical skill content and may share one workspace installation.

Keep previous installed folders outside discovery paths before replacing only the four Zaczyn folders. Preserve unrelated skills, local edits, AGENTS/PROJECT, task records, and outputs. Use a fresh session to verify discovery and context. Roll back by restoring the previous four folders; do not erase user work. No automatic updater or context migration is included.

The context cleanup makes setup decision records point to authoritative preferences and keeps discovery/configuration/verified-use claims separate. Existing user context is not changed by installing 0.5; review it deliberately if you want those improvements applied.

## Guided setup introduced in 0.4

Version 0.4 keeps setup/work/review/grow and changes what setup owns: guided customization at quick, guided, or deep depth. An example task supplied during onboarding no longer starts execution automatically. Explicit setup-then-work requests still authorize continuation.

## Context ownership

New local setups use AGENTS.md for working behavior and PROJECT.md for facts/scope. Claude Code's CLAUDE.md imports AGENTS with `@AGENTS.md`; AGENTS points to PROJECT in ordinary language. Other hosts need their adapter or the chat-edition saving procedure.

Existing PROJECT rules, AGENTS instructions, CLAUDE content, LESSONS, DECISIONS, jars, and outputs remain in place until you choose a migration. Do not replace the entire workspace or regenerate every file because the base version changed.

When consolidating context, inspect and back up current files, identify the authoritative rules, move each behavioral preference once into AGENTS or its relevant linked rule file, keep facts in PROJECT, and update former locations to point to the authority. Preserve unrelated host instructions when changing an import. Resolve conflicting rules with the user. Keep a reversible diff or prior version; verify a fresh session reads the intended context.

## Existing task records

Continue legacy brief/plan/review files and current task notes where they are. A legacy brief owns intent/status, its plan owns progress, and its review owns evidence. If both formats describe one item, retain explicit authority and history. New tasks may use one task.md; there is no automatic conversion or deletion.

| Older command | Current entry |
|---|---|
| zaczyn-initiate | setup |
| zaczyn-start-session | work |
| zaczyn-plan | work, asking to plan only |
| zaczyn-finish-session | review; a pause stays open |

Host command syntax differs. Ordinary language expresses the same four intents in the chat edition.

## Replace defaults separately

Keep the old bundle/reference and selected local customizations. Extract the next native version beside it, or upload the next chat reference separately and explicitly select the current one. Do not overwrite a workspace's customized `zaczyn/` directory: older workspaces may store a customized jar there.

A local `zaczyn/templates/task.md` continues to override the new-task default. Record its source/version and purpose. Compare changed defaults with local overrides manually; keep, revise, or retire them deliberately. To roll back, select the previous bundle/reference and restore only the relevant instruction changes, not user outputs.

For session-loaded Claude Code, launch from the work folder with `claude --plugin-dir /absolute/path/to/the-selected-version`. Do not load two versions together. Graphical plugin update/remove procedures and actual resource discovery must be checked in that host.

## Chat projects and changing hosts

Keep current AGENTS, PROJECT, and selected procedures separate from the shipped ZACZYN reference. If direct source editing is unavailable, save the complete replacement returned by the assistant and replace the old project source after backing it up. A downloadable document has not necessarily been added to project sources. Avoid conflicting active uploads.

Before a fresh chat or transfer, save the current documents and unfinished task state. Select which personal/project material should travel. Destination tools may need installation or sign-in again; a source-host capability status is not proof it works elsewhere. No automatic memory synchronization is provided.

[Verification scope](verification.md) distinguishes tested source/file behavior from actual host installation and persistence.
