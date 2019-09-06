# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
c = '.|.'
s = 'WELCOME'
for i in range(0,n // 2):
    print((c * (i * 2 + 1)).center(m,'-'))
print(s.center(m,'-'))
for i in range(n // 2,0,-1):
    print((c * (i * 2 - 1)).center(m,'-'))
