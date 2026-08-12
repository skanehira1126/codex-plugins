# Skill Development

Codex Skillを作成・更新する前に、workflowの責務と配置を整理するプラグインです。

## インストール

```bash
codex plugin add skill-development@codex-plugins
```

## `plan-skill-change`

依頼したworkflowと利用可能なSkillを比較し、次のどれが適切かを判断します。

- 既存Skillを更新する
- 既存Skillのreference、script、assetだけを拡張する
- 責務が混ざったSkillを分割する
- 新しいSkillを作る
- Skillを作らず、prompt、`AGENTS.md`、設定、connectorなど別の場所へ置く

### 向いている依頼

- 新しいworkflowをSkill化する価値があるか判断したい
- 既存Skillへ追加するか、別Skillにするか迷っている
- repo、user、pluginのどこへ置くか決めたい
- Skill Creatorへ渡す前に対象・非対象を明確にしたい

```text
$skill-development:plan-skill-change を使って、
PRレビューのworkflowを新しいSkillにするべきか判断してください。
```

### 成果物

判断結果、既存Skillとの比較、含める責務と含めない責務、Skill Creatorへ渡せる依頼文をまとめます。このSkill自体は、Skillファイルを作成・変更しません。

!!! tip
    変更対象のSkillと編集内容がすでに明確な場合は、このSkillを挟まず直接更新する方が適切です。
