#!/bin/python3

import os
import sys

#
# Complete the bricksGame function below.
#
def bricksGame(arr):
    #
    # Write your code here.
    #
    # dp[i] 表示玩家在第i个数进行决策时，所能拿到的和的最大值
    # sum[i] 表示 a[i]+a[i+1]+....+a[n]
    # 转移方程:dp[i] = max(sum[i] - dp[i + 1],sum[i] - dp[i + 2],sum[i] - dp[i + 3])
    # 也就是说,当面临a[i]...a[n]的选择时,有3种选择:
    # 1,选择1个,a[i],那么对手的得分为dp[i + 1],我的得分为sum[i] - dp[i + 1]
    # 2,选择2个,a[i]和a[i + 1],那么对手的得分为dp[i + 2],我的得分为sum[i] - dp[i + 2]
    # 3,选择3个,a[i]..a[i + 2],那么对手的得分为dp[i + 3],我的得分为sum[i] - dp[i + 3]
    n = len(arr)
    if n <= 3:
        return sum(arr)
    dp = [0] * n
    dp[-1] = arr[-1]
    dp[-2] = dp[-1] + arr[-2]
    dp[-3] = dp[-2] + arr[-3]
    s = dp[-3]
    for i in range(n - 4,-1,-1):
        s += arr[i]
        dp[i] = max(s - dp[i + 1],s - dp[i + 2],s - dp[i + 3])
    return dp[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
