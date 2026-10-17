# Document Authoring

文章、スライドなど文書的な成果物を、用途に合う構造、根拠、情報配置、ナビゲーションから設計、作成、レビュー、改訂、検証するプラグインです。

## インストール

```bash
codex plugin add document-authoring@codex-plugins
```

## Skill一覧

### `text-document-architect`

Word、Google Docs、Markdownなど文章中心の成果物を、連続読解、学習、検索・引き当てに
合う構造、根拠、情報配置、ナビゲーションと文・段落の表現を設計・作成・レビュー・改訂します。

共通品質原則（Core）を、読み方（sequential / learning / lookup/reference）に合わせて
適用します。複数の素材は読者の目的に沿って統合し、推論はつながる段落、並列項目は
リスト、共通軸の比較は表など、関係に合う表現を選びます。固定の章構成や結論先出しを
すべての文書へ強制しません。

用途固有の文体・必須内容・評価基準（Purpose Preset）は作業環境側で管理します。
ユーザーやAGENTS.md等が明示する要件を確認して取り込み、指定がなければCore × Profileで
動作します。未読の参照先を適用済みとは扱わず、Presetの自動探索・作成・変更は行いません。
レビューのみの依頼では原本と関連ファイルを変更しません。

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
