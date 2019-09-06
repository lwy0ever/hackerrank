#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    n = len(arr)
    ans = []
    mi = float('inf')
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > mi:
            continue
        else:
            if arr[i + 1] - arr[i] < mi:
                mi = arr[i + 1] - arr[i]
                ans.clear()
            ans.append(arr[i])
            ans.append(arr[i + 1])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
