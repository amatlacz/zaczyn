# Native workspace adapter

These exported skills target Claude Code, Codex, Antigravity, and Kiro. Select the instructions for the host actually running this session, not the app that last edited the project. Codex and Antigravity may share .agents/skills; their exported skill contents are identical. Claude Code uses project-local .claude/skills; Kiro uses .kiro/skills. Supporting procedure copies are references, not additional installed skills.

Keep the selected work folder separate from this installed skill directory. Save AGENTS.md and PROJECT.md in the work folder when setup calls for them. Shipped templates are not existing user context. Keep personal procedures and preferences outside shipped Zaczyn skill folders and read only relevant resources.

## Claude Code — project skills

These skills are installed in the selected workspace's .claude/skills directory. Invoke /zaczyn-setup, /zaczyn-work, /zaczyn-review, /zaczyn-grow, or /zaczyn-orchestrate. This installation has no plugin namespace and needs no --plugin-dir flag or account-wide installation. In the desktop app, use a local Code session opened on that work folder.

Setup creates or merges root CLAUDE.md with @AGENTS.md; AGENTS points to PROJECT in ordinary language. Preserve unrelated existing CLAUDE instructions and existing authority. Save user context at the project root, not inside .claude/skills. Never install into the user's home .claude directory for a project-only request. If discovery is stale, start a fresh local session in that same folder. File placement alone is not a verified desktop invocation.

Official mechanisms: [project skills](https://code.claude.com/docs/en/skills), [desktop skills](https://code.claude.com/docs/en/desktop), [context](https://code.claude.com/docs/en/memory).

## Codex

Use the native skill selector or name zaczyn-setup/work/review/grow/orchestrate. In CLI/IDE, `$zaczyn-setup` explicitly selects setup. Codex reads workspace AGENTS.md, which points to PROJECT.md. Respect AGENTS.override.md and closer instruction precedence; no CLAUDE wrapper is needed. If skills do not refresh, start a new session or restart the app.

Official mechanisms: [skills](https://learn.chatgpt.com/docs/build-skills), [context](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Antigravity

Ask for the skill by name in a new conversation. Current workspace discovery uses .agents/skills. For editor context, use Customizations → Rules to create or reuse a workspace rule set to Always On that says: “Read AGENTS.md in the workspace root before work; follow its PROJECT.md pointer.” Keep it a pointer, not a copy of preferences. Verify the rule's activation setting through the UI; a Markdown file alone does not prove Always On is configured. If the actual host already demonstrably loads AGENTS, reuse that mechanism.

Official mechanisms: [skills](https://antigravity.google/docs/skills), [rules](https://antigravity.google/docs/rules-workflows).

## Kiro

Ask for the skill by name. Workspace skills live in .kiro/skills; the IDE's Agent Steering & Skills panel also supports Import a skill → Local folder. Import a complete exported folder. Kiro documents root AGENTS.md loading, so no duplicate steering wrapper is needed for the default agent. Custom agents have their own resources configuration; verify it instead of assuming default discovery.

Official mechanisms: [skills](https://kiro.dev/docs/skills/), [steering](https://kiro.dev/docs/steering/).

## Orchestration

Use `zaczyn-orchestrate` only when named or explicitly requested for cost-aware orchestration. Inspect the running host for available delegation, models, efforts, and permissions; same-model subagents are not assumed to save cost. Claude Code subagents can use supported per-agent model/effort settings, subject to effective configuration. Codex supports explicit spawn settings, defaults, and custom agent files when its subagent tools are enabled. Kiro has subagents and optional workflows, with model controls depending on client and agent configuration. Antigravity delegation is unverified here. The main agent owns routing, integration, and the result. See the [host capability guide](../orchestration.md) for current official references.

## Verify the actual state

Distinguish copying folders, native discovery, successful invocation/resource access, and fresh-session context loading. Record scope and observed evidence for each claim. This adapter does not prove a connected tool is installed, signed in, or usable. Configure only selected additions through supported host mechanisms. When a UI-only step cannot be performed with available tools, give the precise action and leave that state unverified.
