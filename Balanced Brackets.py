#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    brackets = '()[]{}'
    for c in s:
        if c in brackets[0::2]:
            stack.append(c)
        else:
            if len(stack) > 0:
                l = stack.pop()
                if brackets.index(c) != brackets.index(l) + 1:
                    break
            else:
                break
    else:
        if len(stack) == 0:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
