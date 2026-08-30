# Document Authoring

文章、スライドなど文書的な成果物を、用途に合う構造、根拠、情報配置、ナビゲーションから設計、作成、レビュー、改訂、検証するプラグインです。

## インストール

```bash
codex plugin add document-authoring@codex-plugins
```

## Skill一覧

### `text-document-architect`

Word、Google Docs、Markdownなど文章中心の成果物を、連続読解、学習、検索・引き当てに
合う構造、根拠、情報配置、ナビゲーションから設計・作成・構造レビュー・改訂します。

```text
$document-authoring:text-document-architect を使って、
この調査結果を意思決定者向けの提案書にしてください。
```

### `presentation-architect`

PowerPoint、Google Slides、Keynoteなどの発表資料について、意思決定、学習、進捗共有に
合うstoryline、pacing、一枚一メッセージ、本編・speaker notes・Appendix・削除の配置を
設計・レビュー・改訂します。

```text
$document-authoring:presentation-architect を使って、
この報告書から15分の意思決定用deckを設計してください。
```

## Skillの使い分け

| 最終成果物・作業 | Skill |
|---|---|
| 文章中心の文書 | `text-document-architect` |
| スライド資料 | `presentation-architect` |

レビュー指摘を反映するときに不要な残留物を増やしたくない場合は、独立した
[Revision Hygiene](revision-hygiene.md)を併用します。DOCXやPPTXなどの生成・render・
形式検証には、利用可能な形式固有Skillを優先します。
