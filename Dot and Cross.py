import numpy
N = int(input())
arrA = []
arrB = []
for _ in range(N):
    arrA.append(list(map(int,input().split())))
for _ in range(N):
    arrB.append(list(map(int,input().split())))
A = numpy.array(arrA)
B = numpy.array(arrB)
print(numpy.dot(A,B))
#print(numpy.cross(A,B))
