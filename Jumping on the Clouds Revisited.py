#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    ans = 100
    i = k % n
    while i > 0:
        if c[i] == 1:
            ans -= 3
        else:
            ans -= 1
        i = (i + k) % n
    if c[i] == 1:
        ans -= 3
    else:
        ans -= 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
