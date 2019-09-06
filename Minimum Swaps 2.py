#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    i = 0
    s = 0
    while i < len(arr):
        if arr[i] != i + 1:
            p = arr[i]
            arr[i],arr[p - 1] = arr[p - 1],arr[i]
            #print(arr)
            s += 1
        else:
            i += 1
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
