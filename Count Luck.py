#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countLuck function below.
def countLuck(matrix, k):
    di = [(-1,0),(1,0),(0,-1),(0,1)]
    stx = sty = endx = endy = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                stx = i + 1
                sty = j + 1
            if matrix[i][j] == '*':
                endx = i + 1
                endy = j + 1
        matrix[i] = 'X' + matrix[i] + 'X'
    matrix.insert(0,'X' * (m + 2))
    matrix.append('X' * (m + 2))
    print('\n'.join(matrix))
    
    # 需要用深度优先，如果使用广度优先，已经走过的路径会相互影响
    def dfs(x,y,corner):
        #print(x,y,corner)
        #print('\n'.join(matrix))
        if x == endx and y == endy:
            return corner
        cnt = 0 # 记录可行的方向数
        for dx,dy in di:
            if matrix[x + dx][y + dy] in ('.','*'):
                cnt += 1
        #print(cnt)
        if cnt == 1:
            for dx,dy in di:
                if matrix[x + dx][y + dy] in ('.','*'):
                    matrix[x + dx] = matrix[x + dx][:y + dy] + 'X' + matrix[x + dx][y + dy + 1:]
                    return dfs(x + dx,y + dy,corner)
                    matrix[x + dx] = matrix[x + dx][:y + dy] + '.' + matrix[x + dx][y + dy + 1:]
        elif cnt > 1:
            ct = []
            for dx,dy in di:
                if matrix[x + dx][y + dy] in ('.','*'):
                    matrix[x + dx] = matrix[x + dx][:y + dy] + 'X' + matrix[x + dx][y + dy + 1:]
                    ct.append(dfs(x + dx,y + dy,corner + 1))
                    matrix[x + dx] = matrix[x + dx][:y + dy] + '.' + matrix[x + dx][y + dy + 1:]
            return min(ct)
        else:   # cnt == 0
            return float('inf')
    t = dfs(stx,sty,0)
    print(t)
    if t == k:
        return 'Impressed'
    else:
        return 'Oops!'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
