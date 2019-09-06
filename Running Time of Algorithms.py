#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    ans = 0
    n = len(arr)
    for i in range(1,n):
        c = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > c:
            arr[j + 1] = arr[j]
            ans += 1
            j -=1
        arr[j + 1] = c
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
