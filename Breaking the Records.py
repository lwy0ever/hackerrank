#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    s = scores[0]   #small
    b = s   #big
    ans = [0,0]
    for i in range(1,len(scores)):
        if scores[i] < s:
            s = scores[i]
            ans[1] += 1
            continue
        if scores[i] > b:
            b = scores[i]
            ans[0] += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
