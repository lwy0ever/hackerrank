#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    track.sort(key = lambda t:(t[0],t[1],-t[2]))    # 有效排序
    #print(track)
    ans = n * m
    preR = 0
    preC1 = 0
    maxC2 = 0
    for r,c1,c2 in track:
        if r == preR:   # 同一行
            if c1 == preC1: # 同一个起点,由于终点已经倒序排列,因此忽略即可
                continue
            else:
                if c1 <= maxC2:  # 重叠
                    if c2 <= maxC2: # 新的被完全覆盖
                        preC1 = c1
                        continue
                    else:
                        ans -= (c2 - maxC2)
                        preC1 = c1
                        maxC2 = c2
                else:   # c1 > maxC2,不重叠
                    ans -= (c2 - c1 + 1)
                    preC1 = c1
                    maxC2 = c2
        else:
            ans -= (c2 - c1 + 1)
            preR = r
            preC1 = c1
            maxC2 = c2
        #print(r,c1,c2,ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
