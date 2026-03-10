# Quantification Rules

## Purpose

Use numbers to make bullets more concrete, but never invent performance or business impact.
If a number cannot be defended in an interview, it should not appear in the resume.

## Why This Matters

- Good quantification improves scan speed and credibility.
- Bad quantification damages trust immediately.
- For early-career resumes, exact scope counts are often stronger than fake percentages.

## Quantification Priority Order

Use this order when editing bullets:

1. Measured outcomes
   - accuracy improvement
   - noise reduction
   - latency reduction
   - throughput increase
   - error-rate change
   - time saved
   - cost saved
   - user growth

2. Exact scope counts
   - number of services
   - number of components
   - number of deployments
   - number of users or user groups
   - number of joints tracked
   - number of cars simulated
   - team size
   - years of experience
   - time-window size

3. Defensible derived estimates
   - only if the math is simple and traceable to project evidence
   - example: `~30 readings per 5-minute window` from one event every 10 seconds
   - use approximate wording such as `about`, `approximately`, or `~`

4. Qualitative but concrete scope
   - if no number is available, use specific system scope rather than vague claims
   - example: `centralized operator interface`, `real-time diagnostic display`, `event-driven workflow`

## Hard Rules

- Never invent percentage improvements.
- Never invent time savings.
- Never invent revenue, productivity, or efficiency gains.
- Never turn a subjective improvement into a numeric claim.
- Never disguise a guess as a measurement.
- Never add a number only because recruiters like metrics.

## Allowed Uses

- A measured metric already present in the source resume or project spec.
- A verified scope count from the source resume or project spec.
- A user-confirmed estimate recorded under `Quantification Candidates` in the project spec.
- A simple derived estimate only if:
  - the source is documented in the project spec
  - the math is obvious
  - approximate wording is used when needed

## Not Allowed For Resume Use

- Any item placed under a project spec section such as `Potential Metrics To Verify`.
- Brainstormed ranges, hypotheses, or before/after estimates that have not been confirmed by the user.
- "Educated guesses" about efficiency, delay reduction, productivity, or error reduction unless they are promoted into a verified section later.

## Best Practice For Early-Career Bullets

If there is no real impact metric, prefer this pattern:

- action + exact scope count + technical context

Examples:

- `deployed 5 services to AKS`
- `tracked 15 body joints in real time`
- `simulated 100 cars per generation`
- `built in a team of 7`

These are stronger than fake claims such as:

- `improved efficiency by 40%`
- `boosted productivity by 50%`
- `reduced delays by 60%`

unless those numbers are actually measured and documented.

## Editing Guidance

- Preserve existing valid metrics already on the resume.
- If a bullet has no defensible metric, add a scope count only when supported by evidence.
- Approved `Quantification Candidates` may be used in actual resume bullets when they materially improve clarity and fit.
- Prefer one strong number per bullet.
- If a percentage is used, place it near the result clause, not buried in a long sentence.
- Keep the phrasing short and plain:
  - `reduced`
  - `improved`
  - `cut`
  - `sped up`
  - `automated`
- Avoid awkward metric stuffing or stacking multiple percentages in one bullet.
- If the quantified version sounds forced, skip the number and keep the bullet cleaner.
- Do not force a number into every bullet.
- One strong quantified bullet is better than three suspicious ones.

## Natural Phrasing Examples

- `Reduced duplicate section seating mistakes by ~93% by replacing verbal handoffs with a centralized workflow tool.`
- `Cut manual deployment effort by ~90% by automating build and rollout steps across 5 services.`
- `Improved seating throughput by ~8% during rush periods by surfacing table readiness in one place.`
- `Reduced form-correction time by ~13% with immediate posture feedback.`

These are better than:

- `Leveraged a centralized workflow optimization paradigm to achieve a 93% improvement in operational coordination accuracy.`
- `Drove a substantial 90% efficiency gain through implementation of an automated deployment solution.`

## Validation Rules

A quantified bullet should fail review if:

- the number has no source in the resume or project spec
- the number overstates impact beyond the evidence
- a derived estimate is presented as exact
- a percentage is used where only qualitative evidence exists
- the bullet sounds bloated, overly polished, or unnaturally metric-heavy
