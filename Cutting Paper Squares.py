#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, m):
    #return min(n - 1 + n * (m - 1),m - 1 + m * (n - 1))
    return n * m - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
