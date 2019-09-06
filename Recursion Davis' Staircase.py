#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def CombinationNumber(m,n):
    mul = 1
    div = 1
    for i in range(m):
        mul *= (n - i)
        div *= (i + 1)
    return mul // div

def stepPerms(n):
    print(n)
    ans = 0
    for n3 in range(n // 3 + 1):
        for n2 in range((n - n3 * 3) // 2 + 1):
            n1 = n - n3 * 3 - n2 * 2
            #print(n1,n2,n3)
            total = n1 + n2 + n3
            ans += CombinationNumber(n3,total) * CombinationNumber(n2,total - n3)
    return ans % (10 ** 10 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
