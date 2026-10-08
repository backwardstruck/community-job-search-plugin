---
name: recruiter-triage
version: 0.2.0
description: Triage recruiter inbound in under 2 minutes. Input is a pasted recruiter message (LinkedIn, email, anywhere). The skill first checks whether the message is a recruiting blast (too little to analyze), then forks on engagement type. Full-time and part-time roles get a fit verdict (PURSUE / ASK-FIRST / DECLINE); contract roles get a contract verdict (PHONE-FIRST / DEAD / PURSUE). Either way it returns a ready-to-send reply. Trigger whenever the user pastes a recruiter message, forwarded outreach, or job pitch and asks "is this worth it," "how should I respond," "triage this," or pastes recruiter text with no instructions at all. Do NOT use for full job descriptions the user intends to apply to (that's job-application-tailor).
---

# Recruiter Triage

Turns a 20-minute deliberation into a 2-minute decision. Recruiters bury location, level, and comp; this skill front-loads them, applies the user's filters, and drafts the reply in one pass.

## The profile (this skill never edits it)

Facts about the user live in **`~/Documents/job-search/profile.md`**, inside their working folder `~/Documents/job-search/`. It sits outside the plugin on purpose: plugin updates replace the plugin folder, and the profile has to survive them.

- **Read it fresh** before using any fact about the user.
- **Never overwrite, rewrite, reformat, or delete anything in `profile.md`.**
- **If the file doesn't exist:** say so, and offer to create it by copying `${CLAUDE_PLUGIN_ROOT}/profile/profile.TEMPLATE.md` to that path. Do it only after the user agrees, and only if no file is there.
- **If a section this task needs is missing or still `[placeholder]`:** ask for that one section in chat, one at a time, most important first. When the user answers, show the exact text and, only with their OK, append it to the end of `profile.md` as a new top-level section: a `## ` heading with the template's name for it followed by `(added YYYY-MM-DD)`. Append only. If an older placeholder copy of that heading is still in the file, the newest dated copy wins; tell the user they can delete the old one themselves. If they'd rather skip it, carry on without it and say what's missing.

## Step 0: load the profile

Read `~/Documents/job-search/profile.md`. Use *Search targets* (roles, level, scope questions, engagement types, company preferences, warm-channel-only, location, comp, dealbreakers) for the verdict, and *Voice & writing* (tone, sign-off, availability line) for the reply. If *Search targets* is still placeholders, ask for those sections before judging, one at a time (see *The profile*).

## Step 1: is this a blast?

Decide whether the input is a **blast** or a real description. Blast signals:
- role descriptions of one or two lines
- two or more roles in one message
- client undisclosed
- no job description link and no job description text
- template pitch language ("Most firms talk about X. My client is doing X.")

**Two or more signals → BLAST mode.** In BLAST mode the skill is **forbidden** from:
- analyzing, scoring, ranking, or comparing the individual roles
- recommending which role to go for
- inferring team size, team makeup, org shape, or reporting lines from a list of titles
- naming a role the message didn't name
- advising on rate or salary positioning

Say plainly, in one line, that the input is a blast and there isn't enough to evaluate. Output is capped at a verdict plus a reply whose only goal is a phone call. Still run Step 2's engagement-type fork to pick the verdict set; skip everything else.

**A list of titles is not information about a team. One line per role is not a job description.**

## Step 2: extract, and fork on engagement type

**Fork first.** Contract, contract-to-hire, "consulting," staff augmentation, and corp-to-corp → **CONTRACT branch** (below). Full-time and part-time → the **standard path** (Step 3 on). Ambiguous or unstated → standard path, and make "is this full-time, part-time, or contract?" the first question in the reply.

If the profile's *Engagement types* rules out what this is, say so and stop: a warm DECLINE on the standard path, or DEAD on the contract branch, with a short reply that keeps the contact.

**Standard path:** from the message, pull company (or "undisclosed"), role title, level and scope, location and on-site expectation, hours (if part-time matters to the user), comp (if stated), company stage and size, and what the recruiter is actually asking for. Mark anything absent as **UNKNOWN**. Absence is a signal; recruiters leave out what doesn't sell.

**Only extract from this message.** Forwarded emails often carry an older, unrelated thread (a different company, a prior interview). Never pull a company, domain, or detail from that thread into the current role. If the domain isn't stated, say UNKNOWN; if you're guessing from the company name, label it as a guess ("likely X; UNKNOWN, confirm on the call").

## CONTRACT branch

Only Step 1, the engagement-type check and grounding rule in Step 2, and the voice rules apply here. The standard path's filters, scope questions, and templates don't.

**Many contract inbounds are bench-building**: the agency is collecting resumes for work that isn't funded yet. Start from *probably not real yet*. The job is to find out with as little of the user's time as possible.

**Verdicts:** `PHONE-FIRST` / `DEAD` / `PURSUE`. **PHONE-FIRST is the default.** PURSUE only once the engagement is established (funded, a start date, a named end client).

**The gate is existence, not scope.** Two questions only:
1. Is this a funded engagement with a start date, or are you building a bench?
2. Who is the end client?

**Resume:** sending a resume to an agency recruiter isn't a submission to a client. The real control is **submission consent per client, in writing**; that's a call topic. If `~/Documents/job-search/pipeline.md` shows a live process at a plausibly overlapping client, raise it in the first reply.

**Rate is a call topic.** Never stated in a first reply, never used to gate.

**`DEAD` is reserved for:** the profile ruling out contract work, a confirmed no-start-date bench exercise, a rate confirmed below the profile's floor, or a requirement that hits a profile dealbreaker (e.g. relocation).

```
VERDICT: PHONE-FIRST | DEAD | PURSUE (contract branch[ · BLAST mode])
Input: {one line: what was actually given; in BLAST mode, say so and that nothing will be analyzed}
Gate: Is the engagement funded with a start date, or a bench? Who's the end client?
Reply (ready to send):
{drafted message}
```

**Reply cap: 60 words.** Contents: open to contract work; availability; one short clause on what the user does; resume is coming; their availability line and phone from the profile. Nothing else.

> Thanks {name}. Open to contract work right now. {one clause: what I do}. Sending my resume to your email now.
>
> Easier to cover the rest on the phone. {availability line}.
>
> {sign-off from profile}

## Step 3: apply the filters (standard path)

**Hard filters (any one fails → DECLINE, warmly):**
1. **Location** fails the profile's location rule or travel limit.
2. **Role shape** is on the profile's *Do not pursue* list.
3. **Comp** is stated and clearly below the profile's floor.
4. **Hours or engagement type** conflict with the profile (e.g. full-time only when the user wants part-time).
5. Any **other dealbreaker** from the profile.

**Soft signals (weigh, don't auto-kill):**
- Company stage and size vs. the profile's preferences.
- Title vs. target tiers. At startups, titles are unreliable; read for scope.
- **Warm-channel-only:** if the company or sector is on the profile's warm-channel-only list, an inbound recruiter *is* a warm channel, so this is in play. Say so.
- Agency recruiter with an undisclosed client: fine, but get the company name before investing in a call.

**The ask-first rule:** if anything the profile treats as a hard filter is UNKNOWN (location, on-site expectation, hours, level), or any of the profile's *Scope questions to ask early* is unanswered, the verdict is **ASK-FIRST**. No call gets booked and no enthusiasm gets spent until the answers come back. Job descriptions and scope often change between first contact and a late round; the cheapest time to find out is now.

**The inbound rule:** a reasonable-looking inbound that passes the hard filters is usually worth a 30-minute call even when the title looks off. Real scope often only shows up in conversation, especially at small companies. Default to PURSUE in that case, and ask the scope questions on the call.

## Step 4: verdict + reply (standard path)

```
VERDICT: PURSUE | ASK-FIRST | DECLINE
Extracted: {company} · {role} · {location/on-site} · {hours} · {comp} · {stage}
Why: {one or two lines: the filter(s) that decided it}
Reply (ready to send):
{drafted message}
```

### Reply patterns (adapt to the user's voice; don't robotify)

**ASK-FIRST:**
> Thanks for reaching out, this could be interesting. Before we go further: {the missing hard-filter or scope questions, one line each}.

**PURSUE:**
> Thanks, this looks worth a conversation. Quick context so we don't waste your time: I'm focused on {target roles} at {company preferences}, {location rule}. Happy to grab 20–30 minutes: {availability line}. {One scope question from the profile, if any are unanswered.}

**DECLINE (warm, always keeps the contact):**
> Thanks for thinking of me. This one isn't the right fit: {one honest reason}. What I am looking for: {target roles, company type, location, hours}. If something in that lane crosses your desk, I'd like to hear about it.

End every reply with the sign-off from the profile.

## Voice rules

- Never sound desperate; never sound dismissive. Every decline is a future referral.
- Never state comp expectations in a first reply unless directly asked.
- If the recruiter asks a direct factual question (work authorization, start date, notice period, relocation), answer from the profile's *Answer-if-asked facts*. Never volunteer those facts unasked, and never guess them.
- Keep replies under 80 words (60 on the contract branch). Recruiters skim.
- Follow the profile's *Voice & writing* section over these defaults.
- If the verdict is PURSUE (either branch), offer to log it with pipeline-tracker (`/pipeline add`).

## Changelog

- **0.2.0**: Added blast detection, the contract branch (gate on existence, not scope), scope questions from the profile in ASK-FIRST, engagement-type and hours filters, and the warm-channel-only check. The profile lives at `~/Documents/job-search/profile.md`, outside the plugin; this skill never edits it and asks for missing sections one at a time.
- **0.1.0**: Initial community release.
