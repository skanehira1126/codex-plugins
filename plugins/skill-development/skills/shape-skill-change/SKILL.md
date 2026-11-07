---
name: shape-skill-change
description: Plan or review Codex skills and plugin workflows for scope, concise instructions, and maintainability. Use when deciding whether to create, update, extend, split, or avoid a skill, or auditing existing skills for duplication and bloat. Excludes mechanical edits with no boundary question and cross-model robustness testing.
---

# Shape Skill Change

Keep a Codex skill change coherent before and after implementation. This workflow plans or reviews
the change; it does not edit skill files by itself.

## Route the request

- **Before implementation:** read [planning.md](references/planning.md) and produce a decision brief.
- **Existing skill or implemented change:** read [review.md](references/review.md).
- **Both:** plan first; when implementation is requested, continue with `skill-creator` and then
  review without another planning approval. Planning and review alone do not authorize edits.

Read only the reference needed for the current phase. Do not run `evaluate-skill-robustness`
unless the user explicitly invokes that separate, high-cost workflow.

## Use one boundary model

Inspect the full `SKILL.md` of the target and every plausible neighboring skill before deciding.
Search additional discoverable skill locations only when the available catalog is incomplete or
the user points to another location.

Compare the proposal or implementation using:

- user goal and trigger conditions;
- negative trigger conditions;
- expected inputs;
- workflow steps and dependencies;
- output and success criteria;
- scope, ownership, and intended audience.

Aim for the shortest instructions that preserve the workflow. For each section, identify the
decision, action, or output that would worsen if it were removed. Keep non-obvious constraints;
remove generic advice and repetition; load conditional detail only when needed. Use file length
as a diagnostic, not a quality target. A short self-contained skill needs no extra routing layer.

Match instruction structure to the relationship being expressed:

- Numbered lists for steps whose order matters.
- Bullets for independently checked rules, conditions, or alternatives.
- Tables for comparisons or mappings with shared axes.
- Short paragraphs for purpose, rationale, and connected explanation.

Separate independently actionable instructions buried in a paragraph. Keep conditions and
exceptions attached to the instruction they qualify; do not fragment connected reasoning or add
numbering that implies an order the task does not require.

When information is missing:

- Inspect available facts and infer safe defaults that cannot change the boundary, placement, or
  review verdict.
- Ask only unresolved user choices needed for the current result, in dependency order and at most
  three independent, high-impact questions per round.
- Give a recommended answer and brief rationale for each question.

## Complete the requested scope

- Planning ends when the decision brief is supportable.
- Review ends when every material finding has a disposition and the next handoff is clear.
- A combined implementation request ends when material findings are resolved; recheck findings
  affected by further edits. Pause only work that depends on an unresolved user decision.
