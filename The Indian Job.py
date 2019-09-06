#!/bin/python3

import os
import sys

#
# Complete the indianJob function below.
#
def indianJob(g, arr):
    #
    # Write your code here.
    #
    s = sum(arr)
    if g >= s:
        return 'YES'
    if g * 2 < s:
        return 'NO'
    n = len(arr)
    mi = s - g
    ma = g
    # dp[i][j]表示数组的前j个，可以形成一个子数组，使总和为i
    dp = [[False] * (n + 1) for i in range(g + 1)]
    for j in range(n + 1):
        dp[0][j] = True # 0是一定可以组成的
    for i in range(1,g + 1):
        dp[i][0] = False    # 空数组什么都组成不了
    for i in range(1,g + 1):
        for j in range(1,n):
            dp[i][j] = dp[i][j - 1] # 前j－1个可以组成，前j个也能组成（不使用第j个元素即可）
            if i >= arr[j]:
                # 或者前j－1个元素组成了i－arr[j]，加入arr[j]以后就组成了i
                dp[i][j] = dp[i][j] | dp[i - arr[j]][j - 1]
            if i >= mi and dp[i][j]:
                return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ng = input().split()

        n = int(ng[0])

        g = int(ng[1])

        arr = list(map(int, input().rstrip().split()))

        result = indianJob(g,arr)

        fptr.write(result + '\n')

    fptr.close()
