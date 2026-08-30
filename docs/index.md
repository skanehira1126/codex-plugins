# Codex Plugins

日々の開発で繰り返し使える、小さく焦点の合ったCodexプラグインを配布しています。

## 提供中のプラグイン

### Python Coding

保守しやすいPythonコードを書くための設計、テスト、互換性、Polarsの実装判断を支援します。

[Python CodingのSkillを見る](plugins/python-coding.md){ .md-button .md-button--primary }

### Skill Development

新しいworkflowをSkillにするべきか、既存Skillを更新するべきかを整理します。

[Skill Developmentを見る](plugins/skill-development.md){ .md-button }

### Document Authoring

文章やスライドなどの成果物を、用途に合う構造から設計、作成、レビュー、改訂、検証します。

[Document Authoringを見る](plugins/document-authoring.md){ .md-button }

### Revision Hygiene

コード、文書、スライド、設定などへのレビュー修正で、不要なtest、comment、互換層、注記を残さず、現在の契約へ収束させます。

[Revision Hygieneを見る](plugins/revision-hygiene.md){ .md-button }

### Agent Coordination

実装をサブエージェントへ段階的に委譲しながら、メインの会話で設計や方針の議論を続けます。

[Agent Coordinationを見る](plugins/agent-coordination.md){ .md-button }

## すぐに使う

```bash
codex plugin marketplace add skanehira1126/codex-plugins --ref main
codex plugin add python-coding@codex-plugins
```

インストール後は、普段どおりCodexへ依頼できます。確実に特定のSkillを使いたい場合は、依頼文にSkill名を含めます。

```text
$python-coding:choose-effective-tests を使って、
この変更に必要なテストを追加してください。
```

[導入手順へ進む](getting-started.md){ .md-button .md-button--primary }
