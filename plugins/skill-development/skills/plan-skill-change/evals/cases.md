# Regression cases for `plan-skill-change`

Use these cases to review decision discovery after meaningful changes.

## Facts are inspected, not delegated to the user

Request: "Should this workflow become a new skill or extend one we already have?"

Must:

- inspect the available skill catalog and plausible full `SKILL.md` files;
- determine existing trigger, input, output, and success boundaries from evidence;
- ask the user only about material decisions that the inspected evidence cannot settle.

Failure:

- asks the user which nearby skills exist or what their checked-in instructions say.

## Dependent decisions are asked in frontier order

Request: "Help me decide how to package a reusable approval workflow. Interview me if needed."

Must:

- resolve the intended audience and reusable success criterion before asking repo-versus-plugin
  placement questions that depend on them;
- ask up to the three highest-impact currently unblocked decisions in a concise numbered round;
- provide a recommended answer and rationale for each question;
- recompute the frontier after the user's answers.

Failure:

- asks about placement before the required scope is known;
- dumps speculative implementation questions that belong to `skill-creator`.

## Safe defaults do not trigger an interview

Request: "Add one example to this explicitly named skill; no behavior change."

Must:

- infer `extend-existing-resources` when the inspected target and request support it;
- state any harmless assumption and produce the decision brief without unnecessary questions.

Failure:

- starts a broad interrogation despite having enough evidence for one primary decision.
