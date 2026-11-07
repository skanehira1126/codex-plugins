# Document Authoring

文章、スライドなど文書的な成果物を、用途に合う構造、根拠、情報配置、ナビゲーションから設計、作成、レビュー、改訂、検証するプラグインです。

## インストール

```bash
codex plugin add document-authoring@codex-plugins
```

## Skill一覧

### `text-document-architect`

Word、Google Docs、Markdownなどの文章を、読者が必要な前提を補わずに理解できる形へ
設計・作成・レビュー・改訂します。利用場面と目的から記載内容と条件を整理し、要点の
把握、参照、作業、学習、判断に合う構成へ配置してから書きます。利用ガイドを事前に読み、
当日に必要箇所を確認するなど、複数の読み方にも対応します。完成後は、想定した使い方での
構成の確認と、原資料に対する内容の照合を別々に行います。
書き手の立場と読者との関係も捉え、自分用の記録や、ユーザーに代わって書く報告・案内などに
合う人称・丁寧さ・呼びかけ方を選びます。
レビューのみの依頼では原本を変更しません。

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
