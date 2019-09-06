#!/bin/python3

import os
import sys

from collections import defaultdict
# Complete the solve function below.
def solve(arr, queries):
    # similar to https://www.hackerrank.com/challenges/min-max-riddle/problem
    ans = []
    length = len(arr)
    arr.append(10 ** 6)  # because arr[i] < 10 ** 6,10 ** 6 is safe
    stack = []  #(value,left_index)
    value_window = defaultdict(int)
    for i in range(len(arr)):
        left_index = i
        while stack and arr[i] >= stack[-1][0]:
            v,li = stack.pop()
            value_window[arr[i]] = max(value_window[arr[i]],i - li + 1)
            value_window[v] = max(value_window[v],i - li)
            left_index = li
        stack.append((arr[i],left_index))
        #print(stack,value_window)
    del value_window[10 ** 6]
    #print(value_window)

    window_minvalue = defaultdict(int)
    for value in value_window:
        if window_minvalue[value_window[value]] == 0:
            window_minvalue[value_window[value]] = value
        else:
            window_minvalue[value_window[value]] = min(window_minvalue[value_window[value]],value)
    #print(window_minvalue)

    allAns = []
    allAns = [window_minvalue[length]]
    for i in range(length - 1,0,-1):
        if window_minvalue[i] == 0 or window_minvalue[i] > allAns[-1]:
            allAns.append(allAns[-1])
        else:
            allAns.append(window_minvalue[i])
        #print(i,window_minvalue,allAns)
    #print(allAns)
    for q in queries:
        ans.append(allAns[-q])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
