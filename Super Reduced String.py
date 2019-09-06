#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    while True:
        n = len(s)
        s = re.sub(r'(.)\1','',s)
        if n == len(s):
            return s if s else 'Empty String'
    '''
    n = len(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
    return s if s else 'Empty String'
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
