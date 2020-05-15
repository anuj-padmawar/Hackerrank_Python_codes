import numpy


polynomial=[float(x) for x in input().split()]
x=float(input())
print(numpy.polyval(polynomial, x))



