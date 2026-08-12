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

<!-- knowledge-refinery:agents:start lang=jp -->
## Knowledge Refinery

このリポジトリでは、開発中に得た再利用可能な経験をKnowledge Refineryで管理する。

- `.refinery.yaml` が `enabled: true` の場合だけ利用し、repo-scoped MCP toolsには現在repoの絶対パスを `project_path` として渡す。
- statusの`vault_match`がtrueの場合だけrepo-scoped toolsを使う。不一致時は停止してactive vaultを報告し、`vault_id`を手編集して回避しない。
- `enabled: false` は意図的なOFFとして扱い、検索や記録の依頼だけを理由に再有効化しない。再有効化は利用者の明示依頼または確認がある場合だけ行う。
- 設定を修復するときは、存在する `refinery-project` skillと文書化されたCLIだけを使い、存在しないrepair skillやcommandを案内しない。
- projectの名前、概要、検索用tag、主要技術が変わった場合は、現在revisionを取得して中央vaultのproject metadataを部分更新する。目的・領域のtagはlowercase kebab-case、技術名はtechnologiesだけに保存する。
- 作業開始時は、現在project memoryとshared memory、現在project experienceの順に検索する。足りない場合だけ、`project_ids`で選んだproject、さらに必要な場合だけ`all_projects: true`へ広げる。`project_ids`と`all_projects: true`は併用しない。
- meaningfulな検証、比較、不採用判断、失敗から知見を得た場合は `refinery-experience` skillを使う。
- 将来のagentの選択、回避、検証、診断を変える結果だけをexperienceにし、定型作業の完了報告、進捗log、明白なtypo修正、新しい根拠のない反復は記録しない。
- experienceは目的、試したこと、分かったこと、微妙だった点、次の可能性を一つの記録にまとめる。
- statusは、評価可能な結果なら成否を問わず`completed`、根拠不足や矛盾で答えが出ないなら`inconclusive`、評価前に停止したなら`abandoned`、後続experienceが結論を置換した場合だけ`superseded`とする。
- confidenceは、条件を明記した再現可能な直接根拠なら`high`、直接根拠はあるが反復や適用範囲が限定的なら`medium`、部分的・間接的な根拠または重要な未解決点があるなら`low`とする。
- 新規experienceは安定したlowercase slugの`experience_id`を先に決める。結果不明のcreateをretryする前にexact getまたはID検索で保存済みか確認する。
- 既存experience/memoryの更新は現在revisionを使う。optional fieldの省略は保持、空listは明示clear、confidenceのclearは`clear_confidence: true`とする。
- 実装へ採用しなかったことや、evidenceがuntrackedであることを理由に記録を捨てない。
- evidenceを保存するためだけにプロダクトrepoへcommitしない。
- 複数experienceから繰り返し使える原則を抽出するときは `refinery-memory` skillを使う。
- project memoryは原則として反復または相補的な2件以上のexperienceを根拠にする。利用者が明示依頼した場合だけ1件を許し、scopeを狭め、未検証の限界を本文へ書き、confidenceを`high`にしない。
- shared memoryは異なる2 project以上の独立した根拠があっても自動作成しない。候補の原則、scope、限界、反例、confidence、source IDを提示し、利用者の明示承認後だけ作成・昇格する。
- secret、credential、access token、PII（個人情報）、顧客data、redactしていない機密logをvaultへ保存しない。logやevidenceは機密値を除去し、安全にできない場合は非機密の説明と限界だけを残す。
- 作業終了前に、今回の作業から記録すべきexperienceがないか確認する。
- 日次棚卸しでは `refinery-maintenance` skillを使う。
- プロダクトrepoとrefinery repoの変更を同じcommitやPRへ混ぜない。
<!-- knowledge-refinery:agents:end -->
