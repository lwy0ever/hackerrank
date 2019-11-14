#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the mandragora function below.
def mandragora(H):
    n = len(H)
    H.sort()
    total = sum(H)
    ans = 0
    for i in range(n):
        t = (1 + i) * total
        if t > ans:
            ans = t
        else:
            break
        total -= H[i]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        H = list(map(int, input().rstrip().split()))

        result = mandragora(H)

        fptr.write(str(result) + '\n')

    fptr.close()
