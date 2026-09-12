# はじめる

## 1. Marketplaceを登録する

Codex CLIで、このリポジトリをMarketplaceとして登録します。

```bash
codex plugin marketplace add skanehira1126/codex-plugins --ref main
```

## 2. プラグインをインストールする

用途に合うプラグインだけをインストールできます。

=== "Python Coding"

    ```bash
    codex plugin add python-coding@codex-plugins
    ```

=== "Skill Development"

    ```bash
    codex plugin add skill-development@codex-plugins
    ```

=== "Document Authoring"

    ```bash
    codex plugin add document-authoring@codex-plugins
    ```

=== "Agent Coordination"

    ```bash
    codex plugin add agent-coordination@codex-plugins
    ```

=== "Revision Hygiene"

    ```bash
    codex plugin add revision-hygiene@codex-plugins
    ```

## 3. インストールを確認する

```bash
codex plugin list --marketplace codex-plugins
```

インストールしたプラグインと、そのSkillが表示されれば準備完了です。

## Skillを使う

依頼内容がSkillの対象に合う場合、Codexが自動的にSkillを選びます。利用するSkillを明示したい場合は、`$<plugin-name>:<skill-name>`を依頼文に含めます。

```text
$python-coding:choose-code-boundaries を使って、
このリファクタリング案が過剰設計になっていないかレビューしてください。
```

複数のSkillが必要な依頼では、必要なSkill名をすべて指定できます。

## ローカルcheckoutを試す { #local-checkout }

公開前の変更を試したい場合は、cloneしたディレクトリをMarketplaceとして登録します。

```bash
git clone git@github.com:skanehira1126/codex-plugins.git
cd codex-plugins
codex plugin marketplace add "$PWD"
codex plugin add python-coding@codex-plugins
```

同じ名前のMarketplaceをすでに登録している場合は、現在の登録を確認してから切り替えてください。

## 次に読む

- Pythonの設計・実装・テストを支援してほしい: [Python Coding](plugins/python-coding.md)
- Skill変更の実装前後で責務、配置、肥大化を確認したい: [Skill Development](plugins/skill-development.md)
- 文書やスライドを設計・作成・改訂したい: [Document Authoring](plugins/document-authoring.md)
- レビュー修正で不要な残留物を増やしたくない: [Revision Hygiene](plugins/revision-hygiene.md)
- 実装をサブエージェントへ任せながら会話を続けたい: [Agent Coordination](plugins/agent-coordination.md)
