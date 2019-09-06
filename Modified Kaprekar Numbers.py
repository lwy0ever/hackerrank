#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    ans = []
    for x in range(p,q + 1):
        rLen = 10 ** math.ceil(math.log10(x + 1))
        if (x ** 2 % rLen) + (x ** 2 // rLen) == x:
            ans.append(x)
    print(' '.join(map(str,ans)) if ans else 'INVALID RANGE')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
