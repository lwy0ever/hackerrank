n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c = input().split() + ['']
    eval('s.%s(%s)' % (c[0],c[1]))
print(sum(s))
