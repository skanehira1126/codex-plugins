# codex-plugins

個人用のCodexプラグインを管理するリポジトリです。

利用方法と各Skillの選び方は、[利用者向けドキュメント](https://skanehira1126.github.io/codex-plugins/)を参照してください。

## 提供プラグイン

### python-coding

保守しやすいPythonコードの設計・実装・テスト・レビューを支援します。

- `$python-coding:choose-code-boundaries`: 薄いhelperや不要なclassを避け、自然な責務境界を選ぶ
- `$python-coding:choose-effective-tests`: 変更された挙動とリスクを守る必要十分なPythonテストを選ぶ
- `$python-coding:polars-style`: Polarsのnamed expressionを標準化し、`.alias()`の増殖を防ぐ
- `$python-coding:avoid-legacy-python-compatibility`: サポート対象外の旧Python向け互換コードを避ける

### skill-development

Codex Skillの設計、変更、保守を支援します。

- `$skill-development:shape-skill-change`: Skill変更の実装前に責務と配置を判断し、実装後にscope drift、重複、肥大化をレビューする
- `$skill-development:evaluate-skill-robustness`: 明示的に承認したモデルとreasoning effortでSkillの堅牢性を比較評価する

### document-authoring

文章やスライドなどの成果物の構造設計、作成、レビュー、改訂、検証と、コードや設定を含む既存成果物へのレビュー指摘の反映を支援します。

- `$document-authoring:text-document-architect`: 文章中心の文書を、論証、根拠、読者動作から設計・作成する
- `$document-authoring:presentation-architect`: 発表資料のstoryline、pacing、本編・ノート・Appendixを設計する
- `$document-authoring:revision-hygiene`: コードや設定を含むレビュー修正で、不要なtest、comment、互換層などの残留物を増やさない

### agent-coordination

明示的に起動したときだけ、実装をサブエージェントへ段階的に委譲し、メインの会話で議論を続けられるようにします。

- `$agent-coordination:delegate-work-in-stages`: ファイル所有権を分けて1人または複数のサブエージェントへ作業を委譲し、完了時に次の段階を会話で確認する

## 導入方法

Codex CLIでこのリポジトリをmarketplaceとして登録します。

```bash
codex plugin marketplace add skanehira1126/codex-plugins --ref main
```

続けて使用するプラグインをインストールします。

```bash
codex plugin add python-coding@codex-plugins
codex plugin add skill-development@codex-plugins
codex plugin add document-authoring@codex-plugins
codex plugin add agent-coordination@codex-plugins
```

すべてのプラグインをまとめてインストールする場合は、Marketplace登録後に次を実行します。

```bash
./scripts/install-all-plugins.sh
```

実行されるコマンドだけを確認する場合は`--dry-run`を付けます。

インストール結果は次のコマンドで確認できます。

```bash
codex plugin list --marketplace codex-plugins
```

### ローカルcheckoutから導入する

リポジトリの変更を手元で試す場合は、Git marketplaceの代わりにcloneしたディレクトリを登録します。

```bash
git clone git@github.com:skanehira1126/codex-plugins.git
cd codex-plugins
codex plugin marketplace add "$PWD"
./scripts/install-all-plugins.sh
```

Skillとプラグインの概要は[OpenAI公式ドキュメント](https://learn.chatgpt.com/docs/skills-and-plugins)を参照してください。

## ドキュメントをローカルで確認する

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
mkdocs serve
```

ドキュメントは`main`へ反映されるとGitHub ActionsによってGitHub Pagesへ公開されます。
