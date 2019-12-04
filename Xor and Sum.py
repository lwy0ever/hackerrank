#!/bin/python3

import os
import sys

#
# Complete the xorAndSum function below.
#
def xorAndSum(a, b):
    #
    # Write your code here.
    #
    #print(a,b)
    a = int(a,2)
    b = int(b,2)
    n = 314159 + 1
    ans = 0
    for i in range(n):
        ans += a ^ (b << i)
    return ans % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
