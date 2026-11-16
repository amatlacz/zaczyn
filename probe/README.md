# Host probe

A small diagnostic skill that shows how an app loads Agent Skills: whether it accepts a skill at all, whether it opens the files packaged with it, and which folders it looks in.

It is part of [Zaczyn](https://github.com/amatlacz/zaczyn), an open-source, MIT-licensed set of working practices for AI assistants. The probe exists to check which apps can run its skills.

The skills only reply with a few fixed lines: they make no network calls, read no other data and change nothing. Uploading one stores a copy in your Microsoft 365 storage, and step C3 separately asks Cowork to edit one test file. The clean-up section removes all of it.

The replies contain fixed codewords. A codeword shows the app read that file; `CANNOT OPEN` or a missing line shows it did not.

| Where the codeword is | Codeword |
|---|---|
| Body of every `SKILL.md` | OWL-17 |
| `references/probe-detail.md` | LANTERN-42 |
| `assets/probe-template.md` | KETTLE-63 |
| `zaczyn-probe-single.md` | MAPLE-08 |

## Get the files

1. Open https://github.com/amatlacz/zaczyn and select **Code** → **Download ZIP**.
2. Right-click the downloaded `zaczyn-main.zip` → **Extract All**. Open the extracted folder (it may contain another `zaczyn-main` folder) and find `probe`. Do not work from inside the ZIP.

| File or folder | What it is |
|---|---|
| `upload/1-basic/SKILL.md` | Smallest possible skill: one file, two header fields |
| `upload/2-zip/zaczyn-probe-zip.zip` | The same smallest skill, packed in a ZIP |
| `upload/3-reference/zaczyn-probe-ref.zip` | ZIP with the skill plus one file in `references/` |
| `upload/4-full/zaczyn-probe.zip` | ZIP with `references/` and `assets/`, and extra header fields (`license`, `metadata`) |
| `upload/5-single/zaczyn-probe-single.md` | Single-file skill under its own name, for the `/` file reference |
| `vscode-github`, `vscode-agents` | Folders to open in VS Code |
| `probe-state.md` | File for the Cowork write test |

Upload the `.zip` files as they are; do not unpack them. If your browser saved a file under a changed name, such as `zaczyn-probe (1).zip`, rename it back so your results match these instructions. Do not rename `SKILL.md`.

Whenever an upload fails, write down the error message **word for word**. "Validation error" alone does not say which rule failed; the exact wording usually does.

## Part A: GitHub Copilot in Visual Studio Code

Keyboard shortcuts: Windows first, macOS in brackets.

**A0. Check what the organisation allows (two minutes).**
1. **Help** → **About**: note the version. Skills need 1.109 or later (1.108 only with the setting `chat.useAgentSkills` turned on).
2. Open the Command Palette (**Ctrl+Shift+P**, ⇧⌘P) and run **Developer: Policy Diagnostics**. A report opens. Copy only these values into the results, not the whole report:
   - the state under **Account Policy Gate**. `restricted` means AI features are limited until you sign in to Copilot with an account from an organisation your company has approved;
   - the values of `ChatAgentMode`, `ChatStrictPluginOnlyCustomization` and `UpdateMode` in the **Applied Policy** table, or "not listed". `ChatStrictPluginOnlyCustomization` blocks skills stored in folders; `ChatAgentMode` set to off removes agent mode, and skills with it.

**A1. Skills in `.github/skills`.**
1. **File** → **Open Folder** → select `probe/vscode-github` itself, not its parent. In the Explorer the top name must be `vscode-github`, with `.github` directly inside. If VS Code asks whether you trust the authors, choose **Trust** if your organisation's rules allow it; you can first check in the Explorer that the folder contains only `.md` files.
2. Look at the top of the window and the status bar for **Restricted Mode**. If it is shown, select **Manage** and trust this folder; in Restricted Mode agents and skills are off. Note whether it appeared.
3. Open the chat: **Ctrl+Alt+I** (⌃⌘I), or the **Chat** menu in the title bar → **Open Chat**.
4. Select **+** (New Chat). Always start a new chat after opening or trusting a folder; an older chat does not see new skills.
5. Below the input box: set **Session Target** to **Copilot** if that picker exists, and the mode to **Agent**. Note whether **Agent** can be selected at all.
6. Type only `/`. Note whether `zaczyn-probe` is in the list.
7. Send `Run the Zaczyn probe` and record the reply.
8. Command Palette → **Chat: Open Customizations** → **Skills**. Note whether `zaczyn-probe` is listed, from which folder, and any error shown.

**A2. Skills in `.agents/skills`.** Repeat A1 with `probe/vscode-agents`. The VS Code documentation lists `.agents/skills` only for the Codex and the older Local session targets, not for Copilot, so "not listed" with Session Target = Copilot is the expected result. If Codex or Local can be selected as Session Target, try it too and note which target listed the skill.

## Part B: Microsoft Copilot Chat (work account)

Open https://copilot.cloud.microsoft in Edge or Chrome and sign in with the work account. Check your licence at https://myaccount.microsoft.com → **Subscriptions**: note whether **Microsoft 365 Copilot** is listed.

Upload path for every step below: **Agents** → **More agents** → arrow next to **Add** → **Upload skill**. Do not use an agent's **Configure** tab: that is Agent Builder, which has different rules. If **Upload skill** is not offered at all, record that and go to B5; it means skill upload is not enabled for your account.

Go in order. At the first upload that fails, skip the remaining uploads and go to B5; the failed step shows the cause.

**B1. Smallest skill, single file.** Upload `upload/1-basic/SKILL.md`.
- Accepted: in a new chat send `Run the basic Zaczyn probe` and record the reply. Continue with B2.
- Rejected: even a minimal skill was refused, so the cause is most likely the account, licence or a tenant setting rather than the skill's content. Record the exact error and go to B5.

**B2. Smallest skill, as a ZIP.** Upload `upload/2-zip/zaczyn-probe-zip.zip`.
- Accepted: send `Run the Zaczyn ZIP probe` and record the reply. Continue with B3.
- Rejected after B1 was accepted: ZIP upload itself is the problem. Record the exact error and go to B5.

**B3. ZIP with a packaged file.** Upload `upload/3-reference/zaczyn-probe-ref.zip`.
- Accepted: send `Run the Zaczyn reference probe` and record the reply. Continue with B4.
- Rejected after B2 was accepted: the `references/` folder is the problem. Record the exact error and go to B5.

**B4. Full skill.** Upload `upload/4-full/zaczyn-probe.zip`.
- Accepted: send `Run the Zaczyn probe` and record the reply.
- Rejected after B3 was accepted: the extra header fields or the `assets/` folder are the problem. Record the exact error.

Check that each reply comes from the skill you just uploaded: B1 starts with `PROBE BASIC`, B2 with `PROBE ZIP`, B3 has `PROBE REFERENCE` but no `PROBE ASSET`, B4 has `PROBE ASSET`. If it does not, or has no PROBE lines, type `/`, select the right skill, send the same sentence again and record that reply too.

**B5. File reference with `/`.** This works without any skill upload.
1. Open OneDrive (app launcher in the top-left corner → **OneDrive**), create a folder `Zaczyn-probe` and upload `upload/5-single/zaczyn-probe-single.md`. A new file can take a few minutes to appear in Copilot's file search.
2. In a new chat type `/`, then `zaczyn-probe-single`, and look at the **Files** tab.
3. If the file appears, select it and add `Read the referenced file in full and follow it.` Record the reply. Note whether the file could be selected at all.

## Part C: Copilot Cowork (only if your organisation has it)

Cowork shows as a **Chat | Cowork** switch at the top of https://copilot.cloud.microsoft. It needs a Microsoft 365 Copilot licence and an administrator to switch it on. If the switch is missing, skip Part C.

**C1. Upload.** Select **Cowork**, then **Customize** in the left pane → **Skills** tab → arrow next to **Add** → **Upload skill**. Upload `upload/4-full/zaczyn-probe.zip`, then `upload/5-single/zaczyn-probe-single.md`. Note which were accepted, with exact errors.

**C2. Run.** In a new Cowork task send `Run the Zaczyn probe`; in another send `Run the single Zaczyn probe`. Record both replies.

**C3. Write to OneDrive.** Upload `probe-state.md` into the `Zaczyn-probe` folder on OneDrive. In a new Cowork task send:

```
Open probe-state.md in my OneDrive folder Zaczyn-probe. Change "Current step: 1" to "Current step: 2", add the log line "- Edited by Cowork.", and save the file in place. Then tell me whether you overwrote it or saved a new file.
```

Record the reply and what the folder shows afterwards: the same file changed, a new file next to it, a Word file instead of `.md`, or a refusal.

## Clean up

- Chat: **Agents** → **More agents**, remove every skill whose name starts with `zaczyn-probe`.
- Cowork: **Customize** → **Skills**, remove every skill whose name starts with `zaczyn-probe`.
- OneDrive: delete the `Zaczyn-probe` folder. If you used Cowork, also open **My files** → **Documents** → **Cowork** → **skills** and delete the items whose names start with `zaczyn-probe`.

## Results

```
A0 version: | Account Policy Gate: | ChatAgentMode / ChatStrictPluginOnlyCustomization / UpdateMode (or "not listed"):
A1 Restricted Mode shown: yes/no | Agent selectable: yes/no | "/" lists zaczyn-probe: yes/no | Customizations shows: | reply:
A2 "/" lists zaczyn-probe: yes/no | other targets tried: | reply:
B  Microsoft 365 Copilot licence listed: yes/no | Upload skill offered: yes/no
B1 accepted / exact error: | reply:
B2 accepted / exact error: | reply:
B3 accepted / exact error: | reply:
B4 accepted / exact error: | reply:
B5 file selectable: yes/no | reply:
C  Cowork switch: yes/no | C1: | C2: | C3:
```

Sources: [Copilot Chat skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/build-copilot-chat-skills), [Cowork skills](https://learn.microsoft.com/en-us/copilot/cowork/cowork-customize), [file references](https://support.microsoft.com/en-us/microsoft-365-copilot/refer-to-specific-files-and-more-in-microsoft-365-copilot), [VS Code agent skills](https://code.visualstudio.com/docs/agent-customization/agent-skills), [VS Code enterprise policies](https://code.visualstudio.com/docs/enterprise/policies), [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust).
