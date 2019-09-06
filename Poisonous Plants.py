#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    ans = 0  #max
    length = len(p)
    # Number of days the plant[i] will survive
    days = [0] * length
    # We keep in the stack the possible killers for plants that we haven't seen yet.
    stack = []
    for i in range(0,length):
        while stack and p[stack[-1]] >= p[i]:
            # The daysAlive for plant[i] is the max
            # days of all the plants greater than plant[i]
            # that are in the stack (possible killers) because
            # they all need to die before plant[i] dies.
            # Later we add 1 because it dies after the
            # other plants have died.
            days[i] = max(days[i], days[stack.pop()])
        if stack:
            # plant[i] will die, because it exited the while
            # loop and a lower plant was found
            days[i] += 1
        else:
            # when plant[i] is the minimum seen until now.
            # It will never die.
            days[i] = 0
        ans = max(ans, days[i])
        # plant[i] is a possible killer because there 
        # may be plants greater than this that we have 
        # not seen yet
        stack.append(i)
        #print(i,p[i],days,stack)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
