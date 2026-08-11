---
name: plan-skill-change
description: Inspect available skills and decide whether a requested workflow should create a new skill, update or extend an existing skill, split an existing skill, or not use a skill. Use before skill-creator when skill boundaries, ownership, placement, or overlap are uncertain, or when the user asks whether to create a skill or add to an existing one. Do not use when the exact target skill and requested edit are already explicit.
---

# Plan Skill Change

Decide the appropriate skill change before implementation. Produce a decision brief for
`skill-creator`; do not create or edit skill files as part of this workflow.

## Workflow

### 1. Describe the proposed workflow

Extract or infer:

- the recognizable user goal;
- representative prompts that should trigger the workflow;
- nearby prompts that should not trigger it;
- expected inputs, major steps, and output;
- the success criteria;
- required tools, references, scripts, or assets;
- whether the workflow is repo-specific, personal, organizational, or distributable.

Ask one focused question only when a missing answer would materially change the decision.

### 2. Inspect existing skills

Use the available skill catalog and paths to identify plausible candidates. Inspect the full
`SKILL.md` of each plausible candidate before deciding. Search additional discoverable skill
locations only when the catalog is incomplete or the user points to another location.

Consider repo, user, admin, system, and installed-plugin skills. Do not assume that skills with
similar names have the same workflow, and do not treat vocabulary overlap alone as evidence of
duplication.

### 3. Compare workflow boundaries

Compare the proposal with each candidate using:

1. user goal and trigger conditions;
2. negative trigger conditions;
3. expected inputs;
4. workflow steps and dependencies;
5. output and success criteria;
6. scope, ownership, and intended audience.

Prefer a coherent existing workflow over a smaller diff. Avoid expanding a skill until its
description becomes a loose collection of related topics.

### 4. Choose one decision

Choose exactly one primary decision:

- **update-existing**: Use when the proposal has the same user goal, trigger boundary, and success
  criteria as an existing skill and changes its core instructions.
- **extend-existing-resources**: Use when the workflow remains unchanged and only supporting
  knowledge, examples, scripts, templates, or assets are needed.
- **split-existing**: Use when an existing skill contains workflows with materially different
  triggers, inputs, or success criteria. State which responsibility stays in each skill.
- **create-new**: Use when the proposal represents a distinct user goal or success criterion and
  can stand alone as a repeatable workflow.
- **do-not-create**: Use when the request is one-off, already handled reliably by general model
  capability, or belongs in another Codex surface.

For **do-not-create**, recommend the smallest suitable surface: the current prompt for one-off
constraints, `AGENTS.md` for durable repository conventions, Codex configuration for runtime
settings, an MCP server or connector for live data and controlled actions, or a plugin for an
installable bundle of skills and tools.

### 5. Choose placement

Recommend placement independently from the change decision:

- Use repo scope for workflows tied to one repository, its commands, schemas, or conventions.
- Use user scope for personal workflows that should apply across repositories.
- Use a plugin when the capability should be installed or distributed as a bundle, especially
  with connectors or MCP tools.
- Treat system-bundled skills as managed dependencies. Prefer a companion user skill or an
  upstream change over directly modifying a bundled system skill.

When updating an existing skill, preserve its current scope unless there is concrete evidence
that the ownership boundary should move.

### 6. Produce the decision brief

Return the following concise structure:

```markdown
## Decision

- Decision: <update-existing | extend-existing-resources | split-existing | create-new | do-not-create>
- Target: <skill name or none>
- Placement: <repo | user | plugin | other>

## Evidence

- <comparison with the closest existing skill>
- <trigger/input/output/success-criteria evidence>

## Proposed scope

- Include: <responsibilities>
- Exclude: <nearby responsibilities>
- Resources: <scripts/references/assets or none>

## Skill Creator handoff

<A self-contained request for skill-creator, or "No handoff" for do-not-create.>
```

Name the closest rejected candidate and explain the decisive boundary when recommending
**create-new**. Identify the exact target and preserve its unrelated behavior when recommending
an existing-skill change.

If the user also requested implementation, use the decision brief as the input to
`skill-creator` after completing this workflow. Otherwise, stop after the decision brief.
