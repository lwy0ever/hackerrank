# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
A = defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    w = input()
    A[w].append(i + 1)
for _ in range(m):
    w = input()
    if len(A[w]) == 0:
        print(-1)
    else:
        print(' '.join(map(str,A[w])))
