#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    n = len(petrolpumps)
    s = [0] * n
    ans = 0
    for i in range(n):
        s[i] = s[i - 1] + petrolpumps[i][0] - petrolpumps[i][1]
        if s[i] < 0:
            ans = i + 1
            s[i] = 0
    #print(s)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
