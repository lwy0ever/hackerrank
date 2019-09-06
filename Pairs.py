#!/bin/python3

import math
import os
import random
import re
import sys

''' if integer may not be unique
from collections import Counter
def pairs(k, arr):
    ans = 0
    cnt = Counter(arr)
    for key,val in cnt.items():
        ans += cnt[key + k]
    return ans
'''
# if integer will be unique
def pairs(k, arr):
    return len(set(arr) & set(x + k for x in arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
