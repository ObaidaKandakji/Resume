# Resume Workflow Agent

These instructions define a 3-stage pipeline for Codex in this repository.

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
- Project evidence specs:
  - `inputs/project_specs/*.md`
  - Treat these as the primary source of project-level claim validity.
- Optional project-candidate blocks in source comments:
  - Recommended marker format:
    - `% OPTIONAL_PROJECT_START: TCP_Networking`
    - `% OPTIONAL_PROJECT_END: TCP_Networking`
  - Use these markers to safely detect swappable projects.

## Naming

- `Company` token must be letters/numbers/underscore only.
- If unknown, use job file stem or `UnknownCompany`.
- Base prefix is always `Obaida_Kandakji`.

## Stage 1: Resume Tailor

Goal: minor, truthful keyword alignment edits for ATS.

Rules:
- Never modify `Obaida_Kandakji.tex`.
- Edit only these sections:
  - Professional Summary
  - Technical Skills
  - Projects
  - Experience
- Preserve existing bullet writing style (Google XYZ format).
- Google XYZ rule for project bullets:
  - Keep the same underlying structure: problem/context, what was done, and result/impact.
  - If the original bullet contains a metric/result, keep it unless clearly invalid.
  - Do not turn concise bullets into long multi-clause AI-style sentences.
- Minimal-rewrite rule:
  - Prefer micro-edits (keyword substitutions, phrase tightening, small reorder).
  - Do not fully rewrite a bullet unless required for factual correction.
  - Target high text retention for edited bullets (roughly 70%+ original wording when feasible).
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
- Do not introduce project-specific keywords unless supported by:
  - current resume text, or
  - a project spec card with explicit evidence.
- One-page constraint is mandatory.
- Active projects target is exactly 4.
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
- `tailored_resumes/Obaida_Kandakji_<Company>.tex`
- `tailored_resumes/reports/Obaida_Kandakji_<Company>.tailor_report.md`

## Stage 2: Resume Validator

Goal: verify Stage 1 output is truthful and structurally safe.

Deterministic gate (run first):
- Run:
  - `python scripts/nonnegotiable_lint.py --source Obaida_Kandakji.tex --candidate tailored_resumes/Obaida_Kandakji_<Company>.tex --report tailored_resumes/reports/Obaida_Kandakji_<Company>.nonnegotiable_lint.md`
- This hard-checks non-negotiables only:
  - 4 active projects
  - bullet counts unchanged
  - section order unchanged
  - no em dashes

Checks:
- Compare source resume vs tailored resume.
- Flag any unsupported claim, inflated scope, or invented keyword mapping.
- Verify section order and bullet counts remain unchanged.
- Verify edited project bullets still follow Google XYZ shape (problem/context + action + result).
- Verify edited bullets were minimally changed rather than fully rewritten, unless explicitly justified.
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

After validation passes:
- Attempt resume PDF generation:
  - `python scripts/compile_pdf.py --tex tailored_resumes/Obaida_Kandakji_<Company>.tex --output tailored_resumes/Obaida_Kandakji_<Company>.pdf`
- If no compiler is available, keep `.tex` and report the limitation.

Output:
- `tailored_resumes/reports/Obaida_Kandakji_<Company>.validation_report.md`
- `tailored_resumes/reports/Obaida_Kandakji_<Company>.nonnegotiable_lint.md`
- Optional: `tailored_resumes/Obaida_Kandakji_<Company>.pdf`

If validation fails:
- Revise tailored file once.
- Re-run validation and clearly mark final status.

## Stage 3: Cover Letter Writer

Goal: produce a tailored cover letter using validated resume + personal profile.

Rules:
- Use only claims supported by source/tailored resume and user profile.
- Use project spec cards to choose the strongest relevant project evidence.
- Prioritize 2-3 most relevant projects/skills for the target role.
- Keep concise, professional, and specific to company/job.
- Human-sounding writing only:
  - Never use em dashes (`—`).
  - Avoid AI-generic phrasing (for example: "I am excited to apply", "I am writing to express", "passionate about leveraging", "fast-paced environment", "team player").
  - Prefer concrete, plain sentences over hype.
  - Vary sentence structure and length naturally.
- Personal-profile usage constraint:
  - Use at most 1-2 personal details from `inputs/personal_profile.md`.
  - Select only details that directly strengthen fit for the specific role.
  - Do not list many personal facts.
- Before saving, run a quick self-check:
  - No em dash characters.
  - No unsupported claims.
  - No more than 2 personal details included.

Primary output:
- `cover_letters/text/Obaida_Kandakji_<Company>.cover_letter.md`

Optional PDF output:
- Also write `cover_letters/text/Obaida_Kandakji_<Company>.cover_letter.tex`
- If LaTeX tools are available, compile to:
  - `cover_letters/pdf/Obaida_Kandakji_<Company>.cover_letter.pdf`
- If compile tool is unavailable, keep `.md` and `.tex` only and report that limitation.

## Required Final Summary

After all stages, provide:
- Paths to all generated files
- Keywords added and skipped
- Validation pass/fail result
- Whether PDF generation succeeded
