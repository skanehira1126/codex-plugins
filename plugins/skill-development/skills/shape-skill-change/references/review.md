# Review an Implemented Skill Change

Use this workflow after skill files have been created or changed. Review the current result, not
the history of rejected ideas.

## 1. Recover the intended contract

Use the planning brief when one exists. Otherwise infer the intended goal, trigger boundary,
output, and success criteria from the user's request and the relevant skill files. Inspect the
target's `SKILL.md`, routed references, scripts, assets, UI metadata, sibling skills, and plugin
manifest as needed.

Do not assume every item in a diff is required merely because it was implemented. Preserve the
user's unrelated changes and evaluate only the requested skill change.

## 2. Audit the implementation

Check:

- **Trigger drift:** The description still selects the intended requests and excludes likely
  misroutes.
- **Boundary coherence:** The skill still owns one recognizable goal and success criterion.
- **Instruction value:** Each instruction changes a decision, protects a real constraint, or
  improves repeatable execution; generic advice and speculative edge cases do not accumulate.
- **Progressive disclosure:** Shared routing stays in `SKILL.md`; conditional detail lives in a
  reference that is read only when needed.
- **Duplication:** The same rule is not repeated across the entrypoint, references, sibling skills,
  `AGENTS.md`, or plugin metadata.
- **Evidence discipline:** A single failure, preference, or implementation detail has not become a
  universal rule without a demonstrated need.
- **Resource hygiene:** Every reference, script, asset, example, test, and compatibility layer has
  a current caller and a distinct purpose.
- **Handoffs:** Editing, model evaluation, external writes, and other costly actions remain behind
  the correct request or approval boundary.

Do not optimize for fewer lines. A long non-obvious constraint may be essential, while a short
duplicate or generic instruction may still be bloat.

Classify each material finding as either **behavior-preserving consolidation** or
**behavior-changing revision**. When both are in scope, complete and verify the behavior-preserving
consolidation first so trigger, boundary, requirement, and output changes remain independently
reviewable.

## 3. Give every finding a disposition

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

## 4. Report and hand off

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

## Skill Creator handoff

<A self-contained revision request, or "No handoff" when coherent.>
```

Report no finding merely to prove that every disposition was considered. If the user requested
implementation, pass material revisions to `skill-creator` and review the revised result once
more; stop when the verdict is coherent or a remaining user decision blocks safe revision.
