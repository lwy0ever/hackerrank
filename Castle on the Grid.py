#!/bin/python3

#import math
import os
#import random
#import re
#import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    ans = 0
    length = len(grid)
    for i in range(length):
        grid[i] = 'X' + grid[i] + 'X'
    grid.insert(0,'X' * (length + 2))
    grid.append('X' * (length + 2))
    #print(grid)
    cross = {}  # example:{(2,3):{'step':float('inf'),'next':[(2,5),(1,3)]}}
    start = (startX + 1,startY + 1)
    goal = (goalX + 1,goalY + 1)
    cross[start] = {'step':0,'next':[]}
    cross[goal] = {'step':float('inf'),'next':[]}
    connectedCross = set()
    for i in range(1,length + 2):
        for j in range(1,length + 2):
            if grid[i][j] == '.':
                if (i,j) == start or (i,j) == goal:
                    connectedCross.add((i,j))
                if (grid[i - 1][j] == '.' and grid[i][j - 1] == '.') or (grid[i - 1][j] == '.' and grid[i][j + 1] == '.') or (grid[i + 1][j] == '.' and grid[i][j - 1] == '.') or (grid[i + 1][j] == '.' and grid[i][j + 1] == '.'):
                    if (i,j) not in cross:
                        cross[(i,j)] = {'step':float('inf'),'next':[]}
                    connectedCross.add((i,j))
            else:   #connect crosses
                for c in connectedCross:
                    for e in connectedCross:
                        if c != e:
                            cross[c]['next'].append(e)
                connectedCross = set()
    for j in range(1,length + 2):
        for i in range(1,length + 2):
            if grid[i][j] == '.':
                if (i,j) == start or (i,j) == goal:
                    connectedCross.add((i,j))
                if (grid[i - 1][j] == '.' and grid[i][j - 1] == '.') or (grid[i - 1][j] == '.' and grid[i][j + 1] == '.') or (grid[i + 1][j] == '.' and grid[i][j - 1] == '.') or (grid[i + 1][j] == '.' and grid[i][j + 1] == '.'):
                    if (i,j) not in cross:
                        cross[(i,j)] = {'step':float('inf'),'next':[]}
                    connectedCross.add((i,j))
            else:   #connect crosses
                for c in connectedCross:
                    for e in connectedCross:
                        if c != e:
                            cross[c]['next'].append(e)
                connectedCross = set()
            #print(i,j,grid[i][j],connectedCross)
    #print(cross)
    maybe = [start]
    i = 0
    while True:
        #print(i,maybe,cross)
        p = maybe[i]
        if p == goal:
            return cross[p]['step']
        for n in cross[p]['next']:
            if cross[n]['step'] > cross[p]['step'] + 1:
                maybe.append(n)
                cross[n]['step'] = cross[p]['step'] + 1
        #maybeLen = counter
        i += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
