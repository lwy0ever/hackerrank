#!/bin/python3

import os
import sys

import time
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    return time.strftime('%H:%M:%S',time.strptime(s,'%I:%M:%S%p'))
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
