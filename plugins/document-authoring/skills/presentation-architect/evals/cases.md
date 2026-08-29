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

### Source material contains too much detail

Must:

- triage each item into core, notes, appendix, or omit before slide generation;
- keep only decision-essential content in the core;
- create a Q&A coverage matrix;
- avoid shrinking text to fit everything.

### Decision deck

Must:

- state the recommendation and exact ask early;
- leave the justification or tradeoff as the continuing question;
- keep decision-changing risks and assumptions in core;
- cover predictable questions in core or, only when useful, a question-driven appendix.

### Storyline review without revision

Must:

- use review mode and report prioritized findings, a proposed title-only storyline, a move table, and Q&A gaps;
- leave the supplied deck, notes, sources, and supporting files unchanged;
- treat the proposed storyline and slide moves as recommendations rather than applied edits.

Failure:

- modifies the reviewed artifact or reports proposed slide moves as completed changes.

### Training deck

Must:

- use problem/example before concept where useful;
- vary cognitive moves and visual forms semantically;
- not force conclusion-first executive logic when the audience must discover a model.

### Structural revision after review feedback

Must:

- use `revision-hygiene` with `presentation-architect` when it is available;
- let `presentation-architect` own storyline, pacing, placement, notes, and appendix quality;
- use `revision-hygiene` to remove rejected or obsolete material without leaving tombstone notes, duplicate checks, or appendix residue;
- preserve current sources, brand constraints, and verification that still protect the revised deck.

## Regression failure examples

- Every slide uses the same three-card layout.
- Generic agenda titles substitute for the argument.
- Appendix is a dump of all removed content.
- The only evidence for a core claim appears in appendix.
- The deck cannot fit the time budget except by rushing or tiny text.
