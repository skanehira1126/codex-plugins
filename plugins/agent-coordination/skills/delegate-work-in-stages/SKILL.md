---
name: delegate-work-in-stages
description: Delegate implementation to Codex subagents while the main agent handles decisions and parallel discussion. Use only when explicitly invoked to implement a task while continuing the main conversation.
---

# Delegate Work in Stages

First read and apply the baseline contract in
[coordinate-subagent-work](../coordinate-subagent-work/SKILL.md). This skill adds implementation
decision ownership and ongoing discussion to the baseline's delegation, validation, and integration.

## Define the task

Establish the user's goal, agreed scope, constraints, and completion criteria from the request and
conversation. Delegate bounded implementation work while keeping the main agent available to discuss
other aspects of the work.

The main agent chooses internal stages and work assignments. Existing authorization for the task
covers its implementation, validation, and necessary fixes across those stages; an internal stage
boundary does not require renewed user approval.

## Own implementation decisions

The main agent owns decomposition, implementation direction, cross-worker decisions, review, and
integration. Workers may make routine local decisions within their assignment; have them return
questions that affect shared contracts, other assignments, or the task's intended result.

Resolve implementation questions from inspected evidence and the agreed constraints. A worker's
request for guidance is input for the main agent to assess, not an automatic question for the user.

## Keep the main conversation active

After dispatching work, briefly tell the user what is running. Answer discussion and design questions
in the main conversation while implementation continues within the agreed scope.

Treat exploratory ideas as discussion, not implementation instructions. Apply explicit corrections
and new constraints to affected workers. When the user changes direction, revise or stop affected
assignments instead of letting them continue under outdated assumptions.

## Ask at user decision points

Ask only when proceeding requires a change to the agreed goal or scope that the user has not already
authorized, a material choice that cannot be resolved from the user's intent and available evidence,
or a checkpoint the user explicitly requested, such as reviewing a design before implementation.
The baseline's action permissions continue to apply.

Prepare the concrete choice or reviewable result before asking, explain the reason for the pause,
and reuse relevant authorization already given in the conversation. Pause only work that depends on
the answer; continue independent authorized work and discussion while waiting.

## Share results and complete the task

Share a concise update when a verified result or finding materially informs the discussion or a
user decision. Include what completed, relevant validation, and any implication for the task.
An update by itself does not require a reply before work continues.

Use the baseline contract to verify and integrate worker results. Continue the remaining
implementation, review, and necessary fixes until the agreed task completion criteria are met.
An individual worker or internal stage finishing is not completion of the whole task.

Deliver the integrated result with relevant verification and any unresolved limitations.

When testing changes to this workflow, use [evals/cases.md](evals/cases.md) for task completion,
discussion, and user decision boundaries.
