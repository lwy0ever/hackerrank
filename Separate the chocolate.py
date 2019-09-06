#!/bin/python3

# unfinished version

import os
import sys

#
# Complete the separateTheChocolate function below.
#
def separateTheChocolate(chocolate):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mnk = input().split()

    m = int(mnk[0])

    n = int(mnk[1])

    k = int(mnk[2])

    chocolate = []

    for _ in range(m):
        chocolate_item = input()
        chocolate.append(chocolate_item)

    result = separateTheChocolate(chocolate)

    fptr.write(str(result) + '\n')

    fptr.close()
