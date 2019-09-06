#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
from collections import Counter
def nonDivisibleSubset(k, s):
    # Write your code here
    ans = 0
    n = []
    for i in s:
        n.append(i % k)
    cnt = Counter(n)
    print(cnt)
    for i in range(1,(k + 1) // 2):
        ans += max(cnt[i],cnt[k - i])
    if cnt[0] > 0:
        ans += 1
    if k % 2 == 0 and cnt[k // 2] > 0:
        ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
