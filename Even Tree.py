#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
from collections import defaultdict
def evenForest(t_nodes, t_edges, t_from, t_to):
    # 利用dfs统计偶数子树的数量n,则可以通过n - 1次切割,分成n棵子树
    m = defaultdict(list)
    for i in range(t_edges):
        m[t_from[i]].append(t_to[i])
        m[t_to[i]].append(t_from[i])
    nodeCount = [0] * (t_nodes + 1)

    # dfs
    def dfs(node,fathernode):
        if len(m[node]) == 1:
            nodeCount[node] = 1
        cnt = 1 # 需要加上node自己
        for child in m[node]:
            if child != fathernode:
                dfs(child,node)
                cnt += nodeCount[child]
        nodeCount[node] = cnt
    
    dfs(1,0)
    ans = 0
    for i in range(1,t_nodes + 1):
        if nodeCount[i] & 1 == 0:
            ans += 1
    return ans - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
