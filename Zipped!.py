# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
x,n = map(int,sys.stdin.readline().strip().split())
s = []
for _ in range(n):
    s += [list(map(float,sys.stdin.readline().strip().split()))]
#print(list(zip(*s)))
for l in list(zip(*s)):
    print(sum(l) / len(l))

