---
name: evaluate-skill-robustness
description: Evaluate a Codex skill or plugin workflow across explicitly approved subagent model and reasoning-effort profiles, identify model-capability dependence, and report the minimum reliable profile. Use only when the user explicitly invokes this skill while developing or reviewing a SKILL.md or plugin workflow. Do not use for general model benchmarking, API performance or pricing comparisons, or selecting the parent chat model.
---

# Evaluate Skill Robustness

Act as an orchestrator. Design controlled trials, delegate each trial to a fresh subagent, and
compare the returned evidence. Do not solve the target workflow yourself or modify the target
skill/plugin during evaluation.

## Require explicit consent

Treat this as a high-cost workflow. Never launch it implicitly.

Before running evaluation trials or spawning any subagent:

1. Read the target and its required resources without modifying them, and inspect the currently
   available subagent profiles.
2. Prepare a proposed level or custom matrix with profiles, case outlines, maximum subagent runs,
   and the reason it fits the target, so the approval concerns a concrete evaluation scope.
3. Request authorization for that matrix, linking this skill's consent rule, and wait for approval.

Use explicit authorization from this invocation or earlier in the conversation for the same
evaluation matrix without asking again. A level name alone does not authorize execution or
additional runs. Never infer consent from token availability, an approaching reset, or a different
evaluation. The user may cancel or lower the level at any time.

| Level | Profiles | Cases | Repeats | Maximum runs | Intended use |
| --- | ---: | ---: | ---: | ---: | --- |
| Smoke | 2 | 2 | 1 | 4 | Fast regression check |
| Standard | 3 | 3 | 1 | 9 | Default model-sensitivity check |
| Deep | 4 | 4 | 2 | 32 | Variance and capability-floor investigation |
| Custom | User-defined | User-defined | User-defined | User-approved cap | Targeted matrix |

Do not exceed the approved maximum. If the available profiles or required cases would change the
plan, reduce the matrix or ask for new approval before spawning.

## Build the evaluation plan

After consent:

1. Confirm the scoped target and approved matrix. Preserve the target unchanged. Record
   pre-existing worktree changes and avoid treating them as evaluation output.
2. Derive representative cases from the target's declared scope:
   - a typical positive request;
   - an important edge or failure case;
   - a second positive or boundary case for Standard and above;
   - an additional high-risk case for Deep.
3. Separate execution robustness from trigger-boundary review. Explicitly invoking the target in a
   trial proves execution behavior, not implicit trigger quality. Mark unobserved trigger behavior
   as `not evaluated`.
4. Define observable acceptance criteria before starting trials. Prefer deterministic validators,
   file checks, and target-defined completion conditions over stylistic judgment.
5. Read [evaluation-rubric.md](references/evaluation-rubric.md) before scoring results.

## Select profiles from current capabilities

Use only models and reasoning efforts exposed by the current subagent spawning capability. Do not
invent model names, assume that a named model is available, or silently substitute an unsupported
combination.

Choose distinct representative profiles in this order:

1. cost-efficient: the lowest suitable available model/effort combination;
2. balanced: a general-purpose model with medium reasoning when available;
3. strong: the strongest suitable available model with high reasoning when available;
4. stress: a distinct highest-effort or alternate-model combination for Deep.

Use available tool metadata or configured custom-agent metadata to justify the ordering. If the
relative capability is unknown, ask the user to choose the profiles. Skip unavailable profiles and
report the reduced matrix; never replace them without disclosure.

## Run isolated trials

Create one bounded subagent task per profile, case, and repeat. Run independent trials in parallel
up to the current concurrency limit, then continue in waves.

For every trial:

- start with fresh context; when the spawning interface supports it, use no inherited turns;
- pass the target skill path or explicit target invocation, the raw task, necessary input
  artifacts, and the expected output location;
- set the selected model and reasoning effort explicitly when supported;
- omit intended answers, suspected defects, results from other profiles, and the scoring rubric;
- require the subagent to return its result plus concise evidence of validation;
- prohibit edits to the target skill/plugin;
- use a unique temporary output directory when the workflow creates files so trials cannot read or
  overwrite one another;
- preserve the parent's sandbox and approval boundaries; stop and report any blocked trial rather
  than weakening them.

Wait for all started trials. Do not let a stronger-profile result steer a trial that has not yet
started. Keep raw outputs associated with their exact profile, case, and repeat.

## Evaluate without hiding uncertainty

Score and classify every trial with the shared rubric. Apply its failure-attribution and
capability-floor rules, report competing explanations, and narrow the claim or report that no
reliable floor was established when the evidence cannot isolate the cause or establish a stable
minimum profile.

## Report and stop

Match the user's language and any active higher-level instruction. Include:

- approved level and actual run count;
- tested and skipped model/reasoning profiles;
- case-by-profile outcome table;
- concrete failures with evidence;
- model-dependent behaviors and alternative explanations;
- lowest profile supported by the evidence, or that no reliable floor was established;
- proposed skill improvements, separated from model-selection advice;
- untested areas and confidence limits.

End evaluation after the approved trials and report. Hand off separately authorized revisions
without editing the target during evaluation; further trials require a new evaluation budget.
