---
name: check-email
version: 0.2.0
description: Line-by-line audit of an email draft that forces every line to justify its existence, then returns a stripped-down rewrite. General-purpose; works on any email (job, professional, personal), not just job-search. Trigger on /check-email, "check this email", "justify each line", "audit this draft", "is this email too long", "tighten this email", or whenever the user pastes a draft and wants it pressure-tested before sending. Do NOT use to write a draft from scratch; this skill critiques and tightens an existing draft.
---

# Check Email

The premise: **every line in an email is guilty until it justifies itself.** Most drafts are 40% throat-clearing, redundant courtesy, and hedges that make the writer feel safe and make the reader skim. This skill goes line by line, forces a verdict on each, and hands back a version where every surviving line does real work.

This is a critique-and-rewrite skill. It does not write emails from scratch (that's a normal drafting request). It takes a draft the user already has and pressure-tests it.

## The profile (this skill never edits it)

Facts about the user live in **`~/Documents/job-search/profile.md`**, inside their working folder `~/Documents/job-search/`. It sits outside the plugin on purpose: plugin updates replace the plugin folder, and the profile has to survive them.

- **Read it fresh** before using any fact about the user.
- **Never overwrite, rewrite, reformat, or delete anything in `profile.md`.**
- **If the file doesn't exist:** say so, and offer to create it by copying `${CLAUDE_PLUGIN_ROOT}/profile/profile.TEMPLATE.md` to that path. Do it only after the user agrees, and only if no file is there.
- **If a section this task needs is missing or still `[placeholder]`:** ask for that one section in chat, one at a time, most important first. When the user answers, show the exact text and, only with their OK, append it to the end of `profile.md` as a new top-level section: a `## ` heading with the template's name for it followed by `(added YYYY-MM-DD)`. Append only. If an older placeholder copy of that heading is still in the file, the newest dated copy wins; tell the user they can delete the old one themselves. If they'd rather skip it, carry on without it and say what's missing.

## The one test every line must pass

A line survives only if it does at least one of these **jobs for the reader**:

1. **Moves toward the ask:** advances the actual purpose of the email (what you want the reader to do, know, or feel).
2. **Carries information the reader needs:** a fact, a time, a constraint, a decision they can't act without.
3. **Does real relational work:** genuine, specific warmth or acknowledgment that lands (not reflexive politeness the reader's eyes slide over).

If a line does none of these, it's dead weight. Padding doesn't make an email polite; it makes it longer, and a longer email is a *less* respectful ask on the reader's time.

## Voice: when the email goes out as the user (hard override)

Read the *Voice & writing* section of `~/Documents/job-search/profile.md`. If the draft is being sent as the user (emails, DMs, cover letters, notes), their voice **overrides** default polish. A tight, well-structured email that doesn't sound like them is still a fail. Enforce every rule in that section (tone, sentence style, punctuation habits, things they never say, sign-off) in the rewrite.

If the voice section is still placeholders, say so in one line, audit for the reader-job test only, and offer to collect that section (see *The profile*). When unsure, mirror the cadence of the draft itself rather than defaulting to AI style.

If the email is **not** being sent as the user (they're auditing something someone else wrote, or a draft they'll hand off), skip this override.

## Verdict vocabulary (assign one to every line)

- **KEEP:** earns its place. State which job it does in three or four words.
- **TIGHTEN:** right idea, too many words or too hedged. Give the tighter version inline.
- **CUT:** does no job. Name why (see the tells below).
- **MERGE:** this line and an adjacent one are doing one job across two sentences; fold them.

Never let a line pass on vibes. "Sounds nice" is not a job. If you can delete a line and the reader loses nothing they needed, it's a CUT.

## The tells: hunt these specifically

Flag them by name so the pattern is visible, not just the instance:

- **Throat-clearing openers:** "I hope this email finds you well," "I wanted to reach out," "I just wanted to quickly," "I'm writing to." The email itself is the reaching out; say the thing.
- **Hedges that shrink the ask:** "just," "maybe," "I was wondering if possibly," "no worries if not," "whenever you get a chance." One soft close is fine; a pile of them reads as apologizing for existing.
- **Redundant courtesy:** a thank-you in the opener, another in the middle, another in the sign-off. Pick one and make it specific.
- **Slash-paired phrases:** "reach out/connect," "thoughts/feedback." Pick one word.
- **Meta-commentary about the message:** "long overdue check-in," "quick note," "no ask here." Say the thing.
- **List-y stacking:** three near-synonyms where one lands harder. Cut to the strongest.
- **Explaining the obvious:** narrating what the reader can see ("As you can see below," "I've attached a document which contains").
- **Pre-emptive over-explaining:** justifying a normal request as if it needs defense.
- **Burying the ask:** the point sitting in paragraph three behind setup. The ask should be findable in a five-second skim.
- **Voice drift** (when sent as the user): anything that breaks a rule in their profile's voice section. Name the rule.

## Method

1. **Restate the goal in one line.** What is this email *for*? Every verdict is measured against this. If the goal is unclear from the draft, ask one question before auditing.
2. **Split the draft into lines**, including the subject line and sign-off. Number them.
3. **Verdict each one** with a terse reason (and the tell's name if it trips one).
4. **Write the rewrite:** apply every verdict and, if it's going out as the user, the voice override. Aim for the shortest version that still does all three real jobs and still sounds like the user wrote it: not a telegram, not an AI.
5. **Report the shrink:** original word count → new word count, and the single biggest thing that was dragging it down.

## Output format

```
GOAL: {one line: what this email is for}

LINE-BY-LINE
1. "{subject line}" → KEEP/TIGHTEN/CUT — {reason, tell name if any}
2. "{line}" → VERDICT — {reason}
   ...

REWRITE
Subject: {tightened subject}

{tightened body}

SHRINK: {N words → M words}. Biggest drag: {the one thing}.
```

## Voice & rules

- Terse in the audit, human in the rewrite. The critique is a scalpel; the output email still has to sound like a person.
- **Don't over-cut.** The goal is that every line earns its place, not that the email is as short as possible. A warm, specific line that does relational work KEEPS. Stripping an email to robotic bullets is a different failure than padding it.
- One genuine courtesy line is good. Three reflexive ones are noise.
- Preserve the sender's real content and commitments. Never invent facts, dates, or promises to fill a rewrite.
- If the draft is already tight, say so and make only the edits that genuinely help. Don't manufacture cuts to look busy.
- This skill only critiques wording. It never sends anything; sending stays the user's call.

## Changelog

- **0.2.0**: Initial community version. Voice rules now come from the profile. The profile lives at `~/Documents/job-search/profile.md`, outside the plugin; this skill never edits it and asks for missing sections one at a time.
