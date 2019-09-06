#!/bin/python3

import os
import sys

#
# Complete the waiter function below.
#
def getPrime(p):
    t = p[-1]
    while True:
        t += 2
        for i in range(3,int(t ** 0.5) + 1):
            if t % i == 0:
                break
        else:
            p.append(t)
            return

def waiter(number, q):
    #
    # Write your code here.
    #
    ans = []
    prime = [2,3]
    for i in range(q):
        if len(prime) <= i:
            getPrime(prime)
        p = prime[i]
        #print(prime)

        length = len(number)
        i = 0
        while i < length:
            if number[i] % p == 0:
                #print(number[i])
                ans.append(number[i])
                number.pop(i)
                length -= 1
                continue
            i += 1
        number.reverse()
    number.reverse()
    if number:
        ans += number
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
