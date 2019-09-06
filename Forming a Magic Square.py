#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def cost(t,s):
    res = 0
    for i in range(3):
        for j in range(3):
            res += abs(t[i][j] - s[i][j])
    return res

def formingMagicSquare(s):
    ans = float('inf')
    small = [1,2,3,4]
    big = [9,8,7,6]
    pos = [(i,j) for i in range(3) for j in range(3)]
    pos.remove((1,1))
    #print(pos)
    test = [[5] * 3 for _ in range(3)]
    for p1 in pos:
        for p2 in pos:
            if p2 == p1 or (p1[0] + p2[0] == 2 and p1[1] + p2[1] == 2):
                continue
            for p3 in pos:
                if p3 in(p1,p2) or (p1[0] + p3[0] == 2 and p1[1] + p3[1] == 2) or (p3[0] + p2[0] == 2 and p3[1] + p2[1] == 2):
                    continue
                for p4 in pos:
                    if p4 in(p1,p2,p3) or (p1[0] + p4[0] == 2 and p1[1] + p4[1] == 2) or (p4[0] + p2[0] == 2 and p4[1] + p2[1] == 2) or (p3[0] + p4[0] == 2 and p3[1] + p4[1] == 2):
                        continue
                    test[p1[0]][p1[1]] = small[0]
                    test[2 - p1[0]][2 - p1[1]] = big[0]
                    test[p2[0]][p2[1]] = small[1]
                    test[2 - p2[0]][2 - p2[1]] = big[1]
                    test[p3[0]][p3[1]] = small[2]
                    test[2 - p3[0]][2 - p3[1]] = big[2]
                    test[p4[0]][p4[1]] = small[3]
                    test[2 - p4[0]][2 - p4[1]] = big[3]
                    #print('test:')
                    #for t in test:
                    #    print(t)
                    if sum(test[0]) == 15 and sum(test[2]) == 15 and sum([test[i][0] for i in range(3)]) == 15 and sum([test[i][2] for i in range(3)]) == 15:
                        ans = min(ans,cost(test,s))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
