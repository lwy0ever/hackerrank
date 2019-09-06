#!/bin/python3

import os
import sys

#
# Complete the intervalSelection function below.
#
def intervalSelection(intervals):
    #
    # Write your code here.
    #
    # 按照终点排序
    intervals.sort(key = lambda x:x[1])
    #print(intervals)
    ans = 0
    # placed存放当前最靠后的2个interval,保持按照终点倒序排序的状态
    n = 2
    placed = [[0,0] for _ in range(n)]
    # 逐个放置，从终点最靠后的已放置点开始检查
    # 如果新interval的起点在已放置点的右侧,则替换掉已放置点
    for iv in intervals:
        for i in range(n):
            if iv[0] > placed[i][1]:
                ans += 1
                placed[i] = iv
                placed.sort(key = lambda x:x[1],reverse = True)
                break
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        intervals = []

        for _ in range(n):
            intervals.append(list(map(int, input().rstrip().split())))

        result = intervalSelection(intervals)

        fptr.write(str(result) + '\n')

    fptr.close()
