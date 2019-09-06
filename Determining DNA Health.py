#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import bisect_left, bisect_right
from collections import defaultdict

# ------------------------------------------------------------------------------
def getHealth(seq, first, last, largest):
    h, ls = 0, len(seq)
    for f in range(ls):
        for j in range(1, largest + 1):
            if f + j > ls:
                break
            sub = seq[f:f + j]
            if sub not in subs:
                break
            if sub not in genesMap:
                continue
            ids, hs = genesMap[sub]
            h += hs[bisect_right(ids, last)] - hs[bisect_left(ids, first)]
    return h

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    # ------------------------------------------------------------------------------
    genesMap = defaultdict(lambda: [[], [0]])
    subs = set()
    for i, gene in enumerate(genes):
        genesMap[gene][0].append(i)
        for j in range(1, len(gene) + 1):
            subs.add(gene[:j])
    for v in genesMap.values():
        for i, ix in enumerate(v[0]):
            v[1].append(v[1][i] + health[ix])
    # ------------------------------------------------------------------------------
    largest = max(list(map(len, genes)))
    hMin, hMax = float('inf'), 0

    s = int(input())

    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]

        h = getHealth(d, first, last, largest)
        hMin, hMax = min(hMin, h), max(hMax, h)
    print(hMin, hMax)
