---
name: network-overview
version: 0.2.0
description: Read-only, glanceable "state of my network" overview, the networking companion to pipeline-overview. Reads the current network.md (ACTIVE, INITIATIVES, PARKED, NEEDS TRIAGE) and renders one summary: who is owed what and when, the batch of short messages, coffees against the weekly cap, and what needs triage. Trigger on "network overview", "show me my network", "who do I owe", "networking dashboard", or any request for a snapshot of networking follow-ups. Does NOT edit anything; network-tracker owns writes, this skill only reads and presents.
---

# Network Overview

A read-only snapshot of the user's networking: the people and initiatives not tied to an open role. Same job as **pipeline-overview**, for people instead of roles: a view to scan in under a minute without opening the file. **network-tracker** owns `network.md`; this skill only reads it.

## The profile (this skill never edits it)

Facts about the user live in **`~/Documents/job-search/profile.md`**, inside their working folder `~/Documents/job-search/`. It sits outside the plugin on purpose: plugin updates replace the plugin folder, and the profile has to survive them.

- **Read it fresh** before using any fact about the user.
- **Never overwrite, rewrite, reformat, or delete anything in `profile.md`.**
- **If the file doesn't exist:** say so, and offer to create it by copying `${CLAUDE_PLUGIN_ROOT}/profile/profile.TEMPLATE.md` to that path. Do it only after the user agrees, and only if no file is there.
- **If a section this task needs is missing or still `[placeholder]`:** ask for that one section in chat, one at a time, most important first. When the user answers, show the exact text and, only with their OK, append it to the end of `profile.md` as a new top-level section: a `## ` heading with the template's name for it followed by `(added YYYY-MM-DD)`. Append only. If an older placeholder copy of that heading is still in the file, the newest dated copy wins; tell the user they can delete the old one themselves. If they'd rather skip it, carry on without it and say what's missing.

## Source (read it; never write to it)

**`<folder>/network.md`**, where `<folder>` is `~/Documents/job-search/`. Also read the profile's *Networking cap* (default two new coffees or calls a week).

**⛔ Mandatory fresh read, every invocation.** Re-read the entire file from disk before producing any output, even if you believe you already have it in context. If the file can't be found, say so and stop; never invent entries.

**Verification stamp (required first line of output):** `Read from disk: network.md — header says "updated {DATE}", top entry: {NAME}`, echoing the header line and the first `###` entry under `## ACTIVE` exactly as they appear in the file just read. If you can't produce this line from a fresh read, don't produce the overview.

**Get today's date from the system clock**, never from memory. Overdue, due today, and this week are all computed against it.

Only assert what's in the file. Never infer a date, a tier, or a touch the file doesn't state. Items tagged `— confirm` keep the tag.

**Not a source:** `pipeline.md`. Contacts attached to a live role live there and show in pipeline-overview. Don't merge the two views.

## What to output

In this order, readable in under a minute:

1. **Header:** `Network: state as of {date}.` Then one line of counts: `{A} active · {I} initiatives · {P} parked · {T} in triage`.
2. **Due:** one table of every ACTIVE and INITIATIVES entry: `Name | Tier | Size | Next action | Due`. Sort by due date, earliest first; at equal dates, higher tier first. Mark overdue ⚠️ and today 📍. Shorten the next action to what the user actually does; keep any `— confirm` tag. An entry with no due date is a file bug: show it at the top with `❓ no date` and say to run network-tracker.
3. **Alert line:** `⚠️ N overdue ({names}), M due today.` If both are zero, say so.
4. **Short-message batch:** every `Size: 2-line` item due within 7 days, named in one line so they go out in one sitting: `✉️ Batch this week: {names}`. Omit if none.
5. **Coffees and calls:** booked ones in the next 7 days, with day and time where the file states them. Then the cap: how many *new* ones are proposed this week and whether that breaks the profile's cap.
6. **Parked and triage:** PARKED entries past their review date (`⏰ Parked past review: ...`), or `no parked entries past review (next: {earliest review date})`. Then `🗂️ {T} in triage`, with names if 5 or fewer, otherwise the count and a pointer to `/network triage`.
7. **Momentum:** one honest line: how many ACTIVE entries had a touch in the last 7 days versus how many have gone quiet 14+ days, and whether the list is being worked or just carried.

## Voice & rules

- Terse, glanceable, same voice as pipeline-overview. A contact going cold is reported like weather.
- **Read-only.** Never edit network.md, pipeline.md, or anything else. If something needs changing (an overdue item, a missing date, a triage pass), tell the user to run network-tracker and stop there.
- No personal financial figures.
- The per-person notes are in the file; this is the glance.

## Changelog

- **0.2.0**: Initial community version. The profile lives at `~/Documents/job-search/profile.md`, outside the plugin; this skill never edits it and asks for missing sections one at a time.
