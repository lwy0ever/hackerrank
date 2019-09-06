#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
from collections import defaultdict
def countSort(arr):
    def qs(arr):
        n = len(arr)
        if n <= 1:
            return arr
        c = arr[0][0]
        left,eq,right = [],[arr[0]],[]
        for i in range(1,n):
            if c > arr[i][0]:
                left.append(arr[i])
            elif c < arr[i][0]:
                right.append(arr[i])
            else:
                eq.append(arr[i])
        left = qs(left)
        right = qs(right)
        #print(' '.join(map(str,(left + eq + right))))
        return left + eq + right
    n = len(arr)
    #print(n)
    for i in range(n // 2):
        arr[i][1] = '-'
    for i in range(n):
        arr[i][0] = int(arr[i][0])
    #print(arr)
    #arr = qs(arr)
    dd = defaultdict(list)
    for i in range(n):
        dd[arr[i][0]].append(arr[i][1])
    #print(arr)
    ans = []
    #for a in arr:
    #    ans.append(a[1])
    for i in range(100):
        ans += dd[i]
    print(' '.join(ans))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
