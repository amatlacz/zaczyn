# Start with Zaczyn

Zaczyn runs in a native agent working with your project folder. Choose the package for the app you use. You can leave the extracted download in Downloads; the host guide explains which five folders to install in your work project.

| App | Package and instructions |
|---|---|
| Claude Code | `zaczyn-claude-project-0.6.0.zip`; [project-only desktop instructions](adapters/claude-project/README.md) |
| Codex | `zaczyn-codex-0.6.0.zip`; [Codex guide](adapters/codex/README.md) |
| Antigravity (experimental) | `zaczyn-antigravity-0.6.0.zip`; [Antigravity guide](adapters/antigravity/README.md) |
| Kiro (experimental) | `zaczyn-kiro-0.6.0.zip`; [Kiro guide](adapters/kiro/README.md) |

Download the prepared ZIP from the [0.6.0 release page](https://github.com/amatlacz/zaczyn/releases/tag/v0.6.0). Choose the named app package above, not GitHub's automatically generated source-code archive. Ordinary users do not need to clone or build the repository. You need the selected AI app installed and working before installation.

## Claude Code — one project, no terminal required

For an existing folder `XYZ`, download `zaczyn-claude-project-0.6.0.zip`. Extract it, rename the extracted folder `zaczyn-install`, and copy it into XYZ. Open XYZ itself as a local project in Claude Code's desktop app and send:

> Read zaczyn-install/README.md and install Zaczyn for this project only. Preserve my existing files and settings. Do not install globally or start project setup yet.

Claude copies the five complete skills into `XYZ/.claude/skills/`. After installation, start a fresh local conversation in XYZ and select `/zaczyn-setup` in the message box. Send the quick-setup prompt below, or ask for a guided or deep setup. The [project-only guide](adapters/claude-project/README.md) has the folder layout, exact copying rules, and update/undo instructions.

Your project context and outputs belong in XYZ. Other unrelated projects are unaffected. This uses Claude Code's local Code sessions; a normal Chat or Cowork conversation is a different environment.

### Optional plugin path for terminal users

The separate `zaczyn-0.6.0.zip` is still a plugin package, as is a source checkout. Keep its complete folder and load it from a terminal session with `claude --plugin-dir /absolute/path/to/framework`. Plugin commands use `/zaczyn:zaczyn-setup`; project-installed skills use `/zaczyn-setup`. See the [Claude guide](adapters/claude/README.md). The flag is not required for the project-only desktop installation above.

## Codex, Antigravity, and Kiro

Extract the matching host ZIP and read its README. It contains a `skills/` directory with five complete skill folders. Ask the agent to install them into your selected work folder following that README, or copy them manually to the documented destination. Codex and Antigravity use `.agents/skills/`; Kiro uses `.kiro/skills/` or its local-folder import UI. No terminal installer is required for these packages.

These are workspace skill packages distributed as GitHub release downloads; they are not marketplace installations. Codex discovery and bounded owner setup/context checks are recorded. Antigravity/Kiro are experimental: their actual host behavior is unverified, and testing is deferred. See [verification](docs/verification.md). An agent must distinguish copying files from verifying discovery and use.

## Your first conversation

> Quick setup: I want help with <one sentence about your work>. Ask only what you still need, then save my setup.

Quick aims for a short exchange. For more questions and suggestions, ask for a **guided** setup, which explores your working needs, or a **deep** one, which can continue over several sessions. Without a named depth, setup asks you to choose. You can skip questions, stop, or change depth.

The assistant should reuse what you already told it, suggest concrete options, let you choose, and save the setup. An example task describes your needs; it is not automatically executed. At the end, choose to begin work or customize further. Ask “Save our setup progress” whenever you want to stop.

## Your files and the shipped reference

Your behavior and preferences belong in AGENTS.md; project facts belong in PROJECT.md. Extra profiles and procedures are optional. Keep them separate from the shipped Zaczyn bundle/reference so an update does not replace your customizations.

In native workspaces, keep these files in your selected work folder. Host-specific loading instructions must point to them; the folder name alone does not prove the agent reads them. To test continuation, open a fresh session in that folder and ask it to summarize the saved setup before doing work.

## Explicit-read fallback

If a file-capable host cannot load a native plugin, keep the extracted native bundle together and explicitly ask it to read `core/skills/zaczyn-setup/SKILL.md` and linked conventions under that bundle path. Identify your separate work folder. Move the whole extracted folder, including hidden `.claude-plugin/`, rather than copying only visible files. Do not claim plugin installation when using explicit reads.

## Optional graphical and chat editions

Cowork plugin upload is described in the [Claude guide](adapters/claude/README.md). The optional `zaczyn-chat-0.6.0.zip` uses uploaded references and project instructions; see the [chat guide](adapters/chatgpt/README.md). These paths are separate from native agent installation and are not required for it.

If no usable file access or project sources exist, paste the chat edition's project instructions and relevant reference sections, then keep the generated context documents yourself. Continuation requires providing them again. No automatic persistence is promised.

Use `zaczyn-orchestrate` by name or explicitly ask for cost-aware orchestration when you want the current agent to route a task through available subagents or workflows. It does not turn on automatically for ordinary Zaczyn work. For a demanding task, select the strongest available model with high reasoning effort where offered, then invoke `$zaczyn-orchestrate` in Codex, `/zaczyn-orchestrate` in a Claude Code project, or `/zaczyn:zaczyn-orchestrate` with the Claude plugin, followed by your task. The host's normal permissions apply, with no separate approval requirement for each agent. Fresh-install execution in supported hosts remains unverified; see the [host capability guide](adapters/orchestration.md).

See [verification scope](docs/verification.md) and [updating or changing hosts](docs/migration.md).
