# Python CLIの構成

新規CLIでは、`argparse`のサブパーサーに`set_defaults(func=実行関数)`で関数を登録し、共通入口で`func(**kwargs)`を呼ぶ形を優先する。既存CLIを変更するときは、採用済みのframeworkや公開挙動を尊重し、この形への移行は依頼範囲に含まれる場合だけ行う。

## 登録と実行の責務

- 各コマンドの引数定義と実行関数の登録を近くに置く。共通入口にコマンド名の`if` / `elif`や`match`を追加して振り分けない。
- 実行関数は必要な値を明示した引数で受ける。CLI全体の`Namespace`を渡すことや、不要な引数を吸収するだけの`**kwargs`を既定にしない。
- `vars(parser.parse_args(argv))`で辞書に変換し、`func`を取り出してから残りをキーワード引数として渡す。ログ設定など入口だけで使う値も、共通処理で消費して取り除く。
- `add_argument`の`dest`と実行関数の引数名を一致させる。`--output-dir`は通常`output_dir`になる。型注釈だけではCLI入力は変換されないため、必要な`type`や`choices`をparserに指定する。
- `set_defaults`には、同じ実行関数を複数コマンドで使うための固定値も登録できる。共通入口が消費するものを除き、登録した値は関数の引数として受けられるようにする。

小規模なら同じファイルにまとめる。コマンド群が増えたら、群ごとにparserを組み立てる関数と実行関数をモジュールへ置き、rootの`build_parser()`で組み合わせる。共通入口は引数解析、必要な共通初期化、関数呼び出しを担う。

## 最小例

Python 3.10以上を想定した、2つのコマンドで共通入口を使う例。

```python
import argparse


def cli_greet(name: str, upper: bool) -> None:
    message = f"Hello, {name}!"
    print(message.upper() if upper else message)


def cli_add(left: int, right: int) -> None:
    print(left + right)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="example")
    subparsers = parser.add_subparsers()

    greet = subparsers.add_parser("greet", help="挨拶を表示する")
    greet.add_argument("name")
    greet.add_argument("--upper", action="store_true")
    greet.set_defaults(func=cli_greet)

    add = subparsers.add_parser("add", help="整数を加算する")
    add.add_argument("left", type=int)
    add.add_argument("right", type=int)
    add.set_defaults(func=cli_add)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    kwargs = vars(parser.parse_args(argv))
    func = kwargs.pop("func", None)
    if func is None:
        parser.print_help()
        return
    func(**kwargs)


if __name__ == "__main__":
    main()
```

この例では未指定時にヘルプを表示して正常終了する。コマンド必須のCLIでは`add_subparsers(required=True)`で不足を引数エラーにする。既存CLIの終了コードやヘルプの表示先は維持する。

## 拡張時の注意

- ネストしたサブコマンドでも、実行する末端のparserに関数を登録する。各階層で子コマンドを必須にするか、途中までの指定時にヘルプを出すかを決める。`add_subparsers(dest="command")`などでコマンド名を保存した場合は、関数へ渡す前にその管理用の値も取り除く。
- 共通ログ設定や例外から終了コードへの変換は、必要な契約がある場合に入口へまとめる。未知の例外まで一括で成功扱いにしない。ハンドラーが終了コードを返す設計なら、入口から返し、スクリプト起動時は`raise SystemExit(main())`で反映する。
- 共通入口で未知のキーワードを黙って捨てたり、signatureの自動解析で引数不一致を隠したりしない。parserと関数の対応を修正する。

## 確認する挙動

代表的なコマンドを共通入口から実行し、出力や副作用を確認する。異なる引数を持つ別のコマンドでも正しく動き、管理用の値が実行関数へ漏れないことを確認する。`--help`、サブコマンド未指定、必須引数不足、不正な型について、表示と終了コードを確認する。ネストや共通オプションを追加した場合は、その経路も含める。

## 参考資料

- [Python公式: argparseのサブコマンド](https://docs.python.org/3/library/argparse.html#sub-commands): `set_defaults`による実行関数の登録。通常の適用でリンク先を読み込む必要はない。
