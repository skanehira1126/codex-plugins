---
name: shape-skill-change
description: Shape Codex skill changes before and after implementation by choosing the right skill boundary and reviewing the result for scope drift, duplication, and bloat. Use when deciding whether to create, update, extend, split, or avoid a skill, or when reviewing an implemented skill change for maintainability. Do not use for an exact routine edit with no boundary question or for cross-model robustness testing.
---

# Shape Skill Change

Keep a Codex skill change coherent before and after implementation. This workflow plans or reviews
the change; it does not edit skill files by itself.

## Route the request

- **Before implementation:** read [planning.md](references/planning.md) and produce a decision brief.
- **After implementation:** read [review.md](references/review.md) and review the implemented change.
- **Both:** plan first, use the decision brief with `skill-creator`, then review the resulting
  implementation. Apply further edits only when the user requested implementation.

Read only the reference needed for the current phase. Do not run `evaluate-skill-robustness`
unless the user explicitly invokes that separate, high-cost workflow.

## Use one boundary model

Inspect the full `SKILL.md` of the target and every plausible neighboring skill before deciding.
Search additional discoverable skill locations only when the available catalog is incomplete or
the user points to another location.

Compare the proposal or implementation using:

1. user goal and trigger conditions;
2. negative trigger conditions;
3. expected inputs;
4. workflow steps and dependencies;
5. output and success criteria;
6. scope, ownership, and intended audience.

Treat bloat as material that no longer changes decisions, protects a real constraint, or improves
repeatable work. Do not use file length alone as evidence. Prefer one coherent workflow over a
smaller diff, but do not expand a skill into a collection of loosely related tasks.

Inspect facts instead of asking the user. Infer safe defaults that cannot change the boundary,
placement, or review verdict. Ask only unresolved user choices needed for the current result, in
dependency order and at most three independent, high-impact questions per round. Give a
recommended answer and brief rationale for each question.

## Stop at the phase boundary

- Planning ends when the decision brief is supportable.
- Review ends when every material finding has a disposition and the next handoff is clear.
- A combined implementation request ends after the implemented result passes one review cycle or
  remaining tradeoffs require a user decision.
