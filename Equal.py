#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):
    # 最终目标是希望arr的各个元素差值为0
    # 给n - 1个元素增加1,2,5，等价于给1个元素减少1,2,5
    # 存在一种情况:
    # 1,5,5->0,5,5->0,0,5->0,0,0---->共3步
    # 1,5,5->1,3,5->1,1,5->1,1,3->1,1,1---->共4步
    # 所以目标:所有元素减小到最小值min，或者min-1,或者min-2,或者min-3,或者min-4
    ans = float('inf')
    mi = min(arr)
    for i in range(mi - 4,mi + 1):
        t = 0
        for a in arr:
            s = (a - i)
            d,s = divmod(s,5)
            t += d
            d,s = divmod(s,2)
            t += d
            t += s
        ans = min(ans,t)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
