#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    ans = 0
    pre2 = ['',0]
    pre1 = ['',0]
    pre0 = ['',0]
    for i in range(len(s)):
        c = s[i]
        if c == pre0[0]:
            pre0[1] += 1
        else:
            pre2 = pre1
            pre1 = pre0
            pre0 = [c,1]
        #print(pre2,pre1,pre0,c,ans)
        if pre1[1] == 1 and pre2[0] == pre0[0] and pre2[1] >= pre0[1]:    # All characters except the middle one are the same
            ans += 1
        if pre0[1] == 1:
            ans += (pre1[1] + 1) * pre1[1] // 2    # All of the characters are the same
    ans += (pre0[1] + 1) * pre0[1] // 2
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
