#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    jump = {}
    for s,e in ladders:
        jump[s] = e
    for s,e in snakes:
        jump[s] = e
    ans = 0
    visited = {1}
    fromP = {1}
    # bfs
    while fromP:
        toP = set()
        ans += 1
        # 逐点
        for f in fromP:
            # 逐步长
            for i in range(1,7):
                # 终点
                t = f + i
                # 终点是否超100
                if t > 100:
                    break
                # 是否jump
                if t in jump:
                    t = jump[t]
                # 是否到达
                if t == 100:
                    return ans
                # 是否曾经考虑过该点
                if t not in visited:
                    toP.add(t)
                    visited.add(t)
        fromP = toP
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
