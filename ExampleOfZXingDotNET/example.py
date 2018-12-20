# -*- coding: utf-8 -*-

"""
Example of ZXing.Net (for 64bit)
"""

from zxing import *

def RunExample():
    img = Bitmap(path.join(IPY_ZXING, "qrcode.gif"))
    reader = ZXing.BarcodeReader()
    result = reader.Decode(img)
    if result != None:
        print(result.BarcodeFormat.ToString())
        print(result.Text)

if __name__ == '__main__':
    RunExample()