---
name: coordinate-subagent-work
description: Choose subagent models, reasoning effort, and context, then coordinate ownership, validation, and integration when delegation is explicitly requested or already planned independently of this skill. Do not use merely because a task could be parallelized, or for user-owned Codex task management or model-profile evaluation.
---

# Coordinate Subagent Work

Apply this baseline after the user or another workflow requests delegation, or after delegation has
been chosen independently of this skill under the active runtime and user instructions. Loading this
skill is not a reason to start subagents.
Keep the main agent accountable for task scope, integration, validation, and the final result.

## Bound the planned delegation

For planned delegation, require a concrete, bounded subtask that can make independent progress while
the main agent or another worker performs other useful work. Keep the worker count to the minimum
needed; multiple workers need independently useful assignments without unfinished dependencies.

Consider expected speed or quality gains against coordination cost. Do not split tightly coupled
work merely to create parallel activity. If delegation is unavailable, disallowed, or would not
help, continue locally; explain that choice briefly when the user specifically asked for subagents.

## Choose a launch profile

Define which decisions the worker may make and which remain with the parent. Match that latitude
to the harness's current model descriptions and supported efforts, choosing a resource-conscious
profile that meets the acceptance criteria, including likely retries and review work. Respect user
choices; do not hardcode model IDs or infer numerical savings from qualitative descriptions.

Set model and effort explicitly when supported; do not inherit the parent's settings by default.
Use a compact brief containing the necessary instructions, decisions, constraints, and source paths.
With `fork_turns`, prefer `"none"` or limited history; where full-history forks prevent profile
overrides, use the brief to apply the selected profile.

Briefly state the assignment, profile, and selection reason before dispatch without adding an
approval pause. Use a stronger profile for a concrete need in the worker's decisions, not merely
because the overall task is difficult or an input, permission, or environment problem occurred.

When delegating data science or analysis work, read
[Data science and analysis](references/use-cases/data-science-and-analysis.md) for examples of
decision boundaries and suitable model descriptions.

## Assign bounded ownership

Give each worker:

- a concrete outcome and completion criteria;
- the context needed to work independently;
- allowed and forbidden files, components, or actions;
- the validation it should perform;
- the concise evidence or result it should return.

Assume local subagents share the workspace unless the runtime guarantees isolation. Do not allow
concurrent writes to the same files or shared generated artifacts. The main agent must not edit
worker-owned files while that worker is active. When write ownership is uncertain, keep the work
read-only, use one writer, or run workers sequentially.

## Coordinate without noise

Continue useful work in the main agent only when it does not cross a worker's ownership boundary.
Send additive constraints to the affected worker and interrupt work when the user replaces its
direction. Wait for results without repeated polling or exposing raw worker logs as progress.

## Verify and integrate

Inspect the actual workspace state and the evidence that matters before accepting a worker's
claim. Resolve conflicting results and integrate them into one coherent outcome rather than
concatenating summaries. Perform proportionate validation after integration and close or stop
workers that no longer have useful work.

Delegation does not create permission for a new user-owned Codex task, destructive action,
external write, broader project scope, or materially different follow-on work. A specialized
coordination skill may add tighter mode-specific rules; apply those rules within that mode while
preserving this baseline.
