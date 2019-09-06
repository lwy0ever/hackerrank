#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass = [[0,0],[0,1],[0,2],[1,1],[2,0],[2,1],[2,2]]
    sa = []
    for i in range(6 - 2):
        for j in range(6 - 2):
            s = 0
            for h in hourglass:
                s += arr[i + h[0]][j + h[1]]
            sa.append(s)
    return max(sa)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
