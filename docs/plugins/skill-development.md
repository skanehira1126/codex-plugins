# Skill Development

Codex Skill変更の実装前にworkflowの責務と配置を整理し、実装後にscope drift、重複、肥大化をレビューするプラグインです。必要な場合は、モデルやreasoning effortによる実行差も明示的な承認のもとで評価できます。

## インストール

```bash
codex plugin add skill-development@codex-plugins
```

## `shape-skill-change`

変更の段階に応じて、実装前のplanningと実装後のreviewを切り替えます。共通の境界基準だけをentrypointに置き、段階固有の手順は必要なreferenceだけを読みます。

### 実装前

依頼したworkflowと利用可能なSkillを比較し、次のどれが適切かを判断します。

- 既存Skillを更新する
- 既存Skillのreference、script、assetだけを拡張する
- 責務が混ざったSkillを分割する
- 新しいSkillを作る
- Skillを作らず、prompt、`AGENTS.md`、設定、connectorなど別の場所へ置く

### 実装後

実装されたSkill変更を次の観点でレビューします。

- descriptionと実際の責務がずれていないか
- 一つのSkillへ異なるworkflowを詰め込んでいないか
- 各指示が判断、制約、再現性を実際に改善しているか
- 条件付きの詳細をreferenceへ移せるか
- entrypoint、reference、兄弟Skill、`AGENTS.md`で規則が重複していないか
- 未使用のreference、script、asset、exampleが残っていないか

行数だけで肥大化を判定せず、各要素を`keep`、`move`、`merge`、`remove`として扱います。

### 向いている依頼

- 新しいworkflowをSkill化する価値があるか判断したい
- 既存Skillへ追加するか、別Skillにするか迷っている
- repo、user、pluginのどこへ置くか決めたい
- Skill Creatorへ渡す前に対象・非対象を明確にしたい
- 実装後に責務が広がったり、指示が増えすぎたりしていないか確認したい
- planningから実装、実装後reviewまで一貫した境界基準で進めたい

```text
$skill-development:shape-skill-change を使って、
PRレビューのworkflowを新しいSkillにするべきか判断し、実装後もレビューしてください。
```

### 成果物

実装前は判断結果、既存Skillとの比較、含める責務と含めない責務、Skill Creatorへ渡せる依頼文をまとめます。実装後は全体判定、具体的なfindings、維持すべき契約、必要な修正依頼をまとめます。このSkill自体は、Skillファイルを作成・変更しません。

!!! tip
    変更対象のSkillと編集内容が明確で、責務境界や実装後の肥大化を確認する必要がない場合は、このSkillを挟まず直接更新する方が適切です。

## `evaluate-skill-robustness`

明示的に承認したモデルとreasoning effortの組み合わせでSkillを実行し、最低限安定して動くprofileとモデル依存の失敗を報告します。高コストなworkflowのため、自動では起動しません。
