#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort(reverse = True)
    b.sort(reverse = True)
    c.sort(reverse = True)
    lena = len(a)
    lenb = len(b)
    lenc = len(c)
    #print(a,lena,b,lenb,c,lenc)
    ans = 0
    j = 0
    i,k = 0,0
    while j < lenb:
        while i < lena and a[i] > b[j]:
            i += 1
        while k < lenc and c[k] > b[j]:
            k += 1
        ans += (lena - i) * (lenc - k)
        j += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
