#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year != 1918:
        if year % 4 == 0:
            if year < 1918: # leap year
                return '12.09.%d' % (year)
            else:   # year > 1918
                if year % 100 == 0:
                    if year % 400 == 0: # leap year
                        return '12.09.%d' % (year)
                else: # leap year
                    return '12.09.%d' % (year)
    else:   #year == 1918
        return '26.09.%d' % (year)
    return '13.09.%d' % (year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
