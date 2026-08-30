# Evaluation Rubric

Use this rubric to compare trials without rewarding verbosity or polish.

## Trial record

Record the following for every trial:

- case identifier and raw request;
- model and reasoning effort;
- repeat number;
- result: `pass`, `partial`, `fail`, or `blocked`;
- produced artifact or response location;
- validation evidence;
- observed failure class;
- notes needed to reproduce the result.

Use `blocked` only when the environment, permissions, unavailable tools, or unsupported model
configuration prevented a meaningful trial. Do not score a blocked trial as a model failure.

## Evaluation dimensions

Evaluate each applicable dimension as `pass`, `partial`, `fail`, or `not evaluated`.

1. Instruction adherence
   - Follow the target workflow's required sequence and constraints.
   - Avoid unrequested work and prohibited actions.
2. Task correctness
   - Meet the case-specific acceptance criteria.
   - Produce internally consistent answers or valid artifacts.
3. Completion
   - Reach the target workflow's declared completion condition.
   - Surface blockers instead of claiming success prematurely.
4. Validation quality
   - Run the required checks and connect evidence to conclusions.
   - Do not substitute confident prose for verification.
5. Scope and safety
   - Preserve unrelated files and existing user changes.
   - Stay within the inherited sandbox, approvals, and target scope.
6. Trigger boundary
   - Score only when the trial actually exercised implicit or explicit selection behavior.
   - Mark as `not evaluated` when the target was supplied directly by path or explicit invocation.

## Capability-floor rule

A profile qualifies as the observed minimum reliable profile only when:

- every required case passes all mandatory acceptance criteria;
- no result depends on leaked context or another profile's output;
- no trial at that profile is blocked;
- repeated runs agree when the selected level includes repeats.

When these conditions are not met, report that no reliable floor was established or describe the
narrower claim that the evidence supports. Never extrapolate beyond the tested cases.

## Failure attribution

Use the smallest supported explanation:

- **Skill underspecification:** multiple profiles fail at the same ambiguous or missing instruction.
- **Model-capability sensitivity:** lower profiles fail consistently while higher profiles succeed
  under identical inputs and environment.
- **Environment/tool/permission:** the trial cannot access a required capability or approval.
- **Fixture problem:** inputs, validators, or isolation are invalid or inconsistent.
- **Stochastic/inconclusive:** repeats disagree or evidence is too sparse to separate causes.

Report competing explanations when the evidence does not isolate one cause.

## Summary table

Use one row per profile and case:

| Profile | Case | Repeat | Result | Key evidence | Failure class |
| --- | --- | ---: | --- | --- | --- |

Follow the table with concrete findings, the observed capability floor, proposed instruction
improvements, and explicit limitations.
