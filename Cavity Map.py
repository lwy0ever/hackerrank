#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    rn = len(grid)
    cn = len(grid[0])
    adjacency = [(-1,0),(0,-1),(1,0),(0,1)]
    for i in range(1,rn - 1):
        for j in range(1,cn - 1):
            isCavity = True
            for a,b in adjacency:
                if grid[i + a][j + b] == 'X' or grid[i + a][j + b] >= grid[i][j]:
                    isCavity = False
                    break
            if isCavity:
                grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
