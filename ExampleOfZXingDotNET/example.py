# -*- coding: utf-8 -*-

"""
Example of R.Net (for 64bit)
"""

import os.path as path
import sys
import clr
clr.AddReferenceByPartialName("System.Windows.Forms")
from System.Windows.Forms import MessageBox

import rdotnet as r

def RunExample():
    #
    # Example of NumericMatrix.
    #
    mat = r.evaluate("mat <- matrix(1:100, nrow=10)", "numeric")
    print(type(mat))
    #
    # Example of NumericVector.
    #
    vec = r.evaluate("vec <- rnorm(1000)", "numeric")
    hst = r.evaluate("hst <- hist(vec)", "list")
    hst_counts = r.asNumeric(hst["counts"])
    print(list(hst_counts))
    MessageBox.Show("Push Ok.", "Example of hist()")
    r.evaluate("dev.off()")
    #
    # Example of DataFrame.
    #
    fn = path.join(r.IPY_RDOTNET, 'example.csv')
    csv = r.evaluate("csv <- read.csv('" + fn.replace("\\", "/") + "', stringsAsFactors=F)", "dataframe")
    msg = "Name : \r\n" + str(list(csv["Name"])) + "\r\nHeight : \r\n" + str(list(csv["Height"]))
    MessageBox.Show(msg, "Read example.csv")
    #
    # Example of Function.
    #
    fncc_str = "func <- function(var){ var + 10 }"
    func = r.eval(fncc_str, "function")
    vec2 = r.eval("vec2 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)")
    ret = r.runFunction(func, [vec2], "numeric")
    MessageBox.Show(fncc_str + "\r\n " + str(list(ret)), "Example of function")

if __name__ == '__main__':
    RunExample()

