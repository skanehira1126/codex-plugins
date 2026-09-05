---
name: presentation-architect
description: "Design, create, structurally review, or revise slide-based presentations when the final artifact is PowerPoint, Google Slides, Keynote, or another deck. Use for argument, learning, or update storylines, pacing, one-message slides, core/notes/appendix/omit triage, and visual-semantic hierarchy. Do not use for prose-first output or formatting-only edits without structural review; use text-document-architect for prose-first documents."
---

# Presentation Architect

Create slide decks that move an audience through a time-bounded sequence toward a decision,
understanding, learning outcome, alignment, or intervention. Design the main deck as the essential
presentation path and use the appendix only when a query-driven branch helps Q&A or verification.

Route by the **target artifact**, not the source material. If the requested output is prose-first, do not use this skill even when the source is a deck. Match the user's language; default to Japanese for Japanese requests.

## Operating model

```text
audience task
  -> ordered cognitive moves
  -> governing message or objective
  -> intended audience outcome

main deck = sequence everyone must experience
speaker notes = nuance better heard than seen
appendix = material retrieved when a question arises
omit = material with no earned role
```

A presentation is not a long document cut into rectangles. It must manage attention, presentation time, spoken delivery, visual form, and optional depth.

## Select the operating mode

Infer the mode from the request:

- **design**: create the presentation brief, content triage, core storyline, storyboard, and any useful retrieval branch.
- **create**: design first, then produce the requested slide deck or complete slide specification, repairing hard-gate failures before delivery.
- **review**: diagnose and report on an existing deck without modifying the deck, notes, sources, or supporting files.
- **revise**: diagnose and then revise, including moving material among core slides, notes, appendix, and omission, repairing hard-gate failures before delivery.

When the request is simply “発表資料を作って” or “create a deck,” use **create**: pass the design and triage gates, then produce and verify the deck. Pause for design approval only when the user requested that checkpoint.

When **revise** applies self-review or external feedback, also use
`revision-hygiene:revision-hygiene` when available to decide which verification or explanation
should persist. This skill remains authoritative for presentation structure and quality.

## Select the structural profile

The operating mode controls whether to design, create, review, or revise. Separately, read
`references/presentation-patterns.md` and select the structural profile by the audience's task:

- **argument-led** for decisions, proposals, analytical findings, and strategy;
- **learning-led** for training and explanation;
- **update-led** for status reporting and intervention.

Use the selected pattern's progression, not a universal executive storyline. Do not invent a
recommendation, tension, exact ask, or Q&A branch when the audience instead needs to learn a model,
understand a change, align on status, or locate the next action.

## Core workflow

### 1. Inspect sources, constraints, and the real deck

Read supplied source material before drafting. Identify:

- audience, prior knowledge, incentives, objections, and decision authority;
- delivery mode: live presentation, slide-based read-ahead, or hybrid;
- presenter role and expected interaction;
- meeting objective, audience task, intended outcome, duration, applicable interaction or Q&A, and page constraints;
- required data, citations, templates, brand rules, and existing notes;
- whether the deck must remain editable.

For an existing deck, inspect the actual slides and speaker notes. For current or external claims, verify them. Never invent evidence, quotations, citations, numbers, or organizational context.

### 2. Resolve material decisions and build the presentation brief

In design and create modes, establish source- or research-backed facts yourself, state safe
defaults for non-material gaps, and ask only user choices that could materially change the deck.

When the user explicitly asks to be interviewed or grilled, read and follow
`../../references/authoring-interview.md` before finalizing the storyboard or full deck.

Use `assets/presentation-brief.md`. Establish or infer:

- audience state A and desired state B;
- intended outcome: decision, belief, understanding, learning, alignment, support, or action;
- one governing message or objective;
- a real tension, question, changed condition, or learning need when it helps the selected profile;
- delivery mode and time budget;
- the smallest sufficient set of supporting claims, learning beats, or update signals and their evidence or examples;
- likely objections, misconceptions, questions, risks, blockers, or alternative options as relevant;
- visual, brand, and artifact constraints.

For decision decks, show the recommendation early. The open question should usually be **why the audience should accept it**, not **what the recommendation is**. For learning-led and update-led decks, do not add a recommendation or suspense unless the content genuinely requires one.

When the deck makes claims, classify them as **Fact**, **Interpretation**, **Hypothesis**, or
**Proposal**. Read `references/evidence-and-sources.md` when research or quantitative evidence is
involved.

### 3. Choose a presentation pattern

Use the selected profile and choose the matching pattern by what the audience must do: decide,
accept a proposal, understand an analysis, learn a model, align on strategy, or intervene in
progress.

Do not default mechanically to “agenda -> background -> issues -> solution -> summary.” A generic agenda does not create a reason to listen.

### 4. Build the profile-specific content map

Use the map that matches the selected profile:

```text
argument-led: claim -> decisive evidence -> reasoning -> implication -> objection/question
learning-led: objective -> example -> model -> guided application -> misconception -> next use
update-led: objective -> changed signal -> evidence -> blocker/risk -> owner/support -> checkpoint
```

Use likely audience questions to decide the core sequence and, only when useful, appendix coverage.

### 5. Triage every candidate item before slide writing

Read `references/content-triage-and-appendix.md` and assign every candidate item to the core
deck, speaker notes, appendix, or omit. Keep any limitation, risk, assumption, or missing evidence
that could change the intended outcome or interpretation in the core path. The reference owns the
detailed placement test and appendix rules.

### 6. Build the core storyline and storyboard

Use `assets/storyboard.md`. For each core slide, specify:

- slide ID and placement;
- audience task or question;
- primary cognitive move: **Orient, Tension, Question, Observe, Explain, Reframe, Compare, Decide, Act, or Consolidate**;
- message-bearing title;
- decisive evidence or content;
- semantic visual form;
- speaker beat and transition;
- likely question, support or verification need, and appendix link when relevant;
- time weight.

Run the following gates before visual production.

#### Title-only gate

1. Read only the deck title and core slide titles.
2. Confirm that the governing message or objective, progression, and any applicable exact ask remain understandable.
3. Rewrite topic labels such as “背景,” “課題,” “施策,” “まとめ,” or “Appendix” as messages or specific questions.
4. Remove slides that do not advance the audience from A toward B.

#### Filmstrip gate

View the deck as thumbnails or a storyboard:

- Is there a visible progression rather than a set of equal-weight pages?
- Does each slide have one primary job?
- Does the body support the title in a way appropriate to the selected profile rather than repeat it?
- Does the visual form change when the audience's cognitive task changes?
- Does every slide earn presentation time?

#### Time gate

Allocate time by cognitive weight rather than dividing duration evenly. Account for interaction,
transitions, and the learning, discussion, or decision work appropriate to the profile. If the
sequence does not fit, move detail to the appendix or omit it; do not solve the problem by shrinking
text.

### 7. Design cognitive and visual rhythm

Read `references/cognitive-rhythm-and-pacing.md` and use it to vary audience operations, visual
forms, transitions, and time by meaning. Variation must be semantic rather than decorative, and
must not conceal a conclusion the audience needs.

### 8. Add a retrieval branch only when useful

When a foreseeable question, verification need, or audience-task branch should not interrupt the
core sequence, use `assets/appendix-plan.md` and `references/content-triage-and-appendix.md` to
design an appendix. Otherwise continue without an appendix artifact. The reference owns the Q&A
mapping, navigation, density, and promotion rules.

### 9. Separate the checks that matter

Confirm structure and sequence, support and evidence, visual and delivery choices, and artifact
quality as distinct concerns. Combine these checks for a small deck or separate them for a complex
deck; do not let polished rendering hide a weak storyline or unsupported content.

### 10. Produce and verify the slide artifact

Read `references/artifact-production.md`. When a dedicated format-specific skill such as
`Presentations` is available, use it for template handling, file construction, rendering, and
artifact QA. This skill remains authoritative for storyline, evidence, content placement, pacing,
speaker notes, and appendix design. Resolve any conflict by preserving the user's artifact format
and the format-specific skill's technical production requirements.

Follow the format-specific production and QA procedure. Inspect the rendered or previewed slides
and the full filmstrip before delivery.

### 11. Rehearse and review independently

Run a presenter pass:

- Can the presenter explain why each core slide follows the previous one?
- Can the deck fit the available time without rushing its intended audience outcome?
- Can material questions, when present, be answered quickly from the core deck or appendix?
- Are any core slides present only because the source material contained them?
- Is any critical content supported or explained only in speaker notes or appendix?

Score the deck with `references/quality-rubric.md` and handle hard-gate failures according to the selected operating mode.

When a structured Markdown storyboard is available, optionally run:

```bash
python scripts/lint_deck_outline.py path/to/storyboard.md --mode general --check-sources
```

Use `decision` or `proposal` instead of `general` only when the selected pattern requires an early
recommendation or ask. Use `status` for update-led decks; it does not require an invented decision.

Lint findings are editorial prompts, not proof of quality.

## Output contracts

### Design mode

Return:

1. presentation brief;
2. audience-state transition and governing message or objective;
3. argument, learning, or update map and material support needs;
4. content triage: core / notes / appendix / omit;
5. title-only core storyline and storyboard;
6. appendix plan and retrieval coverage when an appendix is useful;
7. hard-gate results.

Do not generate the final deck unless requested.

### Create mode

Deliver the requested deck or complete slide specification, including speaker notes and appendix when useful. Mention only material assumptions, unresolved evidence gaps, and verification risks.

### Review mode

Use `assets/review-report.md` when a structured review artifact is useful.

Return prioritized findings with slide location, audience impact, structural cause, and concrete
fix. When the current structure needs revision, include:

- revised title-only storyline;
- a move table for slides whose placement should change;
- appendix, retrieval, or support gaps when relevant to the selected profile.

### Revise mode

Deliver the revised deck and a concise change summary, including slide moves and appendix additions when applicable. Preserve valid sources, notes, brand rules, and editable structure.

## Reference map

- `references/quality-rubric.md`: scoring, hard gates, and review severity.
- `references/presentation-patterns.md`: core sequences by audience task.
- `references/cognitive-rhythm-and-pacing.md`: audience moves, visual rhythm, transitions, and time.
- `references/content-triage-and-appendix.md`: core, notes, appendix, omit, and Q&A design.
- `references/evidence-and-sources.md`: claim types, source handling, and quantitative evidence.
- `references/examples.md`: before-and-after slide and appendix examples.
- `references/artifact-production.md`: slide generation, notes, rendering, and filmstrip QA.
- `evals/cases.md`: regression prompts for maintainers.
