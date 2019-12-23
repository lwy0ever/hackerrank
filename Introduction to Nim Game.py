#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    # 异或和为0的情况下,second获胜
    # 证明:假设初始异或和为0,先手选择一堆x,拿完剩余y,剩余堆的异或和变为x ^ y
    # 那么一定可以找到一堆a,a二进制中最高位等于x ^ y的最高位,即a >= a^x^y
    # 那么就可以将a变为a^x^y,则异或和重变为0,所以先手必败
    # 若初始异或和>0,则可按上述后手操作将异或和转为0,从而必胜
    ans = 0
    for p in pile:
        ans ^= p
    if ans:
        return 'First'
    else:
        return 'Second'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
