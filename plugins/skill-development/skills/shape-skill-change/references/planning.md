# Plan a Skill Change

Use this workflow before implementation when the skill boundary, ownership, placement, or overlap
is uncertain.

## 1. Describe the proposed workflow

Extract or infer:

- the recognizable user goal;
- representative prompts that should trigger the workflow;
- nearby prompts that should not trigger it;
- expected inputs, major steps, and output;
- the success criteria;
- required tools, references, scripts, or assets;
- whether the workflow is repo-specific, personal, organizational, or distributable.

For ordinary requests, stop questioning as soon as the decision brief is supportable. If the user
explicitly asks for a thorough interview, continue only until the material planning choices are
resolved; leave implementation details to `skill-creator`.

## 2. Choose one decision

Choose exactly one primary decision:

- **update-existing:** The proposal has the same user goal, trigger boundary, and success criteria
  as an existing skill and changes its core instructions.
- **extend-existing-resources:** The workflow remains unchanged and only supporting knowledge,
  examples, scripts, templates, or assets are needed.
- **split-existing:** An existing skill contains workflows with materially different triggers,
  inputs, or success criteria. State which responsibility stays in each skill.
- **create-new:** The proposal represents a distinct user goal or success criterion and can stand
  alone as a repeatable workflow.
- **do-not-create:** The request is one-off, already handled reliably by general model capability,
  or belongs in another Codex surface.

For **do-not-create**, recommend the smallest suitable surface: the current prompt for one-off
constraints, `AGENTS.md` for durable repository conventions, Codex configuration for runtime
settings, an MCP server or connector for live data and controlled actions, or a plugin for an
installable bundle of skills and tools.

Name the closest rejected candidate and the decisive boundary when recommending **create-new**.
Identify the exact target and preserve unrelated behavior when recommending an existing-skill
change.

## 3. Choose placement

Recommend placement independently from the change decision:

- Use repo scope for workflows tied to one repository, its commands, schemas, or conventions.
- Use user scope for personal workflows that should apply across repositories.
- Use a plugin when the capability should be installed or distributed as a bundle, especially
  with connectors or MCP tools.
- Treat system-bundled skills as managed dependencies. Prefer a companion user skill or an
  upstream change over directly modifying a bundled system skill.

When updating an existing skill, preserve its current scope unless concrete evidence supports
moving the ownership boundary.

## 4. Produce the decision brief

Return:

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

If the user requested implementation, use this brief with `skill-creator`, then run the review
phase on the resulting files.
