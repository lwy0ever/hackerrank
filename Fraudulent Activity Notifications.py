#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def median(counts,mid):
    # s means sum
    s = 0
    for k in mid:
        i = mid[k]['pos']
        # position moveleft
        while mid[k]['left'] >= k:
            mid[k]['left'] -= counts[i - 1]
            i -= 1
        # position moveright
        while mid[k]['left'] + counts[i] < k:
            mid[k]['left'] += counts[i]
            i += 1
        # new postion
        mid[k]['pos'] = i
        #print(mid)
        s += mid[k]['pos']
    return s / len(mid)

def activityNotifications(expenditure, d):
    counts = [0] * 201
    for e in expenditure[:d]:
        counts[e] += 1
    mid = {}
    # if d is odd,len(mid) is 1; if d is even,len(mid) is 2
    for i in range((d + 1) // 2,(d + 2) // 2 + 1):
        # initial the median position and how many in the left
        mid[i] = {'pos':0,'left':0}
    avg = median(counts,mid)

    notice = 0
    for i in range(d,len(expenditure)):
        if expenditure[i] >= avg * 2:
            notice += 1
        counts[expenditure[i]] += 1
        counts[expenditure[i - d]] -= 1
        for k in mid:
            if expenditure[i] < mid[k]['pos']:
                mid[k]['left'] += 1
            if expenditure[i - d] < mid[k]['pos']:
                mid[k]['left'] -= 1
        avg = median(counts,mid)
    return notice

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
