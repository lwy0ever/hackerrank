#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    l = len(w)
    if l == 1:
        return 'no answer'
    for i in range(l - 1,0,-1):
        #print(i,w[i - 1] , w[i])
        if w[i - 1] < w[i]:
            break
    else:
        return 'no answer'
    #print(i)
    c = w[i - 1]
    mark = 0
    mi = 'z'
    for j in range(i,l):
        if w[j] > c and w[j] <= mi:
            mi = w[j]
            mark = j
    #print(i - 1,mark)
    return w[:i - 1] + w[mark] + ''.join(sorted(w[i - 1:mark] + w[mark + 1:l]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
