#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def maxRegion(grid):
    ans = 0
    direct = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    #print(n,m,grid)
    for r in range(n):
        grid[r].insert(0,0)
        grid[r].append(0)
    grid.insert(0,[0] * (m + 2))
    grid.append([0] * (m + 2))    
    #print(grid)
    for r in range(1,n + 2):
        for c in range(1,m + 2):
            if grid[r][c] == 1:
                counter = 1
                grid[r][c] = 0
                region = [(r,c)]
                while region:
                    p = region.pop()
                    for d in direct:
                        if grid[p[0] + d[0]][p[1] + d[1]] == 1:
                            counter += 1
                            region.append((p[0] + d[0],p[1] + d[1]))
                            grid[p[0] + d[0]][p[1] + d[1]] = 0
                ans = max(ans,counter)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
