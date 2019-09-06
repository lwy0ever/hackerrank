# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    line = input().split()
    if len(line) > 1:
        eval('d.%s(%s)' % (line[0],line[1]))
    else:
        eval('d.%s()' % (line[0]))
print(' '.join(map(str,list(d))))
