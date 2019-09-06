#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    pre = {}
    minDis = float('inf')
    n = len(a)
    for i in range(n):
        if a[i] in pre:
            minDis = min(minDis,i - pre[a[i]])
        pre[a[i]] = i
    if minDis < float('inf'):
        return minDis
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
