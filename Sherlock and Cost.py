#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    # dp[i][0]表示第i位取1时,最大s
    # dp[i][1]表示第i位取B[i]时,最大s
    n = len(B)
    dp = [[0,0] for _ in range(n)]
    for i in range(1,n):
        # A[i - 1]取1,A[i]取1
        # 或者
        # A[i - 1]取B[i - 1],A[i]取1
        dp[i][0] = max(dp[i - 1][0],dp[i - 1][1] + B[i - 1] - 1)
        # A[i - 1]取B[i - 1],A[i]取B[i]
        # 或者
        # A[i - 1]取1,A[i]取B[i]
        dp[i][1] = max(dp[i - 1][1] + abs(B[i] - B[i - 1]),dp[i - 1][0] + B[i] - 1)
    return max(dp[-1][0],dp[-1][1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
