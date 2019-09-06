import numpy
numpy.set_printoptions(legacy='1.13')
N = int(input())
A = []
for _ in range(N):
    A.append([float(e) for e in input().split(' ')])
#print(A)
print(numpy.linalg.det(A))
