#!/bin/python

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    n = len(s)
    l = 0
    r = n - 1
    while s[l] == s[r] and l <= r:
        l += 1
        r -= 1
    print(l,r)
    if l == r:
        return -1
    #print(s[l + 1:r + 1],s[r:l:-1])
    #print(s[l:r],s[r - 1 - n:l - 1 - n:-1])
    if s[l + 1:r + 1] == s[r:l:-1]:
        return l
    if s[l:r] == s[r - 1 - n:l - 1 - n:-1]:
        return r
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
