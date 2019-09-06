import numpy
numpy.set_printoptions(legacy='1.13')

N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
my_arr = numpy.array(arr)
print(numpy.mean(my_arr,axis = 1))
print(numpy.var(my_arr,axis = 0))
print(numpy.std(my_arr,axis = None))

