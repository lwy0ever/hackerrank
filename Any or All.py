# Enter your code here. Read input from STDIN. Print output to STDOUT
n,s = int(input()),input().split()
print(all([int(e) > 0 for e in s]) and any([e==e[::-1] for e in s]))


