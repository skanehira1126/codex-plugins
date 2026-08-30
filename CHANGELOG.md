# Changelog

このリポジトリで配布するpluginのrelease noteを記録する。2026-08-30以降はこのファイルを
release noteの正本とし、既存のskill別changelogは過去履歴として保持する。

## 2026-08-30

### document-authoring 0.3.1

- `presentation-architect`と`text-document-architect`の重複する詳細を既存referenceへ統合し、
  発火条件、mode、出力契約を維持した。
- `revision-hygiene`へ、重複解消時の正本、routing、残存callerの扱いを追加した。

### python-coding 0.3.1

- `avoid-legacy-python-compatibility`のfuture annotations基準を一箇所へ集約した。
- `choose-effective-tests`の停止条件と完了条件を、保証を維持した一つのchecklistへ統合した。

### skill-development 0.4.1

- `evaluate-skill-robustness`の採点、failure分類、capability-floorの詳細をrubricへ集約した。
- `shape-skill-change`へ、挙動維持の統合と挙動変更を分けるreview順序、および正本指定を追加した。
