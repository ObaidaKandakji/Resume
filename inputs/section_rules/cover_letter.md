# Cover Letter Rules

## Purpose

Write a real cover letter, not a resume summary in paragraph form.
The letter should make a hiring manager quickly understand:

- why this role
- why this company
- why this applicant

It should sound like a real early-career applicant making a case, not a model assembling polished sentences or a polished essay.

## Primary Backbone

Use `coverletteroutline.md` as the structural backbone for every draft.
This file is the quality-control layer on top of that outline.

That means the writer should:

- keep the same high-level flow as the outline
- use the outline's paragraph purpose to decide what belongs where
- still obey the anti-generic, anti-AI, and evidence rules in this file

If the outline and a loose drafting instinct conflict, follow the outline.

## Research Basis

This rule set is based on recurring guidance from major university career centers and hiring-focused resources:

- Harvard Extension Career Services: strong letters explain why the applicant is a good fit for the organization and how skills/experience match the role, while staying to one page.
- Yale Office of Career Strategy: the letter should persuade by connecting interest in the employer with evidence of relevant qualifications, not repeat the resume.
- MIT CAPD: effective letters show knowledge of the employer, highlight relevant skills/qualities, and are customized for both company and role.
- UC Berkeley Career Center: a good cover letter serves as the bridge between resume facts and the employer's needs.
- Columbia Career Education: GenAI can support drafting, but the final letter still needs authentic voice, specificity, and careful human editing.

## High-Return Principles

These are the changes most likely to improve response quality:

1. Start with fit, not gratitude.
   - Open with a clear sentence about the role and why it makes sense for this applicant.
   - Do not waste the first line on generic enthusiasm.

2. Add one concrete company-specific reason.
   - Use a real signal from company research: mission, product, domain, engineering environment, or job-language emphasis.
   - If the company-specific line could fit any employer, it does not count.

3. Lead with evidence early.
   - The second paragraph should already contain a strong proof point:
     project name, metric, scope, tool, system, or real operating context.

4. Translate experience into employer value.
   - Do not merely say what was built.
   - Show why that evidence matters for this job's responsibilities.

5. Include one human sentence that belongs to this applicant.
   - A brief reason, motivation, or perspective drawn from the personal profile or user notes.
   - Keep it relevant and specific.

6. Keep it short enough to read in one pass.
   - One page maximum.
   - Operational default: target roughly 250-400 words so the letter stays readable and selective.

7. Keep the voice at the right career level.
   - Sound like a strong student or recent engineering graduate.
   - Let evidence carry the letter instead of polished rhetoric.
   - If choosing between elegant wording and plain wording, choose plain wording.

## Required Structure

Use the following structure unless the user asks for a different format.
This is the operational version of `coverletteroutline.md`.

### Greeting

- Use `Dear <Hiring Manager Name>,` if known.
- Otherwise use `Dear Hiring Team,`
- Do not use `To whom it may concern`.

### Paragraph 1: Introduction

Must include all of the following:

- company name
- role title
- one company-specific reason for interest
- one truthful candidate-specific angle
- brief professional identity such as recent Computer Engineering graduate

What this paragraph must do:

- establish fit immediately
- sound intentional, not mass-applied
- stay to 2-3 sentences
- give the reader a reason to keep reading

What this paragraph must not do:

- open with generic excitement
- summarize the entire resume
- repeat soft traits without proof
- drift into philosophy, technology commentary, or broad statements about innovation

### Paragraph 2: Technical Skills and Project Proof

Use the strongest 1-2 relevant project examples, but keep the paragraph focused.

Must include:

- at least 1 named project
- concrete scope, metric, or implementation detail
- the problem, what was built or improved, and the result
- explicit connection to one or two role needs
- technologies only when they help prove fit

This paragraph should carry the main persuasive load.
It should feel like proof, not a tool list.

### Paragraph 3: Company Fit and Working Style

Use one of:

- a second relevant project
- a supporting experience signal
- a complementary strength such as troubleshooting, communication, teamwork, or operator-facing design

Must still stay evidence-based.
If using a personal detail, tie it directly to company or role fit.

This paragraph must also:

- explain why this company specifically, using company research
- include at least 1 company-specific fact, product, mission, or domain cue
- show how the applicant would contribute to the team, not only what they hope to gain
- keep soft skills grounded in a real example or real working style signal

### Paragraph 4: Conclusion

- Reaffirm fit and interest briefly.
- End with a short forward-looking sentence about contributing to the team.
- Thank the reader for their time in one plain sentence.
- Add a proper sign-off:
  - `Sincerely,`
  - `Obaida Kandakji`

Do not end on a vague thank-you paragraph with no substance.
Keep the conclusion brief.

## Evidence Selection Rules

- Use at most 2 projects as primary proof.
- Use at most 1-2 personal details from `inputs/personal_profile.md`.
- Prefer one strong personal detail over two weaker ones.
- Pull claims only from:
  - validated tailored resume
  - source resume
  - project specs
  - company research report
  - personal profile
  - explicit user notes in chat
- If a claim is not supported, omit it.
- Prefer named projects, metrics, scope counts, or concrete implementation details over broad summaries.

## Anti-Generic Rules

Ban these patterns:

- `I am excited to apply`
- `I am writing to express`
- `passionate about leveraging`
- `fast-paced environment`
- `team player`
- `results-driven`
- `hard-working`
- `eager to contribute`
- `dynamic`, `innovative`, or `cutting-edge` when unsupported or empty

Also avoid:

- paragraphs that only list technologies
- empty praise of the company
- repeating the resume bullet-by-bullet
- stacked buzzword phrases
- polished but interchangeable language that could fit any applicant
- resume bullets pasted into prose with no synthesis
- trying to mention too many projects in one letter

Ban these tone failures too:

- philosophical openings about technology, innovation, or the future
- lines that sound world-changing or grandiose
- vocabulary that sounds more like an essay than an application
- overly formal praise that a student would not naturally say
- writing that sounds like a senior engineer, consultant, or thought-leader

## Anti-AI Rules

The letter should fail review if any of these are true:

- It reads like a generic summary of the resume.
- It contains no sentence that clearly comes from this applicant's actual profile or motivation.
- It contains no company-specific line grounded in research.
- Most sentences have the same rhythm or opening pattern.
- It uses abstract praise more often than concrete evidence.
- It sounds cleaner than a real person would write, but less specific.
- It sounds too polished, literary, or philosophical for an early-career applicant.
- It sounds older, more senior, or more authoritative than the resume supports.
- It ignores the paragraph roles from `coverletteroutline.md`.

## Style Rules

- Use first person naturally. A cover letter is a personal document.
- Default voice: enthusiastic student or recent graduate who is capable, sincere, and still early in career.
- Sound smart and grounded, not profound.
- Prefer simple, direct wording over elevated or intellectual phrasing.
- Prefer modest confidence over big claims.
- Keep motivation concrete:
  - why this role fits
  - why this company fits
  - what relevant work has already been done
- Avoid abstract reflections unless they are tied to a specific company or role fact.
- Prefer direct sentences over ornate phrasing.
- Vary sentence length and openings.
- Keep paragraphs short and skimmable.
- Use plain English unless the role truly requires more technical wording.
- Mirror the job posting's tone without copying it.
- Show enthusiasm through specifics, not generic excitement phrases.
- Do not over-explain obvious points the reader can already infer from the resume.
- Do not write like a professor, essayist, consultant, or Nobel lecture.

## Output Format

Default markdown output:

```md
Dear Hiring Team,

[Introduction]

[Technical proof paragraph]

[Company fit paragraph]

[Conclusion]

Sincerely,
Obaida Kandakji
```

Do not output the cover letter as a bare block of prose without greeting and sign-off.

## Final Self-Check

Before saving, confirm all of the following:

- One page max
- Greeting present
- Sign-off present
- Company name present
- Role title present
- Professional identity present in the introduction
- At least 1 company-specific sentence from research
- At least 1 candidate-specific sentence from profile, experience, or user notes
- At least 2 concrete proof anchors:
  - metric
  - scope
  - named project
  - named tool
  - real operational context
- Introduction is 2-3 sentences
- Body contains a technical proof paragraph and a company-fit paragraph
- No unsupported claims
- No em dashes
- No banned generic opener
- Does not read like a resume recap
- Sounds like an early-career applicant, not a polished essayist

## Review Rubric

Score each draft from 0-5:

- Specificity to company
- Specificity to applicant
- Strength of evidence
- Clarity and brevity
- Structural discipline against `coverletteroutline.md`

Minimum acceptable total: `20/25`

## Sources

- [Harvard Extension Career Services: Cover Letters](https://careerservices.extension.harvard.edu/resources/cover-letters/)
- [Yale Office of Career Strategy: Cover Letters](https://ocs.yale.edu/channels/cover-letters/)
- [MIT CAPD: Cover Letter Starter Kit](https://capd.mit.edu/resources/cover-letter-starter-kit/)
- [UC Berkeley Career Center: Writing Effective Cover Letters](https://career.berkeley.edu/get-answers/writing-effective-cover-letters/)
- [Columbia CCE: Better Cover Letters with GenAI](https://www.careereducation.columbia.edu/resources/better-cover-letters-genai)
