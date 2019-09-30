#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the steadyGene function below.
from collections import Counter
def steadyGene(gene):
    n = len(gene) // 4  # 每个字符需要且只需要n个
    init = Counter(gene)    # 统计每个字符的数量
    need = Counter()
    dic = 'ACGT'
    for c in dic:   # 多余的数量是需要被替换的
        if init[c] > n:
            need[c] = init[c] - n
    print('need:',need)
    if not need:    # 如果不需要被替换
        return 0
    cnt = Counter()
    ans = n * 4 # 最大可能被替换量
    l = 0
    r = 0
    while l < n * 4 and r < n * 4:
        while l < n * 4 and gene[l] not in need:    #因为要找最短的字符串,字符串的起始位置一定是一个需要被替换的字符
            cnt[gene[l]] -= 1
            l += 1
        #print('move left:',l,r,gene[l:r + 1],cnt)
        if r < l:
            r = l
            cnt = Counter()
            #print('check left right:',l,r,gene[l:r + 1],cnt)
        while r < n * 4 and len(+(need - cnt)) > 0: #查找满足替换需求的结束位置
            c = gene[r]
            cnt[c] += 1
            #print('move right:',l,r,gene[l:r + 1],cnt)
            r += 1
        if len(+(need - cnt)) <= 0: #如果是找到了满足条件的结束位置
            #print('ans:',l,r - 1,gene[l:r],cnt)
            ans = min(ans,r - l)
        else:   #结束位置到了字符串的末尾
            break
        cnt[gene[l]] -= 1   #尝试后移起始位置
        l += 1
    return ans  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
