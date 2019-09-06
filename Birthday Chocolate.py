#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    ans = 0
    for i in range(1,len(s)):
        s[i] += s[i - 1]
    if s[m - 1] == d:
        ans += 1
    for i in range(m,len(s)):
        if s[i] - s[i - m] == d:
            ans += 1
    return ans
    '''
    ans = 0
    ttl = sum(s[:m - 1])
    for i in range(m - 1,len(s)):
        ttl += s[i]
        if ttl == d:
            ans += 1
        ttl -= s[i - m + 1]
    return ans
    '''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
