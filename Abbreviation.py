#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    # https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    m, n = len(a), len(b)
    dp = [[True]*(m+1)] + [[True] + [False]*(m) for _ in range(n)]
    #print(dp)
    #dp[0][0] = True
    #print(a,b)
    for i in range(n):
        for j in range(i,m):
            if a[j] == b[i]:    # upper == upper
                dp[i + 1][j + 1] = dp[i][j]
            elif a[j].upper() == b[i]:  # lower == upper
                # when dp[i][j] is True, capitalize a[j]
                # when dp[i + 1][j] is True, delete a[j]
                dp[i + 1][j + 1] = dp[i][j] or dp[i + 1][j]
            elif a[j].islower():        # lower != upper
                dp[i + 1][j + 1] = dp[i + 1][j]
    #for d in dp:
    #    print(d)
    return "YES" if dp[n][m] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
