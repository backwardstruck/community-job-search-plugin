---
name: interview-debrief
version: 0.2.0
description: 15-minute post-interview capture. Trigger immediately whenever the user says they just finished an interview, screen, or recruiter call ("just got off with {company}," "debrief," "/debrief"), or starts recounting how an interview went; recounting an interview is enough to trigger, don't wait for the word "debrief." Produces a structured debrief file per company and round that feeds interview-prep for later rounds and captures intel while it's fresh. Also use when the user asks "what did they ask me last time" or preps for a later round at a company they've already interviewed with.
---

# Interview Debrief

Memory decays fastest in the first hour. This skill grabs the interview while it's hot: 15 minutes, structured, honest, so every round makes the next one better. Lessons only compound if they get written down.

Files live in the user's **working folder**: `~/Documents/job-search/`, written `<folder>` below.

## The profile (this skill never edits it)

Facts about the user live in **`~/Documents/job-search/profile.md`**, inside their working folder `~/Documents/job-search/`. It sits outside the plugin on purpose: plugin updates replace the plugin folder, and the profile has to survive them.

- **Read it fresh** before using any fact about the user.
- **Never overwrite, rewrite, reformat, or delete anything in `profile.md`.**
- **If the file doesn't exist:** say so, and offer to create it by copying `${CLAUDE_PLUGIN_ROOT}/profile/profile.TEMPLATE.md` to that path. Do it only after the user agrees, and only if no file is there.
- **If a section this task needs is missing or still `[placeholder]`:** ask for that one section in chat, one at a time, most important first. When the user answers, show the exact text and, only with their OK, append it to the end of `profile.md` as a new top-level section: a `## ` heading with the template's name for it followed by `(added YYYY-MM-DD)`. Append only. If an older placeholder copy of that heading is still in the file, the newest dated copy wins; tell the user they can delete the old one themselves. If they'd rather skip it, carry on without it and say what's missing.

## Step 0: find what already exists (before asking anything)

The prep for this round was likely built in a different chat and saved to the working folder. **Never say no brief existed without looking.**

Before the first question, search `<folder>` for:
- `prep-{Company}-*`: every prep brief for this company (all rounds)
- `debrief-{Company}-*`: every prior debrief for this company
- `CARD-{Company}-*`: any one-page card for this call

Read what you find. Then say in one line what was prepped, e.g. *"Found `prep-Acme-HMRound-JordanLee-2026-03-04.md`: a 90-second open, two stories, five questions. Grading against that."* If nothing is there, say so plainly: *"No prep file found for this round."*

## How to run it

Conversational, not a form. The user talks; the skill structures. Ask only for what they haven't already said. If they open with a five-minute recap, most sections are filled; confirm and probe the gaps. Target: 15 minutes, never more than 20.

Capture in this order, skipping anything already covered:

1. **Logistics:** company, role, round (screen / hiring manager / panel / final), interviewer name and title, date, format, length.
2. **Questions asked:** every one they can recall, verbatim where possible. This is the highest-value section; push gently for completeness ("anything technical? behavioral? about your last role?").
3. **Their answers, self-rated:** for each significant question, what they said (one line) and an honest grade: **landed / okay / stumbled**. Push past politeness: "which answer would you want back?" If everything is rated "landed," push once; that's rarely true.
4. **Intel gathered:** team structure and size, tools, pain points they revealed, why the role is open, who decides, timeline, comp signals, culture reads. Anything a later round can use. **Mark stated vs. inferred:** what the interviewer actually said is logged plainly; anything deduced (panel makeup, reporting line, why the seat is open) gets `— confirm`. Never write an inference as a fact.
5. **Their concerns:** stated or read-between-the-lines objections (a gap, a short tenure, level, domain, whatever surfaced). How the user handled it; whether it needs a better answer. Check the profile's *Standing answers to tricky questions* and suggest updating it if a better answer emerged.
6. **Follow-ups owed:** thank-you note (to whom, mentioning what), materials promised, references, scheduling.
7. **Prep delta:** the one or two things to do differently before the next round. See *Grade against the prep*.
8. **Gut read:** their honest probability call, and whether they even want it. Both matter.

## Grade against the prep (section 7)

With the prep file from Step 0 in hand, answer three questions in order:

- **What from the brief got delivered, and how did it land?**
- **What from the brief did NOT get delivered, and what did they say instead?** This is the important one. A common pattern: the material was prepped and good, and under live pressure the user fell back on their standard answers (a chronological walk through the resume instead of the prepped opening, a generic answer instead of the role-specific one). Name it when it happens. It isn't a prep problem.
- **What wasn't in the brief and should have been?** Questions that surprised them, intel that reframes the role.

**When prepped material didn't get delivered, the fix is rehearsal, not a better document.** Write it that way: *"Before the next round, say the opening and story #1 out loud until they're the default. The brief already has them."* Hand that instruction to interview-prep explicitly.

## Output

Write the debrief to `<folder>/debrief-{Company}-{Round}-{YYYY-MM-DD}.md` (the folder root, where Step 0 looks). Example: `debrief-Acme-HMRound-2026-03-04.md`. Use the eight sections above. Terse bullets, the user's words where possible. Cite the prep file by name inside the debrief so the next chat can find it.

Then close in chat with three things:
- **The headline:** one sentence on how it went and the single most important takeaway.
- **Actions:** follow-ups owed with deadlines (thank-you notes are due same day; say so). **Whatever is listed here must also appear in the pipeline entry and in any "what's owed" summary printed this turn.**
- **Handoffs:** offer to log the round with `/pipeline update {company}`, and note that this debrief and the prep file should go to interview-prep before the next round at this company.

## Later-round prep mode

When the user is preparing for round N at a company with existing debriefs, find the prior debrief and prep files (Step 0) and surface: questions already asked (won't repeat, may go deeper), answers rated "stumbled" (sharpen them; draft the better answer together), prepped material that wasn't delivered (rehearse it, don't rewrite it), intel gathered (use it: reference their stated pain points), and concerns raised (have the counter ready). This compounding loop is the whole reason the skill exists.

## Voice

Honest over kind. If an answer stumbled, the debrief says stumbled. The file is private and its only job is to make the next round better. No performance-review energy, no cheerleading. Fifteen minutes, structured, done.

## Changelog

- **0.2.0**: Initial community version. The profile lives at `~/Documents/job-search/profile.md`, outside the plugin; this skill never edits it and asks for missing sections one at a time.
