#!/bin/python3

import os
import sys

#
# Complete the legoBlocks function below.
#
def power(x,y):
    # 快速power
    ans = 1
    base = x
    while y:
        if y & 1:
            ans *= base
            ans %= mod
        base *= base
        base %= mod
        y //= 2
    return ans

def legoBlocks(n, m):
    #
    # Write your code here.
    #
    # 考虑单层的情况:
    # row[i]表示宽度为i的一层,摆放的方案数
    # row[0] = 0,row[1] = 1,row[2] = 2,row[3] = 4,row[i] = row[i - 1] + row[i - 2] + row[i - 3] + row[i - 4]
    # 考虑多层的情况:
    # allplan[i]表示宽度为i,n层的情况下的方案数(含通天缝方案),allplan[i] = row[i] ** n
    # 反向思考:所有的方案-出现垂直通天缝的方案
    # plan[i]表示宽度为i,n层的情况下的方案数(不含通天缝方案)
    # 第一个垂直通天缝出现在位置j的方案plan[j] * allplan[i - j],这里需要用plan[j]而不是allplan[j],是为了保证这个通天缝是第一个出现的
    allplan = [0] * (m + 1)
    for i in range(1,m + 1):
        allplan[i] = power(row[i],n)
    plan = [1] * (m + 1)
    for i in range(2,m + 1):
        plan[i] = allplan[i]
        for j in range(1,i):
            plan[i] -= plan[j] * allplan[i - j]
            plan[i] %= mod # + mod是为了防止在上一步,出现plan[i]为负数的情况,因为 -5 % 3 = 1
    return plan[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    mod = 10 ** 9 + 7

    row = [1] * 1001
    row[1] = 1
    row[2] = 2
    row[3] = 4
    for i in range(4,1001):
        row[i] = row[i - 1] + row[i - 2] + row[i - 3] + row[i - 4]

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
