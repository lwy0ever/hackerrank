#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    dp = [0] * len(n)
    dp[0] = int(n[0])
    for i in range(1,len(n)):
        dp[i] = ((dp[i - 1] * 10) + int(n[i]) * (i + 1)) % (10 ** 9 + 7)
    #print(dp)
    return sum(dp) % (10 ** 9 + 7)
    '''
    ans = 0
    t = int(n)
    while t > 0:
        m = 1
        while t >= m:
            m *= 10
            ans += (t % m)
            #print(t % m)
        t //= 10
    return ans % (10 ** 9 + 7)
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
