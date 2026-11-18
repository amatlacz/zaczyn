# Install Zaczyn in one Claude Code project

Use `zaczyn-claude-project-0.6.0.zip`. This package installs five skills in one project's `.claude/skills/` folder. It works through Claude Code's project-skill mechanism, including local sessions in the desktop app's Code tab. No terminal command or account-wide plugin installation is needed. This guide is for Claude Code, not a normal Chat or Cowork conversation.

## Example: your existing folder is XYZ

1. Extract the ZIP. Rename the extracted folder `zaczyn-install` and copy it into `XYZ`. Check that `XYZ/zaczyn-install/README.md` and `XYZ/zaczyn-install/skills/` exist.
2. Open `XYZ` itself in Claude Code's desktop app as a local project. Work directly in this folder for installation; a separate worktree would receive its own copy.
3. Send this message:

> Read zaczyn-install/README.md and install Zaczyn for this project only. Copy its five complete skill folders into this project's .claude/skills directory, following the installation rules in that README. Preserve my existing files and settings. Do not install anything globally or start project setup yet.

4. When installation finishes, start a fresh local conversation in `XYZ`. Type `/zaczyn-setup` in Claude's message box, select that skill, and add:

> Quick setup: I want help with <one sentence about your work>. Ask only what you still need, then save my setup.

For more questions and suggestions, ask for a guided or deep setup instead.

The slash command is a message to Claude, not a terminal command. Later, use `/zaczyn-orchestrate` for an explicit cost-aware orchestration task; see the [host capability guide](../orchestration.md). If it is absent from the available skills, restart the app and reopen `XYZ`; report the missing entry rather than using a different checkout.

After installation:

```text
XYZ/
  .claude/
    skills/
      zaczyn-setup/       (SKILL.md, VERSION, and supporting references)
      zaczyn-work/
      zaczyn-review/
      zaczyn-grow/
      zaczyn-orchestrate/
  zaczyn-install/         (the extracted installation source)
  ...your existing files
```

After setup, `AGENTS.md` stores working preferences, `PROJECT.md` stores project facts, and `CLAUDE.md` imports AGENTS with `@AGENTS.md`. Existing context is merged and preserved. These belong in `XYZ`, not inside an installed skill.

The installed skills apply to this project and its relevant subdirectories. A separate unrelated project receives no Zaczyn skills from this installation. To use Zaczyn there, install another project copy. The extracted `zaczyn-install` folder is no longer a runtime dependency once the five complete skill folders have been copied; you may move it out of XYZ afterward.

## Installation rules for the assistant

- Resolve the actual selected workspace and this README's location before copying. The workspace is XYZ, not zaczyn-install. Do not substitute a source repository elsewhere on disk.
- Copy exactly `skills/zaczyn-setup`, `skills/zaczyn-work`, `skills/zaczyn-review`, `skills/zaczyn-grow`, and `skills/zaczyn-orchestrate` beside this README into the workspace's `.claude/skills/`. Copy every supporting file; no symlinks or references to the download are required.
- Create only missing parent directories. Do not replace the whole `.claude` or `skills` directory, change global settings, install a plugin, or run a model test.
- If a destination Zaczyn folder exists, compare versions and contents. Preserve local modifications; explain any conflict before replacement. For an authorized update, back up only the replaced Zaczyn folders outside discovery paths.
- Verify all five SKILL.md entries and their linked resources exist inside the installed copies. Distinguish this filesystem check from actual host discovery. Report where you copied them and the exact next action: a fresh local conversation and `/zaczyn-setup`.
- Installation does not create user context, run the setup interview, or execute project work. Those follow the user's setup request.

For manual copying, put those same five complete folders into `XYZ/.claude/skills/`, retaining all other contents. To undo, remove only the five installed Zaczyn folders or restore their backups; retain AGENTS/PROJECT/CLAUDE and your outputs.

Official documentation: [project skills](https://code.claude.com/docs/en/skills) and [desktop support](https://code.claude.com/docs/en/desktop). Earlier package checks do not verify this new skill's execution; this desktop installation path has not had a live UI test. See [verification](../../docs/verification.md).
