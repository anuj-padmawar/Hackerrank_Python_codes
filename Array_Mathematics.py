import numpy

x = []
y = []

n, m = map(int, raw_input().split())
for i in range(n):
    x.append(raw_input().split())
for i in range(n):
    y.append(raw_input().split())

a = numpy.array(x, int)
b = numpy.array(y, int)

print numpy.add(a, b)
print numpy.subtract(a, b)
print numpy.multiply(a, b)
print numpy.divide(a, b)
print numpy.mod(a, b)
print numpy.power(a, b)
