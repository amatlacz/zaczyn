# Single-file runtime

This file is one complete Zaczyn skill with the parts it needs, for apps that work with one file: a skill uploaded to a browser assistant, a document attached or referenced in a chat, or pasted text. The sections after the skill are its references, not separate skills.

- Say once, at the start, which file you are following and whether the app loaded it as a skill or the user attached or pasted it.
- Work only with what this app can actually open. If a step needs a file, folder, or tool you cannot reach, say which, and continue only with steps that do not depend on it.
- Keep the user's working context in documents they own: AGENTS for how to work and PROJECT for facts and scope, in one folder the user names, with those names visible in the file names. Read them when the user attaches or references them; do not assume they were loaded.
- If you can create or edit files in that folder, save there and reopen the file to confirm the change. If you cannot overwrite a file, save a dated replacement next to it and say which one is current. If you cannot save at all, return the complete replacement text with the exact file name.
- Never say a document was saved, a skill installed, or a setting changed without seeing it happen. A drafted document is prepared, not saved.
- The approval rule for connected systems in the workspace conventions covers every connection this app has, such as mail, calendar, chat, trackers, and shared documents.
- Other Zaczyn skills mentioned here are separate files; use them only if the user provides them.
