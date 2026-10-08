<p align="right">
  <a href="#new-to-claude-or-plugins">New to Claude or plugins?</a> ·
  <a href="https://claude.com/download">Get Claude Desktop</a> ·
  <a href="https://code.claude.com/docs/en/overview">Get Claude Code</a> ·
  <a href="https://code.claude.com/docs/en/plugins">Plugin docs</a>
</p>

# community-job-search-plugin

A Claude plugin for running a job search: triage listings, tailor applications, handle recruiter outreach, prepare for and debrief interviews, keep a pipeline and a network that don't rot, and review your week. Built for mid-career people, with a lean toward tech companies, for any role (engineering, product, design, data, IT, ops, and so on).

## Overview

You paste in a pile of job listings, a job description, or a recruiter's message. Claude scores, tailors, or drafts a reply, using your real history and your own rules (location, comp, dealbreakers) so nothing gets invented or overclaimed. A few plain markdown files in one working folder (default `~/Documents/job-search/`) track every application, every contact, and every interview.

**Nothing personal lives in the skills.** Everything about you (history, targets, location rules, comp, voice) goes in one file on your computer: `~/Documents/job-search/profile.md`, outside the plugin so updates never touch it. Fill that in and every skill picks it up. That file stays on your computer.

## Prerequisites

- **A Claude account** (claude.ai). A paid plan is required for plugins.
- **One of these apps** to run the plugin:
  - **Claude desktop app** (Cowork mode): the easier start, no terminal needed.
  - **Claude Code**: a command-line tool, better if you're already comfortable in a terminal.
- **Git, or a zip download,** to get a local copy of this repo.
- **Optional:** the Gmail connector, for `/pipeline sync`.
- **Optional:** Python 3, for the pipeline's counting script (macOS and most Linux systems already have it).

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
| `recruiter-triage` | A recruiter messages you | PURSUE / ASK-FIRST / DECLINE (or a contract verdict) plus a ready-to-send reply; recruiting blasts get a phone-first reply, not an analysis |
| `check-email` | You have a draft to send | A line-by-line audit and a tighter rewrite in your own voice |
| `interview-prep` | You have an interview coming up | A brief, a one-page card to keep in view during the call, and a short rehearsal |
| `interview-debrief` | You just got off an interview | A 15-minute structured debrief, graded against your prep, that feeds the next round |
| `pipeline-tracker` | You want to know where every application stands | A `pipeline.md` CRM with stages, next actions, stale flags, an append-only change log, weekly metrics, and optional Gmail sync |
| `pipeline-overview` | You want a one-minute glance at the search | Read-only dashboard: funnel, live processes, what's overdue, momentum |
| `network-tracker` | You're keeping up with people, not roles | A `network.md` file of contacts and follow-ups, with tiers, a weekly coffee cap, and triage |
| `network-overview` | You want to know who you owe | Read-only glance at networking follow-ups due this week |
| `job-search-review` | It's your weekly planning time | Last week graded, this week's targets, one honest reframe, and an update for your accountability partner |

## Setup

1. **Get the plugin.** Either add this repo as a marketplace straight from GitHub (see *Install* below), or clone or download it somewhere local, e.g. `~/Documents/community-job-search-plugin`.

2. **Create your profile.** Make the folder `~/Documents/job-search/` and copy `plugins/community-job-search/profile/profile.TEMPLATE.md` into it as `profile.md`. Replace every `[bracketed]` placeholder. The more precise you are (exact dates, real metrics, honest gaps, clear dealbreakers), the better every skill gets. Your pipeline, network, and interview files will live in the same folder.
   - The skills never overwrite or edit your `profile.md`. If one needs a section you haven't filled in, it asks you for that one section and, with your OK, appends it to the end as a new dated section; the dated copy wins over any old placeholder.
   - If you skip this step, the first skill you run offers to copy the template for you.

3. **Install the plugin** (next section).

4. **Optional: Gmail.** Connect the Gmail connector if you want `/pipeline sync` to update your pipeline from interview invites and rejections.

## Install

The marketplace and the plugin are both named `community-job-search`.

**Claude Code** (in a session; drop the leading `/` and prefix `claude` to run them from a terminal instead):

```
/plugin marketplace add backwardstruck/community-job-search-plugin

# or from a local copy
/plugin marketplace add ~/Documents/community-job-search-plugin

/plugin install community-job-search@community-job-search
```

**Claude desktop app (Cowork):** Customize → Plugins → Add → **Add marketplace**, and enter `backwardstruck/community-job-search-plugin`. Then install **community-job-search** from it.

## Update

Your profile and working files live in `~/Documents/job-search/`, outside the plugin, so updating never touches them.

**Claude Code:**

```
/plugin marketplace update community-job-search
```

Then open `/plugin` → **Installed** → **community-job-search** → **Update now** (or from a terminal: `claude plugin update community-job-search@community-job-search`). The new version loads in your next session, or run `/reload-plugins`.

If you installed from a local copy, `git pull` in that copy first. A local install loads in place, so the next session (or `/reload-plugins`) picks up the change.

**Claude desktop app (Cowork):** open the marketplace in Customize → Plugins and choose **Check for updates**, or turn on **Sync automatically**.

**When an update adds profile sections,** compare your `profile.md` with the new `profile.TEMPLATE.md`, or just keep working: skills ask for any section they need that you don't have.

## Uninstall

```
/plugin uninstall community-job-search@community-job-search
/plugin marketplace remove community-job-search
```

Removing the marketplace also uninstalls every plugin installed from it. Neither command touches `~/Documents/job-search/`.

**Moving from an older fork of this plugin?** See [MIGRATION.md](MIGRATION.md).

## Quick start

- Paste a batch of listings: *"filter these"*
- Paste one job description: *"tailor my resume for this"*
- Paste a recruiter message: *"triage this"*
- `/pipeline add Acme, Senior PM, applied today via referral from a former teammate`
- `/pipeline report` for the weekly view
- *"prep me for my interview with Acme on Thursday"*, then afterward *"debrief"*
- `/network add Sam, former teammate, now at Acme`
- *"give me the overview"* or *"grade my week"*

## Principles baked in

- **Honest over flattering.** Scores are practical, not cheerleading. Resumes only use what's in your profile; anything inferred is tagged `[VERIFY BEFORE USING]`.
- **Dates and titles match LinkedIn.** Recruiters have it open.
- **Hard filters first.** Location and dealbreakers gate before fit is scored.
- **The file is the truth.** The pipeline and network files are re-read from disk every time, and you confirm the read before anything is written, so multiple chats never clobber each other.
- **Live processes over volume.** Momentum is measured by how many processes are past the application stage, not by how many applications went out.

## License

[MIT](LICENSE)

## Version

0.2.0

## Changelog

- **0.2.0**: Seven new skills (check-email, interview-prep, interview-debrief, pipeline-overview, network-tracker, network-overview, job-search-review). Pipeline ships log and counting script. Recruiter blast detection and a contract branch. The profile moves out of the plugin to `~/Documents/job-search/profile.md` (the plugin ships only `profile.TEMPLATE.md`), skills never edit it and ask for missing sections one at a time, and MIGRATION.md covers moving from an older fork. The profile gains scope questions, engagement types, offer gates, interview material, and answer-if-asked facts.
- **0.1.0**: Initial release with four skills.
