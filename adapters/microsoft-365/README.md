# Zaczyn in Microsoft Copilot (Microsoft 365)

Status: a draft written from Microsoft's documentation of November 2026, **not yet confirmed in a working setup**. In one test with a company Microsoft 365 account, uploading a skill to Copilot Chat failed with a validation error (cause not yet known) and Cowork was switched off. If you try it, tell us which path worked and the exact error text in a [GitHub issue](https://github.com/amatlacz/zaczyn/issues) (needs a free GitHub account). The optional [host probe](https://github.com/amatlacz/zaczyn/tree/main/probe) is a short test of what your app accepts.

Microsoft renamed Microsoft 365 Copilot to **Microsoft Copilot**. Open it at https://copilot.cloud.microsoft with your work or school account; the label next to your profile says **Work**. These features need such an account. Microsoft's description of the Personal, Family, and Premium plans lists Copilot only inside Word, Excel, PowerPoint, OneNote, Outlook, and Designer, without skills or Cowork.

You need the **single-file edition** (`zaczyn-single-<version>.zip`). It is not released yet and will be attached to the next release on the [releases page](https://github.com/amatlacz/zaczyn/releases). Each `zaczyn-<skill>.md` inside is one complete skill. Begin with `zaczyn-setup.md` and the quick-setup prompt: it prepares your two context documents. Then add `zaczyn-work.md` and `zaczyn-review.md`. To test only whether uploading works, try `zaczyn-review.md`, the smallest. Orchestrate is not included, because these apps offer no delegation the skill can control. For your own reusable skills, Cowork's skill creator is a good alternative to Zaczyn's grow skill.

## Pick the first path that works

| Path | What you need | How | If it does not work |
|---|---|---|---|
| **1. Skill in Copilot Cowork** | A Microsoft Copilot licence (formerly Microsoft 365 Copilot), and your organisation has switched Cowork on with usage-based billing. A **Chat \| Cowork** switch appears at the top. | Select **Cowork**, then in the left pane **Plugins** (some screens still say **Customize**) → **Skills** → **Add** → **Upload** (or **Upload skill**) → choose the `.md` file. Alternatively, put the file in OneDrive as `Documents/Cowork/skills/zaczyn-setup/SKILL.md` and start a new Cowork task. | No switch, or upload refused: go to path 2 |
| **2. Personal skill in Copilot Chat** | A work account allowed to open **Agents & Skills** | Copy the file and rename the copy to `SKILL.md`. In Chat select **Agents** → **More agents** → arrow next to **Add** → **Upload skill** → choose that `SKILL.md`. | No **Upload skill**, or a validation error: go to path 3. Organisations that use Information Barriers cannot use skills in Chat. Microsoft recommends files under about 20,000 characters; `zaczyn-setup.md` is slightly over, so try `zaczyn-review.md` to see whether size is the cause. |
| **3. File you reference** | OneDrive for your work account | Put the `.md` files in a OneDrive folder, for example `Zaczyn`. In a chat type `/`, find the file on the **Files** tab, select it, and write: “Read this file in full and follow it for my task: <task>. First say which file you are following.” | Wait a couple of minutes after uploading. If a `.md` file still does not appear (Microsoft does not confirm Markdown for `/`), attach it with **+** → **Upload images and files**, or paste its text. |

A skill from path 1 or 2 is used when your request matches its description. In Copilot Chat that happens only if **Let Copilot use this skill automatically** is on for it under **Agents & Skills**; you can also select the skill there. In Cowork, the side panel's **Skills** section shows which skills loaded. If an answer ignores the skill, start a new conversation and name it: “Use zaczyn-review for …”. Your own skills do not work in Cowork on mobile; use the browser or desktop app.

## Keep your context in OneDrive

Your own context lives in two documents you own, in one OneDrive folder: `AGENTS` (how you want to work) and `PROJECT` (facts and scope). Setup prepares them.

- **Copilot Chat does not update your files.** It returns the complete text with the file name; you save or replace the file yourself. Reference both documents with `/` at the start of each new conversation.
- **Cowork edits existing Word, Excel, and PowerPoint files** after you approve, and saves new files to your OneDrive **Cowork** folder. Editing Markdown in place is not documented, so keeping `AGENTS` and `PROJECT` as Word documents is the safer choice there. Open the file after each change to check it.
- Optionally, in Cowork open **Customize instructions for Cowork** → **Edit** (on the **Plugins** page, or **Customize** → **Preferences**) and add “At the start of a task, read” followed by `/` references to your AGENTS and PROJECT documents. Cowork applies these instructions to every task; whether it opens the referenced files each time is not yet confirmed.

Do not put your AGENTS or PROJECT documents into the knowledge of an agent other people use (Agent Builder or Copilot Studio): everyone with access to that agent could read them.

## Connected apps

Copilot can read and, in Cowork, change mail, calendar, Teams, and documents. Zaczyn's rule applies: it shows the list or draft first and changes only the items you approved. Cowork also asks before sensitive actions; approve one action at a time.

## Sharing with colleagues

In Cowork, open a skill you uploaded, select **Share** → **Specific users in your organization** → **Publish**. Microsoft documents that the people you add can use it and that their copy follows your later changes after you select **Share** or **Re-share** again. They need Cowork themselves; try it with one colleague first.

Sources (checked 2026-11-18): [Cowork customization](https://learn.microsoft.com/en-us/copilot/cowork/cowork-customize), [using Cowork](https://learn.microsoft.com/en-us/copilot/cowork/use-cowork), [Cowork FAQ](https://learn.microsoft.com/en-us/copilot/cowork/cowork-faq), [Copilot Chat skills](https://learn.microsoft.com/en-us/plugins/build-copilot-chat-skills), [creating skills](https://support.microsoft.com/en-us/microsoft-365-copilot/create-edit-skills-copilot), [referencing files](https://support.microsoft.com/en-us/microsoft-365-copilot/refer-to-specific-files-and-more-in-microsoft-365-copilot), [requirements](https://learn.microsoft.com/en-us/copilot/plan/microsoft-copilot-requirements).
