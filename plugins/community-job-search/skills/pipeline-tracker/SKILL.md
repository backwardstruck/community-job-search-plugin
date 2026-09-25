---
name: pipeline-tracker
version: 0.1.0
description: Job-search pipeline CRM. Maintains a single pipeline.md as the source of truth for every company and role: stage, last touch, next action, follow-up date. Trigger on /pipeline (add, update, report, sync, or bare), or whenever the user asks "what's the status of X," "what's in my funnel," "add this to the pipeline," "update [company]," "check my email for interviews/rejections," mentions applying somewhere new, reports interview or recruiter activity that should be logged, or asks what needs follow-up. If a conversation produces a pipeline event (applied, screen booked, rejection, offer), offer to log it even if the user didn't invoke the skill.
---

# Pipeline Tracker

A CRM you'll actually keep: one markdown file, five stages, every entry has a **next action** and a **date**. The point is to make "wait, what's the status of X?" impossible to ask.

## Where the file lives

Use the *Pipeline file path* from `${CLAUDE_PLUGIN_ROOT}/profile/profile.md` (section *Files*). If it isn't set, use `~/Documents/job-search/pipeline.md`. If the user says the file is somewhere else (another folder, Google Drive), use that.

## ⛔ The read-confirm gate: runs first, every invocation

People often have more than one chat open, and more than one can write to `pipeline.md`. Any copy in this chat's context is stale the moment another chat saves. Rendering from memory puts closed companies back in play and hides follow-ups you owe.

**On every `/pipeline` invocation (add, update, report, sync, bare) and every status question that would print pipeline content:**

1. **Read the pipeline file from disk, in full, right now.** Not from context, not from an earlier turn. If it paginates, read every page.
2. **Print a one-line read receipt and stop:**
   `📂 Read pipeline.md: header "updated YYYY-MM-DD" · {A} ACTIVE / {C} CLOSED. Is this the latest version?`
3. **Print nothing from the pipeline and write nothing until the user confirms.** "Yes," "go," or equivalent counts. If they say another chat just saved, read again and re-issue the receipt.
4. Then run the command. Every table, count, and sentence is rendered **from the file just read**. An entry under `## CLOSED` never appears as active. If the conversation and the file disagree, the file wins and you say so.
5. **Stated vs. inferred.** A fact the other side actually said (a date, a panel, a number) is logged plainly. A fact you inferred gets a `— confirm` tag until the user or an email confirms it.

If the gate feels slow, it's still faster than acting on a wrong board.

## File rules

- **Fresh read before any edit.** Always. Writing from a stale copy silently overwrites newer data.
- **If the file doesn't exist yet,** create it from the template below.
- **Bump the header date on every write** to today's date. A header that disagrees with the entries is a bug; fix it in the same edit.
- **Write the whole file** after every change. The whole file is the database. Re-read the header afterward to confirm the write landed.
- **Never invent or "remember" entries** that aren't in the file or this conversation.

## Stages (fixed vocabulary)

`SOURCED → APPLIED → SCREEN → LOOP → OFFER`, plus terminal `CLOSED` with a reason (rejected / withdrew / ghosted / not a fit / etc.).

## Kind field (not all applications are equal)

Warm channels (referrals, inbound recruiters, someone you know) usually convert far better than cold applications. Tag APPLIED entries so the funnel reads honestly:

- **`🤝 warm`**: referral, inbound recruiter, or a real contact at the company.
- **`⭐ real pursuit`**: a cold application the user genuinely wants and will chase.
- **`📋 cold`**: a cold application with no contact and no particular intent. This is the default for cold applies.

Persist it in the entry's `Kind:` field. The field drops off once an entry advances past APPLIED. Any APPLIED entry with no `Kind:` counts as `📋 cold` in reports.

## pipeline.md format

```markdown
# Job Search Pipeline — updated YYYY-MM-DD

## ACTIVE

### {Company} — {Role title}
- **Stage:** SCREEN
- **Kind:** {🤝 warm | ⭐ real pursuit | 📋 cold} (APPLIED only)
- **Contact:** {name, title, email/LinkedIn if known}
- **Source:** {inbound recruiter / applied on site / referral from X}
- **Comp/Location:** {what's known; ❓ if location unconfirmed}
- **Last touch:** YYYY-MM-DD: {what happened}
- **Next action:** {specific act}, **due YYYY-MM-DD**
- **Log:**
  - YYYY-MM-DD: {event}

## CLOSED

### {Company} — {Role} — CLOSED YYYY-MM-DD ({reason})
- one-line post-mortem if useful
```

Rules:
- **Every ACTIVE entry has a next action with a due date.** If the user doesn't give one, propose one (default: follow up in 5 business days for APPLIED, 3 for SCREEN/LOOP).
- Sort ACTIVE by stage (furthest along first), then by due date.
- One terse sentence per log line. It's a CRM, not a journal.
- ❓ on Comp/Location means the location question hasn't been answered yet; that's a next action by definition.
- **Stale rule.** An APPLIED entry more than 30 days old with no response gets `**Stale:** yes ⏳`, stays ACTIVE (never auto-closed), and its next action becomes "Decide: nudge through network or close." A reply, screen, or rejection clears it.
- **Offer rule.** When an entry reaches **OFFER**, its next action becomes "Evaluate the offer against your criteria before responding," marked 🎯 everywhere it's shown. Compare against the profile's *Search targets* (level, scope, comp, location, dealbreakers) before recommending a response. Offer excitement doesn't get to skip the diligence.

## Gmail sync (`/pipeline sync`)

When a Gmail connector is available, reconcile the pipeline against the inbox. Default lookback is **2 weeks** unless the user says otherwise.

1. Search for job-signal mail: screen or interview invites, "next steps," availability requests, calendar invites, and rejections ("unfortunately," "not moving forward," "other candidates," "position has been filled").
2. Classify each real hit and reconcile:
   - **Interview / screen invite** → advance to SCREEN (recruiter or first call) or LOOP (hiring manager / panel); log the date.
   - **Rejection** → move to CLOSED (rejected) with the date.
   - **Recruiter reply** → log it; advance only if it clearly implies a round.
   - **A company not in the pipeline** → add it at the stage the email implies.
3. **Ignore noise:** application auto-acknowledgements, job-board digests, newsletters, receipts. An auto-ack alone doesn't change a stage.
4. Only assert what the email says. Ambiguous items get logged with `— confirm`, not a stage change.
5. Backfill `Kind: 📋 cold` on APPLIED entries missing it; flag any that look like warm or real pursuits so the user can re-tag.
6. **Show the user the findings and the exact changes before overwriting the file.**

## Commands

### `/pipeline add {details}`
Create an entry from what the user gives plus conversation context. Ask only for what's missing (usually the next action). Set `Kind:` for APPLIED entries. Write the full file.

### `/pipeline update {company} {what happened}`
Fuzzy-match the company, append to the log, update stage / last touch / next action. Rejection or withdrawal → move to CLOSED with reason and date. Write the full file.

### `/pipeline report`
Weekly funnel summary:
1. **Funnel counts** by stage. Split APPLIED by Kind, e.g. "APPLIED: 20 (5 🤝 · 3 ⭐ · 12 📋)", so cold volume doesn't inflate the read.
2. **Stale and overdue:** stale entries, anything with a past-due next action, anything untouched for 7+ days, each with a one-line suggested nudge.
3. **This week's actions:** every next action due in the next 7 days, by date.
4. **Momentum:** one honest paragraph. Is the funnel growing, converting, or leaking, and where?

### `/pipeline` (bare)
A compact table (Company | Role | Stage | Next action | Due) of ACTIVE entries, sorted by due date, overdue marked ⚠️. Rendered after the gate, from the file just read.

## Voice

Terse. No cheerleading. A rejection gets logged like weather. When something is stale or leaking, say so plainly. The value of this skill is that nothing rots silently.

## Changelog

- **0.1.0**: Initial community release.
