# Zaczyn in Kiro

**Experimental:** package integrity is checked, but actual Kiro discovery, invocation, and context loading are unverified. Host testing is deferred for this version.

Use `zaczyn-kiro-0.5.1.zip`. This is a native workspace skill package. No browser upload or user-facing command-line installer is required.

## Put it in your work project

1. Extract the ZIP anywhere convenient, such as Downloads. The extracted folder contains `skills/` with four `zaczyn-*` folders. Keep each skill folder complete.
2. Open the folder you actually want to work in with Kiro. The framework download is the installation source, not the work project.
3. Give the agent the path to this extracted README and ask:

> Install the four Zaczyn skill folders beside this README into this workspace's `.kiro/skills/` directory. Read the installation instructions below first. Preserve existing instructions, custom skills, and outputs. Tell me which folders you installed and whether native discovery was actually checked.

The assistant copies `skills/zaczyn-setup`, `skills/zaczyn-work`, `skills/zaczyn-review`, and `skills/zaczyn-grow` into `.kiro/skills/`. It creates missing parent folders only. Existing `.kiro/skills/` content stays in place; do not replace the whole directory. A resulting entry is `.kiro/skills/zaczyn-setup/SKILL.md`.

If you prefer manual copying, copy those four folders to that same destination using your file manager. Hidden folders may need to be shown. Do not copy only SKILL.md: every exported folder contains its own supporting references.

## Start setup

Open a fresh conversation in that workspace after installation; restart the app if discovery does not refresh. Ask Kiro to use zaczyn-setup. In the IDE, Agent Steering & Skills also offers Import a skill → Local folder; select each complete exported skill folder.

Say: “Help me customize this workspace for my work. Show me quick, guided, and deep options before we start a task.” Choose a depth, discuss your needs, and accept only additions you want. Setup should save your preferences and facts in the work project.

Kiro documents automatic AGENTS.md loading. Keep it at the workspace root and point to PROJECT.md. No extra steering wrapper is required for the default agent. Custom agents have their own resource configuration; check it instead of assuming the default paths are enabled.

Work, review, and grow use the same `zaczyn-work`, `zaczyn-review`, and `zaczyn-grow` names. Select the native entry when the host exposes one; naming a skill does not by itself prove it loaded.

## Installation, updates, and undo

The four exported folders are shipped defaults. Personal preferences belong in AGENTS/PROJECT and selected workspace-local procedures, outside those folders. Installation only copies the skill folders; it does not invent a user profile or overwrite context files.

Before replacing an existing Zaczyn folder, compare its VERSION and contents. Move a backup outside all skill-discovery directories, preserve any local edits, then replace only the four selected Zaczyn folders. Do not keep old and new copies discoverable together. If an existing folder has unrelated content or unclear ownership, stop before replacing it and explain the conflict. To undo, remove only the installed Zaczyn folders and restore the saved ones; keep user context, outputs, and unrelated skills.

A copy is an installation step, not proof of discovery or successful use. Check the host's skill list, then ask setup to read a linked resource from the installed path. A fresh-session summary of AGENTS/PROJECT checks context recovery separately. If file access is unavailable, name the missing permission/path; do not claim installation or search for another checkout silently.

Official host mechanisms: [skills](https://kiro.dev/docs/skills/) and [working instructions](https://kiro.dev/docs/steering/). Zaczyn's package checks and actual host evidence are listed in [verification](../../docs/verification.md). Installation and invocation behavior must be verified in the specific app/version in use.
