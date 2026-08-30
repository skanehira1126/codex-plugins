# Text Document Architect 保守ガイド

このSkillは、文章中心の業務文書について、**連続読解・学習・検索参照に合う構造、根拠、情報配置、指定形式の成果物**を一つのワークフローとして扱います。

## この版の重要な方針

1. 本文は、対象読者が目的を達成するための最短かつ十分な読解経路にする。
2. 調査可能な事実は自分で確認し、安全に補えない重要な判断だけをユーザーへ確認する。
3. 説明・断定だけを連続させず、読者の認知動作を切り替える。
4. 規模に応じて、骨格、接続、根拠、読者動作または検索経路、圧縮を分けて確認する。
5. 候補情報を、本文、表／コールアウト、注記、Appendix、削除へ振り分ける。
6. 結論を変え得るリスクや前提をAppendixへ隠さない。
7. 指定形式を守り、改訂時は既存の編集可能な構造を不用意に失わない。

## ディレクトリ構成

```text
text-document-architect/
├── SKILL.md                       # 実行時の中核指示
├── README.md                      # この保守ガイド
├── CHANGELOG.md                   # 変更履歴
├── agents/openai.yaml             # UI表示と既定プロンプト
├── assets/                        # 設計・レビュー用テンプレート
├── references/                    # 判断基準と詳細規則
├── scripts/                       # 構成のヒューリスティック検査
└── evals/                         # 回帰ケースとサンプル
```

## 変更するときの原則

### テキスト文書側だけで完結させる

このSkillは`presentation-architect`へ実行時依存しません。共通に見える原則も、このSkill内に文章文書向けの形で記述しています。文章固有の変更がスライドSkillへ波及しないことを優先します。

### 変更ごとに正本を一つ決める

ルールを変更するときは詳細の正本を一つ決め、他surfaceには同義の説明ではなく、
routing、そのsurface固有の契約、または回帰確認だけを残します。影響範囲として次を確認します。

1. `SKILL.md`：常時必要なroutingと不変条件
2. `references/`：条件付きの判断基準と具体策
3. `evals/cases.md`：利用者から観測できる回帰

テンプレートの入力項目が変わる場合は`assets/`も更新します。機械的に検査できる場合は`scripts/`へ追加します。

## 用語

- **読者動作**：状況把握、問い、観察、説明、再解釈、評価、判断、行動、統合など、読者の頭に求める主な処理
- **認知的なメリハリ**：文の見た目ではなく、読者動作と抽象度を意図的に変えること
- **主経路**：対象読者が目的を達成するために、本文で順番に読む必要がある内容
- **Appendix**：検証、再利用、専門的な深掘りには有用だが、主経路には不要な詳細
- **文章の実況**：「次に説明します」など、対象について新しい関係を伝えない進行報告

## ローカル確認

### Python構文確認

```bash
python -m py_compile scripts/lint_text_document.py
```

### 自動回帰テスト

```bash
python -m unittest discover -s evals -p 'test_*.py'
```

### 良いサンプルの検査

```bash
python scripts/lint_text_document.py evals/sample-good-outline.md --mode decision --check-sources
```

### 悪いサンプルの検査

```bash
python scripts/lint_text_document.py evals/sample-bad-outline.md --mode decision --check-sources
```

日本語オプションも使えます。

```bash
python scripts/lint_text_document.py evals/sample-bad-outline.md --モード 意思決定 --出典確認
```

このlintはヒューリスティックです。注意箇所を絞り込むもので、論理、事実性、読みやすさ、成果物品質を完全に証明するものではありません。

## バージョニング

- 文章表現や例の軽微な修正：パッチ
- 品質ゲート、テンプレート項目、lint規則の意味変更：マイナー
- ワークフローや責務の大幅変更：メジャー
