#!/bin/python3

import os
import sys

#
# Complete the buildString function below.
#
def buildString(a, b, s):
    #
    # Write your code here.
    #
    n = len(s)
    cost = 0
    ns = ''
    l = 0
    while l < n:
        print(ns,cost)
        for i in range(min(l,n - l),0,-1):
            if a * i < b:
                cost += a
                ns += s[l]
                break
            if ns.find(s[l:l + i]) >= 0:
                cost += b
                ns += s[l:l + i]
                break
        else:
            cost += a
            ns += s[l]
        l = len(ns)
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nab = input().split()

        n = int(nab[0])

        a = int(nab[1])

        b = int(nab[2])

        s = input()

        result = buildString(a, b, s)
        fptr.write(str(result) + '\n')

    fptr.close()
