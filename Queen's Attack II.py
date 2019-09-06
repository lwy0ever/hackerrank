#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    left = c_q - 1
    right = n - c_q
    top = n - r_q
    bottom = r_q - 1
    leftTop = min(left,top)
    leftBottom = min(left,bottom)
    rightTop = min(right,top)
    rightBottom = min(right,bottom)
    for r,c in obstacles:
        rr = r - r_q
        cc = c - c_q
        if rr == 0:
            if cc > 0:
                right = min(right,cc - 1)
            else:   # cc < 0
                left = min(left,-cc - 1)
        if cc == 0:
            if rr > 0:
                top = min(top,rr - 1)
            else:   # rr < 0
                bottom = min(top,-rr - 1)
        if rr == cc:
            if rr > 0:  # rightTop
                rightTop = min(rightTop,rr - 1)
            else:   # leftBottom
                leftBottom = min(leftBottom,-rr - 1)
        if rr + cc == 0:
            if rr > 0:  # leftTop
                leftTop = min(leftTop,rr - 1)
            else:   # rightBottom
                rightBottom = min(rightBottom,cc - 1)
    #print(left,right,top,bottom,leftTop,leftBottom,rightTop,rightBottom)
    return left + right + top + bottom + leftTop + leftBottom + rightTop + rightBottom

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
