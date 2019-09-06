#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    description = re.findall(r'(U+|D+)',s)
    height = 0
    v = 0
    for e in description:
        if e[0] == 'U':
            height += len(e)
        else:
            if height >= 0 and height < len(e):
                v += 1
            height -= len(e)
    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
