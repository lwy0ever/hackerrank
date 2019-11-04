#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bfs function below.
from collections import defaultdict
def bfs(n, m, edges, s):
    ans = [-1] * (n + 1)    # 多加1个ans[0]，便于下标计算
    m = defaultdict(list)
    for a,b in edges:
        m[a].append(b)
        m[b].append(a)
    visited = {s}
    fromP = {s}
    step = 1
    distance = 6
    while fromP:
        toP = set()
        for p in fromP:
            if p not in m:
                continue
            for t in m[p]:
                if t in visited:
                    continue
                ans[t] = step * distance
                visited.add(t)
                toP.add(t)
        fromP = toP
        step += 1
    ans.pop(s)
    ans.pop(0)  # 将多加ans[0]的去掉
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
