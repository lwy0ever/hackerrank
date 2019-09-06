# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())
css = ''
for _ in range(N):
    css += input() + '\n'
#print(css)
for r in re.findall(r'[:, ](?:.*?|[ ]*)(#(?:[\da-fA-F]{3}){1,2})[ ]*[),;]',css):
    print(r)
