# Host probe

A small diagnostic skill that shows how an app loads Agent Skills: whether it reads a skill at all, whether it opens the files packaged with it, and which folders it looks in.

It is part of [Zaczyn](https://github.com/amatlacz/zaczyn), an open-source, MIT-licensed set of working practices for AI assistants. The probe exists to check which apps can run its skills.

The skill itself only replies with a few fixed lines: it makes no network calls, reads no other data and changes nothing. Uploading it stores a copy in your Microsoft 365 storage, and step B4 separately asks Cowork to edit one test file. The clean-up section removes all of it.

The probe answers with fixed codewords. A codeword in the reply shows the app read that file; `CANNOT OPEN` or a missing line shows it did not.

| Where the codeword is | Codeword |
|---|---|
| Skill body (`zaczyn-probe/SKILL.md`) | OWL-17 |
| `zaczyn-probe/references/probe-detail.md` | LANTERN-42 |
| `zaczyn-probe/assets/probe-template.md` | KETTLE-63 |
| Single-file skill (`zaczyn-probe-single.md`) | MAPLE-08 |

## Get the files

1. Open https://github.com/amatlacz/zaczyn and select **Code** → **Download ZIP**.
2. Right-click the downloaded `zaczyn-main.zip` → **Extract All**. Open the extracted folder (it may contain another `zaczyn-main` folder) and find `probe`. Do not work from inside the ZIP.

| File or folder | Used in |
|---|---|
| `zaczyn-probe.zip` | B1, B5: skill with companion files, `SKILL.md` at the archive root |
| `zaczyn-probe-single.md` | B3, B4, B6: single-file skill |
| `single-as-SKILL/SKILL.md` | B3: the same single file, named `SKILL.md` |
| `probe-state.md` | B4: file for the write test |
| `vscode-agents`, `vscode-github` | A1, A2: folders to open in VS Code |

Do not unpack `zaczyn-probe.zip`; upload it as it is.

## Part A: GitHub Copilot in Visual Studio Code

Needs VS Code signed in to GitHub with a Copilot plan. Keyboard shortcuts: Windows first, macOS in brackets.

**A1. Skills in `.agents/skills`.**
1. **File** → **Open Folder** → select `probe/vscode-agents`. If VS Code asks whether you trust the authors, choose **Trust**: the folder holds only Markdown files, with no code, settings or extensions, and Restricted Mode turns agents off.
2. Open the chat: **Ctrl+Alt+I** (⌃⌘I), or the **Chat** menu in the title bar → **Open Chat**.
3. Select **+** (New Chat). Below the input box set **Session Target** to **Copilot** (not Claude, not Codex), the agent to **Agent** and the model to **Auto**. If there is no Session Target picker, note that and continue.
4. Type only `/` in the input box. Note whether `zaczyn-probe` is in the list, and which other skills appear.
5. Send `Run the Zaczyn probe` and record the reply.

The VS Code documentation does not say whether Copilot reads `.agents/skills`, so "not listed" is a valid result. Record it and continue with A2.

**A2. Skills in `.github/skills`.** Repeat A1 with `probe/vscode-github`.

**A3. If the skill does not appear.** Open the Command Palette (**Ctrl+Shift+P**, ⇧⌘P) → **Chat: Open Customizations** → **Skills**. It lists every skill VS Code found, its folder and any error. Note what it shows and your Copilot plan (Free, Pro, Business, Enterprise).

## Part B: Microsoft Copilot (work or school account)

Open https://copilot.cloud.microsoft in Edge or Chrome and sign in. The label next to your profile in the left pane must say **Work**. Microsoft is rolling out a new Home view, so the screen may differ slightly; in that view the Chat | Cowork switch sits in the input box.

**B0. What is available.** Note whether there is a **Chat | Cowork** switch at the top. Cowork needs a Microsoft Copilot licence and is switched on by the organisation's administrator. Without it, skip to B5.

**B1. Cowork: upload the skill with companion files.**
1. Select **Cowork**.
2. In the left pane select **Customize** → **Skills** tab.
3. Select the arrow next to **Add** → **Upload skill** → choose `zaczyn-probe.zip`. Cowork may remind you to upload only trusted skills; this one contains only the text you can read in `zaczyn-probe/`.
4. Note whether it was accepted, or the exact error message.

**B2. Cowork: run it.**
1. Start a new Cowork task and send `Run the Zaczyn probe`. Record the reply.
2. Start another new task and type `/zaczyn-probe` without sending it. Note what the menu shows. If the skill is offered, select it, send `Run the Zaczyn probe` and record the reply.

**B3. Cowork: single-file skill.**
1. As in B1, upload `zaczyn-probe-single.md`. If it is rejected, upload `single-as-SKILL/SKILL.md` instead.
2. Start a new task and send `Run the single Zaczyn probe`. Record the reply. If it shows OWL-17 instead of MAPLE-08, the other skill answered; record that.

**B4. Cowork: write to OneDrive.**
1. Open OneDrive (app launcher in the top-left corner → **OneDrive**). Create a folder `Zaczyn-probe` and upload `probe-state.md` and `zaczyn-probe-single.md` into it.
2. Start a new Cowork task and send:

   ```
   Open probe-state.md in my OneDrive folder Zaczyn-probe. Change "Current step: 1" to "Current step: 2", add the log line "- Edited by Cowork.", and save the file in place. Then tell me whether you overwrote it or saved a new file.
   ```

3. Record the reply and what the folder shows afterwards: the same file changed, a new file next to it, a Word file instead of `.md`, or a refusal.

**B5. Copilot Chat: personal skill.**
1. Switch to **Chat**.
2. Select **Agents** → **More agents** and check whether `zaczyn-probe` from B1 already appears among your skills. If it does, go to point 4.
3. Select the arrow next to **Add** → **Upload skill**, choose `zaczyn-probe.zip` and save.
4. In a new chat send `Run the Zaczyn probe` and record the reply. If no PROBE lines come back, type `/`, select `zaczyn-probe`, send the same sentence and record that reply too.

**B6. Copilot Chat: file reference with `/`.**
1. If you skipped B4, open OneDrive, create a folder `Zaczyn-probe` and upload `zaczyn-probe-single.md`. A new file can take a few minutes to appear in Copilot's file search.
2. In a new chat type `/`, then `zaczyn-probe-single`, and look at the **Files** tab.
3. If the file appears, select it and add `Read the referenced file in full and follow it.` Record the reply.
4. Note whether the file could be selected at all.

## Clean up

- Cowork: **Customize** → **Skills**, remove `zaczyn-probe`, `zaczyn-probe-single` and any numbered copies such as `zaczyn-probe-2`.
- Chat: **Agents** → **More agents**, remove `zaczyn-probe` and any numbered copies.
- OneDrive: delete the `Zaczyn-probe` folder. Then open **My files** → **Documents** → **Cowork** → **skills** and delete the items whose names start with `zaczyn-probe`.

## Results

```
A1 Session Target picker: yes/no | listed: yes/no | other skills: | reply:
A2 Session Target picker: yes/no | listed: yes/no | other skills: | reply:
A3 (only if needed):
Copilot plan:
B0 Cowork switch: yes/no
B1 upload: accepted / error:
B2 reply: | "/zaczyn-probe" menu showed: | reply after selecting:
B3 upload (.md / SKILL.md): | reply:
B4 reply: | folder shows:
B5 already listed: yes/no | reply: | reply after selecting with /:
B6 file selectable: yes/no | reply:
```

## Maintainers

Edit only `zaczyn-probe/` and `zaczyn-probe-single.md`, then run `python3 scripts/build_probe.py`. `scripts/check_bundle.py` fails if the derived files or the ZIP differ from their source.

Sources: [Cowork skills](https://learn.microsoft.com/en-us/copilot/cowork/cowork-customize), [Copilot Chat skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/build-copilot-chat-skills), [file references](https://support.microsoft.com/en-us/microsoft-365-copilot/refer-to-specific-files-and-more-in-microsoft-365-copilot), [VS Code agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [VS Code agent harnesses](https://code.visualstudio.com/docs/agents/run/agent-harnesses).
