# Enter your code here. Read input from STDIN. Print output to STDOUT
l1 = int(input())
l2 = set(map(int,input().split()))
l3 = int(input())
l4 = set(map(int,input().split()))
#print(len(l2 ^ l4))
print(len(l2.symmetric_difference(l4)))
