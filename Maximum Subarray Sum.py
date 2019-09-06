#!/bin/python3

#import math
import os
#import random
#import re
#import sys

from bisect import insort, bisect_left,bisect_right
# Complete the maximumSum function below.
def maximumSum(a, m):
    mm,pre = 0,0
    arr = []
    l = 0
    for i in a:
        pre = (pre + i) % m
        mm = max(mm,pre)
        index = bisect_left(arr,pre + 1)
        if index < l:
            mm = max(mm,pre - arr[index] + m)
        arr.insert(index,pre)
        l += 1
    return mm

def XmaximumSum(a, m):
    # Create prefix tree
    prefix = [0] * len(a)
    curr = 0
    for i in range(len(a)):
        curr = (a[i] + curr) % m
        prefix[i] = curr
    
    # Compute max modsum
    pq = [prefix[0]]
    maxmodsum = max(prefix)
    for i in range(1, len(a)):
        # Find cheapest prefix larger than prefix[i]
        left = bisect_right(pq, prefix[i])
        if left != len(pq):
            # Update maxmodsum if possible
            modsum = (prefix[i] - pq[left]) % m
            maxmodsum = max(maxmodsum, modsum)

        # add current prefix to heap
        insort(pq, prefix[i])

    return maxmodsum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
