# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s,size = input().split(' ')
for x in list(permutations(sorted(s),int(size))):
    print(''.join(list(x)))
