# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
sn = set(input().split())
b = int(input())
sb = set(input().split())
print(len(sn & sb))
