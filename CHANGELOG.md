# Changelog

このリポジトリで配布するpluginのrelease noteを記録する。2026-08-30以降はこのファイルを
release noteの正本とし、既存のskill別changelogは過去履歴として保持する。

## 2026-08-30

### document-authoring 0.4.0

- `presentation-architect`をargument-led、learning-led、update-ledの構造profileへ対応させ、
  意思決定を必要としないdeckへ推奨案、緊張、exact ask、Q&A Appendixを強制しないようにした。
- `text-document-architect`をsequential、learning、lookup/referenceの構造profileへ対応させ、
  参照・検索文書では論証やreader-state narrativeより検索経路、分岐、例外を優先するようにした。
- brief、outline、rubric、lint、回帰case、利用者向け文書を新しいprofileへ揃えた。
- 固定pass、固定点数目標、Appendix不作成理由、低文脈読者、未依頼のdual-format納品を
  必須契約から外し、規模、対象読者、指定形式に応じるようにした。
- cross-artifactな`revision-hygiene`を独立pluginへ移し、Document Authoringを文章と
  スライドのarchitectureへ限定した。

### document-authoring 0.3.1

- `presentation-architect`と`text-document-architect`の重複する詳細を既存referenceへ統合し、
  発火条件、mode、出力契約を維持した。
- `revision-hygiene`へ、重複解消時の正本、routing、残存callerの扱いを追加した。

### python-coding 0.3.1

- `avoid-legacy-python-compatibility`のfuture annotations基準を一箇所へ集約した。
- `choose-effective-tests`の停止条件と完了条件を、保証を維持した一つのchecklistへ統合した。
- Python support contractの正本、抽象化境界、private helper testを、固定gateではなく
  project、framework、riskの具体的な根拠で判断するようにした。
- `polars-style`のnamed expressionと`.alias()`禁止は、一貫した可読性規則として維持した。

### skill-development 0.4.1

- `evaluate-skill-robustness`の採点、failure分類、capability-floorの詳細をrubricへ集約した。
- `shape-skill-change`へ、挙動維持の統合と挙動変更を分けるreview順序、および正本指定を追加した。
- `evaluate-skill-robustness`はread-onlyのscoping後に実行matrixの承認を取り、report言語は
  利用者と上位instructionに従うようにした。

### revision-hygiene 0.1.0

- review-driven revisionで、却下・削除された概念を不要なtest、comment、guard、互換層、
  注記として残さず、現在の公開契約と重大リスクを守るcross-artifact overlayを追加した。
