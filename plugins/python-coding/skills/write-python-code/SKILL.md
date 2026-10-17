---
name: write-python-code
description: >-
  Pythonのコード・テストを実装、修正、リファクタリング、レビューするときに、共通のコメント生成指針を適用し、必要な設計・テスト・互換性・Polarsの用途別Skillを選ぶ。コメント・docstringの判断にも使用する。実装判断を伴わない説明・実行だけの依頼や、機械的な書式修正は対象外。
---

# Write Python Code

## 共通指針

コード・テストを生成・変更するとき、またはコメント・docstringの妥当性をレビューするときは、[コメントの指針](references/code-comments.md)を読む。

## 用途別Skill

依頼に含まれる判断に応じて、必要なSkillだけを読む。全件を既定で読み込まない。

| 判断 | Skill |
| --- | --- |
| 共通化、関数分割、責務分離、helper・classなどの抽象化 | [choose-code-boundaries](../choose-code-boundaries/SKILL.md) |
| テストの追加・修正・選択・レビュー、回帰防止、カバレッジ改善 | [choose-effective-tests](../choose-effective-tests/SKILL.md) |
| サポートするPythonに合わせた構文・typing・標準ライブラリ・互換処理の選択 | [avoid-legacy-python-compatibility](../avoid-legacy-python-compatibility/SKILL.md) |
| Polarsのselect・with_columns・agg、動的列やExpr helperの実装 | [polars-style](../polars-style/SKILL.md) |

同じ作業で読んだSkill・referenceは再読しない。用途別Skillから来た場合は呼び出し元を再び読み込まず、共通指針と今回必要な未読Skillを確認して元の作業へ戻る。読み込みを理由に依頼外の設計変更やテスト整理へ広げない。
