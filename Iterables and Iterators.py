# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
N = int(input())
l = input().split(' ')
K = int(input())
r = list(itertools.combinations(l, K))
c = 0
for x in r:
    if 'a' in x:
        c += 1
print(c/len(r))
