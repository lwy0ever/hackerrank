#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    for c in s.lower():
        if c in alphabet:
            alphabet.remove(c)
            if not alphabet:
                return 'pangram'
    return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
