#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the shortestReach function below.
from collections import defaultdict
def shortestReach(n, edges, s):
    ans = [10 ** 5 * n] * (n + 1)  # 从0开始，便于后面下标的使用
    ans[s] = 0
    # 使用广度优先搜索
    fromP = {s}
    while fromP:
        toP = set()
        for p in fromP:
            # 到达当前点的最短路线
            weighted = ans[p]
            for t in edges[p]:
                # 找到了新的最短路线
                if weighted + edges[p][t] < ans[t]:
                    ans[t] = weighted + edges[p][t]
                    toP.add(t)
        fromP = toP
    for i in range(n + 1):
        if ans[i] == 10 ** 5 * n:
            ans[i] = -1
    ans.pop(s)  # 踢掉起点
    ans.pop(0)  # 踢掉0
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        # 构建一个map
        edges = defaultdict(dict)
        for _ in range(m):
            a,b,w = map(int, input().rstrip().split())
            edges[a][b] = edges[b][a] = min(edges[a].get(b,10 ** 5),w)

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
