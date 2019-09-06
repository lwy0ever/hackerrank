#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    c = [0] * n
    t = [0] * n
    for i in range(n):
        for j in range(n):
            c[i] += container[i][j]
            t[j] += container[i][j]
    c.sort()
    t.sort()
    for i in range(n):
        if c[i] != t[i]:
            return 'Impossible'
    return 'Possible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
