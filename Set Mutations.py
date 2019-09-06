# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
A = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    o,_ = input().split()
    B = set(map(int,input().split()))
    #eval('A.%s(B)' % (o))
    getattr(A,o)(B)
print(sum(x for x in A))
