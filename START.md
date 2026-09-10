# Start with Zaczyn

Zaczyn runs in a native agent working with your project folder. Choose the package for the app you use. You can leave the extracted download in Downloads; the host guide explains which four folders to install in your work project.

| App | Package and instructions |
|---|---|
| Claude Code | `zaczyn-0.5.1.zip`; [Claude guide](adapters/claude/README.md) or the source-checkout path below |
| Codex | `zaczyn-codex-0.5.1.zip`; [Codex guide](adapters/codex/README.md) |
| Antigravity (experimental) | `zaczyn-antigravity-0.5.1.zip`; [Antigravity guide](adapters/antigravity/README.md) |
| Kiro (experimental) | `zaczyn-kiro-0.5.1.zip`; [Kiro guide](adapters/kiro/README.md) |

Download the prepared ZIP from the [0.5.1 release page](https://github.com/amatlacz/zaczyn/releases/tag/v0.5.1). Choose the named app package above, not GitHub's automatically generated source-code archive. Ordinary users do not need to clone or build the repository. You need the selected AI app installed and working before installation.

## Claude Code

Keep the framework and your work in separate folders:

- **Framework folder:** the extracted `zaczyn-0.5.1.zip`, or an existing Zaczyn source checkout. It must contain `core/` and the hidden `.claude-plugin/` directory. Keep the complete folder together.
- **Work folder:** the project you want to customize. This is where AGENTS.md, PROJECT.md, and your outputs belong.

Open a terminal in your work folder and launch Claude with the path to the framework folder:

```bash
claude --plugin-dir /absolute/path/to/zaczyn
```

Replace the example path with the actual framework folder. If you already have a source checkout, no ZIP extraction or copying is needed. This flag loads the plugin for that Claude terminal session; it does not install it into another app window. See the [Claude guide](adapters/claude/README.md) for discovery checks and current interface limits.

Inside that session, use `/zaczyn:zaczyn-setup` and describe your work. No browser upload is part of this path.

## Codex, Antigravity, and Kiro

Extract the matching host ZIP and read its README. It contains a `skills/` directory with four complete skill folders. Ask the agent to install them into your selected work folder following that README, or copy them manually to the documented destination. Codex and Antigravity use `.agents/skills/`; Kiro uses `.kiro/skills/` or its local-folder import UI. No terminal installer is required for these packages.

These are workspace skill packages distributed as GitHub release downloads; they are not marketplace installations. Codex discovery and bounded owner setup/context checks are recorded. Antigravity/Kiro are experimental: their actual host behavior is unverified, and testing is deferred. See [verification](docs/verification.md). An agent must distinguish copying files from verifying discovery and use.

## Your first conversation

> Help me customize this for [my project, recurring work, or personal assistant]. I want to see useful possibilities before starting a task.

Choose **quick**, **guided**, or **deep** when offered, or name the depth in that first message. Quick aims for a short exchange; guided explores your working needs; deep can continue over several sessions. You can skip questions, stop, or change depth.

The assistant should reuse what you already told it, suggest concrete options, let you choose, and save the setup. An example task describes your needs; it is not automatically executed. At the end, choose to begin work or customize further. Ask “Save our setup progress” whenever you want to stop.

## Your files and the shipped reference

Your behavior and preferences belong in AGENTS.md; project facts belong in PROJECT.md. Extra profiles and procedures are optional. Keep them separate from the shipped Zaczyn bundle/reference so an update does not replace your customizations.

In native workspaces, keep these files in your selected work folder. Host-specific loading instructions must point to them; the folder name alone does not prove the agent reads them. To test continuation, open a fresh session in that folder and ask it to summarize the saved setup before doing work.

## Explicit-read fallback

If a file-capable host cannot load a native plugin, keep the extracted native bundle together and explicitly ask it to read `core/skills/zaczyn-setup/SKILL.md` and linked conventions under that bundle path. Identify your separate work folder. Move the whole extracted folder, including hidden `.claude-plugin/`, rather than copying only visible files. Do not claim plugin installation when using explicit reads.

## Optional graphical and chat editions

Cowork plugin upload is described in the [Claude guide](adapters/claude/README.md). The optional `zaczyn-chat-0.5.1.zip` uses uploaded references and project instructions; see the [chat guide](adapters/chatgpt/README.md). These paths are separate from native agent installation and are not required for it.

If no usable file access or project sources exist, paste the chat edition's project instructions and relevant reference sections, then keep the generated context documents yourself. Continuation requires providing them again. No automatic persistence is promised.

See [verification scope](docs/verification.md) and [updating or changing hosts](docs/migration.md).
