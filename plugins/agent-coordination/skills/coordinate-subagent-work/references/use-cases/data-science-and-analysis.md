# Data science and analysis

Use these examples to turn an analysis goal into bounded assignments. Apply the launch policy in
[SKILL.md](../../SKILL.md); this guide supplements it with domain examples, not a separate analysis workflow.

## Match the decisions, not the task label

Before choosing a profile, distinguish execution under fixed criteria, choices within an agreed
method, and interpretation that may change the method or next hypothesis. The same task can move
between these levels as its assignment changes. Match descriptions such as "fast and affordable",
"balanced" or "reliable" everyday work, and "complex, demanding work" to the examples below using
the current harness catalog; they are descriptive cues, not fixed model tiers.

| Assignment | Decisions delegated to the worker | Decisions retained by the parent | Suitable description | Evidence to return |
| --- | --- | --- | --- | --- |
| Profile data or produce specified aggregates and plots | Execute the requested checks and flag deviations | Define population, grain, filters, and what differences mean | Fast and affordable | Queries or code, counts, denominators, and anomalies |
| Implement agreed preprocessing or features | Choose implementation details within fixed join, time, and missing-value rules | Decide feature validity, availability at prediction time, and changes to those rules | Balanced coding or reliable everyday work | Changes, grain/cardinality checks, and relevant validation |
| Run a defined training or evaluation plan | Implement and execute fixed splits, metrics, and search bounds | Change the comparison design or decide whether to adopt the result | Reliable everyday work; fast and affordable for execution and result collection alone | Configuration, data/split identifiers, metrics, and failures |
| Investigate a performance drop under an agreed comparison | Choose diagnostics and test candidate causes within the scope | Interpret unresolved competing explanations and choose the next experiment | Balanced or reliable investigation; complex reasoning if ambiguity warrants it | Tested explanations, supporting and contradicting evidence, and remaining uncertainty |
| Critique evaluation design, leakage, or a causal claim | Examine assumptions and develop counterexamples within the assigned question | Integrate the critique with domain constraints and make the final decision | Complex, demanding work when the critique requires broad judgment | Assumptions, concrete failure mechanisms, and evidence that would distinguish explanations |
| Synthesize results and propose the next hypothesis | Compare explanations and propose discriminating experiments, if explicitly delegated | Own the final interpretation and research direction | Complex, demanding work; often keep this with the parent that holds the history | Alternatives, limitations, and rationale for proposed experiments |

## Keep analysis validity in the assignment

Do not equate code execution or passing tests with a valid analytical conclusion. For narrow
assignments, specify the analytical choices needed to make the result interpretable, such as the
population, denominator, split, or metric. If those choices are unresolved and the worker must
decide them, treat the assignment as broader judgment instead of calling it mechanical work.

Separate computation time from decision latitude. A long training run under fixed settings does
not itself need a stronger reasoning profile. A small table can require broad judgment when the
question is whether an observed relationship supports an explanation or decision.

## Example: the same EDA request at different scopes

- **Narrow:** Compute missing rates and target distributions by month using specified filters;
  return code, denominators, and plots. The parent interprets changes.
- **Bounded:** Investigate a specified distribution shift, choosing useful diagnostics and
  reporting supported explanations. The parent decides whether to change the evaluation plan.
- **Broad:** Decide whether the shift undermines the current conclusions and propose a new
  hypothesis or evaluation design. Keep this with the parent or assign a profile suited to the
  required reasoning, with the relevant experiment history.

Narrow an assignment when the parent can supply meaningful criteria without duplicating the
worker's reasoning. Do not split tightly coupled interpretation merely to fit a lighter profile.
