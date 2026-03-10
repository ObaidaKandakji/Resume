# Resume Workflow

This repo now supports a no-API-key agent workflow with 4 sequential stages:

1. Research target company context.
2. Tailor resume to job description.
3. Validate truthfulness and structure.
4. Write a company-specific cover letter.

Source resume is always preserved: `Obaida_Kandakji.tex`.

Resume policy:
- Final resume must remain 1 page.
- Final resume keeps exactly 4 active projects.
- `Neural Network Driving Simulation` is protected by default and should stay active unless explicitly removed by the user.
- Agent may swap in a better-matching commented project and swap out one active project (1-in/1-out), with rationale documented.
- Resume outputs are organized per target under `tailored_resumes/<Target>/`.
- Deterministic gate available for non-negotiables:
  - `python scripts/nonnegotiable_lint.py --source Obaida_Kandakji.tex --candidate tailored_resumes/<Target>/Obaida_Kandakji_<Target>.tex --report tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.nonnegotiable_lint.md`
  - Checks: 4 active projects, unchanged bullet counts, unchanged section order, and no em dashes.
  - Does not require `latexmk`.

Project context policy:
- Use structured project specs, not loose summaries.
- Specs live in `inputs/project_specs/`.
- Template: `inputs/project_specs/TEMPLATE.md`.
- Optional TCP swap candidate starter: `inputs/project_specs/tcp_networking_optional.md`.
- Section-specific writing guides live in `inputs/section_rules/`.
- The Professional Summary uses `inputs/section_rules/professional_summary.md` for length, proof, keyword, and anti-generic rules.
- Resume bullets use `inputs/section_rules/quantification.md` to prefer real metrics and verified scope counts over guessed percentages.

## No-API Agent Mode (Recommended)

Use Codex chat with `AGENTS.md`. The stages run sequentially with file handoffs.

Note: `AGENTS.md` does not spawn independent background agents. The pipeline is executed in one run by one Codex session using staged outputs.

### Prompt To Run Full Pipeline

```text
Use AGENTS.md and run all 4 stages for this job description.
0) Research company context and write company research report.
1) Tailor resume.
2) Validate tailored resume.
3) Write cover letter using inputs/personal_profile.md.
Use inputs/project_specs/*.md as claim-evidence source for projects.
Use inputs/section_rules/*.md as section-specific writing constraints.
Save all outputs with the correct target token.
Prefer the most specific subdivision/department/branch name over a generic parent employer.
If needed for uniqueness, combine subdivision + role.
```

## Input Files

- Job descriptions: `job_descriptions/*.txt` or paste in chat
- Personal profile for cover letters: `inputs/personal_profile.md`
- Project specs for claim validation: `inputs/project_specs/*.md`
- Section rules for targeted writing constraints: `inputs/section_rules/*.md`

## Output Files

- Tailored resume:
  - `tailored_resumes/<Target>/Obaida_Kandakji_<Target>.tex`
- Company research report:
  - `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.company_research.md`
- Tailor report:
  - `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.tailor_report.md`
- Validation report:
  - `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.validation_report.md`
- Non-negotiable lint report:
  - `tailored_resumes/<Target>/reports/Obaida_Kandakji_<Target>.nonnegotiable_lint.md`
- Cover letter text:
  - `cover_letters/text/Obaida_Kandakji_<Target>.cover_letter.md`

Generated outputs in `job_descriptions/`, `tailored_resumes/`, and `cover_letters/` are gitignored by default (local-only).

## Role Files

- Resume editor: `agent_roles/resume_editor.md`
- Resume validator: `agent_roles/resume_validator.md`
- Cover letter writer: `agent_roles/cover_letter_writer.md`
- Company researcher: `agent_roles/company_researcher.md`
