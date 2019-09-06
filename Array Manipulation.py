#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    '''
    l = list(set(list(zip(*queries))[0] + list(zip(*queries))[1]))
    l.sort()
    #print(l)
    r = [0] * (len(l))
    for q in queries:
        #print(r)
        for i in range(l.index(q[0]),l.index(q[1]) + 1):
            r[i] += q[2]
    #print(r)
    return max(r)
    '''
    r = [0] * (n + 1)
    for q in queries:
        r[q[0] - 1] += q[2]
        r[q[1]] -= q[2]
    s = 0
    curm = 0
    for x in r:
        s += x
        if s > curm:
            curm = s
    return curm 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
