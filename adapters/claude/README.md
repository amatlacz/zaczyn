# Claude Code installation

For one project in the Claude Code desktop app, use `zaczyn-claude-project-0.7.0.zip` and the [project-only instructions](../claude-project/README.md). They explain how to put the extracted download in your existing XYZ folder and ask Claude to install its five skills there. No terminal command or global installation is required. Project skills use `/zaczyn-setup`, `/zaczyn-work`, `/zaczyn-review`, `/zaczyn-grow`, and `/zaczyn-orchestrate`.

Use orchestrate only by name or an explicit cost-aware orchestration request; see the [host capability guide](../orchestration.md).

The plugin package `zaczyn-0.7.0.zip` remains an alternative for terminal users and plugin workflows. Its complete folder contains `.claude-plugin/plugin.json`, core skills, and shared references. The following section applies to that alternative only.

## Optional terminal plugin path

Extract the complete native bundle, retaining the hidden `.claude-plugin/` folder. From your work folder launch:

```bash
claude --plugin-dir /absolute/path/to/zaczyn-0.7.0
```

| Intent | Command |
|---|---|
| Setup | `/zaczyn:zaczyn-setup` |
| Work, plan, resume, organize | `/zaczyn:zaczyn-work` |
| Review | `/zaczyn:zaczyn-review` |
| Grow | `/zaczyn:zaczyn-grow` |

The flag loads that plugin for this terminal session. It does not configure a different app window. Check the five entries before testing behavior. If missing, verify the exact folder contains `.claude-plugin/plugin.json` and `core/`, then run:

```bash
claude plugin validate /absolute/path/to/zaczyn-0.7.0
```

After repairing a package, exit and relaunch with the flag. A response that finds a different source checkout is not a successful plugin test. Persistent installations require their own host verification; session loading is the bounded testing path here. See the [plugin reference](https://code.claude.com/docs/en/plugins-reference).

## Optional Claude Cowork path

1. Open **Customize → Plugins** in Claude.
2. Choose the upload option and select the native ZIP. Upload the whole ZIP; do not manually select its visible contents.
3. Inspect the installed plugin and its five skills. Select your actual work folder, not a source checkout or extracted bundle.
4. Invoke setup from the available skills and describe the project, recurring work, or personal assistant you want to customize. Ask for a quick setup, or for a guided or deep one if you want more questions and suggestions.
5. Confirm the assistant can read its shared resources and save your AGENTS/PROJECT context in the chosen folder. If a resource is unavailable, stop and diagnose the selected package instead of silently using another checkout.

Plugin upload is documented in [Cowork's guide](https://claude.com/docs/cowork/guide/plugins). A documented flow is not proof this version has passed it; see [verification scope](../../docs/verification.md). A normal Claude Chat conversation is not the same as Cowork; use an explicit reference/upload workflow if native plugins are unavailable there.

## Workspace context

For a new local setup, create AGENTS.md for working behavior and PROJECT.md for facts/scope. AGENTS tells the assistant when to read PROJECT in ordinary language. For Claude Code, create or merge a CLAUDE.md wrapper importing AGENTS with `@AGENTS.md`. Retain unrelated existing instructions; do not duplicate all project facts in the wrapper.

For an existing workspace, preserve its current authority until a requested migration. A legacy `@PROJECT.md` import is not broken; moving its behavior into AGENTS should preserve each preference once and update its old location. See [migration](../../docs/migration.md). Claude's [memory documentation](https://code.claude.com/docs/en/memory) describes importing AGENTS; the `@` syntax itself is Claude-specific.

In Cowork, verify actual context loading in the selected folder. If unverified, explicitly ask it to read AGENTS and PROJECT before continuing. Do not infer that a plugin-root context file configures every workspace.

## Fallback

If upload or native discovery fails, keep the complete extracted bundle in a folder the assistant can read, identify the actual work folder, and explicitly request setup from its full file path. Read [START](../../START.md) for this fallback. If local files are unavailable, use the [chat edition](../chatgpt/README.md) as explicit guidance with manual saving; do not call it a native Claude plugin installation.
