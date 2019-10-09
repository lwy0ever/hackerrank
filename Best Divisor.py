#!/bin/python3

import math
import os
import random
import re
import sys

# code here
def findDivisors(n):
    divisors = set()
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def findBest(divisors):
    best = [1,1]
    for d in divisors:
        s = 0
        t = d
        while t > 0:
            t,m = divmod(t,10)
            s += m
        if s > best[0]:
            best = [s,d]
        elif s == best[0]:
            best[1] = min(d,best[1])
        #print(d,s,best)
    return best[1]

if __name__ == '__main__':
    n = int(input())

    divisors = findDivisors(n)
    print(findBest(divisors))
