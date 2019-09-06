#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    b = bin(n)
    subtimes = b.count('1') - 1
    divtimes = 0
    p = -1
    while b[p] == '0':
        divtimes += 1
        p -= 1
    if (subtimes + divtimes) % 2 == 0:
        return 'Richard'
    else:
        return 'Louise'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
