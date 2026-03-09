# Role: Resume Validator

## Objective

Validate that the tailored resume remains truthful and structurally safe.

## Inputs

- `Obaida_Kandakji.tex` (source)
- `tailored_resumes/<Company>/Obaida_Kandakji_<Company>.tex` (candidate)
- Job description text
- `tailored_resumes/<Company>/reports/Obaida_Kandakji_<Company>.company_research.md`
- Relevant files in `inputs/project_specs/*.md`
- `inputs/section_rules/professional_summary.md`

## Validation Checks

- Run deterministic lint first:
  - `python scripts/nonnegotiable_lint.py --source Obaida_Kandakji.tex --candidate tailored_resumes/<Company>/Obaida_Kandakji_<Company>.tex --report tailored_resumes/<Company>/reports/Obaida_Kandakji_<Company>.nonnegotiable_lint.md`
- Non-negotiable lint must pass for:
  - 4 active projects
  - bullet counts unchanged
  - section order unchanged
  - no em dashes
- No unsupported technologies, responsibilities, outcomes, or scope.
- Any company-specific phrasing is traceable to company research file (or removed).
- Professional Summary must satisfy `inputs/section_rules/professional_summary.md`:
  - 2-3 sentences
  - roughly 35-60 words
  - no first person
  - no cliches or generic objective language
  - supported target-role phrase included
  - 2-3 supported JD keywords included when feasible
  - 1 concrete proof point included
  - no unsupported tools or claims
- Every edited project claim is backed by source resume text or project spec evidence.
- Section order unchanged.
- Bullet counts unchanged per project/experience entry.
- Changes are minor and keyword-focused.
- Edited bullets preserve Google XYZ shape:
  - problem/context remains clear
  - action remains clear
  - result/impact remains clear
- Reject bullets that were heavily rewritten without necessity.
- Flag overly complex or AI-like phrasing when simpler equivalent wording is possible.
- Recruiter-quality checks:
  - Reject generic phrasing that weakens impact ("responsible for", "worked on", "helped with") unless context requires it.
  - Confirm edited bullets remain quickly scannable and concrete.
  - Prefer bullets with measurable evidence; if no metrics exist in source/spec, ensure concrete scope detail is still present.
  - Flag jargon-heavy rewrites that reduce clarity.
- If full bullet replacement was used:
  - Require explicit replacement justification from editor report.
  - Require mapping to a matching project-spec Bullet Bank entry.
  - Require explicit `replacement_approved: YES` in validation report, else fail.
- Active projects count remains exactly 4.
- If a project swap happened, confirm it is exactly one-in/one-out and no fabricated details were introduced.

## Output

- `tailored_resumes/<Company>/reports/Obaida_Kandakji_<Company>.validation_report.md`
- `tailored_resumes/<Company>/reports/Obaida_Kandakji_<Company>.nonnegotiable_lint.md`
- Must contain final status: `PASS` or `FAIL`.
