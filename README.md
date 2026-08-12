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

- `$skill-development:plan-skill-change`: workflowを新しいSkillにするか、既存Skillを変更するか、別の場所に置くかを判断する

## 導入方法

Codex CLIでこのリポジトリをmarketplaceとして登録します。

```bash
codex plugin marketplace add skanehira1126/codex-plugins --ref main
```

続けて使用するプラグインをインストールします。

```bash
codex plugin add python-coding@codex-plugins
codex plugin add skill-development@codex-plugins
```

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
codex plugin add python-coding@codex-plugins
codex plugin add skill-development@codex-plugins
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
