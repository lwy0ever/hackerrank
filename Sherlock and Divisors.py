#!/bin/python3

import os
import sys

#
# Complete the divisors function below.
#
def divisors(n):
    #
    # Write your code here.
    #
    ans = 0
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0:
            if i & 1 == 0:
                ans += 1
            if (n // i) & 1 == 0:
                ans += 1
    if i * i == n and i & 1 == 0:
        ans -= 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
