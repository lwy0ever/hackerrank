# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
arr = list(map(int,input().split()))
s = set(arr)
print((sum(s) * k - sum(arr)) // (k - 1))
