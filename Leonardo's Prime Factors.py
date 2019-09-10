#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    #
    # Write your code here.
    #
    def isPrime(p):
        for x in prime[1:]:
            if p % x == 0:
                return False
        return True

    l = len(prime)
    i = 0
    s = 1
    while s <= n:
        if i == l:
            p = prime[i - 1] + 2
            while not isPrime(p):
                p += 2
                #print(p)
            prime.append(p)
            l += 1
        #print(n,prime,i)
        s *= prime[i]
        i += 1
    return i - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    prime = [2,3,5,7]

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
