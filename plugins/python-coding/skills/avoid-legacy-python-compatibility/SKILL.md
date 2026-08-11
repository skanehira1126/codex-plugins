---
name: avoid-legacy-python-compatibility
description: >-
  Pythonコードの実装・修正・レビューで、プロジェクトがサポートする最小Pythonバージョンを基準に構文・標準ライブラリ・typing機能を選び、不要な互換import、backport、shim、fallback、version分岐を追加しない。`from __future__ import annotations`、`typing.List`、`typing.Optional`、`typing_extensions`、`tomli`、`sys.version_info`分岐などを追加・踏襲する可能性がある作業で使用する。旧Pythonを含む複数バージョン対応が明示されている場合も、実際のサポート範囲に必要な互換処理だけに限定する。
---

# Avoid Legacy Python Compatibility

## 原則

プロジェクトが宣言するPythonサポート範囲を契約として扱う。最小サポートバージョンで利用できる最も直接的な構文と標準ライブラリを使い、それより古いPythonのためのコードを追加しない。

互換コードは保険として入れない。対象バージョン、依存ライブラリ、実行時のannotation評価など、必要性を示す具体的な根拠がある場合だけ追加する。

## 手順

1. `pyproject.toml`の`requires-python`、package metadata、tox/nox、CI、Docker image、プロジェクト文書の順に確認し、サポート範囲を特定する。ローカルのPythonバージョンだけから推測しない。
2. 宣言が競合する場合は、配布metadataと実際のCI対象を優先して差異を報告する。判断に影響する範囲が特定できない場合は、既存の互換範囲を勝手に広げず確認する。
3. 最小サポートバージョンで利用できるnativeな構文、標準ライブラリ、typing機能を選ぶ。
4. 互換処理を追加する前に、どのサポート対象で何が失敗するか確認する。説明できなければ追加しない。
5. diffを読み、周辺コードから不要なlegacy boilerplateをコピーしていないことを確認する。

## 避けるもの

- boilerplateとしての`from __future__ import annotations`
- 標準ライブラリに存在する機能の不要な`typing_extensions`やbackport
- 最小サポートバージョンより古いPython向けの`try`/`except ImportError` fallback
- 不要な`sys.version_info`分岐、互換alias、shim
- サポート対象でnativeな型注釈を使える場合の旧式表現
- 「将来必要かもしれない」だけを根拠にした複数バージョン対応

## 代表的な置換

- 最小サポートがPython 3.9以上なら、`typing.List`、`typing.Dict`、`typing.Tuple`、`typing.Set`、`typing.Type`ではなく、`list`、`dict`、`tuple`、`set`、`type`のgenericを使う。
- 最小サポートがPython 3.10以上なら、`typing.Optional[T]`や`typing.Union[A, B]`ではなく、`T | None`や`A | B`を使う。
- `typing_extensions`からimportする各symbolが最小サポートバージョンの`typing`に存在し、必要な意味論を満たすなら、標準の`typing`からimportする。同名であることだけで置換せず、type checkerやframeworkがbackport固有の挙動を要求していないことを確認する。
- 最小サポートがPython 3.11以上でTOMLを読むだけなら、`tomli`ではなく`tomllib`を使う。`tomllib`は書き込みや書式保持を提供しないため、それらが必要な用途まで置換しない。

`from __future__ import annotations`は新規ファイルへ既定で追加しない。単なる慣習や、古いPython向けの型注釈互換を理由に追加しない。遅延評価の意味論が実行時に必要であり、別の直接的な表現より明確な場合だけ使用し、その理由を示す。

## 既存コードの扱い

変更対象に既存の互換コードがあっても、無関係な一括削除へ広げない。依頼範囲内で削除する場合は、最小サポートバージョン、runtime introspection、型検査、framework、依存ライブラリへの影響を確認する。特にannotationの評価方法を変えるimportは、`get_type_hints`などの利用箇所とテストを確認してから除く。

## 検証

- サポート範囲を示す設定と、選んだ構文・APIの対応を確認する。
- project標準のlint、type check、変更対象テストを実行する。
- 利用可能なら最小サポートバージョンでもテストする。
- 変更したファイルとdiffを検索し、新しいfuture import、backport、fallback、version分岐が根拠なく増えていないことを確認する。

## 完了条件

- 最小サポートバージョン未満のためだけのコードを追加していない。
- 追加または維持した互換処理は、対象バージョンと必要性を説明できる。
- `from __future__ import annotations`を慣習的に追加していない。
- 既存サポート範囲とruntime behaviorを意図せず変えていない。
