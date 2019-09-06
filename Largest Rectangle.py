#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    ans = 0
    ans = len(h)
    stack = []
    h.append(0)
    for i in range(len(h)):
        left_index = i
        while stack and stack[-1][1] >= h[i]:
            last = stack.pop()
            left_index = last[0]
            ans = max(ans,h[i] * (i + 1 - last[0]),last[1] * (i - last[0]))
        stack.append((left_index,h[i]))
        #print(stack)
    return ans
    '''
    ans = 0
    n = len(h)
    for i in range(n):
        left = i
        right = i
        while left >= 0 and h[left] >= h[i]:
            left -= 1
        while right < n and h[right] >= h[i]:
            right += 1
        #print(i,h[i],left,right)
        ans = max(ans,(right - left - 1) * h[i])
    return ans
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
