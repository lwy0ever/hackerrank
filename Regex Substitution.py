# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
s = ''
for _ in range(n):
    s += input() + '\n'
'''
s = re.sub(r'(?<=[ ])(&&)([ ])',r'and\2',s)
s = re.sub(r'(?<=[ ])(\|\|)([ ])',r'or\2',s)
'''
s = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or',s)
print(s)
