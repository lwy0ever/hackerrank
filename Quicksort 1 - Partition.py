#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    n = len(arr)
    p = arr[0]
    l = 1
    r = n - 1
    while l < r:
        while l < n and arr[l] < p:
            l += 1
        while r >= 0 and arr[r] > p:
            r -= 1
        if l < r:
            arr[l],arr[r] = arr[r],arr[l]
        #print(l,r)
    arr[0],arr[l - 1] = arr[l - 1],arr[0]
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
