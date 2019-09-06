#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringReduction function below.
from collections import Counter
def stringReduction(s):
    # 不知道怎么证明:
    # 1,如果是单一字母,则最终长度为len(s)
    # 2,如果a,b,c的数量同为奇数或者同为偶数,则最终长度为2
    # 3,否则,最终长度为1
    cnt = Counter(s)
    if len(cnt) == 1:
        return list(cnt.values())[0]
    if cnt['a'] & 1 == cnt['b'] & 1 == cnt['c'] & 1:
        return 2
    else:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
