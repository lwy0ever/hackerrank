#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def twoPluses(grid):
    def crossTry(grid,x,y,length):
        #print(x,y,length)
        ds = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(1,length):
            for h,v in ds:
                if grid[x + h * i][y + v * i] == 'B':
                    return False
        return True
    
    def isOverlap(p1,len1,p2,len2):
        mi = min(abs(p1[0] - p2[0]),abs(p1[1] - p2[1]))
        ma = max(abs(p1[0] - p2[0]),abs(p1[1] - p2[1]))
        if mi == 0:
            return ma - (len1 + len2 - 1) < 0
        elif ma < max(len1,len2) and mi < min(len1,len2):
            return True
        else:
            return False

    n = len(grid)
    m = len(grid[0])
    mi = min(m,n)
    ans = 0
    for len1 in range((mi + 1) // 2,0,-1):
        for x1 in range(len1 - 1,n - len1 + 1):
            for y1 in range(len1 - 1,m - len1 + 1):
                if grid[x1][y1] == 'G' and crossTry(grid,x1,y1,len1):
                    #print((x1,y1),len1)
                    cross2Found = False
                    for len2 in range(len1,0,-1):
                        for x2 in range(len2 - 1,n - len2 + 1):
                            for y2 in range(len2 - 1,m - len2 + 1):
                                #if len1 >= 3 and len2 >= 3:
                                #    print((x1,y1),len1,(x2,y2),len2)
                                if grid[x2][y2] == 'G' and crossTry(grid,x2,y2,len2):
                                    if not isOverlap((x1,y1),len1,(x2,y2),len2):
                                        #print((x1,y1),len1,(x2,y2),len2)
                                        ans = max(ans,(len1 * 4 - 3) * (len2 * 4 - 3))
                                        cross2Found = True
                                        break
                            if cross2Found:
                                break
                        if cross2Found:
                            break
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
