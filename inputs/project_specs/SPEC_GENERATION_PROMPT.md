# Prompt To Generate A Project Spec In Another Repo

Use this in a Codex chat opened inside the target project repository:

```text
Analyze this repository and generate a project spec using the exact structure from TEMPLATE.md below.
Rules:
- Only include claims supported by repository code/docs.
- Mark uncertain metrics as UNVERIFIED.
- Add a strict "Do Not Claim" section.
- Provide 4-8 truthful ATS-friendly bullet variants.

<paste TEMPLATE.md content here>
```

Then copy the generated spec into this repo under:

- `inputs/project_specs/<project_name>.md`
