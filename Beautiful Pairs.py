#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    cntA = Counter(A)
    cntB = Counter(B)
    length = len(A)
    common = cntA & cntB
    if sum(common.values()) < length:
        ans = sum(common.values()) + 1
    else:
        ans = length - 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
