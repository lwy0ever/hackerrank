#!/bin/python3

import os
import sys

#
# Complete the kMarsh function below.
#
def kMarsh(grid):
    #
    # Write your code here.
    #
    n = len(grid)
    m = len(grid[0])
    left = [[0] * m for _ in range(n)] # left[i][j]表示从(i,j)(含(i,j))向左,'.'的数量(最长边长+1)
    up = [[0] * m for _ in range(n)] # up[i][j]表示从(i,j)(含(i,j))向上,'.'的数量(最长边长+1)
    right = [[0] * m for _ in range(n)] # right[i][j]表示从(i,j)(含(i,j))向右,'.'的数量(最长边长+1)
    down = [[0] * m for _ in range(n)] # down[i][j]表示从(i,j)(含(i,j))向下,'.'的数量(最长边长+1)
    for i in range(n):
        if grid[i][0] == '.':
            left[i][0] = 1
        for j in range(1,m):
            if grid[i][j] == '.':
                left[i][j] = left[i][j - 1] + 1
    for j in range(m):
        if grid[0][j] == '.':
            up[0][j] = 1
        for i in range(1,n):
            if grid[i][j] == '.':
                up[i][j] = up[i - 1][j] + 1
    for i in range(n):
        if grid[i][m - 1] == '.':
            right[i][m - 1] = 1
        for j in range(m - 2,-1,-1):
            if grid[i][j] == '.':
                right[i][j] = right[i][j + 1] + 1
    for j in range(m):
        if grid[n - 1][j] == '.':
            down[n - 1][j] = 1
        for i in range(n - 2,-1,-1):
            if grid[i][j] == '.':
                down[i][j] = down[i + 1][j] + 1

    # hp表示半周长
    ans = 0
    for i in range(n):
        for j in range(m):  # (i,j)表示栅栏的左上角
            if grid[i][j] == 'x':
                continue
            if (right[i][j] + down[i][j] - 2) * 2 <= ans:
                continue
            # (p,q)表示栅栏的右下角
            for p in range(i + down[i][j] - 1,i,-1):
                if (p - i + right[i][j] - 1) * 2 <= ans:
                    break
                for q in range(j + right[i][j] - 1,j,-1):
                    if grid[p][q] == 'x':
                        continue
                    if (p - i + q - j) * 2 <= ans:
                        break
                    if p - i <= up[p][q] - 1 and q - j <= left[p][q] - 1:
                        ans = max(ans, (p - i + q - j) * 2)
                        break
    print(ans if ans else 'impossible')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    grid = []

    for _ in range(m):
        grid_item = input()
        grid.append(grid_item)

    kMarsh(grid)
