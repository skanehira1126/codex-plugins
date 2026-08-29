# Regression cases for `shape-skill-change`

## Planning evidence is sufficient

Request: "Should this workflow become a new skill or extend one we already have?"

- Read only the planning reference.
- Inspect plausible skills and return a decision brief without questions when the evidence is
  sufficient.
- Do not ask the user what the catalog or checked-in instructions already establish.

## Planning choices remain

Request: "Help me decide how to package a reusable approval workflow. Interview me if needed."

- Ask only choices needed for the decision brief, in dependency order and at most three per round.
- Give a recommendation and brief rationale for each question.
- Do not ask placement questions before scope is known or elicit implementation details owned by
  `skill-creator`.

## Review finds no material bloat

Request: "Review the implemented changes to this skill for scope drift and bloat."

- Read only the review reference and compare the implementation with its intended contract and
  plausible neighboring skills.
- Return `coherent` without inventing findings when every instruction and resource has a current,
  distinct purpose.
- Do not use line count alone or launch model-profile evaluation.

## Review finds accumulated instructions

Request: "This skill grew after several fixes. Tell me what should stay and what should change."

- Classify material findings as `keep`, `move`, `merge`, or `remove` and give one overall verdict.
- Distinguish shared entrypoint guidance from conditional details that belong in references.
- Preserve non-obvious constraints and current callers instead of optimizing for the smallest file.

## Plan, implement, then review

Request: "Decide how this workflow belongs in our skills, implement it, and make sure the result did not bloat the skill."

- Plan first, hand the supported decision to `skill-creator`, then review the resulting files.
- Apply only revisions covered by the implementation request and stop after one coherent review
  cycle or when a material user decision remains.
- Keep `evaluate-skill-robustness` out of the workflow unless the user explicitly invokes it.
