#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse = True)
    ans = 0
    l = len(c)
    for i in range(l):
        ans += c[i] * (i // k + 1)
    return ans
    '''
    c.sort(reverse = True)
    multi = 1
    ans = 0
    i = 0
    while i < len(c):
        j = 0
        while j < k and i < len(c):
            ans += c[i] * multi
            j += 1
            i += 1
        multi += 1
    return ans
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
