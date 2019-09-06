#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    t = {}
    for i in range(1,6):
        t[i] = 0
    for a in arr:
        t[a] += 1
    ans = 1
    for i in range(2,6):
        if t[i] > t[ans]:
            ans = i
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
