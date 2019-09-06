#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the isValid function below.
def isValid(s):
    cnt = Counter(s)
    v = list(cnt.values())
    x = max(v)
    n = min(v)
    if x == n or (x - n == 1 and v.count(x) == 1) or (sum(v) - 1 == x * len(v) - x and n == 1 and v.count(n) == 1):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
