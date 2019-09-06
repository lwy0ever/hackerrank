#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    u = set()
    pre = ''
    cnt = 0
    base = ord('a') - 1
    for c in s:
        if c == pre:
            cnt += 1
        else:
            pre = c
            cnt = 1
        u.add((ord(c) - base) * cnt)
    ans = []
    for q in queries:
        if q in u:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
