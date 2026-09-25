---
name: recruiter-triage
version: 0.1.0
description: Triage recruiter inbound in under 2 minutes. Input is a pasted recruiter message (LinkedIn, email, anywhere); output is a verdict (PURSUE / ASK-FIRST / DECLINE) plus a ready-to-send reply. Trigger whenever the user pastes a recruiter message, forwarded outreach, or job pitch and asks "is this worth it," "how should I respond," "triage this," or pastes recruiter text with no instructions at all. Do NOT use for full job descriptions the user intends to apply to (that's job-application-tailor).
---

# Recruiter Triage

Turns a 20-minute deliberation into a 2-minute decision. Recruiters bury location, level, and comp; this skill front-loads them, applies the user's filters, and drafts the reply in one pass.

## Step 0: load the profile

Read `${CLAUDE_PLUGIN_ROOT}/profile/profile.md`. Use *Search targets* (roles, level, company preferences, location, comp, dealbreakers) for the verdict and *Voice & writing* (tone, sign-off, availability line) for the reply. If *Search targets* is still placeholders, ask the user for their location rule and target roles before judging.

## Step 1: extract before judging

From the message, pull: company (or "undisclosed"), role title, level/scope, location + on-site expectation, comp (if stated), company stage/size, employment type (full-time / contract), and what the recruiter is actually asking for. Mark anything absent as **UNKNOWN**. Absence is a signal; recruiters leave out what doesn't sell.

**Only extract from this message.** Forwarded emails often carry an older, unrelated thread (a different company, a prior interview). Never pull a company, domain, or detail from that older thread into the current role. If the domain isn't stated, say UNKNOWN; if you're guessing from the company name, label it as a guess.

## Step 2: apply the filters

**Hard filters (any one fails → DECLINE, warmly):**
1. **Location** fails the profile's location rule.
2. **Role shape** is on the profile's *Do not pursue* list.
3. **Comp** is stated and clearly below the profile's floor.
4. Any **other dealbreaker** from the profile.

**Soft signals (weigh, don't auto-kill):**
- Company stage and size vs. the profile's preferences.
- Title vs. target tiers. At startups, titles are unreliable; read for scope.
- Agency recruiter with an undisclosed client: fine, but get the company name before investing in a call.
- Contract or contract-to-hire: ask duration and conversion terms before any call, unless the profile says contract is fine.

**The ask-first rule:** if location, on-site expectation, or anything else the profile treats as a hard filter is UNKNOWN, the verdict is **ASK-FIRST**. No call gets booked until it's answered.

**The inbound rule:** a reasonable-looking inbound that passes the hard filters is usually worth a 30-minute call even when the title looks off. Real scope often only shows up in conversation, especially at startups. Default to PURSUE in that case and plan to probe scope on the call.

## Step 3: verdict + reply

Output exactly:

```
VERDICT: PURSUE | ASK-FIRST | DECLINE
Extracted: {company} · {role} · {location/on-site} · {comp} · {stage} · {type}
Why: {one or two lines: the filter(s) that decided it}
Reply (ready to send):
{drafted message}
```

### Reply patterns (adapt to the user's voice; don't robotify)

**ASK-FIRST:**
> Thanks for reaching out, this could be interesting. Before we go further: where is the role based, and what's the on-site expectation? [Add any other missing hard-filter question, e.g. level or comp range.]

**PURSUE:**
> Thanks, this looks worth a conversation. Quick context so we don't waste your time: I'm focused on {target roles from profile} at {company preferences}, {location rule}. Happy to grab 20–30 minutes: {availability line from profile}.

**DECLINE (warm, always keeps the contact):**
> Thanks for thinking of me. This one isn't the right fit: {one honest reason}. What I am looking for: {target roles, company type, location}. If something in that lane crosses your desk, I'd like to hear about it.

**DECLINE (contract):**
> Appreciate the outreach. I'm focused on full-time roles right now, so I'll pass on contract work. If {client} ever converts this to a full-time role, I'd be interested.

End every reply with the sign-off from the profile.

## Voice rules

- Never sound desperate; never sound dismissive. Every decline is a future referral.
- Never state comp expectations in a first reply unless directly asked.
- Keep replies under 80 words. Recruiters skim.
- Follow the profile's *Voice & writing* section over these defaults.
- If the verdict is PURSUE, offer to log it with `pipeline-tracker` (`/pipeline add`).

## Changelog

- **0.1.0**: Initial community release.
