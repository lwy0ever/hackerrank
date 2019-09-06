#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    ans = 0
    once = {}
    twice = {}
    for a in arr:
        if a - d in twice:
            ans += twice[a - d]
        if a - d in once:
            if a in twice:
                twice[a] += once[a - d]
            else:
                twice[a] = once[a - d]
        if a in once:
            once[a] += 1
        else:
            once[a] = 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
