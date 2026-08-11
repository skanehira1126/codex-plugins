---
name: polars-style
description: Polarsのnamed-expression実装規則。`pl.DataFrame` / `pl.LazyFrame` の `select`、`with_columns`、`agg`、動的な列生成、`pl.Expr` helperを実装・修正・レビューするときに使用する。出力名を呼び出し側で与え、`.alias()`の増殖を防ぐ。
---

# Polars Style

## Rules

- `select`、`with_columns`、`agg`ではnamed expressionを使う。
- 固定の出力列名は`output_name=expression`と書く。
- 動的な列名やPython identifierにできない列名は`**{output_name: expression}`と書く。
- `.alias()`は使わない。名前はexpressionではなく、それをDataFrameへ追加する呼び出し側で与える。
- `pl.Expr` helperは名前を埋め込まず、未命名のexpressionまたは`dict[str, pl.Expr]`を返す。
- 既存列をそのまま選ぶだけなら文字列指定を使ってよい。renameを伴う列と動的生成列はnamed expressionにする。
- 列順、key、dtype、null処理、行数を変更前後で維持する。意図的に変える場合はテストで示す。
- 長いexpressionは括弧と改行で整理し、意味のある中間列が必要なら段階的な`with_columns`に分ける。

## Examples

```python
df.with_columns(
    score=pl.col("value") * 2,
    **{dynamic_name: pl.col(source_name)},
)
```

```python
aggregations = {
    f"score_{window}": pl.col("score").mean()
    for window in windows
}
df.group_by("group_key").agg(**aggregations)
```

## Validation

- 変更対象で`.alias()`が増えていないことを確認する。
- プロジェクト標準のlintと変更対象テストを実行する。
- 列名、列順、dtype、key、null処理、行数、代表値を確認する。
