#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    ans = [-1]
    sticks.sort(reverse = True)
    for i in range(len(sticks) - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            ans = [sticks[i + 2],sticks[i + 1],sticks[i]]
            break
    return ans
    '''
    ans = []
    maxPerimeter = 0
    sticks.sort(reverse = True)
    #print(sticks,len(sticks))
    for i in range(len(sticks) - 2):
        #print(i)
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            #print(sum(sticks[i:i+3]))
            if sum(sticks[i:i+3]) >= maxPerimeter:
                maxPerimeter = sum(sticks[i:i+3])
                ans = [sticks[i + 2],sticks[i + 1],sticks[i]]
                break
            else:
                break
    if maxPerimeter == 0:
        ans = [-1]
    return ans
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
