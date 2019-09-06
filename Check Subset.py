# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    an = input()
    a = set(map(int,input().split()))
    bn = input()
    b = set(map(int,input().split()))
    print(True if (a & b == a) > 0 else False)
