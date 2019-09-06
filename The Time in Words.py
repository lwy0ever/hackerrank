#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    NUMBER_CONSTANT = {0:"zero ", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen" };
    IN_HUNDRED_CONSTANT = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
    #BASE_CONSTANT = {0:" ", 1:"hundred", 2:"thousand", 3:"million", 4:"billion"};
    if m == 0:
        return NUMBER_CONSTANT[h] + ' o\' clock'
    if m <= 30:
        mid = ' past '
    else:
        m = 60 - m
        h = (h + 1) % 12
        mid = ' to '
    #print(h,m)
    if m == 15:
        return 'quarter' + mid + NUMBER_CONSTANT[h]
    if m == 30:
        return 'half' + mid + NUMBER_CONSTANT[h]
    if m == 1:
        mid = ' minute' + mid
    else:
        mid = ' minutes' + mid
    if m < 20:
        return NUMBER_CONSTANT[m] + mid + NUMBER_CONSTANT[h]
    else:   # m >= 20
        return IN_HUNDRED_CONSTANT[2] + ' ' + NUMBER_CONSTANT[m % 10] + mid + NUMBER_CONSTANT[h]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
