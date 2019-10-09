#!/bin/python3

import math
import os
import random
import re
import sys

# code here
def reverseGame(n,k):
    # 最终的队列是:
    # n - 1,0,n - 2,1,n - 3,2,...
    if (k + 1) * 2 >= n:
        return (n - k - 1) * 2
    else:
        return (k + 1) * 2 - 1


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(reverseGame(n,k))
