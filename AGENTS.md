# AGENTS.md

## このリポジトリの目的

このリポジトリは、個人の作業で利用する Codex plugin と skill を管理するためのものです。
変更では、skill の数を増やすことよりも、実際の作業で繰り返し使えること、発火条件が明確であること、保守しやすいことを優先してください。

## リポジトリ構成

- `plugins/<plugin-name>/.codex-plugin/plugin.json`: plugin のマニフェスト
- `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`: skill の本体
- `plugins/<plugin-name>/skills/<skill-name>/scripts/`: skill 専用の実行可能な補助スクリプト
- `plugins/<plugin-name>/skills/<skill-name>/references/`: 必要なときだけ読む補足資料
- `plugins/<plugin-name>/skills/<skill-name>/assets/`: テンプレートや静的素材
- `.agents/plugins/marketplace.json`: このリポジトリで配布する plugin の一覧

存在しない補助ディレクトリは、用途が生じるまで作成しないでください。

## 作業方針

1. 変更対象の `SKILL.md` と、同じ plugin 内の関連 skill、plugin manifest を先に読んでください。
2. 新しい skill を作る前に、既存 skill の責務や発火条件を拡張する方が自然でないか確認してください。
3. skill の境界が曖昧な場合は、対象タスク、発火条件、非対象、期待する成果物を先に言語化してください。
4. 変更は依頼に必要な最小範囲に限定し、無関係な skill、表現、整形をまとめて変更しないでください。
5. ユーザーの未コミット変更を保持し、明示的な依頼なしに上書き、削除、巻き戻しをしないでください。

## Skill の作成・更新規約

- skill ディレクトリ名と frontmatter の `name` は同じ kebab-case にしてください。
- `description` には「何をする skill か」だけでなく、「どのような依頼で使用するか」を具体的に記載してください。誤発火しやすい場合は非対象も記載してください。
- `SKILL.md` は、エージェントがそのまま実行できる命令として記述してください。背景説明を増やすより、判断基準、手順、完了条件を明確にしてください。
- 同じ指示を複数箇所に重複させないでください。常に必要な指示は `SKILL.md` に置き、状況依存の詳細は `references/` に分離してください。
- 定型処理や再現性が必要な処理は `scripts/` に置くことを検討してください。スクリプトを追加した場合は、入力、出力、失敗時の挙動を `SKILL.md` に記載してください。
- テンプレートや素材は `assets/` に置き、既存資産を再利用してください。
- 特定マシンの絶対パス、認証情報、個人情報、一時的な作業状態を skill に埋め込まないでください。
- 例は実際の判断を助ける場合だけ追加し、本文の規則と矛盾させないでください。

## Plugin と marketplace の整合性

- plugin を追加、削除、改名、移動した場合は、`.agents/plugins/marketplace.json` も同じ変更で更新してください。
- `.codex-plugin/plugin.json` の `name` は plugin ディレクトリ名と一致させ、`skills` の参照先が実在することを確認してください。
- manifest と marketplace は正しい JSON を維持し、コメントや末尾カンマを入れないでください。
- plugin の利用者向け挙動が変わる場合は、manifest の説明、表示情報、version の更新要否を確認してください。
- 既存 plugin に自然に属する skill のためだけに、新しい plugin を作らないでください。

## 検証

変更内容に応じて、少なくとも次を確認してください。

- 変更したすべての `SKILL.md` を先頭から末尾まで読み直す。
- YAML frontmatter が有効で、`name` と `description` が存在する。
- skill 名、ディレクトリ名、manifest、marketplace の名前とパスが一致する。
- `SKILL.md` から参照するファイル、スクリプト、assets が実在する。
- JSON ファイルを JSON parser で検証する。
- 追加・変更したスクリプトの代表的な正常系と、重要な失敗系を実行する。
- 利用可能な公式 validator がある場合は、変更した skill/plugin に対して実行する。
- `git diff` を読み、依頼外の変更、秘密情報、ローカル専用パスが含まれていないことを確認する。

検証できなかった項目がある場合は、完了報告で理由と影響を明記してください。

## レビューと完了報告

- レビューで発見した問題とレビュー結果は、必ず日本語で記載してください。
- 問題を報告するときは、対象ファイルと該当箇所、影響、修正案を具体的に示してください。
- 完了報告には、変更した内容、実行した検証、未検証事項を簡潔に記載してください。
