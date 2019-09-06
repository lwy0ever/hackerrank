#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    ans = 0
    page = 0
    for problem in arr:
        proNum = 0
        while proNum < problem:
            #print(proNum)
            if proNum % k == 0:
                page += 1
                #print('new page('+str(page)+')')
            if proNum + 1 == page:
                ans += 1
            proNum += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
