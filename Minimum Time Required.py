#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    ans = 0
    #left = math.ceil(goal * min(machines) / len(machines))
    rate = [1 / m for m in machines]
    sum_rate = sum(rate)
    left = math.ceil(goal / sum_rate) - 1
    right = math.ceil(goal * max(machines) / len(machines)) + 1
    #print(left,right)
    while left < right:
        days = (left + right) // 2
        #print(left,days,right)
        total = 0
        for m in machines:
            total += (days // m)
        '''if total == goal:
            ans = days
            break'''
        if total >= goal:
            right = days
        else:
            left = days + 1
    '''while True:
        total = 0
        for m in machines:
            total += (ans - 1) // m
        if total == goal:
            ans -= 1
        else:
            break'''
    #print(left,right)
    ans = left
    return int(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
