#!/bin/python3

import os
import sys

#
# Complete the hackerrankCity function below.
#
def hackerrankCity(A):
    #
    # Write your code here.
    #
    '''
    First, lets compute some auxiliary quantities. Define M[i] as the number of nodes after the i-th iteration. We then have
    M[0] = 6
    M[i] = 4 M[i-1] + 2
    # m[i]表示经过i次迭代之后节点的数量
    # m[0] = 6
    # m[i] = m[i - 1] * 4 + 2

    Also, define D[i] as the length of the longest path after the i-th iteration, e.g. that between one corner and the other. We then have
    D[0] = 3 A[0]
    D[i] = 3 A[i] + 2 D[i-1]
    # 定义d[i]为i次迭代之后,两个最远点的距离
    # d[0] = A[0] * 3
    # d[i] = A[i] * 3 + d[i - 1] * 2

    Also, define B[i] as the sum of paths ending at the southeast corner (we can pick any corner of course, but to be clear and definitely, let's pick the southeast one). This is slightly tricky to compute, so let's draw a picture:
    W  X
    |  |
    g--h
    |  |
    Y  Z
    Suppose this is the tree after the i-th iteration, so that the edges here have length A[i], while g and h are nodes, and W, X, Y, and Z are all equivalent, e.g. the tree after the (i-1)th iteration. We use different letters for convenience in referring to them.
    # 定义b[i]为到达右下角的所有路径和

    We want to compute B[i], which is the sum of all paths that end at the bottom right, e.g. southeast corner of Z. Let's look at the picture and list all contributions:
    - M[i-1] - 1 paths originating from within Z = B[i-1]
    # 在区域z内部,有m[i - 1] - 1个点出发到达z点,路径和 = b[i - 1]
    - the path starting from node h = A[i] + D[i-1]
    # 从h点出发的路径 = A[i] + d[i - 1]
    - the path starting from g = 2 A[i] + D[i-1]
    # 从g点出发的路径 = A[i] * 2 + d[i - 1]
    - M[i-1] paths starting from within X:
        = B[i-1] + M[i-1] * (2 A[i] + D[i-1])
    # m[i - 1]条路径从x区域出发 = b[i - 1] + m[i - 1] * (A[i] * 2 + d[i - 1])
    - 2 M[i-1] paths starting from within W or Y
        = 2 * (B[i-1] + M[i-1] * (3 A[i] + D[i-1]))
    # m[i - 1]条路径从w和y区域出发 = (b[i - 1] + m[i - 1] * (A[i] * 3 + d[i - 1])) * 2

    Summing all these up, we have
    B[i] = 4 B[i-1] + 3 A[i] + 2 D[i-1] + M[i-1] * (8 A[i] + 3 D[i-1])
    # 综上,b[i] = b[i - 1] * 4 + A[i] * 3 + d[i - 1] * 2 + m[i - 1] * (A[i] * 8 + d[i - 1] * 3)

    # 从这儿往后没看懂呢……
    Finally, let's compute the value of C[i], e.g. the sum of all the pairwise paths after the i-th iteration. For convenience, let's repeat the same picture again:
    W  X
    |  |
    g--h
    |  |
    Y  Z


    - 1 path from g to h = A[i]
    - paths within W, within Y, within X, or within Z = 4 C[i-1]
    - paths from g to W, g to Y, h to X, or h to Z:
        = 4 (B[i-1] + A[i] * M[i-1])
    - paths from g to X, g to Z, h to W, or h to Y:
        = 4 (B[i-1] + 2 A[i] * M[i-1])
    - 2 paths from W to Y or X to Z:
        = 4 M[i-1] B[i-1] + 4 A[i] M[i-1]^2
    - 4 paths from W to Z or W to X or Y to Z or Y to X
        = 8 M[i-1] B[i-1] + 12 A[i] M[i-1]^2

    The last two are non obvious and merit explanation: let
    B[i-1] = sum p_k where p_k is the length of a path ending at a corner. A path from W to Y, where path k is chosen in W and path k' is chosen in Y, has distance
        = p_k + p_k' + 2 A[i-1]

    Take this quantity and perform a double sum over k and k'. The sum of p_k is given by M[i-1] B[i-1], and the sum of A[i-1] is given by M[i-1]^2 A[i-1].

    Hence, taking every item above and summing, we end up with

    C[i] = A[i] + 4 C[i-1] + 8 B[i-1] + 12 A[i] M[i-1] + 12 M[i-1] B[i-1] + 16 A[i] M[i-1]^2

    To obtain C[0], we note that C[-1] = 0, B[-1] = 0, and M[-1] = 1, so we have
    C[0] = 29 A[0]
    '''
    md = 10 ** 9 + 7
    b = 0
    c = 0
    d = 0
    m = 1
    for a in A:
        bp = b
        cp = c
        dp = d
        mp = m
        m = (mp * 4 + 2) % md
        d = (dp * 2 + a * 3) % md
        b = mp * (dp * 3 + a * 8) % md
        bterm = [bp * 4,a * 3,dp * 2]
        for term in bterm:
            b += term
        b %= md
        c = (mp * 12) * (a + bp) % md
        cterm = [a,cp * 4,bp * 8,mp * mp * a * 16 % md]
        for term in cterm:
            c += term
        c %= md
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input())

    A = list(map(int, input().rstrip().split()))

    result = hackerrankCity(A)

    fptr.write(str(result) + '\n')

    fptr.close()
