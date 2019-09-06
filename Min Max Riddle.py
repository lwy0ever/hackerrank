#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the riddle function below.
def riddle(arr):
    # complete this function
    ans = []
    length = len(arr)
    # Think about how to identify the largest window a number is the minimum for (e.g. for the sequence 11 2 3 14 5 2 11 12 we would make a map of number -> window_size as value_window = {11: 2, 2: 8, 3: 3, 14: 1, 5: 2, 12: 1})
    arr.append(-1)  # because arr[i] >= 0,-1 is safe
    stack = []  #(value,left_index)
    value_window = defaultdict(int)
    for i in range(len(arr)):
        left_index = i
        while stack and arr[i] <= stack[-1][0]:
            v,li = stack.pop()
            value_window[arr[i]] = max(value_window[arr[i]],i - li + 1)
            value_window[v] = max(value_window[v],i - li)
            left_index = li
        stack.append((arr[i],left_index))
        #print(stack,value_window)
    del value_window[-1]
    #print(stack,value_window)
    #Invert the value_window hashmap breaking ties by taking the maximum value to store a mapping of windowsize -> window_maxvalue (continuing with example above inverted_windows = {1: 14, 8:2, 3:3, 2:11}
    window_maxvalue = defaultdict(int)
    for value in value_window:
        window_maxvalue[value_window[value]] = max(window_maxvalue[value_window[value]],value)
    #print(window_maxvalue)
    #starting from w=len(arr) iterate down to a window size of 1, looking up the corresponding values in inverted_windows and fill missing values with the previous largest window value (continuing with the example result = [2, 2, 2, 2, 2, 3, 11, 14] )
    ans = [window_maxvalue[length]]
    for i in range(length - 1,0,-1):
        if window_maxvalue[i] < ans[-1]:
            ans.append(ans[-1])
        else:
            ans.append(window_maxvalue[i])
        #print(i,ans[-1])
    #print(ans)
    return ans[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
