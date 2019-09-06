# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    d = list(map(int,input().split()))
    #print(d.index(min(d)))
    #print(d[:3])
    l = d[:d.index(min(d))].copy()
    r = d[d.index(min(d)):].copy()
    #print(l,r)
    if len(l) + len(r) == len(d) and sorted(l,reverse = True) == l and sorted(r) == r:
        print('Yes')
    else:
        print('No')
'''
    for _ in range(n):
        if d[len(d) - 1] == max(d) or d[0] == max(d):
            d.remove(max(d))
        else:
            print('No')
            break
    else:
        print('Yes')
'''
