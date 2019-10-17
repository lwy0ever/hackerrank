#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    def bfs(a,b):
        ans = 0
        di = {(-a,-b),(-a,b),(a,-b),(a,b),(-b,-a),(-b,a),(b,-a),(b,a)}
        fromP = {(0,0)}
        endP = (n - 1,n - 1)
        visited = {(0,0)}
        while fromP:
            new_fromP = set()
            for x,y in fromP:
                for dx,dy in di:
                    if x + dx >= 0 and y + dy >= 0 and x + dx < n and y + dy < n:
                        if (x + dx,y + dy) not in visited:
                            new_fromP.add((x + dx,y + dy))
                            visited.add((x + dx,y + dy))
            fromP = new_fromP
            ans += 1
            if endP in visited:
                return ans
        return -1

    ans = [[-1] * (n - 1) for _ in range(n - 1)]
    for i in range(1,n):
        for j in range(1,n):
            ans[i - 1][j - 1] = bfs(i,j)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
