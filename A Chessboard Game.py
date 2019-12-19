#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chessboardGame function below.
def chessboardGame(x, y):
    di = [(-2,1),(-2,-1),(1,-2),(-1,-2)]

    def check(x,y): # True表示胜,False表示负
        if 1 <= x <= 15 and 1 <= y <= 15:
            for a,b in di:
                if not check(x + a,y + b):  # 自己有一种不出界的方案即可
                    return True
            False
        else:   # 对手已经走出界
            return True
    
    return 'First' if check(x,y) else 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()
