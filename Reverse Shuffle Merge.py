#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    cnt = Counter(s)
    req = Counter({k:v // 2 for k,v in cnt.items()})
    #print(req)
    rs = s[::-1]
    ic = ord('a')
    imax = ord('z') + 1
    pos = -1
    ans = ''
    while ic < imax:
        c = chr(ic)
        if c not in list(+req):
            ic += 1
            continue
        i = rs.find(c,pos + 1)
        #print(rs,pos + 1,c,i,req)
        if len(+(req - Counter(rs[i:]))) > 0:
            # not enough characters behind,find bigger character
            ic += 1
        else:
            # there are enough characters behind
            ans += c
            pos = i     #new position to find
            req[c] -= 1 #reduct request
            ic = ord('a')   #find from a to z
            if len(+req) == 0:  #find all
                return ans
        #print(rs,c,req)
        if ic >= imax:
            ic -= 26

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
