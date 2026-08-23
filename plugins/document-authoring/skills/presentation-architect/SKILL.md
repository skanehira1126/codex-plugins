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
- **create**: design first, then produce the requested slide deck or complete slide specification.
- **review**: diagnose an existing deck without rewriting unless requested.
- **revise**: diagnose and then revise, including moving material among core slides, notes, appendix, and omission.

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

### 2. Build the presentation brief

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

Use `references/content-triage-and-appendix.md` and assign each item to exactly one destination:

- **Core deck**: everyone must see it in sequence to understand, evaluate, or decide.
- **Speaker notes**: useful nuance, transition, or example that is better heard than seen.
- **Appendix**: useful for a foreseeable question, verification, methodology, sensitivity, segment detail, or secondary implementation discussion, but not required for the main path.
- **Omit**: redundant, unsupported, decorative, source-order residue, or unlikely to affect understanding or Q&A.

Apply the placement test in order:

1. Would removing it change the audience's understanding, decision, or confidence? **Core deck.**
2. Is it necessary for delivery but better spoken than displayed? **Speaker notes.**
3. Is it useful only when a plausible question or verification need arises? **Appendix.**
4. Otherwise, **omit.**

Never place a limitation, risk, assumption, or missing evidence in the appendix if it could change the recommendation.

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

Read `references/cognitive-rhythm-and-pacing.md`.

Avoid long runs in which every slide only explains or asserts. Deliberately vary audience operations:

```text
orient -> notice tension -> observe evidence -> reframe -> compare -> decide -> act
```

Variation must be semantic, not decorative. Do not alternate layouts merely to look dynamic. Use chart-led, diagram-led, comparison, example, statement, and roadmap slides only when those forms match the message.

After dense evidence, provide synthesis, implication, comparison, or decision. Use an open question as a transition when useful, but never use suspense to conceal a conclusion the audience needs.

### 8. Design the appendix as a Q&A system

Use `assets/appendix-plan.md`.

For each likely audience question, record:

```text
question -> core claim -> appendix slide -> evidence/source -> presenter use
```

Appendix rules:

- organize by anticipated question or decision branch, not source-file order;
- use message-bearing titles and stable IDs such as A1, A2, and A3;
- make each appendix slide independently understandable;
- include enough context, definitions, and sources for retrieval during Q&A;
- cross-reference from the core deck when useful;
- add an appendix index when the set is large;
- allow higher density than the core deck, but never illegibility or raw-data dumping;
- promote frequently needed appendix content into the core deck or create a compact core version.

The appendix is not a content graveyard. Speaker notes are not an overflow bin.

### 9. Generate in staged passes

Do not create the full deck in one undifferentiated pass.

1. **Core skeleton**: titles, slide roles, and sequence.
2. **Proof pass**: evidence, examples, and claim support.
3. **Visual pass**: choose forms that express comparison, causality, sequence, hierarchy, or scale.
4. **Delivery pass**: speaker notes, transitions, and time weights.
5. **Appendix pass**: Q&A coverage, detailed evidence, and navigation.
6. **Artifact pass**: generate, render, inspect, and revise.

### 10. Produce and verify the slide artifact

Read `references/artifact-production.md`. When a dedicated format-specific skill such as
`Presentations` is available, use it for template handling, file construction, rendering, and
artifact QA. This skill remains authoritative for storyline, evidence, content placement, pacing,
speaker notes, and appendix design. Resolve any conflict by preserving the user's artifact format
and the format-specific skill's technical production requirements.

Apply these defaults unless the context requires otherwise:

- one primary message per slide;
- title states the slide's answer or claim;
- body proves the title;
- evidence is close to the claim;
- layout expresses meaning rather than decorating it;
- important material receives greater visual weight;
- live decks leave appropriate work to the speaker without becoming unintelligible;
- read-ahead decks include enough connective explanation to stand alone;
- citations remain traceable without dominating the page.

Render all slides. Inspect individual slides and the full filmstrip for clipping, tiny text, accidental wrapping, monotony, hierarchy, pacing, source notes, and appendix navigation.

### 11. Rehearse and review independently

Run a presenter pass:

- Can the presenter explain why each core slide follows the previous one?
- Can the deck fit the available time without rushing the decision?
- Can likely questions be answered quickly from the appendix?
- Are any core slides present only because the source material contained them?
- Are any critical claims supported only in speaker notes or appendix?

Score the deck with `references/quality-rubric.md` and fix all hard-gate failures.

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
6. appendix plan and Q&A coverage matrix;
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

Deliver the revised deck and a concise change summary, including slide moves and appendix additions. Preserve valid sources, notes, brand rules, and editable structure.

## Prohibited shortcuts

Do not:

- treat a deck as a document split across slides;
- give every slide the same density, role, visual form, or card layout;
- hide the recommendation to manufacture suspense;
- use a generic agenda as a substitute for a storyline;
- place decision-changing evidence, risks, or caveats only in the appendix;
- use the appendix as storage for everything removed from the core deck;
- solve time or density problems by shrinking text;
- make slides repeat the speaker word for word;
- add decorative visuals that compete with the message;
- force visual variety when the semantics do not change;
- fabricate evidence to make the narrative complete.

## Reference map

- `references/quality-rubric.md`: scoring, hard gates, and review severity.
- `references/presentation-patterns.md`: core sequences by audience task.
- `references/cognitive-rhythm-and-pacing.md`: audience moves, visual rhythm, transitions, and time.
- `references/content-triage-and-appendix.md`: core, notes, appendix, omit, and Q&A design.
- `references/evidence-and-sources.md`: claim types, source handling, and quantitative evidence.
- `references/examples.md`: before-and-after slide and appendix examples.
- `references/artifact-production.md`: slide generation, notes, rendering, and filmstrip QA.
- `evals/cases.md`: regression prompts for maintainers.
