import numpy
arr = [int(e) for e in input().split(' ')]
n_arr = numpy.array(arr)
n_arr.shape = (3,3)
print(n_arr)


