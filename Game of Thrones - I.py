#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the gameOfThrones function below.
def gameOfThrones(s):
    cnt = Counter(s)
    total = 0
    for v in cnt.values():
        if v % 2 != 0:
            total += 1
            if total > 1:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
