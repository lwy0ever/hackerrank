#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    # https://zh.wikipedia.org/wiki/置换的奇偶性
    s = 0
    n = len(A)
    visited = [False] * n
    for i in range(n):
        #print('for',i)
        if visited[A[i] - 1]:
            continue
        cur = 1
        t = i
        while not visited[A[t] - 1]:
            visited[A[t] - 1] = True
            cur ^= 1
            t = A[t] - 1
            #print(t,visited)
        s ^= cur
    if s == 0:
        return 'YES'
    else:
        return 'NO'
    '''
    s = 0
    n = len(A)
    for i in range(n - 1):
        for j in range(i + 1,n):
            if A[i] > A[j]:
                s += 1
    if s % 2 == 0:
        return 'YES'
    else:
        return 'NO'
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
