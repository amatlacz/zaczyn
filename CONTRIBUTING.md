# Contributing to Zaczyn

Help people complete useful work and develop a process they can understand and maintain. A contribution can remove instructions as well as add them.

## Useful contributions

- Real examples of friction: the request, available material, result, and where help was needed.
- Small working guidance for the relevant skill or reference that applies to a concrete need without imposing a profession or folder tree.
- Scoped improvements to setup, work, review, or grow, supported by an inspectable example.
- Host adapters with actual installation, resource-access, and context-loading evidence.
- Short examples showing when to keep a prompt, add a rule or template, or retire process.

Formal packs, automatic tool catalogs, and a user-facing CLI are deferred. Prefer proving a local practice first.

## Ground rules

Keep `core/` portable. Host syntax and installation belong in `adapters/`. Shipped defaults must remain separate from workspace customizations. Keep the five entry points short; load supporting references only when useful. Explain guidance in ordinary language and reuse existing domain workflows.

Match verification to the change. A documentation edit needs a consistency check, not an agent benchmark. A behavior change needs a focused case with observable evidence and a case where it should not apply. Set a bounded scope before costly model runs; stop when the question is answered. Do not infer beginner usability from agent simulations or installation success from valid Markdown links.

## Build and check

From the source checkout, with Python 3.9 or newer:

```bash
python3 scripts/build_bundle.py
```

The builder creates six reproducible editions and a `.zip.sha256` sidecar for each:

- `dist/zaczyn-<VERSION>.zip`: native plugin and starter-folder fallback, with the hidden `.claude-plugin/` manifest, portable core, host guides, and examples.
- `dist/zaczyn-claude-project-<VERSION>.zip`: five self-contained project skills for Claude Code desktop/local sessions, with project-only installation instructions.
- `dist/zaczyn-codex-<VERSION>.zip`, `dist/zaczyn-antigravity-<VERSION>.zip`, and `dist/zaczyn-kiro-<VERSION>.zip`: a host guide and five self-contained skill folders for workspace installation/import.
- `dist/zaczyn-chat-<VERSION>.zip`: complete `ZACZYN.md` reference compiled from that core, short project instructions, and chat-specific start/verification guidance.

The GitHub workflow runs the offline checks, builds all editions, and verifies their checksums on pushes and pull requests. It does not call an AI model, install host software, or publish a release. Generated archives stay out of Git; attach the versioned ZIPs and checksum sidecars if you choose to publish a GitHub release.

Edit `core/` and the relevant source under `adapters/`, then rebuild; do not maintain independent exported copies. The native exporter follows resource links, remaps the adapter index to `adapters/native/runtime.md`, and keeps the dependency closure inside each skill. Supporting entries become procedure.md; the AGENTS template is renamed so nested discovery cannot load it as real workspace instructions. Keep host-specific saving behavior in the chat runtime. The compiler converts resource links to internal anchors and rejects missing references. All archives exclude lab material, local settings, test outputs, and contributor tooling. The builder checks the declared public skill entries, native metadata, resource links, extracted bytes, and compiled anchors outside the checkout.

Run the focused offline packaging checks after changing the builder:

```bash
python3 scripts/check_bundle.py
```

If Claude Code is installed, validate the manifest without running an agent:

```bash
claude plugin validate .
```

Verify checksums from the distribution directory with `shasum -a 256 -c *.zip.sha256`. The builder does not install or publish anything. Before advertising a tested host, record its version, successful discovery and invocation, shared-resource loading outside the clone, context behavior, and update/rollback outcome. For chat editions, also verify that a fresh conversation reads saved user context and distinguishes a prepared replacement from an updated project source. CLI simulation does not verify the graphical Cowork or ChatGPT flow. Record limits in [verification](docs/verification.md). Six offline test cases cover all six editions, deterministic builds, source propagation, missing resources, isolated skill copies, identical cross-host skills, and accidental active templates. An actual local skill-discovery API call can add evidence without starting a model turn; it still does not prove behavior. A published download or marketplace entry is a separate release action.

## Sign-off (DCO)

We use the [Developer Certificate of Origin](https://developercertificate.org/). Sign off your commits:

```bash
git commit -s -m "Clarify when a working pattern helps"
```

[MIT license](LICENSE).
