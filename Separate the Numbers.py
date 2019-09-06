#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    ans = 'NO'
    n = len(s)
    for l in range(1,n // 2 + 1):
        if l != 1 and s[0] == '0':
            print('NO')
            return
        st = int(s[0:l])
        sPos = 0
        t = st
        length = l
        #print(st,l)
        while sPos < n:
            if s[sPos:sPos + length] == str(t):
                t += 1
                sPos += length
                length = len(str(t))
            else:
                break
        else:
            if sPos == n:
                print('YES',st)
                return
    print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
