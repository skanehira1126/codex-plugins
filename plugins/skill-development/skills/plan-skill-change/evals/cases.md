# Regression cases for `plan-skill-change`

## Evidence is sufficient

Request: "Should this workflow become a new skill or extend one we already have?"

- Inspect plausible skills and return a decision brief without questions when the evidence is
  sufficient.
- Do not ask the user what the catalog or checked-in instructions already establish.

## User choices remain

Request: "Help me decide how to package a reusable approval workflow. Interview me if needed."

- Ask only choices needed for the decision brief, in dependency order and at most three per round.
- Give a recommendation and brief rationale for each question.
- Do not ask placement questions before scope is known or elicit implementation details owned by
  `skill-creator`.
