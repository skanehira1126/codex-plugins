# `text-document-architect`の回帰ケース

重要な変更後に、起動条件と動作を軽量確認する。

lintの自動回帰テストは次で実行する。

```bash
python -m unittest discover -s evals -p 'test_*.py'
```

## 起動ケース

### 起動すべき

- 「この調査メモから、役員向けの意思決定メモをWordで作って」
- 「この報告書を、初見の人でも読み進められる構成に直して」
- 「このスライドを、出典付きの分析報告書へ変換して」
- “Turn these notes into a coherent analytical report with citations.”

### 起動すべきでない

- 「この内容を10枚のPowerPointにして」→ `presentation-architect`
- 「この一文を校正して」
- 「このメールを丁寧に書き直して」
- 「英語へ翻訳して」

## 動作ケース

### 高密度で平板な解説草稿

依頼：概念の一覧から2,000字の解説を作る。

必須動作：

- 全文を書く前に読者動線アウトラインを作る。
- 参照文書でない限り、定義だけの導入を避ける。
- 高密度の説明セクション間に、具体的な支えと統合を入れる。
- 装飾として修辞疑問を使わない。

### 意思決定メモ

必須動作：

- 求める判断と推奨案を早い位置へ出す。
- 推奨案の妥当性を、読み進める中心的な問いにする。
- 事実、解釈、仮説、提案を分ける。
- 結論を変え得るリスクを本文に残す。

### 参照マニュアル

必須動作：

- 物語的な引きより、定義、全体マップ、予測可能なナビゲーションを優先する。
- 解説記事向けの認知動線を強制しない。

### 分析報告書

必須動作：

- 発見を重要度順にする。
- 発見と離れた後半に考察をまとめず、根拠・解釈・含意を近づける。
- 代替説明と不確実性を、解釈へ影響する場所で示す。

## 回帰失敗の例

- すべてのセクションが同じ長さで、主な認知動作も「説明」である。
- 中立的な議題表が中心命題の代わりになっている。
- 箇条書きは整形されているが、項目間の関係が書かれていない。
- 結論を変える制約がAppendixにだけ書かれている。
- Word文書が必要なのに、編集可能な元ファイルを残さずPDFだけを納品する。

## lint回帰確認

```bash
python scripts/lint_text_document.py evals/sample-good-document.md --mode decision --check-sources
python scripts/lint_text_document.py evals/sample-bad-document.md --mode decision --check-sources
```

期待結果：

- `sample-good-document.md`：指摘なし。
- `sample-bad-document.md`：汎用見出し、箇条書きの壁、文章実況、抽象語、出典不足、説明動作の連続、意思決定の不在を検出する。
