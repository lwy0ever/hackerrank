#!/bin/python3

import os
import sys

# Complete the solve function below.
def gcd(x,y):
    if y == 0:
        return x
    d,m = divmod(x,y)
    return gcd(y,m)

def solve(a, b, x, y):
    # a,a + b   -> a,b就是取最大公约数的过程,而且该过程可逆
    # 所以只需要gcd(a,b) == gcd(x,y)
    # 就可以从a,b移动到x,y
    if gcd(a,b) == gcd(x,y):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abxy = input().split()

        a = int(abxy[0])

        b = int(abxy[1])

        x = int(abxy[2])

        y = int(abxy[3])

        result = solve(a, b, x, y)

        fptr.write(result + '\n')

    fptr.close()
