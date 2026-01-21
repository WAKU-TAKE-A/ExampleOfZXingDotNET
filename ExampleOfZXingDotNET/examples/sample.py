# -*- coding: utf-8 -*-
from pathlib import Path
import zxing

CURRENT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = CURRENT_DIR / "qrcode.gif"

def run():
    print("Testing ZXing with .NET 8.0 Assets...")
    if not IMAGE_PATH.exists():
        print("Error: Image not found: {0}".format(IMAGE_PATH))
        return

    # Bitmapの読み込み
    img = zxing.Bitmap(str(IMAGE_PATH))
    
    # パッケージのヘルパー関数を使用してReaderを取得
    reader = zxing.getReader()
    result = reader.Decode(img)
    
    if result is not None:
        print("Format: {0}".format(result.BarcodeFormat.ToString()))
        print("Text  : {0}".format(result.Text))
    else:
        print("Decode failed.")

if __name__ == '__main__':
    run()
