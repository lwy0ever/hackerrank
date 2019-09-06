# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K,M = map(int,input().split(' '))
s = 0
m = 0
l = []
N = list(list(map(int, input().split()))[1:] for _ in range(K))
#print(N)
#print(N)
#print(list(product(*N)))
results = map(lambda x: sum(i**2 for i in x) % M, product(*N))
print(max(results))

