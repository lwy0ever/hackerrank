#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):
    ans = 'Prime'
    if n == 1:
        return 'Not prime'
    if n in (2,3):
        return ans
    if n % 2 == 0:
        return 'Not prime'
    for i in range(3,int(n ** 0.5) + 1,2):
        if n % i == 0:
            return 'Not prime'
    else:
        return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
