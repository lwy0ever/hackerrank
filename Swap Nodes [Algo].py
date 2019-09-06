#!/bin/python3

import os
import sys

sys.setrecursionlimit(2000)
#
# Complete the swapNodes function below.
#
class Node:
    def __init__(self,value,depth):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None
    def display(self):
        r = []
        if self.left:
            r += self.left.display()
        r.append(self.value)
        if self.right:
            r += self.right.display()
        return r
    def swap(self,k):
        if self.depth % k == 0:
            self.left,self.right = self.right,self.left
        if self.left:
            self.left.swap(k)
        if self.right:
            self.right.swap(k)

def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    depth = 1
    root = Node(1,depth)
    toadd = [root]
    for l,r in indexes:
        cur = toadd.pop(0)
        if l != -1:
            left = Node(l,cur.depth + 1)
            cur.left = left
            toadd.append(left)
        if r != -1:
            right = Node(r,cur.depth + 1)
            cur.right = right
            toadd.append(right)
    ans = []
    for q in queries:
        root.swap(q)
        ans.append(root.display())
    #print(ans)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
