#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key = lambda element:(element[1],element[0]),reverse = True)
    #print(contests)
    ans = 0
    for e in contests[:k]:
        ans += e[0] # important to lose, base on k <= N
    for e in contests[k:]:
        if e[1] == 0:
            ans += e[0] # unimportant to lose
        else:
            ans -= e[0] # important to win
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
