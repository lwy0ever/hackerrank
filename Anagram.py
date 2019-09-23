#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
from collections import Counter
def anagram(s):
    n = len(s)
    if n & 1 == 1:
        return -1
    cnt1 = Counter(s[:n // 2])
    cnt2 = Counter(s[n // 2:])
    ans = 0
    for v in (+(cnt1 - cnt2)).values():
        ans += v
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
