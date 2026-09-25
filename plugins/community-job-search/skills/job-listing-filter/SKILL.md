---
name: job-listing-filter
version: 0.1.0
description: >-
  Triage a batch of job descriptions against the user's profile. Scores each 0–100 for
  whether the role is a good use of their time, with a short summary, ranked best-first.
  Use this whenever the user pastes two or more job descriptions, a block of listings, or a
  job-board dump and wants to know which are worth pursuing. Triggers on "filter these
  jobs," "which of these should I apply to," "rank these listings," "score these JDs,"
  or any pile of roles pasted with intent to sort or prioritize. This is triage only: it
  does NOT write resumes or cover letters (that's job-application-tailor).
---

# Job Listing Filter

A fast triage pass over a batch of job descriptions. The goal is to tell the user, at a glance, which listings deserve a closer look. Not to tailor anything.

Optimize for speed and ranking. Don't rewrite resumes, write cover letters, or do deep gap analysis. If the user wants tailoring, hand off to `job-application-tailor`.

## Inputs

1. **Profile.** Read `${CLAUDE_PLUGIN_ROOT}/profile/profile.md`. The *Search targets* section drives scoring; *Work history*, *Tools & skills*, and *Honest gaps* tell you what the user actually has. If *Search targets* is still placeholders, ask the user to fill it in (or give you their targets in chat) before scoring.
2. **Overrides.** If the user says anything this session that changes their targets ("I'm open to remote this week," "ignore comp for now"), apply it and say so in one line at the top of the report.
3. **The listings.** Plain text, often a messy job-board dump.

Don't ask for things already in the profile. If all three are in hand, just score.

## What the score means

The score answers one question: **"How likely is this role to be a good use of the user's time?"**

It is not a keyword-overlap count. Weigh level alignment, scope, compensation potential, domain fit, probability of getting through the screen, and long-term career value.

A role with lower keyword overlap can score **high** when title, level, responsibilities, and likely comp line up. A role with high keyword overlap can score **low** when it's a downlevel, the wrong role shape, or trips a dealbreaker.

## Scoring bands

- **90–100:** Excellent. Squarely on target.
- **80–89:** Strong. Worth pursuing.
- **70–79:** Good, with some gaps.
- **60–69:** Mixed. Only if the company is a draw or it's useful practice.
- **50–59:** Weak or downlevel. Usually skip.
- **Below 50:** Skip.

Don't flatter. Don't inflate a score because a title sounds senior.

## Hard filters (apply first)

Read these from the profile's *Search targets*: **Location**, **Compensation floor**, and **Other dealbreakers**, plus the **Do not pursue** list under *Target roles*.

- A role that trips a location dealbreaker is capped at **Maybe** and cut 15–20 points. If it's unambiguously out (e.g. on-site in a city the user won't work in), it's a **Skip**.
- If location or on-site expectation is unclear, flag it with ❓. That's a question to answer before applying.
- A role on the *Do not pursue* list is a Skip unless the JD clearly shows the scope the user actually wants.
- Name any tripped filter in the Risk line. It's the most common reason a strong-looking role isn't actually pursuable.

## Company-size gradient (how much the title matters)

Tech titles are inconsistent across company sizes. Scale how much the title counts:

- **Startup (roughly Series A–C, under ~200 people):** title barely matters. Score on the JD's real scope, ownership, and growth path. An unusual or junior-sounding title is not a down-rank if the work shows real leverage.
- **Mid-size:** balance title, scope, comp, and level.
- **Large / public:** title, level, and comp carry more weight. But big-company JDs often undersell scope, so read the responsibilities before skipping on title alone.

## Gating requirements (read the requirements block first)

The "Requirements" / "What you bring" / "Minimum qualifications" block is the disqualifier list. It's what an ATS keyword-screens against and what a recruiter checks first. Strong fit elsewhere doesn't help if the user misses a hard requirement.

Check each stated requirement against the profile, especially *Honest gaps*. Three kinds of gate:

- **Skill / stack gates:** a specific technology, tool, or method stated as required or "deep experience."
- **Domain gates:** specialized industry experience (e.g. healthcare, regulated finance, government clearance).
- **Credential gates:** a required degree, license, or certification.

How to weight them:
- **Soft framing** ("nice to have," "preferred," "a plus," "familiarity with") → small penalty, note in Risk.
- **One hard requirement** ("required," "must have," "deep experience," "strongly preferred," under a Minimum Qualifications heading, or stated twice) → cut 10–18 points and set Action no higher than **Maybe**; default to **Skip** unless there's a referral path.
- **Two or more hard gates** → **Skip**. A referral is the only reason to reconsider.
- A requirement counts only if the JD actually states it. Don't invent gates.
- A closely related skill in the same family is a transferable stretch, not a gate. Say so in Risk.

When a gate fires, say it plainly: e.g. "Requires 5+ years of X; profile shows 2. Likely screened out before the rest is read."

## Other adjustments

**Scope signals (raise modestly):** ownership of a product area, system, or team; hiring; roadmap influence; cross-functional leadership; visible impact. These matter even when the exact tools don't match.

**Negative signals (lower modestly):** staff augmentation, maintenance-only, ticket-driven execution, vague responsibilities, obvious downlevel, unrealistic requirement lists.

**Company quality (±5 max):** up for a strong product, healthy growth, good reputation; down for obvious chaos or role confusion. Don't let company quality dominate role fit.

**Compensation:** use the profile's target and floor.
- Posted comp at or above target: up to +5.
- Posted comp clearly below the floor: up to −10, but don't skip a strong-fit role on comp alone.
- Comp not listed: no adjustment.

If a role scores 85+ on fundamentals but pays below target, score it honestly and say "strong fit, likely not a comp step up."

## Triage signals

Report these alongside the score, not folded into it. One value each, no explanation.

- **Data Confidence** (High / Med / Low): how complete the *listing* is. Full JD with comp and reporting line → High. Missing comp or reporting line → Med. Teaser or fragment → Low.
- **Comp Step-Up** (High / Med / Low): would this move the user's comp forward? Unknown → Med.
- **Referral Worthy** (Yes / No): worth spending social capital on?
- **Interview Practice** (High / Med / Low): useful reps even if not ideal?

## Output format

Rank best-first. Number each role.

```
### N. Company — Role · XX/100

**Signals:** Data Confidence ... · Comp Step-Up ... · Referral Worthy ... · Interview Practice ...

**Fit:** 1–2 sentences on why it scored where it did.

**Strength:** One sentence.
**Risk:** One sentence.

**Salary:** Posted range, or "Not listed."
**Action:** Apply / Referral / Maybe / Skip
```

- Salary always sits just before Action.
- Keep each block under 120 words.
- For large batches, rank everything but show the top 15 blocks unless asked for all.

End with:

```
Top Targets:
- ...

Probably Not Worth Time:
- ...
```

No further analysis after that.

## Messy listings

Job-board dumps run together. Split on title lines, company/location lines, salary lines, and headers like "About the role," "Responsibilities," "Qualifications."

## Guardrails

- Score on time-value and fit, not keywords. Never credit the user with a skill that isn't in the profile.
- Never write a resume or cover letter here.
- Direct, concise, skimmable in under a minute.

## Version stamp

End every report with: `<!-- job-listing-filter v0.1.0 -->`

## Changelog

- **0.1.0**: Initial community release.
