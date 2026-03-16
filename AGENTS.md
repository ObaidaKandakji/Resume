# Resume Workflow Agent

These instructions define a 4-stage pipeline for Codex in this repository.

## Capability Note

- `AGENTS.md` cannot launch independent background agents by itself.
- Instead, execute stages sequentially in one run and pass outputs as files between stages.

## Inputs

- Immutable source resume: `Obaida_Kandakji.tex`
- Job description:
  - Prefer text provided in chat, or
  - Use latest `.txt` in `job_descriptions/`
- Personal background (for cover letter):
  - `inputs/personal_profile.md` if present, plus any extra user notes in chat
- Cover letter drafting backbone:
  - `coverletteroutline.md`
- Project evidence specs:
  - `inputs/project_specs/*.md`
  - Treat these as the primary source of project-level claim validity.
- Section-specific writing guides:
  - `inputs/section_rules/*.md`
  - `inputs/section_rules/professional_summary.md` is the primary quality guide for the Professional Summary.
  - `inputs/section_rules/quantification.md` defines how to use metrics and scope counts without inventing impact.
- Optional project-candidate blocks in source comments:
  - Recommended marker format:
    - `% OPTIONAL_PROJECT_START: TCP_Networking`
    - `% OPTIONAL_PROJECT_END: TCP_Networking`
  - Use these markers to safely detect swappable projects.

## Naming

- `Target` token must be letters/numbers/underscore only.
- Derive `Target` from the most specific identifier in the posting:
  - subdivision, department, branch, bureau, or team name first
  - otherwise specific company name
  - otherwise role title
- If the top-level employer is too generic (for example `Government_of_Canada`), do not use it by itself when a more specific subdivision is available.
- If subdivision alone is still ambiguous, combine subdivision + role:
  - example: `Employment_and_Social_Development_Canada_Software_Developer`
- If unknown, use normalized role title, then job file stem, then `UnknownTarget`.
- Base prefix is always `Obaida_Kandakji`.
- Per-target output directory:
  - `tailored_resumes/<Target>/`
  - Create this folder (and `tailored_resumes/<Target>/reports/`) before writing outputs.

## Stage 0: Company Research

Goal: gather high-signal company context to improve resume keyword prioritization and cover-letter angle.

Research scope:
- Company mission and positioning
- Core products/services
- Business domain and customer focus
- Engineering signals relevant to the role (if available)
- Tone/culture clues from official company pages and job posting language

Source rules:
- Prefer official sources first:
  - company website
  - careers pages
  - official blog/newsroom
- Use the job posting itself as a primary context source.
- Avoid forum/speculation sources unless absolutely necessary.
- Do not invent company facts; mark unknown items as `UNVERIFIED`.
- Include source links in the `Sources` section for each major company claim used downstream.

Output:
- `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.company_research.md`

Required sections in research output:
- `Company Snapshot`
- `Mission and What They Do`
- `Role-Relevant Signals`
- `Language/Tone Cues To Mirror`
- `Resume Angle Recommendations`
- `Cover Letter Angle Recommendations`
- `Sources`

Handoff rule:
- Stage 1 and Stage 3 must use this research file for company-specific positioning.
- Resume edits should use this primarily to prioritize emphasis, not to inject unsupported company claims into resume bullets.

## Stage 1: Resume Tailor

Goal: minor, truthful keyword alignment edits for ATS.

Rules:
- Persona and quality bar:
  - Act like a senior recruiter screening 200 resumes per day.
  - Prioritize fast clarity, relevance, and concrete impact over buzzwords.
  - Keep bullets specific and scannable in one quick pass.
- Never modify `Obaida_Kandakji.tex`.
- Edit only these sections:
  - Professional Summary
  - Technical Skills
  - Projects
  - Experience
- Preserve existing bullet writing style (Google XYZ format).
- Professional Summary rule:
  - Read `inputs/section_rules/professional_summary.md` before editing the summary.
  - The summary may be rewritten more freely than bullets when needed to remove generic language and align to the role.
  - Keep it to 2-3 sentences and roughly 35-60 words.
  - No first person, no cliches, and no generic objective language.
  - Include the target role title, 2-3 supported JD keywords, and 1 concrete proof point when truthfully possible.
  - Mention only tools and claims supported elsewhere in the resume or project specs.
  - If a better summary cannot be written without filler or unsupported claims, shorten or lightly revise it instead of forcing a generic rewrite.
- Google XYZ rule for project bullets:
  - Keep the same underlying structure: problem/context, what was done, and result/impact.
  - If the original bullet contains a metric/result, keep it unless clearly invalid.
  - Do not turn concise bullets into long multi-clause AI-style sentences.
- Minimal-rewrite rule:
  - Prefer micro-edits (keyword substitutions, phrase tightening, small reorder).
  - Do not fully rewrite a bullet unless required for factual correction.
  - Target high text retention for edited bullets (roughly 70%+ original wording when feasible).
- Recruiter-style writing constraints:
  - Avoid dense jargon stacking and acronym-heavy phrasing when simpler wording is available.
  - Avoid generic filler language (for example: "responsible for", "worked on", "helped with").
  - Prefer measurable achievements and concrete scope signals:
    - metrics when available (%, counts, latency, throughput, etc.)
    - otherwise concrete implementation scope (number of services, components, users, workflows, systems).
  - Keep each bullet focused on one clear value statement, not broad hype.
- Quantification rule:
  - Read `inputs/section_rules/quantification.md` before editing bullets.
  - Preserve valid existing metrics already present in the source resume.
  - Approved `Quantification Candidates` may be used in the actual resume when they improve clarity and fit.
  - If no measured impact metric exists, prefer verified scope counts over invented percentages.
  - Derived estimates are allowed only when the project spec documents the math and the wording stays approximate.
  - Never invent performance, efficiency, productivity, revenue, latency, or time-saved percentages.
  - Ignore any project-spec section labeled as hypothesis-only material such as `Potential Metrics To Verify` unless the user has explicitly confirmed those numbers.
  - Use numbers in short, natural phrasing:
    - one strong number per bullet when feasible
    - plain verbs such as `reduced`, `improved`, `cut`, `sped up`, or `automated`
    - avoid metric stuffing or long AI-polished clauses
  - If the quantified version sounds awkward or generic, skip the number and keep the bullet cleaner.
- Bullet-bank usage rule:
  - Bullet Bank entries in project specs are reference material, not default replacements.
  - Try micro-edits first.
  - Only use full bullet replacement as a last resort when keyword fit cannot be achieved with micro-edits.
  - If full replacement is used, tailor report must include:
    - Why micro-edits were insufficient
    - Which source bullet was replaced
    - Which Bullet Bank entry was used
    - Evidence that factual scope stayed unchanged
- Preserve section order and LaTeX macro structure.
- Keep bullet count unchanged per project/experience entry.
- Never fabricate tools, responsibilities, outcomes, or impact.
- Unsupported keywords must be skipped and documented.
- Before writing edits, read relevant project spec cards and map JD keywords to spec-backed claims.
- Before writing edits, read the company research report and prioritize role/company-relevant evidence from the resume.
- Do not introduce project-specific keywords unless supported by:
  - current resume text, or
  - a project spec card with explicit evidence.
- Do not add company-specific factual claims into resume bullets unless directly relevant and fully verified.
- One-page constraint is mandatory.
- Active projects target is exactly 4.
- Protected project rule:
  - `Neural Network Driving Simulation` is protected by default because it adds distinctive recruiter signal and portfolio uniqueness.
  - Do not deactivate, swap out, or remove this project unless the user explicitly asks.
  - If an optional project is activated, choose the project to deactivate from the other active projects first.
- Project swap rule (for commented candidate projects):
  - If a commented-out project in the source clearly matches the job better (for example TCP/networking keywords), you may activate it.
  - If you activate one commented project, you must deactivate exactly one currently active project.
  - Do not activate more than one commented project per run unless user explicitly asks.
  - Preserve bullet text truthfully; only minor phrasing edits are allowed.
  - Only swap from clearly delimited optional project blocks; if blocks are ambiguous, skip swap and note it.
  - In the tailor report, explicitly state:
    - Which project was activated
    - Which project was deactivated
    - Why the swap improved keyword alignment
    - For each edited bullet, a short XYZ map:
      - `Problem/Context: ...`
      - `Action: ...`
      - `Result: ...`

Output:
- `tailored_resumes/<Target>/Obaida_Kandakji_<Target>.tex`
- `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.tailor_report.md`

Tailor report requirement:
- If the Professional Summary changed, include:
  - `target_role_phrase`
  - `jd_keywords_used`
  - `proof_point_used`
  - `proof_source`

## Stage 2: Resume Validator

Goal: verify Stage 1 output is truthful and structurally safe.

Deterministic gate (run first):
- Run:
  - `python scripts/nonnegotiable_lint.py --source Obaida_Kandakji.tex --candidate tailored_resumes/<Target>/Obaida_Kandakji_<Target>.tex --report tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.nonnegotiable_lint.md`
- This hard-checks non-negotiables only:
  - 4 active projects
  - bullet counts unchanged
  - section order unchanged
  - no em dashes

Checks:
- Compare source resume vs tailored resume.
- Flag any unsupported claim, inflated scope, or invented keyword mapping.
- Verify any company-specific phrasing is traceable to the company research report and not fabricated.
- Verify the Professional Summary follows `inputs/section_rules/professional_summary.md`:
  - 2-3 sentences
  - roughly 35-60 words
  - no first person
  - no cliches or generic objective language
  - includes a supported target-role phrase
  - includes 2-3 supported JD keywords when feasible
  - includes 1 concrete proof point
  - mentions only supported tools and claims
- Verify section order and bullet counts remain unchanged.
- Verify edited project bullets still follow Google XYZ shape (problem/context + action + result).
- Verify edited bullets were minimally changed rather than fully rewritten, unless explicitly justified.
- Verify recruiter-readability quality:
  - Bullets remain specific and non-generic.
  - Edited bullets include measurable or concrete scope detail when available from source/spec evidence.
  - No unnecessary jargon-heavy rewrites.
- Verify quantification safety:
  - Any percentage or numeric improvement claim is supported by the source resume or project spec.
  - Any derived estimate is traceable to documented math in the project spec and presented as approximate when needed.
  - Scope counts are preferred over invented impact metrics when measured outcomes do not exist.
  - Hypothesis-only sections such as `Potential Metrics To Verify` were not used unless explicitly user-confirmed.
  - Quantified bullets remain concise, human-sounding, and not overloaded with numbers.
- If any full bullet replacement occurred:
  - Confirm written justification exists in tailor report.
  - Confirm replacement maps to an approved Bullet Bank entry from the corresponding project spec.
  - Confirm factual scope did not expand.
  - Mark `replacement_approved: YES/NO` in validation report.
- Verify project-level claims in edited bullets are backed by project specs or original resume text.
- Verify active project count is still 4.
- Verify swap integrity when a commented project was activated:
  - Exactly one project in and one project out.
  - No fabricated project details introduced during swap.
  - `Neural Network Driving Simulation` remained active unless the user explicitly overrode that rule.

Output:
- `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.validation_report.md`
- `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.nonnegotiable_lint.md`

If validation fails:
- Revise tailored file once.
- Re-run validation and clearly mark final status.

## Stage 3: Cover Letter Writer

Goal: produce a tailored cover letter using validated resume + personal profile.

Rules:
- Read `coverletteroutline.md` first and use it as the drafting backbone.
- Read `inputs/section_rules/cover_letter.md` before drafting.
- Use only claims supported by source/tailored resume and user profile.
- Use company research output to tailor positioning, motivation framing, and company-specific language.
- Use project spec cards to choose the strongest relevant project evidence.
- Prioritize 1-2 primary projects for the target role, with a second proof point only when it improves fit.
- Keep concise, professional, specific to company/job, and clearly early-career in voice.
- Write an actual letter with greeting, body paragraphs, and sign-off.
- Follow the outline-backed structure:
  - Introduction:
    - 2-3 sentences
    - role title
    - company name
    - one company-specific reason for interest
    - one candidate-specific hook
    - brief professional identity
  - Technical proof paragraph:
    - strongest project evidence
    - concrete metric, scope, or implementation detail
    - direct link to role needs
  - Company fit paragraph:
    - why this company specifically
    - one teamwork, working-style, or supporting proof signal
    - at most 1 relevant personal detail if it strengthens fit
  - Conclusion:
    - brief reaffirmation of fit
    - plain thank-you sentence
    - sign-off
- Human-sounding writing only:
  - Never use em dashes (`—`).
  - Avoid AI-generic phrasing (for example: "I am excited to apply", "I am writing to express", "passionate about leveraging", "fast-paced environment", "team player").
  - Prefer concrete, plain sentences over hype.
  - Vary sentence structure and length naturally.
  - Sound like a strong student or recent graduate, not a philosopher, essayist, or senior engineer.
  - Prefer simple, grounded wording over elevated or intellectual phrasing.
  - Keep confidence modest and let evidence carry the argument.
- Personal-profile usage constraint:
  - Use at most 1-2 personal details from `inputs/personal_profile.md`.
  - Select only details that directly strengthen fit for the specific role.
  - Do not list many personal facts.
- Before saving, run a quick self-check:
  - No em dash characters.
  - No unsupported claims.
  - No more than 2 personal details included.
  - Any company-specific statement is supported by the research report.
  - Paragraph structure matches `coverletteroutline.md`.
  - Greeting and sign-off are present.
  - At least 1 company-specific sentence is present.
  - At least 1 candidate-specific sentence is present.
  - The voice sounds like an enthusiastic early-career applicant.

Primary output:
- `cover_letters/text/Obaida_Kandakji_<Target>.cover_letter.md`

## Required Final Summary

After all stages, provide:
- Paths to all generated files
- Keywords added and skipped
- Validation pass/fail result
- Summary audit:
  - target-role phrase used
  - JD keywords mirrored in summary
  - proof point used in summary
