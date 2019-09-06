import numpy
n,m,p = map(int,input().split())
np,mp = [],[]
for _ in range(n):
    np.append(list(map(int,input().split())))
for _ in range(m):
    mp.append(list(map(int,input().split())))
print(numpy.concatenate((np,mp),axis = 0))
