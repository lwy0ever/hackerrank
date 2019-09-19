#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
from collections import Counter
def makingAnagrams(s1, s2):
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    #print(list((+(cnt1 - cnt2)).values()))
    return sum(list((+(cnt1 - cnt2)).values())) + sum(list((+(cnt2 - cnt1)).values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
