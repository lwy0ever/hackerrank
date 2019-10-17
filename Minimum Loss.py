#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
from bisect import bisect,insort
def minimumLoss(price):
    ans = 10 ** 16 + 1
    pre = []
    for i,p in enumerate(price):
        pos = bisect(pre,p)
        if pos < i:
            ans = min(ans,pre[pos] - p)
        insort(pre,p)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
