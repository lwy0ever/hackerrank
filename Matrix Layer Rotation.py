#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    row = len(matrix)
    col = len(matrix[0])
    #print(m,n)
    def newPos(x,y,row,col,r):  # x表示行,y表示列
        circle = min(row - 1 - x,x,col - 1 - y,y)   #从外往内第几圈(从0开始)
        rStart = circle # 最小行
        cStart = circle # 最小列
        rEnd = row - circle - 1 # 最大行(含)
        cEnd = col - circle - 1 # 最大列(含)
        circumference = (rEnd - rStart) * 2 + (cEnd - cStart) * 2 # 圈的周长
        toMove = r % circumference
        newX,newY = x,y
        while toMove > 0:
            if newY == cStart and newX < rEnd:
                if toMove > rEnd - newX:
                    toMove -= rEnd - newX
                    newX = rEnd
                else:
                    toMove -= 1
                    newX += 1
            elif newY == cEnd and newX > rStart:
                if toMove > newX - rStart:
                    toMove -= newX - rStart
                    newX = rStart
                else:
                    toMove -= 1
                    newX -= 1
            elif newX == rStart and newY > cStart:
                if toMove > newY - cStart:
                    toMove -= newY - cStart
                    newY = cStart
                else:
                    toMove -= 1
                    newY -= 1
            elif newX == rEnd and newY < cEnd:
                if toMove > cEnd - newY:
                    toMove -= cEnd - newY
                    newY = cEnd
                else:
                    toMove -= 1
                    newY += 1
        return newX,newY

    ans = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            x,y = newPos(i,j,row,col,r)
            ans[x][y] = matrix[i][j]
    for i in range(row):
        print(' '.join(map(str,ans[i])))

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
