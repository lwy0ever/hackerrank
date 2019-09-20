#!/bin/python3

#import math
import os
#import random
#import re
#import sys

# Complete the insertionSort function below.
def insertionSort(arr):
    import bisect
    from array import array
    ans = 0
    data = array('I')
    #n = 0
    for i,a in enumerate(arr):
        t = bisect.bisect_right(data,a)
        #bisect.insort_right(data,a)
        data.insert(t,a)
        ans += i - t
        #n += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
