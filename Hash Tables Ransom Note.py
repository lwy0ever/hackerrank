#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mc = Counter(magazine)
    nc = Counter(note)
    #print(mc)
    mc.subtract(nc)
    #print(mc)
    for t in mc:
        if mc[t] < 0:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
