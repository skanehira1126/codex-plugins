# codex-plugins

個人用のCodexプラグインを管理するリポジトリです。

## 提供プラグイン

### python-coding

保守しやすいPythonコードの設計・実装・レビューを支援します。

- `$python-coding:choose-code-boundaries`: 薄いhelperや不要なclassを避け、自然な責務境界を選ぶ
- `$python-coding:polars-style`: Polarsのnamed expressionを標準化し、`.alias()`の増殖を防ぐ
- `$python-coding:avoid-legacy-python-compatibility`: サポート対象外の旧Python向け互換コードを避ける

## 導入方法

Codex CLIでこのリポジトリをmarketplaceとして登録します。

```bash
codex plugin marketplace add skanehira1126/codex-plugins --ref main
```

続けて`python-coding`プラグインをインストールします。

```bash
codex plugin add python-coding@codex-plugins
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
```

Skillとプラグインの概要は[OpenAI公式ドキュメント](https://learn.chatgpt.com/docs/skills-and-plugins)を参照してください。
