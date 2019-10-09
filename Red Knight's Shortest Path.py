#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the printShortestPath function below.
from collections import Counter
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    # if possible:n * 2 = I's;n * 1 + m * 2 = J's
    Is = i_end - i_start
    Js = j_end - j_start
    if Is & 1 or (Js - Is // 2) & 1:
        print('Impossible')
        return
    di = [(-2,-1),(-2,1),(0,2),(2,1),(2,-1),(0,-2)]
    dname = ['UL', 'UR', 'R', 'LR', 'LL', 'L']
    steps = Counter()
    while Is != 0 or Js != 0:
        for i,d in enumerate(di):
            if Is == 0:
                if d[0] != 0:
                    continue
                # d[0] == 0
                elif d[1] * Js > 0:
                    j_start += d[1]
                    steps[dname[i]] += 1
                    break
            elif Js == 0:
                if d[0] * Is > 0:
                    i_start += d[0]
                    j_start += d[1]
                    steps[dname[i]] += 1
                    break
            else:   # Is != 0 and Js != 0
                if d[0] * Is > 0 and d[1] * Js > 0:
                    #print(i,d)
                    i_start += d[0]
                    j_start += d[1]
                    steps[dname[i]] += 1
                    break
        #print(i_start,j_start)
        Is = i_end - i_start
        Js = j_end - j_start
    print(sum(steps.values()))
    #print(steps)
    ans = []
    for dn in dname:
        ans += [dn] * steps[dn]
    print(' '.join(ans))



if __name__ == '__main__':
    n = int(input())

    i_startJ_start = input().split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
