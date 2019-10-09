#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.
def connectedCell(matrix):
    di = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    def find(x,y):
        for d in di:
            if x + d[0] >= 0 and x + d[0] < n and y + d[1] >= 0 and y + d[1] < m:
                if matrix[x + d[0]][y + d[1]]:
                    matrix[x + d[0]][y + d[1]] = 0
                    nonlocal t
                    t += 1
                    find(x + d[0],y + d[1])

    ans = 0
    t = 0
    #print(n,m)
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                t = 1
                matrix[i][j] = 0
                find(i,j)
                ans = max(ans,t)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
