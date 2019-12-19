#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the towerBreakers function below.
def towerBreakers(n, m):
    # 如果n % 2 == 0,player1操作tower[i],player2完全模仿player1操作tower[i >> 1 << 1 | (~(i & 1))]即可
    if n & 1 == 0:
        return 2
    # 如果n % 2 == 1,player1将tower[n - 1]减到1,使tower[n - 1]不能再被操作
    # 剩下n - 1个((n - 1) % 2 == 0),回归上面的情况
    if m > 1:
        return 1
    else:
        return 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
