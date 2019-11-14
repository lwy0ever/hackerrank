#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the redJohn function below.
def calWays(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1,n + 1):
        if i - 4 >= 0:
            dp[i] = dp[i - 4] + dp[i - 1]
        else:
            dp[i] = 1
    #print(dp)
    return dp
def redJohn(n):
    if ways[n] < 2:
        return 0
    primes = []
    for w in range(3,ways[n] + 1,2):
        for p in primes:
            if p * p > w:
                primes.append(w)
                break
            if w % p == 0:
                break
        else:
            primes.append(w)
        #print(w,primes)
    return len(primes) + 1  # add 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    ways = calWays(40)
    #print(ways)

    for t_itr in range(t):
        n = int(input())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
