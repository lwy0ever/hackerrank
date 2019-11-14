#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    arr.sort()
    
    n = len(arr)
    ans = 0

    def dfs(cs,i,s):    # 之前已经累积了s,现在从cs[i]开始尝试
        nonlocal ans
        if s - k > 0:
            return
        if k - s < k - ans:
            ans = s

        for j in range(i,n):
            if s + cs[j] - k > abs(ans - k):
                break
            dfs(cs,j,s + cs[j])
    dfs(arr,0,0)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
