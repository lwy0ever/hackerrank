#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    if n == 1:
        return grid    
    if n % 2 == 0:
        ngrid = ['O' * c for i in range(r)]
        return ngrid
    if n % 4 == 1:
        loop = 2
    if n % 4 == 3:
        loop = 1
    for l in range(loop):
        ngrid = ['O' * c for i in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    if i - 1 >= 0:
                        ngrid[i - 1] = ngrid[i- 1][:j] + '.' + ngrid[i - 1][j + 1:]
                    if i + 1 < r:
                        ngrid[i + 1] = ngrid[i + 1][:j] + '.' + ngrid[i + 1][j + 1:]
                    ngrid[i] = ngrid[i][:max(j - 1,0)] + '.' * (min(j + 2,c) - max(j - 1,0)) + ngrid[i][min(j + 2,c):]
        grid = ngrid
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
