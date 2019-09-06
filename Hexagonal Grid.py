#!/bin/python3

import os
import sys

#
# Complete the hexagonalGrid function below.
#
def hexagonalGrid(a, b):
    #
    # Write your code here.
    #
    n = len(a)
    pre = '0'
    cnt = 0
    for i in range(n):
        if a[i] == '0':
            pre = '0'
            cnt ^= 1
        else:   # a[i] == '1'
            if pre == '1' and cnt == 1:
                return 'NO'
            pre = '1'
        #print('a',i)
        if b[i] == '0':
            pre = '0'
            cnt ^= 1
        else:   # b[i] == '1'
            if pre == '1' and cnt == 1:
                return 'NO'
            pre = '1'
        #print('b',i)
    #print(cnt)
    if cnt == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = input()

        b = input()

        result = hexagonalGrid(a, b)

        fptr.write(result + '\n')

    fptr.close()
