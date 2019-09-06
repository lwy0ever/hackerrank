#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    ans = arr[1] - arr[0]
    for i in range(1,len(arr) - 1):
        #print(arr[i + 1],arr[i])
        if arr[i + 1] - arr[i] < ans:
            ans = arr[i + 1] - arr[i]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
