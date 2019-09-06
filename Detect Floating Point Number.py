# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    print(True if re.match(r'^[+-]?\d*\.\d+$',input()) else False)
