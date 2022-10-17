#!/bin/python
import sys


with open("test2.txt", "w") as f:
    f.write("test git compose\n")
    f.write(" ".join(sys.argv))
