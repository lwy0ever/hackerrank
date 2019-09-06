#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ans = 0
    for i in range(n):
        ar[i] %= k
    cnt = Counter(ar)
    ans += cnt[0] * (cnt[0] - 1) // 2
    print(ans)
    for i in range(1,k // 2):
        ans += (cnt[i] * cnt[k - i])
        print(ans)
    if k % 2 == 0:
        ans += cnt[k // 2] * (cnt[k // 2] - 1) // 2
    else:
        ans += (cnt[k // 2] * cnt[k // 2 + 1])
    print(ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
