---
name: coordinate-subagent-work
description: Coordinate Codex subagents for the current task by deciding when independent delegation adds value, assigning bounded non-overlapping work, and integrating verified results. Use when a task contains independently useful workstreams, another workflow delegates to subagents, or the user asks to use subagents or parallel agents. Do not use for user-owned Codex task management or model-profile evaluation.
---

# Coordinate Subagent Work

Use this as the baseline coordination contract whenever subagents participate in the current task.
Keep the main agent accountable for task scope, integration, validation, and the final result.

## Decide whether delegation helps

Delegate only when at least one concrete, bounded subtask can make independent progress while the
main agent or another worker performs other useful work. Prefer one worker; add workers only for
workstreams that are independently useful and do not depend on one another's unfinished results.

Consider expected speed or quality gains against coordination cost. Do not split tightly coupled
work merely to create parallel activity. If delegation is unavailable, disallowed, or would not
help, continue locally; explain that choice briefly when the user specifically asked for subagents.

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
