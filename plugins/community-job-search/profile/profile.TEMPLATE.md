# Profile

**This is a template.** Copy it to **`~/Documents/job-search/profile.md`** and fill in the copy. Every skill reads that copy; it is the only place your personal details live, and the skills themselves contain no facts about you.

Your copy lives outside the plugin so that plugin updates never touch it. The skills never overwrite or edit it. If a skill needs a section your copy doesn't have yet, it asks you for that one section and, with your OK, appends it to the end as a new section marked `(added YYYY-MM-DD)`. If an old placeholder copy of the heading is still in your file, the dated copy wins; delete the old one whenever you like.

**How to fill it in:**
- Replace every `[bracketed]` placeholder. Delete the prompt text once you've written your own.
- Be exact with dates and titles. Copy them from your LinkedIn so the resume never contradicts it.
- If a section doesn't apply, write "N/A". An empty section makes the skills that need it stop and ask you.
- Sections marked *(optional)* can stay as placeholders; the skills skip them.
- Your copy is private. Don't commit it to a shared repo.

---

## Working folder

All the files the skills read and write live in one folder: **`~/Documents/job-search/`**. Nothing to fill in here; this section is for reference.

What lives there (the skills create the others as needed):
- `profile.md`: your copy of this file
- `pipeline.md`: your job-search pipeline (pipeline-tracker writes it)
- `pipeline-log.md`: append-only log of every pipeline change (pipeline-tracker writes it)
- `network.md`: people and relationships outside live roles (network-tracker writes it)
- `prep-*.md`, `CARD-*.md`: interview briefs and one-page cards (interview-prep writes them)
- `debrief-*.md`: post-interview notes (interview-debrief writes them)
- *(optional)* an activity tracker exported as CSV, if you keep one (job-search-review reads it)

## Contact

- **Name:** [First Last]
- **Location:** [City, State]
- **Phone:** [+1 ...]
- **Email:** [you@example.com]
- **LinkedIn:** [linkedin.com/in/...]
- **Portfolio / GitHub / site:** [optional]

## LinkedIn: dates & titles (sanity check)

List every role in **strict reverse-chronological order** (most recent end date first). Dates must match LinkedIn exactly.

- **[Company]**, [MM/YYYY] to [MM/YYYY or Present]. [Title]. (If you were promoted, list each title with its own dates.)
- **[Company]**, [MM/YYYY] to [MM/YYYY]. [Title].

## Canonical facts

The numbers and framings you're willing to stand behind in an interview. The skills will only use these; they won't invent or round up.

- **Years of experience:** [Total years in your field, plus any other figure you might quote (a specialty, managing people). List each separately; the skills will never merge them.]
- **Most recent role:** [Title at Company]
- **How you left / why you're looking:** [Your short, honest answer to "why are you looking?" so your story stays consistent.]
- **Headline accomplishments with metrics:** [2–4 you can defend line by line]

## Work history

### [Company]: [Title] · [MM/YYYY] to [MM/YYYY]
[City or Remote] · [On-site / Hybrid / Remote]

- [What you built, led, shipped, or changed. Include a metric when you have a real one.]
- [...]

(Repeat for each role.)

## Education & certifications

Exact names and years only. No approximations.

- [Degree, Field, School, Year]
- [Certification, Issuer, Year]

## Tools & skills

What you're confident claiming in an interview. Anything not listed here will never show up on a tailored resume as your experience.

[Tools, methods, and skills, separated by ·]

## Honest gaps

Things you **don't** have that roles often ask for. The skills use this to flag real screen-outs instead of glossing over them.

- [A requirement roles in your target often list that you don't meet yet]

## Honest framings *(optional)*

Things you've done that are easy to overstate. Write the truthful way to say each one; the skills will use your wording and never inflate it.

- [e.g. "Adjacent to X, not hands-on X." / "Led the rollout, did not build the system."]

## Domain experience

Industries, customers, or problem spaces where you have real depth.

- [Industry, customer type, or problem area]

## Positioning *(optional)*

How you want to come across, and how that changes by audience.

- **Primary identity:** [One line: what you are, professionally]
- **Secondary identity:** [Optional second angle you can lead with when it fits]
- **Positioning modes:** [Optional. e.g. "Startups: lead with speed and range. Large or regulated orgs: lead with process and reliability."]
- **Targeted assets:** [Optional. Background worth surfacing only for certain employers, e.g. "agency experience, for client-facing roles". Say when to use it and when not to.]
- **Common objections and your counters:** [Optional. e.g. "Too senior for this level → ...". One line each.]

---

## Search targets

This section drives the scoring in job-listing-filter and recruiter-triage, and the offer check in pipeline-tracker.

### Target roles

- **Tier 1 (squarely on target):** [Job titles you're actively pursuing]
- **Tier 2 (only if company or scope is strong):** [Titles worth a look under the right conditions]
- **Do not pursue:** [Titles or role shapes you'll skip, e.g. "contract only"]

### Level & scope

[The level you're aiming for and the scope that makes a role worth it.]

### Scope questions to ask early *(optional)*

[Questions that have to be answered before you invest in a process, e.g. "Is the role new or a backfill?", "Is headcount approved?", "What does the first 90 days look like?". recruiter-triage asks these when the answers are unknown.]

### Engagement types

- **Full-time:** [yes / no]
- **Part-time:** [yes / no; hours per week you want]
- **Contract or contract-to-hire:** [yes / no; minimum duration or rate, if any]

### Company preferences

- **Stage / size:** [Company stage and headcount range you want]
- **Industries you want:** [...]
- **Industries you'll skip:** [...]

### Warm-channel-only *(optional)*

[Companies, sectors, or company types worth pursuing **only** through a referral, intro, or inbound recruiter, because cold applications there don't convert for you. The skills still score them, but recommend the warm route instead of a cold application.]

### Disguised-role tells *(optional)*

[Role shapes that look like your target but aren't, and the phrases that give them away. e.g. "Research roles titled like delivery roles: publications, academic partnerships, PhD preferred." The listing filter caps a role when two or more tells appear.]

### Location (hard filter)

- **Where you'll work:** [Remote, hybrid, or on-site, and in which regions]
- **What's a dealbreaker:** [Anything about location that rules a role out, e.g. relocation]
- **Travel:** [Maximum travel you'll accept, e.g. "up to 25%"]

### Compensation

- **Target total comp:** [$X to $Y, or an hourly rate for part-time or contract]
- **Floor (walk-away):** [$Z]
- **Notes:** [Optional: trade-offs you'd accept, such as more equity for less cash]

### Other dealbreakers

- [Anything else that rules a role out]

### Channels that work for you

[Optional. Which routes into a job have worked for you, e.g. referrals, inbound recruiters, or cold applications. The pipeline tracker uses this to mark cold vs warm applications.]

### Offer go/no-go gates

[The 2–4 things an offer must satisfy before you say yes, written while calm. e.g. "Title and comp match the real scope, in writing." pipeline-tracker reminds you of these the moment anything reaches OFFER.]

---

## Search context

- **Search start date:** [YYYY-MM-DD, the date your search started. The overviews show weeks since.]
- **Runway end date** *(optional)*: [YYYY-MM-DD, if you want the overview to show weeks left]
- **Weekly targets:** [e.g. "5 applications, 3 warm outreaches, 1 follow-up". job-search-review grades against these.]
- **Networking cap:** [Max new coffees or calls per week, default 2]
- **Accountability partner or group** *(optional)*: [Who you report progress to, if anyone. job-search-review drafts an update for them.]
- **Work-search requirement** *(optional)*: [If unemployment benefits require you to log a number of job-search activities per week, note the rule here.]

## Interview material

interview-prep builds every brief from this section. Keep the answers short; they're anchors, not scripts.

- **90-second intro notes:** [What your intro should cover and in what order]
- **Lead story:** [The project or accomplishment you go deepest on. Steps, your role, the result, how you measured it.]
- **Second story:** [A different one, in three lines, for when they ask for another]
- **Why this field / what excites you:** [Your honest answer]
- **Something interesting you've seen recently:** [One item and the date you wrote it. Refresh it every month or so.]
- **Standing answers to tricky questions:** [e.g. "Why did you leave?", "Why the gap?". One or two lines each.]
- **Things never to claim:** [Anything you must not say in an interview]

## Answer-if-asked facts

Facts that come up on applications and calls. The skills use these only when asked; they never volunteer them.

- **Work authorization:** [e.g. "US citizen", "Requires sponsorship"]
- **Earliest start date:** [...]
- **Notice period:** [...]
- **Willing to relocate:** [yes / no]
- **References available:** [yes / no; who, if you want them tracked in network.md]
- **Salary history policy:** [e.g. "Don't share"]

---

## Voice & writing

How you actually write. The skills use this for cover letters, recruiter replies, network messages and email edits, so they sound like you, not like an AI.

- **Tone:** [A few words describing your writing style]
- **Sentence style:** [e.g. "Short sentences, plain words"]
- **Punctuation habits:** [Any punctuation or formatting habits to follow or avoid]
- **Things you never say:** [Phrases that don't sound like you]
- **Sign-off:** [How you sign off with recruiters vs. peers]
- **Availability line for recruiter replies:** [When you're generally free, with time zone]

## Private notes *(optional)*

- **Private notes file:** [A path inside your working folder for sensitive context that should never appear in any output. Skills may read it as background only.]

## Profile changelog

- [YYYY-MM-DD] Created.
