#!/bin/python3

import os
import sys

#
# Complete the downToZero function below.
#
def prepare(N):
    for i in range(1,N + 1):
        nums[i] = min(nums[i],nums[i - 1] + 1)
        j = 2
        while j <= i and i * j <= N:
            nums[i * j] = min(nums[i * j], nums[i] + 1)
            j += 1

def downToZero(n):
    #
    # Write your code here.
    #
    return nums[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    N = 10 ** 6
    nums = [0] + [float('inf')] * N
    prepare(N)

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
