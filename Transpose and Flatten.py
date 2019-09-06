import numpy
n,m = map(int,input().split())
#print(n,m)
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
    #print(arr)
x = numpy.array(arr)
print(numpy.transpose(x))
print(x.flatten())
