#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.
def sumChild(c,node,edge,ind):
    if len(edge[ind]) == 0:
        node[ind] = c[ind]
        return c[ind]
    node[ind] = sum([sumChild(c,node,edge,i) for i in edge[ind]]) + c[ind]
    return node[ind]

def balancedForest(c, edges):
    n = len(c)
    #print(n)
    crossEdge = {i:set() for i in range(n)}
    for (a,b) in edges:
        crossEdge[a - 1].add(b - 1)
        crossEdge[b - 1].add(a - 1)
    edge = {i:[] for i in range(n)}
    rEdge = {}
    fathers = [0]
    while fathers:
        father = fathers.pop()
        #print(crossEdge)
        #print(fathers,father,crossEdge[father])
        for child in crossEdge[father]:
            edge[father].append(child)
            rEdge[child] = father
            crossEdge[child].remove(father)
            #print(crossEdge)
            fathers.append(child)
        del crossEdge[father]
        #print(crossEdge)
    #print('edge:',edge)
    #print('rEdge:',rEdge)
    node = [0] * n
    #sumChild(c,node,edge,0)
    stack = [(0,True)]
    while stack:
        nodeId,needMore = stack.pop()
        if needMore:
            stack.append((nodeId,False))
            for child in edge[nodeId]:
                stack.append((child,True))
        else:
            node[nodeId] = sum([node[i] for i in edge[nodeId]]) + c[nodeId]
    #print('node:',node)
    rNode = {}
    for i in range(n):
        if node[i] in rNode:
            rNode[node[i]].append(i)
        else:
            rNode[node[i]] = [i]
    #print('rNode:',rNode)

    ans = float('inf')
    n0 = node[0]
    for k in rNode.keys():
        #1 splite to: p1 = k, p2 = k
        if k * 3 - n0 >= 0:
            if len(rNode[k]) > 1:
                print('#1',k)
                ans = min(ans,k * 3 - n0)
            for p1 in rNode[k]:
                #2 splite to: p1 = k, p2 = k * 2, p2 is p1's father
                father = p1
                p1fathers = {father}
                while father > 0:
                    father = rEdge[father]
                    p1fathers.add(father)
                if k * 2 in rNode:
                    for p2 in rNode[k * 2]:
                        if p2 in p1fathers:
                            print('#2',k)
                            ans = min(ans,k * 3 - n0)
                #3 splite to: p1 = k, p2 = n0 - k, p2 is p1's father
                if n0 - k in rNode:
                    for p2 in rNode[n0 - k]:
                        if p2 in p1fathers:
                            print('#3',k)
                            ans = min(ans,k * 3 - n0)
                #4 splite to: p1 = k, p2 = n0 - k * 2, p2 is not p1's father, and p1 is not p2's father
                if n0 - k * 2 in rNode:
                    for p2 in rNode[n0 - k * 2]:
                        father = p2
                        p2fathers = {father}
                        while father > 0:
                            father = rEdge[father]
                            p2fathers.add(father)
                        if p2 not in p1fathers and p1 not in p2fathers:
                            print('#4',k)
                            ans = min(ans,k * 3 - n0)
        if n0 - k * 3 >= 0:
            for p1 in rNode[k]:
                father = p1
                p1fathers = {father}
                while father > 0:
                    father = rEdge[father]
                    p1fathers.add(father)
                #5 splite: p1 = k, p2 = (n0 - k) / 2,p2 is not p1's father, and p1 is not p2's father
                if (n0 - k) % 2 == 0 and (n0 - k) // 2 in rNode:
                    for p2 in rNode[(n0 - k) // 2]:
                        father = p2
                        p2fathers = {father}
                        while father > 0:
                            father = rEdge[father]
                            p2fathers.add(father)
                        if p2 not in p1fathers and p1 not in p2fathers:
                            print('#5',k)
                            ans = min(ans,(n0 - k * 3) // 2)
                #6 splite: p1 = k, p2 = (n0 + k) / 2,p2 is p1's father
                if (n0 + k) % 2 == 0 and (n0 + k) // 2 in rNode:
                    for p2 in rNode[(n0 + k) // 2]:
                        if p2 in p1fathers:
                            print('#6',k)
                            ans = min(ans,(n0 - k * 3) // 2)
    return -1 if ans == float('inf') else ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
