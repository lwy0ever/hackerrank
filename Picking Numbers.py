#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    ans = 0
    d = {}
    for e in a:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    for k in sorted(d.keys()):
        if k + 1 in d:
            ans = max(ans,d[k] + d[k + 1])
        else:
            ans = max(ans,d[k])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
