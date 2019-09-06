#!/bin/python3

import math
import os
import random
import re
import sys

def solution(n,k):
    #When k is ODD , k-1 is EVEN , k-1 can always be reached by (k-1) & k.
    #When k is EVEN , k-1 is ODD , k-1 can only be reached if and only if ((k-1) | k) <= n is TRUE
    print(k-1 if (k-1) | k <= n else k-2)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        solution(n,k)
