#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    s = list(s)
    mark = [False] * ((n - 1) // 2 + 1)
    for i in range((n - 1) // 2 + 1):
        if s[i] != s[-i - 1]:
            k -= 1
            s[i] = s[-i - 1] = max(s[i],s[-i - 1])
            mark[i] = True
        if k < 0:
            return '-1'
    #print(k)
    i = 0
    while k > 0 and i < (n - 1) // 2 + 1:
        if s[i] != '9':
            if mark[i] or i * 2 + 1 == n:
                s[i] = s[-i - 1] = '9'
                k -= 1
            elif k >= 2:
                s[i] = s[-i - 1] = '9'
                k -= 2
        i += 1
    return ''.join(s)

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
