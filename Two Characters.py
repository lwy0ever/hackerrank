#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    ss = set(s)
    pre = ''
    for c in s:
        if pre == c and c in ss:
            ss.remove(c)
        pre = c
    ls = list(ss)
    ls.sort()
    n = len(ls)
    d = {}
    stat = {}
    for i in range(n - 1):
        for j in range(i + 1,n):
            d[ls[i] + ls[j]] = 0
            stat[ls[i] + ls[j]] = ''
    #print(stat,d)
    for c in s:
        for xc in ss:
            if xc == c:
                continue
            if min(xc,c) + max(xc,c) not in stat:
                continue
            if stat[min(xc,c) + max(xc,c)] == c:
                del stat[min(xc,c) + max(xc,c)]
                del d[min(xc,c) + max(xc,c)]
            else:
                stat[min(xc,c) + max(xc,c)] = c
                d[min(xc,c) + max(xc,c)] += 1
    return max(list(d.values()) + [0])



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
