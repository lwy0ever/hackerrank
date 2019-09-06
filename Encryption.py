#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(' ','')
    l = len(s)
    #r = math.floor(l ** 0.5)
    c = math.ceil(l ** 0.5)
    #print(r,c)
    ans = []
    for i in range(c):
        #print(i,s[i::c])
        ans.append(s[i::c])
    return ' '.join(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
