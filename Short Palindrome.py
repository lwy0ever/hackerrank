#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the shortPalindrome function below.
def shortPalindrome(s):
    A = [0] * 26
    AB = [[0] * 26 for _ in range(26)]
    #ABB = [[[0] * 26 for _ in range(26)] for _ in range(26)]
    # ABB的情况，不需要关心B，简化为一维数组
    ABB = [0] * 26
    base = ord('a')
    ans = 0
    for c in s:
        i = ord(c) - base
        ans += ABB[i]
        for j in range(26):
            #ans += ABB[i][j][j]
            # ABB的情况，不需要关心B，简化为一维数组，并且移到循环外(line 20)
            #ABB[j][i][i] += AB[j][i]
            ABB[j] += AB[j][i]
            AB[j][i] += A[j]
        A[i] += 1
    return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
