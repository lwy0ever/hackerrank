#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
    def doCheck(G,P,i,j):
        #print(i,j)
        for l,s in enumerate(P):
            #print(G[i + l][j:j + len(s)],s)
            if G[i + l][j:j + len(s)] != s:
                return False
        return True

    rG = len(G)
    cG = len(G[0])
    rP = len(P)
    cP = len(P[0])
    for i in range(rG - rP + 1):
        j = 0
        while j < cG - cP + 1:
            pos = G[i].find(P[0],j)
            #print(i,j,pos)
            if pos >= 0:
                if doCheck(G,P,i,pos):
                    return 'YES'
                j = pos + 1
            else:
                break
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
