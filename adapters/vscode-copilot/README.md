# Zaczyn in GitHub Copilot for Visual Studio Code

Status: a draft written from the VS Code and GitHub documentation of November 2026, **not yet confirmed in a working installation**. In one test on a company-managed computer no workspace skills appeared at all; the cause (organisation policy, version, or trust) was not established. If you try it, tell us what happened in a [GitHub issue](https://github.com/amatlacz/zaczyn/issues). The optional [host probe](https://github.com/amatlacz/zaczyn/tree/main/probe) is a short test; its VS Code part needs some familiarity with settings.

This package (`zaczyn-vscode-copilot-0.7.0.zip`, from the [0.7.0 release](https://github.com/amatlacz/zaczyn/releases/tag/v0.7.0)) contains the five skills in `skills/`. It works for documents and notes as well as code: VS Code is the editor, Copilot the assistant.

## Before you start

- A current VS Code (**Help** → **About**), signed in to GitHub with a Copilot plan. Skills exist since version 1.109; the Session Target and Chat: Open Customizations steps below match versions from 1.143. Copilot Free includes agent mode, but GitHub does not list skills by plan, so check with `/` after installing.
- (For IT) On a managed computer, check the Command Palette (**Ctrl+Shift+P**, ⇧⌘P on macOS) → **Developer: Policy Diagnostics**. If `ChatAgentMode` is off or `ChatStrictPluginOnlyCustomization` is set, your organisation blocks the skills this package uses; ask IT, or attach a skill file to the chat instead.

## Install for one folder

1. Extract the ZIP. Rename the extracted folder `zaczyn-install` and copy it into your work folder, for example `XYZ`.
2. In VS Code, **File** → **Open Folder** → `XYZ` itself. Trust the folder when asked; in Restricted Mode agents are off.
3. Open the chat (**Ctrl+Alt+I**, ⌃⌘I on macOS), select **+** for a new chat, set **Session Target** (the menu that picks which assistant engine runs the chat) to **Copilot** if offered, choose **Agent** in the agent picker, and send:

> Read zaczyn-install/README.md and install Zaczyn for this folder only: copy the five folders from zaczyn-install/skills into .github/skills, keeping every file. Preserve my existing files. Do not install anything globally or start setup yet.

4. Start a **new** chat (an older one does not see new skills) and type `/`. The list should show `zaczyn-setup`, `zaczyn-work`, `zaczyn-review`, `zaczyn-grow`, and `zaczyn-orchestrate`. If a name appears twice, two copies are installed; keep one.
5. Type `/zaczyn-setup` and add: “Quick setup: I want help with <one sentence about your work>. Ask only what you still need, then save my setup.”

Copilot uses `AGENTS.md` (or `.github/copilot-instructions.md`) in the work folder as project instructions. If the folder already has `.github/copilot-instructions.md`, add one line there: “Read AGENTS.md in the folder root.” In a new chat, check that Copilot follows AGENTS.md. Once installed, `zaczyn-install` can be moved out of the folder.

**One copy per folder your apps read.** VS Code's skills page lists `.github/skills` for Copilot; its migration guide also lists `.agents/skills`. The Codex and Antigravity apps read `.agents/skills`. If you use them on the same folder, install into `.agents/skills` only and check with `/` that Copilot lists each skill once; if Copilot shows none, move the copy to `.github/skills` and give the other apps their own folder.

## Installation rules for the assistant

- Copy exactly `skills/zaczyn-setup`, `skills/zaczyn-work`, `skills/zaczyn-review`, `skills/zaczyn-grow`, and `skills/zaczyn-orchestrate` into the work folder's `.github/skills/`, with every file inside them. Create missing parent folders only; do not replace or delete other skills.
- Do not install into the user's home folder or any global location.
- Afterwards list the five `SKILL.md` paths and each `VERSION` file's content. Copying is not proof of discovery: ask the user to start a new chat and type `/`.

## Connected tools

Copilot can use tools and MCP servers (connectors to other tools), such as trackers or wikis. Keep the permission level at **Manual permissions** (the default), not Allow all or Autopilot. For any tool that writes, choose **Allow Once**, not an “in this Session” option or **Always Allow**. Zaczyn shows the list or draft first and changes only the items you approved.

## If the skills do not appear

1. Look for **Restricted Mode** at the top or in the status bar; trust the folder.
2. Start a new chat with Session Target **Copilot** and the **Agent** agent selected.
3. Command Palette → **Chat: Open Customizations** → **Skills** lists the skills found. If one is missing, check that its folder name matches the `name:` line in its SKILL.md; a skill with an invalid name does not load and shows no error.
4. Fallback that works anywhere: attach `.github/skills/zaczyn-review/SKILL.md` to the chat and say “Read this file in full and the files it points to, then follow it for <task>.”

Sources (checked 2026-11-16): [agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [migration guide](https://code.visualstudio.com/docs/agent-customization/migrate-customizations), [approvals](https://code.visualstudio.com/docs/agents/run/approvals), [agent harnesses](https://code.visualstudio.com/docs/agents/run/agent-harnesses), [enterprise policies](https://code.visualstudio.com/docs/enterprise/policies), [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust), [GitHub agent skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills). See [verification](../../docs/verification.md).
