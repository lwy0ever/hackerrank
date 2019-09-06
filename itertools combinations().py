# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s,size = input().split(' ')
for i in range(1,int(size) + 1):
    for x in list(combinations(sorted(s),i)):
        print(''.join(x))
