#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ans = []
    l = len(scores)
    lastScore = -1
    cur = 0
    rank = 0
    for a in alice[::-1]:
        if cur < l:
            while cur < l:
                #print(cur,rank,a)
                if scores[cur] != lastScore:
                    rank += 1
                    lastScore = scores[cur]
                if a >= scores[cur]:
                    break
                cur += 1
            else:   # cur >= l
                rank += 1
        ans.append(rank)
    return ans[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
