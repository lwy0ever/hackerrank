#!/bin/python3

import os
import sys

#
# Complete the restaurant function below.
#
def restaurant(l, b):
    #
    # Write your code here.
    #
    def lcd(l,b):   #求最大公约数
        d,m = divmod(l,b)
        if m == 0:
            return b
        else:
            return lcd(b,m)

    return l * b // (lcd(l,b) ** 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
