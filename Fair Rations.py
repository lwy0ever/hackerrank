#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    ans = 0
    pre = 0
    for p in B:
        if (p + pre) % 2 == 1:
            ans += 2
            pre = 1
        else:
            pre = 0
    if pre == 0:
        return ans
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
