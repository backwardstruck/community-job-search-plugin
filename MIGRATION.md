# Migrating from an older fork

For anyone running an earlier personal fork of this job-search plugin, with a filled-in profile inside the old plugin folder. The goal is to switch to `community-job-search` **without losing or overwriting your profile.**

The big change: your profile no longer lives inside the plugin. It lives at **`~/Documents/job-search/profile.md`**, and the skills never overwrite or edit it. If a skill needs a section your profile doesn't have, it asks you for that one section and, with your OK, appends it to the end as a new dated section; the dated copy wins over any old placeholder.

## Steps

1. **Back up your current profile first.** Find your profile file inside your old plugin's folder (often `profile/profile.md`) and copy it somewhere safe, e.g. `~/Documents/profile-backup.md`. Do this before uninstalling anything; removing a plugin can delete its folder.

2. **Uninstall the old fork.** Use the old plugin's own name (shown under `/plugin` → **Installed**, or in Customize → Plugins in the desktop app):
   ```
   /plugin uninstall <old-plugin-name>@<old-marketplace-name>
   ```
   In the desktop app, remove it from Customize → Plugins.

3. **Install community-job-search.** Follow *Install* in the [README](README.md):
   ```
   /plugin marketplace add backwardstruck/community-job-search-plugin
   /plugin install community-job-search@community-job-search
   ```

4. **Move your profile into the working folder.** Create `~/Documents/job-search/` if it doesn't exist, and copy your backed-up profile there as `profile.md`. If you already have a `pipeline.md` or other job-search files, move them into the same folder.
   ```
   mkdir -p ~/Documents/job-search
   ls ~/Documents/job-search/profile.md   # should say "No such file"
   cp -n ~/Documents/profile-backup.md ~/Documents/job-search/profile.md
   ```
   Then run `ls -l ~/Documents/job-search/profile.md` to confirm the copy happened (on some systems `cp -n` reports success even when it skips). `cp -n` refuses to overwrite. If a `profile.md` is already there (for example, one a skill created from the template), open both files and merge by hand; don't replace either. Don't replace your profile with the template. Your existing headings mostly carry over; the skills read sections by meaning, so you don't need to rename them.

5. **Answer the missing-section prompts.** Use the plugin normally. When a skill needs a section your profile doesn't have yet, it asks for that one section, shows you the exact text, and appends it only if you say yes. You can skip any prompt; the skill carries on and tells you what's missing. To fill everything in at once instead, compare your file with `plugins/community-job-search/profile/profile.TEMPLATE.md`.

## Profile sections the skills read

One line each: what it's for, and the skills that use it. *(optional)* sections can stay empty.

| Section | Used for | Read by |
|---|---|---|
| Contact | Resume header, sign-offs, recruiter replies | job-application-tailor, recruiter-triage |
| LinkedIn: dates & titles | Exact dates and titles; the resume never contradicts them | job-application-tailor |
| Canonical facts | Years of experience, most recent role, why you're looking, headline metrics | job-application-tailor, interview-prep |
| Work history | The only source for resume bullets and interview stories | job-application-tailor, interview-prep, job-listing-filter |
| Education & certifications | Exact credential names and years; credential gates in listings | job-application-tailor, job-listing-filter |
| Tools & skills | What may appear on a resume as your experience | job-application-tailor, job-listing-filter |
| Honest gaps | Real screen-out risks, never claimed as experience | job-listing-filter, job-application-tailor, interview-prep |
| Honest framings *(optional)* | Truthful wording for things easy to overstate | job-application-tailor, interview-prep |
| Domain experience | Domain fit; which jargon needs defining in prep | job-listing-filter, interview-prep |
| Positioning *(optional)* | Identity, audience modes, targeted assets, "Common objections and your counters" | job-application-tailor, job-listing-filter, interview-prep |
| Target roles | Tier 1, tier 2, and do-not-pursue titles | job-listing-filter, recruiter-triage |
| Level & scope | The level and scope that make a role worth it | job-listing-filter, recruiter-triage |
| Scope questions to ask early *(optional)* | Questions asked before any call gets booked | recruiter-triage, interview-prep |
| Engagement types | Full-time, part-time (hours), contract | job-listing-filter, recruiter-triage |
| Company preferences | Stage, size, industries wanted and skipped | job-listing-filter, recruiter-triage |
| Warm-channel-only *(optional)* | Companies or sectors to pursue only by referral or intro | job-listing-filter, recruiter-triage, pipeline-tracker |
| Disguised-role tells *(optional)* | Phrases that reveal a look-alike role that isn't your target | job-listing-filter |
| Location | Where you'll work, dealbreakers, travel limit | job-listing-filter, recruiter-triage |
| Compensation | Target and floor | job-listing-filter, recruiter-triage |
| Other dealbreakers | Anything else that rules a role out | job-listing-filter, recruiter-triage |
| Channels that work for you | Default warm vs. cold tagging for applications | pipeline-tracker |
| Offer go/no-go gates | The checklist shown the moment anything reaches OFFER | pipeline-tracker |
| Search context | Start date, runway, weekly targets, networking cap, accountability partner, work-search rule | pipeline-tracker, pipeline-overview, job-search-review, network-tracker, network-overview |
| Interview material | 90-second intro, lead and second story, standing answers, things never to claim | interview-prep, interview-debrief |
| Answer-if-asked facts | Work authorization, start date, notice period, relocation, salary history policy; used only when asked | job-application-tailor, recruiter-triage |
| Voice & writing | How every draft should sound, sign-offs, availability line | check-email, recruiter-triage, job-application-tailor, network-tracker |
| Private notes *(optional)* | Path to background-only notes that never appear in output | job-application-tailor |

Sections your profile doesn't have yet get asked for one at a time, the first time a skill needs them.
