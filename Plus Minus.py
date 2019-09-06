#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    r = [0,0,0]
    for a in arr:
        if a > 0:
            r[0] += 1
        elif a < 0:
            r[1] += 1
        else:
            r[2] += 1
    for rr in r:
        print(rr / len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
