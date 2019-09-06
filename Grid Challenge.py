#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    n = len(grid)
    for i in range(n):
        l = list(grid[i])
        l.sort()
        grid[i] = ''.join(l)
    #print(list(zip(*grid)))
    for i in range(len(grid[0])):
        for j in range(n - 1):
            if grid[j][i] > grid[j + 1][i]:
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
