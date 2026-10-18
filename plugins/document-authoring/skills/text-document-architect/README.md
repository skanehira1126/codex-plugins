# Text Document Architect 保守ガイド

`SKILL.md`は、読者と目的の把握、素材の整理、執筆、読み直しと納品の順で読む実行手順です。
題材に共通する文章の基本をここに置き、通常の作業が本文だけで進むように保守します。

## 補助資料の役割

- `references/reading-needs.md`：順読・学習・参照など、利用要件に応じて考慮すること。
- `references/verification.md`：数値・引用・参照構造・ファイル納品など、該当時の確認。
- `assets/`：設計やレビューを共有する場合の任意のメモ。
- `evals/`：保守者向けの回帰ケース、編集例、自動テスト。実行時に一式を読ませない。

規則を足す前に、既存の書く手順へ自然に組み込めるか確認します。詳細を分割するだけで
参照先を増やさず、同じ判断を複数箇所で要求しないでください。必須の章構成や採点表を
作るより、読者に何が伝わるかを評価します。スライドSkillへ実行時依存は持ちません。

## 検証

Skillディレクトリから実行します。

```bash
python -m unittest discover -s evals -p 'test_*.py'
python scripts/lint_text_document.py evals/sample-good-document.md --mode decision --check-sources
python scripts/lint_text_document.py evals/sample-bad-document.md --mode decision --check-sources
```

`evals/cases.md`は既存の発火・動作境界、`evals/prose-cases.md`は文章表現と要件適用の回帰を
扱います。`evals/prose-samples.md`は架空の編集例で、生成評価の実行結果ではありません。
ケース追加、原文の編集レビュー、実際の生成実行を区別して記録してください。
lintは注意箇所を示すだけで、意味的な読みやすさは別に確認します。

配布版とrelease noteはplugin manifestとリポジトリrootの`CHANGELOG.md`で管理します。
このSkill内の`CHANGELOG.md`は過去履歴です。
