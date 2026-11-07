# Skill Development

Codex Skill変更の実装前にworkflowの責務と配置を整理し、既存Skillやplugin全体の重複、簡潔さ、検証をレビューするプラグインです。必要な場合は、モデルやreasoning effortによる実行差も明示的な承認のもとで評価できます。

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

### 既存Skill・pluginと実装後のレビュー

対象Skillと必要な参照先を確認し、plugin全体の依頼では各Skillを次の観点でレビューします。

- descriptionと実際の責務がずれていないか
- 一つのSkillへ異なるworkflowを詰め込んでいないか
- 各記述を削ったとき、どの判断・操作・成果物が悪くなるか
- 条件付きの詳細だけを読む経路があるか。分割後も全ファイルを読んでいないか
- entrypoint、reference、兄弟Skill、`AGENTS.md`で規則が重複していないか
- 未使用のreference、script、asset、exampleが残っていないか

行数だけで肥大化を判定せず、各要素を`keep`、`move`、`merge`、`remove`として扱います。
descriptionは主要な用途を先に示し、細かい手順は本文へ置きます。固有の制約、発火境界、
テンプレートの出力契約を保ち、問題のないSkillまで一律に書き換えません。

変更に合う代表依頼と検証を選び、静的な整合性確認と実行で観測した挙動を区別します。
validator通過や明示呼び出しだけで暗黙発火を検証済みとせず、短縮による品質・速度の
改善を主張する場合は、版と実行条件をそろえた比較を使います。

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

実装前は判断結果、既存Skillとの比較、責務、検証案、Skill Creatorへ渡せる依頼文をまとめます。レビューでは全体判定、具体的な指摘、維持すべき契約、検証結果と未確認範囲、必要な修正依頼をまとめます。このSkill自体は、Skillファイルを作成・変更しません。実装も依頼されていれば、Skill Creatorで編集した後に再確認します。

!!! tip
    変更対象のSkillと編集内容が明確で、責務境界や実装後の肥大化を確認する必要がない場合は、このSkillを挟まず直接更新する方が適切です。

## `evaluate-skill-robustness`

対象Skillと利用可能なprofileをread-onlyで確認して推奨matrixと最大run数を提示し、明示的な
承認後にモデルとreasoning effortの組み合わせを実行します。最低限安定して動くprofileと
モデル依存の失敗を報告します。高コストなworkflowのため、自動では起動しません。
対象Skillと参照先の版、入力、実行条件を記録し、明示呼び出しによる実行と暗黙選択の
評価を区別します。未実施の評価や未取得の計測値は、未確認として報告します。

## 設計方針の参考資料

- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)：用途の境界、簡潔な本文、補助リソース、代表依頼による確認。
- [Codex: Skills](https://developers.openai.com/codex/skills)：descriptionによる選択と段階的な読み込み。
- [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)：観測可能な成功条件と実行記録による比較。
