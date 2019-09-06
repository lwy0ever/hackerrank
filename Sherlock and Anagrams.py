#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    r = 0
    for length in range(1,len(s)):
        strs = [''.join(sorted(s[pos:pos + length])) for pos in range(0,len(s) - length + 1)]
        cnt = Counter(strs)
        for k in cnt:
            r += cnt[k] * (cnt[k] - 1) // 2
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
