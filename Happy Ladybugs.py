#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the happyLadybugs function below.
def happyLadybugs(b):
    cnt = Counter(b)
    if cnt['_'] > 0:
        del cnt['_']
        for k in cnt.keys():
            if cnt[k] <= 1:
                return 'NO'
        return 'YES'
    else:
        pre = ''
        count = 2
        for c in b:
            if c == pre:
                count += 1
            else:
                if count == 1:
                    return 'NO'
                pre = c
                count = 1
        if count > 1:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
