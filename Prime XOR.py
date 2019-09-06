#!/bin/python3

# unfinished version

import math
import os
import random
import re
import sys

# Complete the primeXor function below.
from collections import Counter
import sys

def isPrime(x):
    if x == 1:
        return False
    
    if x == 2:
        return True
    if x >> 1 << 1 == x:
        return False

    for d in range(3, int(x ** 0.5) + 1, 2):
        if x % d == 0:
            return False
    return True


def get_nevens(y):
    return y//2 + 1


def get_nodds(y):
    return y//2 + y%2


def primeXor(a):
    #n = len(a)
    c = Counter(a) 
    E = list(c.keys())
    M = 8192 * 2

    Sp = [0] * M
    Sn = [0] * M
    e = E[0]

    Sp[e] = get_nodds(c[e])
    Sp[0] = get_nevens(c[e])


    for e in E[1:]:
        for x in range(0, M):
            Sn[x^e] += Sp[x] * get_nodds(c[e])
            Sn[x] += Sp[x] * get_nevens(c[e])

        # next
        Sp = Sn
        Sn = [0] * M

    result = 0 
    for e in range(0, M):
        if isPrime(e):
            result += Sp[e]

    return int(result%(1e9 + 7))
'''
def isPrime(x):
    if x < 3500 or x > 4500:
        print('error')
        return 'unknown'
    if x % 2 == 0:
        return False
    for i in range(3,int(x ** 0.5) + 1,2):
        if x % i == 0:
            return False
    return True

def primeXor(a):
    ans = 0
    for x in set(a):
        if isPrime(x):
            ans += 1
    toXor = []
    cur = 0
    length = len(a)
    
    ans += 1
    return ans % (10 ** 9 + 7)
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)

        fptr.write(str(result) + '\n')

    fptr.close()
