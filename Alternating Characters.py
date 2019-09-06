#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    ans = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            ans += 1
    return ans
    '''
    r = re.findall(r'A+|B+',s)
    return len(s) - len(r)
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
