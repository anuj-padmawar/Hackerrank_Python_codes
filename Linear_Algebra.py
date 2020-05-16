import numpy
numpy.set_printoptions(legacy='1.13')

N=int(input())
A= numpy.array([input().split() for _ in range(N)],float)


print(numpy.linalg.det(A))




