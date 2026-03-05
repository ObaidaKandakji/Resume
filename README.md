# Resume Workflow

This repo now supports a no-API-key agent workflow with 3 sequential stages:

1. Tailor resume to job description.
2. Validate truthfulness and structure.
3. Write a company-specific cover letter.

Source resume is always preserved: `Obaida_Kandakji.tex`.

Resume policy:
- Final resume must remain 1 page.
- Final resume keeps exactly 4 active projects.
- Agent may swap in a better-matching commented project and swap out one active project (1-in/1-out), with rationale documented.
- Deterministic gate available for non-negotiables:
  - `python scripts/nonnegotiable_lint.py --source Obaida_Kandakji.tex --candidate tailored_resumes/Obaida_Kandakji_<Company>.tex --report tailored_resumes/reports/Obaida_Kandakji_<Company>.nonnegotiable_lint.md`
  - Checks: 4 active projects, unchanged bullet counts, unchanged section order, and no em dashes.
  - Does not require `latexmk`.

Optional resume PDF generation:
- `python scripts/compile_pdf.py --tex tailored_resumes/Obaida_Kandakji_<Company>.tex --output tailored_resumes/Obaida_Kandakji_<Company>.pdf`
- The agent can run this automatically when compiler tooling is available.

Project context policy:
- Use structured project specs, not loose summaries.
- Specs live in `inputs/project_specs/`.
- Template: `inputs/project_specs/TEMPLATE.md`.
- Optional TCP swap candidate starter: `inputs/project_specs/tcp_networking_optional.md`.

## No-API Agent Mode (Recommended)

Use Codex chat with `AGENTS.md`. The stages run sequentially with file handoffs.

Note: `AGENTS.md` does not spawn independent background agents. The pipeline is executed in one run by one Codex session using staged outputs.

### Prompt To Run Full Pipeline

```text
Use AGENTS.md and run all 3 stages for this job description.
1) Tailor resume.
2) Validate tailored resume.
3) Write cover letter using inputs/personal_profile.md.
Use inputs/project_specs/*.md as claim-evidence source for projects.
Save all outputs with the correct company token.
```

## Input Files

- Job descriptions: `job_descriptions/*.txt` or paste in chat
- Personal profile for cover letters: `inputs/personal_profile.md`
- Project specs for claim validation: `inputs/project_specs/*.md`

## Output Files

- Tailored resume:
  - `tailored_resumes/Obaida_Kandakji_<Company>.tex`
- Tailor report:
  - `tailored_resumes/reports/Obaida_Kandakji_<Company>.tailor_report.md`
- Validation report:
  - `tailored_resumes/reports/Obaida_Kandakji_<Company>.validation_report.md`
- Non-negotiable lint report:
  - `tailored_resumes/reports/Obaida_Kandakji_<Company>.nonnegotiable_lint.md`
- Optional tailored resume PDF:
  - `tailored_resumes/Obaida_Kandakji_<Company>.pdf`
- Cover letter text:
  - `cover_letters/text/Obaida_Kandakji_<Company>.cover_letter.md`
- Optional cover letter PDF:
  - `cover_letters/pdf/Obaida_Kandakji_<Company>.cover_letter.pdf`

Generated outputs in `job_descriptions/`, `tailored_resumes/`, and `cover_letters/` are gitignored by default (local-only).

## Role Files

- Resume editor: `agent_roles/resume_editor.md`
- Resume validator: `agent_roles/resume_validator.md`
- Cover letter writer: `agent_roles/cover_letter_writer.md`
