#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    n = len(arr)
    left = n
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            left = i
            break
    if left == n:   # ascending order
        print('yes')
        return
    right = 0
    for i in range(n - 1,0,-1):
        if arr[i - 1] > arr[i]:
            right = i
            break
    if left == right:
        print('no')
        return
    # try swap
    canSwap = True
    arr[left],arr[right] = arr[right],arr[left]
    if left == 0:
        pre = float('-inf')
    else:
        pre = arr[left - 1]
    for i in range(left,right + 1):
        if pre > arr[i]:
            canSwap = False
            break
        pre = arr[i]
    if right < n - 1:
        if arr[right] > arr[right + 1]:
            canSwap = False
    if canSwap:
        print('yes')
        print('swap %d %d'%(left + 1,right + 1))
        return
    else:
        arr[left],arr[right] = arr[right],arr[left]

    # try reverse
    canReverse = True
    if left == 0:
        pre = float('-inf')
    else:
        pre = arr[left - 1]
    for i in range(right,left - 1,-1):
        if pre > arr[i]:
            canReverse = False
            break
        pre = arr[i]
    if right < n - 1:
        if arr[left] > arr[right + 1]:
            canReverse = False
    if canReverse:
        print('yes')
        print('reverse %d %d'%(left + 1,right + 1))
        return

    print('no')
    return

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
