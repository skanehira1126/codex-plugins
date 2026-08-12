# Python Coding

Pythonコードの設計、実装、テスト、レビュー、リファクタリングで使うプラグインです。Skillごとに対象を絞り、必要以上の抽象化、テスト、互換コードを増やさない判断を支援します。

## インストール

```bash
codex plugin add python-coding@codex-plugins
```

## Skill一覧

### `choose-code-boundaries`

関数、class、moduleなどの境界をどう置くか判断します。薄いhelper、処理を渡すだけのwrapper、状態を持たないManagerやServiceを増やす前に、責務を持つ最小の表現を選びます。

**向いている依頼**

- リファクタリング案をレビューする
- helperやclassへ分割するべきか判断する
- Service、Factory、Registryなどの導入が妥当か確認する

```text
$python-coding:choose-code-boundaries を使って、
この処理をclassへ分けるべきか判断し、必要なら実装してください。
```

### `choose-effective-tests`

変更された公開挙動と主要リスクを守る、必要十分なPythonテストを選びます。テスト件数やcoverageのためだけの重複、private実装への依存、過剰なmockを避けます。

**向いている依頼**

- バグ修正へ回帰テストを追加する
- 変更に必要なpytest・unittestを選ぶ
- 重複したテストやmock過多をレビューする

```text
$python-coding:choose-effective-tests を使って、
このバグ修正に必要な回帰テストを追加してください。
```

### `avoid-legacy-python-compatibility`

プロジェクトが宣言する最小Pythonバージョンを調べ、対象外の旧バージョン向けcompatibility codeを追加しないようにします。

**向いている依頼**

- typingや標準ライブラリの選択をレビューする
- backport、shim、fallbackが本当に必要か確認する
- `from __future__ import annotations`を追加・維持する理由を確認する

```text
$python-coding:avoid-legacy-python-compatibility を使って、
この変更をサポート対象のPythonだけに合わせて簡潔にしてください。
```

!!! note
    古いPythonを含むサポート範囲が明示されている場合は、その範囲に必要な互換処理を維持します。

### `polars-style`

Polarsの`select`、`with_columns`、`agg`でnamed expressionを使い、出力列名をDataFrameへ追加する側で指定します。

**向いている依頼**

- Polarsの変換処理を実装・修正する
- 動的な出力列名を扱う
- `.alias()`が増えた処理を整理する

```text
$python-coding:polars-style を使って、
このPolars変換をnamed expressionへ統一してください。
```

## どれを選ぶか

| 判断したいこと | Skill |
| --- | --- |
| コードをどこで分割するか | `choose-code-boundaries` |
| どのテストを追加するか | `choose-effective-tests` |
| 旧Python向け互換処理が必要か | `avoid-legacy-python-compatibility` |
| Polarsの列名をどう付けるか | `polars-style` |
