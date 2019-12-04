#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(y):
    y.sort()
    n = len(y)
    ans = 0
    pre = 0
    #lessThanNum = 0 # 表示已经出现过的,比y[i]小的数量(由于存在y[i - 1] = y[i]的情况)
    for i in range(n):
        # 如果pre == y[i],则小于y[i]的元素数没有增加
        # 如果pre != y[i],则小于y[i]的元素数有i个,大于or等于y[i]的元素数(含y[i]自身)有n - i个
        # ansi表示y[i]产生的v的平均值:
        if y[i] != pre:
            pre = y[i]
            # Imagine a different problem:
            # if you had to place k sticks of equal heights in n slots
            # then the expected distance between sticks
            # (and the expected distance between the first stick and a notional slot 0,
            # and the expected distance between the last stick and a notional slot n+1)
            # is (n+1) / (k+1) since there are k+1 gaps to fit in a length n+1.
            # 考虑一个问题:
            # 有k个等高的stick,摆放在n个slot处
            # stick之间的平均距离(包括:slot[0]到第一个stick,最后一个stick到slot[n])=(n + 1) / (k + 1)
            
            # Returning to this problem,
            # a particular stick is interested in how many sticks (including itself) are as high or higher.
            # If this number is k, then the expected gap to its left is also (n+1)/(k+1).
            # 回到这个问题:
            # 有k个高于或等于当前点的stick
            # 那么每个stick到它左侧stick的平均距离是(n + 1) / (k + 1)
            ansi = (n + 1) / (n - i + 1)
        ans += ansi
    #print(round(ans,2))
    return '{:.2f}'.format(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        y_count = int(input())

        y = list(map(int, input().rstrip().split()))

        result = solve(y)

        #fptr.write('\n'.join(map(str, result)))
        fptr.write(str(result))
        fptr.write('\n')

    fptr.close()
