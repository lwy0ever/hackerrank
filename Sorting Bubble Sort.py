#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    counter = 0
    for i in range(len(a) - 1):
        for j in range(i + 1,len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
                counter += 1
    print('Array is sorted in %d swaps.' % (counter))
    print('First Element: %d' % (a[0]))
    print('Last Element: %d' % (a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
