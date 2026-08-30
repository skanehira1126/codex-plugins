# Revision Hygiene

コード、文書、スライド、設定などへ自己レビューまたは外部レビューの修正を反映するとき、
却下・削除された概念を不要なtest、comment、guard、互換層、注記として残さず、現在の
契約へ直接収束させるプラグインです。

## インストール

```bash
codex plugin add revision-hygiene@codex-plugins
```

## Skill

### `revision-hygiene`

レビュー結果を検証可能な入力として扱い、修正後に成立すべき状態を定義します。現在の
公開契約、security、privacy、課金、重複副作用、互換性などを固有に守る検証は残します。

```text
$revision-hygiene:revision-hygiene を使って、
このレビュー指摘を不要な不在testや墓標commentを増やさずに反映してください。
```

文章やスライドの構造改訂では、`document-authoring`の対応するarchitect Skillを併用します。
DOCX、PPTXなどの生成、render、形式検証には、利用可能な形式固有Skillを優先します。
レビュー結果の診断だけで成果物を修正しない依頼では、このSkillを自動選択しません。
