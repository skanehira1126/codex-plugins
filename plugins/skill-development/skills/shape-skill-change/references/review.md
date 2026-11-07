# Review a Skill or Plugin

Use this workflow for existing skills or implemented changes. Review the current result, not the
history of rejected ideas. For a plugin audit, inspect every skill's entrypoint and metadata, then
follow its resource paths; report which skills need changes and which should remain as they are.

## 1. Recover the intended contract

Use the planning brief when one exists. Otherwise infer the intended goal, trigger boundary,
output, and success criteria from the user's request and the relevant skill files. Inspect the
target's `SKILL.md`, routed references, scripts, assets, UI metadata, sibling skills, and plugin
manifest as needed.

Do not assume every item in a diff is required merely because it was implemented. Preserve the
user's unrelated changes and evaluate only the requested skill change.

## 2. Audit the implementation

Check:

- **Discovery:** The description leads with the intended task and distinguishes likely misroutes;
  detailed procedures stay in the body. Invocation policy and UI prompts agree with this boundary.
- **Boundary coherence:** The skill still owns one recognizable goal and success criterion.
- **Instruction value:** Apply the entrypoint's removal test. Fixed steps and absolute language
  need a concrete correctness, permission, or workflow reason; preserve justified local conventions.
- **Progressive disclosure:** Shared routing stays in `SKILL.md`; conditional detail lives in a
  reference with an explicit load condition. Trace a representative request's reading path; moving
  text into an always-loaded file does not by itself save context.
- **Duplication:** The same rule is not repeated across the entrypoint, references, sibling skills,
  `AGENTS.md`, or plugin metadata.
- **Evidence discipline:** A single failure, preference, or implementation detail has not become a
  universal rule without a demonstrated need.
- **Resource hygiene:** Every reference, script, asset, example, test, and compatibility layer has
  a current caller and a distinct purpose.
- **Handoffs:** Editing, model evaluation, external writes, and other costly actions respect the
  correct request or approval boundary.
  Internal quality gates do not add approval pauses; required approvals identify their scope and
  reuse current consent. A skill-caused pause cites the file and rule, distinguishing its explicit
  requirement from interpretation. Verification ends after relevant risks and required checks pass.

Classify each material finding as either **behavior-preserving consolidation** or
**behavior-changing revision**. When both are in scope, complete and verify the behavior-preserving
consolidation first so trigger, boundary, requirement, and output changes remain independently
reviewable.

## 3. Verify the affected behavior

Choose checks that match the change: intended requests and nearby non-target requests for
description changes; representative inputs, material missing information, and failure paths for
workflow changes. Reuse existing cases and required validators. When the target is
`shape-skill-change`, select applicable cases from [evals/cases.md](../evals/cases.md).

Separate static contract checks from observed runs. A validator proves structure, and a supplied
skill path or explicit invocation exercises execution; neither proves implicit selection. For
before/after runs, record the skill revision, inputs, model/effort, tools, and acceptance criteria;
hold those conditions fixed except for the intended change. Compare outcome and unnecessary work,
using token/time measurements only when available. Report unrun checks and limits; do not infer a
quality or speed gain from fewer lines or launch cross-model evaluation as routine review.

## 4. Give every finding a disposition

Use one of:

- **keep:** It belongs in its current location.
- **move:** It is useful but belongs in another instruction surface or conditional resource.
- **merge:** It duplicates or fragments an existing responsibility and should be consolidated.
- **remove:** It does not change decisions, protect a real contract, or support current execution.

Choose one overall verdict:

- **coherent:** No material change is needed.
- **revise:** The boundary is sound but the implementation needs focused changes.
- **split:** The implementation contains workflows with materially different triggers or success
  criteria.
- **merge:** Another skill already owns the same workflow.
- **retire:** The skill no longer justifies a durable skill surface.

Before assigning `merge` or `remove` to duplicated guidance, name its canonical owner and confirm
that every remaining caller or routing instruction still reaches that owner. Preserve distinct
trigger metadata, routing, and layer-specific invariants rather than treating them as duplicate
detail.

## 5. Report and hand off

Return:

```markdown
## Review

- Verdict: <coherent | revise | split | merge | retire>
- Target: <skill name>
- Compared with: <neighboring skills or none>

## Findings

- <keep | move | merge | remove> [<behavior-preserving | behavior-changing>]: <location, impact,
  specific action, and canonical owner when applicable>

## Preserved contracts

- <important behavior or boundary that must remain>

## Verification

- <checks performed, observed results, and untested behavior>

## Skill Creator handoff

<A self-contained revision request, or "No handoff" when coherent.>
```

Report no finding merely to prove that every disposition was considered. If the user requested
implementation, pass material revisions to `skill-creator` and review the revised result once
more; stop when the verdict is coherent or a remaining user decision blocks safe revision.
