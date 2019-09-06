import numpy
'''
s = ','.join(list(map(str,input().split())))
eval('print(numpy.zeros((%s), dtype = numpy.int))' % (s))
eval('print(numpy.ones((%s), dtype = numpy.int))' % (s))
'''
nums = tuple(map(int,input().split()))
print(numpy.zeros(nums, dtype = numpy.int))
print(numpy.ones(nums, dtype = numpy.int))

