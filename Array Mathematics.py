import numpy
n,m = list(map(int,input().split()))
a,b = [],[]
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))
A = numpy.array(a)
B = numpy.array(b)
#print(A)
#print(B)
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

