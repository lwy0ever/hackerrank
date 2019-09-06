#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    sos = 'SOS'
    ans = 0
    i = 0
    for c in s:
        if sos[i] != c:
            ans += 1
        i += 1
        i %= 3
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
