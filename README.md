# Example of "ZXing.Net" (for 64bit)

Example of "ZXing.Net" in Ironpython script.  
The library of C# is used.

## File

* "ExampleOfZXingDotNET.sln"
  * To install "ZXing.Net".
  * To generate "zxing" package.

## Notes on execution

* Open "ExampleOfZXingDotNET.sln".
* Install "ZXing.Net" with NuGet.
* Build.
* Copy the "x64/debug/zxing" or "x64/release/zxing" folder to IronPython's "Lib" folder.
* Environment variable "IRONPYTHON_HOME" is required. It is the installation location of IronPython.
* "example.py" and "example.exe" are example program.

```
import zxing
import example

example.RunExample()
```