#!/bin/python3

import os
import sys

# Complete the substringDiff function below.
def substringDiff(k, s1, s2):
    from collections import deque
    ans = 0
    n = len(s1)
    # s1和s2错位比较
    for offset in range(n): # offset是错位量
        for _ in range(min(offset + 1,2)):  # offset为0时,只需要比较一次,offset大于1时,需要交换s1和s2一次
            dq = deque()    # dq存放s1和s2相等的位置
            for i in range(n - offset):
                if s1[i] == s2[i + offset]:
                    dq.append(i)
                    # 计算不同位置的数量,如果大于k,则移除最左侧的位置
                    while i - dq[0] + 1 - len(dq) > k:
                        dq.popleft()
                    score = min(len(dq) + k,n - offset) # 可能获得的最大长度,同时不能超过n - offset
                    ans = max(ans,score)
            s1,s2 = s2,s1   # 由于offset是相对的,要交换比较一次
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        kS1S2 = input().split()

        k = int(kS1S2[0])

        s1 = kS1S2[1]

        s2 = kS1S2[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
