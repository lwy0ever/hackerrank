#!/bin/python3

#import math
import os
'''
import random
import re
import sys
'''

# Complete the countInversions function below.
def merge(left, right):
    steps, l, r, result, left_len, right_len = 0, 0, 0, [], len(left), len(right)
    while l < left_len and r < right_len:
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            steps += left_len - l
    result += left[l:]
    result += right[r:]    
    return steps, result
    
def mergesort(arr):
    n = len(arr)
    if n > 2:
        mid = n // 2
        left,right = arr[:mid],arr[mid:]
        left_steps = mergesort(left)
        right_steps = mergesort(right)
        '''
        steps, result = merge(left, right)
        or
        merge without function
        '''
        steps, l, r, left_len, right_len = 0, 0, 0, len(left), len(right)
        i = 0
        while l < left_len and r < right_len:
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
                steps += left_len - l
            i += 1
        while l < left_len:
            arr[i] = left[l]
            i += 1
            l += 1
        while r < right_len:
            arr[i] = right[r]
            i += 1
            r += 1
        return steps + left_steps + right_steps
    if n == 2:
        if arr[0] > arr[1]:
            arr[0],arr[1] = arr[1],arr[0]
            return 1
    return 0

def countInversions(arr):
    #result = []
    return mergesort(arr)
    ''' use bisect
    import bisect
    n = []
    count = 0
    for i in arr[::-1]:
        x = bisect.bisect_left(n,i)
        n.insert(x,i)
        count += x
    return count
    '''
    '''
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1,len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
