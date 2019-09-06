#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    m = len(c)
    #print(c,m)
    ma = 0
    for i in range(m - 1):
        dis = c[i + 1] - c[i]
        ma = max(dis,ma)
    #print(ma)
    ma //= 2
    ma = max(c[0] - 0,ma)
    ma = max((n - 1) - c[-1],ma)
    return ma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
