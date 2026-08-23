# Document Authoring

文章、スライドなど文書的な成果物を、構造設計から作成、自己レビュー、フィードバック反映、改訂、検証まで一貫して扱うプラグインです。

## インストール

```bash
codex plugin add document-authoring@codex-plugins
```

## Skill一覧

### `text-document-architect`

Word、Google Docs、Markdownなど文章中心の成果物を、読者、中心命題、論証、根拠、情報配置、認知的な流れから設計・作成・構造レビュー・改訂します。

```text
$document-authoring:text-document-architect を使って、
この調査結果を意思決定者向けの提案書にしてください。
```

### `presentation-architect`

PowerPoint、Google Slides、Keynoteなどの発表資料について、storyline、pacing、一枚一メッセージ、本編・speaker notes・Appendix・削除の配置、Q&A readinessを設計・レビュー・改訂します。

```text
$document-authoring:presentation-architect を使って、
この報告書から15分の意思決定用deckを設計してください。
```

### `revision-hygiene`

自己レビューまたは外部レビューの修正を反映するとき、却下・削除された概念を不要なtest、comment、guard、互換層、注記として残さず、望ましい修正後状態へ収束させます。

ただし、security、課金、重複副作用、互換性など、現在の公開契約や重大リスクを固有に守る検証は削除しません。

```text
$document-authoring:revision-hygiene を使って、
このレビュー指摘を不要な不在testや墓標commentを増やさずに反映してください。
```

## Skillの使い分け

| 最終成果物・作業 | Skill |
|---|---|
| 文章中心の文書 | `text-document-architect` |
| スライド資料 | `presentation-architect` |
| レビュー後の修正で残留物を増やしたくない | `revision-hygiene` |

改訂では、成果物形式に対応するarchitect Skillと`revision-hygiene`を組み合わせられます。文章・スライド固有の構造品質はarchitect Skill、不要なtestやcommentを残すかどうかの判断は`revision-hygiene`が担当します。
