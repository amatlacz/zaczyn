# Choose your agent environment

Zaczyn targets native agent workspaces: Claude Code, Codex, Antigravity, and Kiro. One portable core defines behavior; each host needs an adapter for actual instruction loading, skill discovery, shared references, and workspace access.

- **Claude Code:** install `zaczyn-claude-project-0.6.0.zip` into one project through the [project-only guide](claude-project/README.md), including desktop sessions without a terminal. The [Claude guide](claude/README.md) retains an optional terminal plugin path. Earlier plugin/setup evidence is distinct from the new desktop path; see [verification](../docs/verification.md).
- **Codex:** use `zaczyn-codex-0.6.0.zip` and the [native workspace guide](codex/README.md). The original four exported skills were discovered by Codex CLI 0.153.4 without a model turn. Owner quick-setup artifacts and fresh-session context recovery were also checked; see verification for the wording correction and scope.
- **Antigravity (experimental):** use `zaczyn-antigravity-0.6.0.zip` and the [native guide](antigravity/README.md). The guide covers workspace skills and the editor's context-rule setting; actual host behavior is unverified and testing is deferred.
- **Kiro (experimental):** use `zaczyn-kiro-0.6.0.zip` and the [native guide](kiro/README.md). Complete-folder import and workspace placement preserve references; actual host behavior is unverified and testing is deferred.

The exported skill files are identical across these four workspace packages; only their user guides differ. Codex and Antigravity can share .agents/skills without replacing each other's host instructions. Each skill carries its dependencies; installing a single exported folder does not depend on another skill or the source checkout. Keep all five at the same version when updating the starter.

For delegation, model controls, Microsoft Copilot, and browser reference use, read the [orchestration host guide](orchestration.md). Fresh-install execution of the fifth skill in supported hosts remains unverified.

A host with file access can read the complete framework as described in [START](../START.md). This fallback is useful but does not verify native skill discovery. Keep user-owned AGENTS/PROJECT context and local procedures separate from the framework defaults.

## Optional editions

[Claude Cowork](claude/README.md) has a documented graphical upload path. [ChatGPT and other chat apps](chatgpt/README.md) can use the generated chat edition with manual context saving. [Grok guidance](other-hosts.md) remains staged. These are optional paths, not the required setup for the native framework.

Only observed behavior in the selected host establishes installation, resource access, and persistence. See [verification](../docs/verification.md) for limits; do not substitute browser uploads for native integration work.
