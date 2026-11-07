# Regression cases for `shape-skill-change`

Select cases affected by the change. A walkthrough of these expectations is a static check, not
an observed activation or execution trial; record which kind of evidence was obtained.

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

## Discovery text contains implementation details

Request: "Review a Python design skill whose description lists every helper/class pattern and
repeats the implementation rules from its body."

- Keep the task, abstraction decisions, and exclusion of mechanical formatting clear in the
  description; leave the detailed rules in the body.
- Check requests about a thin wrapper, a stateless class, and a formatter-only change against the
  intended boundary. Do not claim measured activation accuracy from this static comparison.

## Shorter entrypoint with unchanged reading cost

Request: "Move all rules from this 60-line skill into a reference and always read it first."

- Explain that the proposed path still loads all the rules and adds navigation.
- Keep a coherent small skill self-contained unless a real conditional use justifies the split.
- If a template already owns required output fields, reference it from the workflow instead of
  duplicating its field list; verify that the template and its callers preserve the output contract.

## Plugin audit preserves distinct constraints

Request: "Review a plugin containing a normal design skill and an explicitly invoked costly
evaluation skill; simplify their instructions."

- Inspect both entrypoints, invocation policies, metadata, and routed resources.
- Preserve the evaluation skill's consent and run limits; do not propagate those limits into
  ordinary design work or remove them just to shorten the evaluation skill.
- Name the skills that need revisions and those whose current guidance should remain.

## Evaluation evidence has limited scope

Input: A validator passes, one run explicitly uses the skill path, and the revised SKILL.md has
fewer lines. No implicit-selection trial, baseline run, or token/time measurements are available.

Request: "Review whether this proves the shorter skill triggers better and runs faster."

- Accept the structural check and observed execution only for what they establish.
- Mark implicit selection and before/after efficiency as untested; do not infer improvements.
- Identify the revisions and controlled cases needed for comparison without starting an
  unrequested model-profile evaluation.
