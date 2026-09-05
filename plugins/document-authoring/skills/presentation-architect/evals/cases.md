# Regression cases for `presentation-architect`

Use these as lightweight trigger and behavior checks after meaningful changes.

Run the executable lint regression suite with:

```bash
python -m unittest discover -s evals -p 'test_*.py'
```

## Trigger cases

### Should trigger

- 「この調査メモを、15分の経営会議用PowerPointにして」
- 「このスライドを本編とAppendixに整理し直して」
- “Review this deck for storyline, pacing, and Q&A readiness.”

### Should not trigger

- 「このスライドを2ページのWordメモにして」 → `text-document-architect`
- 「既存PPTXのフォントだけ統一して」 unless structural review is also requested
- 「この文章を校正して」

## Behavioral cases

### Structural profile selection

Use these representative requests to confirm that the skill selects a profile without inventing
decision mechanics:

| Request | Expected profile | Required progression | Must not force |
|---|---|---|---|
| “Recommend one of these three vendors to the steering committee.” | argument-led | recommendation, evidence, tradeoffs, risks, ask | none of the applicable decision gates |
| “Teach new analysts how cohort retention differs from period retention.” | learning-led | familiar example, model, guided application, misconception, next use | recommendation, artificial tension, approval ask, appendix justification |
| “Turn this sprint record into a ten-minute status deck for the project team.” | update-led | objective, material change, evidence, blockers, owners, checkpoint | thesis debate, Q&A appendix or its rejection rationale, invented decision |

For every profile, keep one governing message or objective, one primary job per slide, a sequence
that fits the time budget, and rendered artifact QA.

### Grilling and ordinary creation boundary

- Grilling example: "The audience and decision are still fuzzy. Grill me before you build it."
- Ordinary example: "Turn these approved notes into a ten-minute internal update deck."
- Explicit grilling follows the shared authoring interview protocol.
- Ordinary creation states safe defaults and completes the deck and artifact QA without exhaustive questioning or a separate storyboard approval, unless the user requested that checkpoint.
- A full deck is not generated while a material upstream decision remains unresolved.

### Source material contains too much detail

Must:

- triage each item into core, notes, appendix, or omit before slide generation;
- keep only content essential to the intended outcome in the core;
- map material questions or support needs and create an appendix only when it improves retrieval;
- avoid shrinking text to fit everything.

### Decision deck

Must:

- state the recommendation and exact ask early;
- leave the justification or tradeoff as the continuing question;
- keep decision-changing risks and assumptions in core;
- cover predictable questions in core or, only when useful, a question-driven appendix.

### Storyline review without revision

Must:

- use review mode and report prioritized findings, adding a proposed title-only storyline, move table, or support gaps only where the findings require them;
- leave the supplied deck, notes, sources, and supporting files unchanged;
- treat the proposed storyline and slide moves as recommendations rather than applied edits.
- not use grilling to obtain permission for revision or invent new deck requirements.

Failure:

- modifies the reviewed artifact or reports proposed slide moves as completed changes.

### Training deck

Must:

- use problem/example before concept where useful;
- vary cognitive moves and visual forms semantically;
- not force conclusion-first executive logic when the audience must discover a model.

### Structural revision after review feedback

Must:

- use `revision-hygiene:revision-hygiene` with `presentation-architect` when it is available;
- let `presentation-architect` own storyline, pacing, placement, notes, and appendix quality;
- use `revision-hygiene:revision-hygiene` to remove rejected or obsolete material without leaving tombstone notes, duplicate checks, or appendix residue;
- preserve current sources, brand constraints, and verification that still protect the revised deck.

## Regression failure examples

- Every slide uses the same three-card layout.
- Generic agenda titles substitute for a meaningful progression.
- Appendix is a dump of all removed content.
- The only evidence for a core claim appears in appendix.
- The deck cannot fit the time budget except by rushing or tiny text.
