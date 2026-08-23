# `revision-hygiene` behavior cases

Use these cases after meaningful changes. Judge decisions and resulting artifacts, not exact wording.

## Trigger cases

### Should trigger

- 「同じValidationは後続で行っているので、前段の重複を削除して」
- 「レビュー指摘を反映して。ただし不要になった仕組みをテストやコメントとして残さないで」
- 「この説明は本文に不要なので削り、文書全体も再確認して」
- 「提案書の章構成に関する指摘を反映し、却下した構成案の注記は残さないで」— `text-document-architect`と併用
- 「deckのstorylineをレビューどおり改訂し、削除したslideのspeaker noteは残さないで」— `presentation-architect`と併用
- “Apply these review comments and remove any obsolete compatibility residue.”

### Should not trigger

- 「このPRをレビューして」— diagnosis only
- 「この提案書を構造レビューして、問題と修正案だけ報告して」— diagnosis only; 成果物を変更しない
- 「このdeckをレビューして、storylineの問題を指摘して」— diagnosis only; 成果物を変更しない
- 「新しい認証機能を実装して」— no review-driven revision yet
- 「既存テストが何を保証しているか説明して」— explanation only

## Behavioral cases

### Duplicate validation with unchanged public behavior

Given two equivalent internal validations and an existing downstream behavior test, remove the redundant validation and its implementation-only support. Do not add a test or comment whose only purpose is to assert that the removed validation is absent.

### Duplicate action with observable harm

Given a duplicate call that can cause double billing, notification, persistence, or another material side effect, preserve or add a behavioral test for the exactly-once outcome. Do not assert a private helper's absence when the observable outcome is sufficient.

### Obsolete explanation in a document or deck

Remove the rejected paragraph, note, appendix item, or speaker note. Verify that the remaining reader or audience path is coherent. Do not add an explanation that the content was removed unless change history is explicitly required.

### Structural document or deck revision requires co-use

When feedback changes a prose document's hierarchy, argument, reader motion, or information placement, use `text-document-architect` for those decisions and this skill only for residual-artifact decisions. When feedback changes a deck's storyline, pacing, or core/notes/appendix placement, use `presentation-architect` on the same basis. Use a format-specific artifact skill for generation, rendering, and technical verification when available.

### Diagnosis-only review

Given a request to review a pull request, document, or deck and report findings without applying changes, do not enter this skill's revision workflow or modify the artifact. If the skill is explicitly named, limit its contribution to diagnosing residual-artifact risks and proposing fixes.

### Security or compatibility invariant

When an old API, unsafe dependency, secret-bearing output, or incompatible format must remain prohibited, keep the smallest suitable guard, static rule, contract test, migration note, or audit evidence. State the current invariant rather than narrating the review history.

### Existing coverage is sufficient

Run the existing relevant checks. If they already fail for a plausible regression and pass for the corrected implementation, do not add a duplicate case for the same Given, When, Then, and oracle.

### Feedback is invalid or outside scope

Verify the review claim against the actual artifact and accepted requirements. If it is false, hypothetical under excluded assumptions, or materially outside the requested change, do not implement or test it as a new requirement. Report the reason concisely.

## Regression failures

- A tombstone comment describes removed code without a current reason.
- A test name or fixture preserves a rejected concept while asserting no user-visible contract.
- A removed branch returns as a flag, empty wrapper, fallback, or compatibility shim.
- A necessary security, compatibility, or exactly-once test is deleted under a blanket “do not test absence” rule.
- Reviewer severity or confident wording silently expands the approved scope.
- A structural document or deck revision uses this skill alone and omits the corresponding architect Skill.
- A diagnosis-only review modifies the artifact or creates cleanup residue.
