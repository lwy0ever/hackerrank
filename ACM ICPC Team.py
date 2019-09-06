#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
from itertools import combinations
def acmTeam(topic):
    comb = combinations(topic,2)
    ma = 0
    counter = 0
    for i in comb:
        n = str(bin(int(i[0],2) | int(i[1],2)))[2:].count('1')
        if n > ma:
            ma = n
            counter = 1
        elif n == ma:
            counter += 1
    return ma,counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
