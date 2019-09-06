#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    # https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    length1 = len(s1)    # len(s1) == len(s2)
    length2 = len(s2)    # len(s1) == len(s2)
    pre = [0] * (length2 + 1)
    cur = [0] * (length2 + 1)
    for i in range(length1):
        pre,cur = cur,pre
        for j in range(length2):
            # i and j are used to step forward in each string.
            # Now check if s1[i] and s2[j] are equal 
            if s1[i] == s2[j]:
                ''' Now we have found one longer sequence
                than what we had previously found.
                so add 1 to the length of previous longest
                sequence which we could have found at
                earliest previous position of each string'''
                cur[j + 1] = pre[j] + 1
            else:
                # if not matching pair, get the biggest previous value
                cur[j + 1] = (pre[j + 1] if pre[j + 1] > cur[j] else cur[j])
        #print(pre,cur)
    return cur[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
