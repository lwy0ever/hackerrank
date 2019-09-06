#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
    if n <= p:
        return math.ceil(n / (m * w))
    counter = 0
    candy = 0
    ans = float('inf')
    while candy < n:
        #print(counter,m,w,candy)
        if candy < p:
            i = math.ceil((p - candy) / (m * w))
            counter += i
            candy += m * w * i
            continue
        else:   # candy >= p:
            tobuy,candy = divmod(candy,p)
            total = m + w + tobuy
            half = total // 2
            if m > w:
                m = max(m,half)
                w = total - m
            else:
                w = max(w,half)
                m = total - w

            candy += m * w
            counter += 1

        ans = min(ans, counter + math.ceil((n - candy) / (m * w)))
    return min(ans,counter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
