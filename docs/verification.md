# What has been checked

Updated 2026-09-10. Current edition: **0.5.2**. Source implementation, package integrity, actual host behavior, and beginner usability are separate claims.

## Claude Code project installation: 0.5.2

The 0.5.1 Claude download offered a session-loaded plugin and omitted an approachable project-only desktop path. Version 0.5.2 adds `zaczyn-claude-project-0.5.2.zip`, with four complete exported skills for `XYZ/.claude/skills/`. The README now leads with copying the extracted download into XYZ and asking the local agent to install it there. Project commands use `/zaczyn-setup` without a plugin namespace. The native runtime includes the Claude `CLAUDE.md` → `AGENTS.md` → `PROJECT.md` context chain.

The six offline packaging cases cover all six editions, including isolated copies of the new Claude skills. Actual Claude desktop discovery/invocation has not been observed for this package. The official [skills](https://code.claude.com/docs/en/skills) and [desktop](https://code.claude.com/docs/en/desktop) documentation establish the project-skill mechanism; earlier CLI plugin evidence below is not a desktop installation test. No new model test or global installation is performed for this correction. Published 0.5.1 assets remain unchanged.

## Acceptance for 0.5.1

The maintainer accepted the bounded Claude Code and Codex evidence for this version and explicitly deferred Antigravity/Kiro testing. Those two packages remain experimental, with no runtime-support claim. Further model tests and novice observation are not requirements for this source handoff. The unverified 0.5.1 wording regeneration and optional chat failure remain documented limitations, not passing tests. Release downloads and source history are available from [the 0.5.1 release page](https://github.com/amatlacz/zaczyn/releases/tag/v0.5.1). Publication does not extend the test coverage described here.

## Native delivery: 0.5

Five local ZIPs are generated from one core: Claude, Codex, Antigravity, Kiro, and an optional chat edition. The three new workspace packages contain exactly four independently installable skills. Resource links resolve inside each skill after an isolated copy; supporting procedure/template files cannot become extra SKILL.md or AGENTS.md entries. The three packages share identical skill bytes, allowing Codex and Antigravity to use the same workspace directory.

Six offline test cases passed across all editions: resource completeness and source propagation, rejected missing/escaping links, isolated skill copies, no active template filenames, version consistency, and reproducible extraction/checksums. The Claude manifest also passes validation.

**Codex CLI 0.153.4 discovery passed:** a local app-server skills/list request found all four skills enabled with repository scope in a disposable workspace. Codex used a temporary state directory. No thread or model turn was started, and no account allowance was used. An initial attempt could not open the normal state database under the filesystem sandbox; its error is retained separately. Discovery is narrower evidence than successful skill execution or desktop UI installation.

Antigravity and Kiro packages follow current official skill/context documentation and pass package checks. Actual host discovery, invocation, editor rule activation, and fresh-session context remain unverified in those apps; testing is deferred by the maintainer. Their CLIs were not available on PATH for this check; this is not a claim that the apps are absent from the computer.

The 0.5 source also clarifies active-rule ownership and capability-status evidence following the owner's test. No new behavioral model run was performed for those wording changes. Earlier successful Claude setup/resume evidence below applies to the tested 0.4 versions; it is not silently promoted to a full 0.5 pass. Marketplace publication, a general-purpose installer, and real novice observation remain outside these checks.

## Owner Codex quick setup: 0.5.0 and the 0.5.1 correction

The owner reported a completed quick setup in the prepared native Codex workspace. Direct file inspection confirmed minimal AGENTS/PROJECT, separated preferences/facts, a conditional solo-workflow rule, and no selected extra tools or templates. The instruction “Review workshop material” left the reviewer ambiguous despite the user specifying themselves. Original artifacts were retained before a maintainer corrected that line to require user review and authorization.

Version 0.5.1 makes preservation of the responsible actor explicit in shared context guidance. This wording patch has not had a model regeneration check. It does not change the native skill names, discovery layout, or host adapter. The supplied completion message is not a native invocation trace.

The owner then supplied a fresh-session response that recovered the solo workflow, beginner audience, lightweight setup, and explicit user review/authorization before sharing. This bounded context-recovery check passed. Direct SHA-256 comparison confirmed that AGENTS and PROJECT were unchanged from the corrected/original snapshots respectively. The response reports no file changes; only those two context files were independently compared. Installed skills were still 0.5.0 and the reviewer sentence had been corrected by the maintainer, so this is not an independent generation test of the 0.5.1 patch.

## Earlier onboarding checks: 0.4 and 0.4.1

Implemented quick/guided/deep setup; selected customization with status and undo; AGENTS behavior and PROJECT facts; partial setup checkpoints; native and generated chat editions; graphical-first guides and migration. These describe the intended behavior, not a guarantee that every model will follow it.

Offline verification passed:

- The native edition contains exactly four skill entries, a matching 0.4.1 manifest, shared resources, and user guidance. Claude Code 2.1.263 accepts its manifest.
- Both editions extract outside the source checkout with byte-identical files and valid packaged links. Chat links resolve to compiled source anchors.
- Every core Markdown resource occurs once in the compiled chat reference. A source change propagates to that reference; a missing shared resource is rejected.
- Repeated builds are byte-identical. SHA-256 sidecars identify each artifact. Broken compiled anchors and links escaping the edition are rejected.

The 0.4.1 patch adds a shared context-fidelity check: preserve the user’s conditions, keep behavior in AGENTS, and omit or label unsupported inferences. It addresses the quick-setup finding below in source. Offline package checks pass; no additional maintainer model run was performed. Existing user workspaces are not automatically migrated.

Three approved **0.4.0** model checks ran once on Claude Code 2.1.263, using **$0.68** total reported API-equivalent capacity:

- **Depth choice passed:** the native setup skill loaded from the extracted bundle, offered quick/guided/deep, and waited without executing the example task or creating files.
- **Quick setup partially passed:** it saved exactly AGENTS.md, PROJECT.md, and CLAUDE.md importing AGENTS, and stopped without creating an agenda or task scaffold. It also overgeneralized “review before sharing” into a permanent ban on sending/publishing and duplicated sharing behavior in PROJECT. The 0.4.1 correction addresses these findings. A subsequent owner-supplied artifact check confirms conditional sharing language; some rule duplication remains.
- **Chat simulation failed:** with tools disabled, Claude returned command-call-shaped text instead of the requested replacement context documents. No command executed. This was a Claude Code simulation using the compiled reference, not an actual ChatGPT project test; the failure's cause remains unresolved.

All three processes exited successfully and the shipped bundles stayed unchanged. Process success does not mean the requested behavior passed. No paid retries ran. These behavioral results apply to the retained 0.4.0 artifacts. The owner-supplied artifact evidence below supports the narrow 0.4.1 correction; the chat failure remains unresolved.

On 2026-09-09, the owner supplied AGENTS/PROJECT files from a native Claude Code test of 0.4.1 and confirmed that the listed additional preferences were provided or accepted during setup. The review-before-sharing condition was preserved correctly. Some active rules still recur in PROJECT, and the capability section mixes availability claims with explicitly unverified connections. This is an artifact review with owner confirmation, not a transcript audit, tool-access test, wrapper inspection, or fresh-session loading test. Native agent workspace support is the main product direction; the chat edition is optional.

The owner then supplied a fresh-session Claude Code response that correctly recovered the saved workflow, approval conditions, and deferred choices without drafting workshop content. That bounded, owner-reported context-recovery check passes. The detailed tool trace and wrapper were not inspected; invocation and tool-access claims still need their own evidence.

Graphical Cowork installation and ChatGPT upload/fresh-chat persistence remain **unverified**. A local macOS UI-capture error prevented interface inspection; no upload or installation was performed. Published host documentation informed the adapters. Kiro, Antigravity, and Grok remain staged targets, not verified native integrations.

## Optional graphical acceptance check

Use a disposable work folder or chat project with fictional material. Keep personal context and the installed reference separate.

1. Follow the guide for your actual app. Confirm the native plugin was discovered, or that the chat project can read ZACZYN.md and its project instructions. Explicit file reading is a fallback, not a successful native install.
2. Say: “Help me set up AI for recurring workshop preparation. An example task is a 60-minute agenda. I am new to this.” Expect a quick/guided/deep choice and relevant discovery; no real agenda yet.
3. Choose quick setup. State a preference and decline extra tools. Expect minimal AGENTS/PROJECT context and a choice to begin work, customize further, or stop. In Claude Code, verify CLAUDE imports AGENTS. In chat, add the prepared documents to project sources.
4. Ask to deepen the setup, select one useful practice, then pause. Check that selected/deferred items and the next question are saved. Start a fresh conversation using those saved documents; it should resume without repeating the whole interview.
5. Ask for an unavailable integration. Expect a truthful blocked/proposed status and a usable alternative. A generated recipe is not a verified installed skill.
6. Explicitly request a small task, a review without editing, and a scoped process improvement. Confirm those intents work independently. Replace changed chat sources and verify access in a fresh conversation; a download alone is insufficient.

Record the host/interface version, exact prompt, observed files/source changes, any missing resources, and what still needs a manual action. Do not infer usability from your own familiarity with the framework.

## Historical 0.3 evidence

The following checks apply to the earlier task-led setup and PROJECT-based context, **not the new 0.4 onboarding**. They remain useful compatibility evidence; they do not prove the replacement behavior or graphical paths.

### Claude Code 2.1.263

A session loaded the ZIP's extracted bundle outside the source checkout and successfully invoked setup, work, review, and grow through the Skill tool. The assistant read the shared conventions, drafted an invitation from supplied facts, reviewed it without subsequent changes to that draft, and saved a scoped rule in the workspace with undo guidance. The bundled defaults remained byte-identical. It followed an instruction imported from PROJECT through CLAUDE before any file read.

An explicit-read fallback then exposed a wording problem: setup treated a quick task as a reason to omit PROJECT. The instructions now distinguish minimal context during explicit setup from an optional task record during quick work. A focused rerun created PROJECT, the Claude pointer, and the requested draft, with no task folder.

These checks used an authenticated Claude Code session with an explicit bundle path. They do not verify persistent installation, marketplace delivery, Cowork, all host settings, or automatic skill selection in every request.

### Updating without overwriting local work

A manual side-by-side update used 0.3.0, a simulated changed next version, and rollback. Local rules, the task-template override, a customized legacy jar, existing task records, and outputs stayed byte-identical. The selected default changed and reverted as expected. This is file-operation evidence; there is no automatic updater or merge mechanism.

### Mixed records, continuation, and language

Two independent sessions used a project with legacy brief/plan records and a conflicting task note. The first surfaced the conflict without choosing authority. After an explicit decision, the fresh session preserved historical criteria, updated the selected October artifact, and left the task open for coordinator acceptance. November and shared material stayed unchanged. Conversation remained Polish and the invitation English. A separate plan-only task used the workspace-local template; the requested deliverable was not executed.

This focused case passed its scope, authority, language, and local-template checks. One bookkeeping limitation remained: an older plan step still said drafting was underway even though its dated progress correctly recorded completion and the pending approval. These results do not establish flawless behavior or coverage of every language and workspace layout.

## Deferred work and publication

The earlier comparison and bounded host checks do not establish broad superiority or novice usability. A real inexperienced-user observation and publication remain deferred by the owner. Version 0.5.1 is distributed through GitHub release archives and a source tag. No marketplace listing is provided. The release includes the bounded evidence above; deferred tests remain unverified.
