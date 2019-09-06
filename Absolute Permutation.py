#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return range(1,n + 1)
    elif n % (2*k) != 0 or 2 * k > n: 
        return [-1]
    return [(i+1)+(1 if (i//k)%2==0 else -1)*k for i in range(n)]
    '''
    if k == 0:
        return range(1,n + 1)
    ans = [-1] * n
    for i in range(1,n + 1):
        if ans[i - 1] == -1:
            if i + k <= n:
                ans[i - 1] = i + k
                if ans[i + k - 1] == -1:
                    ans[i + k - 1] = i
                else:
                    return [-1]
            elif i - k > 0:
                ans[i - 1] = i - k
                if ans[i - k - 1] == -1:
                    ans[i - k - 1] = i
                else:
                    return [-1]
            else:
                return [-1]
    return ans
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
