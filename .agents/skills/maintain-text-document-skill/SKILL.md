---
name: maintain-text-document-skill
description: このリポジトリのtext-document-architectを保守・改訂・レビューし、評価資料とlint回帰テストで変更を確認するときに使う。通常の文章作成・文書レビューや、他のskillの保守には使わない。
---

# Text Document Architectの保守

対象は[配布skill](../../../plugins/document-authoring/skills/text-document-architect/SKILL.md)。
このskillはrepo専用とし、評価資料・テストを配布pluginへ含めない。

## 変更とレビュー

1. 対象skill、関連resource、[manifest](../../../plugins/document-authoring/.codex-plugin/plugin.json)と差分を読み、依頼の対象を特定する。
2. 境界の設計・変更後のレビューには[shape-skill-change](../../../plugins/skill-development/skills/shape-skill-change/SKILL.md)を使う。実装には利用可能な`skill-creator`を使い、repoの変更・release規約に従う。レビューのみなら編集しない。
3. 変更に応じて以下の資料から確認ケースを選び、実際のskillの契約と照合する。
   - [cases.md](references/cases.md)：発火条件、動作境界、lintの正常・不良サンプル。
   - [prose-cases.md](references/prose-cases.md)：素材統合、文・段落・表現形式、外部要件の評価。
   - [prose-samples.md](references/prose-samples.md)：編集例との比較が必要な場合。唯一の正解ではない。
4. 検証結果と未確認範囲を日本語で報告する。ケースの追加、編集レビュー、実際の生成評価は区別する。

## ローカル検証

リポジトリrootから実行する。

```bash
python3 -m unittest discover -s .agents/skills/maintain-text-document-skill/scripts -p 'test_*.py'
```

[scripts/test_lint_text_document.py](scripts/test_lint_text_document.py)は引数不要で、配布skillのlintを
一時ファイルと[正常アウトライン](references/sample-good-outline.md)で検証する。
標準出力・標準エラーへテスト結果を返し、失敗時は非ゼロで終了する。実行場所に依存せず、
テストファイルの位置からリポジトリとfixtureを解決する。
手動のlint確認コマンドと期待結果は[cases.mdのlint回帰確認](references/cases.md#lint回帰確認)を使う。
[不良アウトライン](references/sample-bad-outline.md)も比較用に参照できる。
lintは注意箇所の検出であり、意味的な読みやすさは実際の文章で確認する。

複数モデルによる生成比較を明示的に依頼された場合だけ、
[evaluate-skill-robustness](../../../plugins/skill-development/skills/evaluate-skill-robustness/SKILL.md)へ進む。
生成側には選んだ依頼・素材と対象skillを渡し、期待結果・改善例は評価側で保持する。
