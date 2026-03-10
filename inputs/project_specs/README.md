# Project Specs (Source Of Truth)

Use these files to give the resume/cover-letter agents reliable, project-level context.

Why this exists:
- A plain summary is often too vague for safe keyword editing.
- A spec card with evidence is better for preventing fabricated claims.

How to use:
1. Create one spec file per project using `TEMPLATE.md`.
2. For each claim or keyword, include concrete evidence from repo code/docs.
3. Keep `Allowed Keywords` and `Do Not Claim` sections strict.
4. Update specs when project scope changes.

Agent behavior:
- Resume Tailor and Cover Letter Writer should only use project claims that are supported by these specs or current resume text.
- Validator should fail output if unsupported project keywords are introduced.
- If a spec includes `Potential Metrics To Verify`, treat that section as brainstorming only until the user confirms the numbers.
