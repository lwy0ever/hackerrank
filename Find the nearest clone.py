#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    if ids.count(val) < 2:
        return -1
    edge = {}
    for i in range(len(graph_from)):
        if graph_from[i] in edge:
            edge[graph_from[i]].add(graph_to[i])
        else:
            edge[graph_from[i]] = {graph_to[i]}
        if graph_to[i] in edge:
            edge[graph_to[i]].add(graph_from[i])
        else:
            edge[graph_to[i]] = {graph_from[i]}
    print(edge)
    pos = set()
    visit = [float('inf')] * graph_nodes
    for i in range(graph_nodes):
        if ids[i] == val:
            pos.add(i + 1)
            visit[i] = 0
    print(pos,visit)
    while pos:
        newPos = set()
        for p in pos:
            #visit[p - 1] = min(visit[p - 1])
            for np in edge[p]:
                if visit[np - 1] + visit[p - 1] < float('inf'):
                    return visit[np - 1] + visit[p - 1] + 1
                if visit[np - 1] > visit[p - 1] + 1:
                    visit[np - 1] = visit[p - 1] + 1
                    newPos.add(np)
                edge[np].remove(p)
            del edge[p]
        pos = newPos
        print(pos,visit)
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
