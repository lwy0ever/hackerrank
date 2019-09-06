#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    h = len(A)
    w = len(A[0])
    s = 0
    for i in range(h):
        for j in range(w):
            s += A[i][j] * 6    # 每个立方体6个面
            s -= (A[i][j] - 1) * 2 # 2层及以上，每多一层有2个面相对（不露出）
    for i in range(h):
        for j in range(w - 1):
            s -= min(A[i][j],A[i][j + 1]) * 2   # 相邻立面，每一个共有层，减少2个面——统计横向
    for i in range(h - 1):
        for j in range(w):
            s -= min(A[i][j],A[i + 1][j]) * 2   # 相邻立面，每一个共有层，减少2个面——统计纵向
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
