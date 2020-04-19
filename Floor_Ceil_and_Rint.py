# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(map(float, raw_input().split()))

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


