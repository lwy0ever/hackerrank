#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
# https://www.hackerearth.com/zh/practice/notes/disjoint-set-union-union-find/
def get_parent(parent,x):
    while parent[x] != x:
        x = parent[x]
    return x

def maxCircle(queries):
    ans = []
    ma = 0
    parentGroup = {}
    friendNum = {}  # inclue itself
    for a,b in queries:
        if a not in parentGroup:
            parentGroup[a] = a
            friendNum[a] = 1    #exclude itself
        if b not in parentGroup:
            parentGroup[b] = b
            friendNum[b] = 1    #exclude itself
        pa = get_parent(parentGroup,a)
        pb = get_parent(parentGroup,b)
        if pa != pb:
            if friendNum[pa] > friendNum[pb]:
                parentGroup[pb] = pa
                friendNum[pa] = friendNum[pa] + friendNum[pb]   # itself included
                ma = max(ma,friendNum[pa])
            else:
                parentGroup[pa] = pb
                friendNum[pb] = friendNum[pa] + friendNum[pb]   # itself included
                ma = max(ma,friendNum[pb])
        #print(a,b)
        #print(friendNum)
        ans.append(ma)
    return ans
    '''
    ans = []
    ma = 0
    friendGroup = []
    for a,b in queries:
        af = -1
        bf = -1
        for i in range(len(friendGroup)):
            if a in friendGroup[i]:
                af = i
            if b in friendGroup[i]:
                bf = i
        if af == -1 and bf == -1:
            friendGroup.append({a,b})
            n = 2
        else:
            if af == -1:
                friendGroup[bf].add(a)
                n = len(friendGroup[bf])
            elif bf == -1:
                #print(a,b,friendGroup,af,friendGroup[af])
                friendGroup[af].add(b)
                #print(a,b,friendGroup,af,len(friendGroup[af]))
                n = len(friendGroup[af])
            elif af == bf:
                pass
            else:
                print(af,bf)
                if bf < af:
                    af,bf = bf,af
                friendGroup[af] = friendGroup[af].union(friendGroup[bf])
                del friendGroup[bf]
                n = len(friendGroup[af])
        #print(a,b,friendGroup,n)
        ma = max(ma,n)
        ans.append(ma)
    return ans
    '''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
