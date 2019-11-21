#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    na = len(a)
    nb = len(b)
    # dp[i][j]表示a[:i]和b[:j]的最大序列数
    dp = [[0] * (nb + 1) for _ in range(na + 1)]
    # path[i][j]表示获得dp[i][j]的方向
    path = [[0] * (nb) for _ in range(na)]
    ans = []
    for i in range(1,na + 1):
        for j in range(1,nb + 1):
            dp[i][j] = max(dp[i - 1][j - 1],dp[i - 1][j],dp[i][j - 1])
            if a[i - 1] == b[j - 1]:
                if dp[i - 1][j - 1] + 1 >= dp[i][j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    path[i - 1][j - 1] = 1
    #print('\n'.join(map(str,dp)))
    #print('\n'.join(map(str,path)))
    # 根据path重构可能的结果,类似bfs
    di = ((-1,-1),(0,-1),(-1,0))
    fromP = [(na - 1,nb - 1)]
    while len(ans) < dp[-1][-1]:
        #print(fromP)
        toP = []
        for p in fromP:
            if path[p[0]][p[1]] == 1:
                ans.append(a[p[0]])
                toP = {(p[0] - 1,p[1] - 1)}
                fromP = toP
                break
        if toP:
            continue
        for p in fromP:
            for d in di:
                if p[0] + d[0] >= 0 and p[1] + d[1] >= 0:
                    toP.append((p[0] + d[0],p[1] + d[1]))
        fromP = toP
    return ans[::-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
