---
name: delegate-work-in-stages
description: Delegate an approved implementation stage to one or more Codex subagents while keeping the main chat available for discussion, then bring completed work back as a conversational checkpoint before starting another stage. Use only when explicitly invoked for staged background implementation. Do not use for ordinary implementation, autonomous multi-stage execution, or parallel edits with uncertain file ownership.
---

# Delegate Work in Stages

First read and apply the baseline contract in
[coordinate-subagent-work](../coordinate-subagent-work/SKILL.md). This skill adds staged
authorization and conversational checkpoints. It owns stage boundaries and conversation behavior
when its rules are more specific than the baseline.

Coordinate implementation as a sequence of user-approved stages while keeping the main chat
available for discussion.

## Define the current stage

Treat the user's explicit request as authorization for the current implementation stage only.
Before delegating, determine:

- the outcome and completion criteria;
- the validation needed to establish that the stage is complete.

Inspect the workspace for discoverable facts. Ask the user only when an unresolved choice would
materially change the stage, ownership boundary, or intended result.

## Keep the main conversation active

After dispatching the current stage, briefly tell the user what is running and keep the main chat
available for discussion.

Treat new user messages according to their intent:

- answer discussion and design questions in the main chat;
- do not start a newly proposed implementation stage merely because it arose during discussion.

## Complete the authorized stage

When workers finish, use the baseline contract to verify and integrate their work. Follow the
active runtime and repository guidance for proportionate review and non-destructive validation.

Validation, focused fixes, or read-only review needed to complete the already authorized stage may
be delegated under the baseline contract. Do not treat this as authorization for a materially new
feature, refactor, or follow-on stage.

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

When no further stage is needed, provide the integrated final result.

## Boundaries

- Never activate this workflow implicitly.
- Do not run an autonomous chain of implementation stages without conversational checkpoints.
