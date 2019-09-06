# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int,input().split()))
n = int(input())
#print(a)
r = True
for _ in range(n):
    t = set(map(int,input().split()))
    r = (a & t == t and len(a) > len(t)) and r
    if not r:
        break
print(r)
