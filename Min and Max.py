import numpy
N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
my_array = numpy.array(arr)
#print(my_array)
print(max(numpy.min(my_array,axis = 1)))


