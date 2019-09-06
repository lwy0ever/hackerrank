# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for _ in range(N):
    s = input()
    if re.search(r'^[7-9][0-9]{9}$',s):
        print('YES')
    else:
        print('NO')
