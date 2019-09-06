#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
from collections import Counter
def equalizeArray(arr):
    cnt = Counter(arr)
    ma = 0
    ans = 0
    for c in cnt.values():
        if c > ma:
            ans += ma
            ma = c
        else:
            ans += c
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
