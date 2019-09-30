#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s):
    # This function is called once before all queries.
    base = ord('a')
    for i,c in enumerate(s,1):
        k = ord(c) - base
        for j in range(baseLen):
            cnt[i][j] = cnt[i - 1][j] + (j == k)
    #print(cnt)

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    center = 0   #单数字符,可以放在中间的数量
    side = 0   #放在两侧的数量
    d = 1
    for i in range(baseLen):
        num = cnt[r][i] - cnt[l - 1][i]
        center += num % 2
        side += num // 2
        d *= I[num // 2]              #这块没太看懂,"denominators"
    return (center or 1) * F[side] * d % mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    #基础参数
    baseLen = 26
    mod = 1000000007
    n = len(s)
    cnt = [[0] * baseLen for _ in range(n + 1)] #cnt[i]表示s[:i + 1]中各个字符的数量
    F = [1] * n
    I = [1] * n
    for i in range(1, n):               #这块没太看懂
        F[i] = F[i - 1] * i % mod     # modular factorial
        I[i] = pow(F[i], mod - 2, mod)  # modular inverse of factorial
    print(F,I)
    #基础参数结束
    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
