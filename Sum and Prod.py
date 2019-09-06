import numpy
N,M = map(int,input().split(' '))
arr = []
for _ in range(N):
    arr.append([int(e) for e in input().split(' ')])
print(numpy.prod(numpy.sum(arr,axis = 0)))
