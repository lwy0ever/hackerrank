#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the prims function below.
from collections import defaultdict
import bisect
def prims(n, edges, start):
    g = defaultdict(dict)
    for a,b,w in edges:
        g[a][b] = g[b][a] = w
    ans = 0
    nodes = [start]
    weights = [0]
    visited = set()
    while nodes:
        node = nodes.pop(0)
        w = weights.pop(0)
        if node in visited:
            continue
        # not visited
        ans += w
        visited.add(node)
        for k,v in g[node].items():
            if k in visited:
                continue
            pos = bisect.bisect(weights,v)
            weights.insert(pos,v)
            nodes.insert(pos,k)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
