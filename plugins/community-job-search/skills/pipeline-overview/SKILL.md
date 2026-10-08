---
name: pipeline-overview
version: 0.2.0
description: Read-only, glanceable "state of the job search" overview. Reads the current pipeline.md (stages, next actions, due dates, stale flags), its ships log, and network.md, and renders one at-a-glance summary. Trigger on /overview, /dashboard, "how's my search going", "give me the overview", "state of my search", "where does my pipeline stand", or any request for a holistic snapshot of the funnel. Does NOT edit anything; pipeline-tracker owns writes, this skill only reads and presents.
---

# Pipeline Overview

A read-only snapshot of the whole job search: the dashboard the user can scan in under a minute without opening anything. It does **not** maintain data. **pipeline-tracker** owns `pipeline.md` and **network-tracker** owns `network.md`; this skill only reads them.

## The profile (this skill never edits it)

Facts about the user live in **`~/Documents/job-search/profile.md`**, inside their working folder `~/Documents/job-search/`. It sits outside the plugin on purpose: plugin updates replace the plugin folder, and the profile has to survive them.

- **Read it fresh** before using any fact about the user.
- **Never overwrite, rewrite, reformat, or delete anything in `profile.md`.**
- **If the file doesn't exist:** say so, and offer to create it by copying `${CLAUDE_PLUGIN_ROOT}/profile/profile.TEMPLATE.md` to that path. Do it only after the user agrees, and only if no file is there.
- **If a section this task needs is missing or still `[placeholder]`:** ask for that one section in chat, one at a time, most important first. When the user answers, show the exact text and, only with their OK, append it to the end of `profile.md` as a new top-level section: a `## ` heading with the template's name for it followed by `(added YYYY-MM-DD)`. Append only. If an older placeholder copy of that heading is still in the file, the newest dated copy wins; tell the user they can delete the old one themselves. If they'd rather skip it, carry on without it and say what's missing.

## Sources (read them; never write to any)

All files live in the user's **working folder**: `~/Documents/job-search/`, written `<folder>` below. Also read the profile's *Search context* for the search start date, runway end date, and weekly targets.

1. **`<folder>/pipeline.md`**

   **⛔ Mandatory fresh read, every invocation.** Re-read the entire file from disk before producing any output, even if you believe you already have it in context. Other chats write to this file between reads, so an earlier read is stale by definition. If it paginates, read every page. If it can't be found, ask the user where it is; never invent entries.

   **Verification stamp (required first line of output):** `Read from disk: pipeline.md — header says "updated {DATE}", top entry: {COMPANY}`, echoing the header line and the first `###` entry under `## ACTIVE` exactly as they appear in the file just read. If you can't produce this line from a fresh read, don't produce the overview.

   **Stale header:** if the header date is behind the newest entry activity, say so in one line and tell the user to run pipeline-tracker, which bumps it on every write. Never excuse it as cosmetic.

2. **`<folder>/pipeline-log.md`** (the ships log, if it exists). Any comparison across time comes from here: one line per pipeline write with MID, stage counts, and a note. Lines marked `~` were reconstructed; a line with a `NO-STAGE` warning has a MID that's short by the entries it names; say so rather than quoting the number flat. Week-over-week can also come from the `## WEEKLY METRICS` table at the top of `pipeline.md`; if the two disagree, the log wins. If neither exists, skip the trend and say so.

3. **`<folder>/network.md`** (if it exists). Same fresh-read rule. Read only the ACTIVE and INITIATIVES next actions and due dates, the NEEDS TRIAGE count, and PARKED entries past their review date. If the file is missing, skip the network line and say so in one line.

Get today's date from the system clock, never from memory. Only assert what's in the files. Never infer a stage, a date, or a count a file doesn't state.

## What to output

In this order, readable in under a minute:

1. **Header:** "Job Search: state as of {date}." If the profile has a search start date, add weeks since. If it has a runway end date, add weeks left.
2. **Funnel:** one line, furthest along first: `MID {n} · OFFER · LOOP · SCREEN · APPLIED · SOURCED`, plus a CLOSED total. Split APPLIED by Kind, e.g. `APPLIED 20 (5 🤝 · 3 ⭐ · 12 📋)`. An APPLIED entry with no `Kind:` counts as `📋 cold` so the split sums to the total.
3. **Live front:** a compact table of every **OFFER, LOOP, and SCREEN** entry: `Company | Role | Stage | Next action | Due`. Sort by due date, earliest first, so overdue rows float up; mark overdue ⚠️ and OFFER 🎯. At equal dates, the more advanced stage goes first.
4. **Alert line:** `⚠️ N overdue ({names}), M due today`, then a short pointer to the APPLIED follow-up backlog. Don't re-list every date from the table.
5. **Stale:** count and names of entries flagged stale.
6. **Network:** one line: `🤝 Network: N overdue ({names}), M due this week · T in triage`, or `🤝 Network: nothing due this week.` The full view is network-overview.
7. **Momentum:** one honest line led by **MID** (OFFER + LOOP + SCREEN) and its trend from the ships log. Never report application volume as momentum without MID beside it. Compare to the profile's weekly targets if they're set.

## Voice & rules

- Terse, glanceable, no cheerleading. A rejection is reported like weather.
- **Read-only.** Never edit any file. If something needs changing, tell the user to run pipeline-tracker (or network-tracker).
- If a source is missing or looks stale, say so plainly and produce what you can. Never fabricate counts or entries.
- This is a glance, not a report. The deep weekly breakdown is `/pipeline report`.
- Never include personal finances beyond the runway date the profile states.

## Changelog

- **0.2.0**: Initial community version. Fresh-read verification stamp, MID-led funnel and momentum, ships-log trend, and a one-line network summary. The profile lives at `~/Documents/job-search/profile.md`, outside the plugin; this skill never edits it and asks for missing sections one at a time.
