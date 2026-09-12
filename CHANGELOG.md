# Changelog

このリポジトリで配布するpluginのrelease noteを記録する。2026-08-30以降はこのファイルを
release noteの正本とし、既存のskill別changelogは過去履歴として保持する。

## 2026-09-12

### agent-coordination 0.4.0

- `coordinate-subagent-work`の発火条件を、委譲が依頼された、またはこのSkillとは別に決まった場面へ限定した。並列化できる作業があるだけでは選択せず、Skillの読み込みを起動理由にしない。
- 委譲時の担当範囲、編集衝突の防止、検証・統合、実行権限の境界を維持し、呼び出し文と利用者向け説明を新しい発火条件へ揃えた。
- `delegate-work-in-stages`の承認単位を内部工程から依頼されたタスクへ変更した。合意した範囲の実装・検証・必要な修正は、工程をまたいで完了まで進める。
- メインエージェントが実装判断と並行する会話を担い、途中経過の共有と承認待ちを分けた。議論中の案と実装指示を区別し、明示された方向転換を担当へ反映する。
- 未承認の目的・範囲変更、ユーザー固有の重要な選択、指定された確認地点では、回答に依存する作業だけを待機させる。明示起動専用の設定、呼び出し名、基本委譲の所有権・実行権限を維持した。

## 2026-09-05

### agent-coordination 0.2.1

- 委譲不可時のローカル実行と、承認済み段階の扱いを明確化した。次段階の承認は維持し、理由を該当規則で示す。
- 利用者向け文書で、通常の委譲と明示呼び出し限定の段階的委譲を区別した。

### document-authoring 0.5.0

- 通常の作成依頼では設計から成果物検証まで進め、参照先の不要な設計承認前提を解消した。
- 成果物生成後は影響のある評価軸を再確認する。採点基準、必須構造、ハードゲート、形式固有QAは維持した。

### python-coding 0.4.0

- `choose-effective-tests`の追加候補を探し尽くす完了条件を除き、変更と主要リスク、必須checkを検証範囲とした。UIからの呼び出しも既存テストの再利用を含めた。

### skill-development 0.5.0

- 実装まで依頼された作業のphase間継続と、関連箇所の再レビューを明確化した。
- 高コスト評価は具体的なmatrixの承認を維持し、同じ評価への既存承認、後続編集、追加trialの予算を区別した。

変更根拠（2026-09-05本文確認）：[GPT-6 Astra: Prompting best practices](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices)の自律実行、skillとの指示競合、停止理由、検証範囲。[AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)の読み込み範囲と優先順位、[Build skills](https://learn.chatgpt.com/docs/build-skills)の構成・description・段階的読み込みも照合し、既存の識別子、発火条件、参照構造を維持した。

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
