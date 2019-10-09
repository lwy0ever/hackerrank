#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
#from collections import Counter
def stringConstruction(s):
    # 最小的substring就是一个字母,所以,只要是已经存在的字母,都可以no charge的添加
    return len(set(s))
    #return len(Counter(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
