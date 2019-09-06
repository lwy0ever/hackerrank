# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
od = OrderedDict()
for _ in range(N):
    #print(od)
    line = input().split()
    k = ' '.join(line[:-1])
    v = int(line[-1])
    if k in od:
        od[k] += v
    else:
        od[k] = v
#print(od.items())
for k,v in od.items():
    print(k,v)
