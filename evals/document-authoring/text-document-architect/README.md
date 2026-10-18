# Text Document Architectの保守・評価

このディレクトリはリポジトリ内の保守用資料です。marketplaceのplugin sourceである
`plugins/document-authoring/`の外に置き、文章作成Skillには同梱しません。
対象は[text-document-architect](../../../plugins/document-authoring/skills/text-document-architect/SKILL.md)です。

## 既存Skillでの扱い

変更の設計とレビューには[shape-skill-change](../../../plugins/skill-development/skills/shape-skill-change/SKILL.md)を使い、
対象Skillとこの評価ディレクトリを入力として指定します。同Skillの責務・出力・resourceの
確認に使えるため、専用の運用Skillは追加しません。実装には`skill-creator`を使います。

複数モデルで実際の生成結果を比較する場合は、明示依頼と評価範囲の承認を経て
[evaluate-skill-robustness](../../../plugins/skill-development/skills/evaluate-skill-robustness/SKILL.md)を使えます。
変更レビューだけで生成評価を実行したとは扱いません。生成側には選んだ依頼・素材と
対象Skillだけを渡し、期待結果や改善例は評価側で保持します。

## 評価素材

- [cases.md](cases.md)：発火・動作境界の回帰ケース。
- [prose-cases.md](prose-cases.md)：文章表現と利用要件の評価ケース。
- [prose-samples.md](prose-samples.md)：架空の改善前後の編集例。生成評価の実行結果ではありません。
- `sample-*.md`：lint確認用のfixture。
- `test_lint_text_document.py`：配布Skill内のlintを検証するCLI回帰テスト。

## ローカル検証

リポジトリrootから実行します。

```bash
python -m unittest discover -s evals/document-authoring/text-document-architect -p 'test_*.py'
python plugins/document-authoring/skills/text-document-architect/scripts/lint_text_document.py evals/document-authoring/text-document-architect/sample-good-document.md --mode decision --check-sources
python plugins/document-authoring/skills/text-document-architect/scripts/lint_text_document.py evals/document-authoring/text-document-architect/sample-bad-document.md --mode decision --check-sources
```

ケースの追加、原文の編集レビュー、実際の生成実行は区別して記録します。
lintは注意箇所を示すだけで、意味的な読みやすさは別に確認します。
