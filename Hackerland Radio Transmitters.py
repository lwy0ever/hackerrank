#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    ans = 0
    x.sort()
    i = 0
    while i < len(x):
        #print(i)
        t = x[i]
        while i < len(x) and x[i] - t <= k:
            i += 1
        t = x[i - 1]    # build a transmitters
        ans += 1
        while i < len(x) and x[i] - t <= k:
            i += 1
    return ans
    '''
    tester = x[0]
    testLeft = True
    for i in range(1,len(x)):
        if testLeft:
            if x[i] - tester > k:
                t = x[i - 1]    # build a transmitters
                #print('t:',t)
                ans += 1
                testLeft = False
        if not testLeft:
            if x[i] - t > k:
                tester = x[i]
                #print('tester:',tester)
                testLeft = True
    if testLeft:
        ans += 1
    return ans
    '''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
