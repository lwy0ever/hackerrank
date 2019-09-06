#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    ns = len(s)
    nt = len(t)
    commonLength = 0
    while commonLength < ns and commonLength < nt:
        if s[commonLength] == t[commonLength]:
            commonLength += 1
        else:
            break
    #print(k,ns,nt,commonLength)
    if k - (ns - commonLength) - (nt - commonLength) >= 0:
        if k - ns - nt >= 0 or (k - ns - nt < 0 and (k - (ns - commonLength) - (nt - commonLength)) % 2 == 0):
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
