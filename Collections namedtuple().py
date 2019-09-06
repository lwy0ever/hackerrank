# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
columns = input().split()
#print(columns)
spreadsheet = namedtuple('spreadsheet',columns)
sss = []
for _ in range(n):
    sss.append(spreadsheet._make(input().split()))
print(sum(int(s.MARKS) for s in sss) / len(sss))
