# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
l = []
#od = OrderedDict()
for _ in range(n):
    l.append(input())
c = Counter(l)
#print(c)
print(len(c))
#for k,v in c.items():
#    print(v)
print(' '.join(map(str,c.values())))
