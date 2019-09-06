#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total = 0
    for i in range(len(q) - 1,-1,-1):
        if q[i] - 2 > i + 1:
            print('Too chaotic')
            break
        t = 0
        '''
        for j in range(i + 1,len(q)):
            if q[i] > q[j]:
                t += 1
        '''
        for j in q[max(0,q[i] - 2):i]:
            if q[i] < j:
                t += 1
        total += t
    else:
        print(total)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
