#!/bin/python3

import re

nm = input().split()
n = int(nm[0])
m = int(nm[1])
matrix = []
i = 0
while i < n:
#for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    i += 1
s = ''
'''
for i in range(m):
    for j in range(n):
        s += matrix[j][i]
'''
for z in zip(*matrix):
    s += ''.join(z)
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', s))
#print(re.sub(r'(\w)([ ]*?[!@#$%&]+?[ ]*?)(\w)',r'\1 \3',s))
