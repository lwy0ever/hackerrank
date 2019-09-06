#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    k = len(keyboards)
    d = len(drives)
    keyboards.sort()
    drives.sort()
    for i in range(k):
        keyboards[i] = b - keyboards[i]
    ans = -1
    j = d - 1
    for i in range(k):
        while j >= 0:
            if keyboards[i] >= drives[j]:
                ans = max(ans,b - keyboards[i] + drives[j])
                break
            j -= 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
