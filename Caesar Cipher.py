#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    charL = 'abcdefghijklmnopqrstuvwxyz'
    charU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = []
    for c in s:
        if c in charL:
            ans.append(charL[(charL.index(c) + k) % 26])
        elif c in charU:
            ans.append(charU[(charU.index(c) + k) % 26])
        else:
            ans.append(c)
    return ''.join(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
