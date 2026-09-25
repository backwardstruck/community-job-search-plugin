<p align="right">
  <a href="#new-to-claude-or-plugins">New to Claude or plugins?</a> ·
  <a href="https://claude.com/download">Get Claude Desktop</a> ·
  <a href="https://code.claude.com/docs/en/overview">Get Claude Code</a> ·
  <a href="https://code.claude.com/docs/en/plugins">Plugin docs</a>
</p>

# community-job-search-plugin

A Claude plugin for running a job search: triage listings, tailor applications, handle recruiter outreach, and keep a pipeline that doesn't rot. Built for mid-career people looking at tech companies, any role (engineering, product, design, data, ops, and so on).

## Overview

You paste in a pile of job listings, a job description, or a recruiter's message. Claude scores, tailors, or drafts a reply, using your real history and your own rules (location, comp, dealbreakers) so nothing gets invented or overclaimed. A simple `pipeline.md` file tracks where every application stands.

**Nothing personal lives in the skills.** Everything about you (history, targets, location rules, comp, voice) goes in one file: `plugins/community-job-search/profile/profile.md`. Fill that in and every skill picks it up. That file stays on your computer.

## Prerequisites

- **A Claude account** (claude.ai). A paid plan is required for plugins.
- **One of these apps** to run the plugin:
  - **Claude desktop app** (Cowork mode): the easier start, no terminal needed.
  - **Claude Code**: a command-line tool, better if you're already comfortable in a terminal.
- **Git, or a zip download,** to get a local copy of this repo.
- **Optional:** the Gmail connector, for `/pipeline sync`.

### New to Claude or plugins?

- **Claude** is an AI assistant. You chat with it, and it can read and write files on your computer when you allow it.
- **A plugin** is a folder of instructions (called *skills*) that teaches Claude how to do a specific job. This one teaches Claude how to help with a job search. Installing it means pointing Claude at the folder.
- **Claude desktop vs. Claude Code:** both run plugins. Pick the desktop app if you'd rather click than type commands.

Further reading:
- [Download the Claude desktop app](https://claude.com/download)
- [Claude Code overview](https://code.claude.com/docs/en/overview)
- [How plugins work](https://code.claude.com/docs/en/plugins)
- [How plugin marketplaces work](https://code.claude.com/docs/en/plugin-marketplaces) (this repo is one)

## Skills

| Skill | Use it when | What you get |
|---|---|---|
| `job-listing-filter` | You have a pile of job listings | Each scored 0–100 for fit and time-value, ranked, with hard filters and screen-out risks called out |
| `job-application-tailor` | You're applying to one role | Fit score, tailored resume (plus an ATS-friendly version), short cover letter, and a truth check so nothing is overclaimed |
| `recruiter-triage` | A recruiter messages you | PURSUE / ASK-FIRST / DECLINE plus a ready-to-send reply |
| `pipeline-tracker` | You want to know where everything stands | A `pipeline.md` CRM with stages, next actions, stale flags, weekly report, and optional Gmail sync |

## Setup

1. **Get your own copy.** Clone or download this repo somewhere local, e.g. `~/Documents/community-job-search-plugin`. Your filled-in profile stays in *your* copy. Don't push it back here.

2. **Fill in your profile.** Open `plugins/community-job-search/profile/profile.md` and replace every `[bracketed]` placeholder. The more precise you are (exact dates, real metrics, honest gaps, clear dealbreakers), the better every skill gets. The skills will stop and ask if key sections are empty.

3. **Install the plugin.**
   - **Claude Code:**
     ```
     /plugin marketplace add ~/Documents/community-job-search-plugin
     /plugin install community-job-search@community-job-search
     ```
   - **Claude desktop (Cowork):** Settings → Plugins → add from folder, and point at your local copy.

4. **Optional: Gmail.** Connect the Gmail connector if you want `/pipeline sync` to update your pipeline from interview invites and rejections.

## Quick start

- Paste a batch of listings: *"filter these"*
- Paste one job description: *"tailor my resume for this"*
- Paste a recruiter message: *"triage this"*
- `/pipeline add Acme, Senior PM, applied today via referral from a former teammate`
- `/pipeline report` for the weekly view

## Principles baked in

- **Honest over flattering.** Scores are practical, not cheerleading. Resumes only use what's in your profile; anything inferred is tagged `[VERIFY BEFORE USING]`.
- **Dates and titles match LinkedIn.** Recruiters have it open.
- **Hard filters first.** Location and dealbreakers gate before fit is scored.
- **The file is the truth.** The pipeline is re-read from disk every time, so multiple chats never clobber each other.

## Updating your copy

When this repo gets updates, pull them into your copy. Your `profile.md` edits may conflict with template changes; keep your content and adopt any new sections.

## License

[MIT](LICENSE)

## Version

0.1.0
