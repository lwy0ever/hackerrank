# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
mi = set(map(int,input().split()))
N = int(input())
ni = set(map(int,input().split()))

#r = mi.union(ni).difference(mi.intersection(ni))
#for x in sorted(r):
#    print(x)

mi.symmetric_difference_update(ni)
for x in sorted(mi):
    print(x)
