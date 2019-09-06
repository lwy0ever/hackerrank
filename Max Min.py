#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    ans = arr[k - 1] - arr[0]
    for i in range(k,len(arr)):
        if ans > arr[i] - arr[i - k + 1]:
            ans = arr[i] - arr[i - k + 1]
    return ans
    ''' timeout
    cnt = list(Counter(arr).items())
    cnt.sort()
    #print(cnt)
    ans = cnt[-1][0] - cnt[0][0]
    #print(ans)
    for i in range(len(cnt) - 1):
        if cnt[i][1] >= k:
            ans = 0
            break
        c = cnt[i][1]
        for j in range(i + 1,len(cnt)):
            c += cnt[j][1]
            if c >= k:
                if ans > cnt[j][0] - cnt[i][0]:
                    ans = cnt[j][0] - cnt[i][0]
                    break
    return ans
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
