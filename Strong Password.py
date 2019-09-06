#!/bin/python2

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = '0123456789'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_characters = '!@#$%^&*()-+'
    needType = [1] * 4
    for c in password:
        if c in numbers:
            needType[0] = 0
        if c in lower_case:
            needType[1] = 0
        if c in upper_case:
            needType[2] = 0
        if c in special_characters:
            needType[3] = 0
    return 6 - n if n + sum(needType) < 6 else sum(needType)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    password = raw_input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
