#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #print(arr)
    
    hourglass = [[0,0],[0,1],[0,2],[1,1],[2,0],[2,1],[2,2]]
    glasssize = 3

    summax = -999999
    for i in range(6 - glasssize + 1):
        for j in range(6 - glasssize + 1):
            s = 0
            for h in hourglass:
                s += arr[i + h[0]][j + h[1]]
            #print(s)
            if s > summax:
                summax = s
    print(summax)
