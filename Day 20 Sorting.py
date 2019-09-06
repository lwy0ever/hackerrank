#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(n):
    canBreak = True
    for j in range(n-1):
        if a[j] > a[j + 1]:
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t
            canBreak = False
            numSwaps += 1
    if canBreak:
        break
print('Array is sorted in %d swaps.' % (numSwaps))
print('First Element: %d' % (a[0]))
print('Last Element: %d' % (a[n - 1]))
