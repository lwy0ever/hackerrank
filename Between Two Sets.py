#!/bin/python3

import math
import os
import random
import re
import sys

# 求最大公约数
# 欧几里得法(辗转相除法)
# 这条算法基于一个定理：两个正整数a和b（a>b），它们的最大公约数等于a除以b的余数c和b之间的最大公约数
def getmaxcommonfactor(x,y):
    while y > 0:
        t = x % y
        x = y
        y = t
    return x

# 求最小公倍数
def getmincommontimes(x,y):
    return x * y // getmaxcommonfactor(max(x,y),min(x,y))
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    m = a[0]
    for i in range(1,len(a)):
        m = getmincommontimes(m,a[i])
        #print(m)
    b.sort()
    ans = 0
    for i in range(b[0],m - 1,-m):
        #print(i)
        for ib in b:
            if ib % i > 0:
                break
        else:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
