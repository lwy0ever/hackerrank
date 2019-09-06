#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def solution(a):
    pos = {}
    for i in range(len(a)):
        pos[a[i]] = i
    #print(pos)
    #print(a)
    #sa = sorted(a,reverse = reverse)
    sa = sorted(a)
    ans = 0
    for i in range(len(a)):
        if a[i] != sa[i]:
            ans += 1
            index_to_swap = pos[sa[i]]
            pos[a[i]],pos[sa[i]] = pos[sa[i]],pos[a[i]]
            #pos[a[i]] = pos[sa[i]]
            a[i],a[index_to_swap] = a[index_to_swap],a[i]
            #a[i],a[index_to_swap] = sa[i],a[i]
            #print(pos)
            #print(ans,a)
    return ans

def lilysHomework(arr):
    asc = solution(arr.copy())
    desc = solution(arr[::-1].copy())
    return min(asc,desc)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
