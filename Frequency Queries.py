#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    ans = []
    c = Counter()
    times = Counter()
    for op,data in queries:
        if op == 1:
            times[c[data]] -= 1
            c[data] += 1
            times[c[data]] += 1
        elif op == 2:
            if c[data] > 0:
                times[c[data]] -= 1
                c[data] -= 1
                times[c[data]] += 1
        elif op == 3:
            if times[data] > 0:
                ans.append(1)
            else:
                ans.append(0)
        #print(c,times)
    return ans
'''
    ans = []
    queue = []
    for q in queries:
        if q[0] == 1:
            queue.append(q[1])
        elif q[0] == 2:
            if q[1] in queue:
                queue.remove(q[1])
        elif q[0] == 3:
            cnt = Counter(queue)
            for v in cnt.values():
                if v == q[1]:
                    ans.append(1)
                    break
            else:
                ans.append(0)
    return ans
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
