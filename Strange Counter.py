#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    st = 3
    while t > st:
        t = t - st
        st <<= 1
    return st - t + 1
    '''
    C = 3
    st = 1
    while ((st << 1) - 1) * C < t:
        st <<= 1
    #st >>= 1
    i = (st << 1) - 1
    #print(i * C,st * C)
    return i * C - t + 1
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
