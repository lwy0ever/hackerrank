#!/bin/python3

import os
import sys

#
# Complete the sillyGame function below.
#
def sillyGame(n):
    #
    # Write your code here.
    #
    if n == 1:
        return 'Bob'
    if n == 2:
        return 'Alice'
    # 统计小于等于n的prime number数量,不包括2
    if n >= primes[-1]:
        for i in range(primes[-1] + 2,n + 1,2):
            for p in primes:
                if i % p == 0:
                    break
                if p * p > n:
                    primes.append(i)
                    break
            else:
                primes.append(i)
    #print(primes)
    num = 0
    for p in primes:
        if p <= n:
            num += 1
        else:
            break
    return 'Alice' if num & 1 == 0 else 'Bob'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    # 全局设置,避免重复计算
    primes = [3]    # 初始化一个3,避免primes[-1]出错
    for g_itr in range(g):
        n = int(input())

        result = sillyGame(n)

        fptr.write(result + '\n')

    fptr.close()
