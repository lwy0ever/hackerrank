#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    dp = [0] * (n + 1)
    for coin in c:
        if coin > n:    #if coin > value, there's no reason to use it
            continue
        dp[coin] += 1   #coin by itself as a set
        for i in range(coin + 1,n + 1): #fill the remaining sets with a new possibility with this coin
            dp[i] += dp[i - coin]
        #print(dp)
    return dp[-1]
    '''
    dp = [1] + [0] * n  # dp[i]表示组成数字i的可能组合方式
    for i in range(c[0],n + 1,c[0]):
        dp[i] = 1
    #print(dp)
    for coin in c[1:]:
        for i in range(1,n + 1):
            if i - coin > 0:
                dp[i] += dp[i - coin]
        #print('a',dp)
        for i in range(coin,n + 1,coin):
            dp[i] += 1
        #print('b',dp)
    return dp[-1]
    '''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
