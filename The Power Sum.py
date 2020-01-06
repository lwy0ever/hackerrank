#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N):
    d = {}
    def helper(x,n,start):
        if (x,n,start) in d:
            return d[(x,n,start)]
        if x == 0:
            return 1
        ans = 0
        st = start
        while st ** n <= x:
            h = helper(x - st ** n,n,st + 1)
            ans += h
            st += 1
        d[(x,n,start)] = ans
        return ans
    return helper(X,N,1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
