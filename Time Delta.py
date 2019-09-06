#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt
#import time

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    #print(dt.strptime(t1,fmt))
    #print(dt.strptime(t2,fmt))
    return(str(int(abs(dt.strptime(t1,fmt).timestamp() - dt.strptime(t2,fmt).timestamp()))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
