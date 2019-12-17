#!/bin/python3

import os
import sys

#
# Complete the summingPieces function below.
#
def summingPieces(arr):
    #
    # Write your code here.
    #
    # 参考 https://blog.csdn.net/charlie_jilei/article/details/77688738
    # 对于某个包含arr[p]的序列,其左侧有l个元素,右侧有r个元素
    # 左侧l个元素的组合形式有2 ** (l - 1)种(特别的,l = 0时,有1种)
    # 右侧r个元素的组合形式有2 ** (r - 1)种(特别的,r = 0时,有1种)
    # 则arr[p]对于最终结果的贡献为(2 ** (l - 1)) * (2 ** (r - 1)) * (n - l - r) * arr[p]
    # 拆分上述公式(公式x):
    # = (2 ** (l - 1)) * (2 ** (r - 1)) * arr[p] * n
    #   - (2 ** (l - 1)) * (2 ** (r - 1)) * arr[p] * l
    #   - (2 ** (l - 1)) * (2 ** (r - 1)) * arr[p] * r
    # 最终结果为∑(l=0:p-1)∑(r=0:n-p)公式x
    m = 10 ** 9 + 7
    n = len(arr)
    g = [1] * (n + 1) # 预计算2 ** (i - 1),g[i] = 2 ** (i - 1),其中g[0] = 1
    gi = [1] * (n + 1)    # 预计算2 ** (i - 1) * i,gi[i] = 2 ** (i - 1) * i,其中gi[0] = 1
    for i in range(2,n + 1):
        g[i] = (g[i - 1] * 2) % m
        gi[i] = (g[i] * i) % m
    sumA = [1] * (n + 1)  # 预计算∑(i=0:p):2 ** (i - 1)
    sumB = [0] * (n + 1)  # 预计算∑(i=0:p):2 ** (i - 1) * i
    for i in range(1,n + 1):
        sumA[i] = (sumA[i - 1] + g[i]) % m
        sumB[i] = (sumB[i - 1] + gi[i]) % m
    #print(g,gi,sumA,sumB)
    ans = 0
    for i in range(1,n + 1):
        ans += (sumA[i - 1] * sumA[n - i] * n - sumB[i - 1] * sumA[n - i] - sumB[n - i] * sumA[i - 1]) * arr[i - 1] % m
    return ans % m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
