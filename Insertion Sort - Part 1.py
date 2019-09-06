#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    c = arr[-1]
    i = n - 2
    while i >= 0 and c < arr[i]:
        arr[i + 1] = arr[i]
        print(' '.join(map(str,arr)))
        i -= 1
    arr[i + 1] = c
    print(' '.join(map(str,arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
