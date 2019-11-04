#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    n = len(arr)
    mSubarray = arr[0]
    maxSubarray_ending_here = 0
    mSubsequence = float('-inf')
    for a in arr:
        maxSubarray_ending_here = max(a,maxSubarray_ending_here + a)
        mSubarray = max(mSubarray,maxSubarray_ending_here)
        mSubsequence = max(mSubsequence,a,mSubsequence + a)
    return mSubarray,mSubsequence

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
