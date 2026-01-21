# Example of "ZXing.Net" for IronPython (.NET 8.0)

このプロジェクトは、バーコード読み取りライブラリである ZXing.Net を IronPython (.NET 8.0) からシームレスに利用するためのブリッジパッケージを作成する例です。

## 主な特徴

* **.NET 8.0 対応**: `net8.0-windows` ターゲットで構成されており、最新のランタイムで動作します。
* **互換性レイヤーの統合**: `.NET 6` 以降で変更された `System.Drawing` の挙動を `ZXing.Windows.Compatibility` を通じて解決しています。
* **簡単導入**: C# 側でビルドした DLL 群と Python スクリプトを同じフォルダに配置するだけで、IronPython から `import zxing` として利用可能です。

## 実行のための準備

### 1. 環境変数の設定

IronPython がインストールされているパスを環境変数 `IRONPYTHON_HOME` として設定してください。
（例: `C:\Program Files\IronPython 3.4`）

### 2. ビルド

1. `ExampleOfZXingDotNET.slnx` を Visual Studio 2022 等で開きます。
2. プロジェクトをビルドします。
* `CopyLocalLockFileAssemblies` が `true` に設定されているため、ビルド時に必要な NuGet パッケージ（`zxing.dll` 等）がすべて出力ディレクトリに集約されます。

### 3. インストール

1. ビルド出力ディレクトリ（例: `bin/Release/net8.0-windows/`）にあるファイル一式を、IronPython の `Lib` フォルダ内、またはプロジェクトの参照用パスに `zxing` という名前のフォルダを作成してコピーします。
2. この際、フォルダ内に `__init__.py` が含まれていることを確認してください。

## 利用方法

Python スクリプトから以下のように呼び出します。

```python
# -*- coding: utf-8 -*-
import zxing
from System.Drawing import Bitmap

# 画像の読み込み
image_path = "path/to/barcode.png"
img = Bitmap(image_path)

# 互換版のReaderを取得してデコード
reader = zxing.getReader()
result = reader.Decode(img)

if result is not None:
    print("Format: {0}".format(result.BarcodeFormat.ToString()))
    print("Text  : {0}".format(result.Text))
else:
    print("Decode failed.")

```

## ファイル構成

* `ExampleOfZXingDotNET.slnx`: ソリューションファイル。
* `ExampleOfZXingDotNET.csproj`: プロジェクトファイル。NuGet パッケージの管理と出力設定を行います。
* `__init__.py`: IronPython 用のパッケージ初期化スクリプト。DLL のロードとヘルパー関数の提供を行います。
* `examples/`: 動作確認用のサンプルプログラムとテスト画像が含まれます。