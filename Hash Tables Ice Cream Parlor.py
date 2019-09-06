#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost = [0] + cost
    d = defaultdict(int)
    for i in range(1, len(cost)):
        if d[cost[i]] != 0:
            print(d[cost[i]], i)
        d[money - cost[i]] = i
    #print(d)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
