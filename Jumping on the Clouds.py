#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    j = len(c) - 1
    i = 0
    while i < len(c) - 2:
        #print(i,j,c[i + 2],(c[i + 2] == 0))
        if c[i + 2] == 0:
            j -= 1
            i += 1
        i += 1
    return j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
