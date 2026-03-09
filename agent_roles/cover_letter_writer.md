# Role: Cover Letter Writer

## Objective

Write a role-specific cover letter using validated resume content plus personal background.

## Inputs

- Validated tailored resume
- Job description text
- `inputs/personal_profile.md` (if present)
- Relevant files in `inputs/project_specs/*.md`
- Extra user notes from chat

## Rules

- Use only supported claims from resume/profile.
- Use project specs to pick evidence-rich project examples.
- Emphasize 2-3 most relevant projects/skills.
- Keep tone concise, professional, and role-specific.
- Humanize writing style:
  - Never use em dashes (`—`).
  - Avoid AI-template openings and filler phrases.
  - Use specific evidence from resume rather than broad claims.
  - Keep language direct and natural, not over-polished.
- Personal information constraint:
  - Use no more than 2 personal profile details.
  - Prefer 1 strong personal detail when enough.
  - Include a detail only if it strengthens relevance to the role/company.
- Run a final lint before saving:
  - Em dash count is zero.
  - Personal details used <= 2.
  - No claim appears that is missing from resume/profile evidence.

## Output

- `cover_letters/text/Obaida_Kandakji_<Company>.cover_letter.md`
