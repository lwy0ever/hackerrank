#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryChildren function below.
def angryChildren(k, packets):
    packets.sort()
    n = len(packets)
    dis = 0
    s = packets[0] # s用于计算连续k个packets的和
    for i in range(1,k):
        dis += packets[i] * i - s
        s += packets[i]
    ans = dis
    # dis[i]表示packets[i:i + k]的difference
    # dis[i] = dis[i - 1] + ((k - 1) * packets[i + k - 1]  - (s - packets[i - 1])) - ((s - packets[i - 1]) - (k - 1) * packets[i - 1])
    for i in range(1,n - k + 1):
        dis = dis + ((k - 1) * packets[i + k - 1] - (s - packets[i - 1])) - ((s - packets[i - 1]) - (k - 1) * packets[i - 1])
        s = s - packets[i - 1] + packets[i + k - 1]
        ans = min(ans,dis)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    packets = []

    for _ in range(n):
        packets_item = int(input())
        packets.append(packets_item)

    result = angryChildren(k, packets)

    fptr.write(str(result) + '\n')

    fptr.close()
