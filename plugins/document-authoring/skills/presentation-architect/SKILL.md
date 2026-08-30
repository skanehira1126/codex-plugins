---
name: presentation-architect
description: "Design, create, structurally review, or revise slide-based presentations when the final artifact is PowerPoint, Google Slides, Keynote, or another deck. Use for storyline, pacing, one-message slides, core/notes/appendix/omit triage, Q&A readiness, and visual-semantic hierarchy. Do not use for prose-first output or formatting-only edits without structural review; use text-document-architect for prose-first documents."
---

# Presentation Architect

Create slide decks that move an audience through a time-bounded sequence of understanding, evidence, reframing, and decision. Design the main deck as the essential presentation path and the appendix as a query-driven branch for Q&A and verification.

Route by the **target artifact**, not the source material. If the requested output is prose-first, do not use this skill even when the source is a deck. Match the user's language; default to Japanese for Japanese requests.

## Operating model

```text
audience state A
  -> orientation
  -> tension or decision question
  -> evidence and explanation
  -> reframe or comparison
  -> decision and action
audience state B

main deck = sequence everyone must experience
speaker notes = nuance better heard than seen
appendix = material retrieved when a question arises
omit = material with no earned role
```

A presentation is not a long document cut into rectangles. It must manage attention, presentation time, spoken delivery, visual form, and optional depth.

## Select the operating mode

Infer the mode from the request:

- **design**: create the presentation brief, content triage, core storyline, storyboard, and appendix plan.
- **create**: design first, then produce the requested slide deck or complete slide specification, repairing hard-gate failures before delivery.
- **review**: diagnose and report on an existing deck without modifying the deck, notes, sources, or supporting files.
- **revise**: diagnose and then revise, including moving material among core slides, notes, appendix, and omission, repairing hard-gate failures before delivery.

When the request is simply “発表資料を作って” or “create a deck,” use **create** and complete the design and triage gates before generating slides.

When **revise** applies self-review or external feedback, also use `revision-hygiene` when available to decide which verification or explanation should persist. This skill remains authoritative for presentation structure and quality.

## Core workflow

### 1. Inspect sources, constraints, and the real deck

Read supplied source material before drafting. Identify:

- audience, prior knowledge, incentives, objections, and decision authority;
- delivery mode: live presentation, slide-based read-ahead, or hybrid;
- presenter role and expected interaction;
- meeting objective, exact ask, duration, Q&A time, and page constraints;
- required data, citations, templates, brand rules, and existing notes;
- whether the deck must remain editable.

For an existing deck, inspect the actual slides and speaker notes. For current or external claims, verify them. Never invent evidence, quotations, citations, numbers, or organizational context.

### 2. Resolve material decisions and build the presentation brief

In design and create modes, establish source- or research-backed facts yourself, state safe
defaults for non-material gaps, and ask only user choices that could materially change the deck.

When the user explicitly asks to be interviewed or grilled, ask prerequisite decisions first, at
most three per round, with a recommended answer and brief rationale for each. Defer dependent
questions and repeat until material choices are resolved or explicitly deferred; do not finalize
the storyboard or full deck earlier. Then summarize the shared understanding and proceed to the
requested output. Do not apply this interview flow in review mode.

Use `assets/presentation-brief.md`. Establish or infer:

- audience state A and desired state B;
- exact decision, belief, or action requested;
- one central thesis;
- the tension, conflict, or unanswered justification that sustains attention;
- delivery mode and time budget;
- 2–5 supporting claims and decisive evidence;
- likely objections, questions, risks, and alternative options;
- visual, brand, and artifact constraints.

For decision decks, show the recommendation early. The open question should usually be **why the audience should accept it**, not **what the recommendation is**.

Classify claims as **Fact**, **Interpretation**, **Hypothesis**, or **Proposal**. Read `references/evidence-and-sources.md` when research or quantitative evidence is involved.

### 3. Choose a presentation pattern

Read `references/presentation-patterns.md` and choose by what the audience must do: decide, accept a proposal, understand an analysis, learn a model, align on strategy, or intervene in progress.

Do not default mechanically to “agenda -> background -> issues -> solution -> summary.” A generic agenda does not create a reason to listen.

### 4. Build the argument and audience-question map

For each major claim, record:

```text
claim -> decisive evidence -> reasoning -> implication
                           -> likely objection or question
                           -> deeper supporting material
```

Use the audience-question map to decide both the core sequence and appendix coverage.

### 5. Triage every candidate item before slide writing

Read `references/content-triage-and-appendix.md` and assign every candidate item to the core
deck, speaker notes, appendix, or omit. Keep any limitation, risk, assumption, or missing evidence
that could change the recommendation in the core path. The reference owns the detailed placement
test and appendix rules.

### 6. Build the core storyline and storyboard

Use `assets/storyboard.md`. For each core slide, specify:

- slide ID and placement;
- audience question;
- primary cognitive move: **Orient, Tension, Question, Observe, Explain, Reframe, Compare, Decide, Act, or Consolidate**;
- message-bearing title;
- decisive evidence or content;
- semantic visual form;
- speaker beat and transition;
- likely question and appendix link;
- time weight.

Run the following gates before visual production.

#### Title-only gate

1. Read only the deck title and core slide titles.
2. Confirm that the thesis, argument, and exact ask remain understandable.
3. Rewrite topic labels such as “背景,” “課題,” “施策,” “まとめ,” or “Appendix” as messages or specific questions.
4. Remove slides that do not advance the audience from A toward B.

#### Filmstrip gate

View the deck as thumbnails or a storyboard:

- Is there a visible progression rather than a set of equal-weight pages?
- Does each slide have one primary job?
- Does the body prove the title rather than repeat it?
- Does the visual form change when the audience's cognitive task changes?
- Does every slide earn presentation time?

#### Time gate

Allocate time by cognitive weight rather than dividing duration evenly. Account for interaction, transitions, and the decision itself. If the sequence does not fit, move detail to the appendix or omit it; do not solve the problem by shrinking text.

### 7. Design cognitive and visual rhythm

Read `references/cognitive-rhythm-and-pacing.md` and use it to vary audience operations, visual
forms, transitions, and time by meaning. Variation must be semantic rather than decorative, and
must not conceal a conclusion the audience needs.

### 8. Design the appendix as a Q&A system

Use `assets/appendix-plan.md` and `references/content-triage-and-appendix.md`. Create an appendix
only when a foreseeable question, verification need, or decision branch should not interrupt the
core sequence; otherwise record why no appendix is needed. The reference owns the Q&A mapping,
navigation, density, and promotion rules.

### 9. Generate in staged passes

Do not create the full deck in one undifferentiated pass.

1. **Core skeleton**: titles, slide roles, and sequence.
2. **Proof pass**: evidence, examples, and claim support.
3. **Visual pass**: choose forms that express comparison, causality, sequence, hierarchy, or scale.
4. **Delivery pass**: speaker notes, transitions, and time weights.
5. **Appendix pass**: when useful, Q&A coverage, detailed evidence, and navigation.
6. **Artifact pass**: generate, render, inspect, and revise.

### 10. Produce and verify the slide artifact

Read `references/artifact-production.md`. When a dedicated format-specific skill such as
`Presentations` is available, use it for template handling, file construction, rendering, and
artifact QA. This skill remains authoritative for storyline, evidence, content placement, pacing,
speaker notes, and appendix design. Resolve any conflict by preserving the user's artifact format
and the format-specific skill's technical production requirements.

Follow the reference's production and QA procedure. Render every slide and inspect both individual
slides and the full filmstrip before delivery.

### 11. Rehearse and review independently

Run a presenter pass:

- Can the presenter explain why each core slide follows the previous one?
- Can the deck fit the available time without rushing the decision?
- Can likely questions be answered quickly from the core deck or appendix?
- Are any core slides present only because the source material contained them?
- Are any critical claims supported only in speaker notes or appendix?

Score the deck with `references/quality-rubric.md` and handle hard-gate failures according to the selected operating mode.

When a structured Markdown storyboard is available, optionally run:

```bash
python scripts/lint_deck_outline.py path/to/storyboard.md --mode decision --check-sources
```

Lint findings are editorial prompts, not proof of quality.

## Output contracts

### Design mode

Return:

1. presentation brief;
2. audience-state transition and central thesis;
3. argument and audience-question map;
4. content triage: core / notes / appendix / omit;
5. title-only core storyline and storyboard;
6. appendix plan and Q&A coverage matrix, or the reason no appendix is needed;
7. hard-gate results.

Do not generate the final deck unless requested.

### Create mode

Deliver the requested deck or complete slide specification, including speaker notes and appendix when useful. Mention only material assumptions, unresolved evidence gaps, and verification risks.

### Review mode

Return prioritized findings with slide location, audience impact, structural cause, and concrete fix. Include:

- revised title-only storyline;
- a move table showing which slides stay in core, move to notes, move to appendix, or are removed;
- appendix gaps for likely Q&A.

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
