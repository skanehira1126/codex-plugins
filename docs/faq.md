# よくある質問

## Skill名は毎回指定する必要がありますか？

必要ありません。依頼がSkillの発火条件に合えばCodexが選択します。特定のSkillを確実に使いたい場合や、挙動を比較したい場合は`$<plugin-name>:<skill-name>`を指定してください。

## プラグイン単位でインストールするのはなぜですか？

関連するSkillを用途ごとにまとめて配布しているためです。Python開発だけに使う場合は`python-coding`だけをインストールできます。

## 変更を公開前に試せますか？

はい。[ローカルcheckoutを試す](getting-started.md#local-checkout)の手順で、cloneしたディレクトリをMarketplaceとして登録できます。

## Skillが期待どおり選ばれません

まず、プラグインがインストール済みか確認します。

```bash
codex plugin list --marketplace codex-plugins
```

次に、依頼文へ完全なSkill名を含めて再実行してください。

```text
$python-coding:choose-effective-tests を使ってください。
```

それでも利用できない場合は、Marketplaceの登録先が意図したリポジトリまたはローカルcheckoutになっているか確認してください。

## 問題や改善案はどこへ報告しますか？

[GitHub Issues](https://github.com/skanehira1126/codex-plugins/issues)へ、利用したプラグイン名・Skill名と期待した結果を添えて報告してください。認証情報や個人情報は含めないでください。
