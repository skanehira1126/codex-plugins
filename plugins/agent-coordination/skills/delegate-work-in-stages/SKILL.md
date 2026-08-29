---
name: delegate-work-in-stages
description: Delegate an approved implementation stage to one or more Codex subagents while keeping the main chat available for discussion, then bring completed work back as a conversational checkpoint before starting another stage. Use only when explicitly invoked for staged background implementation. Do not use for ordinary implementation, autonomous multi-stage execution, or parallel edits with uncertain file ownership.
---

# Delegate Work in Stages

Coordinate implementation as a sequence of user-approved stages. Keep the main agent responsible
for the conversation, task boundaries, and final quality while subagents perform bounded work.

## Define the current stage

Treat the user's explicit request as authorization for the current implementation stage only.
Before delegating, determine:

- the outcome and completion criteria;
- the files or components each worker may change;
- the files or components each worker must leave alone;
- the validation needed to establish that the stage is complete.

Inspect the workspace for discoverable facts. Ask the user only when an unresolved choice would
materially change the stage, ownership boundary, or intended result.

## Choose workers conservatively

Use one worker by default. Use multiple workers only when their tasks are independently useful and
there is high confidence that their writes cannot overlap. Read-only exploration, review, and test
diagnosis may run alongside a writer when they do not alter the writer's files or generated output.

Do not split tightly coupled work merely to increase parallelism. If ownership is unclear, files
are shared, generated outputs may collide, or one task depends on another's edits, use one worker
or run the tasks sequentially.

For every worker, provide a bounded task that includes its outcome, allowed and forbidden scope,
relevant context, validation expectations, and the concise result it must return. Assume local
subagents may share the workspace unless the runtime explicitly isolates them. The main agent must
not edit worker-owned files while that worker is active.

## Keep the main conversation active

After dispatching the current stage, briefly tell the user what is running and keep the main chat
available for discussion. Do not occupy the conversation with repeated polling or raw worker logs.

Treat new user messages according to their intent:

- answer discussion and design questions in the main chat;
- route additive implementation constraints to the affected worker;
- steer or interrupt work when the user replaces the active direction;
- do not start a newly proposed implementation stage merely because it arose during discussion.

When useful, continue independent analysis in the main agent, but preserve worker file ownership.

## Complete the authorized stage

When workers finish, inspect their summaries and the actual workspace state. Follow the active
runtime and repository guidance for proportionate review and non-destructive validation. The main
agent remains accountable for the integrated result and must not report a worker's claim as
verified without checking the evidence that matters.

Validation, focused fixes, or read-only review needed to complete the already authorized stage may
be delegated to a fresh worker. Keep the same ownership rules. Do not treat this as authorization
for a materially new feature, refactor, or follow-on stage.

## Insert a conversational checkpoint

At a natural boundary, place a concise checkpoint into the main conversation containing:

- what completed and the validation result;
- any finding that changes the current discussion or next decision;
- one concrete proposed next stage, when useful.

Do not require every worker to finish before surfacing a checkpoint when one completed workstream
creates a material decision or safely enables a next step. Keep other independent work running,
but avoid interrupting the conversation for routine partial completions.

Ask for approval in ordinary conversation before delegating the proposed next stage. While waiting,
continue discussing alternatives with the user. Start the next stage only after the user clearly
approves it, then repeat this workflow.

When no further stage is needed, provide the integrated final result and close or stop any agents
that no longer have work.

## Boundaries

- Never activate this workflow implicitly.
- Do not create a separate user-owned Codex task unless the user explicitly asks for one.
- Do not run an autonomous chain of implementation stages without conversational checkpoints.
- Do not allow concurrent writes to the same files or shared generated artifacts.
- Do not broaden permissions, destructive actions, external writes, or project scope through
  delegation.
