# Single-file skills

Use the **single-file edition** (`zaczyn-single-0.6.0.zip`) when your app cannot install a skill folder: a browser assistant, an office assistant that accepts one uploaded file, or any chat where you can attach, reference, or paste a document. Each `zaczyn-<skill>.md` holds one skill with everything it needs. Setup, work, review, and grow are included; orchestrate is not, because it needs an app that can start other agents.

Pick the first way your app allows:

1. **Upload as a skill.** If the app accepts a single Markdown skill file, upload `zaczyn-review.md` (or another). If it insists on the name `SKILL.md`, copy the file, rename the copy to `SKILL.md`, and upload that. If it accepts only a ZIP, put that one `SKILL.md` into a ZIP on its own, without a folder around it.
2. **Attach or reference the file.** Keep the files in a folder your assistant can read, then attach the file to the conversation or reference it (in many apps by typing `/` and the file name) and say: “Read this file in full and follow it for my task: <task>. First say which file you are following.”
3. **Paste it.** As a last resort, paste the file's text at the start of a conversation with the same request.

Your own context stays in two documents you keep in one folder: `AGENTS.md` (how you want to work) and `PROJECT.md` (facts and scope). Setup prepares them. Attach or reference them at the start of a new conversation; most browser assistants do not load them by themselves.

Status: these files are generated from the same core as the other editions and pass the package checks. Whether a particular app accepts the upload, reads the whole file, or can save documents has not been observed yet; see [verification](../../docs/verification.md). The `probe/` folder in the repository contains a small test you can run in your app.
