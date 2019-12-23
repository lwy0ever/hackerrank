#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the misereNim function below.
def misereNim(s):
    # 类似 https://www.hackerrank.com/challenges/nim-game-1/copy-from/134859922
    if set(s) == {1} and len(s) & 1 == 0:
        return 'First'
    if set(s) == {1} and len(s) & 1 == 1:
        return 'Second'
    ans = 0
    for p in s:
        ans ^= p
    if ans:
        return 'First'
    else:
        return 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
