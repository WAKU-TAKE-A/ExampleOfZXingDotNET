# -*- coding: utf-8 -*-

"""
ZXingDotNET for IronPython (.NET 8.0)
"""

__author__  = "Nishida Takehito <takehito.nishida@gmail.com>"
__version__ = "0.9.8.0"
__date__    = "2026/01/18"

from pathlib import Path
from sys import path as systemPath
from System import Environment as env

IRONPYTHON_HOME = env.GetEnvironmentVariable("IRONPYTHON_HOME")
if IRONPYTHON_HOME is None:
    raise Exception("Error : Set path of IRONPYTHON_HOME.")

CURRENT_DIR = Path(__file__).resolve().parent
IRONPYTHON_HOME_PATH = Path(IRONPYTHON_HOME)

_lstPath = [
    IRONPYTHON_HOME_PATH / "Lib",
    IRONPYTHON_HOME_PATH / "DLLs",
    CURRENT_DIR
]

for i in _lstPath:
    if not i.exists():
        raise FileNotFoundError("Required directory not found: {0}".format(i))
    if str(i) not in systemPath:
        systemPath.append(str(i))

import clr

# 出力されたDLL群を優先的に参照し、ランタイムの不整合を防ぐ
dlls = [
    "System.Drawing.Common.dll",
    "zxing.dll", 
    "ZXing.Windows.Compatibility.dll"
]

for dll in dlls:
    dll_path = CURRENT_DIR / dll
    if dll_path.exists():
        clr.AddReferenceToFileAndPath(str(dll_path))

import ZXing
import ZXing.Windows.Compatibility
from System.Drawing import Bitmap

def getReader():
    """互換版のBarcodeReaderを返します"""
    return ZXing.Windows.Compatibility.BarcodeReader()
