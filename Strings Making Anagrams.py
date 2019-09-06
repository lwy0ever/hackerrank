#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    A = Counter(a)
    B = Counter(b)
    return len(list((A | B).elements())) - len(list((A & B).elements()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
