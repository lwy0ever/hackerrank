#!/bin/python3

import os
import sys

#
# Complete the playWithWords function below.
#
def playWithWords(s):
    #
    # Write your code here.
    #
    # dp[i][j]表示s[i:j + 1]中回文子序列的长度
    # 状态初始条件:dp[i][i] = 1
    # 状态转移方程:
    # 如果str[i] == str[j],dp[i][j] = dp[i + 1][j - 1] + 2
    # 如果str[i] != str[j],dp[i][j] = max(dp[i + 1][j],dp[i][j - 1])
    # 外层循环j,从小到大
    # 内层循环i,从大到小(从j - 1到0)
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for j in range(1,n):
        for i in range(j - 1,-1,-1):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j],dp[i][j - 1])
    # 将s分成2部分,s[:m]和s2[m:],取dp[0][m - 1] * dp[m][n - 1]的最大值
    ans = 0
    for i in range(1,n - 1):
        ans = max(ans,dp[0][i - 1] * dp[i][n - 1])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()
